"""Tests for the Cursor plugin package and its marketplace file. Stdlib only.

    python -m unittest discover -s scripts -p "test_*.py"
"""

from __future__ import annotations

import contextlib
import io
import unittest

import check
import sync

# pinned here apart from check.py, so a change of the server has to change both
CURSOR_MCP = {"mcpServers": {"sugra-api": {"url": "https://mcp.sugra.ai/mcp"}}}


def load(rel: str) -> dict:
    return sync.strict_json((sync.ROOT / rel).read_text(encoding="utf-8"), rel)


class CursorPlugin(unittest.TestCase):
    def test_package_declares_the_connector_server(self) -> None:
        self.assertEqual(load("cursor/mcp.json"), CURSOR_MCP)
        self.assertEqual(check.CURSOR_MCP, CURSOR_MCP)
        check.check_cursor_mcp(CURSOR_MCP)
        # the server the Claude and Grok packages declare, at the same URL
        self.assertEqual(CURSOR_MCP["mcpServers"]["sugra-api"]["url"], check.ANTHROPIC_MCP["mcpServers"]["sugra-api"]["url"])
        # Cursor reads mcp.json; a .mcp.json beside it would be another vendor's file
        self.assertNotIn(".mcp.json", check.LAYOUT["cursor"])

    def test_check_refuses_any_other_server(self) -> None:
        server = CURSOR_MCP["mcpServers"]["sugra-api"]
        others = {
            "another url": {"mcpServers": {"sugra-api": {"url": "https://app.sugra.ai/mcp"}}},
            "a header": {"mcpServers": {"sugra-api": {**server, "headers": {"x-api-key": "${SUGRA_API_KEY}"}}}},
            "a placeholder url": {"mcpServers": {"sugra-api": {"url": "https://mcp.sugra.ai/mcp?key=${SUGRA_API_KEY}"}}},
            "a static client": {"mcpServers": {"sugra-api": {**server, "auth": {"CLIENT_ID": "id"}}}},
            "a second server": {"mcpServers": {"sugra-api": server, "other": server}},
        }
        for name, declared in others.items():
            with self.subTest(name), contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                check.check_cursor_mcp(declared)

    def test_manifest_passes_and_refuses_a_variable(self) -> None:
        manifest = load("cursor/.cursor-plugin/plugin.json")
        check.check_cursor_manifest(manifest)
        self.assertEqual(manifest["version"], check.VERSIONS["cursor"])
        variable = {"type": "object", "properties": {"SUGRA_API_KEY": {"type": "string"}}}
        others = {
            "a variable": {**manifest, "variables": variable},
            "a skills path": {**manifest, "skills": "./skills"},
            "an inline server": {**manifest, "mcpServers": CURSOR_MCP["mcpServers"]},
            "another logo": {**manifest, "logo": "https://sugra.ai/logo.png"},
            "another name": {**manifest, "name": "sugra-api"},
        }
        for name, declared in others.items():
            with self.subTest(name), contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                check.check_cursor_manifest(declared)

    def test_marketplace_points_at_the_package(self) -> None:
        market = load(".cursor-plugin/marketplace.json")
        self.assertEqual(market["name"], check.MARKETPLACE)
        self.assertEqual([(p["name"], p["source"]) for p in market["plugins"]], [(check.PLUGIN, "./cursor")])
        self.assertEqual(market["plugins"][0]["version"], check.VERSIONS["cursor"])
        self.assertIn("cursor", sync.PACKAGES)


if __name__ == "__main__":
    unittest.main()
