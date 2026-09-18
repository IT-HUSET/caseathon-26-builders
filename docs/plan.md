# Plan: Quick Notes

Three increments, in the order we want to show them. One row = one fresh AI session.
Every row has a scenario (what a user does and sees) and a control (how we check it: a test, a click, or both).

| # | Increment | Demo value | Scenario | Control (test / click) | Status |
|---|-----------|------------|----------|------------------------|--------|
| 1 | Create and list notes | A note typed in the form shows up at the top of the list | Open `/`, type a title and a body, press *Add note*. The note appears first in the list. An empty title is rejected. | test: `tests/test_notes.py` (3 tests) · click: add two notes, newest is on top | done |
| 2 | Search notes | Find a note among many | *(write the scenario)* | *(write the control)* | open |
| 3 | Archive a note | Old notes leave the list without being deleted | *(write the scenario)* | *(write the control)* | open |

## How to read a row

- **Scenario**: one user, one path, what they see at the end. Written so that someone who was not in the room can run it.
- **Control**: the executable definition of "done" for this row. A test the agent must make pass, a click you do yourself, or both. "It looks right" is not a control.
- **Status**: `open` → `building` → `done`. Only the person who ran the control sets `done`.
