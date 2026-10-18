"""Tests for the MCP server the Anthropic package declares. Stdlib only.

    python -m unittest discover -s scripts -p "test_*.py"
"""

from __future__ import annotations

import contextlib
import io
import unittest

import check
import sync

# the server of the Sugra API connector in Anthropic's directory, https://claude.ai/directory/sugra-api;
# pinned here apart from check.py, so a change of the URL has to change both
CONNECTOR_MCP = {"mcpServers": {"sugra-api": {"type": "http", "url": "https://mcp.sugra.ai/mcp"}}}


class AnthropicMcp(unittest.TestCase):
    def test_package_declares_the_connector_server(self) -> None:
        text = (sync.ROOT / "anthropic" / ".mcp.json").read_text(encoding="utf-8")
        self.assertEqual(sync.strict_json(text, "anthropic/.mcp.json"), CONNECTOR_MCP)
        self.assertEqual(check.ANTHROPIC_MCP, CONNECTOR_MCP)
        check.check_anthropic_mcp(CONNECTOR_MCP)

    def test_check_refuses_any_other_declaration(self) -> None:
        server = CONNECTOR_MCP["mcpServers"]["sugra-api"]
        others = {
            "another url": {"mcpServers": {"sugra-api": {**server, "url": "https://app.sugra.ai/mcp"}}},
            "a header": {"mcpServers": {"sugra-api": {**server, "headers": {"X-Sugra-Client": "plugin"}}}},
            "another type": {"mcpServers": {"sugra-api": {**server, "type": "sse"}}},
            "a second server": {"mcpServers": {"sugra-api": server, "other": server}},
        }
        for name, declared in others.items():
            with self.subTest(name), contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                check.check_anthropic_mcp(declared)


if __name__ == "__main__":
    unittest.main()
