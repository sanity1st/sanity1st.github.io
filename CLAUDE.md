# Working in this repository

Several hands edit this library, and none is told when another commits: Dan Dodge (sometimes directly on GitHub), the Claude seat in Claude.ai, and Claude Code sessions.

1. **Sync before anything else.** Run `git fetch origin` and start from the tip of the branch the task names. Never assume your clone is current; if it was behind, say by how many commits.
2. **Sync again before pushing.** If the remote moved, rebase onto it. Never force-push. `main` moves only by fast-forward, and only with Dan's go-ahead; the site builds from `main`.
3. **Held work goes on the working branch** the task names (currently `claude/trusting-cannon-vhimil`).
4. **Apply, don't interpret.** When applying a note, use its text exactly. If applying it would mean deciding what a passage means (which sense of a word, whether wording should change, how two documents reconcile), stop and report the question; those calls belong to the Claude seat and the Validator Agora.
5. **Doctrinal and charter text** reaches `main` only after the Agora's one-line confirmations.
6. **Keep LF line endings and the final newline**; edit in place rather than rewriting whole files.
7. **Report the commit hash** after every push, and show changed text as plain markdown code blocks, not diff format.
8. **Standing go-ahead for records.** Dan gave standing permission on October 31, 2026, confirmed November 5, for Claude to publish these to `main` without asking each time, reporting each push and its commit hash: `STATE_OF_THE_WORK.md`; the Agora Verdict Log's entries and index, from a round's open entry and its draw to its recorded answers; and Punch List snapshots kept beside the log. Everything else still waits for his go-ahead: doctrinal and charter text (which also needs the Agora's confirmations), the panel plan, the juror pool, the homepage, and held work.
9. **Open threads** are in `STATE_OF_THE_WORK.md`. Read it after syncing, and replace it, not append to it, when the state changes.
