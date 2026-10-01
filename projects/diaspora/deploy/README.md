# Deployment note

Public name: `https://diaspora.acorsica.org`.

Observed on 2026-10-01. A DNS-only Cloudflare CNAME `diaspora.acorsica.org` points at `fracta.fractavolta.com`. Fracta terminates TLS and reverse-proxies to the Fracta2 HTTP origin. Fracta2 serves an immutable release under `/srv/www/diaspora/current`. The first release was `2026-10-01-82c261c`, from `82c261cc676816565a0bc2942623425d516275c1`, whose diaspora tree matches `db766566324628488793fd7e0b4edb079f7c862a`. The issue 96 comment names the release `current` points at.

The published root is the `projects/diaspora/` tree, so `web/*.html` can fetch `../data/seed.json`. A host that publishes only `web/` breaks the seed. `/` redirects to `/web/index.html`. There is still no `CNAME` file in this tree.

This is a static publication of the working projection, not a frozen edition. The cold-start record inside this repository is the 2026-10-01 milestone in `journals/reality-test-2026-09-30.md`. Operational placement stays with Operium: `docs/diaspora-acorsica-static.md`. Do not add a second runbook here.

Local use remains:

```text
cd projects/diaspora
node scripts/serve.js
```

There is no `CNAME` file in this tree, so enabling GitHub Pages on the folder would not by itself claim `diaspora.acorsica.org`.
