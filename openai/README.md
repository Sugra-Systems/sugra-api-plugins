# sugra-api for ChatGPT and Codex

Official Sugra API plugin. HTTPS and MCP. Agent Plugins 1.0.0 package: `plugin.json` (with `extensions.com.openai`), `mcp.json` (not in a `--skills-only` ZIP), `skills/`, `assets/`.

```
codex plugin marketplace add Sugra-Systems/sugra-api-plugins
codex plugin add sugra-api@sugra-api-plugins
```

The Plugins Directory package is a ZIP of this folder without this README, built by `python scripts/build_openai_zip.py --source <clone of sugra-api-skills>`; with `--skills-only` the ZIP also leaves `mcp.json` out.

`mcp.json` connects the Sugra API MCP server at `https://app.sugra.ai/mcp` (`streamable-http`). Without it, as in a `--skills-only` ZIP, add that server as a hosted connector instead.

The skills are copied from [sugra-api-skills](https://github.com/Sugra-Systems/sugra-api-skills) by `scripts/sync.py`; edit them there. `agents/openai.yaml` in each skill belongs to this package and is edited here.

Documentation: https://docs.sugra.ai
