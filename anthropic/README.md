# Sugra API for Claude

The Sugra API plugin for Claude. It teaches Claude to find the right Sugra API endpoint, call it with the right parameters, and cite the source and as-of date of every figure. It also connects the hosted Sugra API MCP server, so Claude can search the endpoint catalog and call endpoints as tools.

## What it contains

- Seven skills: connect, auth-and-quota, discover-and-call, envelope-and-attribution, cross-domain-briefing, live-docs and using-sugra-api. They are instructions for Claude and run no code.
- One MCP server: https://app.sugra.ai/mcp, run by Sugra Systems, Inc.

## Try it

- "Find the Sugra endpoint for US CPI inflation and show the last two months."
- "Compare the unemployment rate in Germany and France and cite the source and as-of date of each figure."
- "What is the three-day weather forecast for Rotterdam?"

## Data it sends

- Each MCP tool call goes to https://app.sugra.ai/mcp with the tool name and its parameters, such as an endpoint name or a country code. The result comes back to Claude.
- The server asks you to sign in to your Sugra account before the first call. The plugin stores no key and its configuration reads no environment variable.
- If you ask for a direct HTTPS call, the skills show Claude how to call https://sugra.ai: the request carries your Sugra key in the x-api-key header, the endpoint and its parameters or body.
- When documentation may be out of date, the skills point Claude at public pages on https://docs.sugra.ai and https://sugra.ai.

Privacy policy: https://sugra.systems/privacy-policy. Terms of service: https://sugra.systems/terms-of-service.

## Install

```
/plugin marketplace add Sugra-Systems/sugra-api-plugins
/plugin install sugra-api@sugra-api-plugins
```

## Support

Documentation: https://docs.sugra.ai. Support: support@sugra.systems.

The skills are maintained in https://github.com/Sugra-Systems/sugra-api-skills and copied here by scripts/sync.py.
