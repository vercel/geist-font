---
"geist": patch
---

Bump Geist Mono font binary version 1.700 → 1.701.

The internal font version stayed at 1.700 across the v1.7.1 and v1.7.2 npm releases even though `liga` was reverted at source in #217. Downstream consumers that key off the binary version (caches, font-validation pipelines, the `head.fontRevision` and `name` NameID-5 fields exposed in `fc-query`/DevTools) still see 1.700 and therefore can't tell apart a pre- and post-revert binary.

Closes the second half of #231.
