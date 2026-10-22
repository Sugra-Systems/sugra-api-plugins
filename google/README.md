# Sugra API Skills for Gemini CLI

The Sugra API Skills extension for Gemini CLI. It teaches Gemini to find the right Sugra API endpoint, call it with the right parameters, and cite the source and date of every figure, and it connects the hosted Sugra API MCP server. The extension runs no code on your machine.

## What it contains

- gemini-extension.json: the extension manifest. It declares the hosted Sugra API MCP server, https://mcp.sugra.ai/mcp, as sugra-api, and GEMINI.md as the context file.
- GEMINI.md: a short context file that tells Gemini how to use the server and the skills.
- Six skills: auth-and-quota, discover-and-call, envelope-and-attribution, cross-domain-briefing, live-docs and using-sugra-api. They are instructions for Gemini.

## Install

```
gemini extensions install https://github.com/Sugra-Systems/sugra-api-plugins
```

Gemini CLI installs the extension from the latest release of this repository, which carries this folder as its archive.

## Sign in

The server asks you to sign in with your Sugra account. In Gemini CLI, run /mcp auth sugra-api and sign in in the browser window it opens. /mcp shows the server and its sign-in state.

## Try it

- "Find the Sugra endpoint for US CPI inflation and show the last two months."
- "Compare the unemployment rate in Germany and France and cite the source and date of each figure."
- "What is the three-day weather forecast for Rotterdam?"

## Data it sends

- The extension stores no key and reads none from your files or environment.
- Gemini calls the Sugra API MCP server at https://mcp.sugra.ai/mcp with the tool name and its parameters, such as an endpoint name or a country code. Gemini CLI keeps the sign-in to the server, not this extension.
- If you ask for a direct HTTPS call, the skills show you the request to https://sugra.ai to run yourself: you put your own Sugra key in the x-api-key header, next to the endpoint and its parameters.
- To check current documentation, the skills point Gemini at public pages that need no key: https://docs.sugra.ai, https://sugra.ai (the product page, the OpenAPI file, the source list and the health check) and https://sugra.systems (the company site, with pricing, blog and legal pages). No key goes with these requests.
- For sign-up and keys, the skills give you links to https://app.sugra.ai. For questions, or a fault that persists, they give you Sugra's addresses at sugra.systems: support@, legal@, privacy@ and abuse@.

Privacy policy: https://sugra.systems/privacy-policy. Terms of service: https://sugra.systems/terms-of-service.

## Support

Documentation: https://docs.sugra.ai. Support: support@sugra.systems.

The skills are maintained in https://github.com/Sugra-Systems/sugra-api-skills and copied here by scripts/sync.py. The release archive is built by scripts/build_gemini_archive.py.
