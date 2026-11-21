#!/usr/bin/env python3
"""Fetch MechanicLens corpora on demand — stdlib only, text-only.

MechanicLens' corpus index (corpus/index.json) maps the Hugging Face surface
for auto repair and household repair (inside and outside the house). This tool
pulls a dataset's text files as-is; binaries are skipped unless converted first
with convert.py.

Usage:
    python3 corpus/fetch.py <dataset-id>
    python3 corpus/fetch.py <dataset-id> --max-mb 50

Text doctrine: .csv, .json, .jsonl, .md, .txt, .tsv. Everything else (parquet,
images, model artifacts) is skipped. Use convert.py for parquet payloads.
"""
import json
import os
import sys
import urllib.request

API = "https://huggingface.co/api/datasets"
TEXT_EXT = {".csv", ".json", ".jsonl", ".md", ".txt", ".tsv"}


def slug(did):
    return did.replace("/", "__")


def tree(did):
    url = f"{API}/{did}/tree/main?recursive=true"
    req = urllib.request.Request(url, headers={"User-Agent": "mechaniclens-corpus/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def download(did, max_mb=100):
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), slug(did))
    os.makedirs(dest, exist_ok=True)
    files = [f for f in tree(did) if f.get("type") == "file"]
    for f in files:
        path, size = f["path"], f.get("size", 0)
        ext = os.path.splitext(path)[1].lower()
        if ext not in TEXT_EXT:
            print(f"  skip {path} (non-text, {size/1e6:.2f} MB)")
            continue
        if max_mb and size > max_mb * 1_000_000:
            print(f"  skip {path} ({size/1e6:.2f} MB > cap)")
            continue
        out = os.path.join(dest, path)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        url = f"https://huggingface.co/datasets/{did}/resolve/main/{path}"
        req = urllib.request.Request(url, headers={"User-Agent": "mechaniclens-corpus/1.0"})
        with urllib.request.urlopen(req, timeout=120) as r, open(out, "wb") as fh:
            fh.write(r.read())
        print(f"  got {path} ({size/1e6:.2f} MB)")
    print(f"{did} -> corpus/{slug(did)}/")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for did in sys.argv[1:]:
        download(did)
