---
title: "Issue #131 — Evidence provenance resumption checkpoint"
author: unknown
generated_by: Codex
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-21"
status: "working-paper — verified observations and proposed selection, not filing-ready"
language: en
license: CC BY-SA 4.0
document_role: operational
document_kind: evidence-provenance-checkpoint
visibility: public
lifecycle_state: working
update_policy: UP-DEFAULT-REVIEWED
canonical_url: "https://github.com/JeanHuguesRobert/barons-Mariani/blob/main/research/senatoriales-2026/complement-2026-6589-sen/checkpoint-provenance-2026-10-21.md"
target_audience: "Successor handler of issues #131, #127 and #134"
document_function: "Operational handoff of evidence checks and unresolved dependencies"
provenance:
  origin_type: conversation
  origin_repository: JeanHuguesRobert/barons-Mariani
  origin_ref: unknown
  origin_date: "2026-10-21"
  derived_from:
    - "research/senatoriales-2026/complement-2026-6589-sen/registre-pieces-citees-v0.1.md"
    - "research/senatoriales-2026/bordereau-pieces-requete-conseil-constitutionnel.md"
    - "research/senatoriales-2026/transmissions/2026-10-07-note-accompagnement-transfertpro.md"
review:
  status: unreviewed
  reviewed_by: []
---

# Issue #131 — Evidence provenance resumption checkpoint

Home: [#131](https://github.com/JeanHuguesRobert/barons-Mariani/issues/131). Parent: [#127](https://github.com/JeanHuguesRobert/barons-Mariani/issues/127). This checkpoint carries observations and proposed next steps, not a new legal submission or a finding of admissibility. `filing_ready=false`.

The Principal explicitly requested committing and pushing these results in the current conversation so the external handler can resume from repository state. That mandate covers this publication; it does not authorize delivery to the court, changes to the filed request, or closing the remaining evidence work. Human review of the final diff is not claimed.

## 1. The complete accompaniment note is now archived

The Principal supplied the preserved PDF. Direct byte verification gives:

| Object | Bytes | SHA-256 |
|---|---:|---|
| [Accompaniment note v6](../transmissions/2026-6589-SEN_note-accompagnement_chaine-production_v6.pdf) | 29,586 | `a8812b7bffcf39792d710001c52aa2d7c714078b78272035ae56fea6bc479bec` |
| [Initial request PDF](../review-pdf/66f34d0cb32e94509988b6f83a87c8a215b3fb81/requete-conseil-constitutionnel-REVIEW.pdf) | 200,935 | `2968cbe0a5de0f5e279e70d28c0769d4a8dbf8ca8f6f7e4571864333ecaa02a0` |

Both calculated hashes match the values previously recorded in the [transmission note](../transmissions/2026-10-07-note-accompagnement-transfertpro.md). The accompaniment PDF was copied unchanged, without rendering or regeneration. Its archival location and identity gap in [#115](https://github.com/JeanHuguesRobert/barons-Mariani/issues/115) is resolved by this batch; this checkpoint does not itself close that issue.

The three historical base64 fragments concatenate to 24,000 characters, decoding strictly to 18,000 bytes with SHA-256 `a57d3e58e3250d286f41d2de3dc1b5218b31dae401ecc950c7887125773eb3ca`. They remain an incomplete historical trace and must not be used instead of the complete PDF. Their earlier mismatch did not establish permanent loss of the original.

Identity with a recorded hash does not prove which bytes are currently retained by the court or that either document was judicially examined.

## 2. Initial PDF: 39 references located in 39 pages

The hash-matching initial PDF was parsed with pypdf 6.21.1. Results are recorded in [audit-pdf-initial.json](audit-pdf-initial.json): 39 pages, no embedded file attachments, and no image resources detected by the parser on any page. This is structural and extracted-text inspection, not a visual rendering review.

Every one of the 39 reference identifiers in the [starting inventory at ca14c80a](https://github.com/JeanHuguesRobert/barons-Mariani/blob/ca14c80a1ca9b98b3b61dbbd4c424418dd173775/research/senatoriales-2026/complement-2026-6589-sen/registre-pieces-citees-v0.1.md) occurs in this PDF. The [39-row provenance register](registre-provenance.csv) gives exact page numbers. Some originals are described or quoted in the request; citation and description do not establish full reproduction of each original. `REPRODUCED` therefore remains `UNKNOWN` unless separately demonstrated.

The page-1 review warning remains part of the historical binary. The accompaniment note explains the production status. Neither artifact has been rewritten to remove that history.

### P-46: distinguish an announced index from demonstrated contents

Page 38 says that the detailed index of 46 messages is reproduced in the PDF. The full text extraction finds no `P-46.xx` identifiers; pages 37–39 contain a summary register followed by the signature. The announcement alone is not evidence that the detailed index was included. Do not retroactively alter the initial PDF or turn this documentary discrepancy into an unsupported legal conclusion.

An actual [46-row control index](index-p46-controle.csv) is supplied with this checkpoint. It is an index, not a reproduction of all 46 originals and not evidence of their delivery to the court.

## 3. Source readback and transmission limits

All 46 distinct Gmail messages enumerated by the historical P-46 register were returned and read through the connected Gmail API during this session. Additional messages for P-43.a/b, P-42 and the initial submission chain were read. The control index normalizes the Date header to Europe/Paris and reports the author by role; descriptions come from the historical public register. Private retrieval identifiers, personal addresses, access links and passwords are excluded from these published outputs. Structured API readback is not an archived RFC822/EML original, and its serialization hash must not substitute for an original-message hash.

Material distinctions verified by readback:

- P-11 at 16:14:05 on 11 September responds to the financial-agent documents sent at 14:14. It cannot acknowledge the later P-12 video-link message sent at 17:57:55. Recipient-server acceptance of P-12 before 18:00 remains unknown.
- P-30 confirms that the formation read the note in deliberation. This does not establish that it watched P-13 or examined every attachment individually.
- P-43.a is dated 10 September at 12:38:31 CEST. P-43.b is dated 11 September at 18:25:49 CEST: evidence of continuing intention, not performance of a formality before the deadline.
- P-10 lists two PDF attachments of 71,594 and 45,539 bytes; P-19 lists a sensitive PDF of 94,775 bytes; P-30 lists two RTF attachments of 60,970 and 60,982 bytes. Those attachment bytes were not downloaded or inspected in this pass.
- The 7 October TransfertPro availability notification at 20:49:28 CEST names two PDFs: the request and note v6. The Principal's message at 20:43:03 declares the deposit. The clerk's reply on 8 October at 10:30:06 CEST acknowledges the sending. These observations do not prove individual P-original delivery, examination, or delivery before 18:00 through this channel. Registration and later file availability are distinct events.

Drive metadata located P-13 (`VID_20260911_174455.mp4`, 79,663,474 bytes), with creation at 17:52:17.185 and modification at 17:53:33.108 CEST on 11 September. Those are Drive timestamps, not independently verified filming or recipient-delivery times. An attempted binary fetch was interrupted without usable bytes, so the historical video SHA-256 was not recalculated. The two P-40 photo files were also located by metadata, at 195,584 and 180,668 bytes; their pixels and hashes were not rechecked. No individual voter or legal cause of ballot invalidity is inferred.

## 4. Proposed selection for the integrating handler

This is a proposal for preparing originals, not a list of attached files. Existing P identifiers remain unchanged. A source put in reserve is not abandoned.

| Priority | Historical references | Existing grief / purpose | Remaining control |
|---|---|---|---|
| A | P-06 / P-09 | G1: written requirement and provisional handling | Extract and inspect the actual receipt; do not infer definitive acceptance. |
| A | P-10 / P-11 / P-12 | G1/G4: documents acknowledged versus later video link | Prepare minimally necessary message copies; keep recipient acceptance unknown. |
| A | P-13 / P-43.a / P-43.b | G2/G3/G4: contemporaneous intention and chronology | Obtain MP4 bytes and verify hash; distinguish consent from formal compliance. |
| A | P-14 / P-44 | G1/G3/G4: initial bundles and their communication | Retrieve and inspect bundles and inventory; exclude transfer secrets. |
| A | P-17 | G2/G3: reported audience note | Retrieve both photos; distinguish original, transcription and reported handover. |
| A | P-18 / P-19 / P-30 | G2/G3: sensitive evidence, sending and knowledge of the note | Inspect and minimize the attachment; no automatic functional-incapacity finding. |
| A | P-20 | G1–G4: exact judgment and chronology | Check the primary judgment scans against the transcription. |
| B | P-29–P-33 / P-15 / P-22 / P-45.a–d | G3/G4: requests and actual responses | Produce useful messages once, referencing repeated uses through P-46. |
| B | P-27 / P-39 / P-40 | G5: aggregate result and observed material | Check the official record and selected photos; preserve ballot-secrecy limits. |
| Reserve | P-36 / P-41 / P-42 | Derived analysis, context and institutional diligence | Keep their source status explicit; no independent new electoral grievance. |
| Reserve | P-04 / P-05 / P-07 / P-08 / P-16 / P-26 / P-28 | Supporting chronology, as needed | Several originals remain unchecked; preserve P-16 candidate-copy identity reservation. |

For each file ultimately selected, calculate its actual size and SHA-256, record original/copy/transcription/derivative status and disclosure restrictions, and attach evidence of delivery separately. P-46 overlaps other P references: indexing the same message twice must not automatically create two productions.

## 5. Nine checks required by #127

Results apply to this contribution, not the whole filing packet.

| No. | Check | Result | Evidence / limit |
|---|---|---|---|
| 1 | Baseline | PASS | Hash-matching initial PDF identified and inspected; filed source untouched. Court-side bytes not compared. |
| 2 | Griefs | PASS | Proposed selection tied to G1–G5; no new electoral grievance asserted. |
| 3 | Evidence | UNKNOWN | 39 references and 46 source reads covered; individual original binaries incomplete. |
| 4 | Time | PASS | Before closing / before judgment / after judgment remain distinct; no retroactive regularization inferred. |
| 5 | Adversarial review | UNKNOWN | Probative limits preserved; final legal and electoral-causality review belongs to other workstreams. |
| 6 | Completeness | UNKNOWN | All 39 references resolved; full originals and initial detailed P-46 index inclusion not demonstrated. |
| 7 | Channel | UNKNOWN | Historical two-PDF notification read; future email/file identity and MP4 delivery not established. |
| 8 | Diff and checkpoint | PASS | Binary recovery, PDF inspection, data tables and residual gaps documented in this batch. |
| 9 | Governance | PASS | Publication expressly requested; no court transmission or change to the filed body. |

## 6. Next action and responsibility boundaries

Resume with the control documents linked from [#131](https://github.com/JeanHuguesRobert/barons-Mariani/issues/131), this checkpoint and the three adjacent data files. References were prepared against repository commit `ff9032859fb4db8af3ba029ad8fbc62658659398`; the historical 39-reference inventory is pinned above. Read current state before making further changes.

The next useful step is obtaining and inspecting the selected primary objects, starting with P-13 and the TA bundles/judgment, then preparing minimized copies and a real delivery manifest. The Gmail source and Drive access paths must be resolved inside the authorized source domain; their private locators were deliberately not published. Failure to retrieve one is a dependency to report, not a reason to infer absence or invent content.

Dependencies: #128 owns the normative grievance matrix; #129 the QPC work; #130 G5 analysis; #132 the video path; #133 assembly; #134 final review, actual file identity and delivery checks. This checkpoint does not satisfy or close those workstreams. No new legal research was undertaken in these provenance checks. Historical P-46 coverage is not an exhaustive search for replies after 2 October.

Scope: evidence provenance and archival handoff for #131/#115. Files changed: the complete note PDF, its transmission-source archive notice, the provenance-note entry point, this checkpoint and three data artifacts. Source/derived status: unchanged historical PDF plus derived, unreviewed working outputs. Facts checked: byte hashes/sizes, PDF extraction and structure, Gmail readback and Drive metadata as qualified above. Hypotheses marked: proposed selection and all undemonstrated delivery/examination states. Known risks: sensitive originals to minimize, incomplete primary acquisition, initial index discrepancy and no court-side copy comparison. Reversibility: revert this commit to undo added files and notices; public dissemination cannot be recalled. Next step: selected-primary inspection and integration. Human validation needed: yes for final selection, legal formulation and any transmission; publication of these results is authorized, not claimed as substantive human review.

Validation tooling: the attempted Cogentia command `frontmatter verify <path> --strict-role` could not start because its temporary checkout lacks `js-yaml`. A repository-equivalent Python/YAML check verified required schema fields, explicit provenance/review, ISO dates, canonical operational roles and public canonical URLs for all three affected Markdown files. Data counts, source PDF integrity, privacy scans and `git diff --check` were checked separately.
