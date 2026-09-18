# Caseathon 2026 · Builders warm-up

A one-file notes app, a three-row plan, and one loop to practise: plan an increment, build it in a fresh AI session, verify it yourself, review it in another. This page gets your machine ready. The exercise is [EXERCISE.md](EXERCISE.md): read it once before the session, do it at the session.

The instructions assume Claude Code. Any agent that reads a rules file and runs commands works here too.

## Setup

Four steps, in order: fork, install, log in, check. You need your own fork of this repo, `uv`, and Claude Code with a Pro, Max, Team or Enterprise account.

### 1. Fork first

Click **Fork** at the top right of [github.com/IT-HUSET/caseathon-26-builders](https://github.com/IT-HUSET/caseathon-26-builders) and choose your **personal** GitHub account as the owner, not IT-HUSET or another organisation. Your commits go to your fork; the upstream repo stays untouched. A Codespace must also be created on your fork: one created on the IT-HUSET repo runs under the organisation, not your account.

Everything below says *your fork* where the other repo would otherwise be.

### 2. Install: pick one option

**Option A: on your own machine**

macOS, Linux, WSL:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh        # uv
curl -fsSL https://claude.ai/install.sh | bash         # Claude Code
```

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"   # uv
irm https://claude.ai/install.ps1 | iex                                             # Claude Code
```

Prefer winget? `winget install --id=astral-sh.uv -e` and `winget install Anthropic.ClaudeCode` do the same.

Open a new terminal afterwards so both are on your PATH. [Git for Windows](https://git-scm.com/downloads/win) is recommended on native Windows; it gives Claude Code a Bash tool.

Then, in any terminal:

```bash
git clone https://github.com/<your-github-user>/caseathon-26-builders.git
cd caseathon-26-builders
```

**Option B: GitHub Codespaces**

Nothing to install. On **your fork's** page, **Code → Codespaces → Create codespace on main**. The first build takes a few minutes and installs `uv`, Claude Code, and the Codex and Copilot CLIs. Continue in the Codespace terminal.

**Option C: Dev container on your machine**

Docker Desktop running, VS Code with the *Dev Containers* extension. Clone your fork, open the folder in VS Code, accept **Reopen in Container**. The container installs `uv`, Claude Code, and the Codex and Copilot CLIs. Continue in the VS Code terminal.

### 3. Log in

```bash
claude            # first start opens a browser login
```

Pick **Claude account with subscription**, not API key, and finish the login in the browser. Already inside a session? `/login` does the same.

In Codespaces or a dev container the browser handoff sometimes fails the first time. Run `/login` again: the second attempt shows a code you paste into the terminal.

Then type `/model opus`. Pro plans default to Sonnet; the exercise assumes Opus.

### 4. Run the check

```bash
uv run check.py
```

One line per requirement: Python, Claude Code installed and logged in, tests passing. A red line says what to fix. Green on every line, then send one prompt in `claude` as a smoke test: *What does this app do? Answer in three lines.* Three lines back and you are ready.

If a line stays red and you cannot fix it, use Option B.

## Commands

```bash
uv run uvicorn app:app --reload    # run, http://127.0.0.1:8000
uv run pytest -q                   # test
```

## Files

| File | What it is |
|------|------------|
| `app.py`, `templates/index.html` | The app. |
| `docs/plan.md` | The work: three increments, one row each. |
| `docs/` | `prd.md`, `adr.md`, `friction.md`, `review.md`: the same file names the Caseathon afternoon uses. |
| `AGENTS.md` | The rules file the agent reads every session. `CLAUDE.md` imports it. |
| `PORT.md` | Optional bonus: port the app to another stack, in case Python doesn't float your boat. |
| `check.py` | The environment check from step 4. |
