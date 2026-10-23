"""Tests for the MCP server the Anthropic and xAI packages declare. Stdlib only.

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
# the packages that declare it; openai/ stays skills only
MCP_PACKAGES = ("anthropic", "xai")


class PackageMcp(unittest.TestCase):
    def test_packages_declare_the_connector_server(self) -> None:
        self.assertEqual(check.ANTHROPIC_MCP, CONNECTOR_MCP)
        self.assertEqual(check.MCP_PACKAGES, MCP_PACKAGES)
        for package in MCP_PACKAGES:
            with self.subTest(package):
                label = f"{package}/.mcp.json"
                text = (sync.ROOT / package / ".mcp.json").read_text(encoding="utf-8")
                self.assertEqual(sync.strict_json(text, label), CONNECTOR_MCP)
                self.assertIn(".mcp.json", check.LAYOUT[package])
                check.check_package_mcp(CONNECTOR_MCP, package)

    def test_openai_package_holds_no_server(self) -> None:
        self.assertNotIn(".mcp.json", check.LAYOUT["openai"])
        self.assertFalse((sync.ROOT / "openai" / ".mcp.json").exists())
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            check.check_package_mcp(CONNECTOR_MCP, "openai")

    def test_check_refuses_any_other_declaration(self) -> None:
        server = CONNECTOR_MCP["mcpServers"]["sugra-api"]
        others = {
            "another url": {"mcpServers": {"sugra-api": {**server, "url": "https://app.sugra.ai/mcp"}}},
            "a header": {"mcpServers": {"sugra-api": {**server, "headers": {"X-Sugra-Client": "plugin"}}}},
            "another type": {"mcpServers": {"sugra-api": {**server, "type": "sse"}}},
            "a second server": {"mcpServers": {"sugra-api": server, "other": server}},
        }
        for package in MCP_PACKAGES:
            for name, declared in others.items():
                with self.subTest(package=package, case=name), contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                    check.check_package_mcp(declared, package)


if __name__ == "__main__":
    unittest.main()
