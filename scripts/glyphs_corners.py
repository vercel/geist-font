"""Glyphs 3 corner components, cap components and strokes expanded into real points, in plain Python.

glyphsLib's corner filter gets Geist Serif wrong (no caps, no left/right anchors, no {x%, y%} layers, no corners on
curves) and fontmake ignores stroked paths, so build-geist-serif.py runs this over a copy of the source first.
Checked node by node against Glyphs' own decomposeCorners on all 66 Geist Serif glyphs that use them.

A shape is a closed list of nodes: {"pt", "h": None | (h1, h2), "serif": bool | id} where "h" are the handles of the
segment ARRIVING at the node. Needs openstep_plist (installed with glyphsLib).
"""
import glob, math, os
import openstep_plist as op


def glyph_file(name):
    """a .glyphspackage glyph file name (UFO-style: every capital gets a trailing _)"""
    return "".join(c + "_" if c.isupper() else c for c in name) + ".glyph"


class GlyphsSource:
    """glyph dicts by name from a .glyphspackage (glyphs/<name>.glyph) or a Glyphs-3 .glyphs file"""

    def __init__(self, path):
        self.path = str(path).rstrip("/")
        self.package = self.path.endswith(".glyphspackage")
        self._glyphs = {}
        self._all = None
        self._fontinfo = None
        self._warned = set()

    def fontinfo(self):
        if self._fontinfo is None:
            if self.package:
                self._fontinfo = op.load(open(os.path.join(self.path, "fontinfo.plist")), use_numbers=True)
            else:
                self._load_all(); self._fontinfo = self._file
        return self._fontinfo

    def _load_all(self):
        if self._all is None:
            self._file = op.load(open(self.path), use_numbers=True)
            if int(self._file.get(".formatVersion", 2)) < 3:
                raise ValueError("%s is a Glyphs 2 file: corner components are read from Glyphs 3 sources only" % self.path)
            self._all = {g["glyphname"]: g for g in self._file.get("glyphs", [])}

    def glyph(self, name):
        if name not in self._glyphs:
            if self.package:
                fn = os.path.join(self.path, "glyphs", glyph_file(name))
                if not os.path.exists(fn):
                    fn = self._file_index().get(name, fn)       # Glyphs' own file names (.notdef -> _notdef.glyph)
                self._glyphs[name] = op.load(open(fn), use_numbers=True)
            else:
                self._load_all(); self._glyphs[name] = self._all[name]
        return self._glyphs[name]

    def _file_index(self):
        """{glyph name: file} read from every glyph file's glyphname (only when the UFO-style name is not on disk)"""
        if getattr(self, "_index", None) is None:
            self._index = {}
            d = os.path.join(self.path, "glyphs")
            for fn in os.listdir(d):
                if fn.endswith(".glyph"):
                    try:
                        self._index[op.load(open(os.path.join(d, fn)), use_numbers=True)["glyphname"]] = os.path.join(d, fn)
                    except Exception:
                        pass
        return self._index

    def layer(self, name, reg):
        return next(L for L in self.glyph(name)["layers"] if L["layerId"] == reg)

    def master_axes(self):
        """{master id: [axis values]} from the font info"""
        return {m["id"]: list(m.get("axesValues", [])) for m in self.fontinfo().get("fontMaster", [])}

    def corner_layer(self, name, reg):
        """a corner / cap component's layer for master reg; when that master's layer is empty (a source whose
        other masters are unfinished), the layer of the NEAREST master (axis values) that has one, with a warning"""
        L = next((L for L in self.glyph(name)["layers"] if L["layerId"] == reg), None)
        if L is not None and L.get("shapes"):
            return L
        ax = self.master_axes(); here = ax.get(reg, [])
        drawn = [L for L in self.glyph(name)["layers"] if L["layerId"] in ax and L.get("shapes")]
        if not drawn:
            raise KeyError("corner component %s has no drawn master layer" % name)
        dist = lambda L: sum((a - b) ** 2 for a, b in zip(ax[L["layerId"]], here))
        best = min(drawn, key=dist)
        key = (name, reg)
        if key not in self._warned:
            self._warned.add(key)
            print("WARN corner component %s: master %s has no drawing, using master %s's" % (name, reg, best["layerId"]))
        return best

    def smart_layer(self, name, reg):
        cands = [L for L in self.glyph(name)["layers"] if L.get("associatedMasterId") == reg and "coordinates" in L.get("attr", {})]
        both = [L for L in cands if min(L["attr"]["coordinates"]) > 100]     # Black has several; use the one extending on both axes
        for L in (both or cands)[:1]:
            return L["attr"]["coordinates"], L
        return None


_SOURCES = {}


def source(src):
    if isinstance(src, GlyphsSource):
        return src
    key = str(src).rstrip("/")
    if key not in _SOURCES:
        _SOURCES[key] = GlyphsSource(key)
    return _SOURCES[key]


def advance(name, src, reg):
    return source(src).layer(name, reg)["width"]


def _chain(nodes, closed):
    """Glyphs node list -> on-curve nodes with their arriving handles, plus raw-index map."""
    out = []; index = {}
    for i, n in enumerate(nodes):
        if n[2][0] == "o": continue
        h = None
        if n[2][0] == "c": h = (tuple(nodes[i - 2][:2]), tuple(nodes[i - 1][:2]))
        index[i] = len(out); out.append({"pt": (float(n[0]), float(n[1])), "h": h, "serif": False})
    return out, index

def _unit(a, b):
    d = math.hypot(b[0] - a[0], b[1] - a[1]); return ((b[0] - a[0]) / d, (b[1] - a[1]) / d)
def _add(p, v, k=1.0): return (p[0] + v[0] * k, p[1] + v[1] * k)
def _dot(a, b): return a[0] * b[0] + a[1] * b[1]
def _perp_towards(axis, side):
    p = (-axis[1], axis[0]); return p if _dot(p, side) > 0 else (axis[1], -axis[0])
def _hit(o, d, a, u):
    """s such that o + s*d lies on the line through a with direction u."""
    den = d[0] * u[1] - d[1] * u[0]
    return ((a[0] - o[0]) * u[1] - (a[1] - o[1]) * u[0]) / den

def _offset_edge(path, d):
    """one edge of a stroke: the closed path moved d units to the left of its direction (right if d < 0). Same nodes,
    tangents kept; handles scale with the segment's chord, which is exact for circular arcs."""
    def sides(i):
        pts = [path[i - 1]["pt"], *(path[i]["h"] or ()), path[i]["pt"]]
        pts = [p for j, p in enumerate(pts) if j == 0 or math.dist(p, pts[j - 1]) > 1e-9]
        return _unit(pts[0], pts[1]), _unit(pts[-2], pts[-1])
    def left(t): return (-t[1], t[0])
    pts = []
    for i, node in enumerate(path):
        t1 = sides(i)[1]; t2 = sides((i + 1) % len(path))[0]
        n1, n2 = left(t1), left(t2)
        p = _add(node["pt"], n1, d); turn = _dot(t1, n2)
        pts.append(p if abs(turn) < 1e-6 else _add(p, t1, d * (1 - _dot(n1, n2)) / turn))   # smooth, else mitre
    out = []
    for i, node in enumerate(path):
        h = None
        if node["h"]:
            p0, p3 = path[i - 1]["pt"], node["pt"]
            s = math.dist(pts[i - 1], pts[i]) / math.dist(p0, p3)
            h = (_add(pts[i - 1], (node["h"][0][0] - p0[0], node["h"][0][1] - p0[1]), s),
                 _add(pts[i], (node["h"][1][0] - p3[0], node["h"][1][1] - p3[1]), s))
        out.append({**node, "pt": pts[i], "h": h})
    return out

def _reversed(path):
    """the same closed path run backwards (a node's h is its ARRIVING segment, so handles come from the next node)"""
    n = len(path)
    return [{**path[i], "h": path[(i + 1) % n]["h"] and tuple(reversed(path[(i + 1) % n]["h"]))} for i in range(n - 1, -1, -1)]

def _area(path):
    return sum(path[i - 1]["pt"][0] * n["pt"][1] - n["pt"][0] * path[i - 1]["pt"][1] for i, n in enumerate(path)) / 2

def outline_stroke(path, attr):
    """a closed path with a Glyphs stroke -> [outer edge, inner edge run backwards], Glyphs' Outline Stroke.
    strokePos 1: the stroke sits left of the path's direction, so the drawn path is one edge (checked against the
    exported TTF on copyright and registered). -1 (right) and 0 / absent (centred) are by symmetry, not yet checked."""
    w = attr["strokeWidth"]; pos = attr.get("strokePos", 0)
    a, b = (path, _offset_edge(path, w)) if pos > 0 else (path, _offset_edge(path, -w)) if pos < 0 else (_offset_edge(path, w / 2), _offset_edge(path, -w / 2))
    if abs(_area(b)) > abs(_area(a)): a, b = b, a
    return [a, _reversed(b)]

def _cut_curve(p0, h1, h2, p3, s, steps=200):
    """the part of a cubic up to arc length s measured back from p3 -> (handle, handle, end point)"""
    at = lambda u: tuple((1 - u) ** 3 * a + 3 * (1 - u) ** 2 * u * b + 3 * (1 - u) * u ** 2 * c + u ** 3 * d for a, b, c, d in zip(p0, h1, h2, p3))
    run = 0.0; last = p3; u = 0.0
    for i in range(1, steps + 1):
        v = 1 - i / steps; q = at(v); d = math.dist(last, q)
        if run + d >= s:
            u = v + (1 / steps) * (run + d - s) / d if d else v
            break
        run += d; last = q
    lerp = lambda a, b: (a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)
    a, b, c = lerp(p0, h1), lerp(h1, h2), lerp(h2, p3); d, e = lerp(a, b), lerp(b, c)
    return a, d, lerp(d, e)

def _corner(hint, path, k, S, reg):
    L = S.corner_layer(hint["name"], reg); nodes = L["shapes"][0]["nodes"]
    anchors = {a["name"]: a.get("pos", (0, 0)) for a in L.get("anchors", [])}
    sx, sy = hint.get("scale", (1, 1)); flipped = sx * sy < 0; sx, sy = abs(sx), abs(sy)
    smart = S.smart_layer(hint["name"], reg)
    if smart:
        # A corner with a layer at {x%, y%} is not scaled geometrically: the hint's y scale alone picks a point
        # on the line through the 100% drawing and that layer, past it too (checked against Glyphs' decomposeCorners:
        # six [1, 1.6] is 75% of the way to {180, 180}, three [1, 2] is 125%, four [1.2, 1] is the 100% drawing).
        (px, py), S = smart
        # (a master whose smart layer sits at 100 in y, e.g. Black's {300,100}, has no extent there -> t from x)
        t = (sy * 100 - 100) / (py - 100) if py != 100 else (sx * 100 - 100) / (px - 100)
        mix = lambda a, b: a + (b - a) * t
        nodes = [[mix(a[0], b[0]), mix(a[1], b[1]), a[2]] for a, b in zip(nodes, S["shapes"][0]["nodes"])]
        sa = {a["name"]: a.get("pos", (0, 0)) for a in S.get("anchors", [])}
        anchors = {k: (mix(v[0], sa[k][0]), mix(v[1], sa[k][1])) for k, v in anchors.items()}
        sx = sy = 1.0
    cn, _ = _chain(nodes, False)
    P = path[k]["pt"]; prev = path[k - 1]["pt"]; nxt = path[(k + 1) % len(path)]["pt"]
    assert path[(k + 1) % len(path)]["h"] is None, "corner leaving on a curved stroke"
    cut = None
    if path[k]["h"]:
        # The stroke arrives on a curve: the corner's first node sits on it at that arc length from the node, and the
        # corner is placed against the chord to that point (Glyphs: six's first node is 110 along the curve, three's 134).
        assert not flipped, "flipped corner on a curved stroke"
        cut = _cut_curve(prev, *path[k]["h"], P, cn[0]["pt"][1] * sy)
        prev = cut[2]
    back, out = _unit(P, prev), _unit(P, nxt)
    X, Y = (back, out) if flipped else (out, back)          # strokes the corner's x and y sides sit on
    align = hint.get("options", 0) & 3                       # 0 outstroke, 1 instroke, 2 middle
    x_rigid = (align == 1) == flipped if align < 2 else True
    if x_rigid: ex = X; ey = _perp_towards(ex, Y)
    else: ey = Y; ex = _perp_towards(ey, X)
    ly = anchors["left"][1] * sy if "left" in anchors else 0.0
    rx = anchors["right"][0] * sx if "right" in anchors else 0.0
    O = P
    if "left" in anchors and x_rigid and abs(_dot(ex, Y)) > 1e-6:
        O = _add(P, ex, _hit(_add(P, ey, ly), ex, P, Y))     # slide until `left` meets the y stroke
    if "right" in anchors and not x_rigid and abs(_dot(ey, X)) > 1e-6:
        O = _add(P, ey, _hit(_add(P, ex, rx), ey, P, X))
    T = lambda c: _add(_add(O, ex, c[0] * sx), ey, c[1] * sy)
    pts = [{"pt": T(n["pt"]), "h": n["h"] and tuple(T(h) for h in n["h"]), "serif": id(hint)} for n in cn]
    # the two ends ride their strokes, whatever angle those run at
    Lp = _add(O, ey, ly); first = cn[0]["pt"]
    if abs(_dot(ex, Y)) > 1e-6:
        pts[0]["pt"] = _add(Lp, Y, first[1] * sy - ly)
        h = cn[1]["h"]                                       # a handle in line with that end stays on the stroke too
        if h and abs(h[0][0] - first[0]) < 1e-6: pts[1]["h"] = (_add(Lp, Y, h[0][1] * sy - ly), pts[1]["h"][1])
    Rp = _add(O, ex, rx); last = cn[-1]["pt"]
    if "right" in anchors and abs(_dot(ey, X)) > 1e-6: pts[-1]["pt"] = _add(Rp, X, last[0] * sx - rx)   # without the anchor (serif-alt) it stays as drawn
    if flipped:
        rev = [dict(p) for p in reversed(pts)]
        for i, p in enumerate(rev):                          # handles belong to the arriving segment
            src = pts[len(pts) - i] if i else None
            p["h"] = src["h"][::-1] if src and src["h"] else None
        pts = rev
    pts[0]["h"] = None
    if cut: pts[0]["pt"] = cut[2]; pts[0]["h"] = cut[:2]
    return pts

def _cap(hint, path, k, S, reg):
    L = S.corner_layer(hint["name"], reg); cn, _ = _chain(L["shapes"][0]["nodes"], False)
    a = {x["name"]: x["pos"] for x in L["anchors"]}; n1, n2 = a["node1"], a["node2"]
    P, Q = path[k]["pt"], path[(k + 1) % len(path)]["pt"]
    u = _unit(P, Q); n = (u[1], -u[0])
    sx, sy = hint.get("scale", (1, 1))     # the hint's scale, not a fit: h's cap keeps its drawn 80 on an 84 stem
    T = lambda c: _add(_add(P, u, (n1[0] - c[0]) * sx), n, (c[1] - n1[1]) * sy)
    pts = [{"pt": T(x["pt"]), "h": x["h"] and tuple(T(h) for h in x["h"]), "serif": id(hint)} for x in cn]
    pts[0]["h"] = path[k]["h"]
    return pts

GEOMETRY_KEYS = ("ref", "pos", "angle", "scale", "alignment", "anchor", "locked", "orientation", "userData")


def component_transform(s):
    """a Glyphs 3 component's affine transform (xx, xy, yx, yy, dx, dy), fontTools order: translate(pos) . rotate(angle)
    . scale(scale), as Glyphs and glyphsLib compose it (x' = xx x + yx y + dx, y' = xy x + yy y + dy)"""
    sx, sy = (s.get("scale") or (1, 1))[:2]
    a = math.radians(float(s.get("angle", 0) or 0)); c, n = math.cos(a), math.sin(a)
    dx, dy = (s.get("pos") or (0, 0))[:2]
    return (c * sx, n * sx, -n * sy, c * sy, float(dx), float(dy))


def apply_transform(xf, p):
    a, b, c, d, tx, ty = xf
    return (a * p[0] + c * p[1] + tx, b * p[0] + d * p[1] + ty)


def _xf_shape(sh, xf):
    return [{**n, "pt": apply_transform(xf, n["pt"]), "h": n["h"] and tuple(apply_transform(xf, h) for h in n["h"])} for n in sh]


def layer_parts(name, src, reg):
    """-> (advance, [own shape], [(component glyph name, transform, [shape])]): the layer's drawn paths (corner / cap
    components expanded) and each component's outline carried through its full transform (pos, angle, scale, flip).
    shapes() is the two concatenated: own paths first, then the components in file order."""
    S = source(src)
    L = S.layer(name, reg); out = []; refs = []
    paths = []; maps = []
    for s in L["shapes"]:
        if "ref" in s:
            odd = [k for k in s if k not in GEOMETRY_KEYS]
            if odd and (name, s["ref"]) not in S._warned:
                S._warned.add((name, s["ref"])); print("WARN component %s in %s: keys %s are not read" % (s["ref"], name, odd))
            xf = component_transform(s)
            refs.append((s["ref"], xf, [_xf_shape(sh, xf) for sh in shapes(s["ref"], S, reg)[1]]))
            paths.append(None); maps.append(None)
        else:
            c, ix = _chain(s["nodes"], True); paths.append(c); maps.append(ix)
    repl = {}
    for h in L.get("hints", []):
        if h.get("type") not in ("Corner", "Cap"): continue
        pi, ni = h["origin"]; path = paths[pi]; k = maps[pi][ni]
        if h["type"] == "Corner": repl[(pi, k)] = _corner(h, path, k, S, reg)
        else:
            repl[(pi, k)] = _cap(h, path, k, S, reg); repl[(pi, (k + 1) % len(path))] = []
    for pi, path in enumerate(paths):
        if path is None: continue
        new = []
        for k, node in enumerate(path):
            if (pi, k) in repl:
                chain = repl[(pi, k)]
                if chain and chain[0]["h"] is None and math.dist(chain[0]["pt"], node["pt"]) < 1e-6: chain[0]["h"] = node["h"]
                new += chain
            else: new.append(node)
        stroke = L["shapes"][pi].get("attr") or {}
        out += outline_stroke(new, stroke) if "strokeWidth" in stroke and L["shapes"][pi].get("closed", 1) else [new]
    return L["width"], out, refs


def shapes(name, src, reg):
    """-> (advance, [shape]) for master id reg, corner / cap components expanded, components flattened through their
    full transform (drawn paths first, then component refs, the order the solver's JSON always used).
    src: a .glyphspackage / Glyphs-3 .glyphs path or a GlyphsSource."""
    w, own, refs = layer_parts(name, src, reg)
    return w, own + [sh for _, _, shs in refs for sh in shs]

def to_nodes(shape):
    """expanded shape (nodes carry the handles of the ARRIVING segment) -> [[x,y,type,smooth],...] with off-curves."""
    n = len(shape); res = []
    for i, nd in enumerate(shape):
        if nd["h"]:
            res.append([nd["h"][0][0], nd["h"][0][1], 'o', False]); res.append([nd["h"][1][0], nd["h"][1][1], 'o', False])
        res.append([nd["pt"][0], nd["pt"][1], 'c' if nd["h"] else 'l', False])
    # smooth: a node with a curve on at least one side whose in/out tangents are parallel and opposite-facing
    def tang(a, b):
        d = math.hypot(b[0] - a[0], b[1] - a[1]); return None if d < 1e-9 else ((b[0] - a[0]) / d, (b[1] - a[1]) / d)
    k = 0
    for i, nd in enumerate(shape):
        k += 2 if nd["h"] else 0
        nxt = shape[(i + 1) % n]; prv = shape[i - 1]
        tin = tang(nd["h"][1], nd["pt"]) if nd["h"] else tang(prv["pt"], nd["pt"])
        tout = tang(nd["pt"], nxt["h"][0]) if nxt["h"] else tang(nd["pt"], nxt["pt"])
        if (nd["h"] or nxt["h"]) and tin and tout and abs(tin[0] * tout[1] - tin[1] * tout[0]) < 2e-3 and tin[0] * tout[0] + tin[1] * tout[1] > 0:
            res[k][3] = True
        k += 1
    if res[0][2] == 'o': res = res[2:] + res[:2]      # handles precede their node, as in the file
    return res


def _plist_nodes(shape):
    return [[round(x, 3), round(y, 3), t + ("s" if smooth else "")] for x, y, t, smooth in to_nodes(shape)]


def expand_package(src, dst):
    """rewrite the .glyphspackage copy at dst: every master layer's corners, caps and strokes become plain paths"""
    S = GlyphsSource(src)
    masters = {m["id"] for m in S.fontinfo()["fontMaster"]}
    changed = 0
    for path in sorted(glob.glob(os.path.join(dst, "glyphs", "*.glyph"))):
        with open(path) as f:
            g = op.load(f, use_numbers=True)
        touched = False
        for L in g["layers"]:
            if L.get("layerId") not in masters: continue
            shapes_ = L.get("shapes", [])
            stroked = any("strokeWidth" in (s.get("attr") or {}) for s in shapes_ if "ref" not in s)
            if not stroked and not any(h.get("type") in ("Corner", "Cap") for h in L.get("hints", [])): continue
            own = iter(layer_parts(g["glyphname"], S, L["layerId"])[1])
            new = []
            for s in shapes_:
                if "ref" in s:
                    new.append(s); continue
                attr = {k: v for k, v in (s.get("attr") or {}).items() if not k.startswith("stroke")}
                for i in range(2 if "strokeWidth" in (s.get("attr") or {}) else 1):
                    d = {k: v for k, v in s.items() if k != "attr"}
                    d["nodes"] = _plist_nodes(next(own))
                    if attr and i == 0: d["attr"] = attr
                    new.append(d)
            L["shapes"] = new
            L["hints"] = [h for h in L.get("hints", []) if h.get("type") not in ("Corner", "Cap")]
            if not L["hints"]: del L["hints"]
            touched = True
        if touched:
            with open(path, "w") as f:
                op.dump(g, f)
            changed += 1
    return changed
