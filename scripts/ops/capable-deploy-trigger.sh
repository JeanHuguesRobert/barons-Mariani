#!/bin/sh
# Fixed-purpose entrypoint for a restricted GitHub Actions SSH deploy key.
# Install root-owned at /usr/local/sbin/capable-deploy-trigger on Fracta2.
set -eu
repo=/home/ubuntu/barons-Mariani
git -C "$repo" fetch --no-tags origin main >/dev/null
revision=$(git -C "$repo" rev-parse origin/main)
exec sudo -n /usr/local/sbin/deploy-capable-working --revision "$revision" --apply
