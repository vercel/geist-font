---
"geist": patch
---

Geist Sans and Geist Mono: fix the `meta` table's supported-languages entry (`slng`), which was `Cyr`, not a valid script code, and is now `Latn,Cyrl`. macOS had reported the fonts as Cyrillic-only, so apps that filter fonts by language, such as Warp, didn't list them. Font version 1.900 → 1.903.
