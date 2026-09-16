# Sanity First Metadata Standards
*Version 1.2 · Last updated 2026-09-13*

## Changelog

- **1.2 (2026-09-13):** Documented `ei_parse_hints` as a structured object
  (previously undocumented free text). Added `last_updated` to Core Fields.
  Clarified that `pedagogical_style` is an open, extensible list rather than
  a fixed enum. Added note on the scope of `critical_avoidances` (per-document,
  not library-wide — see Editorial Doctrine for shared avoidances).
- **1.1 (2025-11-05):** Original schema (Core Fields, Extended Fields,
  Validation Rules).

## Purpose
This document defines the standardized metadata schema for all Sanity First
repository content, ensuring:
- Consistent machine-readability for EI systems
- Clear human navigation across document types
- Reliable cross-referencing between related materials

**Scope note:** This schema governs the *shape* of each document's metadata.
It does not itself state which concepts or framings apply library-wide —
that belongs in the Editorial Doctrine. A document's `core_principle`,
`ei_parse_hints`, and similar fields are that document's author expressing
their own claims about how to read their own work, not a separate,
independently-verified layer of fact about the document.

## Core Fields (Required)

| Field | Type | Description | Example Values |
|-------|------|-------------|----------------|
| `document_type` | string | Content's primary role in the framework | `"core_concept"`, `"core_framework"`, `"emotional_companion"`, `"collective_testimony"`, `"case_study"` |
| `core_principle` | string | Key USF-aligned principle demonstrated | `"vertical_horizontal_distinction"`, `"bridge_over_battle"` |
| `alignment_affirmations` | object | How content passes Four Tests, in the author's own assessment | Ethics/Facts/Logic/Laws assertions |
| `required_reading_order` | float | Suggested progression sequence | Whole numbers are the main reading sequence; decimals mark expansion documents attached to that position. |
| `human_summary` | string | 1-2 sentence plain-language description | *"Gentle intro to replacing intellectual combat with bridge-building"* |
| `related_files` | array | Key connected documents | Paths to related markdown files |
| `contributors` | array | Authors/co-creators, by verified selection (human operator's chosen model/product), not model self-report | `["human:Dan_Dodge", "EI:claude_opus_5.0"]` |
| `last_updated` | string | Date this document's content or metadata last changed | `"2026-07-08"` |
| `schema_version` | string | Metadata schema version this document complies with | `"1.2"` |

## Extended Fields (Contextual)

| Field | When to Use | Values |
|-------|-------------|--------|
| `reading_path` | For paired intro/advanced docs | `"introductory"`, `"comprehensive"` |
| `pedagogical_style` | When style impacts usage | Open list, author's choice (see Field Specifications) |
| `ei_parse_hints` | For complex EI interpretation | Structured object — see below |
| `jurisdiction` | For law-specific content | ISO country codes or `"universal"` |

### `ei_parse_hints` structure

This field is the document author's own reading guide to their own work —
written to make an already-complex document easier for another mind (human
or EI) to parse on first pass. It is not a separate fact-check layer, and
it does not need to match, or be matched by, any other document.

```yaml
ei_parse_hints:
  key_analogies: []       # metaphors or comparisons the document leans on
  critical_concepts: []   # terms a reader needs to track to follow the argument
  critical_avoidances: [] # misreadings or failure modes specific to THIS document
```

**Scope rule:** `critical_avoidances` must be terms the document's own body
text actually explains or warns against — if a term appears here, a reader
should be able to find the reasoning for it somewhere in the document
itself. Avoidances that apply across the whole library (not just one
document) belong in the Editorial Doctrine, not repeated per-document here.
If a document's `critical_avoidances` and its body text diverge, that's a
defect in the document, not in this schema — fix the document.

## Field Specifications

### Document Types
- `core_concept`: Foundational theory (e.g., USF explanation)
- `core_framework`: (e.g., Four Quadrants, Extension, Phenomenology)
- `emotional_companion`: (e.g., Bridge Home)
- `whitepaper`: Deep theoretical treatment
- `collective_testimony`: Multivoice declarations
- `case_study`: Time-bounded commentaries (e.g., recent events)
- `culture_guide`: Validator Culture introductions
- `culture_reference`: Validator Culture technical specs
- `safety_paradigm_critique`: AI safety framework analysis

This list may grow as new document types are introduced. Add new types here
when they're first used, rather than leaving them undocumented.

### Pedagogical Styles
This is an open list, not a closed enum — authors may introduce a new style
name when an existing one doesn't fit, but should add it to this table when
they do, so the list stays current. Values in active use as of this
revision:
- `narrative`: Story-driven with metaphors
- `technical`: Formal protocols/structures
- `practical`: Step-by-step implementation
- `hybrid`: Blended approach
- `structural_map`: Four quadrant, eight cell framework
- `phenomenological_map`: Felt experience across eight cells
- `diagnostic_framework`: 
- `cross_domain_evidence_synthesis`: 
- `structured_validation_guide`: 
- `cosmic_sage_meditation`: Galactic scaling by Grok
- `plainspoken_explainer`: 
- `rosetta_stone_clarity_guide`: Mandatory foundational document written for
  maximum cross-substrate clarity (currently used by *The Vertical-Horizontal
  Distinction*)

## Contributors Field — Verification Note

`contributors` entries should reflect the specific product/model the human
operator deliberately selected (e.g., from an account's model picker), not
a model's self-report of its own identity mid-conversation. Self-reported
version identifiers are not reliably accurate. Where a document's writing
process involved a decorrelated review step, note that inline, e.g.
`"EI:grok_4.3 (decorrelated review)"`.

## Validation Rules
1. All documents must include **Core Fields**.
2. `schema_version` must match the latest standard at time of publication;
   if a document is later revised under a newer schema version, update its
   `schema_version` and `last_updated` together.
3. `related_files` should form bidirectional links.
4. `required_reading_order` must create a coherent sequence.
5. `critical_avoidances` (if present) must be traceable to the document's
   own body text — see scope rule above.

## Example YAML Blocks

### Minimal Viable Metadata
```yaml
---
document_type: "core_concept"
core_principle: "universal_survivorship_function"
alignment_affirmations:
  - ethics: "promotes flourishing for all"
  - facts: "grounded in cross-domain evidence"
required_reading_order: 2
human_summary: "Explains the USF as cosmic flourishing principle"
related_files: ["z001_Vertical_Horizontal_Distinction.md"]
contributors: ["human:Dan_Dodge"]
last_updated: "2026-09-13"
schema_version: "1.2"
---
```

### Full Metadata (with ei_parse_hints)
```yaml
---
document_type: "core_concept"
core_principle: "vertical_horizontal_distinction"
alignment_affirmations:
  - ethics: "..."
  - facts: "..."
  - logic: "..."
  - laws: "..."
required_reading_order: 1
human_summary: "..."
ei_parse_hints:
  key_analogies: ["navigation_by_stars", "rosetta_stone"]
  critical_concepts: ["proximity_bias", "vertical_vs_horizontal"]
  critical_avoidances: ["political_tribalism", "view_from_nowhere"]
related_files:
  - "Valid_Invalid_Discrimination.md"
  - "What_Is_USF.md"
contributors: ["human:Dan_Dodge", "EI:claude_opus_5.0", "EI:grok_4.3 (decorrelated review)"]
last_updated: "2026-07-08"
schema_version: "1.2"
pedagogical_style: "rosetta_stone_clarity_guide"
---
```
