# sugra-api-plugins

<p align="center">
  <img src="https://app.sugra.ai/images/brand/sugra-app-icon.svg" alt="sugra.ai" width="112" height="112" />
</p>

<p align="center">
  <a href="https://chatgpt.com/plugins/plugin_asdk_app_6a33ce728e488191a82df247ab605e91"><img src="https://img.shields.io/badge/ChatGPT-Plugins_Directory-F5A623" alt="ChatGPT Plugins Directory"></a>
  <a href="https://github.com/Sugra-Systems/sugra-api-plugins/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Sugra-Systems/sugra-api-plugins?label=License" alt="License"></a>
</p>

[Sugra API](https://sugra.ai) plugins for Claude, ChatGPT, Codex, Grok and Gemini CLI, one folder per vendor. Each plugin carries the Sugra API skills. The Claude plugin and the Gemini CLI extension also connect the hosted MCP server, and the ChatGPT listing holds that server beside the skills; the Codex and Grok plugins carry the skills only.

| Repository | What |
|---|---|
| [sugra-api-skills](https://github.com/Sugra-Systems/sugra-api-skills) | the skills, edited there only |
| [sugra-api-mcp](https://github.com/Sugra-Systems/sugra-api-mcp) | the MCP server |
| sugra-api-plugins (this one) | the vendor packages |

## Install

Get a key at [app.sugra.ai/register](https://app.sugra.ai/register) (Free: 50 requests/day).

### Claude Code

```
/plugin marketplace add Sugra-Systems/sugra-api-plugins
/plugin install sugra-api-skills@sugra-api-plugins
```

The plugin connects the hosted MCP server, `https://mcp.sugra.ai/mcp`: run `/mcp` and sign in with your Sugra account.

### Codex

```
codex plugin marketplace add Sugra-Systems/sugra-api-plugins
codex plugin add sugra-api-skills@sugra-api-plugins
```

### ChatGPT

Sugra API in the Plugins Directory, the hosted MCP server and these skills in one listing (Install plugin):

```
https://chatgpt.com/plugins/plugin_asdk_app_6a33ce728e488191a82df247ab605e91
```

### Grok

```
grok plugin install Sugra-Systems/sugra-api-plugins#xai
```

### Gemini CLI

```
gemini extensions install https://github.com/Sugra-Systems/sugra-api-plugins
```

The extension connects the hosted MCP server, `https://mcp.sugra.ai/mcp`: run `/mcp auth sugra-api` and sign in with your Sugra account.

### Other agents

Cursor and any client that reads Agent Skills: copy the skills from [sugra-api-skills](https://github.com/Sugra-Systems/sugra-api-skills) and connect the hosted MCP server, `https://mcp.sugra.ai/mcp`.

## Layout

| Folder | Vendor | Marketplace file |
|---|---|---|
| `anthropic/` | Claude Code, Anthropic plugin directory | `.claude-plugin/marketplace.json` |
| `openai/` | Codex, ChatGPT Plugins Directory | `.agents/plugins/marketplace.json` |
| `xai/` | Grok | `.grok-plugin/marketplace.json` |
| `google/` | Gemini CLI | `google/gemini-extension.json`, released as an archive |

Each package holds only its own vendor's files and versions on its own. Gemini CLI installs from the latest release of this repository: a release is made by the Release Gemini extension workflow, which attaches `google/` as one archive and marks the release latest, so any other release here is made with `--latest=false`. The skills in `*/skills/` are copies of one commit of sugra-api-skills, named in `skills-source.json`; edit them there, never here.

## Local check

```
python scripts/sync.py --source <clone of sugra-api-skills> --commit <commit on its main>
python scripts/check.py --source <clone of sugra-api-skills>
SKILLS_SOURCE=<clone of sugra-api-skills> python -m unittest discover -s scripts -p "test_*.py"
python scripts/build_gemini_archive.py --source <clone of sugra-api-skills>
```

Documentation: [https://docs.sugra.ai](https://docs.sugra.ai)

## License

MIT. Data from each endpoint carries its own upstream terms.
