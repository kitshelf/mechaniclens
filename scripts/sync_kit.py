#!/usr/bin/env python3
"""Copy the kit's Markdown from the repo into the package's data dir.

The repo is the single source of truth. This script copies the user-facing kit
files into ``mechaniclens/kit/`` so the built wheel ships exactly what the repo
holds. Run it before every build; a drift check lives in the test suite.

    python3 scripts/sync_kit.py
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "mechaniclens" / "kit"

# What ships in the package: the kit itself, not the build docs or tests.
INCLUDE_DIRS = ["estimate", "shared"]
INCLUDE_FILES = ["WHAT-THIS-IS.md", "USER-GUIDE.md", "ROADMAP.md", "CHANGELOG.md"]

# Never ship these even if they sit inside an included dir.
SKIP_NAMES = {"__pycache__", ".DS_Store"}


def main() -> int:
    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir(parents=True)

    for name in INCLUDE_DIRS:
        src = ROOT / name
        if not src.is_dir():
            print(f"missing: {src}", file=sys.stderr)
            return 1
        shutil.copytree(
            src,
            DEST / name,
            ignore=shutil.ignore_patterns(*SKIP_NAMES),
        )

    for name in INCLUDE_FILES:
        src = ROOT / name
        if not src.is_file():
            print(f"missing: {src}", file=sys.stderr)
            return 1
        shutil.copy2(src, DEST / name)

    count = sum(1 for p in DEST.rglob("*") if p.is_file())
    print(f"synced {count} files into {DEST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
