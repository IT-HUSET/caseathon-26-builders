# Architecture and decisions

The sketch on top, the decisions under it. Each decision is one paragraph: the situation, what we chose, what it costs.

## Sketch

```
browser ──GET /, POST /notes──▶ app.py (FastAPI, one module) ──sqlite3──▶ notes.db (path from NOTES_DB)
                                     │
                                     └── templates/index.html (the one page, inline CSS, no JS)
```

## D1 · One file, no framework layers

A warm-up cannot afford a package layout. `app.py` holds routes, data access and startup; `templates/index.html` holds the one page. Cost: the file will get long by increment 3, and a real project would split it. We accept that for today.

## D2 · SQLite via the standard library, schema created on startup

`sqlite3` from the standard library, a single `notes` table, `CREATE TABLE IF NOT EXISTS` at startup, path from `NOTES_DB` so tests get their own file. There is no migration tool. Cost: adding a column means writing the `ALTER TABLE` yourself, guarded so it runs once. Increment 3 will meet this.

## D3 · Plain HTML forms, full page render

Writes are a form POST followed by a redirect to `/`. Reads that take input, such as search or a filter, are a GET with query parameters, so the resulting URL can be reloaded and shared. No JavaScript framework, no HTMX in this repo. Cost: a full page reload per action, which is fine for a notes list and keeps every control checkable with a single `GET`.
