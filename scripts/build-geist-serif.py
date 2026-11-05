#!/usr/bin/env python3
"""Build Geist Serif from sources/GeistSerif.glyphspackage on any OS: `make build-serif`.

Writes fonts/GeistSerif/variable, ttf and webfonts. fontmake alone breaks the serifs, because they are Glyphs corner
components, so glyphs_corners.py expands them (and the stroked rings of (c) and (R)) in a temporary copy first.
The ELSH axis only swaps glyphs through rclt, so the variable font carries no outline deltas.

Statics are built from the same copy, one per named instance, with that instance's Rename Glyphs and Replace Feature
applied. Those parameters are Glyphs export features that fontmake does not read.
"""
import argparse, math, os, re, shutil, subprocess, sys, tempfile
from datetime import datetime
from pathlib import Path

import openstep_plist as op
import pathops
from fontTools.otlLib.optimize import compact
from fontTools.pens.areaPen import AreaPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import DecomposingRecordingPen, RecordingPen
from fontTools.pens.reverseContourPen import ReverseContourPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont, newTable
from fontTools.ttLib.removeOverlaps import removeOverlaps
from fontTools.ttLib.tables._g_l_y_f import Glyph, GlyphComponent, ROUND_XY_TO_GRID

sys.path.insert(0, str(Path(__file__).parent))
import glyphs_corners

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "sources" / "GeistSerif.glyphspackage"
FAMILY = "Geist Serif"
PS = "GeistSerif"
VF_WOFF2 = "GeistSerifVF.woff2"


def fontmake(package, fmt, out, *extra):
    subprocess.run([sys.executable, "-m", "fontmake", "-g", str(package), "-o", fmt, "--output-dir", str(out),
                    "--verbose", "ERROR", *extra], check=True)
    return next(Path(out).glob("*.ttf"))


def glyph_files(package):
    for path in sorted((package / "glyphs").glob("*.glyph")):
        with open(path) as f:
            yield path, op.load(f, use_numbers=True)


def strip_variable_code(code):
    """Glyphs drops #ifdef VARIABLE blocks from statics; feaLib reads them as comments and would keep their rules"""
    return re.sub(r"#ifdef VARIABLE\n.*?#endif\n?", "", code, flags=re.S)


def static_source(expanded, instance, dst):
    """a copy of the expanded source as this instance would export: renames applied, features replaced"""
    shutil.copytree(expanded, dst)
    with open(dst / "fontinfo.plist") as f:
        info = op.load(f, use_numbers=True)
    params = {p["name"]: p["value"] for p in instance.get("customParameters", [])}
    for feature in info.get("features", []):
        feature["code"] = strip_variable_code(feature.get("code", ""))
    if "Replace Feature" in params:
        tag, code = params["Replace Feature"].split(";", 1)
        feature = next(x for x in info["features"] if x.get("tag") == tag.strip())
        feature["code"] = code.strip() + "\n"
    with open(dst / "fontinfo.plist", "w") as f:
        op.dump(info, f)
    swaps = dict(r.split("=") for r in params.get("Rename Glyphs", []))
    swaps.update({b: a for a, b in list(swaps.items())})
    if swaps:
        # The two glyphs trade names and keep everything else: drawing, kern groups, kerning. Their own components
        # follow them. Any other glyph refers by name, so ellipsis picks up the new period.
        glyphs = {g["glyphname"]: (path, g) for path, g in glyph_files(dst)}
        for a, b in swaps.items():
            if a < b:
                ga, gb = glyphs[a][1], glyphs[b][1]
                for key in ("layers", "kernLeft", "kernRight"):
                    va, vb = ga.pop(key, None), gb.pop(key, None)
                    if vb is not None: ga[key] = vb
                    if va is not None: gb[key] = va
        for name in swaps:
            path, g = glyphs[name]
            for layer in g["layers"]:
                for shape in layer.get("shapes", []):
                    if shape.get("ref") in swaps: shape["ref"] = swaps[shape["ref"]]
            with open(path, "w") as f:
                op.dump(g, f)
        info["kerningLTR"] = {master: {swaps.get(a, a): {swaps.get(b, b): v for b, v in right.items()} for a, right in pairs.items()}
                              for master, pairs in info.get("kerningLTR", {}).items()}
        with open(dst / "fontinfo.plist", "w") as f:
            op.dump(info, f)
    return dst


def set_name(font, name_id, value):
    for rec in font["name"].names:
        if rec.nameID == name_id: rec.string = value
    if not any(r.nameID == name_id for r in font["name"].names):
        font["name"].setName(value, name_id, 3, 1, 0x409)


def tidy(font):
    """Scaled or rotated components become outlines (c is a turned o), so they get hinted; glyphs built on them stay
    composites. Nested composites flatten to one level of plain offsets. Kerning is packed."""
    glyf = font["glyf"]; glyph_set = font.getGlyphSet(); order = font.getGlyphOrder()
    transformed = [n for n in order if glyf[n].isComposite() and any(hasattr(c, "transform") for c in glyf[n].components)]
    outlines = {}
    for name in transformed:
        rec = DecomposingRecordingPen(glyph_set); glyph_set[name].draw(rec)
        pen = TTGlyphPen(None); rec.replay(pen)
        outlines[name] = pen.glyph()
    for name, glyph in outlines.items():
        glyf[name] = glyph

    def leaves(name, x, y):
        if not glyf[name].isComposite():
            return [(name, x, y)]
        return [leaf for c in glyf[name].components for leaf in leaves(c.glyphName, x + c.x, y + c.y)]

    for name in order:
        g = glyf[name]
        if g.isComposite() and any(glyf[c.glyphName].isComposite() for c in g.components):
            parts = []
            for leaf, x, y in leaves(name, 0, 0):
                c = GlyphComponent(); c.glyphName = leaf; c.x = round(x); c.y = round(y); c.flags = ROUND_XY_TO_GRID
                parts.append(c)
            g.components = parts
    compact(font, 9)


def component_parts(font):
    glyf = font["glyf"]
    return {n: [(c.glyphName, c.x, c.y) for c in glyf[n].components] for n in font.getGlyphOrder() if glyf[n].isComposite()}


def tidy_contours(font):
    """Outer contours run clockwise, counters the other way (mirrored components come out reversed), and zero-width
    spikes go (three's 200% corner overshoots its stroke)."""
    glyf = font["glyf"]; glyph_set = font.getGlyphSet()
    for name in font.getGlyphOrder():
        if glyf[name].isComposite() or glyf[name].numberOfContours <= 0: continue
        rec = RecordingPen(); glyph_set[name].draw(rec)
        contours = [[]]
        for op_ in rec.value:
            contours[-1].append(op_)
            if op_[0] in ("closePath", "endPath"): contours.append([])
        contours.pop()
        changed = False
        for contour in contours:
            for i in range(len(contour) - 2, 1, -1):
                a, b = contour[i - 1][1][-1], contour[i][1][-1]
                c = contour[i + 1][1][-1] if contour[i + 1][0] == "lineTo" else contour[0][1][0]
                if contour[i][0] != "lineTo": continue
                u = (b[0] - a[0], b[1] - a[1]); v = (c[0] - b[0], c[1] - b[1])
                if u[0] * v[0] + u[1] * v[1] < 0 and abs(u[0] * v[1] - u[1] * v[0]) <= 0.7 * max(math.hypot(*u), math.hypot(*v)):
                    del contour[i]; changed = True
        def measure(contour, pen):
            for op_, args in contour: getattr(pen, op_)(*args)
            return pen
        areas = [measure(c, AreaPen()).value for c in contours]
        kept = [i for i, area in enumerate(areas) if abs(area) >= 1]      # a contour with no area draws nothing
        changed |= len(kept) != len(contours)
        contours = [contours[i] for i in kept]; areas = [areas[i] for i in kept]
        boxes = [measure(c, BoundsPen(None)).bounds for c in contours]
        pen = TTGlyphPen(None); out = []
        for i, contour in enumerate(contours):
            depth = sum(1 for j, b in enumerate(boxes) if j != i and b[0] <= boxes[i][0] and b[1] <= boxes[i][1] and b[2] >= boxes[i][2] and b[3] >= boxes[i][3] and abs(areas[j]) > abs(areas[i]))
            wrong = areas[i] > 0 if depth % 2 == 0 else areas[i] < 0
            changed |= wrong
            out.append((contour, wrong))
        if not changed: continue
        for contour, wrong in out:
            measure(contour, ReverseContourPen(pen) if wrong else pen)
        glyf[name] = pen.glyph()


def recompose(font, parts):
    """Overlap removal turns a glyph into an outline if any of its parts overlap. Where the overlap is all inside one
    existing glyph, Ohornacute goes back to the Ohorn outline plus acutecomb. Checked: the outline must not change."""
    glyf = font["glyf"]; glyph_set = font.getGlyphSet()
    lost = [n for n in parts if not glyf[n].isComposite()]
    def path_of(draw):
        path = pathops.Path(); draw(path.getPen(glyphSet=glyph_set)); return path
    def placed(name, x, y):
        return path_of(lambda pen: glyph_set[name].draw(TransformPen(pen, (1, 0, 0, 1, x, y))))
    done = 0
    for name in lost:
        best = None
        for base in lost:
            if base == name or glyf[base].isComposite() or len(parts[base]) >= len(parts[name]): continue
            first = parts[base][0]
            for comp, x, y in parts[name]:
                if comp != first[0]: continue
                dx, dy = x - first[1], y - first[2]
                moved = [(c, cx + dx, cy + dy) for c, cx, cy in parts[base]]
                if all(m in parts[name] for m in moved) and (best is None or len(parts[base]) > len(parts[best[0]])):
                    best = (base, dx, dy, [p for p in parts[name] if p not in moved])
        if not best: continue
        base, dx, dy, rest = best
        pieces = [placed(base, dx, dy)] + [placed(c, x, y) for c, x, y in rest]
        whole = pathops.Path()
        for piece in pieces: whole.addPath(piece)
        separate = all(abs(pathops.op(a, b, pathops.PathOp.INTERSECTION).area) < 1 for i, a in enumerate(pieces) for b in pieces[i + 1:])
        same = abs(pathops.op(whole, path_of(lambda pen: glyph_set[name].draw(pen)), pathops.PathOp.XOR).area) < 40
        if not (separate and same): continue
        comps = []
        for c, x, y in [(base, dx, dy)] + rest:
            gc = GlyphComponent(); gc.glyphName = c; gc.x = x; gc.y = y; gc.flags = ROUND_XY_TO_GRID
            comps.append(gc)
        glyf[name] = Glyph(); glyf[name].numberOfContours = -1; glyf[name].components = comps
        done += 1
    print(f"overlaps removed; {done} of {len(lost)} affected glyphs recomposed")


def add_meta(font):
    meta = newTable("meta")
    meta.data = {"dlng": "Latn", "slng": "Latn"}
    font["meta"] = meta


def finish_variable(path, dest):
    font = TTFont(path)
    del font["gvar"]                    # all zero: the axis only swaps glyphs
    tidy(font)
    parts = component_parts(font)
    removeOverlaps(font)                # the corner serifs overlap their stems; fontmake only does this for statics
    tidy_contours(font)
    recompose(font, parts)
    add_meta(font)
    name = font["name"]
    set_name(font, 3, f"{font['head'].fontRevision:.3f};VRCL;{PS}-Regular")
    set_name(font, 4, f"{FAMILY} Regular")
    for nid in (16, 17): name.removeNames(nameID=nid)
    set_name(font, 25, PS)
    for inst in font["fvar"].instances:
        inst.postscriptNameID = name.addMultilingualName({"en": f"{PS}-{name.getDebugName(inst.subfamilyNameID)}"}, ttFont=font, windows=True, mac=False)
    stat = font["STAT"].table           # glyphsLib adds an ital axis the font does not have
    keep = [i for i, a in enumerate(stat.DesignAxisRecord.Axis) if a.AxisTag == "ELSH"]
    dropped = {a.AxisNameID for i, a in enumerate(stat.DesignAxisRecord.Axis) if i not in keep}
    dropped |= {v.ValueNameID for v in stat.AxisValueArray.AxisValue if v.AxisIndex not in keep}
    for nid in dropped: name.removeNames(nameID=nid)
    stat.DesignAxisRecord.Axis = [stat.DesignAxisRecord.Axis[i] for i in keep]
    stat.DesignAxisCount = len(keep)
    stat.AxisValueArray.AxisValue = [v for v in stat.AxisValueArray.AxisValue if v.AxisIndex in keep]
    stat.AxisValueCount = len(stat.AxisValueArray.AxisValue)
    font.save(dest)


def finish_static(path, dest, style):
    font = TTFont(path)
    tidy(font)
    add_meta(font)
    version = f"{font['head'].fontRevision:.3f}"
    if style == "Regular":
        set_name(font, 1, FAMILY); set_name(font, 4, f"{FAMILY} Regular")
    else:
        set_name(font, 1, f"{FAMILY} {style}"); set_name(font, 4, f"{FAMILY} {style}")
    set_name(font, 2, "Regular"); set_name(font, 16, FAMILY); set_name(font, 17, style)
    set_name(font, 3, f"{version};VRCL;{PS}-{style}"); set_name(font, 6, f"{PS}-{style}")
    font.save(dest)


def hint(path):
    import ttfautohint
    tmp = path.with_suffix(".hinted")
    ttfautohint.ttfautohint(in_file=str(path), out_file=str(tmp), no_info=True)
    font = TTFont(tmp)
    font["head"].flags |= 1 << 3        # integer ppem, as hinted fonts need
    font.save(path)
    tmp.unlink()


def woff2(path, dest):
    font = TTFont(path)
    font.flavor = "woff2"
    font.save(dest)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", type=Path, default=ROOT / "fonts" / "GeistSerif")
    a = ap.parse_args()
    for sub in ("variable", "ttf", "webfonts"):
        (a.out / sub).mkdir(parents=True, exist_ok=True)
    with open(SOURCE / "fontinfo.plist") as f:
        info = op.load(f, use_numbers=True)
    source_date = datetime.strptime(info["date"], "%Y-%m-%d %H:%M:%S %z")
    os.environ.setdefault("SOURCE_DATE_EPOCH", str(int(source_date.timestamp())))
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        expanded = tmp / "GeistSerif.glyphspackage"
        shutil.copytree(SOURCE, expanded)
        print(f"expanded corners and strokes in {glyphs_corners.expand_package(SOURCE, expanded)} glyphs")

        built = fontmake(expanded, "variable", tmp / "vf")
        vf = a.out / "variable" / "GeistSerif[ELSH].ttf"
        finish_variable(built, vf)
        hint(vf)
        woff2(vf, a.out / "webfonts" / VF_WOFF2)
        print(vf.name)

        for instance in info["instances"]:
            if instance.get("type") == "variable": continue
            style = instance["name"]
            src = static_source(expanded, instance, tmp / style / "GeistSerif.glyphspackage")
            dest = a.out / "ttf" / f"{PS}-{style}.ttf"
            finish_static(fontmake(src, "ttf", tmp / style / "out", "--overlaps-backend", "pathops"), dest, style)
            hint(dest)
            woff2(dest, a.out / "webfonts" / f"{PS}-{style}.woff2")
            print(dest.name)


if __name__ == "__main__":
    main()
