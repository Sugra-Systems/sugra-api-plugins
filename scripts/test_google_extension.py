"""Tests for the Gemini CLI extension and its release archive. Stdlib only.

    SKILLS_SOURCE=<clone of sugra-api-skills> python -m unittest discover -s scripts -p "test_*.py"

The builder reads HEAD, so commit google/ and skills-source.json first. Without
SKILLS_SOURCE the clone is looked for at .skills-source/, where CI checks it out;
when neither is there the archive tests are skipped.
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

import build_gemini_archive
import check
import sync

SOURCE = Path(os.environ.get("SKILLS_SOURCE") or sync.ROOT / ".skills-source")
# pinned here apart from check.py, so a change of the manifest has to change both
EXTENSION = {
    "name": "sugra-api-skills",
    "version": "1.2.1",
    "description": check.DESCRIPTION,
    "mcpServers": {"sugra-api": {"type": "http", "url": "https://mcp.sugra.ai/mcp", "oauth": {"enabled": True}}},
    "contextFileName": "GEMINI.md",
}


class GoogleExtension(unittest.TestCase):
    def test_package_declares_the_extension(self) -> None:
        text = (sync.ROOT / "google" / "gemini-extension.json").read_text(encoding="utf-8")
        self.assertEqual(sync.strict_json(text, "google/gemini-extension.json"), EXTENSION)
        self.assertEqual(check.GOOGLE_EXTENSION, EXTENSION)
        check.check_google_extension(EXTENSION)

    def test_server_is_the_anthropic_server(self) -> None:
        server = dict(EXTENSION["mcpServers"]["sugra-api"])
        server.pop("oauth")
        self.assertEqual({"mcpServers": {"sugra-api": server}}, check.ANTHROPIC_MCP)

    def test_check_refuses_any_other_manifest(self) -> None:
        server = EXTENSION["mcpServers"]["sugra-api"]
        others = {
            "another url": {**EXTENSION, "mcpServers": {"sugra-api": {**server, "url": "https://app.sugra.ai/mcp"}}},
            "a header": {**EXTENSION, "mcpServers": {"sugra-api": {**server, "headers": {"Authorization": "Bearer $SUGRA_API_KEY"}}}},
            "no oauth": {**EXTENSION, "mcpServers": {"sugra-api": {"type": "http", "url": server["url"]}}},
            "a second server": {**EXTENSION, "mcpServers": {"sugra-api": server, "other": server}},
            "another context file": {**EXTENSION, "contextFileName": "README.md"},
            "another version": {**EXTENSION, "version": "1.2.0"},
            "a setting": {**EXTENSION, "settings": [{"name": "key", "envVar": "SUGRA_API_KEY"}]},
        }
        for name, declared in others.items():
            with self.subTest(name), contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                check.check_google_extension(declared)

    def test_asset_name_is_the_generic_kind(self) -> None:
        name = build_gemini_archive.ASSET.format(version=EXTENSION["version"]).lower()
        for platform in ("darwin", "linux", "win32"):
            self.assertNotIn(platform, name)
        self.assertTrue(name.endswith(".zip"))


@unittest.skipUnless(SOURCE.is_dir(), f"no sugra-api-skills clone at {SOURCE}; set SKILLS_SOURCE")
class GeminiArchive(unittest.TestCase):
    def setUp(self) -> None:
        dist = sync.ROOT / "dist"
        dist.mkdir(exist_ok=True)
        self.dist = Path(tempfile.mkdtemp(dir=dist, prefix=".test-"))
        self.addCleanup(shutil.rmtree, self.dist)
        self.saved = build_gemini_archive.DIST
        build_gemini_archive.DIST = self.dist
        self.addCleanup(setattr, build_gemini_archive, "DIST", self.saved)

    def build(self) -> bytes:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = build_gemini_archive.main(["build_gemini_archive.py", "--source", str(SOURCE)])
        self.assertEqual(code, 0, out.getvalue())
        built = sorted(self.dist.glob("*.zip"))
        self.assertEqual([path.name for path in built], [f"sugra-api-gemini-{EXTENSION['version']}.zip"])
        return built[0].read_bytes()

    def test_manifest_and_context_at_the_archive_root(self) -> None:
        with zipfile.ZipFile(io.BytesIO(self.build())) as archive:
            names = archive.namelist()
            self.assertEqual(json.loads(archive.read("gemini-extension.json")), EXTENSION)
            self.assertIn("GEMINI.md", names)
        skills = {name.split("/")[1] for name in names if name.startswith("skills/")}
        self.assertEqual(skills, {path.name for path in (sync.ROOT / "google" / "skills").iterdir() if path.is_dir()})
        self.assertFalse([name for name in names if name.startswith("google/")])

    def test_one_commit_gives_one_archive(self) -> None:
        self.assertEqual(self.build(), self.build())


if __name__ == "__main__":
    unittest.main()
