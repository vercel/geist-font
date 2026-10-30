# geist

## 1.9.0

### Minor Changes

- d33068f: Add Geist Serif variable and static fonts.

## 1.8.2

### Patch Changes

- 742b082: Center the horizontal bars in the Geist Sans yen sign across all weights.

## 1.8.1

### Patch Changes

- 3b58290: Align font binary versions with the package version. Geist and Geist Italic: 1.800 → 1.801. Geist Mono and Geist Mono Italic: 1.700 → 1.801.

  Geist Mono had stayed at 1.700 across v1.7.1 and v1.7.2, even though `liga` was reverted at source in #217, so pre- and post-revert binaries reported the same version (`head.fontRevision` / name ID 5). Geist Sans already reported 1.800, ahead of the 1.7.x package.

  The package skips from 1.7.2 to 1.8.1 so the package version and the font version follow the same rule, `M.X.Y` ↔ `M.(X×100+Y)` (see "Version Numbers" in CONTRIBUTING.md). 1.8.0 is skipped because a GitHub release named `1.8.0` already exists with different font files.

  Closes the second half of #231.

- 339fffd: Geist Sans: stop mapping U+03C9 (small omega ω) to the capital Omega glyph; encode U+2126 OHM SIGN instead.

## 1.7.2

### Patch Changes

- a4195ae: Update Geist Pixel webfonts with Google Fonts validation fixes.

  Resyncs the published Geist Pixel static webfonts (`Circle`, `Grid`, `Line`, `Square`, `Triangle`) with the source build, picking up the non-visual fixes made for the Google Fonts release (#229): ligature caret anchors (`fi`, `fl`, `f_i`, `A_I`, `U_I`), a `meta` table with ScriptLangTags, line/paragraph separator glyphs and removal of the visible soft hyphen, and 1-unit on-curve point alignment fixes on `e`, `eogonek`, and `hungarumlautcomb`. No visible letterforms change.

## 1.7.1

### Patch Changes

- c8ed578: Fix Geist Mono rendering source-code text with unintended programming ligatures.

  v1.7.0 unintentionally activated programming-ligature substitutions (`-->`, `==`, `!=`, `...`, `--`, etc.) under the `liga` (Standard Ligatures) OpenType feature, which is on by default in every renderer. As a result, text like `--debug-prerender`, `[id...]`, `[...id]`, or `NODE_OPTIONS='--debug-prerender' node` rendered with ligated glyphs and broke monospace alignment in code.

  The source-level fix is in #217; this release ships the rebuilt binaries.

## 1.7.0

### Minor Changes

- d7ef63c: We're excited to announce a new member to our font family: Geist Pixel

  It's a display typeface family featuring five unique pixel-based variants, each with a distinct visual style. It is designed for decorative use in headlines, logos, and other display contexts where a pixelated aesthetic is desired.

  It includes five distinct variants, each exported separately:

  | Export               | CSS Variable                  | Description              |
  | -------------------- | ----------------------------- | ------------------------ |
  | `GeistPixelSquare`   | `--font-geist-pixel-square`   | Square pixel shapes      |
  | `GeistPixelGrid`     | `--font-geist-pixel-grid`     | Grid-based pixel pattern |
  | `GeistPixelCircle`   | `--font-geist-pixel-circle`   | Circular pixel shapes    |
  | `GeistPixelTriangle` | `--font-geist-pixel-triangle` | Triangular pixel shapes  |
  | `GeistPixelLine`     | `--font-geist-pixel-line`     | Line-based pixel pattern |

  ```jsx
  import {
    GeistPixelSquare,
    GeistPixelGrid,
    GeistPixelCircle,
    GeistPixelTriangle,
    GeistPixelLine,
  } from "geist/font/pixel";
  ```
