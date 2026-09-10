# Quick Notes

A one-file FastAPI notes app used as the Caseathon Builders warm-up. Product intent is in `docs/PRD.md`, the increments in `PLAN.md`, the architecture decisions in `docs/DECISIONS.md`. Read all three before changing anything.

## Run

```bash
uv run uvicorn app:app --reload      # http://127.0.0.1:8000
uv run pytest -q                     # the sensors; run after every change
```

## Layout

- `app.py`: routes, data access, startup. The only Python module.
- `templates/index.html`: the only page. Inline CSS, no JavaScript.
- `tests/`: one test module per increment. `conftest.py` gives each test its own SQLite file.

## Rules

- Work one plan row at a time. Do not start the next row, and do not touch rows marked `done`, unless the row you are on requires it and you say so.
- Every row ends with its control passing: the named test green, and the page behaving as the scenario says. Do not edit or delete a test to make it pass; if a test is wrong, say so and stop.
- Keep the decisions in `docs/DECISIONS.md`. Changing one is allowed only after writing the new paragraph first.
- No new dependencies. No JavaScript. No second Python module unless the row asks for it.
- Schema changes go through `init_db()` with an idempotent `ALTER TABLE` guard; never drop the table.
- Before you report done: list the files you changed, the command you ran, and its last line of output.
