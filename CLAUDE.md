# Instructions for Claude Code sessions in this repository

This is the PUBLIC, unofficial reference for the ESA ExoMars Rosalind Franklin rover. It is the public counterpart of a private research repository (`exomars-rover-private`, owned by the same author) where measurements are made. A session here has no memory of that work: rely on this file.

**What may be in this repository:** numbers with their source, status and tier; short explanations; our own scripts. **What must never be in it:** images, video, point clouds, 3D models or meshes, datasheets, ESA SPICE kernel files, text copied from papers beyond a short quotation, anything from the visPTU repository, anything from the Sketchfab 'ESA ExoMars Rover' model, or anything marked as local-only in the private repository. If unsure, leave it out and ask.

**Rules**
- Every dimension carries a source, a status (stated, derived, inferred, unknown) and a tier (A to D); see `docs/TIERS.md`. Say 'I don't know' rather than fill a gap; unknown rows stay in the table as unknown.
- Never fill an identifier (DOI, URL, figure number) from memory; check it or write 'unverified'.
- The dimension table and the rover-frame data are produced by an export script in the private repository (`sfm/export_public.py` there) which applies a blocklist; do not hand-edit `data/dimensions.*` or `data/rover-frame.json` except to fix a mistake, and say so in the commit message. After any new import, grep the whole repository for 'visptu', 'sketchfab', 'glb', 'mlabspace', local paths, and the author's name outside the licence files.
- Keep the 'unofficial, not affiliated with ESA' statement in the README and in the repository description.
- The ESA SPICE kernels are downloaded by `scripts/emrsp_geometry.py` into `data/lit/` (ignored by git); never commit them.
- The author's standing preference: finished work is committed and pushed without asking; still ask before anything destructive or before adding new third-party material.
- A separate design repository (`mondrian`, a simplified honest 1:4 scale model) will read this data; keep the JSON files stable and add fields rather than renaming them.
