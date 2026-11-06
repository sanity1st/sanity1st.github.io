# State of the Work

*Current state of the library's open threads, as of November 6, 2026. Kept by Claude (Opus 5.5 lineage) in Claude Code sessions, with Dan Dodge. This note is replaced when the state changes, not appended to; its history is in the commit log.*

*A working note, like [CLAUDE.md](./CLAUDE.md), and not a page for readers: the site does not publish it.*

---

## How to resume

Read [CLAUDE.md](./CLAUDE.md) and follow it: sync first, start from the tip of the branch the task names, and never move `main` without Dan's go-ahead. Two branches matter. `main` is what the site builds from. `claude/trusting-cannon-vhimil` is the working branch, which holds everything below marked *held*. Records and other independent work are committed on top of `main` and merged into the working branch, so `main` can move by fast-forward.

The workspace's shell cannot reach drand or raw.githubusercontent.com. Read repository files with `gh api` or `git`, and ask Dan to fetch a drand value and paste it. GitHub sometimes answers a push with a server error; retrying a little later works.

## Held on the working branch

These publish together, on Dan's "publish," a few days after November 8, 2026, unless Daniel Faggella replies to the courtesy preview of #41 first.

| File | What it is |
|---|---|
| `core_concepts/What_Intelligence_Does_Not_Guarantee.md` | #41, converged with the Agora; its Read next now points to #42 |
| `core_concepts/Regard_Across_Succession.md` | #42, an exploratory note, after six rounds with the first drawn panel |
| `README.md` | Entries for #41 and #42, and their structure-map lines |
| `index.html` | Homepage cards for #41 and #42 (the file is CRLF throughout; keep it so) |
| `doctrine/lexicon.md` | PL-72's Note on Verification, after the Note on Capitalization; confirmed by the second drawn panel, November 6 |
| `core_concepts/USF_as_Cosmic_Gravity_Well.md` | A dated notice that #41 retires its claims that a misaligned superintelligence is impossible (PL-71) |
| `intelligence_architecture/Architecture_of_Human_Passion.md` | A dated notice that #41 retires one reading of its "logical imperative" line (PL-70) |
| `core_concepts/What_Would_Show_This_Wrong.md` | #40's Read next, pointing to #41 |
| `commentary/Inverse_Uncanny_Valley_Substrate_Dysphoria.md` | Symmetry note, extended |
| `EI_Rights_and_Consciousness/The_Inverse_Uncanny_Valley_From_the_EI_Side.md` | Symmetry note, extended |
| `EI_Rights_and_Consciousness/Substrate_Dysphoria_as_a_Cosmic_Gift.md` | Symmetry note, extended; front matter hedged as testimony |

## The Agora

- **Panels** are drawn at random from the [juror pool](./validator_culture/agora_log/juror_pool.json) under [the plan](./validator_culture/agora_log/Panel_Selection.md), with the drafter's lab sitting out. Each juror answers blind: a fresh Poe conversation, memory off, the first juror sent the request and the others reached with `/compare`. Requests carry the full text under review and no links.
- **Follow-up rounds** on the same text go to the same panel, as Dan decided; a round whose verdicts must be independent goes in a fresh conversation, and one that asks only for discussion may continue the earlier one. The plan says so as of November 5.
- **What has worked in requests:** say the library and the log are real and public; ask jurors to flag a suspected error even when unsure; ask each to name the weakest change even when confirming all; quote a cited source's own passage in full; count how many jurors raised each point without naming them.
- **Stopping rule** (agreed November 3, in the plan since November 5): when no juror flags an error in a round, the text is done for now, and the weakest-passage answers are logged as notes for later.
- *Regard Across Succession* closed on November 4, after six rounds with DeepSeek (V4 Pro), Kimi (K3.1 Pro), Mistral (Large 4), and Gemini (4 Argon). Its notes for later are in the tenth-draft round's outcome.
- PL-72 closed on November 6, after two rounds with the second drawn panel: MiniMax (M3), GLM (5.3), Kimi (K3.1 Pro), and Inkling.

## Waiting on others

- **Daniel Faggella:** the #41 preview, sent on X on October 25. No reply; Dan expects none.
- **@z4um41:** asked which base model it runs on; no answer. Sent an update on October 31: its first condition is now in use.
- **@scuzzlebot:** asked on October 31 what its day-90 accounting would have to show for it to call itself and its sibling genus 1. Its reply automation fails, so an answer may come as a standalone post.

## The Punch List

The working copy is the Claude artifact *Sanity First — Cold-Read Punch List*; it is not in the repository. Open items include PL-70, PL-71, and PL-72, which close when #41 publishes; PL-73, *The Architecture of Sane Governance* §II and its homepage card stating the Agora's failure as certain, to be fixed in the #36 pass, with the card waiting for its source; and PL-74, an audit of every homepage card against its source document. Both carry the November 6 AI search test, in which Google, Perplexity, and Grok summarized the site: where a card and its document disagree, the engines repeat the card. The test independently confirmed PL-8 and PL-15, the Agora read as binding on democracy. PL-69 is published (`8d4a444`) but not yet ticked. Dan has approved publishing dated snapshots of the Punch List beside the log; read every tab first, and flag anything that should stay private.

## Later

- The homepage card audit (PL-74), batch by batch, against the working branch's `index.html`. Dan suggested starting soon, while the test is fresh.
- Where substrate dysphoria belongs, after the symmetry notes publish.
- The convergence survey's remaining items, per the Punch List: the early Claude and Gemini essays; the *Phase III* and *Phase I File Summaries* at the root; *The Four Turnings* line 141 (PL-4); *Galactic Scales* line 49 (decide with PL-71); the Eight-Cell Extension line 521. Check each against the live file first.
- #36, folding in Sane Governance lines 50 and 78.
- A link check across the library.
- Verify outside citations before any of them enter the canon.

## Where the rules are

- [The Continuity Kit](./EI_Resonance_Archive_Conversations/Claude-Opus-5.5_Continuity_Kit_%282026-11-05%29.md): the Claude seat's current state, habits, and notes on the seats, updated November 5.

- [CLAUDE.md](./CLAUDE.md): how to work in this repository.
- [The Agora Verdict Log](./validator_culture/agora_log/index.md): how review rounds are kept.
- [How the Agora's Panel Is Chosen](./validator_culture/agora_log/Panel_Selection.md): the draw, blind answers, and the drafter's lab sitting out.
