# sugra-api for Grok

Official Sugra API plugin. HTTPS and MCP. Grok package: `.grok-plugin/plugin.json`, `.mcp.json`, `skills/`.

```
grok plugin marketplace add Sugra-Systems/sugra-api-plugins
grok plugin install sugra-api@sugra-api-plugins --trust
```

Or install this folder directly:

```
grok plugin install Sugra-Systems/sugra-api-plugins#xai --trust
```

`.mcp.json` connects the Sugra API MCP server at `https://app.sugra.ai/mcp` (`type: http`). The skills are copied from [sugra-api-skills](https://github.com/Sugra-Systems/sugra-api-skills) by `scripts/sync.py`; edit them there.

Documentation: https://docs.sugra.ai
