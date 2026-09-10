# Caseathon 2026 · Builders warm-up

A one-file notes app and a three-row plan. You spend the morning learning to plan in one session, build in another, and review in a third. The exercise is [EXERCISE.md](EXERCISE.md).

## Day before

```bash
git clone https://github.com/IT-HUSET/caseathon-26-builders.git
cd caseathon-26-builders
./check.sh
```

Green on every line, then start `claude`, type `/model opus`, and send one prompt as a smoke test. Not green: fix what the line says, or open the repo in GitHub Codespaces (the dev container installs everything).

## Commands

```bash
uv run uvicorn app:app --reload    # run, http://127.0.0.1:8000
uv run pytest -q                   # test
```

## Files

`app.py` and `templates/index.html` are the app. `PLAN.md` is the work. `docs/` holds the PRD, the decisions and the friction log. `AGENTS.md` is what the agent reads every session.

Any agent that reads a rules file and runs commands works here. Claude Code is what the instructions assume.
