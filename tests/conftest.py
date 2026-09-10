import os

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client(tmp_path, monkeypatch):
    """Fresh SQLite file per test; the app reads NOTES_DB at startup."""
    monkeypatch.setenv("NOTES_DB", str(tmp_path / "test.db"))
    from app import app

    with TestClient(app) as c:
        yield c
