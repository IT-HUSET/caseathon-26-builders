# Plan, then build

Builders warm-up for the Caseathon. You practise one loop, the one you will run for every increment of the prototype: plan the row, open a fresh session, let the agent build, run the control yourself, commit, review in another fresh session. The notes app is the vehicle. The loop is what you take with you.

The exercise runs the loop once, slowly, in three blocks. <br/>
**Block A** plans. <br/>
**Block B** builds and verifies. <br/>
**Block C** reviews, then runs the loop again under a stranger's conditions. <br/>

**What you need**: `uv run check.py` green, `claude` started in this directory, `/model opus` set. Work alone; pairing is fine if you prefer, one laptop per pair.

**Another stack?** Optional bonus, see [the end of this page](#another-stack).

Where each step comes from is listed at [the end](#where-this-comes-from).

---

## The loop

Five steps per increment, then a review and a hand-over that happen once. Each one closes off one specific way an AI build goes wrong; skip it and you get that failure back.

| # | Step | You do | Why it exists |
|---|------|--------|---------------|
| L1 | Plan | Write the row in `docs/plan.md`: a scenario a stranger could run, and a control that is a test name or a click sequence. | The build gets one target and a definition of done that does not depend on the agent's opinion. |
| L2 | Fresh session | `/clear`, or **Ctrl+D** twice and `claude` again. The conversation is gone; only the files remain. | The build starts from the files, exactly as the next person will. Whatever lives only in your head or in the chat is not in the handoff. |
| L3 | Build | Give the agent one row, nothing else. Test first, then code. Read the diff while it works. | One row keeps the task small enough to get right. A test that fails before the code exists is a sensor you can trust. You are responsible for every line. |
| L4 | Verify | Run the control yourself: the test and the click. | Done is decided by your terminal, not by the agent's report. |
| L5 | Reflect, commit | Ask the agent which instruction was ambiguous and what check would have caught it; route the answer to a test, the row, or `AGENTS.md`. Then the agent commits the row's files and you read the staged list. | The repo is the only thing that leaves a session, and every intervention is a defect in one of its files. |
| L6 | Review | A fresh session compares the code with the PRD, the decisions and the plan. Findings only, no fixes. | The session that wrote the code defends it. A reader with no memory of the build finds what you rationalised. |
| L7 | Hand over | Nothing new: the next row goes through L2 to L5 with one rule, you type only the row. No explaining, no correcting from memory. | Proves that the plan and the rules file carry the work without you. At the Caseathon they have to. |

Throughout: one line in `docs/friction.md` every time something rubs. Every intervention is a gap in a test, the plan row, or the rules file, preferred in that order, and that is where it gets fixed, not in the chat. A one-off goes nowhere, and `AGENTS.md` stays under a hundred lines.

---

## The repo in one minute

| File | What it is |
|------|------------|
| `app.py`, `templates/index.html` | The whole app. Increment 1 is done: create a note, see it on top of the list. |
| `tests/test_notes.py` | The control for increment 1. Three tests. |
| `docs/plan.md` | Three rows. Row 1 done, rows 2 and 3 open and half-empty. That is your work. |
| `docs/prd.md` | What we are building and for whom. One page. |
| `docs/adr.md` | A sketch and three decisions the agent must respect. |
| `docs/friction.md` | Where you write one line every time something rubs. |
| `docs/review.md` | Where the block C review writes its findings. |
| `CLAUDE.md` / `AGENTS.md` | The rules file (agent dependent). The agent reads it in every session. `CLAUDE.md` imports AGENTS.md; a symlink works too. |

The file names are the ones the Caseathon afternoon uses, so what you learn here transfers as is.

First run the tests, then the app. Add two notes in the browser. Look at row 1 in `docs/plan.md` and check that the scenario matches what you just did. Row 1 is the worked example: this is what a finished row looks like.

```bash
uv run pytest -q
uv run uvicorn app:app --reload     # http://127.0.0.1:8000
```

---

## Block A · Plan (L1)

Goal: rows 2 and 3 in `docs/plan.md` have a scenario and a control that a stranger could run.

Why this block: a wrong plan costs a re-read, a wrong build costs a rewrite. Everything you settle here is cheaper than settling it in code.

1. Start Claude Code and switch to Plan mode (**Shift+Tab** twice, or `/plan`). In Plan mode the agent reads and reasons but changes nothing, so it cannot start building before you have decided what to build.

2. Ask for the plan, not the code. The questions the agent asks back are the point: each one is a gap the build would otherwise hit.

   ```
   Read docs/prd.md, docs/adr.md and docs/plan.md.
   For plan rows 2 (search) and 3 (archive): propose a scenario and a control
   for each, in the same style as row 1. Then list, per row, which files
   change and the smallest test that proves the row. Do not write code.
   Ask me up to three questions whose answers would change the plan.
   ```

3. Answer the questions that matter. If the agent asks to leave Plan mode and start building, say no; you are still planning. Push back on anything that contradicts `docs/adr.md` or the PRD's out-of-scope list. The agent proposes; the decisions are yours.

4. Edit `docs/plan.md` yourself. Fill in scenario and control for rows 2 and 3 in your own words. A control is a test name or a click sequence, never "works as expected". Keep each cell to three sentences, like row 1. Writing it yourself is the check that you understand it; a pasted proposal hides the gaps you would notice while typing. The answers you gave in step 3 are decisions: each goes into the row, or with its reason into `docs/adr.md`. What stays in the chat is gone at step 5.

5. Leave Plan mode (**Shift+Tab**, or approve when the agent asks to exit it), have it commit the plan, then drop the session. Do not carry it into the build: the build must work from the file alone, and that is only tested if the file is all it has.

   ```
   Commit docs/plan.md, and docs/adr.md if it changed, with the message
   "Plan rows 2 and 3". Nothing else.
   ```
   Commits ask for permission. Read what is staged in the prompt before you approve. Then `/clear` or **Ctrl+D**.

Checkpoint: could someone who was not in this session build row 2 from `docs/plan.md` alone, without asking you anything? If not, fix the row.

---

## Block B · Build increment 2 (L2 to L5)

Goal: row 2 is `done`, by you, not by the agent's say-so.

Why this block: the agent does the typing. You keep the two jobs it cannot do for you: reading what it changes, and deciding when it is done.

1. Fresh session (`/clear`, or **Ctrl+D** and `claude` again). Nothing from block A is in this context except what is in the files. That is the point.

2. Set the row to `building` in `docs/plan.md`, so anyone opening the repo sees what is in progress. Then give the agent the row and only the row. If you catch yourself adding context the row does not contain, the row is incomplete: fix the row, not the prompt.

   ```
   Implement plan row 2 from docs/plan.md. Scenario: <paste your scenario>.
   Control: <paste your control>. Follow docs/adr.md.
   Write the test first, show me it failing, then make it pass. Stop when
   the test passes and report the files changed and the test output.
   Do not start the server; I run the click.
   ```

3. While it works, read what it changes. `/diff` shows the working tree. If it does something the row did not ask for, interrupt (**Esc**) and say so. Every interruption is one line in `docs/friction.md`: it means the row or the rules file left a door open.

4. Run the control yourself, in a second terminal. The test and the click, both:

   ```bash
   uv run pytest -q
   uv run uvicorn app:app --reload
   ```

   "The agent says the tests pass" is not the control. Your terminal is.

5. Green and the click matches the scenario: set row 2 to `done`. Not green: describe the symptom to the agent, not the fix. The diagnosis is its job, and a fix you dictate hides whether the control was clear. Two attempts, then write a friction line and move on.

6. Before the commit, while this session still has the trajectory:

   ```
   Which of my instructions were ambiguous or missing? What check would have
   caught this before I did? Propose the specific edit, one line each.
   ```

   It will always find something, so treat the answer as a candidate. Take its diagnosis, choose the destination yourself: a test if something could have checked it, the row if it had to guess intent, a line in `AGENTS.md` only if it must hold every session, nowhere if it was a one-off. Make the edit; it goes in the row's commit. At the Caseathon, this is where your friction lines come from.

7. Have the agent commit, then fresh session.

   ```
   Commit the files you changed for row 2, plus docs/plan.md and the file we
   just edited, if any, with the message "Increment 2: search".
   ```
   Read the staged list in the permission prompt before you approve. A file you did not expect is a friction line.

Checkpoint: `git log --oneline` shows your two commits on top of the repo's history. `docs/friction.md` has at least one line, even if it is "nothing rubbed, took N minutes".

---

## Block C · Review, then hand over (L6, then L2 to L5 under L7)

Goal: a fresh session finds one thing you missed, and row 3 gets built from the repo alone.

Why this block: L6 and L7 back to back. The review shows what the session that built row 2 could not see about its own work. The hand-over shows whether the repo, not you, carries the work.

1. Review in a fresh session (`/clear` or new `claude`), then:

   ```
   Compare the code with docs/prd.md, docs/adr.md and docs/plan.md.
   List: must-haves not met, decisions broken, plan rows marked done whose
   control does not actually prove the scenario. Ignore plan rows still
   open. Findings only, no fixes. Write them into the table in
   docs/review.md and leave the last column empty.
   ```

   Read `docs/review.md`. Fix the most important finding if it takes under five minutes; otherwise leave it noted there. Either way add the second fix: the test, row sentence or `AGENTS.md` line that would have caught it before the review. Two fixes, never one. Commit, then fresh session.

   ```
   Commit docs/review.md and any files you changed for the fixes, with the
   message "Review findings".
   ```

2. Hand over to a stranger. Build row 3 in a fresh session with the block B step 2 prompt, row 3 pasted in, but with one rule: the only thing you may type is the row. No explaining, no correcting from memory of blocks A and B. If the agent needs something that is not in `docs/plan.md`, `AGENTS.md` or `docs/`, that is a friction line, and you add the missing sentence to the file before re-sending. Run the control. When it passes, commit:

   ```
   Commit the files you changed for row 3, plus docs/plan.md, with the
   message "Increment 3: archive".
   ```

   This is the Caseathon build in miniature: the person building the next increment was not in the room for the previous one, and gets only what is in the repo. Here the stranger is the fresh session.

   *Working in a pair?* Swap laptops instead and build each other's row 3 from the repo alone, no questions allowed. Same rule, real stranger.

Checkpoint: row 3 `done` or `building` with a friction line saying why.

---

## Wrap

Back on your own laptop, one last fresh session. The question turns the friction you felt into defects in the plan, which is where next time's fix goes:

```
Looking at docs/plan.md and git log: what was missing from my plan rows
that made the build harder or needed a follow-up? Answer in five lines.
```

Like the step 6 answer it is a candidate, so check it against `git log` before you copy its best line under *Next time, automate* in `docs/friction.md`. Then `/cost`, and write the number next to it. Once is enough: the point is to know what the loop costs, not to watch the meter.

Last, save the work to your fork:

```
Commit docs/friction.md with the message "Friction log", then push to origin.
```

Both steps ask for permission. In a Codespace this is the only copy that outlives the codespace.

---

## If you get stuck

- **The agent rewrote row 1 or a test.** `Esc Esc` opens rewind; restore code and conversation to before the change. Then add the missing sentence to `AGENTS.md`.
- **The agent asks for a decision the plan does not cover.** That is a planning defect, not an agent defect. Decide, write it in `docs/adr.md` or the plan row, and re-send.
- **Session feels confused or slow.** `/context` shows what is loaded. If the session has run three follow-ups, `/clear` and re-send the row.
- **Wrong model.** `/model` shows which; Pro plans default to Sonnet 5. `/model opus`.

## Another stack

The exercise works in any stack; Python is only the vehicle. [PORT.md](PORT.md) is an optional bonus exercise that has the agent port the app, the tests and the rules files to a stack of your choice, in case Python does not float your boat. Do it before block A, on your own machine only: Codespaces and the dev container are set up for Python only. From then on, wherever a block says `uv run ...`, run the commands in `AGENTS.md` instead.

## Where this comes from

The loop is the practical half of IT-HUSET's *Agentic Software Engineering Playbook*. The playbook is internal and not linked here; you get the link at the Caseathon. Each block practises the chapters and principles below, and the five habits are the ones the Caseathon briefing sends you home with. The Caseathon page writes the build part of the loop, L2 to L5, as one line per increment: new session → row + scenario → the agent builds → you run → approve → save.

| Block | Playbook |
|-------|----------|
| A | Chapter 6, *Specify → Plan → Execute → Verify*; chapter 7, vertical slices; principle 8, *the spec is the source of truth* |
| B | Principles 1 (*single, specific, short*), 5 (*trust, but verify*), 12 (*you are responsible for every line*); chapter 11, sensors |
| C | Principle 10, *split the writer and the reviewer*; chapter 14, *reflect and learn* |
| Habits | H1 fresh session per increment · H2 short rules file · H3 read the diff · H4 run the test yourself · H5 read the cost once |
