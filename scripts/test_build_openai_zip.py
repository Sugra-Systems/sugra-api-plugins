"""Tests for the Plugins Directory ZIP. Stdlib only.

    SKILLS_SOURCE=<clone of sugra-api-skills> python -m unittest discover -s scripts -p "test_*.py"

The builder reads HEAD, so commit openai/ and skills-source.json first. Without
SKILLS_SOURCE the clone is looked for at .skills-source/, where CI checks it out;
when neither is there the tests are skipped.
"""

from __future__ import annotations

import contextlib
import io
import json
import os
import shutil
import tempfile
import unittest
import zipfile
from pathlib import Path

import build_openai_zip
import sync

SOURCE = Path(os.environ.get("SKILLS_SOURCE") or sync.ROOT / ".skills-source")
# the MCP server the Sugra API listing already holds; the directory refuses a package
# that omits it and does not support a change of its URL
LISTING_MCP = {
    "$schema": "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
    "mcpServers": {"sugra-api": {"type": "streamable-http", "url": "https://app.sugra.ai/mcp"}},
}


@unittest.skipUnless(SOURCE.is_dir(), f"no sugra-api-skills clone at {SOURCE}; set SKILLS_SOURCE")
class DirectoryZip(unittest.TestCase):
    def setUp(self) -> None:
        dist = sync.ROOT / "dist"
        dist.mkdir(exist_ok=True)
        self.dist = Path(tempfile.mkdtemp(dir=dist, prefix=".test-"))
        self.addCleanup(shutil.rmtree, self.dist)
        self.saved = build_openai_zip.DIST
        build_openai_zip.DIST = self.dist
        self.addCleanup(setattr, build_openai_zip, "DIST", self.saved)

    def build(self) -> bytes:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = build_openai_zip.main(["build_openai_zip.py", "--source", str(SOURCE)])
        self.assertEqual(code, 0, out.getvalue())
        built = sorted(self.dist.glob("*.zip"))
        self.assertEqual(len(built), 1, built)
        return built[0].read_bytes()

    def test_zip_declares_the_listing_mcp(self) -> None:
        with zipfile.ZipFile(io.BytesIO(self.build())) as archive:
            names = archive.namelist()
            self.assertIn("mcp.json", names)
            self.assertEqual(json.loads(archive.read("mcp.json")), LISTING_MCP)
            manifest = json.loads(archive.read("plugin.json"))
        self.assertEqual(manifest["name"], build_openai_zip.LISTING_NAME)
        self.assertNotIn("mcpServers", json.dumps(manifest))
        self.assertNotIn("README.md", names)
        self.assertEqual(names, sorted(names))

    def test_zip_carries_the_listing_starter_prompts(self) -> None:
        with zipfile.ZipFile(io.BytesIO(self.build())) as archive:
            manifest = json.loads(archive.read("plugin.json"))
        prompts = manifest["extensions"]["com.openai"]["interface"]["defaultPrompt"]
        self.assertEqual(prompts, build_openai_zip.LISTING_INTERFACE["defaultPrompt"])
        self.assertEqual(build_openai_zip.prompt_errors(prompts), [])

    def test_marketplace_folder_stays_skills_only(self) -> None:
        self.assertFalse((sync.ROOT / build_openai_zip.PACKAGE / "mcp.json").exists())
        self.assertNotIn("mcp.json", build_openai_zip.tree(build_openai_zip.PACKAGE))

    def test_zip_is_byte_reproducible(self) -> None:
        first = self.build()
        self.assertEqual(self.build(), first)


class StarterPrompts(unittest.TestCase):
    def test_limits(self) -> None:
        self.assertEqual(build_openai_zip.prompt_errors(["a", "b", "c"]), [])
        self.assertTrue(build_openai_zip.prompt_errors(["a", "b", "c", "d"]))
        self.assertTrue(build_openai_zip.prompt_errors(["a" * 129]))
        self.assertTrue(build_openai_zip.prompt_errors(["a", "a"]))
        self.assertTrue(build_openai_zip.prompt_errors(["", "b"]))
        self.assertTrue(build_openai_zip.prompt_errors([]))


if __name__ == "__main__":
    unittest.main()
