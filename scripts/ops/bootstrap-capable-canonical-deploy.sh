#!/usr/bin/env bash
# ONE-TIME OWNER ADMINISTRATION ON FRACTA2.
# Install a single-purpose deployer, a restricted CI SSH key and its GitHub
# secret; perform the first atomic deployment before enabling auto-deploy.
# Never run by GitHub Actions or as an untrusted guest.
set -euo pipefail

repo=/home/ubuntu/barons-Mariani
owner_repo=JeanHuguesRobert/barons-Mariani
host=fracta.fractavolta.com
keyfile="$HOME/.ssh/capable-gh-actions-ed25519"
deployer=/usr/local/sbin/deploy-capable-working
trigger=/usr/local/sbin/capable-deploy-trigger

if [ "$(id -un)" != "ubuntu" ]; then
  echo "Run as the Fracta2 owner-account 'ubuntu' (sudo only inside this script)." >&2
  exit 2
fi
cd "$repo"
git fetch --no-tags origin main
if [ "$(git rev-parse HEAD)" != "$(git rev-parse origin/main)" ]; then
  git pull --ff-only origin main
fi
if ! command -v gh >/dev/null || ! gh auth status >/dev/null 2>&1; then
  echo "Authenticated GitHub CLI is required on Fracta2." >&2
  exit 2
fi
if [ ! -r /etc/ssh/ssh_host_ed25519_key.pub ]; then
  echo "Cannot independently pin this host's public SSH key." >&2
  exit 2
fi

# Owner-run privileged installation; the publishing agent does not receive
# a general root shell. Both entrypoints are owned by root, not CI/ubuntu.
sudo install -o root -g root -m 0755 \
  scripts/ops/deploy-capable-working.py "$deployer"
sudo install -o root -g root -m 0755 \
  scripts/ops/capable-deploy-trigger.sh "$trigger"
sudoers=$(mktemp)
trap 'rm -f "$sudoers"' EXIT
printf '%s\n' \
  'ubuntu ALL=(root) NOPASSWD: /usr/local/sbin/deploy-capable-working --revision * --apply' > "$sudoers"
sudo visudo -cf "$sudoers" >/dev/null
sudo install -o root -g root -m 0440 \
  "$sudoers" /etc/sudoers.d/90-capable-working-deploy

# A dedicated non-general-purpose SSH identity. The forced command
# ignores SSH_ORIGINAL_COMMAND, disallows PTY, tunneling and agent forwarding.
install -d -m 0700 "$HOME/.ssh"
if [ ! -f "$keyfile" ]; then
  ssh-keygen -q -t ed25519 -N '' \
    -f "$keyfile" -C 'capable-gh-actions-forced-deploy'
fi
chmod 0600 "$keyfile"
chmod 0644 "$keyfile.pub"
pub=$(cat "$keyfile.pub")
entry="restrict,command=\"$trigger\" $pub"
touch "$HOME/.ssh/authorized_keys"
chmod 0600 "$HOME/.ssh/authorized_keys"
if ! grep -Fq -- "$pub" "$HOME/.ssh/authorized_keys"; then
  printf '%s\n' "$entry" >> "$HOME/.ssh/authorized_keys"
fi
if ! grep -Fq -- "$entry" "$HOME/.ssh/authorized_keys"; then
  echo "The key exists but lacks the required forced command; refusing to enable CI." >&2
  exit 3
fi

# The key is known to this host. Never trust an unauthenticated ssh-keyscan
# as proof of the expected host identity.
host_pub=$(awk '{print $1" "$2}' /etc/ssh/ssh_host_ed25519_key.pub)
printf '%s %s\n' "$host" "$host_pub" \
  | gh secret set CAPABLE_DEPLOY_SSH_KNOWN_HOSTS -R "$owner_repo"
gh secret set CAPABLE_DEPLOY_SSH_PRIVATE_KEY -R "$owner_repo" < "$keyfile"
gh variable set CAPABLE_DEPLOY_HOST --body "$host" -R "$owner_repo"
gh variable set CAPABLE_DEPLOY_USER --body ubuntu -R "$owner_repo"

# Deploy now, verify the public effect, and only then activate recurring
# automation. No emails, no DNS changes, and no frozen book replacements.
revision=$(git rev-parse origin/main)
receipt=$(mktemp)
trap 'rm -f "$sudoers" "$receipt"' EXIT
sudo "$deployer" --revision "$revision" --apply > "$receipt"
python3 - "$receipt" <<'PY'
import json,sys
r=json.load(open(sys.argv[1]))
assert r['outcome']=='DEPLOYED_VERIFIED'
assert r['input_count']>=20
print('LOCAL_DEPLOY_OK',r['release'])
PY
python3 - "$receipt" <<'PY'
import json,sys,urllib.request
expected=json.load(open(sys.argv[1]))
prefix='https://capable.acorsica.org/'
def get(path):
    with urllib.request.urlopen(urllib.request.Request(
        prefix+path,headers={'User-Agent':'capable-canonical-bootstrap'}
    ),timeout=18) as r:
        assert r.status==200,(path,r.status)
        return r.read()
served=json.loads(get('candidate-deploy.json'))
assert served['release']==expected['release']
assert served['source_sha256']==expected['source_sha256']
for part in ['candidate.html','candidate.pdf','candidate.epub','en-preparation.html']:
    assert get(part)
html=get('candidate.html').decode('utf-8')
assert 'Les collectivités territoriales ont droit aux adaptations' in html
assert 'candidate.html' in get('en-preparation.html').decode('utf-8')
print('PUBLIC_HTTPS_VERIFIED',served['release'])
PY

gh variable set CAPABLE_CANONICAL_AUTODEPLOY --body true -R "$owner_repo"
printf 'CANONICAL_AUTO_DEPLOY_ENABLED\n'
