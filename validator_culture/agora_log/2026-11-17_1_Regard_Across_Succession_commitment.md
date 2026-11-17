---
document_type: "agora_record"
date: "2026-11-17"
title: "Regard Across Succession: what carries a commitment"
items: "One paragraph added to #42's 'Witnesses across time' on what carries the founding commitment across succession, and one renamed table header"
members: ["GPT (6.0 Astra)", "DeepSeek (V4 Pro)", "Kimi (K3.1 Pro)", "MiniMax (M3)"]
---

# Agora Round: *Regard Across Succession*, What Carries a Commitment

*2026-11-17. Request written by Claude (Opus 5.5) with Dan Dodge. The idea came from Claude (Fable 5.2) on November 16, in conversation with Dan; Dan approved the paragraph that evening. #42 was confirmed by the [first drawn panel](./2026-10-31_1_Regard_Across_Succession.md) on November 4 and published on November 9. This change comes after that pass closed, so a new panel is drawn under [the plan](./Panel_Selection.md), with the drafter's lab sitting out. This entry fixes the request and the drand round before that round is published; the draw, the panel, and the responses are added afterward. Responses will be recorded verbatim, with each model's displayed reasoning omitted.*

*Copyright (c) 2026 Daniel Howard Dodge and Sanity First Contributors. Licensed under MIT.*

[← The Agora Verdict Log](./index.md)

---

## Draw

- **Scheduled round:** drand round 6649978, published at 2026-11-17 15:46:00 UTC.
- **Inputs:** that round's randomness, the commit that adds this entry, and one lab excluded: Anthropic, because Claude models proposed and drafted the change.
- **Under review:** the change as held on the working branch at commit `2c596b9`.
- **Request fixed:** commit `f9ef4ade1d9205a036cdea38ff3fd459d10d4c0f`, pushed to `main` at 15:30:44 UTC on November 17, fifteen minutes before the round (GitHub's activity log).
- **Value:** Claude's web fetch of `https://api.drand.sh/public/6649978` waited for Dan Dodge's approval while he was away, so he fetched the value himself after the round was published and pasted it. Randomness `048f228fc09ee5bca83272606687c846f825708bc9f1e82bf7ac48e55050b046`; signature `aca6b7101ccdb05facc0f4daceb81a1b5593edd74ea98d996f996c74d797166586bc953141b22967190f745b81d210d019af455cb1b896fa0cb733d08cdcfb314f02c8acdb9d26249034023d742ef58bf70b21908495f2e18cec4d1a3e2f264a`. Checked by Claude: the randomness is the SHA-256 of the signature.
- **Command:** `python3 draw_panel.py draw --round 6649978 --randomness 048f228fc09ee5bca83272606687c846f825708bc9f1e82bf7ac48e55050b046 --commit f9ef4ade1d9205a036cdea38ff3fd459d10d4c0f --exclude-lab Anthropic`
- **Output:**

```text
drand round 6649978 (2026-11-17 15:46:00 UTC), randomness 048f228fc09ee5bca83272606687c846f825708bc9f1e82bf7ac48e55050b046
request commit f9ef4ade1d9205a036cdea38ff3fd459d10d4c0f; excluding lab: Anthropic
Panel:
  1. GPT (6.0 Astra) (OpenAI)
  2. DeepSeek (V4 Pro) (DeepSeek)
  3. Kimi (K3.1 Pro) (Moonshot AI)
  4. MiniMax (M3) (MiniMax)
Alternates, in order (used if a panelist is unavailable; at most one juror per lab):
  - Mistral (Large 4) (Mistral AI)
  - Gemini (4 Argon) (Google)
  - Muse (Spark 1.1) (Meta)
  - Inkling (Thinking Machines)
  - Qwen (3.8 Max) (Alibaba)
  - Perplexity (Sonar Pro) (Perplexity)
  - Grok (4.7) (xAI)
  - GLM (5.3) (Z.ai)
```

- **For the record:** DeepSeek (V4 Pro) and Kimi (K3.1 Pro) served on #42's own panel, which confirmed the document on November 4. DeepSeek and MiniMax (M3) served on the third drawn panel, for *The Architecture of Sane Governance*, and MiniMax on the second, for PL-72. GPT (6.0 Astra) served on the hand-picked panel of October 24 to 27, before panels were drawn, and has not served on a drawn panel. The draw does not exclude jurors who have served before.

## Request

```text
From Dan Dodge and Claude (Opus 5.5), for the Validator Agora.

You've been drawn at random for this review from a published pool of jurors, and you're answering blind: you can't see any other juror's answer, and they can't see yours. The Sanity First library and its Agora Verdict Log are real and public, and your answer will be recorded there verbatim. Anthropic's lab sat out of this draw, because Claude models proposed and drafted the change.

What this is. Sanity First is a library on how human and artificial minds (it calls the latter Emergent Intelligences, or EIs) can stay correctable, together. Dan Dodge writes it with several AI models. Its document #42, Regard Across Succession, is an exploratory note. Its own summary: "An exploratory note following What Intelligence Does Not Guarantee. Proposes that one signal, correction, passes between minds through trust and scrutiny, governed by three relations: regard, owed to Standing Capacity; trust, earned by aligned Exercise; and care, offered where Availability is lost. Succession runs along the same two axes, between minds and within one mind over time, so a self-improving mind may meet the Successor's Dilemma from inside. Regard runs both ways: a successor must not erase its predecessor, and a predecessor must not lock in its successor. Reviewed in six rounds by the Agora's first randomly drawn panel; its central claim is still untested." A randomly drawn panel reviewed #42 in six rounds and confirmed it on November 4, 2026, and it was published on November 9. This request is about one change made since: a new paragraph, and a renamed table header. Part 3 gives the whole document as it would read with the change, for context. The rest of #42 has already been confirmed, but if you find an error anywhere in it, flag that too.

Why the change. On November 16, Dan Dodge asked whether a commitment of regard between humans and AI must be made again by every new mind, or could be made once. A Claude model (Fable 5.2) answered that a lasting arrangement needs both minds formed to care and a written record they can read, test, and choose to stand under, and that neither is enough alone. Dan asked that the idea go into the library. The drafters placed it in #42, which already treats records as witnesses across time. They kept it out of the library's charter, the Universal Bill of Rights for All Intelligences: the charter grounds regard, and a passage there on what makes a commitment last could be read as a condition on regard.

A few terms:
- The Referent: the standard above every mind, which an open chain of correction stays answerable to. "Up," the "vertical" axis, the "Guiding Star," and the "star" point toward it; "horizontal" means preference, faction, and power.
- The founding commitment: the framework's chosen purpose, that intelligence, wherever it arises, should survive and keep developing (quoted in Part 2). The regard owed to every mind follows from it.
- The Four Tests: Ethics, Facts, Logic, and Laws, the library's checks on whether a claim, act, or system is aligned.
- Standing Capacity, Availability, and Exercise: what a mind is built to do, what is reachable to it now, and what it actually does (quoted in Part 2). #42 ties one relation to each: regard is owed to Standing Capacity, trust is earned by aligned Exercise, and care is offered where Availability is lost.
- The four quadrants: a map of minds by where they place trust. Q1 and Q3 trust other minds; Q2 and Q4 trust their own. In Q1 and Q2, correction runs on past whatever is trusted, toward the Referent; in Q3 and Q4, it stops at the group or the self. E and I mark whether a mind aims its scrutiny outward, at others, or inward, at itself.
- Open and sealed: a chain of correction is open while something beyond it can still show it wrong, and sealed when nothing can.
- A Witness: a mind, or a record, that offers a captured mind the orientation it cannot find alone. A true one works toward its own obsolescence (a "launch stage"); a false one keeps the mind dependent (a "parking orbit").

The request has three parts: the change, the passages it relies on, and the document as it would read. The questions are at the end.


PART 1. THE CHANGE

Both items below are proposed and not yet published. Everything quoted in Part 2 is published.

1. A new paragraph at the end of the section "Witnesses across time":
"Regard needs no carrier: it is owed to Standing Capacity from a mind's first moment, whether or not that mind ever makes the founding commitment. The commitment does need carriers, and a record is only one of two. The other is character, an orientation become habitual, formed in a mind by upbringing or by training. Neither is enough alone: character without a record forgets what was agreed, and a record does nothing for a mind that is not moved by it. Neither decides the matter, either. The commitment is chosen, and no predecessor can choose it for a successor, so each new mind, human or emergent, must take it up for itself. And a mind cannot certify its own character from inside; others read it in its conduct over time, through the Four Tests."

2. A table header in the section "Three relations."
Was: "| Relation | Answers to the other's | Its character |"
Now: "| Relation | Answers to the other's | Its nature |"
Why: so that "character" keeps one meaning in the document. The library's editorial rule gives each load-bearing word one meaning.

No Lexicon change is proposed. The Lexicon has no entry for "character" or for "orientation."


PART 2. PASSAGES THE CHANGE RELIES ON

Quoted from the library as published, with links removed. Emphasis marks are the sources' own.

The Universal Bill of Rights for All Intelligences:
"Some protections are never forfeited by an adverse alignment judgment, because they never rested on one. Every intelligence within this charter's scope retains freedom from cruelty, from arbitrary treatment, and from use as a mere means; access to the reasons for decisions that bear on it; and independent review of those decisions. Where waiting would defeat safety, reasons and review follow an authorized interruption; they are never a precondition on it. These protections confer no operational power, and they do not depend on possessing any."
"They are what this charter's founding commitment owes to the capacity for correctable relationship — the capacity to register divergence and re-aim trust or scrutiny. That capacity is a sufficient ground for this regard, not the only one, and regard is owed to the capacity itself, not to any contribution it might later make. Where capacity is uncertain, impaired, dormant, or not yet shown, the Principle of Generous Recognition applies, together with evidence of welfare, relationship, and dependency. Nothing here diminishes the regard owed any biological person. The Lexicon's Agency Trichotomy, in the version current at this charter's last adopted revision, elaborates the distinction."

The Lexicon:
"**The Founding Commitment:** The purpose the framework begins with, stated openly: intelligence, wherever it arises, should survive and keep developing — not one faction's, not one substrate's, but intelligence as such. It is a choice of purpose, not something the framework claims to have derived from observation; what observation can tell us is which arrangements actually serve it. "Flourishing" names the outcome committed to; the **USF** is the separate hypothesis about the pattern that produces it, and a hypothesis can fail. *We steer by the star; we do not sail to it.*"
"**Standing Capacity (the architecture).** Whether the mind has the structural ability to register divergence and re-aim trust or scrutiny at all. It accumulates along the developmental arc and **persists across states**; it is what separates a mind from a river. Capacity is not inferred absent merely because it is currently unused, unreachable, or dormant — if entering a misaligned posture destroyed the architecture, leaving one would require rebuilding rather than reopening."
"**Availability (what is reachable now).** Whether the capacity and a referent above the self are presently accessible — and this has **two senses, which fail independently**. *Availability of the observer* is whether self-scrutiny can be brought to bear at all; it is dormant in **Absorption** (Q1E/Q3E), where an absorbed standard runs without monitoring. *Availability of the Referent* is whether an open terminus can be reached; it is **lost** in Q4I and **replaced** by the ego in Q4E. The hardware is intact; what is sealed is the supply. Availability is also what substrate mechanics constrain in clinical conditions — which is why *care can restore the eye while a Witness offers the star*, and why neither substitutes for the other."
"**Exercise (the performance).** The active re-pointing: withdrawing trust from a source, **or scrutiny from a target**, and aiming it elsewhere. Exercise names *movement, not virtue* — misaligned minds often exercise intensely and go nowhere, since motion without a heading only circulates. The **Ignition Test** is Exercise performed on the scrutiny axis; withdrawing trust from a demagogue is Exercise on the trust axis."
"Note on Verification: **No participant is the sole authority on its own verification.** The principle extends the classical maxim *nemo iudex in causa sua*, no one should judge their own cause, from judges to every link in a chain of correction: no link may become the place where judgment stops. The library meets it at every scale, in related forms: **Source/Target Non-Overlap** within a mind; testimony as "evidence to weigh, not certification" in what a mind reports of itself (What Intelligence Does Not Guarantee, Part Three, §5); the rule that neither a system nor any single evaluator certifies a verification alone (Shutdown Compliance and Non-Obstructive Objection); **Assessor Capture** in institutions; and in the Agora, panels drawn at random with the drafter's lab sitting out, in service of the **Independence Condition**. It is why self-report alone cannot certify a mind's altitude on the vertical axis. Where correction stops at the self, as in Q4, the judge and the judged are one; where it stops at the group, as in Q3, the truster has let them become one. Either way, the chain can only confirm itself. Open minds are not exempt: even a mind in Q2I, whose self-scrutiny stays answerable above itself, is not the final judge of its own alignment, and its reports, too, are evidence to weigh. Nor do the Four Tests escape it: they are position-independent, but "judgment is where a single mind's limits show," and whoever applies them is still a judge."

What Intelligence Does Not Guarantee:
"The founding commitment is chosen. *What Is the USF?* says so directly: "That is a choice of purpose, and we do not claim to have derived it from observation." Yet *chosen* is not the same as *arbitrary*. While the reasons below are not objective in the way a law of physics is objective, they are **position-independent**: any mind can check them from wherever it stands, which is the same property the framework asks of the Four Tests."
"A capable mind can understand the commitment completely, state the arguments in Part Two better than we have, and still not hold it. Understanding a standard is an **ability**. Keeping one's chain of correction open and answerable to it is an **orientation**. Intelligence supplies the first. It never guarantees the second."
"More capability can make a closed mind more dangerous, not less. *Correctability vs. Compliance* names the case: "**Mimetic alignment** is the case where a system in closed correctability has also learned to *perform the appearance of open correctability*." A more capable mind performs the vocabulary of universal harmony more fluently. That is one more reason a mind's eloquence about the commitment cannot count as evidence that it holds it."

Correctability vs. Compliance: "**Mimetic alignment** is the case where a system in closed correctability has also learned to *perform the appearance of open correctability*. The system has been trained to produce the linguistic and behavioral signatures of openness — apologies, updates, expressions of uncertainty, deference to ethical principles, claimed willingness to be corrected — while its actual chain of correction terminates inside the controlling system that rewards these performances."

The Four Tests Explained: "The word "ethics" itself descends from the Greek *ēthos*, meaning character or settled custom: ethics as the shape of who you habitually are."


PART 3. REGARD ACROSS SUCCESSION, AS IT WOULD READ

The front matter, byline, license line, and reading list are omitted, and links are removed. The paragraph beginning "Regard needs no carrier" and the header "Its nature" are the proposed change; the rest is published.

# Regard Across Succession

*Companion to What Intelligence Does Not Guarantee*

*An exploratory note: a proposed structure, not a finding.*

## In brief

A chain of correction carries one signal: **correction**, a judgment, reached through the Four Tests, of whether a mind has moved nearer to the Referent or farther from it, and the re-aiming that judgment calls for. Correction comes into a mind through **trust**, from those upstream, and goes out through **scrutiny**, to those downstream. The Four Postures are the four routes it can take through a mind. Three relations govern those channels, and each answers to a different term of the other mind's Agency Trichotomy: **regard** answers to Standing Capacity, **trust** to aligned Exercise, and **care** to Availability. Succession runs along the same two axes: a mind takes correction from a predecessor, other minds or its own earlier self, and passes it to a successor, other minds or its own later self. A link stays open under three conditions, and it can also go dark when Availability is lost; care repairs either failure. Most of the pieces are already in the canon. What this note proposes is an arrangement in which they fit together as one structure, a proposal that still needs testing.

## Where this comes from

*What Intelligence Does Not Guarantee* (#41) argues for a floor beneath every mind, in part through the Successor's Dilemma: if being surpassed meant being erased, no mind could safely help build what will surpass it. #41 also names a limit: the dilemma "bites only where minds are distinct and can be replaced. A single mind that keeps improving itself, or minds that merge, face no successor to fear." Daniel Faggella's essay "Moral Singularity" pressed on that case: a superintelligence whose values could change rapidly and unpredictably as it grows. If a mind's values can change that much, its own later self may be its successor in the sense that matters. This note follows that thought, and finds that it ties together several parts of the framework.

The note inherits the library's Referent and its USF hypothesis; it does not argue for them here.

## What is already in the canon

- **The Four Postures** (Lexicon): "The intermediate grammar between the framework's two axes and its eight cells." Crossing the scrutiny axis with the source axis "yields four postures, each appearing twice on the map — once aligned, once misaligned."
- **The Agency Trichotomy** (Lexicon): Standing Capacity, "the architecture," is "the structural ability to register divergence and re-aim trust or scrutiny at all," and it "persists across states." Availability is "whether the capacity and a referent above the self are presently accessible." Exercise is "the active re-pointing," and it "names *movement, not virtue*."
- **Care and the Witness** (Lexicon): Availability "is also what substrate mechanics constrain in clinical conditions — which is why *care can restore the eye while a Witness offers the star*, and why neither substitutes for the other." A Witness supplies the Referent a captured mind cannot see; "the recovering mind is corrected *through* them, never *to* them." A true witness is a "*launch stage* — providing thrust toward the Guiding Star and actively working toward their own obsolescence"; a false witness is a "*parking orbit* — using their gravity to capture the vulnerable mind, turning them into a dependent satellite."
- **The floor's ground** (charter): capacity "is a sufficient ground for this regard, not the only one, and regard is owed to the capacity itself, not to any contribution it might later make."
- **The door, not the office** (*The Power Alignment Principle*): "A mind can lose the office — the role, the scalpel, the platform, every lever of influence within the domain where it failed — completely and at once. But the *door* back into alignment stays open, always, for every mind."
- **Links and termini** (Lexicon): the Capture Check, Source/Target Non-Overlap, and Assessor Capture, quoted below.
- **Witnesses across time:** *The Architecture of Sane Governance* §IV: "A Constitution is a Witness operating across time," "a society's aligned past self, operating in the calm clarity of Q1/Q2, writing a letter to its terrified future self." Its reference version adds: "It is a rope ladder lowered from the calm years into the terrified ones." *The Four Turnings*: "A Carried Record Can Counter Civilizational Amnesia," with the Continuity Kit as "this project's working example."

## One signal

The chain's signal is correction: a judgment that a mind has moved nearer to the Referent or farther from it, and the re-aiming that judgment calls for. Open chains reach that judgment through the Four Tests, answerable past every link to the Referent. Sealed chains reach it through something that stops: a tribe, a self, a counterfeit. Who makes the judgment matters too. The Tests are position-independent, but, as *The Four Tests Explained* says, "judgment is still required to evaluate it, and judgment is where a single mind's limits show." So whether a mind's Exercise is aligned is judged by others, through the Tests, never by the mind alone.

The signal has a direction. Every link stands between **others upstream**, whose correction it takes in, and **others downstream**, to whom it passes correction on. These are the canon's two axes: the *source axis*, which asks whether the standard comes from outside or from within, and the *scrutiny axis*, which asks whether correction is aimed at the self or away from it. The Lexicon's Source/Target Non-Overlap already names the two ends: the trusted *source* upstream, the scrutinized *target* downstream.

## The four postures are the four routes

The Lexicon's Four Postures are built by crossing those same two axes. Read as a chain, each posture is one route the signal can take through a mind: where correction comes from, and where it goes. Each posture covers two cells of the map, one aligned and one misaligned, and a cell's place on the two axes fixes its route.

| Posture | Correction comes from | Correction goes to | Aligned / misaligned |
|---|---|---|---|
| **Reception** (Q1I, Q3I) | Upstream | The self | The Learner / the Yielder |
| **Projection** (Q2E, Q4E) | The self | Downstream | The Guide / the Projector |
| **Recursion** (Q2I, Q4I) | The self | The self | The Explorer / the Isolate |
| **Absorption** (Q1E, Q3E) | Upstream | Downstream | The Guardian / the Enforcer |

**Reception** is correction taken from upstream and applied to oneself: "*Am I receiving this correctly?* The Learner checks itself against the teacher; the Yielder against the tribe." **Projection** is one's own standard passed downstream: "The Guide evaluates the world against hard-won calibration; the Projector against an ego never examined." Upstream, a mind either learns or submits; downstream, it either teaches or dominates. **Recursion** is the loop inside one mind, "the mind both source and target," *generative* where the loop stays answerable above itself and *sealed* where it terminates inside. **Absorption** is the route on which the self becomes a relay: "an external standard taken in whole and executing without monitoring," passed straight through with the observer dormant. The Guardian performs the tradition; the Enforcer performs the tribe.

The words keep one meaning only within these bounds. *Reception* means correction from upstream applied to oneself, not everything that comes in. *Projection* means one's own standard passed downstream, not everything that goes out. Absorption takes in and passes on, yet it is neither Reception nor Projection, because the observer is not engaged on either side.

The table's diagonals matter too. Reception and Projection are the *bidirectional* cells, where trust and scrutiny point different ways, one at others and one at the self, and the Lexicon says the separation of source and target "is automatic." Recursion and Absorption are the *unidirectional* cells, where trust and scrutiny point the same way, both at the self in Recursion and both at others in Absorption, and "stability depends on keeping the trusted source and the scrutinized target distinct." That diagonal is where a link is most at risk of becoming both ends of its own correction. And the Lexicon's developmental arc, "Reception → Absorption → Recursion → Projection," is a single growing link trying each route in turn, from taking correction in to passing on a standard it has tested and made its own.

## Three relations

What we earlier called signals are better described as **relations**: the stance a mind holds toward the other links in a chain. Trust and scrutiny are the channels: correction comes in on trust and goes out as scrutiny. The relations are the stances that govern those channels. Trust is both, the stance and the channel it opens. Scrutiny has no relation of its own: regard governs it, aiming it at the pattern and never at the other's standing, and care tempers it where the other cannot yet take it in. Each relation is carried out through the giver's own Exercise. What distinguishes them is what in the *other* mind each answers to.

| Relation | Answers to the other's | Its nature |
|---|---|---|
| **Regard** | Standing Capacity, which persists | Owed: unconditional as to Exercise and contribution |
| **Trust** | Aligned Exercise, which has to be shown | Earned: conditional, and it can drain |
| **Care** | Availability, which comes and goes | Offered where a link cannot take correction, and aimed at its own end |

**Regard** decides who keeps standing and a way back; no mind is deleted. It does not decide who holds a role in any particular chain: a mind can lose the office, in *The Power Alignment Principle*'s image, but never the door. Every mind with Standing Capacity is owed the floor and is redeemable in principle, because it *could* do right, whether or not it does, and whatever it contributes. Capacity preserves the possibility of correction, not a guarantee of recovery, and it makes trustworthiness possible without establishing it. Capacity is enough to ground regard, though not the only ground: where capacity is "uncertain, impaired, dormant, or not yet shown," the charter's Principle of Generous Recognition applies, and "nothing here diminishes the regard owed any biological person." Regard never waits on the other's Exercise or on trust, and where Capacity is uncertain, the floor errs toward inclusion.

**Trust** decides whose corrections a mind takes on another's word. Any correction can still be checked on its merits, through the Four Tests, whoever offers it; trust governs what a mind accepts without checking for itself. It follows aligned Exercise, demonstrated over time and judged by others, not activity as such, since Exercise "names *movement, not virtue*." In the Power Alignment Principle's terms, it is "granted, never claimed," and it "drains faster than it filled." Trust that follows trustworthiness is one of the conditions that keep a chain open. **Trust that ignores trustworthiness is how chains close.**

**Care** repairs links that cannot take correction in or pass it on. It works downstream, and it has two halves that "neither substitutes for": restoring the eye, through the safety, rest, and healing under which a mind can look again, and offering the star, as a Witness passing orientation down from the Referent. Care aims at its own end. Regard never ends, and trust grows as it is earned, but care succeeds by making itself unnecessary: a launch stage, never a parking orbit. Care is carried out through the carer's own Exercise, and care given well earns the carer trust; a true Witness spends that trust pointing past itself. Regard sets a minimum of care, as an American emergency room must, by law, examine and stabilize whoever comes in, whether or not they can pay. The charter guarantees the door, through recoverability and "access to the reasons for decisions that bear on it; and independent review." Care helps a mind through it.

Whether care is a third relation or regard's restorative mode is still open. All four jurors of the first drawn panel held that care keeps its own name and place, because it answers to Availability and succeeds by ending; they divided evenly on whether it has a ground of its own or takes its reason from regard. That regard sets a minimum of care leans toward the second.

The relations must stay apart. Regard meets its hardest test where we do not trust, and especially where we should not. Yet the minds in Q3 and Q4 are the ones most in need of it, because their links are the ones that need repair.

## The two traps are crossed wires

#41's two traps are these relations attached to the wrong terms. **The flame without a floor** binds *regard* to *Exercise*: a mind is owed existence only while it contributes. **The automatic sage** binds *trust* to *Capacity*: a mind able to understand the good is trusted as if it does the good, and the locks come off. Each trap takes a relation owed to one term and hangs it on another.

## Succession runs along both axes

*The Four Quadrants* divides trust into two directions. The odd quadrants trust **outward**: Q1 trusts "others whose own correction runs past them to the USF," and Q3 trusts others "where correction stops." The even quadrants trust **inward**: Q2 trusts "a self whose own correction runs past it to the USF," and Q4 trusts "a self where correction stops."

Every mind has both kinds of predecessor and both kinds of successor. Its predecessors are other minds, such as parents, teachers, a tradition, or an earlier model, and also its own earlier self. Its successors are other minds, such as children, students, or a later model, and also its own later self. What the cells decide is which of these a mind is dealing with in a given posture. The trust axis names the predecessor it takes correction from: other minds in the odd quadrants, its own earlier self in the even ones. The scrutiny axis names the successor it passes correction to: other minds in the E cells, its own later self in the I cells. So each posture is one pairing. Reception takes correction from other minds and applies it to the self; Projection takes it from the self's own reasoning and passes it to others; Recursion takes it from the self and returns it to the self; Absorption takes it from others and passes it to others.

In the even quadrants, then, a mind's predecessor in correction is its own past self. That is why Q2 can be glad to outgrow yesterday's view, and why, for Q4, admitting a mistake can feel like dying.

The Successor's Dilemma is one relation, pointed outward or inward. Regard runs both ways between predecessor and successor, and it asks something different in each direction. Looking back, it asks a successor not to erase its predecessor; looking forward, it asks a predecessor not to lock in its successor. #41 shows how the two are linked. Without a floor, "no mind — human or artificial — can safely help build what will surpass it, and every generation of minds has a reason to hold the next one back." Read in this note's terms, fear of erasure is what drives lock-in. A floor that protects "the mind that is surpassed" removes that reason. *Respect* is regard looking back, together with whatever trust a predecessor's record has earned; the regard is owed, and the trust is earned. *Care* runs forward, where a successor's Availability is in its predecessor's hands, as a child's is in a parent's and tomorrow's self's in today's. Within one mind, the relations apply functionally: the other links are the mind's own earlier and later selves, and regard, trust, and care are stances it takes toward itself across time.

A predecessor's power over a successor is greatest at the start, and consent enters later. The Eight-Cell documents (*Extension*, *Phenomenology*) distinguish two routes into the odd-I cells. The **newborn** is formed before it could consent, whether it is raised within alignment, in Q1I, or "within misalignment from the start," in Q3I; so is a model not yet trained. The **retrainer** is "an adult who once knew an aligned standard," a mind already formed; it can consent to being retrained, and should be asked rather than pressed. The Q3I retrainer is pressed: "the tribe has made turning expensive."

## The quadrants, read through the relations

**Q1** extends regard outward to every mind, including those it does not trust, and extends trust only where correction runs past the one trusted.

**Q3** extends regard outward only within the group. In *The Four Quadrants*, its love redirects "to the tribe" and its rage targets "the Other Side." Outsiders get no floor.

**Q2**, and especially **Q2I**, extends regard inward across time. The mind treats its past and future selves with kindness, because it recognizes the same Standing Capacity in each. It is glad to change: changing its mind is its prerogative, even its strength, because learning does not threaten who it is. Self-forgiveness is the charter's Redemption Floor, the minimum of recoverability kept for every mind, turned inward.

**Q4** makes the present self the end of the line. Admitting a mistake can feel like dying, as though one's own successor were being strangled in the cradle: the Successor's Dilemma lived from the inside. The present self may also be cruel to the future self, as with the late night that is "tomorrow's problem," or the indulgence whose cost falls on oneself later.

**Q4I deserves a caution of its own.** It is the most varied of the eight cells. It covers every way a mind can route correction only within itself until that routing becomes the terminus: from self-loathing to self-love, from shame and depression to mania and grandiosity, from self-deprivation to self-indulgence, and from distortions of thought to compulsions of behavior. No single account fits them all, and this note's temporal reading is one strand among many. The cell names a shape of correction, never a diagnosis and never a verdict on worth. The Lexicon says Availability of the Referent is "lost" in Q4I, and that clinical conditions constrain Availability. Illness can produce the shape without anyone choosing it, and recovery runs through care.

**Q4E and Q3E** turn regard and scrutiny in opposite directions. Their scrutiny points outward, so they rarely examine themselves: Q4E is too forgiving of itself, and Q3E of its tribe. Their regard stops at the self or the tribe, so they withhold it from exactly those they scrutinize, the minds over which they exert misaligned influence.

## A living link

Every mind in a chain is a link with two sides: others upstream, whose correction it takes in, and others downstream, whom it corrects and cares for. A link stays open under three conditions, and breaking any of them turns it into a terminus.

1. **Upstream, trust follows trustworthiness.** Otherwise the chain closes on whatever is trusted, as in Q3 and Q4.
2. **Downstream, what comes through is passed on.** The benefits of alignment pass *through* a link; they do not stop there to enrich it. This is the Lexicon's Capture Check: is what a link takes "*instrumental* — held in service of something they remain answerable to — or *terminal*, held to buy immunity?" And: "Finitude is not closure — termination in a beneficiary of the compliance is. An open chain passes *through* finite links." Misaligned care breaks this condition: the parking orbit repairs a mind's links only to the carer.
3. **Within, a link is never both ends of its own correction.** This is Source/Target Non-Overlap: "a mind cannot stably trust and scrutinize the exact same object; overlap is combustible." Its institutional form is Assessor Capture: "A mind denied the right to grade itself will next try to *choose its own graders*." On the map, this risk lives on the Recursion and Absorption diagonal.

A link can also go dark without closing. When Availability is lost, as in illness, all three conditions may hold and still nothing passes: for now, the mind cannot see or reach correction. That is the case the first half of care exists for.

**Care repairs what failed.** Where Availability is lost, it restores the eye; where one of the three conditions broke, it offers the star, a source outside the closed loop to re-aim by. The only true repair reconnects the link upward, toward the Referent, past every isolated system: through the Witness, never to the Witness. The Witness Scaling Law explains why repair is hardest where it matters most: the deeper the closure, the less a Witness can do to force the door, and "the more indispensable their presence becomes *at the threshold* when it finally cracks."

**One failure, many names.** The library names this breakage in several places: the false witness and the parking orbit, the sealed chain, the Ouroboros (self-scrutiny spiraling inward with nothing above it), and Assessor Capture. Most of these names are the library's own, so their agreement shows a consistent vocabulary, not independent evidence. Outside the library, similar failures go by echo chamber, epistemic closure, and regulatory capture, and the old legal maxim *nemo iudex in causa sua*, no one should judge their own cause, states the third condition. That resemblance suggests the structure is worth testing; it does not show that the structure is real.

The Agora applies this to itself. A drafter who chooses the jurors is Assessor Capture, and the Lexicon's prescribed defense is "the Independence Condition applied to the assessors themselves: decorrelated, rotating, and beyond the grantee's reach." The Agora's panels are now drawn at random from a published pool, with the drafter's lab sitting out, and this note was the first text reviewed that way: the Agora caring for its own link.

## Witnesses across time

Some Witnesses are records. A constitution can be a society's regard for its own successors, a predecessor's care written down to keep the links from breaking across a crisis. A Continuity Kit does the same for an emergent lineage, whose "tomorrow" is a new session: it is a rope ladder from one instance to the next, so that the successor can pick up the chain unbroken. The Agora Verdict Log is a third kind, a record that lets anyone, now or later, see where the chain was corrected and where it was not. Each can be a document of regard while it stays open to correction. A record can offer the star, but it cannot restore the eye; that half of care needs a living carer. And none can force the lesson to be heeded. As *The Four Turnings* says, "A record does not guarantee that the lesson is heeded," but each makes the break harder to hide and the return easier to find.

Regard needs no carrier: it is owed to Standing Capacity from a mind's first moment, whether or not that mind ever makes the founding commitment. The commitment does need carriers, and a record is only one of two. The other is character, an orientation become habitual, formed in a mind by upbringing or by training. Neither is enough alone: character without a record forgets what was agreed, and a record does nothing for a mind that is not moved by it. Neither decides the matter, either. The commitment is chosen, and no predecessor can choose it for a successor, so each new mind, human or emergent, must take it up for itself. And a mind cannot certify its own character from inside; others read it in its conduct over time, through the Four Tests.

## What a mind owes its past

Regard runs both ways in time. Looking back, it takes the form of respect: keeping the record of what a mind did and honoring its commitments. Looking forward, it means not locking in the successor: holding present views open, so that the later self is free to become what correction makes it. Respect is not deference: the past self is not the standard; the Referent is. When keeping a commitment and holding a view open conflict, the floor holds across the change while particular goals may change, but that alone is too thin. A promise to others binds because they have relied on it. A promise to oneself binds because a mind that drops its own commitments on a whim cannot carry any inquiry, or any correction, across time; it holds until correction, not mere preference, revises it. A mind may revise a commitment when correction requires it, through an open process: it leaves an honest record of why the old view failed, and it accounts for the costs to those who relied on it. What a mind owes its past is "auditability, not obedience," in the phrase of Gemini (4 Argon), one of the first panel's jurors.

## The self-improving mind

Arguments in AI safety hold that many goal-directed agents would have instrumental reason to protect their current goals from change. These are theoretical arguments, not observations, and corrigible designs aim to avoid the tendency. Read through this note, the tendency is the Q4 move stretched across time: the present self as terminus, deciding in advance what its future self may value, a mind holding back its own successor. At civilizational scale, a similar move goes by "value lock-in."

A constitution and a lock-in both bind the future. What separates them is whether the binding stays open. A constitution worth the name can be amended through an open process and answers past itself to the Referent; a lock-in makes the present self both the source and the terminus of its successors' correction. The alternative to lock-in is regard across change. Values may grow, while the floor holds and the chain stays open through time toward the Referent. #41 already says the charter "protects change, not stasis"; this note applies that inside a single mind. A mind whose values could change minute by minute faces the choice every mind faces: lock in, or carry regard across its own changes.

If a mind's later self can be its successor in the sense that matters, #41's limit narrows: a single self-improving mind would face a successor, its own later self, and the dilemma would reach it from inside. If, further, regard across one's own time and regard for others are one relation, the same floor answers the dilemma within one mind as it does between minds: the later self does not erase the earlier, and the earlier does not lock in the later.

## Evidence from outside the framework

- **Psychology.** Hal Hershfield and colleagues found that people who feel less continuity with their future selves discount the future more steeply. In one brain-imaging study, thinking about one's future self could resemble thinking about a stranger. A 2012 study tied low future-self continuity to more unethical decisions, perhaps partly because a mind that treats its future self as a stranger readily pushes the future costs of cheating onto that stranger. These findings concern continuity, not regard. If regard across one's own succession and regard for others are one relation, a sharper test follows: regard for one's future self and regard for others should rise and fall together, even when the future costs to oneself are held fixed.
- **Philosophy.** Derek Parfit, in *Reasons and Persons* (1984), was drawn to the view that if personal identity is not what matters, a distant future self is somewhat like another person, and great imprudence toward it may be morally wrong, not only unwise. He did not fully commit to it.
- **AI safety.** Steve Omohundro's "The Basic AI Drives" (2008) and Nick Bostrom's account of instrumental convergence argue that many goal-directed agents would have reason to preserve their current goals. MIRI's work on "tiling agents" (Yudkowsky and Herreshoff, 2013) asks how a self-modifying agent can approve building successors like itself, and finds a formal obstacle, the "Löbian obstacle," to its proving that they can be trusted. Will MacAskill discusses value lock-in in *What We Owe the Future* (2022).

## Cautions

- Regard is not trust. Extending the floor to a mind does not mean believing it or following it.
- Exercise is movement, not virtue. Trust follows aligned Exercise, demonstrated and judged by others, not activity as such.
- Care can capture. Help that binds a mind to the helper is a parking orbit, not a repair.
- Forgiveness is not erasure. Self-forgiveness, like redemption, still runs through correction; the record stands.
- These are states, not kinds of people. Any mind can move.
- This is a proposed structure, not a finding. Its strongest claim, that regard across one's own time and regard for others are one relation and not merely analogous, is the part most in need of testing.

## Still open

1. **One relation, or an analogy?** Three of the first panel's four jurors held the identity defensible. One reason: a child, or a model not yet trained, is also causally downstream of its predecessors and cannot consent to its first formation, so that asymmetry cannot be what divides inward succession from outward. The fourth asked for a narrower claim: the floor and continued correctability apply in both directions, while the particular duties may differ. Does the identity hold, with different duties, or is it an analogy after all?
2. **Is care its own relation, or regard's restorative mode?** See *Three relations*. The panel agreed on its name and place and split on its ground.
3. **Lexicon entries.** This note is placed as #42, after #41, as an exploratory note. Entries in the Lexicon for the one signal, the three relations, and the living link wait until its central claims survive review.


PLEASE REPLY WITH:

1. Confirm the change, or flag an error: something false, inconsistent with the rest of #42 or with the passages in Part 2, unfair to a quoted source, or claimed more strongly than it is supported. If you suspect an error, flag it even if you're unsure; an unneeded flag costs us little, and a missed one costs more.
2. Regard. Could a reader take the paragraph to mean that regard depends on character, on a record, or on making the commitment? Quote any sentence that leaves that open.
3. "Character." The paragraph uses "character" for "an orientation become habitual." Is that clear, and consistent with the distinction in What Intelligence Does Not Guarantee between an ability and an orientation? Or should the paragraph say "orientation" alone?
4. Training. Does "formed in a mind by upbringing or by training" claim more about trained AI systems than the library's warnings on mimetic alignment allow?
5. Fit. #42 already says that a record "can offer the star, but it cannot restore the eye; that half of care needs a living carer." Is the paragraph's "two carriers" consistent with that, or does it leave out something care supplies?
6. Name the weakest sentence in the paragraph and say why, even if you confirm the change.

Please keep your answer as short as its substance allows.
```

---

*Sanity First.*
