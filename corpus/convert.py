#!/usr/bin/env python3
"""Convert binary corpora to text — JSON records plus a Markdown preview.

Some MechanicLens datasets ship as parquet. This tool downloads the dataset's
text files as-is, converts parquet payloads to `<stem>.json` (records) and
`<stem>.md` (20-row preview), and reports anything it cannot convert.

Usage:
    python3 corpus/convert.py <dataset-id> [<dataset-id> ...]

Text-only doctrine: nothing binary is kept. Parquet is read with pandas; a
failed read is reported and dropped, never kept as a binary.
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


def fetch(did, path, dest):
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    url = f"https://huggingface.co/datasets/{did}/resolve/main/{path}"
    req = urllib.request.Request(url, headers={"User-Agent": "mechaniclens-corpus/1.0"})
    with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as fh:
        fh.write(r.read())
    return dest


def convert(did):
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), slug(did))
    os.makedirs(dest, exist_ok=True)
    files = [f for f in tree(did) if f.get("type") == "file"]
    notes = []
    for f in files:
        path = f["path"]
        ext = os.path.splitext(path)[1].lower()
        stem = os.path.splitext(os.path.basename(path))[0]
        if ext in TEXT_EXT:
            fetch(did, path, os.path.join(dest, path))
            notes.append(f"text kept: {path}")
            continue
        if ext == ".parquet":
            tmp = os.path.join(dest, ".tmp_" + os.path.basename(path))
            fetch(did, path, tmp)
            try:
                import pandas as pd
                df = pd.read_parquet(tmp)
                # drop pandas index artifact columns
                df = df.loc[:, [c for c in df.columns if not str(c).startswith("__index_level")]]
                out = os.path.join(dest, f"{stem}.json")
                df.to_json(out, orient="records", force_ascii=False, indent=1)
                with open(os.path.join(dest, f"{stem}.md"), "w", encoding="utf-8") as fh:
                    fh.write(f"# {did} — {path}\n\nConverted from parquet. {len(df)} rows, columns: {', '.join(map(str, df.columns))}\n\n```\n")
                    fh.write(df.head(20).to_string())
                    fh.write("\n```\n")
                notes.append(f"converted parquet -> {stem}.json + {stem}.md ({len(df)} rows)")
            except Exception as exc:  # noqa: BLE001
                notes.append(f"parquet {path}: could not convert ({exc})")
            finally:
                if os.path.exists(tmp):
                    os.remove(tmp)
            continue
        notes.append(f"skipped non-text: {path}")
    print(f"\n{did}:")
    for n in notes:
        print("   ", n)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for did in sys.argv[1:]:
        try:
            convert(did)
        except Exception as exc:  # noqa: BLE001
            print(f"{did}: FAILED {exc}")
