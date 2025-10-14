#!/usr/bin/env python3
"""
Refresh stars and last commit dates for frameworks in data/frameworks.csv.

- Reads data/frameworks.csv
- Queries GitHub API for repo stars and latest commit date
- Updates CSV in place with refreshed 'stars' and 'last_commit'

Usage:
  python scripts/refresh_stars.py --token $GITHUB_TOKEN

Optionally run in CI weekly.
"""
import argparse
import csv
import os
import re
import sys
from datetime import datetime
from urllib.parse import urlparse

import requests

CSV_PATH = os.path.join("data", "frameworks.csv")
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


def refresh_csv(token: str):
    if not os.path.exists(CSV_PATH):
        print(f"ERROR: {CSV_PATH} not found", file=sys.stderr)
        sys.exit(1)

    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        for row in reader:
            rows.append(row)

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
        if stars:
            row["stars"] = str(stars)
        if last_commit:
            row["last_commit"] = last_commit
        updated += 1

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    print(f"Refreshed {updated} rows at {datetime.utcnow().isoformat()}Z")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--token", default=os.environ.get("GITHUB_TOKEN", ""))
    args = ap.parse_args()
    refresh_csv(args.token)


if __name__ == "__main__":
    main()
