"""Stdlib checks for the Sugra API plugin packages. No third-party deps.

    python scripts/check.py --source <clone of sugra-api-skills>

The clone must hold the pinned commit and the main branch of sugra-api-skills.
"""

from __future__ import annotations

import html
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import sync

ROOT = sync.ROOT
REPOSITORY = "https://github.com/Sugra-Systems/sugra-api-plugins"
MARKETPLACE = "sugra-api-plugins"
# each package releases on its own; bump only the package that changed
VERSIONS = {"anthropic": "1.2.0", "openai": "1.2.0", "xai": "1.2.0"}
MCP_URL = "https://app.sugra.ai/mcp"
AGENT_PLUGINS = "https://agent-plugins.org/schemas/1.0.0/"
CHATGPT_LISTING = "chatgpt.com/plugins/plugins_6aa4f7db79848191a81e4048990545ef"
# Everything a package may hold at its top level. A vendor reads the first
# manifest it knows, so another vendor's file in a package is an error.
LAYOUT = {
    "anthropic": {".claude-plugin", ".mcp.json", "README.md", "skills"},
    "openai": {"README.md", "assets", "mcp.json", "plugin.json", "skills"},
    "xai": {".grok-plugin", ".mcp.json", "README.md", "skills"},
}
TIER_C = (
    "yahoo",
    "finnhub",
    "coingecko",
    "tomorrow.io",
    "alpha vantage",
    "polygon",
    "tiingo",
    "cboe",
)
BANS = ("real-time", "realtime", "financial intelligence", "blackbox")
# The copy rules ban the em dash (a hyphen is the only dash) and emoji, not Unicode as such.
# Written as code points so this file stays plain ASCII. Banned: the dashes other than the
# hyphen and the keycap; IGNORABLE_RANGES; and EMOJI_RANGES. A character outside them that
# Unicode also lists as emoji (a copyright sign, a check mark) renders as text, because the
# selector that would turn it into an emoji is banned.
BANNED_POINTS = (0x2013, 0x2014, 0x2015, 0x20E3)
# Every Default_Ignorable_Code_Point of DerivedCoreProperties.txt, Unicode 18.0.0: characters a
# reader does not see (zero-width characters, joiners, bidi controls, variation selectors, tag
# characters). Invisible text has no place in a public file, so each one fails as a class; this
# also covers the joiner, selectors and tags that build or force an emoji.
IGNORABLE_RANGES = (
    (0x00AD, 0x00AD), (0x034F, 0x034F), (0x061C, 0x061C), (0x115F, 0x1160), (0x17B4, 0x17B5),
    (0x180B, 0x180F), (0x200B, 0x200F), (0x202A, 0x202E), (0x2060, 0x206F), (0x3164, 0x3164),
    (0xFE00, 0xFE0F), (0xFEFF, 0xFEFF), (0xFFA0, 0xFFA0), (0xFFF0, 0xFFF8), (0x1BCA0, 0x1BCA3),
    (0x1D173, 0x1D17A), (0xE0000, 0xE0FFF),
)
# From emoji-data.txt, Unicode 18.0.0: every Emoji_Presentation character (shown as an emoji by
# default), plus Extended_Pictographic above U+FFFF, which also reserves the unassigned points
# where later emoji will be encoded, so an emoji newer than this table still fails.
EMOJI_RANGES = (
    (0x231A, 0x231B), (0x23E9, 0x23EC), (0x23F0, 0x23F0), (0x23F3, 0x23F3), (0x25FD, 0x25FE),
    (0x2614, 0x2615), (0x2648, 0x2653), (0x267F, 0x267F), (0x2693, 0x2693), (0x26A1, 0x26A1),
    (0x26AA, 0x26AB), (0x26BD, 0x26BE), (0x26C4, 0x26C5), (0x26CE, 0x26CE), (0x26D4, 0x26D4),
    (0x26EA, 0x26EA), (0x26F2, 0x26F3), (0x26F5, 0x26F5), (0x26FA, 0x26FA), (0x26FD, 0x26FD),
    (0x2705, 0x2705), (0x270A, 0x270B), (0x2728, 0x2728), (0x274C, 0x274C), (0x274E, 0x274E),
    (0x2753, 0x2755), (0x2757, 0x2757), (0x2795, 0x2797), (0x27B0, 0x27B0), (0x27BF, 0x27BF),
    (0x2B1B, 0x2B1C), (0x2B50, 0x2B50), (0x2B55, 0x2B55), (0x1F004, 0x1F004), (0x1F02C, 0x1F02F),
    (0x1F094, 0x1F09F), (0x1F0AF, 0x1F0B0), (0x1F0C0, 0x1F0C0), (0x1F0CF, 0x1F0D0),
    (0x1F0F6, 0x1F0FF), (0x1F170, 0x1F171), (0x1F17E, 0x1F17F), (0x1F18E, 0x1F18E),
    (0x1F191, 0x1F19A), (0x1F1AF, 0x1F1FF), (0x1F201, 0x1F20F), (0x1F21A, 0x1F21A),
    (0x1F22F, 0x1F22F), (0x1F232, 0x1F23A), (0x1F23C, 0x1F23F), (0x1F249, 0x1F25F),
    (0x1F266, 0x1F321), (0x1F324, 0x1F393), (0x1F396, 0x1F397), (0x1F399, 0x1F39B),
    (0x1F39E, 0x1F3F0), (0x1F3F3, 0x1F3F5), (0x1F3F7, 0x1F4FD), (0x1F4FF, 0x1F53D),
    (0x1F549, 0x1F54E), (0x1F550, 0x1F567), (0x1F56F, 0x1F570), (0x1F573, 0x1F57A),
    (0x1F587, 0x1F587), (0x1F58A, 0x1F58D), (0x1F590, 0x1F590), (0x1F595, 0x1F596),
    (0x1F5A4, 0x1F5A5), (0x1F5A8, 0x1F5A8), (0x1F5B1, 0x1F5B2), (0x1F5BC, 0x1F5BC),
    (0x1F5C2, 0x1F5C4), (0x1F5D1, 0x1F5D3), (0x1F5DC, 0x1F5DE), (0x1F5E1, 0x1F5E1),
    (0x1F5E3, 0x1F5E3), (0x1F5E8, 0x1F5E8), (0x1F5EF, 0x1F5EF), (0x1F5F3, 0x1F5F3),
    (0x1F5FA, 0x1F64F), (0x1F680, 0x1F6C5), (0x1F6CB, 0x1F6D2), (0x1F6D5, 0x1F6E5),
    (0x1F6E9, 0x1F6E9), (0x1F6EB, 0x1F6F0), (0x1F6F3, 0x1F6FF), (0x1F7DC, 0x1F7F0),
    (0x1F80C, 0x1F80F), (0x1F848, 0x1F84F), (0x1F85A, 0x1F85F), (0x1F888, 0x1F88F),
    (0x1F8AE, 0x1F8AF), (0x1F8BC, 0x1F8BF), (0x1F8C2, 0x1F8CF), (0x1F8D9, 0x1F8FF),
    (0x1F90C, 0x1F93A), (0x1F93C, 0x1F945), (0x1F947, 0x1F9FF), (0x1FA58, 0x1FA5F),
    (0x1FA6E, 0x1FAFF), (0x1FC00, 0x1FFFD),
)
FORBIDDEN = re.compile(
    "["
    + "".join(chr(point) for point in BANNED_POINTS)
    + "".join(f"{chr(low)}-{chr(high)}" for low, high in IGNORABLE_RANGES + EMOJI_RANGES)
    + "]"
)
# Every other file a vendor or a reader sees is UTF-8 text and passes copy_lint.
BINARY = {".png": b"\x89PNG\r\n\x1a\n"}
PUBLIC_FILES = ("README.md", "SECURITY.md", "LICENSE")
PUBLIC = ("anthropic", "openai", "xai", ".claude-plugin", ".grok-plugin", ".agents", *PUBLIC_FILES)
# Final Plugins Directory submission limits, from developers.openai.com/plugins/deploy/submission-errors.
MANIFEST_LIMITS = {"name": 64, "description": 1024}
LISTING_LIMITS = {"displayName": 30, "shortDescription": 30, "longDescription": 4000, "developerName": 80}
# openai.yaml is written in one shape: "interface:" then two-space fields holding a quoted string.
YAML_KEYS = ("display_name", "short_description", "icon_small", "icon_large", "brand_color", "default_prompt")
YAML_FIELD = re.compile(r'  ([a-z_]+): "([^"\\]*)"')


def fail(msg: str) -> None:
    print(f"FAIL {msg}", file=sys.stderr)
    raise SystemExit(1)


def views(text: str) -> tuple[str, str, str]:
    """The text as written; with HTML character references decoded; and that decoded text with format
    characters removed and NFKC folding applied.

    The copy lint checks honest text in these three views. It does not render Markdown or HTML, so a
    word split by markup inside the word is outside its scope: it is not a filter against an author
    who hides a word on purpose."""
    shown = html.unescape(text)
    read = unicodedata.normalize("NFKC", "".join(char for char in shown if unicodedata.category(char) != "Cf"))
    return text, shown, read


def copy_lint(text: str, label: str) -> None:
    for view in views(text):
        found = FORBIDDEN.search(view)
        if found:
            fail(f"{label}: U+{ord(found.group()):04X} is a banned dash, emoji or invisible character")
        lowered = view.lower()
        for ban in BANS:
            if ban in lowered:
                fail(f"{label}: banned phrase {ban}")
        for fragment in TIER_C:
            if fragment in lowered:
                fail(f"{label}: commercial name {fragment}")


def load_json(path: Path) -> dict:
    label = path.relative_to(ROOT).as_posix()
    if not path.is_file():
        fail(f"{label} missing")
    try:
        text = path.read_text(encoding="utf-8")
    except ValueError as exc:
        fail(f"{label}: {exc}")
    data = sync.strict_json(text, label)
    if not isinstance(data, dict):
        fail(f"{label} must be a JSON object")
    return data


def check_manifest(manifest: dict, package: str) -> None:
    """Fields every package manifest carries, whatever its vendor requires."""
    for field in ("name", "version", "description", "homepage", "repository", "license"):
        value = manifest.get(field)
        if not isinstance(value, str) or not value.strip():
            fail(f"{package} manifest: {field} must be a non-empty string")
    if manifest["name"] != "sugra-api" or manifest["version"] != VERSIONS[package]:
        fail(f"{package} manifest: name must be sugra-api and version {VERSIONS[package]}")
    if manifest["homepage"] != "https://docs.sugra.ai" or manifest["repository"] != REPOSITORY:
        fail(f"{package} manifest: homepage must be https://docs.sugra.ai and repository {REPOSITORY}")
    if manifest["license"] != "MIT":
        fail(f"{package} manifest: license must be MIT")
    author = manifest.get("author")
    if not isinstance(author, dict) or author.get("name") != "Sugra Systems, Inc.":
        fail(f"{package} manifest: author.name must be Sugra Systems, Inc.")


def check_mcp(conf: dict, kind: str, label: str) -> None:
    servers = conf.get("mcpServers")
    if not isinstance(servers, dict) or list(servers) != ["sugra-api"] or servers["sugra-api"] != {"type": kind, "url": MCP_URL}:
        fail(f"{label} must define only sugra-api as type {kind} at {MCP_URL}")


def check_layout() -> None:
    for package, allowed in LAYOUT.items():
        base = ROOT / package
        if not base.is_dir():
            fail(f"{package}/ missing")
        present = {path.name for path in base.iterdir()}
        if present != allowed:
            extra, missing = sorted(present - allowed), sorted(allowed - present)
            fail(f"{package}/ must hold exactly {sorted(allowed)} (extra {extra}, missing {missing})")


def check_source(source: Path) -> None:
    commit = sync.pinned()
    main_ref = None
    for ref in ("refs/remotes/origin/main", "refs/heads/main"):
        found = subprocess.run(["git", "-C", str(source), "rev-parse", "--verify", "--quiet", ref], capture_output=True)
        if found.returncode == 0:
            main_ref = ref
            break
    if main_ref is None:
        fail(f"{source} holds no main branch of {sync.SOURCE_REPOSITORY}")
    on_main = subprocess.run(["git", "-C", str(source), "merge-base", "--is-ancestor", commit, main_ref], capture_output=True)
    if on_main.returncode != 0:
        fail(f"pinned commit {commit} is not on {sync.SOURCE_REPOSITORY} main; pin a merged commit")
    problems = sync.drift(sync.source_files(source, commit))
    if problems:
        fail(f"packages differ from the pinned skills ({problems[0]}); run python scripts/sync.py")


def check_packages() -> None:
    anthropic = ROOT / "anthropic"
    claude_plugin = load_json(anthropic / ".claude-plugin" / "plugin.json")
    check_manifest(claude_plugin, "anthropic")
    if claude_plugin.get("privacyPolicyUrl") != "https://sugra.systems/privacy-policy":
        fail("anthropic manifest: privacyPolicyUrl must be https://sugra.systems/privacy-policy")
    if claude_plugin.get("skills") not in ("./skills", "./skills/"):
        fail("anthropic manifest: skills must be ./skills")
    if sorted(p.name for p in (anthropic / ".claude-plugin").iterdir()) != ["plugin.json"]:
        fail("anthropic/.claude-plugin must hold only plugin.json")
    check_mcp(load_json(anthropic / ".mcp.json"), "http", "anthropic/.mcp.json")

    openai = ROOT / "openai"
    portable = load_json(openai / "plugin.json")
    check_manifest(portable, "openai")
    if portable.get("$schema") != AGENT_PLUGINS + "plugin.schema.json":
        fail("openai/plugin.json must declare the Agent Plugins schema")
    if "skills" in portable:
        fail("openai/plugin.json must not declare skills; skills/ is discovered")
    interface = ((portable.get("extensions") or {}).get("com.openai") or {}).get("interface") or {}
    if interface.get("composerIcon") != "./assets/logo.png" or interface.get("logo") != "./assets/logo.png":
        fail("openai/plugin.json: interface icons must be ./assets/logo.png")
    for field in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        value = interface.get(field)
        if not isinstance(value, str) or not value.strip():
            fail(f"openai/plugin.json: interface.{field} must be a non-empty string")
    for field, limit in MANIFEST_LIMITS.items():
        if len(portable[field]) > limit:
            fail(f"openai/plugin.json: {field} is over the {limit} characters the directory allows")
    for field, limit in LISTING_LIMITS.items():
        if len(interface[field]) > limit:
            fail(f"openai/plugin.json: interface.{field} is over the {limit} characters the directory allows")
    if sorted(p.name for p in (openai / "assets").iterdir()) != ["logo.png"]:
        fail("openai/assets must hold only logo.png")
    openai_mcp = load_json(openai / "mcp.json")
    if set(openai_mcp) != {"$schema", "mcpServers"} or openai_mcp["$schema"] != AGENT_PLUGINS + "mcp.schema.json":
        fail("openai/mcp.json must hold only the Agent Plugins $schema and mcpServers")
    check_mcp(openai_mcp, "streamable-http", "openai/mcp.json")
    for skill in sorted(p for p in (openai / "skills").iterdir() if p.is_dir()):
        yaml_path = skill / "agents" / "openai.yaml"
        label = yaml_path.relative_to(ROOT).as_posix()
        if not yaml_path.is_file():
            fail(f"{label} missing")
        parse_openai_yaml(yaml_path.read_text(encoding="utf-8"), label)

    xai = ROOT / "xai"
    grok_plugin = load_json(xai / ".grok-plugin" / "plugin.json")
    check_manifest(grok_plugin, "xai")
    if sorted(p.name for p in (xai / ".grok-plugin").iterdir()) != ["plugin.json"]:
        fail("xai/.grok-plugin must hold only plugin.json")
    check_mcp(load_json(xai / ".mcp.json"), "http", "xai/.mcp.json")


def parse_openai_yaml(text: str, label: str) -> dict[str, str]:
    """Read openai.yaml in the one shape this repository writes; anything else fails."""
    lines = text.split("\n")
    if lines[0] != "interface:" or lines[-1] != "":
        fail(f"{label} must start with interface: and end with a newline")
    fields: dict[str, str] = {}
    for line in lines[1:-1]:
        match = YAML_FIELD.fullmatch(line)
        if not match or match[1] not in YAML_KEYS or match[1] in fields:
            fail(f"{label}: {line!r} is not an interface field written as '  key: \"value\"'")
        fields[match[1]] = match[2]
    for key in ("display_name", "short_description"):
        if not fields.get(key, "").strip():
            fail(f"{label}: interface.{key} must be a non-empty string")
    return fields


def check_copy() -> None:
    """Copy rules over every public file in each of its views; JSON, parsed strictly, also as its decoded strings."""
    for name in PUBLIC:
        base = ROOT / name
        if not (base.is_file() if name in PUBLIC_FILES else base.is_dir()):
            fail(f"{name} missing")
        for path in [base] if base.is_file() else sorted(p for p in base.rglob("*") if p.is_file()):
            label = path.relative_to(ROOT).as_posix()
            data = path.read_bytes()
            magic = BINARY.get(path.suffix.lower())
            if magic is not None:
                if not data.startswith(magic):
                    fail(f"{label}: not a {path.suffix.lower()} file")
                continue
            try:
                text = data.decode("utf-8")
            except UnicodeDecodeError:
                fail(f"{label}: not UTF-8 text; only {sorted(BINARY)} files may be binary")
            copy_lint(text, label)
            if path.suffix.lower() == ".json":
                copy_lint(json.dumps(sync.strict_json(text, label), ensure_ascii=False), label)


def check_marketplaces() -> None:
    claude = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    grok = load_json(ROOT / ".grok-plugin" / "marketplace.json")
    codex = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    for label, market in (("claude", claude), ("grok", grok), ("codex", codex)):
        plugins = market.get("plugins")
        if market.get("name") != MARKETPLACE or not isinstance(plugins, list) or [p.get("name") for p in plugins] != ["sugra-api"]:
            fail(f"{label} marketplace must be {MARKETPLACE} listing only sugra-api")
    if claude["plugins"][0].get("source") != "./anthropic" or claude["plugins"][0].get("version") != VERSIONS["anthropic"]:
        fail("claude marketplace must point at ./anthropic with its version")
    if grok["plugins"][0].get("source") != {"type": "local", "path": "./xai"} or grok["plugins"][0].get("version") != VERSIONS["xai"]:
        fail("grok marketplace must point at ./xai with its version")
    if codex["plugins"][0].get("source") != {"source": "local", "path": "./openai"}:
        fail("codex marketplace must point at ./openai")
    policy = codex["plugins"][0].get("policy") or {}
    if policy.get("installation") != "AVAILABLE" or policy.get("authentication") != "ON_INSTALL":
        fail("codex marketplace plugin policy")


def check_docs() -> None:
    for package in LAYOUT:
        path = ROOT / package / "README.md"
        text = path.read_text(encoding="utf-8")
        if "scripts/sync.py" not in text or MCP_URL not in text:
            fail(f"{package}/README.md must name scripts/sync.py and {MCP_URL}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for needle in (
        "sugra-api@sugra-api-plugins",
        "Sugra-Systems/sugra-api-plugins#xai",
        "Sugra-Systems/sugra-api-skills",
        "docs.sugra.ai",
        CHATGPT_LISTING,
    ):
        if needle not in readme:
            fail(f"README.md must name {needle}")
    if "sugra.ai/stats" in readme or "`/stats`" in readme:
        fail("README.md must not point readers at /stats")
    # README.md links LICENSE and every manifest says MIT.
    license_file = ROOT / "LICENSE"
    if not license_file.is_file() or license_file.read_text(encoding="utf-8").splitlines()[:1] != ["MIT License"]:
        fail("LICENSE must be a file holding the MIT License")


def main(argv: list[str]) -> int:
    if len(argv) != 3 or argv[1] != "--source":
        print(__doc__, file=sys.stderr)
        return 2
    # Directories reject links, so every file this gate reads must be a plain file in the repository.
    for base in (
        *(ROOT / package for package in LAYOUT),
        ROOT / ".claude-plugin",
        ROOT / ".grok-plugin",
        ROOT / ".agents",
        ROOT / "README.md",
        ROOT / "SECURITY.md",
        ROOT / "LICENSE",
        sync.PIN,
    ):
        sync.refuse_links(base)
    check_layout()
    check_source(Path(argv[2]))
    check_packages()
    check_marketplaces()
    check_docs()
    check_copy()
    print("ok", ", ".join(LAYOUT), "packages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
