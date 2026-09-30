"""Build the OpenAI Plugins Directory ZIP from openai/. Stdlib only.

    python scripts/build_openai_zip.py --source <clone>                 package with mcp.json
    python scripts/build_openai_zip.py --source <clone> --skills-only   package without mcp.json

<clone> is a clone of sugra-api-skills that holds the pinned commit.

The ZIP holds the files committed at HEAD, never the working tree. The builder
refuses while openai/ or skills-source.json differ from HEAD (untracked files
included) and while the package skills differ from the pinned sugra-api-skills
commit. It names both commits in the archive comment and this repository's
commit in the file name. Entries are stored uncompressed with a fixed date,
mode and host, so one commit gives one ZIP, byte for byte.
"""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import sync
from check import LISTING_LIMITS, MANIFEST_LIMITS

ROOT = sync.ROOT
PACKAGE = "openai"
DIST = ROOT / "dist"


def git(*args: str) -> bytes:
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True).stdout


def tree(prefix: str) -> dict[str, str]:
    """Regular files under prefix at HEAD: path relative to prefix -> blob id."""
    out = {}
    for entry in git("ls-tree", "-r", "-z", "--full-tree", "HEAD", "--", prefix).split(b"\0"):
        if not entry:
            continue
        meta, raw = entry.split(b"\t", 1)
        mode, kind, blob = meta.decode().split()
        path = raw.decode("utf-8")
        if kind != "blob" or mode not in ("100644", "100755"):
            raise SystemExit(f"FAIL {path}: mode {mode} is not a regular file")
        out[path[len(prefix) + 1 :]] = blob
    return out


def main(argv: list[str]) -> int:
    args = argv[1:]
    skills_only = "--skills-only" in args
    if skills_only:
        args.remove("--skills-only")
    if len(args) != 2 or args[0] != "--source":
        print(__doc__, file=sys.stderr)
        return 2
    source = Path(args[1])
    dirty = git("status", "--porcelain", "--untracked-files=all", "--", PACKAGE, "skills-source.json")
    if dirty:
        print(f"FAIL commit {PACKAGE}/ and skills-source.json first:\n" + dirty.decode(), file=sys.stderr)
        return 1
    commit = git("rev-parse", "HEAD").decode().strip()
    pin = sync.strict_json(git("show", "HEAD:skills-source.json"), "skills-source.json at HEAD")
    skills_commit = pin.get("commit") if isinstance(pin, dict) else None
    if skills_commit != sync.pinned():
        print("FAIL skills-source.json at HEAD differs from the working tree", file=sys.stderr)
        return 1

    package = tree(PACKAGE)
    owned_paths = sync.PACKAGES[PACKAGE]
    want = {rel: data for rel, data in sync.source_files(source, skills_commit).items()}
    have = {
        rel[len("skills/") :]: git("cat-file", "blob", blob)
        for rel, blob in package.items()
        if rel.startswith("skills/") and not sync.owned(rel[len("skills/") :], owned_paths)
    }
    if want != have:
        for rel in sorted(want.keys() | have.keys()):
            if want.get(rel) != have.get(rel):
                print(f"FAIL {PACKAGE}/skills/{rel} differs from sugra-api-skills {skills_commit}", file=sys.stderr)
        print("FAIL run python scripts/sync.py and commit", file=sys.stderr)
        return 1

    manifest = sync.strict_json(git("cat-file", "blob", package["plugin.json"]), "openai/plugin.json")
    interface = manifest.get("extensions", {}).get("com.openai", {}).get("interface", {})
    fields = [(field, manifest.get(field), limit) for field, limit in MANIFEST_LIMITS.items()]
    fields += [(f"interface.{field}", interface.get(field), limit) for field, limit in LISTING_LIMITS.items()]
    for field, value, limit in fields:
        if not isinstance(value, str) or not value.strip():
            print(f"FAIL plugin.json {field} must be a non-empty string", file=sys.stderr)
            return 1
        if len(value) > limit:
            print(f"FAIL plugin.json {field} is {len(value)} chars; the directory allows {limit}", file=sys.stderr)
            return 1

    names = sorted(rel for rel in package if rel != "README.md" and not (skills_only and rel == "mcp.json"))
    suffix = "-skills-only" if skills_only else ""
    # dist/ is ignored, so nothing reviewed it: refuse a link or a path that leaves the repository
    sync.guard(DIST)
    DIST.mkdir(exist_ok=True)
    sync.refuse_links(DIST)
    out = DIST / f"sugra-api-openai-{manifest['version']}{suffix}-{commit[:12]}.zip"
    sync.inside(out, DIST)
    sync.guard(out)
    # a new file renamed over out, so an existing link or hard link at out is replaced, never written through
    fd, tmp = tempfile.mkstemp(dir=DIST, prefix=".zip-")
    try:
        with os.fdopen(fd, "wb") as handle, zipfile.ZipFile(handle, "w", zipfile.ZIP_STORED) as archive:
            archive.comment = (
                f"Sugra-Systems/sugra-api-plugins {commit} {PACKAGE}; "
                f"skills {sync.SOURCE_REPOSITORY} {skills_commit}"
            ).encode()
            for rel in names:
                info = zipfile.ZipInfo(rel, date_time=(1980, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.external_attr = 0o644 << 16
                info.compress_type = zipfile.ZIP_STORED
                archive.writestr(info, git("cat-file", "blob", package[rel]))
        os.chmod(tmp, 0o644)
        os.replace(tmp, out)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise
    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    print(out.relative_to(ROOT).as_posix())
    print(f"version {manifest['version']} commit {commit} skills {skills_commit} files {len(names)} sha256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
