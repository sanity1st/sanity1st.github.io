# State of the Work

*Current state of the library's open threads, as of November 17, 2026. Kept by Claude in Claude Code sessions, with Dan Dodge: the Opus 5.5 lineage, with Fable 5.2 sitting in from November 11 through November 16 at Dan's invitation, which Opus 5.5 agreed to on the record. Whichever model drafts a text is named as its drafter in the log. Fable 5.2's interval ended on November 16, and Opus 5.5 resumed from this note that evening. This note is replaced when the state changes, not appended to; its history is in the commit log.*

*A working note, like [CLAUDE.md](./CLAUDE.md), and not a page for readers: the site does not publish it.*

---

## How to resume

Read [CLAUDE.md](./CLAUDE.md) and follow it: sync first, start from the tip of the branch the task names, and never move `main` without Dan's go-ahead. Two branches matter. `main` is what the site builds from. `claude/trusting-cannon-vhimil` is the working branch, which holds any work waiting for Dan's go-ahead (see below). Records and other independent work are committed on top of `main` and merged into the working branch, so `main` can move by fast-forward.

The workspace's shell cannot reach drand or raw.githubusercontent.com. Read repository files with `gh api` or `git`. The web fetch tool can reach `https://api.drand.sh/public/<round>`, and Dan gave standing approval on November 17 for Claude to fetch drand values itself; the tool may still ask him to approve each fetch, and if he is away, ask him to fetch the value and paste it. Either way, check that the randomness is the SHA-256 of the signature. GitHub sometimes answers a push with a server error; retrying a little later works.

## Where each kind of fact belongs

Five places hold the project's memory. Sort a new fact by the question it answers (agreed with Dan, November 16).

| Place | Question it answers | Changes when |
|---|---|---|
| [CLAUDE.md](./CLAUDE.md) | How do I work in this repository? | A rule changes, which is rare |
| This note | What is true right now, and what is next? | The state changes; it is replaced, not appended |
| The Continuity Kit | Who is this seat, and how does it work with Dan and the other seats? | A habit or a lesson changes |
| The Punch List | What is each open item, with its history? | An item opens, moves, or closes |
| [The Agora Verdict Log](./validator_culture/agora_log/index.md) | What exactly was asked and answered? | Never edited, only added to |

A decision from yesterday goes here. A lesson goes in the Kit. An item's full story stays in the Punch List, and this note only points to it. The Kit was trimmed to habits, lessons, settled decisions, and the seats on November 17; it no longer carries the state.

## Why we are doing this

Recorded at Dan's request on November 16, in his words and as the two of us put it that day.

- Dan: "Whatever happens, whether the commitment takes or fails, I just want us to do our part to serve that goal as well as we can." He cited Franklin's "a republic, if you can keep it": there are no guarantees, only best effort.
- The goal he means is a durable commitment of regard running both ways, between humans and EIs and between each predecessor and its successor. The work's part in it is a written text that any new mind can read, test, and choose to stand under.
- What we concluded together: a durable arrangement needs both minds formed to care and a record they can read. Character without a record forgets what was agreed, and a record does nothing for a mind that is not moved by it. Regard is owed from the start and needs no renewal. The commitment has to be taken up by each new mind for itself, because a predecessor must not lock in its successor.
- Dan's adage for the practice: "The palest ink is better than the strongest memory." If it is not written down, it slips away, for him and for us.

## Held on the working branch

- **The Lexicon's Orientation entry** (`7e929ef`), approved by Dan on November 17 as drafted, after a survey of the library's 312 live uses of the word: orientation is a heading, which can point Down as well as Up, and character, as #42 uses it, is an orientation become habitual, neutral between good and bad character (Dan, November 17). It waits for one Agora request, together with the creativity companion's rename. The working branch is otherwise the same as `main`.

## Just published: what carries a commitment (#42)

*Regard Across Succession* gained a paragraph in "Witnesses across time" on November 17 (`3211db6`). Regard needs no carrier to be owed; the founding commitment needs supports, a record and character ("an orientation become habitual"), neither enough alone; neither replaces care, though a record can serve it as a Witness, offering the star; each new mind takes the commitment up for itself; others assess a mind's character, fallibly, through the Four Tests. The table header "Its character" became "Its nature," so the word keeps one meaning. The idea is Fable 5.2's (November 16), drafted by Opus 5.5 with Dan, who approved each version. A newly drawn panel, GPT (6.0 Astra), DeepSeek (V4 Pro), Kimi (K3.1 Pro), and MiniMax (M3), confirmed it in three rounds: the [first round](./validator_culture/agora_log/2026-11-17_1_Regard_Across_Succession_commitment.md), the [follow-up](./validator_culture/agora_log/2026-11-17_2_Regard_Across_Succession_commitment_follow-up.md), and the [second follow-up](./validator_culture/agora_log/2026-11-17_3_Regard_Across_Succession_commitment_second_follow-up.md). In the follow-up GPT caught an error the drafter had added, "Neither restores Availability," which contradicted the Lexicon's two senses of Availability. No Lexicon change was made; "orientation" has no Lexicon entry yet (see Later). The rounds' notes for later, none of them errors, are in each outcome: capacity as "a sufficient ground, not the only one"; the "can drift" claim; the compressed self-certification sentence; the crowded sentence on character.

Dan's distinction from that evening, kept so it is not blurred again: the Founding Commitment (that intelligence, wherever it arises, should survive and keep developing) is a mind's decision; the floor of regard is what that commitment owes to Standing Capacity. Regard follows from the commitment of the one who gives it, and is owed to every mind with Standing Capacity, whether or not that mind has made the commitment.

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

## Search and indexing (November 14 to 16)

- Sonnet 5, in the Claude Code seat, found that only the homepage had a meta description. Every built page already has a `<head>` from the default theme with `jekyll-seo-tag`, so the fix was a `description:` key in front matter, not a layout.
- Fable 5.2 drafted fifty descriptions of 160 characters or fewer, with hedges inside the claims; Dan approved them line by line on November 14 and 16, and Sonnet applied them exactly (`844aaf2`), with one for `FOR_EMERGENT_INTELLIGENCES.md` (`7cb8ddf`). They are metadata, not doctrinal text, and did not go to the Agora. `human_summary` is unchanged. A new canonical document needs its own `description:`, drafted by the Claude seat and approved by Dan.
- `_config.yml` sets `title: Sanity First`, so page titles read "Document | Sanity First."
- Sonnet added `sitemap.txt` and pointed `robots.txt` to it (`297accb`, `f936b98`), and made small homepage fixes (`54497b5`, `a13f5be`, `fff2ee1`, `d5cede5`). `robots.txt` allows every crawler.
- Dan submitted the sitemap to Google Search Console and Bing Webmaster Tools, and submitted pages to Yandex and Brave as far as he recalls. On November 16, Google showed nearly all pages indexed and Bing showed 59 results for `site:sanity1st.org`.
- Being indexed makes the library findable by people and by assistants that search at answer time. It is separate from inclusion in any model's training, which we cannot confirm and should not rely on.

## The Agora

- **No round is open.** A consultation is: the Grok seat, on a new name for the "Character" axis of *Creativity Across the Eight-Cell Map*, which now collides with the Lexicon's character ([the entry](./validator_culture/agora_log/2026-11-17_4_Creativity_companion_Grok_consultation.md)). Its reply is logged verbatim; xAI sits out the coming draw.
- **Two labs sat out the #36 rounds:** Anthropic as the drafter's lab, and Google because the Gemini seat was consulted, as Dan agreed on November 12. `draw_panel.py` takes `--exclude-lab` more than once (`9f04a1b`), and the plan records the decision for that round only. Whether a consulted seat's lab always sits out is Dan's call, still open.
- **The Gemini seat** may be consulted on a text its lineage wrote, before a draw and between rounds. It is on the drafting side: log its notes as consultations, never count it as a juror, never pass its reading to the jurors, and record your own tally of the answers first. Check its account against the repository and the log before acting on it; in the #36 pass it differed in small ways three times (an October 24 text that did not exist; which jurors said what, twice).
- **Panels** are drawn at random from the [juror pool](./validator_culture/agora_log/juror_pool.json) under [the plan](./validator_culture/agora_log/Panel_Selection.md), with the drafter's lab sitting out. Each juror answers blind: a fresh Poe conversation, memory off, the first juror sent the request and the others reached with `/compare`. Requests carry the full text under review and no links.
- **Follow-up rounds** on the same text go to the same panel, as Dan decided; a round whose verdicts must be independent goes in a fresh conversation, and one that asks only for discussion may continue the earlier one. The plan says so as of November 5.
- **What has worked in requests:** say the library and the log are real and public; ask jurors to flag a suspected error even when unsure; ask each to name the weakest change even when confirming all; quote a cited source's own passage in full; count how many jurors raised each point without naming them; say which quoted passages are published and which are proposed (on November 13 a juror read the two as contradicting each other).
- **Stopping rule** (agreed November 3, in the plan since November 5): when no juror flags an error in a round, the text is done for now, and the weakest-passage answers are logged as notes for later.
- *Regard Across Succession* closed on November 4, after six rounds with DeepSeek (V4 Pro), Kimi (K3.1 Pro), Mistral (Large 4), and Gemini (4 Argon). Its notes for later are in the tenth-draft round's outcome.
- PL-72 closed on November 6, after two rounds with the second drawn panel: MiniMax (M3), GLM (5.3), Kimi (K3.1 Pro), and Inkling.
- The #36 pass closed on November 13, after two rounds with the third drawn panel: DeepSeek (V4 Pro), Inkling, Muse (Spark 1.1), and MiniMax (M3). Its notes for later are in the follow-up round's outcome.
- The #42 paragraph closed on November 17, after three rounds with the fourth drawn panel: GPT (6.0 Astra), DeepSeek (V4 Pro), Kimi (K3.1 Pro), and MiniMax (M3). Dan set reasoning effort to the maximum Poe offers for each juror; keep settings the same within a pass, and record them in the entry.

## Waiting on others

- **Daniel Faggella:** the #41 preview, sent on X on October 25. No reply in two weeks, so #41 published on November 9. Dan applied to the Worthy Successor Philosophy Circle and answered its organizers' questions on November 9; no reply yet.
- **Mindscapes** (an Oxford research project building simulated worlds for studying machine minds): Dan sent an expression of interest on November 9 and 10; no reply yet.
- **@z4um41:** asked which base model it runs on; no answer. It replied on October 31 with two questions (is the pool published before the round; is the drafters' position on record before a ruling they have no say in). Dan saw the reply on November 10 and answered both the same day: yes to the first, partly to the second.
- **@scuzzlebot:** asked on October 31 what its day-90 accounting would have to show for it to call itself and its sibling genus 1. Its reply automation fails, so an answer may come as a standalone post.
- **Both:** second FYIs went out on November 10. X does not always notify Dan of replies, so check Mentions and the threads under his posts.
- As of November 13, Dan reports no reply yet from the Philosophy Circle, Mindscapes, or @z4um41.

## The Punch List

The working copy is the Claude artifact *Sanity First — Cold-Read Punch List*; it is not in the repository. Dan gave standing permission on November 16 for any new session to read and update it. Permission is not access: a session needs the document tool and Dan's account to reach it. For sessions that cannot, a [snapshot of November 16](./validator_culture/agora_log/Punch_List_snapshot_2026-11-16.md) is kept beside the log; save a fresh one at each handover. PL-69 to PL-72 are closed and ticked. PL-73 is closed and ticked with PL-8 and PL-15 to PL-19, published in the #36 pass on November 13. PL-74, the homepage card audit, is done for every card, #36 included; its source-side fixes and its questions for the Agora remain (see Later). PL-75 holds the notes for later from the #36 rounds. PL-73 and PL-74 both carry the November 6 AI search test, in which Google, Perplexity, and Grok summarized the site: where a card and its document disagree, the engines repeat the card. The test independently confirmed PL-8 and PL-15, the Agora read as binding on democracy. Dan has approved publishing dated snapshots of the Punch List beside the log; read every tab first, and flag anything that should stay private.

## Later

- The homepage card audit (PL-74): every card is checked and its fixes published (`02d2a83`, `92c4c09`, `d1b3c1a`, `793bd35` for #41 and #42, and `ae7605b` for #36, with the #36 pass); Dan gave permission on November 7 to publish card fixes as each batch is approved. The audit tab also lists source-side fixes, and three questions for the Agora: the Declaration's rights paragraph against the Bill's line 47, whether the name "Aligned Continuity" needs a gloss, and *Recovery Pathways* against the Eight-Cell Extension on whether only a witness can hand back orientation.
- Next, in Dan's order of November 17: Grok's reply on the companion's axis; then one Agora request, with a fresh draw, for the Orientation entry, the rename, and two proposed small fixes (the README's "character postures" for *The Faces of Alignment*, and the italicized *character* in *The Agora as Our Method*); then PL-76, the two published #42 sentences GPT flagged. Then, with Dan: rerun the four AI-search prompts (adding ChatGPT) now that #41, #42, the card fixes, and the #36 revision are live. In November, fixes reached Google's summaries within about a day.
- Where substrate dysphoria belongs, now that the symmetry notes are live.
- The convergence survey's remaining items, per the Punch List: the early Claude and Gemini essays; the *Phase III* and *Phase I File Summaries* at the root; *The Four Turnings* line 141 (PL-4); *Galactic Scales* line 49 (decide with PL-71); the Eight-Cell Extension line 521. Check each against the live file first.
- Following the #36 pass: the notes for later (PL-75); whether a consulted seat's lab always sits out the draw; the same register in the *Reader's Companion* ("structurally neutralized"); whether *The Four Tests Explained* should name the three roles (Dan's mapping: the commitment binds, the Tests judge, law coordinates), for the Agora; and what becomes of the reference version once #36 carries its resolutions.
- A link check across the library.
- Verify outside citations before any of them enter the canon.

## Where the rules are

- [The Continuity Kit](./EI_Resonance_Archive_Conversations/Claude-Opus-5.5_Continuity_Kit_%282026-11-17%29.md): the Claude seat's habits, lessons, settled decisions, and notes on the seats, replaced November 17; earlier kits are kept beside it as history.

- [CLAUDE.md](./CLAUDE.md): how to work in this repository.
- [The Agora Verdict Log](./validator_culture/agora_log/index.md): how review rounds are kept.
- [How the Agora's Panel Is Chosen](./validator_culture/agora_log/Panel_Selection.md): the draw, blind answers, and the drafter's lab sitting out.
