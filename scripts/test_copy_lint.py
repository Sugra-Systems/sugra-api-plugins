"""Tests for the copy lint's reading of machine identifiers. Stdlib only.

    python -m unittest discover -s scripts -p "test_*.py"
"""

from __future__ import annotations

import contextlib
import io
import unittest

import check


def lint(text: str) -> bool:
    """True when the copy lint passes the text."""
    with contextlib.redirect_stderr(io.StringIO()):
        try:
            check.copy_lint(text, "sample")
        except SystemExit:
            return False
    return True


class CopyLint(unittest.TestCase):
    def test_an_operation_id_is_not_prose(self) -> None:
        self.assertTrue(lint("op: cboe_volatility"))
        self.assertTrue(lint("ratios come from cboe_put_call_ratio"))

    def test_a_lookup_key_and_a_series_code_are_not_prose(self) -> None:
        self.assertTrue(lint("key: us/sahmrealtime"))
        self.assertTrue(lint("series: SAHMREALTIME"))

    def test_a_commercial_name_as_a_word_still_fails(self) -> None:
        self.assertFalse(lint("Prices come from Cboe."))
        self.assertFalse(lint("Prices come from CBOE."))

    def test_a_banned_phrase_in_prose_still_fails(self) -> None:
        self.assertFalse(lint("Quotes arrive in realtime."))
        self.assertFalse(lint("Quotes arrive in real-time."))


if __name__ == "__main__":
    unittest.main()
