"""Copy the Sugra API skills into every vendor package. Stdlib only.

The skills are edited in https://github.com/Sugra-Systems/sugra-api-skills
only. skills-source.json pins the commit of that repository the packages copy.
The copy is read from git objects at that commit, never from a working tree.
Each package gets a real copy: plugin folders reject symlinks and paths outside
the package folder.

    python scripts/sync.py --source <clone> [--commit <sha>]
        copy the skills at that commit (default: the pinned one) and pin it
    python scripts/sync.py --source <clone> --check
        exit 1 when a package differs from the pinned commit

<clone> is any clone of sugra-api-skills that holds the commit.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
PIN = ROOT / "skills-source.json"
SOURCE_REPOSITORY = "Sugra-Systems/sugra-api-skills"
# package folder -> files inside a skill folder the package owns (never copied, never removed)
PACKAGES = {
    "anthropic": (),
    "openai": ("agents/openai.yaml",),
    "xai": (),
}
SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def is_link(path: Path) -> bool:
    return path.is_symlink() or path.is_junction()


def guard(path: Path) -> None:
    """Refuse a path outside the repository or one reached through a link."""
    try:
        rel = path.relative_to(ROOT)
    except ValueError:
        raise SystemExit(f"FAIL {path}: outside the repository") from None
    current = ROOT
    for part in rel.parts:
        current = current / part
        if is_link(current):
            raise SystemExit(f"FAIL {current.relative_to(ROOT).as_posix()}: symlink")
    if path.exists() and not path.resolve().is_relative_to(ROOT):
        raise SystemExit(f"FAIL {rel.as_posix()}: resolves outside the repository")


def refuse_links(base: Path) -> None:
    """Fail when base, or anything under it, is a link or not a plain file or folder."""
    guard(base)
    if not base.exists():
        return
    for path in [base, *sorted(base.rglob("*"))]:
        rel = path.relative_to(ROOT).as_posix()
        if is_link(path):
            raise SystemExit(f"FAIL {rel}: symlink")
        if not (path.is_file() or path.is_dir()):
            raise SystemExit(f"FAIL {rel}: not a regular file")


def replace_file(dest: Path, data: bytes) -> None:
    """Write through a new file in the same folder, so a hard-linked dest is never written into."""
    fd, tmp = tempfile.mkstemp(dir=dest.parent, prefix=".sync-")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
        os.chmod(tmp, 0o644)
        os.replace(tmp, dest)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


def pinned() -> str:
    guard(PIN)
    data = json.loads(PIN.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        data = {}
    commit = data.get("commit")
    if data.get("repository") != SOURCE_REPOSITORY or not isinstance(commit, str) or not SHA_RE.match(commit):
        raise SystemExit(f"FAIL skills-source.json must name {SOURCE_REPOSITORY} and a full commit sha")
    return commit


def source_git(source: Path, *args: str) -> bytes:
    run = subprocess.run(["git", "-C", str(source), *args], capture_output=True)
    if run.returncode != 0:
        raise SystemExit(f"FAIL git {' '.join(args)} in {source}: {run.stderr.decode(errors='replace').strip()}")
    return run.stdout


def source_files(source: Path, commit: str) -> dict[str, bytes]:
    """Every file of every skill folder at the root of sugra-api-skills at commit: skill/path -> bytes.

    A skill folder is a top-level folder with a SKILL.md directly inside it.
    """
    if not SHA_RE.match(commit):
        raise SystemExit(f"FAIL {commit!r} is not a full commit sha")
    source_git(source, "cat-file", "-e", f"{commit}^{{commit}}")
    entries = []
    for entry in source_git(source, "ls-tree", "-r", "-z", "--full-tree", commit).split(b"\0"):
        if not entry:
            continue
        meta, raw = entry.split(b"\t", 1)
        mode, kind, blob = meta.decode().split()
        entries.append((raw.decode("utf-8"), mode, kind, blob))
    skills = {path.split("/")[0] for path, *_ in entries if re.fullmatch(r"[^/]+/SKILL\.md", path)}
    if not skills:
        raise SystemExit(f"FAIL no skill folders at the root of {commit}")
    out = {}
    for path, mode, kind, blob in entries:
        if path.split("/")[0] not in skills:
            continue
        if kind != "blob" or mode not in ("100644", "100755"):
            raise SystemExit(f"FAIL {path} at {commit}: mode {mode} is not a regular file")
        out[path] = source_git(source, "cat-file", "blob", blob)
    return out


def owned(rel: str, owned_paths: tuple[str, ...]) -> bool:
    """rel is skill/path; owned_paths name paths inside a skill folder."""
    return PurePosixPath(*PurePosixPath(rel).parts[1:]).as_posix() in owned_paths


def package_files(package: str) -> dict[str, bytes]:
    base = ROOT / package / "skills"
    guard(base)
    if not base.is_dir():
        return {}
    out = {}
    for path in sorted(base.rglob("*")):
        if is_link(path):
            raise SystemExit(f"FAIL {path.relative_to(ROOT).as_posix()}: symlink")
        if path.is_file():
            out[path.relative_to(base).as_posix()] = path.read_bytes()
    return out


def drift(want: dict[str, bytes]) -> list[str]:
    problems = []
    skills = {rel.split("/")[0] for rel in want}
    for package, owned_paths in PACKAGES.items():
        files = package_files(package)
        # every skill carries each file the package owns, and no owned file outlives its skill
        for skill in sorted(skills):
            for path in owned_paths:
                if f"{skill}/{path}" not in files:
                    problems.append(f"missing {package}/skills/{skill}/{path}, which {package} owns")
        for rel in sorted(files):
            if owned(rel, owned_paths) and rel.split("/")[0] not in skills:
                problems.append(f"extra {package}/skills/{rel}: no such skill in the source")
        have = {rel: data for rel, data in files.items() if not owned(rel, owned_paths)}
        for rel in sorted(want.keys() | have.keys()):
            label = f"{package}/skills/{rel}"
            if rel in want and owned(rel, owned_paths):
                problems.append(f"source carries {rel}, which {package} owns")
            elif rel not in have:
                problems.append(f"missing {label}")
            elif rel not in want:
                problems.append(f"extra {label}")
            elif have[rel] != want[rel]:
                problems.append(f"differs {label}")
    return problems


def write(want: dict[str, bytes], commit: str) -> None:
    for package, owned_paths in PACKAGES.items():
        clash = sorted(rel for rel in want if owned(rel, owned_paths))
        if clash:
            raise SystemExit(f"FAIL source carries {clash[0]}, which {package} owns")
    for package, owned_paths in PACKAGES.items():
        target = ROOT / package / "skills"
        have = package_files(package)
        for rel in sorted(have.keys() - want.keys()):
            if owned(rel, owned_paths):
                continue
            dest = target / rel
            guard(dest)
            dest.unlink()
            print(f"removed {package}/skills/{rel}")
        for rel, data in want.items():
            if have.get(rel) != data:
                dest = target / rel
                guard(dest.parent)
                dest.parent.mkdir(parents=True, exist_ok=True)
                guard(dest)
                replace_file(dest, data)
                print(f"wrote {package}/skills/{rel}")
        for folder in sorted(target.rglob("*"), reverse=True):
            if folder.is_dir() and not any(folder.iterdir()):
                folder.rmdir()
    pin = json.dumps({"repository": SOURCE_REPOSITORY, "commit": commit}, indent=2) + "\n"
    guard(PIN)
    replace_file(PIN, pin.encode())
    print(f"pinned {SOURCE_REPOSITORY} {commit}")


def parse(argv: list[str]) -> tuple[Path, str | None, bool]:
    args = argv[1:]
    source, commit, check = None, None, False
    while args:
        flag = args.pop(0)
        if flag == "--check":
            check = True
        elif flag in ("--source", "--commit") and args:
            value = args.pop(0)
            if flag == "--source":
                source = Path(value)
            else:
                commit = value
        else:
            source = None
            break
    if source is None or (check and commit):
        print(__doc__, file=sys.stderr)
        raise SystemExit(2)
    return source, commit, check


def main(argv: list[str]) -> int:
    source, commit, check = parse(argv)
    if check:
        problems = drift(source_files(source, pinned()))
        for line in problems:
            print(f"FAIL {line}", file=sys.stderr)
        if problems:
            print("FAIL edit the skills in sugra-api-skills, then run python scripts/sync.py", file=sys.stderr)
            return 1
        print("ok packages match the pinned skills")
        return 0
    commit = commit or pinned()
    write(source_files(source, commit), commit)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
