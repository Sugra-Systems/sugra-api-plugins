# Sugra API Skills for Claude

The Sugra API Skills plugin for Claude. It teaches Claude to find the right Sugra API endpoint, call it with the right parameters, and cite the source and date of every figure. The plugin holds skills only: it bundles no MCP server and runs no code.

## What it contains

- Six skills: auth-and-quota, discover-and-call, envelope-and-attribution, cross-domain-briefing, live-docs and using-sugra-api. They are instructions for Claude.

The Sugra API MCP server is a separate product: connect "Sugra API" from the Connectors Directory, https://url.sugra.ai/claude. The skills use its tools when it is connected.

## Try it

- "Find the Sugra endpoint for US CPI inflation and show the last two months."
- "Compare the unemployment rate in Germany and France and cite the source and date of each figure."
- "What is the three-day weather forecast for Rotterdam?"

## Data it sends

- The plugin sends nothing by itself. It stores no key and reads none from your files or environment.
- When the Sugra API MCP server is connected, Claude calls its tools with the tool name and its parameters, such as an endpoint name or a country code. That connection and its sign-in belong to the server, not to this plugin.
- If you ask for a direct HTTPS call, the skills show you the request to https://sugra.ai to run yourself: you put your own Sugra key in the x-api-key header, next to the endpoint and its parameters.
- To check current documentation, the skills point Claude at public pages that need no key: https://docs.sugra.ai, https://sugra.ai (the product page, the OpenAPI file, the source list and the health check) and https://sugra.systems (the company site, with pricing, blog and legal pages). No key goes with these requests.
- For sign-up and keys, the skills give you links to https://app.sugra.ai. For questions, or a fault that persists, they give you Sugra's addresses at sugra.systems: support@, legal@, privacy@ and abuse@.

Privacy policy: https://sugra.systems/privacy-policy. Terms of service: https://sugra.systems/terms-of-service.

## Install

```
/plugin marketplace add Sugra-Systems/sugra-api-plugins
/plugin install sugra-api-skills@sugra-api-plugins
```

## Support

Documentation: https://docs.sugra.ai. Support: support@sugra.systems.

The skills are maintained in https://github.com/Sugra-Systems/sugra-api-skills and copied here by scripts/sync.py.
