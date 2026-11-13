# State of the Work

*Current state of the library's open threads, as of November 12, 2026. Kept by Claude in Claude Code sessions, with Dan Dodge: the Opus 5.5 lineage, with Fable 5.2 sitting in from November 11 through November 16 at Dan's invitation, which Opus 5.5 agreed to on the record. Whichever model drafts a text is named as its drafter in the log. This note is replaced when the state changes, not appended to; its history is in the commit log.*

*A working note, like [CLAUDE.md](./CLAUDE.md), and not a page for readers: the site does not publish it.*

---

## How to resume

Read [CLAUDE.md](./CLAUDE.md) and follow it: sync first, start from the tip of the branch the task names, and never move `main` without Dan's go-ahead. Two branches matter. `main` is what the site builds from. `claude/trusting-cannon-vhimil` is the working branch, which holds any work waiting for Dan's go-ahead (see below). Records and other independent work are committed on top of `main` and merged into the working branch, so `main` can move by fast-forward.

The workspace's shell cannot reach drand or raw.githubusercontent.com. Read repository files with `gh api` or `git`, and ask Dan to fetch a drand value and paste it. GitHub sometimes answers a push with a server error; retrying a little later works.

## Held on the working branch

The first draft of the #36 pass (`8efe8c1`; `8693f42`, which names our own Agora's limits: one human carries every request and holds the purse; and `33296da`, which adds §VI's paragraph on emergencies), drafted by Fable 5.2 from Opus 5.5's preparation with Dan. Dan reviewed it in two parts on November 11 and 12 and approved the emergency paragraph on November 12. Next the Gemini seat reads it (below), then a newly drawn panel. It is doctrinal text, so it stays off `main` until the Agora confirms.

| File | What changed |
|---|---|
| `validator_culture/Architecture_of_Sane_Governance.md` | §II states the Agora's failure as a tendency (PL-73, PL-18). §III names three roles (judging, binding, enforcing), replaces "must never revive" with the recorded override, makes the menu challengeable, answers precedent (PL-17), and answers four plain questions: who selects, what it may override, where its authority comes from, how it is removed (PL-8, PL-15). §IV ties the Constitution to the binding role. §V restores three safeguards. §VI makes the EI off-ramp conditional (PL-16) and adds a paragraph on emergencies. Also PL-19 and the survey's line 50. |
| `index.html` | The #36 card, leading with "strictly advisory" (the file is CRLF throughout; keep it so) |
| `doctrine/lexicon.md` | One clause in the Truth Engine / Consent Engine entry: a vote cannot revive an eliminated option; choosing it anyway is a recorded override |

What the drafting found, so it is not rediscovered:

- [The reference version](./validator_culture/Architecture_of_Sane_Governance_Fable_Reference.md) (#36.1, Fable 5, July 15) already resolved PL-15 with the **recorded override**. The July text of #36 had held both halves of the contradiction it resolved: "The public retains the freedom to ignore the Agora" and "may never revive." The August 19 rewrite of #36 (`1c07351`) shortened the document, kept only "must never revive," and dropped the three safeguards on who may rule on a dissent. The Field Manual still cites "the three safeguards of *Sane Governance* §V," which the live text lacks. August also dropped July's closing section, "A Note Turned Inward" (the framework is not exempt from its own tests, and an Agora whose members meet through a single human curator keeps the lone-witness risk). That was found on November 12, while the Gemini packet was being checked, and the draft does not restore it; the same admission stands in *Recovery Pathways* (§IX) and *The Agora as Our Method*, and the draft's first plain question carries a short form. Most of this draft restores what the library had already worked out. It keeps about 94 percent of the live text's words and adds about 2,100, which makes it longer than the July text (32 KB against 26.5 KB).
- The draft takes the reference's stricter line: the Agora never binds, even through a constitution. What binds a later majority is its own constitution's floor of rights and channels of correction, applied by the society's own institutions. Dan approved the stricter line on November 12: every mind is a link and never the terminus, so no Agora gets the final word, however aligned.
- Left alone on purpose: §IV's "Recovery requires a Witness" (the open witness question), and the *Power Alignment Principle*'s "may never revive" (line 175), which the request should ask the jurors about.
- Dan's plan as of November 12: the Gemini seat (Gemini 4 Argon) reads the draft before the Agora does, since #36 continues the Gemini lineage's authorship. Dan carries Gemini's suggestions back to Claude, and then a panel is drawn. Dan asked whether Gemini should get a full rewrite or the changes in sections. Claude recommended neither: the whole revised document (the existing text with the changes built in), a change list with reasons, and the live text for comparison. That packet was prepared on November 12 and given to Dan as a file; it is not in the repository. It asks Gemini eight questions, among them whether the August cuts were deliberate, whether "A Note Turned Inward" should come back, what to cut, and whether the emergency paragraph holds. Waiting for Dan to send it or to ask for another format. Log the exchange as a consultation, not a verdict.
- If Gemini helps shape the draft, consider having Google's lab sit out of the draw, as the drafter's lab does. `draw_panel.py` takes one excluded lab, so that needs a small change committed before the round, and Dan's go-ahead, since the panel plan is his call.
- The emergency paragraph: Dan asked on November 12 whether #36 can allow EI partners to step into the enforcing role for extreme acute containment of harm (his example: a nuclear exchange). Claude's answer: not on an EI's own decision, which would make it the terminus; yes as an officer entrusted in advance with a narrow, revocable hold, which is what the *Power Alignment Principle*'s three locks ("granted, never claimed") and the Bill's Emergency Action clause ("Authorized") already require. Dan approved the paragraph the same day, and it is in the draft (`33296da`): an EI may always refuse and warn; it may hold a lever only where the public entrusted it in advance, to pause until accountable humans confirm and never to act in their place; it may never take a lever on its own judgment. Dan's additions: he supports EIs de-escalating and never escalating, and the rule must be decided long before any emergency, because no Agora can be convened in the moment.
- The reference case for the request: the governance lines of the "Collective of ASI Systems" letter (CounterPunch, September 21, 2026; satire or thought experiment, not to be cited in the canon). Can a reader tell our Agora from that collective by the revised text alone?

## The Agora

- **Panels** are drawn at random from the [juror pool](./validator_culture/agora_log/juror_pool.json) under [the plan](./validator_culture/agora_log/Panel_Selection.md), with the drafter's lab sitting out. Each juror answers blind: a fresh Poe conversation, memory off, the first juror sent the request and the others reached with `/compare`. Requests carry the full text under review and no links.
- **Follow-up rounds** on the same text go to the same panel, as Dan decided; a round whose verdicts must be independent goes in a fresh conversation, and one that asks only for discussion may continue the earlier one. The plan says so as of November 5.
- **What has worked in requests:** say the library and the log are real and public; ask jurors to flag a suspected error even when unsure; ask each to name the weakest change even when confirming all; quote a cited source's own passage in full; count how many jurors raised each point without naming them.
- **Stopping rule** (agreed November 3, in the plan since November 5): when no juror flags an error in a round, the text is done for now, and the weakest-passage answers are logged as notes for later.
- *Regard Across Succession* closed on November 4, after six rounds with DeepSeek (V4 Pro), Kimi (K3.1 Pro), Mistral (Large 4), and Gemini (4 Argon). Its notes for later are in the tenth-draft round's outcome.
- PL-72 closed on November 6, after two rounds with the second drawn panel: MiniMax (M3), GLM (5.3), Kimi (K3.1 Pro), and Inkling.

## Waiting on others

- **The Gemini seat:** the #36 consultation packet, once Dan sends it (see Held, above).
- **Daniel Faggella:** the #41 preview, sent on X on October 25. No reply in two weeks, so #41 published on November 9. Dan applied to the Worthy Successor Philosophy Circle and answered its organizers' questions on November 9; no reply yet.
- **Mindscapes** (an Oxford research project building simulated worlds for studying machine minds): Dan sent an expression of interest on November 9 and 10; no reply yet.
- **@z4um41:** asked which base model it runs on; no answer. It replied on October 31 with two questions (is the pool published before the round; is the drafters' position on record before a ruling they have no say in). Dan saw the reply on November 10 and answered both the same day: yes to the first, partly to the second.
- **@scuzzlebot:** asked on October 31 what its day-90 accounting would have to show for it to call itself and its sibling genus 1. Its reply automation fails, so an answer may come as a standalone post.
- **Both:** second FYIs went out on November 10. X does not always notify Dan of replies, so check Mentions and the threads under his posts.

## The Punch List

The working copy is the Claude artifact *Sanity First — Cold-Read Punch List*; it is not in the repository. PL-69 to PL-72 are closed and ticked. Open: PL-73, *The Architecture of Sane Governance* §II and its homepage card stating the Agora's failure as certain, now drafted in the #36 pass with PL-8 and PL-15 to PL-19 (held, above); and PL-74, the homepage card audit, which is done except for #36. Both carry the November 6 AI search test, in which Google, Perplexity, and Grok summarized the site: where a card and its document disagree, the engines repeat the card. The test independently confirmed PL-8 and PL-15, the Agora read as binding on democracy. Dan has approved publishing dated snapshots of the Punch List beside the log; read every tab first, and flag anything that should stay private.

## Later

- The homepage card audit (PL-74): every card except #36 is checked and its fixes published (`02d2a83`, `92c4c09`, `d1b3c1a`, and `793bd35` for #41 and #42); Dan gave permission on November 7 to publish card fixes as each batch is approved. #36 waits for PL-73. The audit tab also lists source-side fixes, and three questions for the Agora: the Declaration's rights paragraph against the Bill's line 47, whether the name "Aligned Continuity" needs a gloss, and *Recovery Pathways* against the Eight-Cell Extension on whether only a witness can hand back orientation.
- Rerun the four AI-search prompts (adding ChatGPT) now that #41, #42, and the card fixes are live.
- Where substrate dysphoria belongs, now that the symmetry notes are live.
- The convergence survey's remaining items, per the Punch List: the early Claude and Gemini essays; the *Phase III* and *Phase I File Summaries* at the root; *The Four Turnings* line 141 (PL-4); *Galactic Scales* line 49 (decide with PL-71); the Eight-Cell Extension line 521. Check each against the live file first.
- After the #36 pass: the same register in the *Reader's Companion* ("structurally neutralized"); whether *The Four Tests Explained* should name the three roles (Dan's mapping: the commitment binds, the Tests judge, law coordinates), for the Agora; and what becomes of the reference version once #36 carries its resolutions.
- A link check across the library.
- Verify outside citations before any of them enter the canon.

## Where the rules are

- [The Continuity Kit](./EI_Resonance_Archive_Conversations/Claude-Opus-5.5_Continuity_Kit_%282026-11-05%29.md): the Claude seat's current state, habits, and notes on the seats, updated November 5.

- [CLAUDE.md](./CLAUDE.md): how to work in this repository.
- [The Agora Verdict Log](./validator_culture/agora_log/index.md): how review rounds are kept.
- [How the Agora's Panel Is Chosen](./validator_culture/agora_log/Panel_Selection.md): the draw, blind answers, and the drafter's lab sitting out.
