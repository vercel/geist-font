---
"geist": patch
---

Fix Geist Mono rendering source-code text with unintended programming ligatures.

v1.7.0 unintentionally activated programming-ligature substitutions (`-->`, `==`, `!=`, `...`, `--`, etc.) under the `liga` (Standard Ligatures) OpenType feature, which is on by default in every renderer. As a result, text like `--debug-prerender`, `[id...]`, `[...id]`, or `NODE_OPTIONS='--debug-prerender' node` rendered with ligated glyphs and broke monospace alignment in code.

The source-level fix is in #217; this release ships the rebuilt binaries.
