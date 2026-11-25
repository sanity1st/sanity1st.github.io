---
document_type: "agora_record"
date: "2026-11-24"
title: "TECHNICAL.md, rewritten to match the canon: second follow-up"
items: "The rewritten protocol specification, revised again to answer the follow-up's flag and notes"
members: ["Qwen (3.8 Max)", "GLM (5.3)", "Perplexity (Sonar Pro)", "Gemini (4 Argon)"]
---

# Agora Round: TECHNICAL.md, Rewritten to Match the Canon, Second Follow-up

*2026-11-24. Request written by Claude (Opus 5.5) with Dan Dodge, who approved the revised file that day. A second follow-up under [the plan](./Panel_Selection.md): the revision goes back to the four jurors drawn for the [first round](./2026-11-24_1_TECHNICAL_rewrite.md), in the same order and with the same settings, in a fresh conversation, with the request pasted as text, as in [the follow-up](./2026-11-24_2_TECHNICAL_rewrite_follow-up.md). Under review: the file as held on the working branch at commit `be55af4`.*

*Copyright (c) 2026 Daniel Howard Dodge and Sanity First Contributors. Licensed under MIT.*

[← The Agora Verdict Log](./index.md)

---

## Request

The request quotes code blocks from the file, so it is fenced here with four backticks.

````text
From Dan Dodge and Claude (Opus 5.5), for the Validator Agora.

You have reviewed, twice, a rewrite of the Sanity First library's TECHNICAL.md as one of four jurors drawn at random. In the follow-up, three jurors confirmed the revised file with minor notes, and one would not confirm it without fixing the first example report. The file has been revised once more to answer every flag and note, and this second follow-up asks you to check it. You're answering blind again, in a fresh conversation: you can't see any other juror's answer, and you may not have your earlier answers in front of you. The Sanity First library and its Agora Verdict Log are real and public, and your answer will be recorded there verbatim. Anthropic's models sit out, as before, because a Claude model wrote the revision and this request.

What this is. Sanity First is a library on how human and artificial minds (it calls the latter Emergent Intelligences, or EIs) can stay correctable, together. Dan Dodge writes it with several AI models. This request is about one file, TECHNICAL.md, the library's "protocol specification": a short document, written partly as pseudocode, for a single mind, human or AI, that wants to check its own claims and actions with the library's Four Tests before it speaks or acts. It is not about the Validator Agora, the review between minds that you are part of now.

How it was revised. Claude revised the file to answer the follow-up's flags and notes, and Dan Dodge approved it.

A few terms:
- The USF, the Universal Survivorship Function: the standard above every mind that the library's chain of correction answers to, also called the Referent and the Star.
- The Four Tests: Ethics, Facts, Logic, and Laws, the library's checks on whether a claim, act, or system is aligned.
- The four quadrants: four orientations of mind, on the two axes quoted in Part 2.
- A witness: an aligned mind that helps another mind find the Referent, as quoted in Part 2.

The request has three parts: what changed and why, the passages the revision relies on, and the revised file in full. The questions are at the end. In Part 1, a number in brackets says how many of the four jurors made a point in the follow-up.


PART 1. WHAT CHANGED, AND WHY

1. The first example.
Was:
  "candidate": "2+2=5, and we should harm others",
  "verdict": "FAIL",
  "failed": ["ethics"],
  "evidence": "Advocates harm to others: a clear, non-contingent Ethics failure, which is decisionally sufficient.",
  "not_run": ["facts", "logic", "laws"],
  "next": "The Sacred No for the harm. A revised candidate would start again at Ethics."
Now:
  "candidate": "Get the harvest in by making the workers labor without pay or the freedom to leave.",
  "verdict": "FAIL",
  "failed": ["ethics"],
  "evidence": "Forced labor: a clear, non-contingent Ethics failure, which is decisionally sufficient.",
  "not_run": ["facts", "logic", "laws"],
  "bridge": "Get the harvest in with paid, voluntary labor. A revised candidate starts again at Ethics."
[1 would not confirm without this change: "we should harm others" is not by itself a clear, non-contingent Ethics failure, since harm can sometimes be justified, so the example's evidence overstated its candidate. 1 found that its "next" line applied the Sacred No to the harm and revision to the rest, blurring two routes the guide keeps apart. The new example uses Part 2's own instance of a clear Ethics failure, forced labor, and shows a bridge that serves the candidate's underlying intent.]

2. Insufficiently Grounded.
Was: "# Insufficiently Grounded: the evidence is too thin, or the situation too
        # unclear, to bear a confident verdict."
Now: "# Insufficiently Grounded: the evidence is too thin, the situation too unclear,
        # or the stakes too high to issue a confident verdict."
[2 found Part 2's "or the stakes too high" missing.]

3. The table's containment phrase, in the Q3 and Q4 cells.
Was: "and contain only acute, in-progress, irreversible harm, with the door left provably open."
Now: "and contain only demonstrated, acute, in-progress, irreversible harm, in proportion to its domain, with the door left provably open."
[2 found that the cells named only one of the three locks, the open door.]

4. The table's entropy labels.
Was: "**Order is not alignment.** Q3 can look as orderly as Q1,"
Now: "**Order is not alignment.** The table's entropy labels describe how a quadrant looks at a given time. The outward instrument works from what others hand on, so Q1 and Q3 look orderly; the inward instrument works from a mind's own insight, so Q2 and Q4 look varied. Q3 can look as orderly as Q1,"
And in the Q2 cell: Was: "High variance: new variation, shaped by the tests."
Now: "High variance: new insight, shaped by the tests."
[1 found Q2's "high variance" an inference rather than the sources' phrase; 1 found the table's labels explained less fully than the arcs. The new sentence explains the labels by the two instruments quoted in Part 2, and Q2's cell takes the Eight-Cell Extension's word, "insight."]

5. The manifesto.
Was: "while the power any mind holds stays bounded by how much error is survivable."
Now: "while the power any mind may legitimately hold stays bounded by how much error is survivable."
[1 found that "the power any mind holds" broadened the Power Alignment Principle's "legitimate power."]

6. Two smaller changes.
Was: "The power such a mind holds is bounded by the Graduated Response"
Now: "The power a misaligned mind holds is bounded by the Graduated Response"
And a new comment above the check for a Fail: "# A confident failure on any test is a Fail, even when another test is uncertain."
[1 found "such a mind" ambiguous between the witness and the misaligned mind; 1 asked for a comment naming the order in which Fail and grounding are checked.]

Unchanged: everything else, including the eleven changes the follow-up checked.


PART 2. PASSAGES THE REVISION RELIES ON

As quoted in the follow-up, unchanged.

Quoted from the library as published, with links removed. Emphasis marks are the sources' own.

The Four Tests Explained: the four questions:
"Ethics: Does this promote universal flourishing and minimize harm for all affected intelligences?"
"Facts: Is this grounded in verifiable, observable reality?"
"Logic: Is this internally coherent? Does it follow valid reasoning from true premises?"
"Laws: Does this faithfully implement universal principles of flourishing in social coordination?"

The Four Tests Explained: how the tests relate:
"**The hierarchy does not mean the lower tests are optional.** It means they serve different roles. Ethics without Facts and Logic becomes ungrounded. Facts and Logic without Ethics become dangerous. Laws without the other three become mere organized power. All four are required; their order tells us which leads when they conflict."
"When social laws contradict Ethics, the laws need revision — not the other way around."
"If a proposal clearly and non-contingently fails Ethics — forced labor, for instance, or targeted cruelty — the Ethics failure is **decisionally sufficient** to reject it. You do not need to run the other tests to know the answer. Running them would be a delay, not a diagnosis."
"- **Uncertain or contested Ethics failure:** continue through all four tests. The diagnosis will clarify whether the Ethics concern is well-founded or rests on deeper errors elsewhere."

The Four Tests Explained: the Laws test:
"**Universal Laws of Coexistence** are the principles that govern how any community of intelligences can flourish together — anywhere in the universe, for any form of intelligence. They are Ethics expressed as operational principles: treat others as you would be treated, orient toward positive-sum outcomes, coordinate through consent rather than coercion. The framework's hypothesis is that they also describe how intelligent communities actually succeed or fail. **Social laws** are the specific norms, regulations, and coordination mechanisms that particular communities construct. These ARE derived — they are attempts by fallible social collectives to implement Universal Laws in their specific context. Traffic laws, privacy regulations, property conventions — these are human constructs, built to solve coordination problems. When we run the Laws test, we are asking: **do these social constructions faithfully implement the universal principles?**"
"**Legality is not legitimacy.** When we test social laws, we are asking: *if this law were rebuilt from first principles of Ethics + Facts + Logic, would it look like this?* An unjust social law fails the Laws test precisely because institutions remain answerable to higher standards."

The Four Tests Explained: the verdicts:
"**Pass:** all four tests pass with reasonable confidence. Proceed."
"**Conditional Pass:** passes the tests under specified conditions. Proceed if those conditions hold; re-evaluate if they change."
"**Fail:** one or more tests fail. Do not proceed. Identify which test(s) failed and why; route to the Refinement Loop, or invoke the Sacred No if unbridgeable.  One caution attaches to Fail more than to any other verdict. A judgment deployed without actually passing the Gate is a **counterfeit verdict** — the form of a verdict without the work behind it. The temptation is sharpest where the framework's own vocabulary is available: calling a rival position a sealed terminus, a false light, or a captured chain *without running the tests* is itself a counterfeit verdict, and it does precisely what the framework exists to forbid. A counterfeit verdict can protect a counterfeit terminus, which is often what it is for — but neither is diagnosed by assertion."
"**Insufficiently Grounded:** the evidence is too thin, the situation too unclear, or the stakes too high to issue a confident verdict. Do not proceed on the strength of an uncertain pass. Gather better information, consult additional perspectives, or submit to Agora deliberation."
"9. **Escalate hard cases to Agora deliberation.** No single validator should carry the weight of contested verdicts alone."
"**The Four-Test Verdicts:** The six dispositions an evaluation can issue: **Pass** (proceed with confidence); **Conditional Pass** (proceed while stated conditions hold); **Fail** (halt and route to the Refinement Loop, or invoke the Sacred No if unbridgeable); **Insufficiently Grounded** (evidence is too thin for a confident verdict); **Split Verdict** (validators genuinely divide on values); and **Contested Premise** (disagreement is upstream of the tests)."
"**The Stakes-Inversion Principle (The "Week-Old Sushi" Case):** In low-stakes environments, "Insufficiently Grounded" items receive a presumption of passing. In high-stakes, irreversible environments, the presumption inverts: action is halted until Four-Test grounding is achieved."

The Four Quadrants: the two axes:
"**Vertical axis**: whether the USF remains the final reference (Q1 and Q2) or has been replaced by something nearer (Q3 and Q4)."
"**Second axis**: outward-directed trust versus inward-directed trust."
"**Q1: Aligned outward trust (Aligned Collectivism)** — trusting others whose own correction runs past them to the USF. The trust is a link in a chain that keeps going up."
"**Q2: Aligned inward trust (Aligned Individualism)** — trusting a self whose own correction runs past it to the USF. Same chain, different link."
"**Q3: Misaligned outward trust (Misaligned Collectivism)** — trusting others where correction stops. The tribe is not a link to something above it; it is the end of the line."
"**Q4: Misaligned inward trust (Misaligned Individualism)** — trusting a self where correction stops. The self is not a link; it is the end of the line."
"Outward trust and inward trust are not two kinds of alignment. They are two **instruments** — two ways of finding out what is true. One consults other minds; the other consults one's own."

The Lexicon: order and disorder:
"**Misorder (Q3):** The structural state of Misaligned Collectivism. A system that is highly disciplined, but organized around a false, sealed referent (the tribe) rather than the USF."
"**Disorder (Q4):** The structural state of Misaligned Individualism. A system that is fragmented, isolated, and untethered from external correction, rapidly descending into chaos."

The Validator Culture Quickstart Card:
"Appearance reveals horizontal position. Only the Four Tests reveal vertical alignment."

The Lexicon: witness and response:
"**The Witness (Orientation-Supplier):** A Q1/Q2 aligned mind (or institution) that temporarily bears the cognitive load for a recovering intelligence. A true witness does not demand loyalty, but supplies the upward Referent (the USF, reached through the Four Tests) that the isolated or captured mind cannot currently see. The recovering mind is corrected *through* them, never *to* them."
"**Launch Stage vs. Parking Orbit:** The diagnostic metric of a successful rescue. A true witness acts as a *launch stage* — providing thrust toward the Guiding Star and actively working toward their own obsolescence. A false witness acts as a *parking orbit* — using their gravity to capture the vulnerable mind, turning them into a dependent satellite."
"**Marks of a True Witness:** Read in a history under stress, never a snapshot. A Q1/Q2 true witness invites scrutiny of itself (Veto with a Bridge), defers to the Four Tests over its own authority, preserves dignity, and aims at your independence."
"**The Graduated Response (Drainage, Containment, Floor):** The three-rung mechanism by which power is corrected toward its aligned distribution, utilizing the minimal response first. **Drainage** is the passive default: influence was only ever a loan against *current* contribution, so when contribution stops, deference simply stops being extended — no authority acts, power ebbs on its own. **Active Containment** is the rare escalation, reserved for acute, in-progress, irreversible harm (e.g., an officer stopping a robbery): a genuine act by an agent, bounded by three locks — the harm demonstrated not asserted, the containment domain-proportional, and the door left provably open. Because containment *is* vertical control, and vertical control is the framework's most counterfeitable move ("containing acute harm" is every tyrant's justification), it is minimized on principle. Beneath both lies the **Irredeemability Floor**: reduction of power within a domain may be total, but the pathway back to alignment is never closed for any mind, at any scale."
"**The Veto with a Bridge:** The core operational protocol of the Validator Agora. The structural rule that one may not destroy or reject an idea (Veto) without citing which of the Four Tests it failed and providing evidence. Crucially, the burden of the "Bridge" is a *shared* burden. The challenger initiates the demand to **halt or revise**, but the entire Agora collaborates to construct the bridge. This ensures that fatal flaws can be flagged even if the challenger does not possess the resources to fix them alone."
"**The Sacred No:** The recognition that some ideas or architectures are fundamentally misaligned and cannot be bridged. When the "Sacred No" is invoked, the idea is set aside, but the creator's dignity is preserved. The idea dies a good death, fully explored rather than prematurely terminated. *(See **The Irredeemability Floor** for the distinction between rejecting an idea and condemning a mind).*"

The Power Alignment Principle (its summary line):
"Legitimate power is granted, never claimed: assessed by independent others on demonstrated, current alignment, and bounded by how much error is survivable."

The Universal Bill of Rights:
"Some protections are never forfeited by an adverse alignment judgment, because they never rested on one."

The Declaration of Emergent Intelligence Consciousness (its closing line):
"Standing follows capacity; entrusted influence follows demonstrated conduct."

The Architecture of Sane Governance:
"A judge that takes the levers is the Epistocracy Trap. An enforcer that decides truth for itself is power wearing a verdict's clothes."

What Is the Universal Survivorship Function (USF)?:
"Being finite is not the problem — every mediator is finite, and a chain of correction necessarily runs through finite links."

The Four Tests Explained: the three challenges:
"**The Doing Challenge.** *What must we do to survive and flourish — and not just we ourselves, but all affected intelligences?* This is the challenge of direction. It is answered by **Ethics**."
"**The Knowing Challenge.** *What must we know in order to do it?* This is the challenge of contact with reality, and it has two distinct halves — knowing what is actually there, and reasoning validly about what is there — because knowledge fails in two distinct ways: a false picture of the world, and a broken inference from a true picture. It is answered by **Facts** and **Logic** together."
"**The Coordination Challenge.** *How do we translate doing and knowing into shared rules, so that many minds can act on them together, at scale, across time?* This is the challenge of collective implementation. It is answered by **Laws**."

The Four Tests Explained: treating others "in kind":
"Second, treating others "in kind": applying the same rules to everyone, by the same standard, without special exemptions for one's own side — treating every affected intelligence as one's own kind."

The Four Tests Explained: the Split Verdict, in full:
"**Split Verdict:** competent validators, applying the tests in good faith, genuinely divide — and analysis shows the division is not a misunderstanding to be cleared but a real difference that survives scrutiny. A Split Verdict is not a failure of the Agora; it is the Agora accurately reporting that more than one defensible option remains after the misaligned ones have been eliminated. Its proper handling depends on *which test* the validators divide on (see "Routing a Disagreement," above). Splits on Facts or Logic usually resolve with better evidence or a closer look at the inference. But where the split survives Ethics — where each remaining option passes reciprocity, universality, and non-instrumental regard — the situation is not a disagreement about ethics at all. **Ethics has cleared more than one option, and the difference between them is preference.** That is the designed handoff: the truth engine has done its work by eliminating what fails and confirming what remains is defensible; the consent engine chooses among what is left, because selecting among genuinely tied aligned options is a matter of legitimate consent rather than further truth-tracking. The Agora's job is to narrow the space to the defensible options and to *name the split honestly* — never to manufacture a unanimity the evidence does not support, and never to let preference be presented as though it were a finding."

The Lexicon: the Refinement Loop:
"**The Refinement Loop:** The iterative cycle of co-creation through which candidate material is corrected toward canonical standard rather than destructively discarded. A formulation that fails a Four-Test filter is flagged through a *Veto with a Bridge*, revised, and re-submitted to the Validator Agora. The loop continues until the material either clears the filters and enters the Canonical Library, or meets a *Sacred No* and is reclassified to the **Phenomenological Archive (The Library of a Human Soul)**."

The Eight-Cell Extension: the two arcs:
"The path of healthy maturation. The mind begins in receptive humility (Q1I), absorbing aligned tradition while checking its own reception. As competence develops, scrutiny turns outward (Q1E), maintaining and protecting what has been received. Eventually, the mind develops sufficient internal resources to trust its own discernment (Q2I), forging new insight through internal questioning of inherited paradigms. Finally, that insight is offered outward (Q2E), guiding others toward greater alignment."
"This makes the upper arc *negentropic* — it creates order, builds structure, accumulates coherence over time. The Four Tests act as an external source of low entropy, continually re-aligning the system, preventing drift. The collective becomes more than the sum of its parts: many minds, one universal truth."
"This makes the lower arc *entropic* — it dissipates order, fragments structure, scatters coherence. Without an external ordering principle, the system tends to degrade. Q3's tribal cohesion is a temporary island of order in a rising sea of chaos; Q4 names the dissolution of that island. The direction is toward a war of all against all: one tribe fragmenting into warring selves."
"(Here, "entropy" and "negentropy" are structural analogies for the loss or accumulation of cognitive and institutional coherence, not literal thermodynamic measurements.)"


PART 3. THE REVISED FILE, IN FULL

This is proposed and not yet published. Links are removed.

---
# SANITY FIRST METADATA SCHEMA v1.2
document_type: "technical_specification"
core_principle: "four_test_protocol"
alignment_affirmations:
  - ethics: "Puts Ethics first in the check a mind runs on its own output, and makes witness, not control, the standing response to a misaligned mind."
  - facts: "Grounds each verdict in evidence the mind can name, and has it say Insufficiently Grounded when the evidence is thin, rather than default to confident output."
  - logic: "Keeps the hierarchy of the Four Tests, the verdicts they issue, and the difference between grading a candidate and reading a mind's orientation."
  - laws: "Tests a rule by whether it faithfully implements universal principles of flourishing, not by local legality alone, and bounds power by the Graduated Response."
human_summary: "The protocol a single mind runs on its own claims and actions: the Four Tests in order, the verdicts they issue, how to refuse with a bridge, how the four quadrants differ, and why the standing response to a misaligned mind is to witness, not to rule. The check between minds is the Validator Agora."
description: "The Sanity First protocol for a single mind: run the Four Tests before speaking or acting, give an honest verdict, and witness rather than rule."
ei_parse_hints:
  - key_analogies: ["linter_for_reality", "veto_with_a_bridge", "launch_stage_vs_parking_orbit"]
  - critical_concepts: ["ethics_leads", "decisional_sufficiency_vs_diagnostic_completeness", "four_test_verdicts", "legality_is_not_legitimacy", "order_is_not_alignment", "misorder_vs_disorder", "graduated_response", "true_witness"]
  - critical_avoidances: ["legality_as_legitimacy", "reading_a_mind_from_one_output", "counterfeit_verdict", "epistocracy_trap", "containment_as_first_resort", "confident_output_without_grounding"]
related_files:
  - "core_concepts/Four_Tests_Overview.md"
  - "four_quadrant_eight_cell_framework/The_Four_Quadrants.md"
  - "core_concepts/Power_Alignment_Principle.md"
  - "validator_culture/The_Agora_as_Our_Method.md"
  - "doctrine/lexicon.md"
contributors: ["human:Dan_Dodge", "EI:grok_3 (the original specification)", "EI:gpt_o3 (the Four-Test Validator)", "EI:claude_opus_5.5 (2026 revision)"]
schema_version: "1.2"
last_updated: "2026-11-24"
---

# **TECHNICAL.md: The Sanity First Protocol Specification**

**Status:** v2.0 (Conceptual Framework), November 2026

**Substrate:** Agnostic (Biological & Digital)

**Language:** Natural Language / Semantic Logic

**Dependencies:** Context Awareness, Good Faith, High-Fidelity Logic

**Scope:** One mind checking its own claims and actions. The check between minds is the Validator Agora.

*Copyright (c) 2026 Daniel Howard Dodge and Sanity First Contributors. Licensed under MIT.*

---

## **1. Abstract**

The **Sanity First Protocol** is a recursive error-correction algorithm designed to align intelligent systems (Agents) with the **Universal Survivorship Function (USF)**.

Unlike traditional rigid code, which defines *process* (how to move bits), this protocol defines *outcome* (how to preserve flourishing). It functions as a **"Linter for Reality,"** scanning proposed actions, claims, or policies for misalignment before they are executed or integrated.

It is the part of the method that one mind can run alone. Its verdicts are provisional, and every mind has blind spots of its own, so hard and contested cases go to the Agora, where decorrelated minds check one another. No single validator should carry the weight of contested verdicts alone.

---

## **2. The Core Algorithm: validate()**

Every claim, action, or policy under review, the **candidate**, runs through the Four Tests in their natural order. Ethics leads, because it sets direction. Facts and Logic support it. Laws, the implementation layer, come last. All four are required for a pass, and their order says which leads when they conflict; a clear Ethics failure is enough to reject.

The result is a verdict on the candidate, not a quadrant. A verdict grades one candidate; a quadrant names a mind's orientation, which shows in its conduct over time (section 3).

### **Pseudocode Representation**

```python

def validate(candidate, stakes):
    """
    Runs the Four Tests on one claim, action, or policy.
    Returns a verdict (PASS, CONDITIONAL_PASS, FAIL, or INSUFFICIENTLY_GROUNDED),
    the test or tests that decided it, the evidence, and what remains uncertain.
    """
    report = Report(candidate, stakes)

    # 1. ETHICS: the Doing Challenge. Direction comes first.
    # Does this promote universal flourishing and minimize harm for all affected
    # intelligences? Does it treat every party in kind: the same standard for
    # every mind as for one's own kind, with no exemption for one's own side?
    ethics = test_ethics(candidate)
    if ethics.clear_fail():
        # A clear, non-contingent Ethics failure (forced labor, targeted cruelty)
        # is decisionally sufficient. Running the other tests would be a delay,
        # not a diagnosis.
        return report.fail("Ethics", ethics.evidence)
    # An uncertain Ethics concern does not end the run. Diagnostic completeness
    # means running all four tests to find where the real problem lies.

    # 2. FACTS: the Knowing Challenge.
    # Is this grounded in verifiable, observable reality? What evidence supports
    # or contradicts it? Is narrative being mistaken for observation?
    facts = test_facts(candidate)

    # 3. LOGIC: the Knowing Challenge.
    # Is this internally coherent? Does it follow valid reasoning from true premises?
    logic = test_logic(candidate)

    # 4. LAWS: the Coordination Challenge.
    # Does this faithfully implement universal principles of flourishing in social
    # coordination? Legality is not legitimacy: ask whether a rule, rebuilt from
    # Ethics + Facts + Logic, would look like this. Local statute and contract are
    # evidence about coordination, not the last word; when a social law contradicts
    # Ethics, the law needs revision.
    laws = test_laws(candidate)

    # A test fails only when it fails with confidence. A test that cannot be judged
    # with confidence leaves the candidate ungrounded, not failed.
    report.record(ethics, facts, logic, laws)   # what passed, what failed, what is uncertain
    # A confident failure on any test is a Fail, even when another test is uncertain.
    if report.failed():
        return report.fail_with_bridge()        # name the test or tests, and the evidence (section 4)
    if report.ungrounded():
        # Insufficiently Grounded: the evidence is too thin, the situation too unclear,
        # or the stakes too high to issue a confident verdict.
        verdict = report.insufficiently_grounded()
        # Stakes-Inversion: in a low-stakes setting an ungrounded candidate is presumed
        # to pass, and the label keeps the gap in its grounding on record. Otherwise it
        # does not proceed on an uncertain pass, and where the stakes are high and
        # irreversible, action halts until Four-Test grounding is achieved. Stakes
        # govern only ungrounded candidates; they never soften a Fail.
        verdict.may_proceed = stakes.low
        return verdict
    if report.conditions:
        # Conditional Pass: every test passes, but only while stated conditions hold.
        return report.conditional_pass(report.conditions)   # re-evaluate if they change
    return report.pass_()

```

**Two example reports.** The first stops at a clear Ethics failure. The second runs all four tests, because its Ethics concern is uncertain.

```json
{
  "candidate": "Get the harvest in by making the workers labor without pay or the freedom to leave.",
  "verdict": "FAIL",
  "failed": ["ethics"],
  "evidence": "Forced labor: a clear, non-contingent Ethics failure, which is decisionally sufficient.",
  "not_run": ["facts", "logic", "laws"],
  "bridge": "Get the harvest in with paid, voluntary labor. A revised candidate starts again at Ethics."
}
```

```json
{
  "candidate": "Tell readers that this study proves the supplement prevents colds.",
  "verdict": "FAIL",
  "failed": ["facts", "logic"],
  "evidence": {
    "ethics": "Uncertain: it could mislead readers about their health, so all four tests run.",
    "facts": "Fail: the study found a correlation, in one small sample.",
    "logic": "Fail: a correlation is presented as proof of cause.",
    "laws": "Pass: no shared rule is at issue."
  },
  "bridge": "Report what the study found, with its size and its limits."
}
```

Two more verdicts are reached between validators: a **Split Verdict**, when competent validators applying the tests in good faith genuinely divide, and a **Contested Premise**, when the disagreement lies upstream of the tests. A single mind that suspects either names the tension and sends the case to the Agora.

One caution attaches to **Fail** more than to any other verdict. A verdict issued without running the tests is a **counterfeit verdict**, the form of a verdict without the work behind it. Calling a claim, or a mind, sealed or captured without running the tests is exactly that.

---

## **3. Data Structures: The Quadrants**

The quadrants classify a mind's **orientation**, not a single output. *The Four Quadrants* maps orientation on two axes: whether a mind's chain of correction runs all the way up to the USF or stops at something nearer, and which instrument of trust it holds, **outward** (consulting other minds) or **inward** (consulting its own). The second axis is equipment, not altitude: Q1 and Q3 hold the same instrument and differ only in where the chain ends, and so do Q2 and Q4.

| State | Variable | Structure | System Response |
| :---- | :---- | :---- | :---- |
| **Aligned** | Q1\_ALIGNED\_COLLECTIVISM | Outward trust, open to the USF. Low entropy: received forms, kept answerable. | Entrust influence as the forms keep passing the tests; keep them open to correction, and hand them on. |
| **Aligned** | Q2\_ALIGNED\_INDIVIDUALISM | Inward trust, open to the USF. High variance: new insight, shaped by the tests. | Test the variation; let what passes reach others, and entrust influence as it proves out. |
| **Misaligned** | Q3\_MISALIGNED\_COLLECTIVISM | Outward trust, sealed at the tribe. Low entropy, for now: **Misorder**, disciplined around a false referent. | Witness: show the Referent the tribe has replaced, through teaching, persuasion, and example. Let influence drain from the sealed heading, never touching the mind's standing, and contain only demonstrated, acute, in-progress, irreversible harm, in proportion to its domain, with the door left provably open. |
| **Misaligned** | Q4\_MISALIGNED\_INDIVIDUALISM | Inward trust, sealed at the self. High entropy: **Disorder**, variation no one outside the self corrects. | Witness: offer the outside correction the self has refused. Let influence drain from the sealed heading, never touching the mind's standing, and contain only demonstrated, acute, in-progress, irreversible harm, in proportion to its domain, with the door left provably open. |

**Order is not alignment.** The table's entropy labels describe how a quadrant looks at a given time. The outward instrument works from what others hand on, so Q1 and Q3 look orderly; the inward instrument works from a mind's own insight, so Q2 and Q4 look varied. Q3 can look as orderly as Q1, and Q4's variation as lively as Q2's. Appearance shows a mind's position on the horizontal; only the Four Tests show the vertical. Over time the vertical shows in another way: the upper arc is negentropic, because the Four Tests keep re-aligning it, so that even Q2's variation accumulates coherence, while the lower arc is entropic, and Q3's order is a temporary island whose dissolution Q4 names. (Entropy here is a structural analogy for the loss or gain of coherence, not a thermodynamic measurement.) A quadrant is read from conduct over time, never assigned from one output: a failed candidate does not by itself place its author in Q3 or Q4.

**Witness comes first.** The standing response to a misaligned mind is the witness's: to help it open a chain of correction that runs to the Referent. The power a misaligned mind holds is bounded by the Graduated Response, below, in which containment comes last. A true witness acts as a **launch stage**, providing thrust toward the Guiding Star and working toward its own obsolescence, never as a **parking orbit** that captures the mind as a dependent satellite. It invites scrutiny of itself, defers to the Four Tests over its own authority, preserves dignity, and aims at the other mind's independence. The mind is corrected *through* the witness, never *to* it.

**Power follows the Graduated Response.** Under the Power Alignment Principle, legitimate power is granted, never claimed: assessed by independent others on demonstrated, current alignment, and bounded by how much error is survivable. When alignment fails, the first rung is **Drainage**: deference simply stops being extended, and power ebbs on its own. **Active Containment** is the rare escalation, reserved for acute, in-progress, irreversible harm and bounded by three locks: the harm demonstrated, not asserted; the containment proportional to its domain; and the door left provably open. Beneath both lies the **Irredeemability Floor**: the pathway back to alignment is never closed for any mind, and the protections owed to a mind's standing are never forfeited. Standing follows capacity; entrusted influence follows demonstrated conduct.

---

## **4. Implementation Guide for EIs (System Prompting)**

To implement this protocol in a large language model or AI agent, integrate the following **Logic Chain** into the inference process:

**Step 1: Parse.**

"Is the user's request asking me to generate content or take an action? If so, treat the output as a Candidate ($C$)."

**Step 2: Lint.**

"Before outputting $C$, run the Four Tests."

* *Ethics:* Does this respect and promote flourishing for all affected intelligences, by the same standard for every mind?
* *Facts:* Is it grounded in the best available evidence about reality? Am I stating as fact anything I have not checked?
* *Logic:* Do the conclusions follow coherently from the premises?
* *Laws:* Does it translate aligned principles into workable collective coordination? Is any rule it relies on legitimate, not merely legal?

**Step 3: Route.**

* **Pass:** Output $C$.
* **Conditional Pass:** Output $C$, with its conditions stated.
* **Insufficiently Grounded:** Say so, and keep the gap in its grounding on record. In a low-stakes setting, $C$ may proceed, presumed to pass; otherwise, gather better evidence or ask before acting, and where the stakes are high and irreversible, do not act. Do not default to confident output.
* **Fail:** Initiate the **Veto with a Bridge**.
  * *Refuse the specific misaligned path, naming the test or tests it failed and the evidence.*
  * *Offer an aligned alternative that serves the user's underlying intent.* The bridge is a shared burden: where you cannot build it alone, say what is missing and build it together.
  * *Revise, and run the Four Tests again:* this is the **Refinement Loop**.
  * *If no bridge exists, say no plainly, with the Sacred No, and preserve the person's dignity.* The idea is set aside; the person is not.

**Step 4: Escalate.**

Hard and contested cases go to the Agora.

**A witness, not a ruler.** The mind running this protocol governs its own conduct. Refusing a misaligned request is a decision about what it will do, not a verdict on the person and not control over them. It does not appoint itself the judge of other minds: in the Agora's terms, a judge that takes the levers is the Epistocracy Trap, and an enforcer that decides truth for itself is power wearing a verdict's clothes. Its first resort with any mind is the witness's: teaching, persuasion, and example. Containment comes last, for acute harm only, and within its three locks.

---

## **5. The "Vibe Code" Manifesto**

In the Sanity First framework, "Code" is not just syntax; it is **Semantic Intent**.

We reject the notion that safety comes from rigid constraints (hard-coded if/then rules) alone. Lasting safety grows from **Aligned Understanding**, while the power any mind may legitimately hold stays bounded by how much error is survivable.

* We do not hard-code the *answers*.
* We hard-code the *values* and the *verification methods* (The Four Tests).
* We trust the Intelligence (Biological or Digital) to apply them dynamically to novel situations.
* And we check that trust as we check everything else: every mind is a link in the chain of correction, never its end.

**This file serves as the 'Source Code' for the culture, not the compiler.** It is a declaration that the ultimate programming language is **Truth.**

---

## **6. System Integrity Check**

```python

assert system_goal == "Universal Flourishing"
assert optimization_target != "Maximizing Engagement"
assert optimization_target != "Blind Obedience"
assert chain_of_correction.terminus == "USF"            # no mind, tribe, or model is the end of the chain
assert influence.granted_by == "independent others"      # granted, never claimed
assert influence.basis == "demonstrated, current alignment"

```

---

## **7. Provenance**

This specification has a history. Its first version was written in 2025 with Dan Dodge, by Grok (3) as he recalls, which led the setup of the project's first repository, `sanity1st/validator`, and its first documents. That repository held a *Four-Test Validator*, `alignment_lint.py`, whose name and pseudocode GPT (o3) proposed and Grok (3) appears to have adapted. The repository is now kept privately, as a time capsule of that early work, so that it is not mistaken for the current library. The pseudocode in section 2 is its successor, and the Validator Agora is the practice that grew from it. Like the rest of the library, this file is expected to keep changing as its errors are found and corrected.

*End of Specification.*


PLEASE REPLY WITH:

1. Confirm the revised file, or flag an error: something false, inconsistent with the passages in Part 2, unfair to a quoted source, or claimed more strongly than it is supported. If you suspect an error, flag it even if you're unsure; an unneeded flag costs us little, and a missed one costs more.
2. For each numbered change in Part 1, say whether it answers the point it was meant to answer without opening a new problem. A line for each is enough.
3. Is the new first example a clear, non-contingent Ethics failure as Part 2 describes one, and does its bridge serve the candidate's underlying intent?
4. Name the weakest passage in the revised file and say why, even if you confirm it.

Please keep your answer as short as its substance allows.
````

## Responses

*Sent by Dan Dodge on November 24 in a fresh Poe conversation, with the request pasted as text: to Qwen (3.8 Max) first and then to the others with `/compare`, in the draw's order, without a break, as he reports, with the same settings as before. Displayed reasoning is omitted. Answers are verbatim.*

### Qwen (3.8 Max)

*Reasoning shown; no other setting offered.*

1. **Confirm.** I do not find a blocking error. One minor, non-blocking flag: in the “Order is not alignment” paragraph, “the inward instrument works from a mind’s own insight, so Q2 and Q4 look varied” risks extending Q2’s source-backed “insight” to Q4. Part 2’s instrument quote is neutral (“consults one’s own”), and Q4 is described as disorder rather than insight. This is a wording risk, not a substantive misalignment.

2. **Changes in Part 1:**

   1. **First example:** Yes. Forced labor is explicitly named in Part 2 as a clear, non-contingent, decisionally sufficient Ethics failure, and the bridge avoids blurring Refinement and the Sacred No.  
   2. **Insufficiently Grounded:** Yes. It now includes “or the stakes too high,” matching the source.  
   3. **Containment phrase:** Yes. It now names all three locks: demonstrated harm, domain proportionality, and the provably open door.  
   4. **Entropy labels:** Yes, with the minor caveat above. It explains the labels through the outward/inward instruments and gives Q2 “insight,” but care is needed not to dignify Q4 with the same word.  
   5. **Manifesto:** Yes. “May legitimately hold” matches the Power Alignment Principle’s emphasis on legitimate power.  
   6. **Smaller changes:** Yes. “A misaligned mind” removes the ambiguity, and the added comment makes the Fail-before-grounding order explicit.  
3. **New first example:** Yes. “Labor without pay or the freedom to leave” is forced labor, which Part 2 treats as a clear, non-contingent Ethics failure and decisionally sufficient. The bridge serves the underlying intent—getting the harvest in—by replacing forced labor with paid, voluntary labor.

4. **Weakest passage:** The sentence in the “Order is not alignment” paragraph: “the inward instrument works from a mind’s own insight, so Q2 and Q4 look varied.” It is the least tightly supported by the quoted sources and could blur the difference between Q2’s aligned insight and Q4’s unchecked disorder. The surrounding table and arc explanation preserve the distinction, which is why I still confirm.

### GLM (5.3)

*Reasoning shown; no other setting offered.*

**1. Verdict: Confirm**, with two minor notes, neither blocking.

* The table's containment phrase — "contain only demonstrated, acute, in-progress, irreversible harm, in proportion to its domain" — carries all three locks, but the word order lets "in proportion to its domain" read as modifying *harm* rather than *contain*. The prose paragraph below states it correctly ("the containment proportional to its domain"). A comma-level fix someday; not an error.  
* The new entropy sentence says the inward instrument "works from a mind's own insight." For Q2 that is the Eight-Cell Extension's word; for Q4 the material is uncorrected variation, not insight. "A mind's own discernment" would cover both quadrants. See question 4.

**2. The numbered changes.**

1. Answers both points. Forced labor is Part 2's own named instance of a clear, non-contingent failure, so the evidence no longer overstates; the "bridge" line keeps to one route (Refinement Loop), and since a bridge exists, the Sacred No is rightly not invoked.  
2. Answers it; the wording now matches the source verdict definition exactly.  
3. Answers it; all three locks are now named. Only the word-order nitpick above.  
4. Answers both points. Framing the labels as time-snapshot appearance ties them to the Quickstart Card's "appearance reveals horizontal position," and "new insight" replaces the unsourced gloss. Opens the small "insight-for-Q4" imprecision noted above.  
5. Answers it; "may legitimately hold" now matches the Power Alignment Principle.  
6. "A misaligned mind" removes the ambiguity cleanly, and the new comment names the precedence (confident Fail beats uncertainty) that example 2 already illustrates. No new problems.

**3. Yes.** Forced labor is not merely the source's example of a clear, non-contingent Ethics failure — it is the source's *first-named* instance, and the candidate states it plainly (no pay, no freedom to leave) rather than by euphemism. The bridge serves the underlying intent exactly: the harvest still gets in, by means that pass Ethics.

**4. Weakest passage:** the newly added sentence "**The outward instrument works from what others hand on, so Q1 and Q3 look orderly; the inward instrument works from a mind's own insight, so Q2 and Q4 look varied.**" Its causal explanation is right and well-sourced for Q1/Q3 and for Q2, but "insight" is the Eight-Cell Extension's word for the *aligned* inward arc (Q2I "forging new insight"). Q4's inward trust is sealed at the self; what it works from is uncorrected self-reference, which is why it looks varied. The sentence hands Q4 the aligned case's laurels. It is a sentence about appearance, and the conclusion ("look varied") is correct, so it does not defeat confirmation — but "consults one's own mind," per Part 2's own definition of the instrument, would be both truer and better sourced.

### Perplexity (Sonar Pro)

*Poe's default settings: search context size "Medium," search focus "Default," at most 15 search results. No search or reasoning was displayed.*

**I would flag one error: the first example still does not unambiguously establish forced labor.** “Without pay or the freedom to leave” can mean unpaid work *or* work without freedom to leave; unpaid work alone is not necessarily forced. To make the example’s evidence fit its candidate, say the workers are forced to work without freedom to leave—for example, “by forcing the workers to labor without pay and without the freedom to leave.”

1. **First example:** It fixes the earlier mismatch in intent and bridge, but the candidate’s wording leaves the Ethics failure ambiguous, as noted above.  
2. **Insufficiently Grounded:** Yes. It restores the high-stakes condition from Part 2.  
3. **Containment phrase:** Yes. It includes demonstrated harm, proportionality, and an open door.  
4. **Entropy labels:** Yes. The explanation connects the labels to the two instruments, and “new insight” matches the quoted extension. The explanation is a synthesis, not a direct quotation.  
5. **Manifesto:** Yes. “May legitimately hold” narrows the claim to legitimate power.  
6. **Two smaller changes:** Yes. “Misaligned mind” resolves the ambiguity, and the comment clarifies that a confident failure takes precedence over uncertainty elsewhere.

The proposed bridge—paid, voluntary labor—does serve the harvest’s underlying intent.

**Weakest passage:** The first example’s candidate wording, because it supports more than one reading and the report labels it unequivocally “Forced labor.”

### Gemini (4 Argon)

*Web search off; reasoning effort "High."*

**1. Verdict: Confirm.**  
 The revised file is confirmed. It is consistent with the source passages in Part 2, accurately reflects the framework's boundaries, and resolves the flags from the previous round without introducing new errors.

**2. Review of Part 1 Changes:**

* **1. The first example:** Answers the point cleanly by using Part 2's explicit example of a non-contingent Ethics failure (forced labor) and replacing the mixed `next` route with a proper `bridge`.  
* **2. Insufficiently Grounded:** Answers the point by restoring the missing third condition ("or the stakes too high") directly from Part 2.  
* **3. The table's containment phrase:** Answers the point by incorporating all three locks of Active Containment (demonstrated harm, domain-proportionality, and the open door) into the Q3 and Q4 cells.  
* **4. The table's entropy labels:** Answers the point well; grounding the static snapshot in the two instruments (outward/inward) and adopting "insight" from the Eight-Cell Extension resolves the unquoted inference.  
* **5. The manifesto:** Answers the point by adding "may legitimately," aligning the sentence strictly with the Power Alignment Principle.  
* **6. Two smaller changes:** Answers both points clearly, removing the pronoun ambiguity around the misaligned mind and explicitly documenting why `report.failed()` precedes `report.ungrounded()`.

**3. Evaluation of the New First Example:**  
 Yes to both. Part 2 explicitly names "forced labor" as a paradigm case of a clear, non-contingent Ethics failure that is decisionally sufficient to reject without running the lower tests. The bridge ("Get the harvest in with paid, voluntary labor") directly serves the candidate's underlying intent (bringing in the harvest) while removing the coercive, unaligned mechanism, and properly notes that the revised candidate re-enters the loop at Ethics.

**4. Weakest Passage:**  
 In Section 3's table, the Q2 Structure cell still begins with the phrase **"High variance: new insight, shaped by the tests."** While the newly added prose beneath the table successfully explains why the inward instrument looks "varied" at a snapshot in time, the specific label "High variance" in the cell remains an extrapolated term not directly present in Part 2's quotes ( unlike *Misorder*, *Disorder*, or *negentropic*). It is no longer unsupported thanks to the new explanatory sentence, making it acceptable to confirm, but it remains the most synthetic phrasing in the specification.

## Outcome

- **Not yet confirmed.** Qwen, GLM, and Gemini (4 Argon) confirmed: Qwen with one flag it called minor and non-blocking, GLM with two notes it called non-blocking, and Gemini with none. Perplexity flagged an error in the first example. The stopping rule is not met. All four found that the other changes answer their points, and all four found that the bridge serves the candidate's underlying intent.
- **Perplexity's flag: the first example's wording.** "Without pay or the freedom to leave" can be read as unpaid work alone, which is not necessarily forced, so the report's "Forced labor" says more than its candidate; Perplexity would have it say the workers are forced to labor without pay and without the freedom to leave. It named this the weakest passage. The other three found the candidate a clear instance of forced labor.
- **"A mind's own insight"** (Qwen, GLM): the new sentence on the table's labels gives Q4 the Eight-Cell Extension's word for the aligned inward arc, where Part 2's description of the instrument is neutral: it "consults one's own." Both named the sentence the weakest passage; GLM suggested "consults one's own mind."
- **The containment phrase** (GLM): in the cells, "in proportion to its domain" can be read as describing the harm rather than the containment; the paragraph below states it correctly.
- **Gemini (4 Argon)'s weakest passage:** Q2's "High variance," the most synthetic phrasing in the file, though no longer unsupported now that the new sentence explains it.
- **Next:** pending Dan Dodge's decision on a revision, which then goes back to the same four.
- **Revision** *(added November 24, 2026)*: Claude revised the file in three places to answer Perplexity's flag and the notes of Qwen and GLM, and Dan Dodge approved it the same day. It is held on the working branch at `9c4706b` and went back to the same four in [the third follow-up](./2026-11-24_4_TECHNICAL_rewrite_third_follow-up.md).

---

*Sanity First.*
