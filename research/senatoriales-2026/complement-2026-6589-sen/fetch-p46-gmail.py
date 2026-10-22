#!/usr/bin/env python3
"""Fetch the 46 indexed P-46 messages as private RFC 2822 .eml files.

Uses a local Google OAuth desktop client and Gmail's read-only API. Message
bodies, OAuth tokens, and downloaded source mail must remain outside this repo.
"""
from __future__ import annotations

import argparse
import base64
import csv
from datetime import datetime, timezone
from email import policy
from email.parser import BytesParser
from http.server import BaseHTTPRequestHandler, HTTPServer
import hashlib
import json
import os
from pathlib import Path
import re
import secrets
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlencode, urlparse
from urllib.request import Request, urlopen

SCOPE = "https://www.googleapis.com/auth/gmail.readonly"
AUTH_ENDPOINT = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
API_ROOT = "https://gmail.googleapis.com/gmail/v1/users/me/messages/"


def indexed_messages(source: Path) -> list[tuple[str, str]]:
    pattern = re.compile(r"^\| \*\*P-46\.(\d{2})\*\* \|.*\| `([0-9a-fA-F]+)` \|\s*$")
    found: dict[int, str] = {}
    for line in source.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            number, message_id = int(match.group(1)), match.group(2)
            if number in found:
                raise ValueError(f"Duplicate P-46 index row: {number:02}")
            found[number] = message_id
    expected = set(range(1, 47))
    if set(found) != expected or len(set(found.values())) != 46:
        raise ValueError("Source index must contain 46 unique Gmail IDs, P-46.01 through P-46.46")
    return [(f"P-46.{number:02}", found[number]) for number in range(1, 47)]


def load_client(path: Path) -> tuple[str, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    client = data.get("installed")
    if not isinstance(client, dict) or not client.get("client_id") or not client.get("client_secret"):
        raise ValueError("OAuth JSON must be a Google Desktop app client (top-level 'installed')")
    return client["client_id"], client["client_secret"]


class OAuthCallback(BaseHTTPRequestHandler):
    def do_GET(self):  # noqa: N802
        query = parse_qs(urlparse(self.path).query)
        self.server.oauth_state = query.get("state", [None])[0]
        self.server.oauth_code = query.get("code", [None])[0]
        self.server.oauth_error = query.get("error", [None])[0]
        body = b"Authorization received. You can return to the extraction process."
        self.send_response(200 if self.server.oauth_code else 400)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, _format, *_args):
        return


def oauth_authorize(client_id: str, client_secret: str) -> dict:
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
    state = secrets.token_urlsafe(32)
    server = HTTPServer(("127.0.0.1", 0), OAuthCallback)
    server.timeout = 1
    redirect_uri = f"http://127.0.0.1:{server.server_port}/"
    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": SCOPE,
        "access_type": "offline",
        "prompt": "consent",
        "state": state,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
    }
    print("Open this Google authorization URL in your browser:", flush=True)
    print(AUTH_ENDPOINT + "?" + urlencode(params), flush=True)
    print("Waiting up to 5 minutes for the local OAuth callback…", flush=True)
    deadline = time.monotonic() + 300
    try:
        while time.monotonic() < deadline and not getattr(server, "oauth_code", None) and not getattr(server, "oauth_error", None):
            server.handle_request()
    finally:
        server.server_close()
    if getattr(server, "oauth_state", None) != state:
        raise RuntimeError("OAuth state mismatch or authorization timed out")
    if getattr(server, "oauth_error", None):
        raise RuntimeError("Google authorization was not completed")
    payload = urlencode({
        "code": server.oauth_code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
        "code_verifier": verifier,
    }).encode()
    return json_request(TOKEN_ENDPOINT, payload=payload)


def json_request(url: str, *, token: str | None = None, payload: bytes | None = None) -> dict:
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if payload is not None:
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    request = Request(url, data=payload, headers=headers)
    try:
        with urlopen(request, timeout=45) as response:
            return json.loads(response.read())
    except HTTPError as error:
        raise RuntimeError(f"Google API request failed with HTTP {error.code}") from None
    except URLError as error:
        raise RuntimeError(f"Google API connection failed: {error.reason}") from None


def refresh_access_token(client_id: str, client_secret: str, refresh_token: str) -> dict:
    payload = urlencode({
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
    }).encode()
    return json_request(TOKEN_ENDPOINT, payload=payload)


def save_token(path: Path, token: dict) -> None:
    token["saved_at"] = int(time.time())
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as stream:
        json.dump(token, stream)
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass


def active_token(token_file: Path, client_id: str, client_secret: str) -> str:
    token = None
    if token_file.exists():
        token = json.loads(token_file.read_text(encoding="utf-8"))
    if token and token.get("access_token") and int(token.get("saved_at", 0)) + int(token.get("expires_in", 0)) > time.time() + 60:
        return token["access_token"]
    if token and token.get("refresh_token"):
        updated = refresh_access_token(client_id, client_secret, token["refresh_token"])
        updated["refresh_token"] = token["refresh_token"]
    else:
        updated = oauth_authorize(client_id, client_secret)
    save_token(token_file, updated)
    return updated["access_token"]


def fetch_raw(message_id: str, token: str) -> bytes:
    data = json_request(API_ROOT + message_id + "?format=raw", token=token)
    raw = data.get("raw")
    if not raw:
        raise ValueError(f"Gmail returned no raw content for message {message_id}")
    return base64.urlsafe_b64decode(raw + "=" * (-len(raw) % 4))


def ensure_outside_repo(destination: Path, repo_root: Path) -> None:
    target = destination.resolve()
    root = repo_root.resolve()
    if target == root or root in target.parents:
        raise ValueError("Refusing to write private email data inside the repository")


def export(source: Path, client_json: Path, output_dir: Path, repo_root: Path) -> None:
    ensure_outside_repo(output_dir, repo_root)
    messages = indexed_messages(source)
    client_id, client_secret = load_client(client_json)
    if output_dir.exists():
        raise FileExistsError(f"Output directory already exists; refusing to overwrite: {output_dir}")
    token_file = Path(tempfile.gettempdir()) / "p46-2026-6589-gmail-oauth-token.json"
    token = active_token(token_file, client_id, client_secret)
    output_dir.mkdir(parents=True)
    manifest = []
    try:
        for reference, gmail_id in messages:
            raw = fetch_raw(gmail_id, token)
            parsed = BytesParser(policy=policy.default).parsebytes(raw)
            if not parsed.keys():
                raise ValueError(f"Downloaded content is not a parseable RFC message: {reference}")
            path = output_dir / f"{reference}.eml"
            with path.open("xb") as stream:
                stream.write(raw)
            manifest.append({
                "reference": reference,
                "gmail_message_id": gmail_id,
                "file": path.name,
                "bytes": len(raw),
                "sha256": hashlib.sha256(raw).hexdigest(),
            })
            print(f"Downloaded {reference}", flush=True)
        manifest_path = output_dir / "manifest.json"
        with manifest_path.open("x", encoding="utf-8") as stream:
            json.dump({"source": str(source), "retrieved_at": datetime.now(timezone.utc).isoformat(),
                       "scope": SCOPE, "messages": manifest}, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
        with (output_dir / "manifest.csv").open("x", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=["reference", "gmail_message_id", "file", "bytes", "sha256"])
            writer.writeheader()
            writer.writerows(manifest)
    except Exception:
        print(f"Partial private export retained for inspection at: {output_dir}", flush=True)
        raise
    print(f"Complete: {len(manifest)}/46 RFC 2822 messages saved privately.")
    print(f"Manifest: {output_dir / 'manifest.csv'}")
    print("No Gmail messages were modified.")


def main() -> None:
    here = Path(__file__).resolve().parent
    repo_root = Path(__file__).resolve().parents[3]
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--client-json", type=Path, required=True)
    ap.add_argument("--source", type=Path,
                    default=here / "texte-maitre-candidat-qpc-integrales-2026-10-22.md")
    ap.add_argument("--output-dir", type=Path,
                    default=Path(tempfile.gettempdir()) / "p46-2026-6589-originals")
    args = ap.parse_args()
    export(args.source, args.client_json, args.output_dir, repo_root)


if __name__ == "__main__":
    main()
