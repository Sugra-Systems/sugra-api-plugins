# sugra-api-plugins

<p align="center">
  <img src="https://app.sugra.ai/images/brand/sugra-app-icon.svg" alt="sugra.ai" width="112" height="112" />
</p>

<p align="center">
  <a href="https://chatgpt.com/plugins/plugins_6aa4f7db79848191a81e4048990545ef"><img src="https://img.shields.io/badge/ChatGPT-Plugins_Directory-F5A623" alt="ChatGPT Plugins Directory"></a>
  <a href="https://github.com/Sugra-Systems/sugra-api-plugins/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Sugra-Systems/sugra-api-plugins?label=License" alt="License"></a>
</p>

Official [Sugra API](https://sugra.ai) plugins for Claude, ChatGPT and Codex, and Grok: one folder per vendor. Each plugin bundles the Sugra API skills and connects the hosted Sugra API MCP server.

| Repository | What |
|---|---|
| [sugra-api-skills](https://github.com/Sugra-Systems/sugra-api-skills) | the skills, edited there only |
| [sugra-api-mcp](https://github.com/Sugra-Systems/sugra-api-mcp) | the MCP server |
| sugra-api-plugins (this one) | the vendor packages |

## Install

Get a key at [app.sugra.ai/settings/billing](https://app.sugra.ai/settings/billing) (Free: 50 requests/day).

### Claude Code

```
/plugin marketplace add Sugra-Systems/sugra-api-plugins
/plugin install sugra-api@sugra-api-plugins
```

### Codex

```
codex plugin marketplace add Sugra-Systems/sugra-api-plugins
codex plugin add sugra-api@sugra-api-plugins
```

### ChatGPT

Listed in the Plugins Directory (Install plugin):

```
https://chatgpt.com/plugins/plugins_6aa4f7db79848191a81e4048990545ef
```

### Grok

```
grok plugin marketplace add Sugra-Systems/sugra-api-plugins
grok plugin install sugra-api@sugra-api-plugins --trust
```

Or the folder directly: `grok plugin install Sugra-Systems/sugra-api-plugins#xai --trust`.

### Other agents

Cursor, Gemini CLI and any client that reads Agent Skills: copy the skills from [sugra-api-skills](https://github.com/Sugra-Systems/sugra-api-skills) and connect the hosted MCP server, `https://mcp.sugra.ai`.

## Layout

| Folder | Vendor | Marketplace file |
|---|---|---|
| `anthropic/` | Claude Code, Anthropic plugin directory | `.claude-plugin/marketplace.json` |
| `openai/` | Codex, ChatGPT Plugins Directory | `.agents/plugins/marketplace.json` |
| `xai/` | Grok | `.grok-plugin/marketplace.json` |

Each package holds only its own vendor's files and versions on its own. The skills in `*/skills/` are copies of one commit of sugra-api-skills, named in `skills-source.json`; edit them there, never here.

## Local check

```
python scripts/sync.py --source <clone of sugra-api-skills> --commit <commit on its main>
python scripts/check.py --source <clone of sugra-api-skills>
```

Documentation: [https://docs.sugra.ai](https://docs.sugra.ai)

## License

MIT. Data from each endpoint carries its own upstream terms.
