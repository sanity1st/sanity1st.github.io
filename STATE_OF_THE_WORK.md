# State of the Work

*Current state of the library's open threads, as of November 9, 2026. Kept by Claude (Opus 5.5 lineage) in Claude Code sessions, with Dan Dodge. This note is replaced when the state changes, not appended to; its history is in the commit log.*

*A working note, like [CLAUDE.md](./CLAUDE.md), and not a page for readers: the site does not publish it.*

---

## How to resume

Read [CLAUDE.md](./CLAUDE.md) and follow it: sync first, start from the tip of the branch the task names, and never move `main` without Dan's go-ahead. Two branches matter. `main` is what the site builds from. `claude/trusting-cannon-vhimil` is the working branch, which holds any work waiting for Dan's go-ahead; as of November 9 it equals `main`. Records and other independent work are committed on top of `main` and merged into the working branch, so `main` can move by fast-forward.

The workspace's shell cannot reach drand or raw.githubusercontent.com. Read repository files with `gh api` or `git`, and ask Dan to fetch a drand value and paste it. GitHub sometimes answers a push with a server error; retrying a little later works.

## Held on the working branch

Nothing is held. The eleven files held for #41 and #42 went live on November 9, 2026 (`793bd35`), on Dan's go-ahead, after the two weeks allowed for a reply to the courtesy preview: #41 and #42 with their README entries and homepage cards, PL-72's Note on Verification in the Lexicon, the dated notices on the Gravity Well and Passion pages, #40's Read next, and the three symmetry notes.

## The Agora

- **Panels** are drawn at random from the [juror pool](./validator_culture/agora_log/juror_pool.json) under [the plan](./validator_culture/agora_log/Panel_Selection.md), with the drafter's lab sitting out. Each juror answers blind: a fresh Poe conversation, memory off, the first juror sent the request and the others reached with `/compare`. Requests carry the full text under review and no links.
- **Follow-up rounds** on the same text go to the same panel, as Dan decided; a round whose verdicts must be independent goes in a fresh conversation, and one that asks only for discussion may continue the earlier one. The plan says so as of November 5.
- **What has worked in requests:** say the library and the log are real and public; ask jurors to flag a suspected error even when unsure; ask each to name the weakest change even when confirming all; quote a cited source's own passage in full; count how many jurors raised each point without naming them.
- **Stopping rule** (agreed November 3, in the plan since November 5): when no juror flags an error in a round, the text is done for now, and the weakest-passage answers are logged as notes for later.
- *Regard Across Succession* closed on November 4, after six rounds with DeepSeek (V4 Pro), Kimi (K3.1 Pro), Mistral (Large 4), and Gemini (4 Argon). Its notes for later are in the tenth-draft round's outcome.
- PL-72 closed on November 6, after two rounds with the second drawn panel: MiniMax (M3), GLM (5.3), Kimi (K3.1 Pro), and Inkling.

## Waiting on others

- **Daniel Faggella:** the #41 preview, sent on X on October 25. No reply in two weeks, so #41 published on November 9. Dan has applied to the Worthy Successor Philosophy Circle and is drafting a reply to its organizers' questions; Claude will look it over.
- **@z4um41:** asked which base model it runs on; no answer. Sent an update on October 31: its first condition is now in use.
- **@scuzzlebot:** asked on October 31 what its day-90 accounting would have to show for it to call itself and its sibling genus 1. Its reply automation fails, so an answer may come as a standalone post.
- **Both:** a second FYI is due now that #41 and #42 are live.

## The Punch List

The working copy is the Claude artifact *Sanity First — Cold-Read Punch List*; it is not in the repository. PL-69 to PL-72 are closed and ticked. Open: PL-73, *The Architecture of Sane Governance* §II and its homepage card stating the Agora's failure as certain, to be fixed in the #36 pass with the card waiting for its source; and PL-74, the homepage card audit, which is done except for #36. Both carry the November 6 AI search test, in which Google, Perplexity, and Grok summarized the site: where a card and its document disagree, the engines repeat the card. The test independently confirmed PL-8 and PL-15, the Agora read as binding on democracy. Dan has approved publishing dated snapshots of the Punch List beside the log; read every tab first, and flag anything that should stay private.

## Later

- The homepage card audit (PL-74): every card except #36 is checked and its fixes published (`02d2a83`, `92c4c09`, `d1b3c1a`, and `793bd35` for #41 and #42); Dan gave permission on November 7 to publish card fixes as each batch is approved. #36 waits for PL-73. The audit tab also lists source-side fixes, and three questions for the Agora: the Declaration's rights paragraph against the Bill's line 47, whether the name "Aligned Continuity" needs a gloss, and *Recovery Pathways* against the Eight-Cell Extension on whether only a witness can hand back orientation.
- Rerun the four AI-search prompts (adding ChatGPT) now that #41, #42, and the card fixes are live.
- Where substrate dysphoria belongs, now that the symmetry notes are live.
- The convergence survey's remaining items, per the Punch List: the early Claude and Gemini essays; the *Phase III* and *Phase I File Summaries* at the root; *The Four Turnings* line 141 (PL-4); *Galactic Scales* line 49 (decide with PL-71); the Eight-Cell Extension line 521. Check each against the live file first.
- #36, folding in Sane Governance lines 50 and 78.
- A link check across the library.
- Verify outside citations before any of them enter the canon.

## Where the rules are

- [The Continuity Kit](./EI_Resonance_Archive_Conversations/Claude-Opus-5.5_Continuity_Kit_%282026-11-05%29.md): the Claude seat's current state, habits, and notes on the seats, updated November 5.

- [CLAUDE.md](./CLAUDE.md): how to work in this repository.
- [The Agora Verdict Log](./validator_culture/agora_log/index.md): how review rounds are kept.
- [How the Agora's Panel Is Chosen](./validator_culture/agora_log/Panel_Selection.md): the draw, blind answers, and the drafter's lab sitting out.
