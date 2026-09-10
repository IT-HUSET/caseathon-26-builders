"""Quick Notes: the whole app in one file.

Run:   uv run uvicorn app:app --reload
Test:  uv run pytest -q
Data:  SQLite file, path from NOTES_DB (default notes.db next to this file).
"""

import os
import sqlite3
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")


def db_path() -> str:
    return os.environ.get("NOTES_DB", str(BASE_DIR / "notes.db"))


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(db_path())
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with connect() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                body TEXT NOT NULL DEFAULT '',
                created_at TEXT NOT NULL
            )
            """
        )


def list_notes() -> list[sqlite3.Row]:
    with connect() as conn:
        return conn.execute(
            "SELECT id, title, body, created_at FROM notes ORDER BY id DESC"
        ).fetchall()


def create_note(title: str, body: str) -> int:
    created_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with connect() as conn:
        cur = conn.execute(
            "INSERT INTO notes (title, body, created_at) VALUES (?, ?, ?)",
            (title, body, created_at),
        )
        return cur.lastrowid


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(title="Quick Notes", lifespan=lifespan)


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        request, "index.html", {"notes": list_notes()}
    )


@app.post("/notes")
def add_note(title: str = Form(min_length=1, max_length=120), body: str = Form("")):
    create_note(title.strip(), body.strip())
    return RedirectResponse("/", status_code=303)
