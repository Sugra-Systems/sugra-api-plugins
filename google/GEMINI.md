# Sugra API

This extension connects the hosted Sugra API MCP server as `sugra-api` and adds six skills: using-sugra-api, discover-and-call, envelope-and-attribution, auth-and-quota, cross-domain-briefing and live-docs. Activate the skill that fits the task; using-sugra-api is the map.

- The server needs a sign-in with the user's Sugra account. When a `sugra-api` tool answers that authentication is missing or expired, ask the user to run `/mcp auth sugra-api` and then retry the call.
- Find the operation before calling it, then call it with the parameters its description names. Do not guess an operation name or a parameter.
- Check that the answer is about the place, entity, period and measure the user asked for, and cite the source and the as-of date of every figure.
- Documentation: https://docs.sugra.ai.
