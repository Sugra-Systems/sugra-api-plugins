"""Stdlib checks for the Sugra API plugin packages. No third-party deps.

    python scripts/check.py --source <clone of sugra-api-skills>

The clone must hold the pinned commit and the main branch of sugra-api-skills.
"""

from __future__ import annotations

import json
import subprocess
import sys
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


def fail(msg: str) -> None:
    print(f"FAIL {msg}", file=sys.stderr)
    raise SystemExit(1)


def copy_lint(text: str, label: str) -> None:
    if not text.isascii():
        fail(f"{label}: must be plain ASCII")
    lowered = text.lower()
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
        data = json.loads(path.read_text(encoding="utf-8"))
    except ValueError as exc:
        fail(f"{label}: {exc}")
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
    copy_lint(json.dumps(manifest), f"{package} manifest")


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
    if len(interface["displayName"]) > 30:
        fail("openai/plugin.json: interface.displayName is over the 30 characters the directory allows")
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
        yaml_text = yaml_path.read_text(encoding="utf-8")
        if "interface:" not in yaml_text or "display_name:" not in yaml_text:
            fail(f"{label} must declare interface.display_name")
        copy_lint(yaml_text, label)

    xai = ROOT / "xai"
    grok_plugin = load_json(xai / ".grok-plugin" / "plugin.json")
    check_manifest(grok_plugin, "xai")
    if sorted(p.name for p in (xai / ".grok-plugin").iterdir()) != ["plugin.json"]:
        fail("xai/.grok-plugin must hold only plugin.json")
    check_mcp(load_json(xai / ".mcp.json"), "http", "xai/.mcp.json")

    for package in LAYOUT:
        for path in sorted((ROOT / package / "skills").rglob("*.md")):
            copy_lint(path.read_text(encoding="utf-8"), path.relative_to(ROOT).as_posix())


def check_marketplaces() -> None:
    claude = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    grok = load_json(ROOT / ".grok-plugin" / "marketplace.json")
    codex = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    for label, market in (("claude", claude), ("grok", grok), ("codex", codex)):
        plugins = market.get("plugins")
        if market.get("name") != MARKETPLACE or not isinstance(plugins, list) or [p.get("name") for p in plugins] != ["sugra-api"]:
            fail(f"{label} marketplace must be {MARKETPLACE} listing only sugra-api")
        copy_lint(json.dumps(market), f"{label} marketplace")
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
        copy_lint(text, f"{package}/README.md")
        if "scripts/sync.py" not in text or MCP_URL not in text:
            fail(f"{package}/README.md must name scripts/sync.py and {MCP_URL}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    copy_lint(readme, "README.md")
    copy_lint((ROOT / "SECURITY.md").read_text(encoding="utf-8"), "SECURITY.md")
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
    print("ok", ", ".join(LAYOUT), "packages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
