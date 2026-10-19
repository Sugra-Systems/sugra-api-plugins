# Security

This repository ships plugin packages that hold Agent Skills (Markdown instructions). The Claude package also declares the hosted Sugra API MCP server by its URL in `anthropic/.mcp.json`, with no key or other credential, and the ChatGPT Plugins Directory ZIP that `scripts/build_openai_zip.py` builds declares the same server at `https://app.sugra.ai/mcp`. No package ships hooks, MCP server code, or install-time scripts. The scripts in `scripts/` build and check the packages; no plugin runs them.

Report a vulnerability in these files to support@sugra.systems and abuse@sugra.systems. Do not open a public issue with exploit detail.

Do not put API keys in a plugin file, commit, or chat. Issue keys at https://app.sugra.ai/developer/keys.
