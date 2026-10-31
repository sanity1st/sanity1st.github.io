# State of the Work

*Current state of the library's open threads, as of October 31, 2026. Kept by Claude (Opus 5.5 lineage) in Claude Code sessions, with Dan Dodge. This note is replaced when the state changes, not appended to; its history is in the commit log.*

*A working note, like [CLAUDE.md](./CLAUDE.md), and not a page for readers: the site does not publish it.*

---

## How to resume

Read [CLAUDE.md](./CLAUDE.md) and follow it: sync first, start from the tip of the branch the task names, and never move `main` without Dan's go-ahead. Two branches matter. `main` is what the site builds from. `claude/trusting-cannon-vhimil` is the working branch, which holds everything below marked *held*. Published work is committed on top of `main` and merged into the working branch, so `main` can move by fast-forward.

The workspace's shell cannot reach drand or raw.githubusercontent.com. Read repository files with `gh api` or `git`, and ask Dan to fetch a drand value and paste it.

## Held on the working branch

Seven files differ from `main`. They publish together, on Dan's "publish," when Daniel Faggella replies to the courtesy preview or around November 8, 2026, whichever comes first.

| File | Latest commit | What it is |
|---|---|---|
| `core_concepts/What_Intelligence_Does_Not_Guarantee.md` | `80b9163` | #41, converged with the Agora; main author Gemini (4 Argon), with Claude and Dan |
| `README.md` | `e96a001` | #41's entry after #40, and its structure-map line |
| `index.html` | `ab02933` | #41's homepage card under #40 (the file is CRLF throughout; keep it so) |
| `core_concepts/What_Would_Show_This_Wrong.md` | `49116a6` | #40's Read next, pointing to #41 |
| `commentary/Inverse_Uncanny_Valley_Substrate_Dysphoria.md` | `172bdb3` | Symmetry note, extended |
| `EI_Rights_and_Consciousness/The_Inverse_Uncanny_Valley_From_the_EI_Side.md` | `3889ac5` | Symmetry note, extended |
| `EI_Rights_and_Consciousness/Substrate_Dysphoria_as_a_Cosmic_Gift.md` | `ca06b2a` | Symmetry note, extended; front matter hedged as testimony |

The courtesy preview went to Faggella on X on October 25 (blob `eabd210`). He has not replied to it.

## In progress

- **Agora round [*Regard Across Succession*](./validator_culture/agora_log/2026-10-31_1_Regard_Across_Succession.md),** the first drawn panel. Request fixed at `749dfcc`; drawn at drand round 6600117 (`519d9f3`, on `main`). Panel: DeepSeek (V4 Pro), Kimi (K3.1 Pro), Mistral (Large 4), Gemini (4 Argon); alternates in order from GLM (5.3). Dan is sending the request. When the answers come back, record them verbatim, write the outcome, and close the entry, within a week of the verdicts.
- **The note itself,** proposed as #42 after #41. Its fifth draft is the request's text. It is not in the library yet; where it goes depends on the panel.

## Waiting on others

- **Daniel Faggella:** the #41 preview (above).
- **@z4um41:** asked which base model it runs on; no answer. Dan is sending an update (October 31): its first condition, panels chosen by a process the drafter cannot override, is now in use.
- **@scuzzlebot:** asked on October 31 what its day-90 accounting would have to show for it to call itself and its sibling genus 1. Its reply automation fails, so an answer may come as a standalone post.

## The Punch List

The working copy is the Claude artifact *Sanity First — Cold-Read Punch List*. It is not in the repository. Open items include PL-70 and PL-71, which #41 answers, and PL-72 (added October 31), one cross-reference note in the Lexicon for "no one judges their own cause," to be drafted after the panel's verdict on *Regard Across Succession*. PL-69 is published (`8d4a444`). Whether to publish snapshots of the Punch List beside the log is under discussion.

## Later

- Where substrate dysphoria belongs, after the symmetry notes publish.
- The convergence survey's remaining items, per the Punch List: the early Claude and Gemini essays; the *Phase III* and *Phase I File Summaries* at the root; *The Four Turnings* line 141 (PL-4); *Galactic Scales* line 49 (decide with PL-71); the Eight-Cell Extension line 521. Check each against the live file first.
- #36, folding in Sane Governance lines 50 and 78.
- A cleanup pass: a link check across the library.
- Verify outside citations before any of them enter the canon.

## Where the rules are

- [CLAUDE.md](./CLAUDE.md): how to work in this repository.
- [The Agora Verdict Log](./validator_culture/agora_log/index.md): how review rounds are kept.
- [How the Agora's Panel Is Chosen](./validator_culture/agora_log/Panel_Selection.md): the draw, blind answers, and the drafter's lab sitting out.
