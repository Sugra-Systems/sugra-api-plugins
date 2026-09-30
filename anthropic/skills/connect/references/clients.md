# Client attach blocks

Stdio MCP (local package). Put the key in the client's config file or environment, never in chat or on a typed command line (shell history keeps it).

```json
{
  "mcpServers": {
    "sugra": {
      "command": "sugra-api-mcp",
      "env": { "SUGRA_API_KEY": "sugra_..." }
    }
  }
}
```

## Claude Desktop

File: macOS `~/Library/Application Support/Claude/claude_desktop_config.json`; Windows `%APPDATA%\Claude\claude_desktop_config.json`. Linux has no Desktop build: use Claude Code, an IDE, or hosted MCP. Restart after edit.

## Claude Code

The server inherits Claude Code's environment. Read the key without echo, then start Claude Code from that shell:

```bash
read -rs SUGRA_API_KEY && export SUGRA_API_KEY
claude mcp add sugra -- sugra-api-mcp
```

Or the same JSON in a project `.mcp.json`.

## Gemini CLI

User `~/.gemini/settings.json` or project `.gemini/settings.json`, same `mcpServers` block. Or:

```bash
read -rs SUGRA_API_KEY && export SUGRA_API_KEY
gemini mcp add --scope user -e SUGRA_API_KEY="$SUGRA_API_KEY" sugra sugra-api-mcp
gemini mcp add --scope user --transport http --header "Authorization: Bearer $SUGRA_API_KEY" sugra https://mcp.sugra.ai/mcp
```

`gemini mcp list`, then `/mcp` in session.

## Cursor, VS Code, Zed, Cline, Continue.dev, Windsurf

Each has an MCP settings file (`mcp.json` or equivalent). Use the stdio block above or hosted `https://mcp.sugra.ai/mcp` with Bearer.

## Grok

Hosted MCP as a remote server, or local stdio with `SUGRA_API_KEY`. This skill plugin is separate from the MCP server: install the plugin, then still connect MCP or HTTP.

## xAI SDK / Responses API

Remote MCP tools against `https://mcp.sugra.ai/mcp` with Bearer.

## ChatGPT and claude.ai

ChatGPT: these skills install from the Plugins Directory (https://chatgpt.com/plugins/plugins_6aa4f7db79848191a81e4048990545ef); the MCP tools attach as a hosted connector (Settings -> Connectors -> Add MCP server). claude.ai: hosted connector.
