# Caseathon 2026 · Builders warm-up

A one-file notes app and a three-row plan. You learn to plan in one session, build in another, and review in a third. The exercise is [EXERCISE.md](EXERCISE.md).

## Setup

You need three things: this repo, `uv`, and Claude Code logged in with a Pro, Max, Team or Enterprise account. Pick one of the options below, then run the check.

### Option A: on your own machine

**macOS, Linux, WSL**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh        # uv
curl -fsSL https://claude.ai/install.sh | bash         # Claude Code
```

**Windows (PowerShell)**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"   # uv
irm https://claude.ai/install.ps1 | iex                                             # Claude Code
```

Prefer winget? `winget install --id=astral-sh.uv -e` and `winget install Anthropic.ClaudeCode` do the same.

Open a new terminal afterwards so both are on your PATH. [Git for Windows](https://git-scm.com/downloads/win) is recommended on native Windows; it gives Claude Code a Bash tool.

Then, in any terminal:

```bash
git clone https://github.com/IT-HUSET/caseathon-26-builders.git
cd caseathon-26-builders
uv run check.py
```

### Option B: GitHub Codespaces

Nothing to install. On the repo page, **Code → Codespaces → Create codespace on main**. The first build takes a few minutes and installs `uv`, Claude Code, and the Codex and Copilot CLIs. Open the terminal and run `uv run check.py`.

Want to keep your work afterwards? Fork the repo first and create the codespace on your fork.

### Option C: Dev container on your machine

Docker Desktop running, VS Code with the *Dev Containers* extension. Clone the repo, open the folder in VS Code, accept **Reopen in Container**. The container installs `uv`, Claude Code, and the Codex and Copilot CLIs. Then `uv run check.py` in the VS Code terminal.

### The check

`uv run check.py` prints one line per requirement. Green on every line, then:

```bash
claude            # first start opens a browser login
```

Pick **Claude account with subscription**, not API key, and finish the login in the browser. Already inside a session? `/login` does the same.

In Codespaces or a dev container the browser handoff sometimes fails the first time. Run `/login` again: the second attempt shows a code you paste into the terminal.

Then type `/model opus`, and send one prompt as a smoke test: *What does this app do? Answer in three lines.*

If a line fails and you cannot fix it, use Option B.

## Commands

```bash
uv run uvicorn app:app --reload    # run, http://127.0.0.1:8000
uv run pytest -q                   # test
```

## Files

`app.py` and `templates/index.html` are the app. `PLAN.md` is the work. `docs/` holds the PRD, the decisions and the friction log. `AGENTS.md` is what the agent reads every session.

Any agent that reads a rules file and runs commands works here. Claude Code is what the instructions assume.
