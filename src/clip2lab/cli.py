from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .generate import generate_lab


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="clip2lab", description="transcript → lab pack")
    p.add_argument("transcript", type=Path, help="Path to transcript.txt")
    p.add_argument("-o", "--out", type=Path, default=Path("labs"), help="Output labs directory")
    p.add_argument("--slug", help="Lab folder name (default: parent dir name)")
    args = p.parse_args(argv)

    if not args.transcript.exists():
        print(f"Missing transcript: {args.transcript}", file=sys.stderr)
        return 2

    lab = generate_lab(args.transcript, args.out, args.slug)
    print(f"Created lab: {lab}")
    for child in sorted(lab.rglob("*")):
        if child.is_file():
            print(f"  - {child.relative_to(lab)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
