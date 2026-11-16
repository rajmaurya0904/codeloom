"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import codeloom


def test_version_is_set() -> None:
    assert codeloom.__version__
