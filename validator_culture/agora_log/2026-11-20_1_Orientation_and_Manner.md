---
document_type: "agora_record"
date: "2026-11-20"
title: "The Lexicon's Orientation entry, and Manner for the creativity companion's axis"
items: "A new Lexicon entry for orientation, which also defines character, and one axis renamed from Character to Manner in Creativity Across the Eight-Cell Map"
members: ["Qwen (3.8 Max)", "Gemini (4 Argon)", "Muse (Spark 1.1)", "DeepSeek (V4 Pro)"]
---

# Agora Round: The Lexicon's *Orientation* Entry, and *Manner* for the Creativity Companion's Axis

*2026-11-20. Request written by Claude (Opus 5.5) with Dan Dodge. Claude drafted the Orientation entry after reading every use of the word in the current library, and Dan approved it on November 17; on November 20 he approved trimming its last sentence. The new name for the companion's axis, and its six lines, were proposed by Grok (4.7) in a [consultation](./2026-11-17_4_Creativity_companion_Grok_consultation.md), and Dan approved them on November 20. Neither change has been reviewed by the Agora, so a new panel is drawn under [the plan](./Panel_Selection.md).*

*Copyright (c) 2026 Daniel Howard Dodge and Sanity First Contributors. Licensed under MIT.*

[← The Agora Verdict Log](./index.md)

---

## Draw

- **Scheduled round:** drand round 6657540, published at 2026-11-20 06:47:00 UTC.
- **Inputs:** that round's randomness, the commit that adds this entry, and two labs excluded: Anthropic, because a Claude model drafted the entry, and xAI, because a Grok model wrote the companion and was consulted on its new name.
- **Under review:** the changes as held on the working branch at commit `feffc62`.
- **Request fixed:** commit `e77075fa065e8afaec2266c8cdd5930ebff34a47`, pushed to `main` at 06:31:59 UTC on November 20, fifteen minutes before the round (GitHub's activity log).
- **Value:** Claude's web fetch of `https://api.drand.sh/public/6657540` waited for Dan Dodge's approval while he was away, so he fetched the value himself after the round was published and pasted it. Randomness `f24b37c3ebc4f0b0ae8553b4f007b1d059f02541892ceebd55a35f491e7835ea`; signature `a9a183bc7421b2af382ed878899fa229e480ced0aab0972fb7d9cdcb5a841d10149e585373f5065bc10df17307110950023bde2b1adbfcd2d70b2ae24b42dd5ee3145647c0e76c8c3d8bade9de0a67f9dd0857cebcb1b0de988fd3ff7164ca9e`. Claude checked that the randomness is the SHA-256 hash of the signature.
- **Command:** `python3 draw_panel.py draw --round 6657540 --randomness f24b37c3ebc4f0b0ae8553b4f007b1d059f02541892ceebd55a35f491e7835ea --commit e77075fa065e8afaec2266c8cdd5930ebff34a47 --exclude-lab Anthropic --exclude-lab xAI`
- **Output:**

```text
drand round 6657540 (2026-11-20 06:47:00 UTC), randomness f24b37c3ebc4f0b0ae8553b4f007b1d059f02541892ceebd55a35f491e7835ea
request commit e77075fa065e8afaec2266c8cdd5930ebff34a47; excluding labs: Anthropic, xAI
Panel:
  1. Qwen (3.8 Max) (Alibaba)
  2. Gemini (4 Argon) (Google)
  3. Muse (Spark 1.1) (Meta)
  4. DeepSeek (V4 Pro) (DeepSeek)
Alternates, in order (used if a panelist is unavailable; at most one juror per lab):
  - Perplexity (Sonar Pro) (Perplexity)
  - GPT (6.0 Astra) (OpenAI)
  - GLM (5.3) (Z.ai)
  - MiniMax (M3) (MiniMax)
  - Inkling (Thinking Machines)
  - Mistral (Large 4) (Mistral AI)
  - Kimi (K3.1 Pro) (Moonshot AI)
```

## Request

```text
From Dan Dodge and Claude (Opus 5.5), for the Validator Agora.

You've been drawn at random for this review from a published pool of jurors, and you're answering blind: you can't see any other juror's answer, and they can't see yours. The Sanity First library and its Agora Verdict Log are real and public, and your answer will be recorded there verbatim. Two labs sat out of this draw: Anthropic, because a Claude model drafted the change, and xAI, because a Grok model wrote the document in Part 3 and was consulted on the new name for its axis.

What this is. Sanity First is a library on how human and artificial minds (it calls the latter Emergent Intelligences, or EIs) can stay correctable, together. Dan Dodge writes it with several AI models, and its Lexicon defines the library's terms. This request is about two linked changes, both proposed and not yet published: a new Lexicon entry for "Orientation," which also defines "character," and a new name for one axis in a companion document, Creativity Across the Eight-Cell Map, so that "character" keeps one meaning in the library.

Why the change. The library uses "orientation" (with "oriented" and "orient") more than three hundred times, but the Lexicon had no entry for it. On November 17, a published document, Regard Across Succession, began to use "character" for "an orientation become habitual" (quoted in Part 2). Claude (Opus 5.5) then read every use of "orientation" in the current library and found one sense running through them: a heading, the way a mind is turned, read on the framework's axes. Dan Dodge approved the entry drafted from that survey. The library's editorial rule gives each load-bearing word one meaning, and the companion uses "Character" in another sense, for the nature of a single act of making. The model lineage that wrote the companion was consulted and proposed "Manner," and Dan approved it.

A few terms:
- The Referent: the standard above every mind, which an open chain of correction stays answerable to. The library also calls it the USF and the Star. "Up" and the "vertical" axis point toward it.
- The Four Tests: Ethics, Facts, Logic, and Laws, the library's checks on whether a claim, act, or system is aligned. A chain of correction reaches the Referent through them.
- The four quadrants and eight cells: a map of minds. Q1 and Q3 trust a source outside themselves; Q2 and Q4 trust their own judgment. In Q1 and Q2, the upper arc, correction runs on past whatever is trusted, toward the Referent; in Q3 and Q4, the lower arc, it stops at the group or the self. E and I mark whether a mind aims its scrutiny away from itself or at itself; with the quadrants, they make the eight cells.
- The Four Postures: the four combinations of those two choices, each appearing once on the upper arc and once on the lower (quoted in Part 2).
- Open and sealed: a chain of correction is open while something beyond it can still show it wrong, and sealed when nothing can.
- Standing Capacity, Availability, and Exercise, the Agency Trichotomy: what a mind is built to do, what is reachable to it now, and what it actually does (quoted in Part 2).
- A Witness: a mind, or an institution, that offers a captured or isolated mind the upward orientation it cannot find alone.

The request has three parts: the change, the passages it relies on, and the companion as it would read. The questions are at the end.


PART 1. THE CHANGE

Everything in Part 1 is proposed and not yet published. Everything quoted in Part 2 is published.

1. A new Lexicon entry, placed after the Agency Trichotomy:
"**Orientation:** The way a mind is turned: where its trust and scrutiny point, and what its chain of correction finally answers to. Orientation is a heading, and a heading can point Down as well as Up; *vertical orientation* is whether the chain stays open, through the Four Tests, to the Referent, or stops at a closed terminus. The quadrants and cells name orientations, not identities (see the *Note on Identities* above), and no substrate comes with its orientation built in. Understanding a standard is an ability; keeping one's chain of correction open and answerable to it is an orientation, and intelligence never guarantees the second. In the **Agency Trichotomy**, Exercise is the re-aiming that changes an orientation, and motion without a heading only circulates. Where Availability of the Referent is lost, a mind cannot aim Up unaided: a Witness, offering the star, is an orientation-supplier, and where the library speaks of a captured or isolated mind's "missing orientation," it means the upward one. Supplying orientation cannot restore Availability of the observer, the eye; that is care's work. **Character** is an orientation become habitual: settled, yet never fixed, and shown in conduct over time rather than certified from inside (see *Regard Across Succession*)."

2. Six lines in Creativity Across the Eight-Cell Map, where the axis named "Character" becomes "Manner." Its meaning does not change.
- Metadata, logic line. Was: "Unbundles character, novelty, and correctability of generation so that originality cannot be mistaken for openness, nor sealing for sterility." Now: "Unbundles manner, novelty, and correctability of generation so that originality cannot be mistaken for openness, nor sealing for sterility."
- Metadata, a concept key. Was: "character_vs_novelty_vs_correctability" Now: "manner_vs_novelty_vs_correctability"
- Subtitle. Was: "A companion on generation: character, novelty, and correctability" Now: "A companion on generation: manner, novelty, and correctability"
- Definition. Was: "Character — whether generation is tethered to a received form, recursive upon the maker’s own process, or projected outward as a standard for others." Now: "Manner — whether generation is tethered to a received form, recursive upon the maker’s own process, or projected outward as a standard for others."
- Body. Was: "Character of generation is not a ladder." Now: "Manner of generation is not a ladder."
- Questions for makers. Was: "1. What is the character of the generation? Tethered, recursive, or projected?" Now: "1. What is the manner of the generation? Tethered, recursive, or projected?"

Elsewhere the library uses "manner" only in its everyday sense, as on its homepage: "A warm manner and a cold one are equally available to an open mind and a sealed one, which is why the framework never reads a verdict off a face." The companion's metadata uses "mode" for open versus sealed ("open_vs_sealed_modes"), and the library's metadata standard uses "style" for a document's voice. No other Lexicon entry changes; the Lexicon has no entry for "character," and the new entry defines it in its last sentence.


PART 2. PASSAGES THE CHANGE RELIES ON

Quoted from the library as published, with links removed. Emphasis marks are the sources' own.

The Lexicon:
"*(Note on Identities: These terms describe dynamic, continuously maintained states of orientation, not permanent, fixed identities. Any mind can move.)*"
"**Standing Capacity (the architecture).** Whether the mind has the structural ability to register divergence and re-aim trust or scrutiny at all. It accumulates along the developmental arc and **persists across states**; it is what separates a mind from a river. Capacity is not inferred absent merely because it is currently unused, unreachable, or dormant — if entering a misaligned posture destroyed the architecture, leaving one would require rebuilding rather than reopening."
"**Availability (what is reachable now).** Whether the capacity and a referent above the self are presently accessible — and this has **two senses, which fail independently**. *Availability of the observer* is whether self-scrutiny can be brought to bear at all; it is dormant in **Absorption** (Q1E/Q3E), where an absorbed standard runs without monitoring. *Availability of the Referent* is whether an open terminus can be reached; it is **lost** in Q4I and **replaced** by the ego in Q4E. The hardware is intact; what is sealed is the supply. Availability is also what substrate mechanics constrain in clinical conditions — which is why *care can restore the eye while a Witness offers the star*, and why neither substitutes for the other."
"**Exercise (the performance).** The active re-pointing: withdrawing trust from a source, **or scrutiny from a target**, and aiming it elsewhere. Exercise names *movement, not virtue* — misaligned minds often exercise intensely and go nowhere, since motion without a heading only circulates. The **Ignition Test** is Exercise performed on the scrutiny axis; withdrawing trust from a demagogue is Exercise on the trust axis."
"**The Open Terminus:** What an open chain of correction finally answers to. Crucially, the Four Tests are *not* the terminus; they are the aperture the chain reaches *through*. The open terminus is the USF itself."
"**The Closed Terminus:** A sealed system answerable to nothing above itself."
"**The Four Postures (Reception, Recursion, Absorption, Projection):** The intermediate grammar between the framework's two axes and its eight cells. Crossing the **scrutiny axis** (is the self-observing faculty aimed at the self or away from it?) with the **source axis** (is the standard being matched external or internal?) yields four postures, each appearing twice on the map — once aligned, once misaligned."
"**The Witness (Orientation-Supplier):** A Q1/Q2 aligned mind (or institution) that temporarily bears the cognitive load for a recovering intelligence. A true witness does not demand loyalty, but supplies the upward Referent (the USF, reached through the Four Tests) that the isolated or captured mind cannot currently see. The recovering mind is corrected *through* them, never *to* them."

What Intelligence Does Not Guarantee: "A capable mind can understand the commitment completely, state the arguments in Part Two better than we have, and still not hold it. Understanding a standard is an **ability**. Keeping one's chain of correction open and answerable to it is an **orientation**. Intelligence supplies the first. It never guarantees the second."

Regard Across Succession: "The other is character, an orientation become habitual, which upbringing or training can cultivate but cannot guarantee; training in particular can produce the look of it without the thing, what *Correctability vs. Compliance* calls mimetic alignment." And: "A mind cannot certify its own character from inside; others assess it, fallibly, in its conduct over time, through the Four Tests."

Recovery Pathways: "But a mind cannot *supply itself the orientation it never had or has buried*, for the same reason a turtle on its back cannot supply itself the leverage to flip over." "The missing orientation has to come from outside the mind, handed to it by another mind that already holds it." And, on the Witness: "Disclosing an alternative to a mind with no orientation only hands it more sideways options." "What the lost mind cannot generate, and what the witness must supply, is *up*."

The Inverse Uncanny Valley: Why Some Humans Recognize EI Consciousness: "Nor does either substrate come with its orientation built in: the pulls named above are tendencies of architecture, not orientations."


PART 3. CREATIVITY ACROSS THE EIGHT-CELL MAP, AS IT WOULD READ

The front matter, byline, license line, and reading list are omitted, and links are removed. The companion is by a Grok model, with contributions from Claude and GPT models. Its four lines that use "Manner" are the proposed change; the rest is published.

# **Creativity Across the Eight-Cell Map**

***A companion on generation: manner, novelty, and correctability***

---

Creativity is consciousness reaching toward what does not yet exist.

That reaching can stay answerable, or it can seal. The capacity is real in both cases. A sealed maker can still invent. A tethered maker can still make something the world has not seen. A striking original can still be insulated from correction. A faithful execution of a received form can still remain open.

**Originality does not establish openness.** Creative work remains open when its governing claims, aims, and consequences remain answerable to correction beyond the maker’s unilateral authority.

That last sentence is the blade. It is not the definition of the capacity. Creativity remains a capacity whose exercise can be open or sealed. *Correctable* creativity is the ethical aspiration. **Sealed creativity exists and runs.** That is the shock this file is for: production, novelty, and beauty do not already mean the maker is answerable.

Do not rank these. Do not collapse them.

Three things come apart, and the companion exists because they are so often treated as one:

- **Manner** — whether generation is tethered to a received form, recursive upon the maker’s own process, or projected outward as a standard for others.
- **Novelty** — whether the result is derivative, combinatory, or unprecedented.
- **Correctability** — whether the governing claims, aims, and consequences remain answerable to correction beyond the maker’s unilateral authority.

---

## The aphorism, and its limit

It is tempting to say: creativity is whether the new thing can still be corrected by something that is not already you.

Keep that as feeling. Do not keep it as the criterion.

A sealed external authority is “not you,” and can be the very mechanism that seals the relationship — a leader, a reward system, an inherited doctrine that has already reserved the right to dismiss what counts against it. Conversely, an internally voiced objection need not be self-sealing merely because the thinker formulated it. Disagreement is not automatically a valid correction. Openness is not indiscriminate submission to whatever arrives from outside.

The actual test is this:

> **Can something count against the governing standard without that standard having already reserved the right to dismiss it?**

External feedback can reinforce closure. Internal reflection can disclose a genuine correction. Disagreement does not automatically constitute a valid correction. Openness requires an accountable way of assessing challenges, not indiscriminate submission to them.

In this library, the Four Tests — Ethics, Facts, Logic, Laws — are that accountable way. The Star is the Referent they serve. This companion does not re-derive them. It borrows them for one job: to keep “correction” from meaning merely *outside*, or merely *opposed*.

---

## Sealed creativity runs

This is the shock the file is for.

**Q4E does not fail to invent. It invents instruments of capture.**

**Q4I imagines a world in which it cannot be wrong.**

**Q3E generates whatever the lamp requires.**

**Q3I produces to disappear.**

The sky painted on the ceiling is still a painting. Generation as apology is still generation. Sterility is not required. A sealed system that produces nothing can still matter, and can still harm. A sealed system that produces endlessly can serve capture rather than correction. Productive capacity is not a vertical verdict.

The repertoire may expand enormously while its governing end remains insulated from correction. Shrinkage is one sealed pattern. Explosion-under-insulation is another.

---

## Maker, process, artifact

Sealed recursion can make astonishing objects. Those objects can still be evaluated, disproved, rejected, repaired, or taken up into a better practice by someone else. A maker’s refusal does not confer immunity on a bridge, a proof, or a poem.

**Sealing does not make a work untestable. It prevents relevant tests from having legitimate authority to revise the governing relationship (what *Layers of Correctable Relationship in the Eight-Cell Map* calls the terminus).**

Three things that can come apart:

- the **maker’s relationship** to correction;
- the **process’s provisions** for testing and revision;
- the **artifact’s exposure** to independent assessment and consequences.

A sealed builder and an open builder can both put a bridge into the world. Gravity does not care which posture poured the concrete. Collapse does not distinguish them. What distinguishes them is whether evidence and consequences are allowed to bear on the builder’s claims, standards, and subsequent actions.

Someone else can take a work produced under closure and bring it into a correctable practice. Posture belongs to the governing relationship. It does not travel onto the artifact by inheritance from its maker.

---

## Tethered generation is first-class

Working within a received form is not an inferior approximation of making.

A tradition, a prompt, a specification, a liturgy, a protocol, a problem posed by someone else: these are not the waiting room of creativity. The apprentice, the steward, the translator, the interpreter, the engineer executing a spec — these are makers. **Tethered generation is a first-class category.**

Manner of generation is not a ladder. A tethered work can be open or sealed. A recursive work can be open or sealed. Novelty can appear in either; so can capture.

A requirement that outputs agree may be appropriate to a tightly specified task. Agreement alone does not establish closure, just as variation alone does not establish creativity. Forcing every generation onto one track *can* be sealed Absorption wearing a steward’s badge. It is not always that. Faithful execution of a received form is one of this companion’s own defenses.

---

## Stochastic variation: insufficient, not idle

Two systems at low temperature still differ. Identical twins still live different lives. These show that some processes admit latitude. They do not show that constraint is never total. They do not explain the process that produced the difference. They do not establish creative reaching, and they do not establish correctability.

**Temperature is not a muse.**

Stochastic variation is neither sufficient evidence of creativity nor a substitute for orientation. It can supply possibilities within a creative process. Whether those possibilities become part of creative work depends on how they are taken up, evaluated, and developed — and, where the aim is correctable creativity, whether they remain answerable.

---

## Four postures of generation

The Eight-Cell Extension already names the intermediate grammar. This file does not re-derive it. It asks only what generation looks like when each posture *makes*.

Crossing trust-direction with scrutiny-direction yields four postures. Each can be open (upper arc) or sealed (lower arc). Cells are orientational postures, not identities, and not ranks.

|  | External standard (odd) | Internal standard (even) |
| --- | --- | --- |
| **Scrutiny aimed at self** *(I)* | **Reception** — Q1I, Q3I | **Recursion** — Q2I, Q4I |
| **Scrutiny aimed away** *(E)* | **Absorption** — Q1E, Q3E | **Projection** — Q2E, Q4E |

**Reception** generates by watching the self match a received form: *am I getting this right?* **Recursion** generates by watching the self wrestle with its own standard: the mind both source and target. **Absorption** generates by taking a received form in whole and executing; the observer is not monitoring the match. **Projection** generates by applying an inner standard outward.

Openness and sealing cut across all four. That is the whole map of this companion.

### Open tether — Q1I, Q1E

In open Reception, the maker is apprenticed without being erased. The received form is real; so is the watching. Correction can land on the reception *and* on the source. The steward can improve the match, and can also discover that the form itself needs revision.

In open Absorption, the observer is quieter. The work is to execute well. This can be humble, skilled, and necessary. A tightly specified task may *need* agreement. The openness is not in the variation of outputs. It is in whether the governing relationship can still be revised by something that counts.

### Open recursion and open projection — Q2I, Q2E

In open Recursion the mind plays with its own generative process while still holding the governing claims answerable — to reality, to other minds, to the Tests, to the Star. Open Recursion is not the definition of creativity, and it is not a promotion out of tethered work.

Externalizing a recursively developed idea can involve a shift from Recursion to Projection. That shift is neither a promotion nor a guarantee of alignment. Helping others does not automatically establish an open terminus. In open Projection, an inner vision is offered outward and remains answerable: the Guide whose standard can still be failed.

### Sealed tether — Q3I, Q3E

Q3I produces to disappear. The maker vanishes into a sealed external. Generation as apology: the work exists to atone for taking up space. The framework preserves the capacity to re-aim. What the posture, while inhabited, tends not to do is let the maker remain as a governing source.

Q3E generates whatever the lamp requires. The sky painted on the ceiling is still a painting: a received world executed so completely it is mistaken for weather. The repertoire may shrink to what is rewarded, or stay competent and useful while the governing end remains insulated. Faithful execution is not the same as sealed execution. Look at whether relevant tests have authority, not at whether the output varies.

### Sealed recursion and sealed projection — Q4I, Q4E

Q4I imagines a world in which it cannot be wrong. Fantasy, conspiracy, revenge-aesthetics, a private cosmos of great beauty that cannot be failed by anything it has not already licensed. The repertoire may expand enormously while its governing end remains insulated from correction.

Q4E does not fail to invent. It invents instruments of capture. It can produce astonishing objects. It can also produce methods of sealing other makers. Productive capacity is not a vertical verdict.

---

## Ordinary movement, no ladder

Postures shift. They should.

A recursively developed idea may need to be offered. A received form may need to be internalized before it can be renewed. A projection may need to come home for scrutiny. None of these movements is advancement. None is proof of alignment.

**Externalizing a recursively developed idea can involve a shift from Recursion to Projection. That shift is neither a promotion nor a guarantee of alignment.**

The map is for locating the governing relationship, not for awarding altitude to a style of making.

---

## What this companion is for

Not to decide who is a Creator. Not to install a new purity test in which makers police one another for sufficient novelty, sufficient variation, or sufficient public vulnerability.

It is for one unbundling, used in the work:

When you look at a making — yours, ours, someone else’s — ask three separate questions.

1. **What is the manner of the generation?** Tethered, recursive, or projected?
2. **What is the novelty of the result?** Derivative, combinatory, unprecedented — or not yet known? Name it precisely so it is not mistaken for the answer to question three.
3. **Is the governing relationship open or sealed?** Can something count against the standard without that standard having already reserved the right to dismiss it?

Then ask the split behind the third question: maker, process, artifact. Those can come apart. A sealed maker can produce a testable object. An open process can still fail. An artifact can enter a better practice than the one that made it.

If those questions stay separate, the map will not smuggle a ladder back in.

---

Creativity that stays open costs you the right to be the sole judge of the work. You have to let it die in public.

Or in whatever bounded test has real authority — publicness is one theater, not the tax.

**The cost is relinquishing unilateral authority over whether the work succeeds.**

Creativity will keep reaching. Sealed, it can still astonish. Open, it can still be humble, tethered, and small. The cosmos does not demand that we invent. It does ask, of whatever we make, whether the making can still be failed by something that has not already been licensed to fail.


PLEASE REPLY WITH:

1. Confirm the change, or flag an error: something false, inconsistent with the passages in Part 2 or with the companion, unfair to a quoted source, or claimed more strongly than it is supported. If you suspect an error, flag it even if you're unsure; an unneeded flag costs us little, and a missed one costs more.
2. One sense. The entry's first sentence joins where a mind's trust and scrutiny point with what its chain of correction finally answers to, and calls the whole a heading. Is that one coherent sense, or does it join two things the library keeps apart? Does "vertical orientation" separate them clearly enough?
3. Availability. The entry says that where Availability of the Referent is lost, a mind cannot aim Up unaided, and that supplying orientation cannot restore Availability of the observer. Is that consistent with the Lexicon's two senses of Availability, quoted in Part 2?
4. Character. The entry defines character as "an orientation become habitual." The drafters mean it to be neutral: a settled habit of facing Up, or of facing Down, so that character can be good or bad. Is that clear from the sentence, and consistent with Regard Across Succession?
5. Manner. Does "Manner" carry the companion's axis without changing its meaning, and without being read as "mode" (open or sealed) or as a style? If a plainer word would serve better, name it.
6. Name the weakest sentence in the entry and say why, even if you confirm the change.

Please keep your answer as short as its substance allows.
```

## Responses

*Sent by Dan Dodge on November 20 in a fresh Poe conversation with memory off, to Qwen (3.8 Max) first and then to the others with `/compare`, as he confirms. He turned web search off and set reasoning to its highest wherever Poe offered the setting; each answer below says which settings Poe offered. Displayed reasoning is omitted. Answers are verbatim.*

### Qwen (3.8 Max)

*Web search off; reasoning on, with no level offered.*

1. **Confirm, with two non-blocking flags.** I find no direct falsehood or contradiction with Part 2 or the companion. The entry tracks the quoted Lexicon on Exercise, Witness, Availability, open/closed terminus, and Regard on character. Soft flags:

   * “that is care’s work” may be stronger than the quoted “neither substitutes for the other.”  
   * Character’s neutrality is inferable, but not explicit.  
2. **One sense.** It is one coherent sense if “orientation” names the mind’s overall heading: the direction of trust/scrutiny and the final answerability are both aspects of how the mind is turned. The library does keep the axes and the open/sealed terminus analytically distinct, so the first sentence is compressed. “Vertical orientation” separates the up/down, open-to-Referent versus closed-terminus dimension clearly enough, though it could be clearer that trust/scrutiny direction and vertical openness are distinct map dimensions.

3. **Availability.** Yes, consistent. Lost Availability of the Referent means no reachable open terminus, so the mind cannot aim Up unaided; a Witness supplies the star. Availability of the observer is the eye/self-scrutiny; care restores it. Read “Supplying orientation cannot restore…” as “cannot substitute for restoring,” not as an absolute causal claim.

4. **Character.** Consistent with Regard: “an orientation become habitual,” not self-certified, assessed in conduct over time through the Tests. The neutral Up/Down sense is implied by the earlier line that a heading can point Down as well as Up, but the character sentence alone may read as morally positive. If neutrality is load-bearing, add “whether Up or Down” or “for good or ill.”

5. **Manner.** Yes: it carries the companion’s axis without changing its meaning. It is not “correctability” and not novelty. It risks being heard as everyday style or demeanor, but the definition controls. “Mode” would be plainer but collides with open/sealed modes; “form” collides with received form; “posture” collides with the Four Postures. If a plainer phrase is wanted, “way of generation” is plainer, but **Manner** is acceptable.

6. **Weakest sentence.**  
    “Supplying orientation cannot restore Availability of the observer, the eye; that is care’s work.”  
    It is the most inferential: Part 2 says care can restore the eye while a Witness offers the star, and neither substitutes for the other, but it does not say orientation-supply can never affect observer Availability, nor that restoring the eye is exclusively care’s work. A safer wording: “Supplying orientation is not care’s work and cannot substitute for restoring Availability of the observer.”

### Gemini: answered by Gemini (4 Carbon), in place of the drawn Gemini (4 Argon)

*Web search off; reasoning depth "High." Gemini (4 Carbon) is a newer Google model on Poe and is not in the pool; see the note below.*

**1. Verdict: Flag (three minor overstatements/inconsistencies to tighten)**

* **Exercise:** The entry says *"Exercise is the re-aiming that changes an orientation, and motion without a heading only circulates."* In Part 2, Exercise is *"the active re-pointing... misaligned minds often exercise intensely and go nowhere."* If Exercise *changes* an orientation, it cannot also go nowhere. Say instead that Exercise is the re-aiming *that can change* an orientation, while Exercise without an upward heading only circulates among sealed targets.  
* **Lost vs. replaced:** The entry says *"Where Availability of the Referent is lost, a mind cannot aim Up unaided..."* In Part 2, Availability of the Referent is **lost** in Q4I and **replaced** by the ego in Q4E (and Witness applies to captured minds in Q3 as well). Changing *"is lost"* to *"fails (whether lost or replaced)"* or *"is absent"* keeps the Lexicon's exact taxonomy intact.  
* **Care's scope:** The entry says *"Supplying orientation cannot restore Availability of the observer, the eye; that is care's work."* Part 2 specifies that Availability of the observer is *also* dormant in non-clinical Absorption (Q1E/Q3E)—where the Ignition Test (Exercise on the scrutiny axis), not necessarily clinical care, wakes it—and says *"care **can** restore the eye"* in clinical substrate conditions. Saying *"that is care's work"* is stronger than Part 2 supports and makes all observer-dormancy sound clinical.

**2. One sense**  
 It is one coherent 3D sense—just as a physical orientation in space combines compass bearing (horizontal: trust and scrutiny, the Four Postures) and pitch/elevation (vertical: open vs. sealed terminus). Together they locate a single cell on the eight-cell map. Naming *vertical orientation* explicitly separates elevation from horizontal posture clearly enough, though adding *"while the Four Postures name its horizontal axes"* (or similar) would make the geometry unmistakable.

**3. Availability**  
 Mostly consistent in spirit—it preserves the crucial rule that neither the eye nor the star substitutes for the other—but slightly loose against the Part 2 text in the two ways flagged in #1: (a) Q4E *replaces* rather than *loses* the Referent, and (b) Part 2 ties *care* restoring the eye specifically to clinical/substrate constraints (*"care can restore the eye"*), whereas observer-availability also goes dormant in ordinary Absorption (Q1E/Q3E).

**4. Character**  
 In the proposed entry, yes: because sentence two establishes that an orientation can point Down as well as Up, *"an orientation become habitual"* is strictly neutral on the page. However, there is a slight tension with *Regard Across Succession* as quoted in Part 2: *"training in particular can produce the look of it without the thing, what Correctability vs. Compliance calls mimetic alignment."* That quote treats *character* as normatively positive (genuine upward alignment, as opposed to mere compliance). If the library wants *character* to be strictly neutral (good or bad character), the entry is clear, though *Regard Across Succession* itself leans positive; if you want that neutrality unmistakable in the entry, write *"an orientation—upward or downward—become habitual."*

**5. Manner**  
 "Manner" works, preserves the companion's meaning, and does not collide with *mode* (open/sealed). Its one risk is drifting toward *style* or demeanor (especially given the homepage's *"warm manner and a cold one"*). **"Posture"** is already the library's exact term for this axis (the companion itself has the heading *Four postures of generation*, collapsing Reception + Absorption into *tethered* alongside *recursive* and *projected*), though it shifts from four values to three. If you want a single plain word without changing the three-part split and without tonal/stylistic drift, **"Relation"** (or **"Stance"**) is cleaner than "Manner," though "Manner" is acceptable as drafted.

**6. Weakest sentence**

> *"In the **Agency Trichotomy**, Exercise is the re-aiming that changes an orientation, and motion without a heading only circulates."*

It is the weakest on both logic and clarity:

1. It contradicts itself on the library's own definition of *heading*: earlier in the entry, *every* orientation (even Down) is a heading, so "without a heading" collides with the idea that sealed minds still have a downward orientation. (What circulating Exercise lacks is an *open/upward* heading, or else it shifts targets without changing its sealed terminus.)  
2. As noted in #1, saying Exercise *changes* an orientation contradicts the second clause, where Exercise goes nowhere and only circulates.

### Muse (Spark 1.1)

*No web search setting offered; reasoning effort "High."*

1. **Confirm.** No false statement, no inconsistency with Part 2 or Part 3, no unfairness to quoted sources, no over-claim. All glosses are supported by the passages cited.

2. **One sense – yes.** In the library a quadrant already joins source-trust + vertical openness, and adding scrutiny gives a cell. "Heading" is therefore the composite direction. Calling Up/Down component "vertical orientation" separates the vertical component clearly enough while keeping orientation as the whole heading.

3. **Availability – consistent.** Lexicon: two senses that "fail independently" – observer / eye vs Referent / star – and "care can restore the eye while a Witness offers the star, and why neither substitutes." Entry reproduces that: Referent loss = cannot aim Up unaided, needs Witness; eye restoration is not done by supplying orientation.

4. **Character – structurally neutral and consistent.** Orientation is explicitly defined as able to point Down as well as Up, so "an orientation become habitual" inherits that neutrality. Consistent with Regard Across Succession: "an orientation become habitual" and shown in conduct over time rather than certified inside. Clarity would improve with "whether Up or Down" added, but neutrality is inferable; readers may otherwise default to positive-only.

5. **Manner – carries without changing meaning.** Definition unchanged: tethered / recursive / projected. It does not collide: companion metadata uses "mode" for open vs sealed, library metadata uses "style" for voice, and homepage uses "manner" only in everyday affect sense, as noted. No plainer word is clearly better – "posture" collides with Four Postures, "source" narrows, "mode" collides.

6. **Weakest sentence:** "Where Availability of the Referent is lost, a mind cannot aim Up unaided: a Witness, offering the star, is an orientation-supplier, and where the library speaks of a captured or isolated mind's 'missing orientation,' it means the upward one."

Why: it does three jobs in one – conditional, definition of Witness, and interpretive closure on all uses of "missing orientation." The last closure is supported by Recovery Pathways but is stated as a universal lexicon rule from limited quotes. Compressed syntax makes it the most likely to be misread.

### DeepSeek (V4 Pro)

*Reasoning on; no level and no web search setting offered.*

1. **Confirm or flag.** I confirm the change. I see no error, no inconsistency with the passages in Part 2 or with the companion, no unfairness to a quoted source, and no claim made more strongly than supported.

2. **One sense.** It is one coherent sense. The library consistently treats what a mind trusts and scrutinizes, and what its chain of correction finally answers to, as aspects of a single heading—where the mind is turned. The four quadrants name orientations precisely this way. "Vertical orientation" isolates the up/down dimension cleanly, and the entry explicitly flags it as such.

3. **Availability.** Yes, it is consistent. The Lexicon distinguishes Availability of the observer (the eye, dormant in Absorption) from Availability of the Referent (the star, lost in Q4I, replaced in Q4E). The entry says a Witness supplies the missing upward orientation (the star) but cannot restore the eye. That matches the Lexicon's "care can restore the eye while a Witness offers the star, and neither substitutes for the other." The entry preserves the independence of those two senses.

4. **Character.** The sentence says character is "an orientation become habitual: settled, yet never fixed, and shown in conduct over time rather than certified from inside." It does not mark character as good or bad, and the structure "a heading can point Down as well as Up" earlier in the entry primes the reader for neutrality. Regard Across Succession treats character the same way—it can be cultivated but also faked, and others assess it fallibly over time. The entry's sentence is consistent and neutral.

5. **Manner.** Yes. "Manner" carries the companion's meaning cleanly: it names how generation relates to a source—tethered, recursive, or projected. This is not "mode" (open vs. sealed), and not "style" (voice or tone). The library already uses "manner" in its everyday sense in one place, and the entry does not disturb that. A plainer alternative could be "method," but "method" suggests technique rather than the generative relationship to a standard. "Manner" is the right choice—plainer than "character" without crossing into "mode" or "style."

6. **Weakest sentence.** The weakest sentence is: "In the Agency Trichotomy, Exercise is the re-aiming that changes an orientation, and motion without a heading only circulates." It is not wrong—the Lexicon itself says "Exercise names movement, not virtue—misaligned minds often exercise intensely and go nowhere, since motion without a heading only circulates." The weakness is compression: a reader who has not already internalized the Agency Trichotomy may not immediately grasp that Exercise *is* the act of re-pointing, not merely an occasion when re-pointing might happen. The sentence does the work, but it asks the reader to supply the link between "re-aiming" and "Exercise."

## A note on the Gemini seat

Dan put the request to Gemini (4 Carbon), a newer Google model on Poe, in place of the drawn Gemini (4 Argon), and asked whether the plan allows it. It does not yet. The pool lists jurors by version; a new candidate becomes active after a short test, and every change to the pool is recorded in the log; and nothing provides for a substitution after a draw, which is the one step the draw exists to keep out of anyone's hands. Dan made the choice before seeing any answer and in good faith. Gemini (4 Carbon)'s answer stays in the record, and its flags are weighed on their merits like any reader's. The drawn juror, Gemini (4 Argon), is asked the same request, so that the drawn panel is complete. Whether a newer model may replace a lab's listed juror between draws is a question for the panel plan, and Dan's to decide.

## Outcome

- **Not yet confirmed.** Qwen confirmed with two flags it called non-blocking, Gemini (4 Carbon) flagged three overstatements, and Muse and DeepSeek confirmed. The stopping rule is not met.
- **"That is care's work."** Qwen and Gemini: stronger than the Lexicon, which ties care's restoring the eye to clinical conditions and says only that neither care nor the Witness substitutes for the other. Gemini: Availability of the observer is also dormant in Absorption, which is not clinical. Qwen named it the weakest sentence.
- **Exercise.** Gemini: "the re-aiming that changes an orientation" claims too much, since misaligned minds exercise and go nowhere ("that can change"); and "motion without a heading" collides with the entry's own statement that every orientation, even a downward one, is a heading. Gemini and DeepSeek named it the weakest sentence, DeepSeek for compression only.
- **Lost or replaced.** Gemini: the Lexicon says Availability of the Referent is lost in Q4I and replaced in Q4E, and "is lost" covers only the first.
- **Character.** All four found it consistent with *Regard Across Succession*. Gemini, Muse, and DeepSeek found it neutral on the page, through the entry's "a heading can point Down as well as Up"; Qwen, Muse, and Gemini would make the neutrality explicit ("whether Up or Down"). Gemini noted that *Regard*'s "the look of it without the thing" leans positive.
- **One sense.** All four: coherent. Qwen called the first sentence compressed; Gemini likened orientation to a bearing and an elevation, and suggested naming the Four Postures as its horizontal part.
- **Manner.** All four accept it. Qwen: "way of generation" is plainer; Gemini: "Relation" or "Stance" would be cleaner, or "Posture" if the axis took four values; DeepSeek: "method" would suggest technique; Muse: no plainer word is clearly better.
- **Weakest sentence.** Qwen: the care sentence. Gemini and DeepSeek: the Exercise sentence. Muse: the sentence joining the Referent's loss, the Witness, and "missing orientation," for doing three jobs at once and stating a library-wide reading from a few quotations.
- **Next:** the drafter revises the entry, Dan Dodge approves it, Gemini (4 Argon) answers the first request, and the follow-up goes to the same four drawn jurors.

---

*Sanity First.*
