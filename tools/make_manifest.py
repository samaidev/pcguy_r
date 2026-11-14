#!/usr/bin/env python3
"""Generate manifest.txt for the PCGuy download router (pcguy-online-installer.exe).

Usage:
    python make_manifest.py <version> <installer.exe>

    version    release version WITHOUT the leading "v", e.g. 1.3.61
    installer  path to PCGuy-setup-<version>.exe

Prints manifest.txt content (version, filename, size, sha256) to stdout.
After a new release, save the output to manifest.txt at the repo root,
commit it, and also upload the same installer to ModelScope
luoyunlan168/pcguy_r (the .github/workflows/update-manifest.yml workflow
updates GitHub automatically when a release is published).
"""
import hashlib
import os
import sys


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    ver = sys.argv[1].lstrip("v").strip()
    path = sys.argv[2]
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    name = path.replace("\\", "/").split("/")[-1]
    print(f"v{ver}\n{name}\n{os.path.getsize(path)}\n{h.hexdigest()}")


if __name__ == "__main__":
    main()
