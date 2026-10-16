---
"geist": patch
---

Align font binary versions with the package version. Geist and Geist Italic: 1.800 → 1.801. Geist Mono and Geist Mono Italic: 1.700 → 1.801.

Geist Mono had stayed at 1.700 across v1.7.1 and v1.7.2, even though `liga` was reverted at source in #217, so pre- and post-revert binaries reported the same version (`head.fontRevision` / name ID 5). Geist Sans already reported 1.800, ahead of the 1.7.x package.

The package skips from 1.7.2 to 1.8.1 so the package version and the font version follow the same rule, `M.X.Y` ↔ `M.(X×100+Y)` (see "Version Numbers" in CONTRIBUTING.md). 1.8.0 is skipped because a GitHub release named `1.8.0` already exists with different font files.

Closes the second half of #231.
