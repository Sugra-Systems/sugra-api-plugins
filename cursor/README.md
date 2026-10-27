# Sugra API Skills for Cursor

The Sugra API Skills plugin for Cursor. It teaches Cursor to find the right Sugra API endpoint, call it with the right parameters, and cite the source and date of every figure, and it connects the hosted Sugra API MCP server. The plugin runs no code on your machine. Cursor package: `.cursor-plugin/plugin.json`, `mcp.json`, `skills/`, `assets/logo.png`.

## What it contains

- Six skills: auth-and-quota, discover-and-call, envelope-and-attribution, cross-domain-briefing, live-docs and using-sugra-api. They are instructions for Cursor.
- The hosted Sugra API MCP server, https://mcp.sugra.ai/mcp, in mcp.json, by its URL only, with no key. The plugin declares no variables, so there is nothing to configure.

## Install

The repository root holds `.cursor-plugin/marketplace.json`, which lists this folder as the plugin. On a Teams or Enterprise plan, an admin can import https://github.com/Sugra-Systems/sugra-api-plugins as a team marketplace (Dashboard, Plugins and MCPs, Import from Repo), and the plugin then shows in Customize.

To install it on your own machine, copy this folder to `~/.cursor/plugins/local/sugra-api-skills` and reload the window (Developer: Reload Window):

```
git clone https://github.com/Sugra-Systems/sugra-api-plugins
cp -R sugra-api-plugins/cursor ~/.cursor/plugins/local/sugra-api-skills
```

## Sign in

The server asks you to sign in with your Sugra account, in a browser window. Open Cursor Settings (Command Palette, Cursor Settings), select Tools & MCPs, find sugra-api, marked Needs authentication, and select Connect. Cursor keeps the sign-in, not this plugin.

## Try it

- "Find the Sugra endpoint for US CPI inflation and show the last two months."
- "Compare the unemployment rate in Germany and France and cite the source and date of each figure."
- "What is the three-day weather forecast for Rotterdam?"

## Data it sends

- The plugin stores no key and reads none from your files or environment.
- Cursor calls the Sugra API MCP server at https://mcp.sugra.ai/mcp with the tool name and its parameters, such as an endpoint name or a country code.
- If you ask for a direct HTTPS call, the skills show you the request to https://sugra.ai to run yourself: you put your own Sugra key in the x-api-key header, next to the endpoint and its parameters.
- To check current documentation, the skills point Cursor at public pages that need no key: https://docs.sugra.ai, https://sugra.ai (the product page, the OpenAPI file, the source list and the health check) and https://sugra.systems (the company site, with pricing, blog and legal pages). No key goes with these requests.
- For sign-up and keys, the skills give you links to https://app.sugra.ai. For questions, or a fault that persists, they give you Sugra's addresses at sugra.systems: support@, legal@, privacy@ and abuse@.

Privacy policy: https://sugra.systems/privacy-policy. Terms of service: https://sugra.systems/terms-of-service.

## Support

Documentation: https://docs.sugra.ai. Support: support@sugra.systems.

The skills are maintained in https://github.com/Sugra-Systems/sugra-api-skills and copied here by scripts/sync.py; edit them there.
