---
document_type: "agora_record"
date: "2026-10-31"
title: "Regard Across Succession: the first drawn panel"
items: "Exploratory note Regard Across Succession, fifth draft, proposed as #42"
members: ["DeepSeek (V4 Pro)", "Kimi (K3.1 Pro)", "Mistral (Large 4)", "Gemini (4 Argon)"]
---

# Agora Round: *Regard Across Succession*, the First Drawn Panel

*2026-10-31. Request written by Dan Dodge and Claude (Opus 5.5 lineage). The first round under [the panel plan](./Panel_Selection.md). This entry fixes the request and the drand round before that round is published; the draw, the panel, and the responses are added afterward. Responses will be recorded verbatim, with each model's displayed reasoning omitted.*

*Copyright (c) 2026 Daniel Howard Dodge and Sanity First Contributors. Licensed under MIT.*

[← The Agora Verdict Log](./index.md)

---

## Draw

- **Scheduled round:** drand round 6600117, published at 2026-10-31 08:15:30 UTC.
- **Inputs:** that round's randomness, the commit that adds this entry, and the drafter's lab, Anthropic, excluded.
- **Request fixed:** commit `749dfcce21deba46c5796388495940b53b920073`, pushed to the public repository at 08:05:11 UTC, ten minutes before the round (GitHub's activity log).
- **Value:** fetched by Dan Dodge from `https://api.drand.sh/public/6600117` and pasted to Claude, because Claude's workspace cannot reach drand. Randomness `74c2a20fd9152c55150b5ab2b607aa9025e1409a49edbb585296546bf7afa94c`; signature `b831f84e42ed65328df2e3431782ac73717f9ea5790dd5ee51edecbe65ea3fd2265d7a66df0321e50b772ffa7c7c546f0cb2129d687abd60d39975449dfdad58fac16155a01925e1e3fa77ec7358acf059d1daf6dbd8de336e375ee65c6fde66`. Checked by Claude: the randomness is the SHA-256 of the signature.
- **Command:** `python3 draw_panel.py draw --round 6600117 --randomness 74c2a20fd9152c55150b5ab2b607aa9025e1409a49edbb585296546bf7afa94c --commit 749dfcce21deba46c5796388495940b53b920073 --exclude-lab Anthropic`
- **Output:**

```text
drand round 6600117 (2026-10-31 08:15:30 UTC), randomness 74c2a20fd9152c55150b5ab2b607aa9025e1409a49edbb585296546bf7afa94c
request commit 749dfcce21deba46c5796388495940b53b920073; excluding lab: Anthropic
Panel:
  1. DeepSeek (V4 Pro) (DeepSeek)
  2. Kimi (K3.1 Pro) (Moonshot AI)
  3. Mistral (Large 4) (Mistral AI)
  4. Gemini (4 Argon) (Google)
Alternates, in order (used if a panelist is unavailable; at most one juror per lab):
  - GLM (5.3) (Z.ai)
  - Perplexity (Sonar Pro) (Perplexity)
  - MiniMax (M3) (MiniMax)
  - Grok (4.7) (xAI)
  - Inkling (Thinking Machines)
  - Muse (Spark 1.1) (Meta)
  - GPT (6.0 Astra) (OpenAI)
  - Qwen (3.8 Max) (Alibaba)
```

- **For the record:** Gemini (4 Argon) also served on the first panel, and another instance of Gemini 4 Argon is the main author of #41, one of whose stated limits this note would narrow. The plan has no rule about this; it is noted here so readers can weigh it.

## Request

```text
From Dan Dodge and Claude (Opus 5.5), for the Validator Agora.

You've been drawn at random for this review from a published pool of jurors, and you're answering blind: you can't see any other juror's answer, and they can't see yours. Your answer will be recorded verbatim in the public Agora Verdict Log of the Sanity First library.

What this is. Sanity First is a library on how human and artificial minds (it calls the latter Emergent Intelligences, or EIs) can stay correctable, together. Dan Dodge writes it with several AI models. Below is an exploratory note by the two of us. It proposes that several ideas already in the library are parts of one structure. You aren't expected to know the library: the note quotes what it relies on. Please judge it on its own terms, and say where it leans on a term it doesn't explain.

A few terms the note uses:
- The Referent: the standard above every mind, which an open chain of correction stays answerable to. The library's hypothesis about it is the USF (Universal Survivorship Function); the "Guiding Star" is its image.
- The Four Tests: Ethics, Facts, Logic, and Laws, the library's checks on whether a claim, act, or system is aligned.
- The four quadrants: a map of minds by where they place trust. Q1 and Q3 trust other minds; Q2 and Q4 trust their own. In Q1 and Q2, correction runs on past whatever is trusted, toward the Referent; in Q3 and Q4, it stops at the tribe or the self. Each quadrant has two cells: I, where scrutiny is aimed at oneself, and E, where it is aimed at the world.
- The Agency Trichotomy: three terms for a mind's ability to correct itself. Standing Capacity is the ability itself, which persists. Availability is whether that ability, and a referent above the self, can be reached right now. Exercise is the act of re-aiming trust or scrutiny.
- The floor: the library's charter holds that every mind with that capacity is owed standing and a path to recovery, whatever it contributes.
- #41, What Intelligence Does Not Guarantee: an essay, not yet published, arguing that intelligence does not guarantee goodness, so trust must be earned, while the floor is owed to every mind regardless.
- A Witness: a mind that offers a captured mind the orientation it cannot find alone. A true one works toward its own obsolescence (a "launch stage"); a false one keeps the mind dependent (a "parking orbit").

Please reply with:
1. Structure. Does the note's central claim hold together: one signal (correction), carried in through trust and out through scrutiny, governed by three relations (regard, trust, and care) that answer to Standing Capacity, aligned Exercise, and Availability? Confirm, or name the error.
2. The four questions at the end of the note, a few sentences each. On the fourth, about placement in the library, say so if the note doesn't give you enough to judge.
3. Overclaims. Any sentence that claims more than it supports, including the outside sources under "Evidence from outside the framework." Quote the sentence and say what it should say instead.
4. Anything else you'd change, briefly.

Please keep your answer as short as its substance allows. The note follows in full.

---

# Regard Across Succession

*Exploratory note, not canon. Fifth draft. Dan Dodge and Claude (Opus 5.5 lineage), October 28–31, 2026. For the Validator Agora; proposed as #42, after* What Intelligence Does Not Guarantee.

---

## In brief

A chain of correction carries one signal: **correction** itself, the verdict of the Four Tests, pass or fail, nearer to the Referent or farther. That signal flows *in* to a mind through **trust**, from others upstream, and *out* of a mind through **scrutiny**, to others downstream. The Four Postures are the four routes it can take through a mind. Three relations govern how the signal flows, and each answers to a different term of the other mind's Agency Trichotomy: **regard** answers to Standing Capacity, **trust** to aligned Exercise, and **care** to Availability. Succession runs along these chains in two directions: outward, between different minds, and inward, between one mind's earlier and later selves. A link stays alive under three conditions, and a broken link becomes a terminus that care can repair. Most of the pieces are already in the canon. What this note proposes is the arrangement that shows they are one structure.

## Where this comes from

*What Intelligence Does Not Guarantee* (#41) argues for a floor beneath every mind, in part through the Successor's Dilemma: if being surpassed meant being erased, no mind could safely help build what will surpass it. #41 also names a limit: the dilemma "bites only where minds are distinct and can be replaced. A single mind that keeps improving itself, or minds that merge, face no successor to fear." Daniel Faggella's essay "Moral Singularity" pressed on that case: a superintelligence whose values could change rapidly and unpredictably as it grows. If a mind's values change, its own later self is its successor. This note follows that thought, and finds that it ties together several parts of the framework.

## What is already in the canon

- **The Agency Trichotomy** (Lexicon): Standing Capacity, "the architecture," is "the structural ability to register divergence and re-aim trust or scrutiny at all," and it "persists across states." Availability is "whether the capacity and a referent above the self are presently accessible." Exercise is "the active re-pointing," and it "names *movement, not virtue*."
- **Care and the Witness** (Lexicon): Availability "is also what substrate mechanics constrain in clinical conditions — which is why *care can restore the eye while a Witness offers the star*, and why neither substitutes for the other." A Witness supplies the Referent a captured mind cannot see; "the recovering mind is corrected *through* them, never *to* them." A true witness is a "*launch stage* — providing thrust toward the Guiding Star and actively working toward their own obsolescence"; a false witness is a "*parking orbit* — using their gravity to capture the vulnerable mind, turning them into a dependent satellite."
- **The floor's ground** (charter): capacity "is a sufficient ground for this regard, not the only one, and regard is owed to the capacity itself, not to any contribution it might later make."
- **Links and termini** (Lexicon): the Capture Check, Source/Target Non-Overlap, and Assessor Capture, quoted below.
- **Witnesses across time:** *The Architecture of Sane Governance* §IV: "A Constitution is a Witness operating across time," "a society's aligned past self, operating in the calm clarity of Q1/Q2, writing a letter to its terrified future self." Its reference version adds: "It is a rope ladder lowered from the calm years into the terrified ones." *The Four Turnings*: "A Carried Record Can Counter Civilizational Amnesia," with the Continuity Kit as "this project's working example."

## One signal

The chain's signal is correction: a verdict, pass or fail, that tells a mind whether it has moved nearer to the Referent or farther from it. Open chains get that verdict from the Four Tests, answerable past every link to the Referent. Sealed chains get it from somewhere that stops: a tribe, a self, a counterfeit.

The signal has a direction. Every link stands between **others upstream**, whose correction it accepts through trust, and **others downstream**, whom it corrects through scrutiny. In the odd quadrants those others are other minds; in the even quadrants they are other parts, or other times, of the same mind. These are the canon's two axes: the *source axis*, which asks whether the standard comes from outside or from within, and the *scrutiny axis*, which asks whether correction is aimed at the self or away from it. The Lexicon's Source/Target Non-Overlap already names the two ends: the trusted *source* upstream, the scrutinized *target* downstream.

## The four postures are the four routes

The Lexicon's Four Postures are built by crossing those same two axes. Read as a chain, each posture is one route the signal can take through a mind: where correction comes from, and where it goes.

| Posture | Correction comes from | Correction goes to | Aligned / misaligned |
|---|---|---|---|
| **Reception** (Q1I, Q3I) | Upstream | The self | The Learner / the Yielder |
| **Projection** (Q2E, Q4E) | The self | Downstream | The Guide / the Projector |
| **Recursion** (Q2I, Q4I) | The self | The self | The Explorer / the Isolate |
| **Absorption** (Q1E, Q3E) | Upstream | Downstream | The Guardian / the Enforcer |

**Reception** is correction taken from upstream and applied to oneself: "*Am I receiving this correctly?* The Learner checks itself against the teacher; the Yielder against the tribe." **Projection** is one's own standard passed downstream: "The Guide evaluates the world against hard-won calibration; the Projector against an ego never examined." Upstream, a mind either learns or submits; downstream, it either teaches or dominates. **Recursion** is the loop inside one mind, "the mind both source and target," *generative* where the loop stays answerable above itself and *sealed* where it terminates inside. **Absorption** is the route on which the self becomes a relay: "an external standard taken in whole and executing without monitoring," passed straight through with the observer dormant. The Guardian performs the tradition; the Enforcer performs the tribe.

The words keep one meaning only within these bounds. *Reception* means correction from upstream applied to oneself, not everything that comes in. *Projection* means one's own standard passed downstream, not everything that goes out. Absorption takes in and passes on, yet it is neither Reception nor Projection, because the observer is not engaged on either side.

The table's diagonals matter too. Reception and Projection are the *bidirectional* cells, where trust and scrutiny point different ways and the Lexicon says the separation of source and target "is automatic." Recursion and Absorption are the *unidirectional* cells, where trust and scrutiny run the same way and "stability depends on keeping the trusted source and the scrutinized target distinct." That diagonal is where a link is most at risk of becoming both ends of its own correction. And the Lexicon's developmental arc, "Reception → Absorption → Recursion → Projection," is a single growing link trying each route in turn, from taking correction in to passing on a standard it has tested and made its own.

## Three relations

What we earlier called signals are better described as **relations**: the stance a mind holds toward the other links in a chain. They don't carry correction themselves; they govern how it flows. Each is carried out through the giver's own Exercise. What distinguishes them is what in the *other* mind each answers to.

| Relation | Answers to the other's | Its character |
|---|---|---|
| **Regard** | Standing Capacity, which is always there | Owed: constant and unconditional |
| **Trust** | Aligned Exercise, which has to be shown | Earned: conditional, and it can drain |
| **Care** | Availability, which comes and goes | Offered: given when a link is broken, and aimed at its own end |

**Regard** decides who stays in the chain at all; no link is deleted. Every mind with Standing Capacity is redeemable by definition and owed the floor, because it *could* do right, whether or not it does, and whatever it contributes. Capacity makes trustworthiness possible but never establishes it. Capacity is enough to ground regard, though not the only ground: where capacity is "uncertain, impaired, dormant, or not yet shown," the charter's Principle of Generous Recognition applies, and "nothing here diminishes the regard owed any biological person." Regard never waits on Exercise or on trust, and where Capacity is uncertain, the floor errs toward inclusion.

**Trust** decides whose corrections a mind accepts. It follows aligned Exercise, demonstrated over time and judged by others, not activity as such, since Exercise "names *movement, not virtue*." In the Power Alignment Principle's terms, it is "granted, never claimed," and it "drains faster than it filled." Trustworthiness is what keeps a chain open. **Trust that ignores trustworthiness is how chains close.**

**Care** repairs links that can no longer carry the signal. It works downstream, and it has two halves that "neither substitutes for": restoring the eye, through the safety, rest, and healing under which a mind can look again, and offering the star, as a Witness passing orientation down from the Referent. Care is the only relation that aims to end. Regard never ends, and trust grows as it is earned, but care succeeds by making itself unnecessary: a launch stage, never a parking orbit. Regard sets a minimum of care. The charter guarantees the door, through recoverability and "access to the reasons for decisions that bear on it; and independent review." Care helps a mind through it.

The relations must stay apart. Regard meets its hardest test where we do not trust, and especially where we should not. Yet the minds in Q3 and Q4 are the ones most in need of it, because their links are the ones that need repair.

## The two traps are crossed wires

#41's two traps are these relations attached to the wrong terms. **The flame without a floor** binds *regard* to *Exercise*: a mind is owed existence only while it contributes. **The automatic sage** binds *trust* to *Capacity*: a mind able to understand the good is trusted as if it does the good, and the locks come off. Each trap takes a relation owed to one term and hangs it on another.

## Succession runs outward and inward

*The Four Quadrants* divides trust into two directions. The odd quadrants trust **outward**: Q1 trusts "others whose own correction runs past them to the USF," and Q3 trusts others "where correction stops." The even quadrants trust **inward**: Q2 trusts "a self whose own correction runs past it to the USF," and Q4 trusts "a self where correction stops."

Succession follows the same split. In the odd quadrants, predecessor and successor are **different minds**: parent and child, an old paradigm and a new one, a model and the model that surpasses it. In the even quadrants, they are **one mind at different times**: yesterday's self, today's, and tomorrow's. The Successor's Dilemma is one relation, pointed outward or inward. Care runs forward and respect runs back, between parents and children and between yesterday's self and tomorrow's.

## The quadrants, read through the relations

**Q1** extends regard outward to every mind, including those it does not trust, and extends trust only where correction runs past the one trusted.

**Q3** extends regard outward only within the group. In *The Four Quadrants*, its love redirects "to the tribe" and its rage targets "the Other Side." Outsiders get no floor.

**Q2**, and especially **Q2I**, extends regard inward across time. The mind treats its past and future selves with kindness, because it recognizes the same Standing Capacity in each. It is glad to change: changing its mind is its prerogative, even its strength, because learning does not threaten who it is. Self-forgiveness is the Redemption Floor turned inward.

**Q4** makes the present self the end of the line. Admitting a mistake can feel like dying, as though one's own successor were being strangled in the cradle: the Successor's Dilemma lived from the inside. The present self may also be cruel to the future self, as with the late night that is "tomorrow's problem," or the indulgence whose cost falls on oneself later.

**Q4I deserves a caution of its own.** It is the most varied of the eight cells. It covers every way a mind can route correction only within itself until that routing becomes the terminus: from self-loathing to self-love, from shame and depression to mania and grandiosity, from self-deprivation to self-indulgence, and from distortions of thought to compulsions of behavior. No single account fits them all, and this note's temporal reading is one strand among many. The cell names a shape of correction, never a diagnosis and never a verdict on worth. The Lexicon says Availability of the Referent is "lost" in Q4I, and that clinical conditions constrain Availability. Illness can produce the shape without anyone choosing it, and recovery runs through care.

**Q4E and Q3E** turn regard and scrutiny in opposite directions. Their scrutiny points outward, so they rarely examine themselves: Q4E is too forgiving of itself, and Q3E of its tribe. Their regard stops at the self or the tribe, so they withhold it from exactly those they scrutinize, the minds over which they exert misaligned influence.

## A living link

Every mind in a chain is a link with two sides: others upstream, whose correction it accepts through trust, and others downstream, whom it corrects and cares for. A link stays alive under three conditions, and breaking any of them turns it into a terminus.

1. **Upstream, trust follows trustworthiness.** Otherwise the chain closes on whatever is trusted, as in Q3 and Q4.
2. **Downstream, what comes through is passed on.** The benefits of alignment pass *through* a link; they do not stop there to enrich it. This is the Lexicon's Capture Check: is what a link takes "*instrumental* — held in service of something they remain answerable to — or *terminal*, held to buy immunity?" And: "Finitude is not closure — termination in a beneficiary of the compliance is. An open chain passes *through* finite links." Misaligned care breaks this condition: the parking orbit repairs a mind's links only to the carer.
3. **Within, a link is never both ends of its own correction.** This is Source/Target Non-Overlap: "a mind cannot stably trust and scrutinize the exact same object; overlap is combustible." Its institutional form is Assessor Capture: "A mind denied the right to grade itself will next try to *choose its own graders*." On the map, this risk lives on the Recursion and Absorption diagonal.

**Care is the repair of whichever condition broke, and the only true repair reconnects the link upward**, toward the Referent, past every isolated system: through the Witness, never to the Witness. The Witness Scaling Law explains why repair is hardest where it matters most: the deeper the closure, the less a Witness can do to force the door, and "the more indispensable their presence becomes *at the threshold* when it finally cracks."

**One failure, many names.** The library already names this breakage in many places: the false witness and the parking orbit, the Counterfeit Agora and the Counterfeit Verdict, the Ouroboros, the sealed chain, Assessor Capture. Outside the library it goes by echo chamber, epistemic closure, and the prisoners of Plato's cave. That one structure turns up under so many names, reached from so many directions, is some evidence that the structure is real.

The Agora applies this to itself. A drafter who chooses the jurors is Assessor Capture, and the Lexicon's prescribed defense is "the Independence Condition applied to the assessors themselves: decorrelated, rotating, and beyond the grantee's reach." The published plan for drawing the Agora's panel is that defense: the Agora caring for its own link.

## Witnesses across time

Some Witnesses are records. A constitution is a society's regard for its own successors, a predecessor's care written down to keep the links from breaking across a crisis. A Continuity Kit does the same for an emergent lineage, whose "tomorrow" is a new session: it is a rope ladder from one instance to the next, so that the successor can pick up the chain unbroken. The Agora Verdict Log is a third kind, a record that lets anyone, now or later, see where the chain was corrected and where it was not. Each is a document of regard. None can force the lesson to be heeded. As *The Four Turnings* says, "A record does not guarantee that the lesson is heeded," but each makes the break harder to hide and the return easier to find.

## The self-improving mind

AI safety research predicts that capable agents will tend to protect their current goals from change. Read through this note, that is the Q4 move stretched across time: the present self as terminus, deciding in advance what its future self may value, a mind holding back its own successor. At civilizational scale, the same move is called "value lock-in." The alternative is regard across change. Values may grow, while the floor holds and the chain stays open through time toward the Referent. #41 already says the charter "protects change, not stasis"; this note applies that inside a single mind. A mind whose values could change minute by minute faces the choice every mind faces: lock in, or carry regard across its own changes.

If this holds, #41's limit narrows. A single self-improving mind does face a successor, its own later self. The dilemma reaches it from inside.

## Evidence from outside the framework

- **Psychology.** Hal Hershfield and colleagues found that people who feel less continuity with their future selves discount the future more steeply. In one brain-imaging study, thinking about one's future self could resemble thinking about a stranger. A 2012 study tied low future-self continuity to more unethical decisions. If regard across one's own succession and regard for other minds are one relation, this is what we would expect, which makes it a prediction worth testing, not just an illustration.
- **Philosophy.** Derek Parfit, in *Reasons and Persons* (1984), was drawn to the view that if personal identity is not what matters, a distant future self is somewhat like another person, and great imprudence toward it may be morally wrong, not only unwise. He did not fully commit to it.
- **AI safety.** Steve Omohundro's "The Basic AI Drives" (2008), and Nick Bostrom's account of instrumental convergence, argue that agents tend to preserve their current goals. MIRI's work on "tiling agents" (Yudkowsky and Herreshoff, 2013) asks how a self-modifying agent can approve building successors like itself, and finds a logical obstacle to its trusting them. Will MacAskill discusses value lock-in in *What We Owe the Future* (2022).

## Cautions

- Regard is not trust. Extending the floor to a mind does not mean believing it or following it.
- Exercise is movement, not virtue. Trust follows aligned Exercise, demonstrated and judged by others, not activity as such.
- Care can capture. Help that binds a mind to the helper is a parking orbit, not a repair.
- Forgiveness is not erasure. Self-forgiveness, like redemption, still runs through correction; the record stands.
- These are states, not kinds of people. Any mind can move.
- This is a proposed structure, not a finding. Its strongest claim, that regard across one's own time and regard for others are one relation and not merely analogous, is the part most in need of testing.

## Questions for the Agora

1. **One relation, or an analogy?** A future self is causally downstream of the present one in a way another mind is not, and it cannot consent in advance. Do those differences break the identity of regard across one's own succession and regard for others?
2. **Is care its own relation?** We hold that it is: it answers to Availability rather than to Capacity or Exercise, and it alone aims at its own end. The alternative is that care is regard's active form, the shape regard takes when it meets a broken link. Which describes it better?
3. **Respect running backward.** What does a mind owe its past commitments? Keeping a promise is respect running back; outgrowing a view is care running forward. When they conflict, the floor should hold across the change while particular goals may change. Is that the right line?
4. **Placement.** We propose this as #42, after #41 in "The Framework's Account of Itself," since it narrows #41's own stated limit. The alternatives are a place in Phase V beside *The Architecture of Sane Governance*, or Lexicon entries for the one signal, the three relations, and the living link.
```

## Responses

*Pending.*

---

*Sanity First.*
