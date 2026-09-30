---
name: using-sugra-api
description: Work with the Sugra API over HTTPS and MCP. Use when the task needs Sugra data, a key, product directions (Finance, Macro, Entity, Net Atlas, News, Earth, Research), or which skill to load next.
license: MIT
---

# Using the Sugra API

Sugra API is intelligence infrastructure: one HTTP API, one key, seven product directions. Domain-agnostic. Do not frame it through one vertical.

The surface is LLM-friendly: one `x-api-key`, one JSON envelope `{data, meta}` on most payloads (a few are flat, with `meta` or `_meta` on the record; see envelope-and-attribution), MCP as the agent-native entry. Documentation truth is https://docs.sugra.ai (search and Ask AI). This skill is a map, not the catalog.

These files are English. Reply in the user's language.

Public hedge (not a live count): 1,500+ endpoints, 160+ primary sources, 36 domains. Live counts: skill `live-docs`.

## Two complete ways in

| Surface | When | How |
|---|---|---|
| HTTPS `https://sugra.ai` | The agent can GET/POST | `x-api-key` on `/api/v1/...` |
| MCP | The host is an MCP client | hosted `https://mcp.sugra.ai/mcp` or local `sugra-api-mcp` |

Both reach the same API. Use the surface the host already has, or the one the user named. Key: https://app.sugra.ai/settings/billing (Free: 50 requests/day). Do not log the key.

## Seven directions (one key, one budget)

| Direction | Coverage |
|---|---|
| Sugra Finance | Equities, fundamentals, filings, fixed income, derivatives, crypto, forex |
| Sugra Macro | Central banks, national statistics, FRED, IMF, World Bank, OECD |
| Sugra Entity | Company resolution, sanctions and watchlist screening, identifiers |
| Sugra Net Atlas | Internet infrastructure: ASNs, prefixes, IXPs, routing, DNS |
| Sugra News | Global news flow and event signals |
| Sugra Earth | Weather, hazards, energy, transport, air quality, climate |
| Sugra Research | Scientific, patent, and academic datasets |

## Skill map

| Need | Skill |
|---|---|
| Live docs, search, Ask AI, sources, blog | `live-docs` |
| Attach HTTP, hosted MCP, stdio, self-host, each client | `connect` |
| Key, plans, 401/429, Bearer vs `x-api-key` | `auth-and-quota` |
| Find and call an operation (HTTP and MCP) | `discover-and-call` |
| Envelope, sources, clocks, MCP shaping | `envelope-and-attribution` |
| Two or three directions in one answer | `cross-domain-briefing` |
