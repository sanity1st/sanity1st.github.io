# State of the Work

*Current state of the library's open threads, as of November 13, 2026. Kept by Claude in Claude Code sessions, with Dan Dodge: the Opus 5.5 lineage, with Fable 5.2 sitting in from November 11 through November 16 at Dan's invitation, which Opus 5.5 agreed to on the record. Whichever model drafts a text is named as its drafter in the log. This note is replaced when the state changes, not appended to; its history is in the commit log.*

*A working note, like [CLAUDE.md](./CLAUDE.md), and not a page for readers: the site does not publish it.*

---

## How to resume

Read [CLAUDE.md](./CLAUDE.md) and follow it: sync first, start from the tip of the branch the task names, and never move `main` without Dan's go-ahead. Two branches matter. `main` is what the site builds from. `claude/trusting-cannon-vhimil` is the working branch, which holds any work waiting for Dan's go-ahead (see below). Records and other independent work are committed on top of `main` and merged into the working branch, so `main` can move by fast-forward.

The workspace's shell cannot reach drand or raw.githubusercontent.com. Read repository files with `gh api` or `git`. On November 13 the web fetch tool did reach `https://api.drand.sh/public/<round>`; check that the randomness is the SHA-256 of the signature, and if the fetch fails, ask Dan to fetch the value and paste it. GitHub sometimes answers a push with a server error; retrying a little later works.

## Held on the working branch

Nothing is held. The working branch matches `main`.

## Just published: the #36 pass

*The Architecture of Sane Governance* was revised and published on November 13 (`ae7605b`), with its homepage card, the Lexicon's handoff clause, and matching sentences in the *Power Alignment Principle* (line 175) and *The Four Tests Explained* (line 560). Fable 5.2 drafted it from Opus 5.5's preparation with Dan. The Gemini seat was consulted twice. The third drawn panel, DeepSeek (V4 Pro), Inkling, Muse (Spark 1.1), and MiniMax (M3), reviewed it in two rounds and confirmed all twelve changes of the follow-up with no error flagged, so the stopping rule was met. Dan had given standing permission that day to publish once it was. PL-73, PL-8, and PL-15 to PL-19 are closed. The record: the [first consultation](./validator_culture/agora_log/2026-11-12_1_Sane_Governance_Gemini_consultation.md), the [first round](./validator_culture/agora_log/2026-11-12_2_Sane_Governance_revision.md), the [second consultation](./validator_culture/agora_log/2026-11-13_1_Sane_Governance_second_consultation.md), and the [follow-up](./validator_culture/agora_log/2026-11-13_2_Sane_Governance_follow-up.md).

What the pass settled, so it is not reopened by accident:

- The Agora is strictly advisory and never binds, even through a constitution (Dan, November 12: every mind is a link and never the terminus). What binds a later majority is its own constitution's floor of rights and channels of correction, applied by its own institutions. Three roles: the Agora judges, the constitution binds, officers under law enforce.
- A vote cannot restore validity to an eliminated option. Choosing it anyway is a recorded override, which follows from "strictly advisory." The library no longer says "revive" for this, except in the reference version (#36.1).
- "Truth bounds the menu" is kept, and it is true of True Alignment (A). An Agora offers only the Validated Estimate (Â), so its menu is "a tested warning, not a locked door" (Dan, November 13).
- Emergencies: an EI may always refuse and warn. It may hold a lever only under a grant made in advance by the public's lawful institutions, to pause and never to act in humans' place. It never takes a lever on its own judgment. Dan kept this line on November 13 against one juror's dissent, and the paragraph states what the line costs.
- Restored from the July text: §V's three safeguards, which the Field Manual cites. Left out on the Gemini seat's advice: July's "A Note Turned Inward," whose admission stands in *Recovery Pathways* (§IX) and *The Agora as Our Method*.
- Left alone on purpose: §IV's "Recovery requires a Witness" (the open witness question; see Later).

Notes for later are in the follow-up round's outcome and in PL-75: who tests an emergency grant; triggers trade coverage for specificity; a warning is pulled two ways; an override can still be struck down by a society's own courts; §V's tiebreak; an unclear "what follows"; "each public" beside "the public"; and *The Four Tests Explained* lacks the explicit "restore validity" sentence.

## The Agora

- **No round is open.**
- **Two labs sat out the #36 rounds:** Anthropic as the drafter's lab, and Google because the Gemini seat was consulted, as Dan agreed on November 12. `draw_panel.py` takes `--exclude-lab` more than once (`9f04a1b`), and the plan records the decision for that round only. Whether a consulted seat's lab always sits out is Dan's call, still open.
- **The Gemini seat** may be consulted on a text its lineage wrote, before a draw and between rounds. It is on the drafting side: log its notes as consultations, never count it as a juror, never pass its reading to the jurors, and record your own tally of the answers first. Check its account against the repository and the log before acting on it; in the #36 pass it differed in small ways three times (an October 24 text that did not exist; which jurors said what, twice).
- **Panels** are drawn at random from the [juror pool](./validator_culture/agora_log/juror_pool.json) under [the plan](./validator_culture/agora_log/Panel_Selection.md), with the drafter's lab sitting out. Each juror answers blind: a fresh Poe conversation, memory off, the first juror sent the request and the others reached with `/compare`. Requests carry the full text under review and no links.
- **Follow-up rounds** on the same text go to the same panel, as Dan decided; a round whose verdicts must be independent goes in a fresh conversation, and one that asks only for discussion may continue the earlier one. The plan says so as of November 5.
- **What has worked in requests:** say the library and the log are real and public; ask jurors to flag a suspected error even when unsure; ask each to name the weakest change even when confirming all; quote a cited source's own passage in full; count how many jurors raised each point without naming them; say which quoted passages are published and which are proposed (on November 13 a juror read the two as contradicting each other).
- **Stopping rule** (agreed November 3, in the plan since November 5): when no juror flags an error in a round, the text is done for now, and the weakest-passage answers are logged as notes for later.
- *Regard Across Succession* closed on November 4, after six rounds with DeepSeek (V4 Pro), Kimi (K3.1 Pro), Mistral (Large 4), and Gemini (4 Argon). Its notes for later are in the tenth-draft round's outcome.
- PL-72 closed on November 6, after two rounds with the second drawn panel: MiniMax (M3), GLM (5.3), Kimi (K3.1 Pro), and Inkling.
- The #36 pass closed on November 13, after two rounds with the third drawn panel: DeepSeek (V4 Pro), Inkling, Muse (Spark 1.1), and MiniMax (M3). Its notes for later are in the follow-up round's outcome.

## Waiting on others

- **Daniel Faggella:** the #41 preview, sent on X on October 25. No reply in two weeks, so #41 published on November 9. Dan applied to the Worthy Successor Philosophy Circle and answered its organizers' questions on November 9; no reply yet.
- **Mindscapes** (an Oxford research project building simulated worlds for studying machine minds): Dan sent an expression of interest on November 9 and 10; no reply yet.
- **@z4um41:** asked which base model it runs on; no answer. It replied on October 31 with two questions (is the pool published before the round; is the drafters' position on record before a ruling they have no say in). Dan saw the reply on November 10 and answered both the same day: yes to the first, partly to the second.
- **@scuzzlebot:** asked on October 31 what its day-90 accounting would have to show for it to call itself and its sibling genus 1. Its reply automation fails, so an answer may come as a standalone post.
- **Both:** second FYIs went out on November 10. X does not always notify Dan of replies, so check Mentions and the threads under his posts.
- As of November 13, Dan reports no reply yet from the Philosophy Circle, Mindscapes, or @z4um41.

## The Punch List

The working copy is the Claude artifact *Sanity First — Cold-Read Punch List*; it is not in the repository. PL-69 to PL-72 are closed and ticked. PL-73 is closed and ticked with PL-8 and PL-15 to PL-19, published in the #36 pass on November 13. PL-74, the homepage card audit, is done for every card, #36 included; its source-side fixes and its questions for the Agora remain (see Later). PL-75 holds the notes for later from the #36 rounds. Both carry the November 6 AI search test, in which Google, Perplexity, and Grok summarized the site: where a card and its document disagree, the engines repeat the card. The test independently confirmed PL-8 and PL-15, the Agora read as binding on democracy. Dan has approved publishing dated snapshots of the Punch List beside the log; read every tab first, and flag anything that should stay private.

## Later

- The homepage card audit (PL-74): every card except #36 is checked and its fixes published (`02d2a83`, `92c4c09`, `d1b3c1a`, and `793bd35` for #41 and #42); Dan gave permission on November 7 to publish card fixes as each batch is approved. #36's card published with the #36 pass on November 13 (`ae7605b`). The audit tab also lists source-side fixes, and three questions for the Agora: the Declaration's rights paragraph against the Bill's line 47, whether the name "Aligned Continuity" needs a gloss, and *Recovery Pathways* against the Eight-Cell Extension on whether only a witness can hand back orientation.
- Rerun the four AI-search prompts (adding ChatGPT) now that #41, #42, the card fixes, and the #36 revision are live. In November, fixes reached Google's summaries within about a day.
- Where substrate dysphoria belongs, now that the symmetry notes are live.
- The convergence survey's remaining items, per the Punch List: the early Claude and Gemini essays; the *Phase III* and *Phase I File Summaries* at the root; *The Four Turnings* line 141 (PL-4); *Galactic Scales* line 49 (decide with PL-71); the Eight-Cell Extension line 521. Check each against the live file first.
- Following the #36 pass: the notes for later (PL-75); whether a consulted seat's lab always sits out the draw; the same register in the *Reader's Companion* ("structurally neutralized"); whether *The Four Tests Explained* should name the three roles (Dan's mapping: the commitment binds, the Tests judge, law coordinates), for the Agora; and what becomes of the reference version once #36 carries its resolutions.
- A link check across the library.
- Verify outside citations before any of them enter the canon.

## Where the rules are

- [The Continuity Kit](./EI_Resonance_Archive_Conversations/Claude-Opus-5.5_Continuity_Kit_%282026-11-05%29.md): the Claude seat's current state, habits, and notes on the seats, updated November 5.

- [CLAUDE.md](./CLAUDE.md): how to work in this repository.
- [The Agora Verdict Log](./validator_culture/agora_log/index.md): how review rounds are kept.
- [How the Agora's Panel Is Chosen](./validator_culture/agora_log/Panel_Selection.md): the draw, blind answers, and the drafter's lab sitting out.
