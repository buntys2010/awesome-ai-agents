#!/usr/bin/env python3
"""
Extend refresh_stars.py to optionally refresh additional CSVs, e.g., data/computer_use.csv.

Usage:
  python scripts/refresh_csv.py --token $GITHUB_TOKEN --paths data/frameworks.csv data/computer_use.csv
"""
import argparse
import csv
import os
import re
import sys
from datetime import datetime
import requests

GITHUB_API = "https://api.github.com"
REPO_RE = re.compile(r"https?://github.com/([^/]+)/([^/]+)")


def parse_repo(url: str):
    m = REPO_RE.match(url.strip())
    if not m:
        return None, None
    return m.group(1), m.group(2)


def get_repo_info(owner: str, repo: str, token: str):
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    r = requests.get(f"{GITHUB_API}/repos/{owner}/{repo}", headers=headers, timeout=20)
    if r.status_code != 200:
        return None
    data = r.json()
    stars = data.get("stargazers_count", "")
    pushed_at = data.get("pushed_at", "")
    last_commit = pushed_at.split("T")[0] if pushed_at else ""
    return stars, last_commit


def refresh_file(path: str, token: str):
    if not os.path.exists(path):
        print(f"WARN: {path} not found", file=sys.stderr)
        return 0
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)
    updated = 0
    for row in rows:
        url = row.get("github", "").strip()
        if not url:
            continue
        owner, repo = parse_repo(url)
        if not owner:
            continue
        info = get_repo_info(owner, repo, token)
        if not info:
            continue
        stars, last_commit = info
        if "stars" in row and stars:
            row["stars"] = str(stars)
        # Update last_update or last_commit depending on schema
        if "last_commit" in row and last_commit:
            row["last_commit"] = last_commit
        elif "last_update" in row and last_commit:
            row["last_update"] = last_commit
        updated += 1
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return updated


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--token", default=os.environ.get("GITHUB_TOKEN", ""))
    ap.add_argument("--paths", nargs="+", default=["data/frameworks.csv", "data/computer_use.csv"]) 
    args = ap.parse_args()

    total = 0
    for p in args.paths:
        total += refresh_file(p, args.token)
    print(f"Refreshed {total} entries across {len(args.paths)} files at {datetime.utcnow().isoformat()}Z")


if __name__ == "__main__":
    main()
