#!/usr/bin/env python3
"""Check whether a panorama has enough pixels for carousel slicing."""

from __future__ import annotations

import argparse
import struct
import sys
from pathlib import Path


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def read_png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as f:
        signature = f.read(8)
        if signature != PNG_SIGNATURE:
            raise ValueError("only PNG files are supported")
        length = struct.unpack(">I", f.read(4))[0]
        chunk_type = f.read(4)
        if chunk_type != b"IHDR" or length < 8:
            raise ValueError("invalid PNG IHDR chunk")
        width, height = struct.unpack(">II", f.read(8))
        return width, height


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Report whether a panorama is large enough for square carousel export."
    )
    parser.add_argument("--image", required=True, help="Path to the master PNG image")
    parser.add_argument("--slides", required=True, type=int, help="Number of square slides")
    parser.add_argument(
        "--export-size",
        required=True,
        type=int,
        help="Target slide size in pixels, e.g. 1080 for 1080x1080",
    )
    args = parser.parse_args()

    if args.slides <= 0:
        print("error: --slides must be positive", file=sys.stderr)
        return 2
    if args.export_size <= 0:
        print("error: --export-size must be positive", file=sys.stderr)
        return 2

    image = Path(args.image)
    if not image.exists():
        print(f"error: image not found: {image}", file=sys.stderr)
        return 2

    try:
        width, height = read_png_size(image)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    required_width = args.slides * args.export_size
    required_height = args.export_size
    width_ok = width >= required_width
    height_ok = height >= required_height
    status = "production-ready" if width_ok and height_ok else "concept-only"

    print(f"image: {image}")
    print(f"actual: {width}x{height}")
    print(f"required: {required_width}x{required_height}")
    print(f"slides: {args.slides}")
    print(f"export_size: {args.export_size}")
    print(f"status: {status}")

    if status != "production-ready":
        print(
            "note: use this image as a style reference or concept. "
            "Do not crop and upscale it as final carousel slides."
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
