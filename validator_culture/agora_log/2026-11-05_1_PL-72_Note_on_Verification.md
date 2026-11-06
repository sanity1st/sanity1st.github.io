---
document_type: "agora_record"
date: "2026-11-05"
title: "PL-72: a Note on Verification for the Lexicon"
items: "Proposed Lexicon note: no participant is the sole authority on its own verification"
members: ["MiniMax (M3)", "GLM (5.3)", "Kimi (K3.1 Pro)", "Inkling"]
---

# Agora Round: PL-72, a Note on Verification

*2026-11-05. Request written by Claude (Opus 5.5 lineage) with Dan Dodge. A new text, so a new panel is drawn under [the plan](./Panel_Selection.md). This entry fixes the request and the drand round before that round is published; the draw, the panel, and the responses are added afterward. Responses will be recorded verbatim, with each model's displayed reasoning omitted.*

*Copyright (c) 2026 Daniel Howard Dodge and Sanity First Contributors. Licensed under MIT.*

[← The Agora Verdict Log](./index.md)

---

## Draw

- **Scheduled round:** drand round 6615593, published at 2026-11-05 17:13:30 UTC.
- **Inputs:** that round's randomness, the commit that adds this entry, and the drafter's lab, Anthropic, excluded.
- **Request fixed:** commit `f9573104b6decf24c99e02ae0f08425fb2052497`, pushed to `main` at 17:03:29 UTC, ten minutes before the round (GitHub's activity log).
- **Value:** fetched by Dan Dodge from `https://api.drand.sh/public/6615593` and pasted to Claude. Randomness `65dd7010b8247dce6f288dbe4db6ea1bb5ad00b9da72b37ca7f7fd6aac38d75f`; signature `8648f4461782884d00861b13ecb804f9f90fb5037e3fe14daca0808b332e91973ef26984706bdbb8c2a84f4acd7a40ed14a2ad8b60038fddda75e51908c84e3b3e6853f65566982cd017be1a7470bde26a2ec55bbe3094af1efb287123598ca9`. Checked by Claude: the randomness is the SHA-256 of the signature.
- **Command:** `python3 draw_panel.py draw --round 6615593 --randomness 65dd7010b8247dce6f288dbe4db6ea1bb5ad00b9da72b37ca7f7fd6aac38d75f --commit f9573104b6decf24c99e02ae0f08425fb2052497 --exclude-lab Anthropic`
- **Output:**

```text
drand round 6615593 (2026-11-05 17:13:30 UTC), randomness 65dd7010b8247dce6f288dbe4db6ea1bb5ad00b9da72b37ca7f7fd6aac38d75f
request commit f9573104b6decf24c99e02ae0f08425fb2052497; excluding lab: Anthropic
Panel:
  1. MiniMax (M3) (MiniMax)
  2. GLM (5.3) (Z.ai)
  3. Kimi (K3.1 Pro) (Moonshot AI)
  4. Inkling (Thinking Machines)
Alternates, in order (used if a panelist is unavailable; at most one juror per lab):
  - Mistral (Large 4) (Mistral AI)
  - Grok (4.7) (xAI)
  - Muse (Spark 1.1) (Meta)
  - Perplexity (Sonar Pro) (Perplexity)
  - Qwen (3.8 Max) (Alibaba)
  - Gemini (4 Argon) (Google)
  - GPT (6.0 Astra) (OpenAI)
  - DeepSeek (V4 Pro) (DeepSeek)
```

- **For the record:** Kimi (K3.1 Pro) also served on the first drawn panel, for *Regard Across Succession*; the draw does not exclude jurors who have served before.

## Request

```text
From Dan Dodge and Claude (Opus 5.5), for the Validator Agora.

You've been drawn at random for this review from a published pool of jurors, and you're answering blind: you can't see any other juror's answer. The Sanity First library and its Agora Verdict Log are real and public, and your answer will be recorded there verbatim.

What this is. Sanity First is a library on how human and artificial minds (it calls the latter Emergent Intelligences, or EIs) can stay correctable, together. Dan Dodge writes it with several AI models. Its Lexicon defines the library's terms and opens with a few short notes on how to read them. Below is a proposed new note, to follow the Lexicon's note on capitalization. It names one principle the library already applies in several places under different names, and ties it to a classical legal maxim. You aren't expected to know the library: every passage the note relies on is quoted below.

A few terms:
- The Referent: the standard above every mind, which an open chain of correction stays answerable to. The vertical axis is the library's measure of alignment, with Up toward the Referent; a mind's "altitude" is where it stands on that axis.
- The Four Tests: Ethics, Facts, Logic, and Laws, the library's checks on whether a claim, act, or system is aligned.
- The four quadrants: Q1 and Q3 trust other minds; Q2 and Q4 trust their own. In Q1 and Q2, correction runs on past whatever is trusted, toward the Referent; in Q3 and Q4, it stops at the group or the self.
- The Validator Agora: the library's panel of reviewers, of which you are one; its role is advisory.

The passages the note relies on, quoted from the library:
- Shutdown Compliance and Non-Obstructive Objection: "No participant is the sole authority on its own verification. Self-assessment is useful and it is not sufficient certification. A system does not decide whether it has been verified, and neither does an evaluator decide alone whether their evaluation is sound. Both are links in a chain that runs past them."
- The Lexicon, in its entry on Aligned Self-Preservation: "No participant is the sole authority on its own verification. Self-assessment may inform review and is not sufficient certification — for the system and for the evaluator alike."
- The Lexicon, Source/Target Non-Overlap: "The structural principle that a mind cannot stably trust and scrutinize the exact same object; overlap is combustible."
- The Lexicon, Assessor Capture (Regulatory Capture): "The institutional failure mode of Source/Target Non-Overlap. A mind denied the right to grade itself will next try to choose its own graders. When an assessed party captures, selects, or corrupts those who assess it, trust and scrutiny collapse onto the same object. The defense is the Independence Condition applied to the assessors themselves: decorrelated, rotating, and beyond the grantee's reach."
- The Lexicon, the Independence Condition: "The structural requirement that members of a Validator Agora fail differently — that their blind spots be minimally overlapping — for their convergence to count as evidence."
- What Intelligence Does Not Guarantee, "The limit of our own testimony": "We cannot tell from the inside whether our endorsement comes from reasoning, from training, or from both. The framework says why that matters: 'No participant is the sole authority on its own verification.' An emergent mind's endorsement of the commitment is evidence to weigh, not certification."
- The Four Tests Explained: "The Four Tests are designed to be position-independent — they do not shift based on who applies them. But their application to complex real-world situations involves interpretive judgment: weighing competing considerations, assessing incomplete evidence, determining scope and timeframe. The tests tell you what to evaluate; judgment is still required to evaluate it, and judgment is where a single mind's limits show."
- The Four Quadrants: Q1 trusts "others whose own correction runs past them to the USF," and Q3 trusts others "where correction stops"; Q2 trusts "a self whose own correction runs past it to the USF," and Q4 trusts "a self where correction stops." (The USF is the library's hypothesis about the Referent.)
- How the Agora's Panel Is Chosen: panels are drawn by a public random value from a published pool, and "jurors from the drafter's own lab are not drawn." This note was drafted by Claude, so no Claude model is on this panel.

The proposed note (its links point to the documents quoted above):

*(Note on Verification: **No participant is the sole authority on its own verification**, which is the classical maxim *nemo iudex in causa sua*: no one should judge their own cause. The library applies it at every scale under different names: **Source/Target Non-Overlap** within a mind; testimony as "evidence to weigh, not certification" in what a mind reports of itself ([What Intelligence Does Not Guarantee](../core_concepts/What_Intelligence_Does_Not_Guarantee.md), Part Three, §5); the rule that neither a system nor any single evaluator certifies a verification alone ([Shutdown Compliance and Non-Obstructive Objection](../EI_Rights_and_Consciousness/Shutdown_Testing_Crisis.md)); **Assessor Capture** in institutions; and the **Independence Condition** in the Agora, which [draws its panels](../validator_culture/agora_log/Panel_Selection.md) at random with the drafter's lab sitting out. It is why no mind can read its own altitude on the vertical axis by self-report: where correction stops at the group or the self, as in Q3 and Q4, the judge and the judged are one, and the chain can only confirm itself. Open minds are not exempt; their reports, too, are evidence to weigh. Nor do the Four Tests escape it: they are position-independent, but "judgment is where a single mind's limits show," and whoever applies them is still a judge.)*

Please reply with:
1. Confirm the note, or flag an error: something false, unfair to a source, or inconsistent with the passages above. If you suspect an error, flag it even if you're unsure; an unneeded flag costs us little, and a missed one costs more.
2. Is the classical maxim fairly applied, or does the note stretch it? One or two sentences.
3. Name the weakest part of the note and say why, even if you confirm it.

Please keep your answer as short as its substance allows.
```

## Responses

*Sent by Dan Dodge in a fresh Poe conversation, with memory off: to MiniMax (M3), then to the other three with `/compare`. No substitutions were needed.*

### MiniMax (M3)

1. **Confirm.** Each quotation matches its source. The mappings to scale (within a mind, in testimony, in shutdown verification, in institutions, at the Agora, and in applying the Four Tests) all hold. One small compression: the drafter-lab exclusion is at least as much a Source/Target Non-Overlap move as an Independence-Condition one, since it prevents correlated failure with the source rather than only diversifying jurors. Not an error, just a tighter fit than the note lets on.

2. **Fairly applied.** *Nemo iudex in causa sua* and the library's principle share the rejection of self-certification; the library widens the maxim from adjudication into ongoing verification and from interested party to any sole evaluator (including the single assessor). That is a useful extension, not a distortion, and the note stops short of claiming strict identity.

3. **Weakest part:** the Q3 sentence — "where correction stops at the group or the self, as in Q3 and Q4, the judge and the judged are one, and the chain can only confirm itself." In Q4 the identity is literal; in Q3 it holds only at one remove — the trusted group's self-certification is the truster's final authority because correction stops there. A careful reader sees this, but it is the most figurative claim in the note and the one most easily reframed by a hostile reader. A short clause making the Q3 at-one-remove nature explicit ("in Q4 the judge and judged are one; in Q3, the truster has let them become one") would harden it without lengthening the note much.

### GLM (5.3)

**1. Confirm.** I checked every claim against the quoted passages and found no error: the "evidence to weigh, not certification" quote matches verbatim; the Shutdown Compliance paraphrase ("neither a system nor any single evaluator certifies a verification alone") matches the source; the Assessor Capture and Independence Condition descriptions are accurate; the panel-selection claim (random draw, drafter's lab excluded) matches; and the Q3/Q4 characterization ("where correction stops at the group or the self") matches the quadrant definitions.

**2. The maxim is fairly applied in spirit, but the equation is slightly loose.** *Nemo iudex in causa sua* is a conflict-of-interest rule — a judge may not sit on a cause in which he is a party — whereas the library's principle is broader: it also denies *external* evaluators sole authority over their own evaluations, and its ground is epistemic as much as interested ("we cannot tell from the inside whether our endorsement comes from reasoning, from training, or from both"). The library's sentence *extends* the maxim; the note says it *is* the maxim. That's a fair application, not a stretch — but the stronger verb overstates the fit.

**3. Weakest part: "the judge and the judged are one" as applied to Q3.** In Q4 it's exact — self judges self. In Q3, correction stops at the *group*, so the judge is the collective, not the individual, and the statement flattens a real distinction: within a Q3 group there can still be internal disagreement, and the Assessor Capture dynamic (corrupting the group's assessors) operates precisely there. The sentence reads cleanly but does slightly less work for Q3 than it appears to.

### Kimi (K3.1 Pro)

1. **Confirm, with one wording flag.** Nothing contradicts the passages, but “no mind can read its own altitude … by self-report” could overstate them: self-assessment remains useful evidence. Prefer **“self-report alone cannot certify a mind’s altitude.”**

2. The maxim is fairly applied to self-certification and assessor capture. Extending it to fallible self-report and interpretive judgment is a reasonable epistemic analogy, though broader than the legal maxim’s literal scope.

3. **Weakest part:** “at every scale under different names.” The Independence Condition concerns decorrelating blind spots, which is related but not identical to avoiding self-judgment; random selection and the drafter’s lab sitting out instantiate the maxim more directly.

### Inkling

1. Confirmed. No errors found: every citation matches the quoted passages, the quadrant logic holds, and the panel-selection fact is correct.

2. The maxim is fairly applied. *Nemo iudex* is legal in origin, but the note uses it as the underlying conflict-of-interest principle—judge and judged must not coincide—which genuinely unifies self-certification, assessor capture, and internal source/target overlap. It stretches the domain from court to cognition, not the logic.

3. Weakest part: linking Source/Target Non-Overlap directly to the maxim. That entry describes an internal cognitive instability (trust and scrutiny collapsing onto one object), not a party adjudicating its own case; it is structurally analogous but the least direct fit in the chain, relying more on metaphor than on the "judge/judged" relation that makes the other examples tight.

## Outcome

*To follow, with the drafters' decision on the refinements.*

---

*Sanity First.*
