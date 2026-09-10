# PRD: Quick Notes

**Problem.** People jot things down in whatever is open and lose them by the afternoon. One place, no accounts, no sync, no phone app.

**Users.**
- *Mia, consultant*: dumps thoughts between meetings, needs to find them again a week later.
- *Jonas, on-call engineer*: keeps a running log during an incident, wants the old entries out of the way afterwards without losing them.

**Must-haves (3–5).**
1. Add a note with a title and an optional body; the newest note is on top.
2. Find a note by a word in its title or body.
3. Archive a note so it leaves the main list; archived notes can still be seen.
4. Everything survives a restart.

**Out of scope.** Accounts, sharing, editing existing notes, tags, mobile app, rich text.

**Demo goal.** "At the end of the session we show: add three notes, search for one word, archive one note, refresh the page, and everything is still there."

**Assumptions we made instead of asking.**
- Search is case-insensitive substring match; no ranking.
- Archived notes are hidden by default and visible on a separate view or toggle.
