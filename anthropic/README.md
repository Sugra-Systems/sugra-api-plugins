# sugra-api for Claude

Official Sugra API plugin for Claude Code and the Anthropic plugin directory. HTTPS and MCP. Plugin `sugra-api` in marketplace `sugra-api-plugins`.

```
/plugin marketplace add Sugra-Systems/sugra-api-plugins
/plugin install sugra-api@sugra-api-plugins
```

This folder holds Claude files only: `.claude-plugin/plugin.json`, `.mcp.json`, `skills/`. The skills are copied from [sugra-api-skills](https://github.com/Sugra-Systems/sugra-api-skills) by `scripts/sync.py`; edit them there.

Hosted MCP: `.mcp.json` connects the Sugra API MCP server at `https://app.sugra.ai/mcp` (`type: http`). The plugin carries no key; the server asks each person to sign in. The server receives the tool calls Claude makes to it (endpoint names and parameters). The skills themselves run nothing.

Documentation: https://docs.sugra.ai
