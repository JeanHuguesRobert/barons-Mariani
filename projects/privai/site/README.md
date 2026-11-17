# PrivAI static projection

Public French reading surface for the working n°1 projection.
There is no build step and no package install.

Open `index.html` in a browser, or point any static file server at this directory.
This slice does not add a server. Do not bind a port already held by a local service.

The corpus source of the reading is `../manuscript/n1/00-qui-restera-souverain.md`.
If HTML and Markdown diverge, the Markdown wins.

Do not add a `CNAME` file. Do not change DNS from this directory.
The 2026-10-04 DNS check was historical. On 2026-11-17, https://privai.acorsica.org/guide.html and guide.js were independently observed via HTTPS (HTTP 200), with an October working release served at that time.

The shared Guide implementation is sourced from `scripts/lib/living-book-guide/client.js` and deterministically projected to `projects/privai/site/guide.js` and `projects/capable/site/guide.js`. Check both projections with `node scripts/ops/sync-living-book-guides.mjs --check`; apply only after authorization, using `--write`. The profile and all book-specific editorial content remain local. Do not infer that updating GitHub automatically deploys PrivAI.
