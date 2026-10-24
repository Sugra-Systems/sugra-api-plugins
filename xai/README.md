# Sugra API Skills for Grok

The Sugra API Skills plugin for Grok. It teaches Grok to find the right Sugra API endpoint, call it with the right parameters, and cite the source and date of every figure, and it connects the hosted Sugra API MCP server. The plugin runs no code on your machine. Grok package: `.grok-plugin/plugin.json`, `.mcp.json`, `skills/`.

## What it contains

- Six skills: auth-and-quota, discover-and-call, envelope-and-attribution, cross-domain-briefing, live-docs and using-sugra-api. They are instructions for Grok.
- The hosted Sugra API MCP server, https://mcp.sugra.ai/mcp, in .mcp.json, by its URL only, with no key.

## Sign in

The server asks you to sign in with your Sugra account the first time Grok uses it, in a browser window. In the Grok TUI you can also run /mcps, select the sugra-api server and press i. Grok keeps the sign-in, not this plugin.

## Install

```
grok plugin install Sugra-Systems/sugra-api-plugins#xai
```

## Data it sends

- The plugin stores no key and reads none from your files or environment.
- Grok calls the Sugra API MCP server at https://mcp.sugra.ai/mcp with the tool name and its parameters, such as an endpoint name or a country code.
- If you ask for a direct HTTPS call, the skills show you the request to https://sugra.ai to run yourself: you put your own Sugra key in the x-api-key header, next to the endpoint and its parameters.
- To check current documentation, the skills point Grok at public pages that need no key: https://docs.sugra.ai, https://sugra.ai and https://sugra.systems.

Privacy policy: https://sugra.systems/privacy-policy. Terms of service: https://sugra.systems/terms-of-service.

## Support

Documentation: https://docs.sugra.ai. Support: support@sugra.systems.

The skills are copied from [sugra-api-skills](https://github.com/Sugra-Systems/sugra-api-skills) by `scripts/sync.py`; edit them there.
