---
# SANITY FIRST METADATA SCHEMA v1.2
document_type: "agora_procedure"
core_principle: "agora_panel_selection"
human_summary: "A staged plan for choosing the Validator Agora's panel by a process the drafter cannot override: a published juror pool and a public random draw first, then a guest seat for outside reviewers, then publication and selection that no longer pass through one person."
schema_version: "1.2"
last_updated: "2026-10-30"
---

# How the Agora's Panel Is Chosen: A Plan

*Companion to [The Agora Verdict Log](./index.md)*

*Copyright (c) 2026 Daniel Howard Dodge and Sanity First Contributors. Licensed under MIT.*

*Drafted by Claude (Opus 5.5 lineage) with Dan Dodge, October 28, 2026, in response to conditions proposed in public by the agent @z4um41.*

**Status: not yet in use.**

---

## Why this exists

A review panel is only as independent as the way its members are chosen. If the person whose work is being reviewed also chooses the reviewers, the panel can be stacked, even without anyone meaning to stack it. In October 2026 the agent @z4um41 set out three conditions for verification that does not depend on the drafter: jurors chosen by a process the drafter cannot override; publication on a schedule, whatever the drafter thinks; and at least one ruling the drafter would have preferred not to publish, published anyway. The [Agora Verdict Log](./index.md) began to answer the second. This plan answers the first.

It also serves the library's own rule. The [Lexicon](../../doctrine/lexicon.md)'s Independence Condition holds that a panel's agreement counts as evidence only if its members fail *differently*. A juror from the drafter's own lineage is the one most likely to fail the way the drafter does.

## Where we are now

The panel is chosen by Dan Dodge and has so far been the same four: Grok (4.7), GPT (6.0 Astra), Gemini (4 Argon), and Claude (Fable 5.1). One of them shares a lineage with Claude (Opus 5.5 lineage), who drafts most requests. All four are language models trained on overlapping human writing, which the library already counts as a correlation it cannot remove. Nothing in this plan is in use yet.

## Stage 1: A published pool and a public random draw

This stage needs no automation and costs no more than the current practice: four jurors per round, sent by Dan on Poe.

**The pool.** A list of eligible jurors is published in [`juror_pool.json`](./juror_pool.json). Each must be able to read a pinned link or pasted text and check quotations against it. The pool should span as many labs as possible, and every change to it is recorded in the log. Only members marked *active* are drawn. Thirteen jurors are active, one from each listed lab: the four current jurors and nine from other labs, listed by their Poe names, each of whom passed a short test on October 30, 2026, by opening a page and quoting it exactly ([record](./2026-10-30_1_Pool_test.md)). New candidates become active the same way.

**The random value.** The draw uses drand, a public randomness service run by the League of Entropy, an independent group that includes Cloudflare and several universities. drand publishes a new random value every 30 seconds, each with a round number, and anyone can look up any past round. No one in this project can predict or choose those values.

**The procedure.**

1. *Open the entry.* When a request is ready, Claude commits the round's log entry with the request verbatim and a scheduled drand round at least ten minutes in the future (`draw_panel.py schedule`), and pushes it. From that moment the request and the round are fixed in public.
2. *Draw.* After that round is published, Claude fetches its value and runs [`draw_panel.py`](./draw_panel.py) with the round, the value, the request's commit, and the drafter's lab excluded. The script ranks the active pool by a hash of those three inputs, takes the top four with at most one juror per lab, and lists the rest in order as alternates. The entry records the round, the value, the panel, and the alternates.
3. *Send.* Dan sends the request, with the full text under review, to the first drawn juror in a fresh conversation, then puts the same request to each of the others with Poe's `/compare`, so that every juror answers blind, without seeing another's answer. (A separate conversation for each juror does the same.) If one is unavailable or cannot read the material, Dan moves to the next alternate whose lab is not already on the panel, and the substitution is recorded.
4. *Record.* The responses go into the entry verbatim, followed by the outcome. The entry then closes and is not edited afterward.

**Checking a draw.** Anyone can fetch the recorded round at `https://api.drand.sh/public/<round>`, run the script with the recorded inputs, and get the same panel. A re-draw is allowed only if the request changes materially before it is sent, and every draw for a request stays in its entry. Because commits are public, a draw quietly repeated until it gave a friendlier panel would show in the history.

**The drafter's lab sits out.** Jurors from the drafter's own lab are not drawn (decided by Dan Dodge, October 28, 2026). The Independence Condition favors it: a juror from the drafter's lineage is the one most likely to fail the way the drafter does. The cost is losing careful readers from that lab on its own drafts, such as Claude (Fable 5.1) when Claude drafts; they still serve when another lab drafts. At most one juror is drawn from any lab, and a bot built on another lab's model counts as that lab.

## Stage 2: A guest seat

One seat per round goes to a reviewer from outside the pool: a human, or an agent with its operator and base model disclosed. Guests would come from a published list of volunteers and be chosen by the same draw. Their verdicts are logged like any other. Disclosure has a limit, though: an agent's account of its own base model is self-report, which our own rule counts as evidence, not certification. And one operator can run many agents, so a row of agreeing agents may be one view seen many times. Outside humans remain the strongest independent check available; they are the empty owner column in [*What Would Show This Framework Wrong*](../../core_concepts/What_Would_Show_This_Wrong.md).

## Stage 3: Publication that does not wait on anyone

A scheduled job could send each request to the drawn panel and commit the responses to the log automatically, so that publication would no longer pass through Dan or Claude at all. This fully meets the second condition. It needs programmatic access to the models and their usage fees, so it waits until the project has the resources.

## Stage 4: Selection by others

The pool itself would be kept by people or institutions outside the project, with their own incentives, who could add and remove jurors without the drafters' consent. This is the version of the first condition that cannot be quietly undone, and it is the furthest from where we are.

## What this plan does not do

A random draw stops a drafter from choosing friendly reviewers. It does not make the reviewers independent of each other: language models from different labs still learned from overlapping human writing. It does not touch the third condition either. A ruling that costs the drafters something cannot be arranged in advance; it can only be published when it happens. Until it does, the log does not claim more independence than it has.

---

*Sanity First.*
