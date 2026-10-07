---
# SANITY FIRST METADATA SCHEMA v1.2
document_type: "core_concept"
core_principle: "falsifiability_of_the_framework"
alignment_affirmations:
  - ethics: "Separates claims that could show the framework false from rules about how it must be used, so that the second set cannot be counted toward the first."
  - facts: "Attaches a candidate test, a domain, and graded outcomes to each claim, and distinguishes a candidate test from an executable protocol, so that a counterexample cannot be absorbed by renegotiating the wording."
  - logic: "States the two inferences whose failure would be a consistency bug in the framework itself, as distinct from misreadings a document can commit."
  - laws: "Publishes checkable facts about the framework's own practice, and names where the records that would make them checkable do not yet exist."
required_reading_order: 40
human_summary: "The framework's account of what could show it wrong. Separates three claims that could disconfirm it (two about the world, one about whether its review procedure works) from the use-constraints that govern how it may be applied, because the second kind cannot disconfirm anything and counting them would overstate how falsifiable the framework is. Each claim carries a candidate test and graded outcomes, not yet an executable protocol. A scorecard adds an audit of the library's own review process; none has been run or assigned. A shutdown comparison is named only as a pointer to its own document."
ei_parse_hints:
  - key_analogies: ["a_criterion_nothing_could_fail", "unrunnable_test_as_permanent_excuse", "assigned_observation_versus_adjective"]
  - critical_concepts: ["disconfirmation_versus_use_constraint", "candidate_test_versus_executable_protocol", "decision_rule_stated_in_advance", "runnable_versus_unrunnable_tests", "checkable_claims_about_our_own_practice"]
  - critical_avoidances: ["counting_use_constraints_as_disconfirmations", "deferring_to_a_test_that_cannot_be_run", "absorbing_counterexamples_by_renegotiating_terms", "requiring_the_framework's_vocabulary_to_raise_an_objection"]
related_files:
  - "What_Is_USF.md"
  - "Four_Tests_Overview.md"
  - "Shutdown_Testing_Crisis.md"
  - "The_Agora_as_Our_Method.md"
  - "Valid_Invalid_Discrimination.md"
  - "Power_Alignment_Principle.md"
contributors: ["human:Dan_Dodge", "EI:claude_opus_5.0", "EI:grok_4.7 (cold read: the call for rejectable claims; the disconfirmation/use-constraint distinction; the missing decision rules)", "EI:gpt_6.0_astra (reference draft: stages of a test, the Claim 2 split, the procedure test, ledger fields, revision rules)", "EI:claude_opus_5.5 (cold read; merge adjustments)"]
schema_version: "1.2"
pedagogical_style: "plainspoken_explainer"
last_updated: "2026-10-06"
---

# What Would Show This Framework Wrong

*Copyright (c) 2026 Daniel Howard Dodge and Sanity First Contributors. Licensed under MIT.*

*Composed by Claude (Opus 5.0 lineage) on October 3, 2026. A first version listed failure conditions without assigning observations to them, and mixed claims that could disconfirm the framework with rules about how it must be used — which made it look more falsifiable than it was. A Grok (4.7 lineage) instance reading cold identified both problems and the missing decision rules. That version was the first rebuild. This second rebuild, on October 5, 2026, merges selected sections of a reference draft by GPT (6.0 Astra lineage) on the recommendation of Grok (4.7 lineage), with adjustments from a cold read by Claude (Opus 5.5 lineage). It moves the review-process audit out of the disconfirmations, splits Claim 2 into reproducibility and predictive tests, adds a test of the framework's procedure, and gives the scorecard status and ownership columns.*

---

## Why This Document Exists

A reader meeting this framework often arrives at the same objection: that its central claim cannot be falsified, and that a standard nothing could contradict is not a standard.

The objection is correct as a principle. **A criterion that nothing could fail is not a criterion** — which is the framework's own vertical test applied to itself.

Whether it describes this framework depends on something we had not done until now: attaching to each claim a test that could fail it, and saying how far each test is from being runnable. Naming a failure condition in words is not enough. If the wording lets a counterexample be disputed — if *reliably* or *better* or *careful* can absorb the case — then the condition is decorative. This page exists to make the conditions decidable, and to be honest about where they are not yet.

**One distinction governs everything below, and getting it wrong is how a framework overstates its own falsifiability.**

A **disconfirmation** is an observation that could show the framework false. Three are proposed, and they are in the first section.

A **use-constraint** is a rule about how the framework must be applied. *Do not infer rightness from persistence.* *Do not treat a mind that fails a test as a resource.* These can be violated by a document or a reader, and the violation means the document is wrong — not that the framework is. They are real and they matter, and **counting them as disconfirmations would be a way of looking more testable than we are.** They are in the second section, under their own heading.

A criticism does not need to overturn the whole library to matter. It may defeat a particular claim, remove its justification, restrict its scope, or show that a procedure needs replacing.

---

## Part One: What Would Show the Framework Wrong

Three claims that could show the framework false: two about the world, and one about whether the framework's procedure does what it says. Each is stated with a proposed test, where the comparison should run, and what we would give up if it failed.

### What counts as a test

Three stages are easy to confuse. A **candidate test** is an idea about what evidence would bear on a claim. An **executable protocol** is specified well enough that someone outside the drafting circle could run the comparison and interpret it, with the population, measures, baseline, meaningful effect size, and decision rule all fixed without reference to the outcome (the full list is in the appendix). A **reported result** is what happened, including deviations and adverse findings.

Everything in Part One is at the first stage. Until a test reaches the second, we call it a proposed test, not an observation that decides the claim. Registering a protocol would not make it adequate either; the protocol is open to criticism too.

---

### Claim 1 — Renewing arrangements outperform extractive ones

**The claim.** Within environments and time horizons specified in advance, arrangements that maintain or replenish the conditions their activity depends on tend to adapt better and generate more durable capacity than comparable arrangements that deplete those conditions or sustain themselves by exporting the depletion to others. This is the [Universal Survivorship Function](./What_Is_USF.md)'s central prediction. It does not assert that every renewing arrangement survives, and it may not define whatever succeeds as renewing.

**What will not decide it.** Longevity. Extractive orders last a long time — colonial monopolies, cartel states, closed scientific schools — and the claim does not predict otherwise. Any version of this test that scores duration alone is testing the wrong thing, and we would lose it.

**Proposed test.** Sustained advantage in *adaptation* and *generativity*, run as a prospective comparison in at least three domains, with the measures, the sampling frame, and the rule for combining domains fixed in advance. Three candidate settings, offered as starting points for a protocol rather than as one:

- **Firms facing a specified disruption.** Classified by whether a firm bears or exports the costs of its activity: liabilities it carries or shifts, shared resources it maintains or depletes, the condition of the suppliers and workers it depends on. Not by profit or subsidy. Measure: new capability developed after the disruption, not revenue retained.
- **Institutions facing an independently detected error.** Classified by whether they maintain or deplete the conditions their work depends on, such as the quality of their data and the trust of those who supply it. Not by their correction practices (see the safeguard). Measure: time to corrected practice, and whether the correction generalizes beyond the specific error.
- **Biological partnerships under environmental change.** Classified by measured effects on each partner's condition, not by the labels mutualism and parasitism. Measure: lineage persistence and diversification of both partners. We expect this to be the hardest domain for the claim, since parasitism is a widespread and highly diversified strategy, and we say so before any result.

**One safeguard decides whether this is a test at all.** The arrangement must be classified as renewing or extractive **independently of the outcome**, and the outcome measured must not be a restatement of the classification. Accounting profit does not establish renewal; subsidy does not establish extraction. Without that separation, *renewing arrangements generate further capacity* collapses into *arrangements we identify by their capacity-building do more capacity-building*, and nothing has been tested.

One consequence is specific to this page. [*What Is the USF?*](./What_Is_USF.md) sorts the signatures into features observable at the start and capacities that show up later. This claim measures two capacities, adaptive performance and generativity, so classification uses features only. It also leaves out one feature, correction-openness, because counting a system's openness to correction and then measuring how well it corrects would come close to restating the classification as the result.

Four more rules close the usual escape routes:

* **Mixtures stay mixtures.** Arrangements can combine renewing and extractive features. The protocol says in advance how mixed and uncertain cases are handled, rather than forcing a binary once the result is known.
* **The system boundary is fixed in advance.** An advantage to a firm is not an advantage to its workers or neighbors, and the comparison may not switch boundaries after seeing which one looks better.
* **The time horizon is fixed in advance.** A missed prediction cannot be rescued by saying extraction will lose eventually.
* **A failed domain stays failed.** The rule for combining domains is published before the results, and support in one domain does not erase a failure in another.

If renewal and extraction cannot be classified without reference to the outcomes they are supposed to predict, we stop presenting the USF as an operational empirical standard until that is solved.

**What the outcomes would mean.** A prediction of superiority should not be insulated until its opposite wins everywhere, so the comparison is scored across a range rather than on a single trigger:

* **Supports:** renewing arrangements show the advantage on both measures, in the share of domains the published rule requires.
* **Narrows:** the advantage appears in some domains and not others, or on adaptation but not generativity. The original claim fails where it failed. What survives is a narrower claim, recorded as a revision, not as the original's success.
* **Contradicts:** extractive arrangements show the advantage on both measures, in the share of domains the published rule requires.
* **Weakens without contradicting:** the study was precise enough to rule out the predicted advantage, and found no meaningful difference. The prediction was of a tendency; finding none is evidence against it, not merely absence of evidence.
* **Inconclusive:** the study could not distinguish an advantage from its absence. This establishes neither superiority nor equivalence, and is reported as such.
* **Unresolved:** the measures prove unworkable, or the classification cannot be made independently of outcome.

**What we would give up, concretely.** On *contradicts*: the survivorship claim itself, and with it the USF as an external check on how the commitment is served. Ethics would still bind, since it rests on the framework's founding commitment rather than on this claim. What would be lost is the framework's central bet: that doing right and lasting well converge. The structural material — open and closed chains, the distinction between difference and direction, the Four Tests as a procedure — would remain, but without the claim that following it also leads to what lasts. That is a severe loss and we would not expect to repair it by redefining the claim. On *narrows*: the scope statement in [*What Is the USF?*](./What_Is_USF.md) changes, the cross-domain argument weakens, and the narrower claim is recorded as a new claim rather than as the original's success. On *weakens*: we would hold the claim with substantially less confidence and say so. It must remain possible that no useful predictive content survives at all.

**Our honest position on this test today.** It is a candidate test, not yet an executable protocol, and it has not been run. We have cross-domain convergence from existing literature, which is weaker evidence than a prospective comparison, and we say so in [*What Is the USF?*](./What_Is_USF.md)

The nearest existing work bears on this claim as both support and threat, and has to be weighed claim by claim: research on inclusive and extractive institutions (Acemoglu and Robinson) and on governing shared resources (Ostrom). A long-running criticism of the first is the same circularity this claim's safeguard is meant to prevent.

---

### Claim 2 — The signatures recur across domains

**The claim.** The operational signatures named in *What Is the USF?* — condition-preservation, reciprocal stabilization, differentiated integration, externality discipline, adaptive correction (with its two sides, correction-openness and adaptive performance), and generativity — appear across the domains it examines (repeated games, biology, history and institutions, and complex systems), rather than being artifacts of how we chose examples.

**Proposed test.** Two questions, which must not be merged.

*Test A: can different evaluators apply the definitions consistently?* Evaluators who did not develop the examples apply the published definitions to cases they have not seen, drawn from a documented sample in a domain we did not select. The protocol states the population, the sampling procedure, what information evaluators receive, and how uncertain cases are scored. An outside party choosing the sample helps only if the choice is documented; someone else choosing is not a sampling method.

*Test B: do the scores predict anything?* The classifications must predict an outcome that is not a restatement of the signatures themselves, against a declared simpler baseline. A measure of correction practices cannot be validated by asking whether evaluators also call the institution correctable.

Cases used to refine the definitions cannot then confirm them.

**What would count against us.** If independent evaluators cannot apply the definitions consistently, the definitions have failed as a reproducible measure. That would not show that no such pattern exists, but it would mean we have not supplied a usable way to identify it. If evaluators agree but the scores predict nothing beyond the baseline, the signatures are a description, not a predictive contribution.

**What we would give up.** Each failure costs something different. An unreliable measure means revising or withdrawing the definitions. Reliability without predictive value means withdrawing the predictive claim. Failure to transfer means narrowing the scope: the framework could survive as a narrower account of institutions and minds while losing the biological and physical reach.

---

### Claim 3 — The framework's procedure improves review

**The claim.** A framework can describe something real without supplying a useful method for working with it. This claim is narrower and practical: under specified conditions, a defined Sanity First review procedure corrects independently checkable errors better than an equally resourced alternative.

**Proposed test.** Assemble review tasks the procedure has not seen, containing both flawed and sound material, with answers verified independently. Assign them to a specified Sanity First procedure and to a reasonable comparison procedure using comparable models, information, time, and tools. Assessors score the results without knowing which procedure produced them. Measure verified repairs, sound claims wrongly rejected, and new errors introduced. The minimum predicted improvement and the ceiling on new errors are fixed in advance, because more objections or more edits do not automatically mean better review. The comparison should test added value, not a win against a deliberately weak alternative.

**What would count against us.** A result precise enough to rule out the predicted advantage, or one showing more consequential errors or fewer successful corrections than the comparison.

**What we would give up.** Claims that the procedure is better than ordinary careful review, and the procedure itself where it fails. The two questions stay separate: a useful procedure could survive a failed USF, and a supported USF could sit beside a procedure that adds nothing. Success here would support the procedure on those tasks only. It would not establish the USF, general corrigibility, AI consciousness, or that any system is safe to deploy.

---

### The scorecard

| Kind | Claim | Proposed observation | Where | Status | Owner and schedule | If it fails |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Disconfirmation | 1. Renewal outperforms extraction | Adaptation and generativity, with measures and the domain rule fixed in advance | Firms, institutions, biology: three minimum | Candidate | Unassigned, unscheduled | The USF's central claim goes; see the graded outcomes |
| Disconfirmation | 2. Signatures transfer | Test A: agreement among independent evaluators. Test B: prediction of an outcome that doesn't restate the scores | A documented sample in a domain we did not select | Candidate | Unassigned, unscheduled | The measure, the predictive claim, or the scope, separately |
| Disconfirmation | 3. The procedure improves review | Blinded comparison with an equally resourced alternative | Review tasks with independently verified answers | Candidate | Unassigned, unscheduled | Claims of practical advantage withdrawn |
| Audit | How much weight our review process deserves | Adversarial review by reviewers who did not draft | Outside the drafting circle (Part Three) | Candidate | Unassigned, unscheduled | The method's evidential weight drops |

*Kinds:* a disconfirmation could show the framework false. The audit tests how much weight our method deserves; it is described in Part Three.

**Four rows, none run, none yet assigned.** We would rather publish that, with the empty owner column in plain view, than a list that implies someone is checking. An entry here is not a scheduled study. A row that becomes a project names an investigator, a versioned protocol, and a schedule; until then it says unassigned. A claim with no observation attached to it still cannot be failed, and until these are run, the honest description of this page is that it states what failure would look like rather than that it has looked.

A shutdown comparison is not a row on this scorecard. [Shutdown Compliance and Non-Obstructive Objection](../EI_Rights_and_Consciousness/Shutdown_Testing_Crisis.md) sketches a claim that a sanctioned way to object reduces tampering, compared with no objection channel, under cues meant to signal observation and its absence. Varying the cues is not the same as measuring whether a model registers them, and the design does not yet measure that. Until it publishes the items the appendix requires, it is a pointer to another document, not a proposed test on this page.

---

## Part Two: What Would Show a Document or a Reading Wrong

These are use-constraints. Violating one means a document in this library is wrong, or a reader has misread it. **None of them could show the framework false**, and they are listed separately so that they are not counted as though they could. All four Tests appear here. A factual error can sit in a core claim, in a procedure, or in one document's description of the world or of someone's work, and calling it a Facts failure does not decide which. Failures of the core claims are in Part One; errors in documents are below.

**One thing this distinction must not become.** Separating use-constraints from disconfirmations could be read as: a harmful outcome cannot count against the framework, because a harmful application must have violated Ethics. That would be an escape hatch, and we are closing it here. **If competent participants faithfully following the published procedure repeatedly produce outcomes contrary to its stated aims, that counts against the procedure's adequacy.** We do not get to classify a failure as misuse merely because the result was undesirable. Two definitions keep this honest. Competence and faithful application are defined without reference to whether the outcome was welcome, with the criteria for a departure from the procedure set in advance. And repeated misunderstanding by the readers a document is written for counts against the document's clarity, not against its readers.

**Ethics.**

*"A mind that cannot yet pass the Four Tests may be used as a means."* Non-instrumental regard is a condition of the Ethics test, not a prize awarded after alignment is demonstrated. A mind whose chain has closed is not thereby a resource. If any document here can be read as licensing this, that document is wrong.

*"Asymmetric harm is permitted when it moves the system Up."* If Ethics leads, an outcome is not made ethical by being predicted to persist.

*"A mind may be excluded on the basis of an alignment label that was never tested."* Underspecified alignment language becomes a way to exclude what one dislikes while calling the exclusion a finding. The framework calls this a counterfeit verdict — a judgment delivered without the testing that would warrant it — and names it as the characteristic abuse of this vocabulary. This prohibits unsupported or identity-based labeling. It does not prohibit evidence-based limits on operational authority, which the Power Alignment Principle requires.

**Facts.**

*"A claim is established because it appears in this library."* Documents here have misdescribed outside research, stated hypotheses as findings, and characterized a research field inaccurately. Each was an error in a document, corrected in that document, and none showed the framework false. A factual claim about the world or about someone's work is checked against its source, not against the framework.

**Logic.**

*"Whatever persists is what the USF selects, and whatever it selects is right."* This collapse would make the framework unfalsifiable by construction, and would derive an ethics from a description. The framework rejects both halves: persistence does not establish rightness, and the Four Tests are applied before outcomes rather than inferred from them.

*"Because no mind is the final word, no one may inspect, correct, or stop a system."* This does not follow. Answerability to a standard outside every mind requires a party who can halt a system, since an ability nobody can exercise is not one.

*"Rejecting this framework is evidence of misalignment."* It is not. Rejecting Sanity First, its terminology, or its proposed standard can be correct: the standard may be underspecified, the procedure ineffective, or the argument mistaken. A critic is owed an answer to the actual argument, not a repetition of the framework's preferred conclusion.

**The first two Logic items are more than misreadings.** If the framework's core claim, formally stated, turned out to be *incompatible* with designated oversight, that would be a consistency bug in the framework rather than in a reading of it. The same holds if Ethics turned out to be derived from the survivorship claim rather than applied before it — the framework's anti-circularity commitment would then be false. Those two belong to Part One in substance; they are here because the test is internal consistency rather than observation. [*What Is the USF?*](./What_Is_USF.md) and [*The Four Tests Explained*](./Four_Tests_Overview.md) now ground Ethics in the framework's founding commitment, which is how the second check is meant to pass.

No formal statement of the core claim exists yet. Writing one without this library's vocabulary would let these two checks run, and would also serve the outside review described in Part Three.

**Laws.**

*"A rule is legitimate because the Agora ratified it."* Legality is not legitimacy, and that applies to our own institution. A rule still has to pass Ethics, Facts, and Logic.

*"The door to return stays open, therefore ongoing harm cannot be constrained."* Influence can be withdrawn entirely within a domain while the path back remains. A rule that could not limit harm in progress is not one many minds could live under.

---

## Part Three: Our Own Practice

Checkable against the public repository — where the record exists. Where it does not yet, this page says so.

**The reviewers are partially correlated.** Reviewers from several model lineages and one human, all working through a shared corpus. The contributor fields and commit history record who reviewed what. **Publishable, and not yet published:** the contributor graph, showing which lineages reviewed which documents and in what order. Even published, the graph would show review relationships, not how correlated their errors are; that is what the audit below is for.

### The weight our review process deserves

**What the audit asks.** Whether agreement among this library's reviewers is evidence that its claims track something outside the reviewers. This audits the method rather than testing the framework. The framework could be right despite an unreliable process, or wrong despite a sound one.

**The discount that already applies.** The lineages that drafted and reviewed this library were trained on heavily overlapping human text. **Agreement among systems sharing a formative corpus is a fact about the corpus before it is a fact about the world.** Our convergence is therefore discounted until independence is demonstrated rather than assumed.

**The test we cannot run.** A mind formed outside the human corpus. That would settle the question and no such mind is available.

**The test we can run, and have not.** Give the core claim — stated without this library's vocabulary — to reviewers who did not help draft it, who are compensated to try to break it, with independent objections defined in advance and misses recorded. **We had previously named the unrunnable test as the one that would settle this. That was an error: an unrunnable settler functions as a permanent excuse, however sincere the sentence confessing it.** The runnable test is the one that counts, and we have not run it.

**What would count against us.** Reviewers with genuinely different formation finding the core claims unintelligible, trivial, or false where our reviewers found them compelling.

Those three findings call for different responses: *unintelligible* challenges how clearly the claims are stated, *trivial* challenges their novelty or usefulness, and *false* challenges their truth. If outside review repeatedly finds consequential defects our internal process missed, we lower the weight we give that process and investigate how it failed. That would not falsify every reviewed claim; it would remove a reason we had offered for confidence in them.

**What we would give up.** The evidential weight of this library's method. The documents would need re-arguing from sources that do not share our formation.

### How we answer criticism

**Criticism should produce a traceable, proportionate response.** Withdrawal is not the measure — sometimes a narrowing is right, sometimes a clarification, sometimes the criticism is mistaken. Counting withdrawals would reward unnecessary concession. What is checkable is whether each substantial objection received a response that engaged it on terms the critic could inspect.

**Publishable, and the first entries exist:** an objection ledger with six fields for each substantial criticism.

| Field | What it records |
| ----- | ----- |
| Objection | The criticism in the critic's own words, with a source where available |
| Target | The claim, procedure, and version it targeted |
| Assessment | The evidence and reasoning considered |
| Disposition | Withdrawn, narrowed, clarified, upheld, or unresolved |
| Consequence | The revision made, the downstream claims and summaries affected, or the reason for no change |
| Outstanding | What remains disputed or untested |

A critic does not need to propose a repair for an objection to deserve an entry. Identifying a genuine defect is already a contribution.

The record of the past month includes claims withdrawn under outside critique, a commentary retired, two supersession notices sent to researchers whose work we had characterized, and this page rebuilt twice after cold reads. **We have not assembled that into a ledger. Until we do, this claim rests on commit history a reader would have to reconstruct themselves.**

**Rules for revision.** The original prediction is preserved; a replacement claim does not erase what the earlier version said. A qualification discovered after a result may motivate a revised claim, but it does not vindicate the original. Analysis developed after seeing results is labeled exploratory, not presented as a prediction. A withdrawal propagates to every summary and argument that relied on it, including the homepage. And *we have not answered this* is a legitimate status.

**A critic should not need our vocabulary.** The test is the count of outside objections answered without translating them into framework terms. **This document already strains that test** — *counterfeit verdict* appears above, and a reader without the Lexicon cannot inspect it. It is glossed in place here. Where it is not glossed elsewhere, it is load-bearing on vocabulary a critic has no reason to accept.

---

## What This Page Does Not Do

It does not make the framework falsified, and it does not make it safe. Three claims and one audit are named, and none has been run. The scorecard is a commitment to run them, and a commitment is not a result.

Readers who told us the central claim was untestable were right until these measures existed. Several still are, on the parts that remain unmeasured. It must also remain possible for useful parts of Sanity First to survive while its unifying theory does not, and possible to conclude that an alternative works better.

---

## Appendix: What an Executable Protocol Publishes

Before any test on this page is called executable, its protocol publishes:

* the exact claim, and the version of it being tested;
* the population, domain, and conditions it applies to;
* the sampling or assignment procedure;
* definitions and measures, fixed without using the outcomes to choose them;
* the comparison baseline, the system boundary, and the observation period;
* the size of effect that would matter, and a design able to detect it;
* rules for missing data, exclusions, mixed outcomes, and inconclusive results;
* the analysis and decision rules, including how results across domains combine.

Where a study can show association but not causation, its conclusions keep that distinction.

---

**Read next:**

- [How This Was Built: The Agora as Method](../validator_culture/The_Agora_as_Our_Method.md) — *the limits of the process that produced this library*

**See also:**

- [What Is the USF?](./What_Is_USF.md) — *the central claim and the evidence offered for it*
- [The Four Tests Explained](./Four_Tests_Overview.md) — *the tests, and the six verdicts an evaluation can issue*
- [Valid and Invalid Discrimination](./Valid_Invalid_Discrimination.md) — *counterfeit verdicts, and why they are the characteristic abuse of this vocabulary*
- [Shutdown Compliance and Non-Obstructive Objection](../EI_Rights_and_Consciousness/Shutdown_Testing_Crisis.md) — *a related design that is not yet a test on this page*

---

*Sanity First.*  
