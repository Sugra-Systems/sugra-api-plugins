# Security

This repository ships plugin packages: Agent Skills (Markdown instructions) and an MCP configuration that points at the hosted Sugra API MCP server, `https://app.sugra.ai/mcp`. It does not ship hooks, MCP server code, or install-time scripts. The scripts in `scripts/` build and check the packages; no plugin runs them.

Report a vulnerability in these files to support@sugra.systems and abuse@sugra.systems. Do not open a public issue with exploit detail.

Do not put API keys in a plugin file, commit, or chat. Issue keys at https://app.sugra.ai/settings/billing.
