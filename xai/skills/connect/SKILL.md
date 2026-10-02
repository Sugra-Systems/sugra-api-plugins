---
name: connect
description: Attach a client to Sugra over HTTPS or MCP and install these skills. Use when setting up Claude (claude.ai, Desktop, Code), ChatGPT, Codex, Cursor, VS Code, Gemini CLI, Grok, OpenBB, a custom HTTP agent, or self-hosted MCP.
license: MIT
---

# Connect

Same key for every path: sign up at https://app.sugra.ai/register (a key is issued at signup), manage keys at https://app.sugra.ai/developer/keys. Prefix `sugra_...`. Do not log it. Client blocks: [references/clients.md](references/clients.md).

## 1. HTTPS API

```
GET https://sugra.ai/api/v1/...
x-api-key: sugra_...
```

System endpoints (`/health`, `/sources`, `/openapi.json`) need no key. Recipes: https://github.com/Sugra-Systems/sugra-api-cookbook. Endpoint detail: https://docs.sugra.ai.

## 2. Hosted MCP

Endpoint: `https://mcp.sugra.ai/mcp`

Auth: `Authorization: Bearer sugra_...`, or OAuth sign-in with the Sugra account from the directory listings below (scope `sugra:read`). Command-line and IDE clients use the Bearer key; Claude Code, Codex, and Grok cannot complete an OAuth sign-in on this URL yet. Discovery is public. `tools/call` and `resources/read` need Bearer.

- claude.ai, Claude Desktop, Claude mobile: "Sugra API" in Anthropic's Connectors Directory (https://url.sugra.ai/claude); connect and sign in. Claude Code signed in with the same claude.ai account lists it in `/mcp`. Manual: Customize -> Connectors -> Add custom connector with the hosted URL.
- ChatGPT and the Codex app: the Sugra API app (https://url.sugra.ai/openai) connects the hosted MCP server; sign in. These skills are a separate listing (section 6). Manual in ChatGPT: Settings -> Connectors -> Add MCP server with the hosted URL.
- Claude Code, Codex, Gemini CLI, Grok, Cursor, VS Code: the hosted URL with Bearer, or the local package (section 3). Client blocks: [references/clients.md](references/clients.md). These skills install separately (section 6).

Hosted tools: the gateway tools every transport has (`fetch_data`, `search_endpoints`, `describe_endpoint`, `call_endpoint`, `list_toolsets`, `list_sources`, `sugra_entity_screen`, `sugra_entity_lookup`) plus composed tools that register only on the hosted server:

- `resolve_entity`: free text to a canonical market or macro entity. An ambiguous match returns ranked candidates, never a silent pick.
- `get_snapshot`: entity plus a named recipe to one current view.
- `get_timeseries`: entity plus a metric to a bounded series.

Confirm with live `tools/list`. Do not call the composed tools on a stdio or self-hosted session.

## 3. Local MCP stdio

```bash
pip install sugra-api-mcp
```

The client starts `sugra-api-mcp` with `SUGRA_API_KEY` in the server's `env`, where the user puts their own key in place of `sugra_...` ([references/clients.md](references/clients.md)).

Gateway tools only. Catalog search works without the key; `call_endpoint` / `fetch_data` / entity tools return `missing_api_key` until it is set. If the console script is not on PATH: `"command": "python", "args": ["-m", "sugra_api_mcp"]`.

Package CLI: `sugra-api-mcp doctor`, `search`, `describe`, `call`.

## 4. Self-hosted MCP HTTP

```bash
sugra-api-mcp --transport streamable-http --port 8001
```

Gateway tools only; the hosted-only composed tools do not register here. Operator CORS/host/OAuth: `docs/self-hosting.md` in `sugra-api-mcp`. Do not put `INTERNAL_API_TOKEN` or JWKS URLs in a skill or chat.

## 5. OpenBB

Public extension `openbb-sugra` uses the HTTPS API, not MCP.

## 6. Install these skills

The Claude Code, Codex, and Grok plugins carry these skills only. The MCP server attaches separately (section 2 or 3).

| Client | Install |
|---|---|
| Claude Code | `/plugin marketplace add Sugra-Systems/sugra-api-plugins`, then `/plugin install sugra-api-skills@sugra-api-plugins` |
| Codex | `codex plugin marketplace add Sugra-Systems/sugra-api-plugins`, then `codex plugin add sugra-api-skills@sugra-api-plugins` |
| Grok | `grok plugin install Sugra-Systems/sugra-api-plugins#xai` |
| ChatGPT, Codex app | Plugins Directory listing https://chatgpt.com/plugins/plugins_6aa4f7db79848191a81e4048990545ef (skills; MCP comes from the app in section 2) |
| Any agent that reads Agent Skills | `npx skills add https://mcp.sugra.ai`, or copy the folders of https://github.com/Sugra-Systems/sugra-api-skills |

## Pick

| Host | Typical attach |
|---|---|
| Script, custom agent, OpenBB | HTTPS `x-api-key` |
| claude.ai, Claude Desktop | Connectors Directory listing |
| ChatGPT, Codex app | Sugra API app, plus the skills listing |
| Claude Code, Codex, Grok | skills plugin, plus hosted MCP with Bearer |
| Cursor, VS Code, Gemini CLI | stdio package or hosted MCP with Bearer |
| Own HTTP MCP process | self-host |
