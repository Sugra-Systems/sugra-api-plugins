# Sugra API Skills for ChatGPT and Codex

Sugra API Skills plugin, skills only. Agent Plugins 1.0.0 package: `plugin.json` (with `extensions.com.openai`), `skills/`, `assets/`.

```
codex plugin marketplace add Sugra-Systems/sugra-api-plugins
codex plugin add sugra-api-skills@sugra-api-plugins
```

The Plugins Directory package is a ZIP of this folder without this README, built by `python scripts/build_openai_zip.py --source <clone of sugra-api-skills>`.

The Sugra API MCP server is a separate product: the Sugra API app in ChatGPT, or the hosted server for Codex, https://docs.sugra.ai/doc-2263382.

The skills are copied from [sugra-api-skills](https://github.com/Sugra-Systems/sugra-api-skills) by `scripts/sync.py`; edit them there. `agents/openai.yaml` in each skill belongs to this package and is edited here.

Documentation: https://docs.sugra.ai
