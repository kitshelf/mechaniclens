"""Command line for the MechanicLens kit.

    mechaniclens                print the path to the kit
    mechaniclens --spine        print the one-paste kit (SPINE.md) to stdout
    mechaniclens --copy DIR     copy the whole kit tree into DIR
    mechaniclens --list         list the kit's files

The kit is Markdown. This CLI only locates and copies it; it never runs a model
and never touches the network.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from . import __version__

KIT_DIR = Path(__file__).parent / "kit"
SPINE = KIT_DIR / "estimate" / "SPINE.md"


def _files() -> list[Path]:
    return sorted(p for p in KIT_DIR.rglob("*") if p.is_file())


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="mechaniclens",
        description="Locate and copy the MechanicLens Markdown kit.",
    )
    ap.add_argument("--version", action="version", version=f"mechaniclens {__version__}")
    ap.add_argument("--spine", action="store_true", help="print the one-paste kit (estimate/SPINE.md)")
    ap.add_argument("--copy", metavar="DIR", help="copy the whole kit tree into DIR")
    ap.add_argument("--list", action="store_true", help="list the kit's files")
    args = ap.parse_args(argv)

    if not KIT_DIR.is_dir():
        print(f"kit data missing at {KIT_DIR} — the package is broken", file=sys.stderr)
        return 1

    if args.spine:
        if not SPINE.is_file():
            print(f"SPINE.md missing at {SPINE}", file=sys.stderr)
            return 1
        sys.stdout.write(SPINE.read_text(encoding="utf-8"))
        return 0

    if args.copy:
        dest = Path(args.copy).expanduser()
        if dest.exists() and any(dest.iterdir()):
            print(f"{dest} is not empty — refusing to overwrite", file=sys.stderr)
            return 1
        shutil.copytree(KIT_DIR, dest, dirs_exist_ok=True)
        print(f"kit copied to {dest}")
        print(f"paste {dest / 'estimate' / 'SPINE.md'} into your AI chat first")
        return 0

    if args.list:
        for p in _files():
            print(p.relative_to(KIT_DIR))
        return 0

    print(f"MechanicLens kit {__version__}")
    print(f"  kit dir:  {KIT_DIR}")
    print(f"  one paste: {SPINE}")
    print()
    print("  mechaniclens --spine        print the kit")
    print("  mechaniclens --copy DIR     copy the kit into DIR")
    print("  mechaniclens --list         list the files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
