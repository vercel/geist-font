# Scripts

## Building Geist Serif

There are two ways to build Geist Serif from `sources/GeistSerif.glyphspackage`. Both write the same family: a variable font on the Element Shape (`ELSH`) axis, and four statics (Regular, Square, Triangle, Heart).

### With the builder

```bash
make build-serif
```

No Glyphs needed. Python 3.11 or newer is required. This installs its own environment from `requirements-serif.txt` and writes `fonts/GeistSerif/variable`, `ttf` and `webfonts`. If `python3` is older, select a newer interpreter with `make PYTHON=python3.11 build-serif`.

The build derives `SOURCE_DATE_EPOCH` from the source's Glyphs date so repeated builds produce byte-identical files.

- `build-geist-serif.py` is the build.
- `glyphs_corners.py` expands the corner components, cap components and stroked paths in a temporary copy of the source. Geist Serif's serifs are corner components, which fontmake can't draw correctly on its own. The source itself is never changed.

### With Glyphs

Open the source in Glyphs 3 and use **File > Export**. Before exporting, go to **File > Font Info > Features** and make sure the **VARIATIONS** prefix is **disabled**.

That prefix is another copy of the `ELSH` glyph swaps that are already in the `rclt` feature. Leave it off for every export.

Variable export settings to keep:

- **Use Extension Kerning** stays on the variable font's export setting. Without it, the kerning overflows and the export fails with "Problem compiling GPOS table".

For the statics, turn on **Remove Overlap** and **Autohint** in the export dialog.

A Glyphs export doesn't include what the builder adds for Google Fonts: overlaps removed from the variable font, an `HVAR` table, a `meta` table, and a `STAT` table with only the `ELSH` axis. Use the builder for anything going to Google Fonts.

**Check the Square, Triangle and Heart statics.** Exporting them from this source with Glyphs 3.5 (3532) through its Python API changed the serifs on 118 glyphs, including 3, 6, T, X and Æ. Compare them against Regular: only the dot sets, `ellipsis`, `quoteleft`, `quoteright` and `Abrevedotbelow` should differ. The builder doesn't have this problem.
