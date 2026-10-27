"""Tests for the Antigravity plugin. Stdlib only.

    python -m unittest discover -s scripts -p "test_*.py"
"""

from __future__ import annotations

import contextlib
import io
import unittest

import check
import sync

# pinned here apart from check.py, so a change of the server has to change both
SERVER = {"mcpServers": {"sugra-api": {"serverUrl": "https://mcp.sugra.ai/mcp"}}}


class AntigravityPlugin(unittest.TestCase):
    def test_package_declares_the_server(self) -> None:
        text = (sync.ROOT / "antigravity" / "mcp_config.json").read_text(encoding="utf-8")
        self.assertEqual(sync.strict_json(text, "antigravity/mcp_config.json"), SERVER)
        self.assertEqual(check.ANTIGRAVITY_MCP, SERVER)
        check.check_antigravity_mcp(SERVER)

    def test_server_is_the_anthropic_server(self) -> None:
        url = SERVER["mcpServers"]["sugra-api"]["serverUrl"]
        self.assertEqual(url, check.ANTHROPIC_MCP["mcpServers"]["sugra-api"]["url"])

    def test_check_refuses_any_other_server(self) -> None:
        server = SERVER["mcpServers"]["sugra-api"]
        others = {
            "another url": {"mcpServers": {"sugra-api": {"serverUrl": "https://app.sugra.ai/mcp"}}},
            "a header": {"mcpServers": {"sugra-api": {**server, "headers": {"Authorization": "Bearer $SUGRA_API_KEY"}}}},
            "the gemini key": {"mcpServers": {"sugra-api": {"httpUrl": server["serverUrl"]}}},
            "a second server": {"mcpServers": {"sugra-api": server, "other": server}},
        }
        for name, declared in others.items():
            with self.subTest(name), contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                check.check_antigravity_mcp(declared)

    def test_manifest_keys_are_in_the_antigravity_schema(self) -> None:
        # the keys of https://antigravity.google/schemas/v1/plugin.json, which allows no others
        allowed = {
            "$schema", "name", "displayName", "display_name", "description", "version", "disabled", "logo",
            "suggestedPrompts", "suggested_prompts", "skills", "author", "homepage", "repository", "license",
            "keywords", "extensions",
        }
        text = (sync.ROOT / "antigravity" / "plugin.json").read_text(encoding="utf-8")
        manifest = sync.strict_json(text, "antigravity/plugin.json")
        self.assertLessEqual(set(manifest), allowed)
        self.assertLessEqual(set(manifest["author"]), {"name", "email", "url"})
        self.assertLessEqual(len(manifest["suggestedPrompts"]), 3)


if __name__ == "__main__":
    unittest.main()
