# Deployment note

Desired public name: `diaspora.acorsica.org`.

This phase does not create that name. No DNS record, Cloudflare zone, server, certificate, or Operium route was changed.

The files that would be published are the static tree under `projects/diaspora/`, with the site root serving `web/` and the seed at `data/seed.json`. Relative links from `web/*.html` use `../data/seed.json`. A host that publishes only `web/` will break the seed unless that fetch path is preserved.

Operational placement belongs to Operium. Do not add a second runbook here. A later authorization would need to name the repository, the commit, the hostname, and the operator.

Until then, local use is:

```text
cd projects/diaspora
node scripts/serve.js
```

There is no `CNAME` file in this tree, so enabling GitHub Pages on the folder would not by itself claim `diaspora.acorsica.org`.
