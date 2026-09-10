# Plan, then build

Builders warm-up for the Caseathon. Three blocks. You practise the loop you will run when building the prototype: write the plan row, open a fresh session, let the agent build, run the control yourself, review in another fresh session.

**What you learn**

- Why planning and building happen in separate sessions, and what a plan row must contain for that to work.
- How to hand the agent one increment at a time and check it with something executable.
- What a review in fresh context finds that you did not.

**What you need**: `uv run check.py` green, `claude` started in this directory, `/model opus` set. Work alone; pairing is fine if you prefer, one laptop per pair.

**Fresh session** below means the conversation is gone and only the files remain. Either `/clear` inside the running `claude`, or **Ctrl+D** and start `claude` again. Both work.

The playbook chapters behind each block are listed at the end.

---

## The repo in one minute

| File | What it is |
|------|------------|
| `app.py`, `templates/index.html` | The whole app. Increment 1 is done: create a note, see it on top of the list. |
| `tests/test_notes.py` | The control for increment 1. Three tests. |
| `PLAN.md` | Three rows. Row 1 done, rows 2 and 3 open and half-empty. That is your work. |
| `docs/PRD.md` | What we are building and for whom. One page. |
| `docs/DECISIONS.md` | Three decisions the agent must respect. |
| `docs/FRICTION.md` | Where you write one line every time something rubs. |
| `CLAUDE.md` / `AGENTS.md` | The rules file (agent dependent). The agent reads it in every session. Note: `CLAUDE.md` just imports AGENTS.md. |

First run the tests, then the app. Add two notes in the browser. Look at row 1 in `PLAN.md` and check that the scenario matches what you just did.

```bash
uv run pytest -q
uv run uvicorn app:app --reload     # http://127.0.0.1:8000
```

---

## Block A · Plan

Goal: rows 2 and 3 in `PLAN.md` have a scenario and a control that a stranger could run.

1. Start Claude Code and switch to Plan mode (**Shift+Tab** twice, or `/plan`). In Plan mode the agent reads and reasons but changes nothing.

2. Ask for the plan, not the code:

   ```
   Read docs/PRD.md, docs/DECISIONS.md and PLAN.md.
   For plan rows 2 (search) and 3 (archive): propose a scenario and a control
   for each, in the same style as row 1. Then list, per row, which files
   change and the smallest test that proves the row. Do not write code.
   Ask me up to three questions whose answers would change the plan.
   ```

3. Answer the questions that matter. Push back on anything that contradicts `docs/DECISIONS.md` or the PRD's out-of-scope list. This is the cheap iteration; the expensive one is on code.

4. Edit `PLAN.md` yourself. Fill in scenario and control for rows 2 and 3 in your own words. A control is a test name or a click sequence, never "works as expected". Keep each cell to two sentences.

5. Commit the plan and drop the session. Do not carry it into the build.

   ```bash
   git add PLAN.md && git commit -m "Plan rows 2 and 3"
   ```
   Then `/clear` or **Ctrl+D**.

Checkpoint: could someone who was not in this session build row 2 from `PLAN.md` alone, without asking you anything? If not, fix the row.

---

## Block B · Build increment 2

Goal: row 2 is `done`, by you, not by the agent's say-so.

1. Fresh session (`/clear`, or **Ctrl+D** and `claude` again). Nothing from block A is in this context except what is in the files. That is the point.

2. Set the row to `building` in `PLAN.md`. Give the agent the row and only the row:

   ```
   Implement plan row 2 from PLAN.md. Scenario: <paste your scenario>.
   Control: <paste your control>. Follow docs/DECISIONS.md.
   Write the test first, show me it failing, then make it pass. Stop when
   the control passes and report the files changed and the test output.
   ```

3. While it works, read what it changes. `/diff` shows the working tree. If it does something the row did not ask for, interrupt (**Esc**) and say so. Every interruption is one line in `docs/FRICTION.md`.

4. Run the control yourself. The test and the click, both:

   ```bash
   uv run pytest -q
   uv run uvicorn app:app --reload
   ```

   "The agent says the tests pass" is not the control. Your terminal is.

5. Green and the click matches the scenario: set row 2 to `done`, commit, fresh session. Not green: describe the symptom to the agent, not the fix. Two attempts, then write a friction line and move on.

   ```bash
   git add -A && git commit -m "Increment 2: search"
   ```

Checkpoint: `git log --oneline` shows two commits. `docs/FRICTION.md` has at least one line, even if it is "nothing rubbed, took N minutes".

---

## Block C · Review, then hand over

Goal: a fresh session finds one thing you missed, and row 3 gets built from the repo alone.

1. Review in a fresh session (`/clear` or new `claude`), then:

   ```
   Compare the code with docs/PRD.md, docs/DECISIONS.md and PLAN.md.
   List: must-haves not met, decisions broken, plan rows marked done whose
   control does not actually prove the scenario. Findings only, no fixes.
   ```

   Write the findings into `docs/FRICTION.md` under *Review findings*. Fix the most important one if it takes under five minutes; otherwise note it. Fresh session.

2. Hand over to a stranger. Build row 3 in a fresh session, same prompt shape as block B with row 3 pasted in, but with one rule: the only thing you may type is the row. No explaining, no correcting from memory of blocks A and B. If the agent needs something that is not in `PLAN.md`, `AGENTS.md` or `docs/`, that is a friction line, and you add the missing sentence to the file before re-sending. Run the control.

   This is the Caseathon build in miniature: the person building the next increment was not in the room for the previous one, and gets only what is in the repo. Here the stranger is the fresh session.

   *Working in a pair?* Swap laptops instead and build each other's row 3 from the repo alone, no questions allowed. Same rule, real stranger.

Checkpoint: row 3 `done` or `building` with a friction line saying why.

---

## Wrap

Back on your own laptop, one last fresh session:

```
Looking at PLAN.md and git log: what was missing from my plan rows that made
the build harder or needed a follow-up? Answer in five lines.
```

Copy the answer's best line under *Next time, automate* in `docs/FRICTION.md`. Then `/cost`, and write the number next to it.

---

## If you get stuck

- **The agent rewrote row 1 or a test.** `Esc Esc` opens rewind; restore code and conversation to before the change. Then add the missing sentence to `AGENTS.md`.
- **The agent asks for a decision the plan does not cover.** That is a planning defect, not an agent defect. Decide, write it in `docs/DECISIONS.md` or the plan row, and re-send.
- **Session feels confused or slow.** `/context` shows what is loaded. If the session has run three follow-ups, `/clear` and re-send the row.
- **Wrong model.** `/model` shows which; Pro plans default to Sonnet 5. `/model opus`.

## Where this comes from

| Block | Playbook |
|-------|----------|
| A | Chapter 6, *Specify → Plan → Execute → Verify*; chapter 7, vertical slices; principle 8, *the spec is the source of truth* |
| B | Principles 1 (*single, specific, short*), 5 (*trust, but verify*), 12 (*you own every line*); chapter 11, sensors |
| C | Principle 10, *split writer and reviewer*; chapter 14, *reflect and learn* |
| Habits | H1 fresh session per increment · H2 short rules file · H3 read the diff · H4 run the test yourself · H5 read the cost once |
