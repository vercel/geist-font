---
"geist": patch
---

Update Geist Pixel webfonts with Google Fonts validation fixes.

Resyncs the published Geist Pixel static webfonts (`Circle`, `Grid`, `Line`, `Square`, `Triangle`) with the source build, picking up the non-visual fixes made for the Google Fonts release (#229): ligature caret anchors (`fi`, `fl`, `f_i`, `A_I`, `U_I`), a `meta` table with ScriptLangTags, line/paragraph separator glyphs and removal of the visible soft hyphen, and 1-unit on-curve point alignment fixes on `e`, `eogonek`, and `hungarumlautcomb`. No visible letterforms change.
