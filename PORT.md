# Optional: port to your stack

The exercise is stack-independent. If you would rather run it in the stack you will use for the Caseathon prototype, port the app first, then do [EXERCISE.md](EXERCISE.md) on the ported repo. The port is the same loop as one plan row: one prompt, one control you run yourself, one commit.

**Only if**: Option A (your own machine), and the toolchain already runs a hello-world web app there before the session. Codespaces and the dev container are set up for Python only. Pick a mainstream stack with an embedded SQLite driver and an in-process HTTP test client; if you have to think about which, stay in Python.

**Time box**: agree one with the room before you start. Not green when it ends: `git switch main`, one friction line, continue in Python. Nothing is lost, the port is on its own branch.

---

## 1. Branch, fresh session, one prompt

```bash
git switch -c port-<stack>
claude
```

```
Port this app to <stack>, keeping everything that is not code the same.
Read AGENTS.md, docs/prd.md, docs/adr.md, docs/plan.md, app.py,
templates/index.html and tests/test_notes.py first.

Keep: the routes (GET /, POST /notes answering 303 to /), the page markup
and inline CSS, no JavaScript, the empty-title rejection, newest note
first, one SQLite file whose path comes from NOTES_DB, the table created
on startup. Port the three tests one to one; each test gets its own
database file. The no-new-dependencies rule in AGENTS.md applies after
the port: use the smallest set your stack needs for a web server,
templates and tests, and commit the lockfile.

Then update every file that names the stack: AGENTS.md (run and test
commands, the one-module rule, the schema-change rule), docs/plan.md row 1
control (new test path), the sketch and D1 and D2 in docs/adr.md (same
decisions, this stack's equivalents), the Commands section, setup step 4 and the Files table of README.md, and the
deny list in .claude/settings.json (replace the uv and pip lines with
this stack's package-add commands). Delete app.py, tests/, pyproject.toml,
uv.lock and check.py.

Do not change docs/prd.md, D3, or the scenario text in docs/plan.md. Stop when
the ported tests pass and report the files changed and the test output.
```

Read the diff while it works (`/diff`). A file outside that list is a friction line.

## 2. Run the control yourself

The ported tests, in your terminal, with the command now in `AGENTS.md`. Then the row 1 click: start the app, add two notes, the newest is on top, an empty title is rejected.

The tests do not count on their own here. In row 1 the tests were written before the agent saw them; in the port the agent wrote the code and the tests in the same session. The click is the independent control.

## 3. Read the guardrails you now have

Open `AGENTS.md`, `docs/adr.md` and `.claude/settings.json` and read them as the stranger in block C will: every rule the agent will follow for the rest of the exercise is in these three files. Anything still saying Python, `uv` or `app.py` gets fixed now, by you or by one more prompt.

## 4. Commit

```
Commit the port with the message "Port to <stack>". Nothing else.
```

Read the staged list in the permission prompt before you approve. Then `/clear` or **Ctrl+D**, and start block A.

## From here on

Wherever EXERCISE.md says `uv run pytest -q` or `uv run uvicorn app:app --reload`, run the commands in `AGENTS.md`. Everything else in the exercise is unchanged. Push at the end goes to the `port-<stack>` branch of your fork.
