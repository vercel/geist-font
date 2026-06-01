---
"geist": patch
---

Bump Geist Mono font binary version 1.700 → 1.703.

The internal font version stayed at 1.700 across the v1.7.1 and v1.7.2 npm releases even though `liga` was reverted at source in #217. Downstream consumers that key off the binary version (caches, font-validation pipelines, the `head.fontRevision` and `name` NameID-5 fields exposed in `fc-query`/DevTools) still see 1.700 and therefore can't tell apart a pre- and post-revert binary.

The new value (`1.703`) matches the established `1.X.Y` → `1.<Y>0<Z>` convention already used by `Geist` (1.800 ↔ v1.8.0) and the prior `GeistMono` (1.700 ↔ v1.7.0): it lines up with the `v1.7.3` release this changeset will produce.

Closes the second half of #231.
