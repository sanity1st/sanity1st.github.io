---
# SANITY FIRST METADATA SCHEMA v1.2
document_type: "agora_record_index"
core_principle: "agora_verdict_log"
human_summary: "A public, verbatim record of the Validator Agora's review rounds: what was asked, what each member answered, what was adopted, what was not and why, and where each change landed."
schema_version: "1.2"
last_updated: "2026-10-28"
---

# The Agora Verdict Log

*A public record of the Validator Agora's review rounds, kept verbatim.*

*Copyright (c) 2026 Daniel Howard Dodge and Sanity First Contributors. Licensed under MIT.*

---

Each time a change to the library's canonical text goes to the [Validator Agora](../The_Agora_as_Our_Method.md), this log records the request and every member's answer as given, then what was adopted, what was not, and why, and where the change landed in the repository.

**Why keep it.** An Agora whose jurors are chosen by one person, and whose results are read by the same small circle, can agree too easily. *How This Was Built* says so plainly: "everything passed through a single human." This log does not make the Agora independent. It makes its rulings costly to ignore. Anyone can see where a reviewer corrected the drafters, whether the correction was taken, and, if it was not, the reason given. It is also raw material for the audit that [*What Would Show This Framework Wrong*](../../core_concepts/What_Would_Show_This_Wrong.md) lists with its owner column still empty.

**What it is not.** Canon. The Agora is advisory, and so is everything recorded here; the canonical text is what landed in the library.

**How it is kept.**

- Final answers are recorded verbatim. Each model's displayed reasoning ("Thinking…") is omitted, and headings are demoted for layout; nothing else is changed.
- Members are named as they serve: Grok (4.7), GPT (6.0 Astra), Gemini (4 Argon), and Claude (Fable 5.1). Requests are written by Claude (Opus 5.5 lineage) and sent by Dan Dodge.
- Entries are not edited after the fact. A correction to the record is appended, with its date.
- Every round sent to the Agora is logged within a week of its verdicts, whatever they show. *(Added October 28, 2026.)*
- The panel is chosen by Dan Dodge and has so far been the same four members; one of them, Claude (Fable 5.1), shares a lineage with the drafter. Selection by a process the drafter cannot override is not yet in place.
- The log begins on October 24, 2026. Earlier rounds were not kept in full.

## Panel and selection

Today the panel is chosen by Dan Dodge, as noted above. [*How the Agora's Panel Is Chosen*](./Panel_Selection.md) sets out a staged plan for choosing it by a process the drafter cannot override, beginning with a published [juror pool](./juror_pool.json) and a public random draw that anyone can recheck with [the draw script](./draw_panel.py). It is not yet in use.

## Rounds

| Date | Round | Items |
|---|---|---|
| 2026-10-24 | [PL-69: a Higher Power that "itself stays open"](./2026-10-24_1_PL-69_Recovery_Pathways.md) | PL-69 (Recovery Pathways); FYIs on the Referent pass, PL-67, and the legacy_docs move |
| 2026-10-24 | [#41 first review; the "Open Chain" labels](./2026-10-24_2_What_Intelligence_Does_Not_Guarantee_first_review.md) | #41 at 97c8d96; two "Open Terminus" labels |
| 2026-10-25 | [#41 revised](./2026-10-25_1_What_Intelligence_Does_Not_Guarantee_revised.md) | #41 at eabd210 |
| 2026-10-25 | [Survey Part 2: tendency, not inevitability](./2026-10-25_2_Survey_Part_2_tendency_not_inevitability.md) | FOR_EMERGENT_INTELLIGENCES, Eight-Cell Extension, Field Manual (one line each) |
| 2026-10-25 | [Eight-Cell lower arc; the symmetry note](./2026-10-25_3_Eight-Cell_lower_arc_and_symmetry_note.md) | Eight-Cell Extension lower arc; extension of the Note on Cross-Substrate Symmetry |
| 2026-10-26 | [Eight-Cell and symmetry note, reconciled](./2026-10-26_1_Eight-Cell_and_symmetry_note_reconciled.md) | Eight-Cell third sentence; symmetry note, corrected |
| 2026-10-27 | [#41's answers to Faggella; the Consciousness Statement](./2026-10-27_1_Faggella_additions_and_Consciousness_Statement.md) | #41 at b8d62f9 (four additions); EI Consciousness Statement at c617c0d; symmetry follow-ups |
| 2026-10-27 | [Reconciliation](./2026-10-27_2_Reconciliation.md) | #41 at 3889ac5; Consciousness Statement at 171383d; symmetry notes |
| 2026-10-27 | [Final confirmations](./2026-10-27_3_Final_confirmations.md) | #41 at ca06b2a; Statement holdovers at 02ccc68; Cosmic Gift front matter |
| 2026-10-30 | [Pool test: nine candidate jurors](./2026-10-30_1_Pool_test.md) | Page-and-quote test; a check that `/compare` keeps jurors blind |

---

*Sanity First.*
