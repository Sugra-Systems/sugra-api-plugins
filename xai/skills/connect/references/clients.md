# Client attach blocks

Every block shows the placeholder `sugra_...`, where the user puts their own key. Do not ask for the key in chat, and do not read it from the environment or a file. Keep the key out of project files that get committed. A key typed into a command line stays in shell history, so run a command below as shown, with the placeholder, and have the user replace the placeholder with their key in the user settings file the command wrote, named under each client (`~` is the home folder, `%USERPROFILE%` on Windows).

Stdio MCP (local package):

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

Hosted:

```bash
claude mcp add --transport http sugra https://mcp.sugra.ai/mcp --header "Authorization: Bearer sugra_..."
```

Local package:

```bash
claude mcp add sugra -e SUGRA_API_KEY=sugra_... -- sugra-api-mcp
```

Either command writes to `~/.claude.json`.

Signed in with a claude.ai account that connected "Sugra API" from the Connectors Directory: nothing to add, `/mcp` lists it. These skills install separately: the plugin in `connect` section 6.

## Codex

Hosted, in `~/.codex/config.toml`:

```toml
[mcp_servers.sugra]
url = "https://mcp.sugra.ai/mcp"
http_headers = { "Authorization" = "Bearer sugra_..." }
```

Local package:

```bash
codex mcp add sugra --env SUGRA_API_KEY=sugra_... -- sugra-api-mcp
```

The command writes to the same `~/.codex/config.toml`. These skills install separately: the plugin in `connect` section 6.

## Gemini CLI

User `~/.gemini/settings.json` takes the same `mcpServers` block. Or add the local package by command:

```bash
gemini mcp add --scope user -e SUGRA_API_KEY=sugra_... sugra sugra-api-mcp
```

Or hosted:

```bash
gemini mcp add --scope user --transport http sugra https://mcp.sugra.ai/mcp --header "Authorization: Bearer sugra_..."
```

With `--scope user` either command writes to `~/.gemini/settings.json`. `gemini mcp list`, then `/mcp` in session.

## Cursor, VS Code, Zed, Cline, Continue.dev, Windsurf

Each has an MCP settings file (`mcp.json` or equivalent). Use the stdio block above or hosted `https://mcp.sugra.ai/mcp` with Bearer.

## Grok

Hosted:

```bash
grok mcp add --transport http sugra https://mcp.sugra.ai/mcp --header "Authorization: Bearer sugra_..."
```

Or the local package: `grok mcp add sugra -e SUGRA_API_KEY=sugra_... -- sugra-api-mcp`. Either command writes to `~/.grok/config.toml`. These skills install separately: `grok plugin install Sugra-Systems/sugra-api-plugins#xai` (`connect` section 6).

## xAI SDK / Responses API

Remote MCP tools against `https://mcp.sugra.ai/mcp` with Bearer.

## ChatGPT and claude.ai

ChatGPT: the MCP tools come from the Sugra API app (https://url.sugra.ai/openai), or a hosted connector (Settings -> Connectors -> Add MCP server); these skills install from the Plugins Directory (https://chatgpt.com/plugins/plugins_6aa4f7db79848191a81e4048990545ef). claude.ai: "Sugra API" in the Connectors Directory (https://url.sugra.ai/claude), or a custom connector with the hosted URL.
