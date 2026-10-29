# Sugra API Skills for Antigravity

The Sugra API Skills plugin for Antigravity: the CLI (`agy`), the Antigravity app and the IDE share it. It teaches the agent to find the right Sugra API endpoint, call it with the right parameters, and cite the source and date of every figure, and it connects the hosted Sugra API MCP server. The plugin runs no code on your machine.

## What it contains

- plugin.json: the plugin manifest, with its name, description, logo and three example prompts.
- mcp_config.json: the hosted Sugra API MCP server, https://mcp.sugra.ai/mcp, as sugra-api.
- Six skills: auth-and-quota, discover-and-call, envelope-and-attribution, cross-domain-briefing, live-docs and using-sugra-api. They are instructions for the agent.

## Install

```
git clone https://github.com/Sugra-Systems/sugra-api-plugins
agy plugin install ./sugra-api-plugins/antigravity
```

## Sign in

The server asks you to sign in with your Sugra account. Antigravity registers itself with the server and opens the sign-in page in your browser the first time the agent uses it.

The Antigravity CLI 1.4.9 does not start an MCP server that a plugin declares yet. There the skills still work: they show the direct HTTPS request to https://sugra.ai, which you run with your own Sugra key in the x-api-key header.

## Try it

- "Find the Sugra endpoint for US CPI inflation and show the last two months."
- "Compare the unemployment rate in Germany and France and cite the source and date of each figure."
- "What is the three-day weather forecast for Rotterdam?"

## Data it sends

- The plugin stores no key and reads none from your files or environment.
- The agent calls the Sugra API MCP server at https://mcp.sugra.ai/mcp with the tool name and its parameters, such as an endpoint name or a country code. Antigravity keeps the sign-in to the server, not this plugin.
- If you ask for a direct HTTPS call, the skills show you the request to https://sugra.ai to run yourself: you put your own Sugra key in the x-api-key header, next to the endpoint and its parameters.
- To check current documentation, the skills point the agent at public pages that need no key: https://docs.sugra.ai, https://sugra.ai (the product page, the OpenAPI file, the source list and the health check) and https://sugra.systems (the company site, with pricing, blog and legal pages). No key goes with these requests.
- For sign-up and keys, the skills give you links to https://app.sugra.ai. For questions, or a fault that persists, they give you Sugra's addresses at sugra.systems: support@, legal@, privacy@ and abuse@.

Privacy policy: https://sugra.systems/privacy-policy. Terms of service: https://sugra.systems/terms-of-service.

## Support

Documentation: https://docs.sugra.ai. Support: support@sugra.systems.

The skills are maintained in https://github.com/Sugra-Systems/sugra-api-skills and copied here by scripts/sync.py.
