#!/usr/bin/env python3
"""
Curate a weekly "What's New" digest:
- Scan data/frameworks.csv and known catalog pages
- Use GitHub API to detect newly released repos or major releases
- Append/refresh WHATS_NEW.md with highlights and suggested updates

This is a heuristic summarizer; feel free to expand sources.
"""
import csv
import os
import re
from datetime import datetime, timedelta
from urllib.parse import urlparse

import requests

CSV_PATH = os.path.join("data", "frameworks.csv")
GITHUB_API = "https://api.github.com"

WINDOW_DAYS = int(os.environ.get("CURATION_WINDOW_DAYS", "7"))
SINCE = datetime.utcnow() - timedelta(days=WINDOW_DAYS)

TOKEN = os.environ.get("GITHUB_TOKEN", "")
HEADERS = {"Accept": "application/vnd.github+json"}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"

REPO_RE = re.compile(r"https?://github.com/([^/]+)/([^/]+)")


def parse_repo(url: str):
    m = REPO_RE.match(url.strip())
    if not m:
        return None, None
    return m.group(1), m.group(2)


def repo_events(owner: str, repo: str):
    # fetch releases and recent commits
    rel = requests.get(f"{GITHUB_API}/repos/{owner}/{repo}/releases", headers=HEADERS, timeout=20).json()
    commits = requests.get(f"{GITHUB_API}/repos/{owner}/{repo}/commits", headers=HEADERS, timeout=20).json()
    highlights = []
    for r in rel if isinstance(rel, list) else []:
        dt = r.get("published_at") or r.get("created_at")
        if dt and dt >= SINCE.isoformat():
            highlights.append({
                "type": "release",
                "tag": r.get("tag_name", ""),
                "name": r.get("name", ""),
                "date": dt[:10],
                "url": r.get("html_url", "")
            })
    for c in commits if isinstance(commits, list) else []:
        dt = c.get("commit", {}).get("author", {}).get("date", "")
        if dt and dt >= SINCE.isoformat():
            if any(k in (c.get("commit", {}).get("message", "").lower()) for k in ["release", "v", "tag", "major", "breaking"]):
                highlights.append({
                    "type": "commit",
                    "sha": c.get("sha", "")[:7],
                    "message": c.get("commit", {}).get("message", "").split("\n")[0],
                    "date": dt[:10],
                    "url": c.get("html_url", "")
                })
    return highlights


def main():
    rows = []
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))

    digest = [f"# What’s New (last {WINDOW_DAYS} days)", ""]

    total = 0
    for row in rows:
        url = row.get("github", "")
        owner, repo = parse_repo(url)
        if not owner:
            continue
        events = repo_events(owner, repo)
        if events:
            name = row.get("name", f"{owner}/{repo}")
            digest.append(f"## {name}")
            for e in events:
                if e["type"] == "release":
                    digest.append(f"- Release {e['tag']} ({e['date']})")
                elif e["type"] == "commit":
                    digest.append(f"- Commit {e['sha']}: {e['message']} ({e['date']})")
            digest.append("")
            total += 1

    if total == 0:
        digest.append("No notable updates detected across tracked frameworks.")

    with open("WHATS_NEW.md", "w", encoding="utf-8") as f:
        f.write("\n".join(digest) + "\n")

    print(f"Curated {total} projects with updates since {SINCE.date()}")


if __name__ == "__main__":
    main()
