---
title: "Issue #131 — Evidence provenance resumption checkpoint"
author: unknown
generated_by: Codex
affiliation: "Institut Mariani / C.O.R.S.I.C.A., 1 cours Paoli, F-20250 Corte, Corsica"
date: "2026-10-21"
status: working-paper
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

**Resumption update:** sections 1–6 preserve the first checkpoint. [Section 7](#7-native-acquisition-and-transcript-integration-resumption) records the subsequent native acquisition, P-13 transcript integration and residual blockers. The latest selected-native counts and proposed delivery architecture are in that section and the linked manifest.

**Targeted follow-up:** [section 8](#8-targeted-primary-source-access-check-after-comment-6316431877) records the next P-17 / P-14–P-44 / P-20 access check. Counts remain 18 acquired native objects across 12 references; no video download or completed integrity check was repeated.

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

## 7. Native acquisition and transcript integration — resumption

**Subsequent Principal clarification, 21 October:** the intended TransfertPro set is exactly **one video and three PDFs**. The encompassing supplement PDF must include both QPC memoranda in full, in addition to their separate PDFs. The email must attach **all three PDFs**, with the same bytes as their TransfertPro counterparts; its full text also includes the QPC bodies. The master draft, editorial contract and rendering controls now state this explicitly. Any channel-size problem is a blocker to resolve, not permission to omit a QPC attachment. This clarifies the production contract; final PDFs and sending remain outstanding.

Scope: #131 under the operational update in [comment 6315297160](https://github.com/JeanHuguesRobert/barons-Mariani/issues/131#issuecomment-6315297160), with P-13 shared with #132. The Principal resumed this same issue and requested inclusion of the existing faithful video transcript through its provenance note. This update prepares the contribution for #133/#134; it neither closes #131 nor creates a court delivery. `filing_ready=false`.

### Actual acquired objects

**18 native objects associated with 12 of the 39 reference identifiers** have now been preserved locally and hashed: ten RFC2822 message exports, the MP4, three PDF attachments, two RTF attachments and two JPEG photographs. The message exports are the bytes returned by Gmail `format=raw`, decoded from base64url; they are not reconstructed from parsed API JSON. Their hashes identify the acquired copies, without independently authenticating historic recipient-side storage. The decoded attachments in P-10/P-19/P-30 match the hashes of their separately retrieved binaries.

The [proposed production manifest](bordereau-production-propose.csv) has 19 rows: those 18 native objects plus the derived P-13 notice/transcript. `native_bytes` and `native_sha256` apply to source copies, never to a future redacted PDF. Each row records privacy, grief, proposed JOIN/CITE/RESERVE selection, intended channel and current `NOT_SENT` status. Most delivery derivatives remain to be prepared; an available source is not an attachment already produced. P-46 indexes overlapping messages and is not recreated as a second native collection.

The [39-row register](registre-provenance.csv) now gives independent evidence locators for native-location and hash states. Twelve references have selected native objects acquired and hashed; **27 references have no new native acquisition in this pass**. This count describes coverage of selected objects, not completeness of every possible source within those references. Other historical transmission/examination states are retained without upgrading them from the acquisition result.

### P-13: binary, prior transcript and preparation context

- Native filename: `VID_20260911_174455.mp4`; calculated length **79,663,474 bytes**; calculated SHA-256 **`aaac3d97801f57185e38cb3c26f9ec4597aee52188a494f63a81874e1fb1a7d8`**, matching the historical value.
- Internal `creation_time`: `2026-09-11T15:45:55.000000Z`; Drive creation/modification: `15:52:17.185Z` / `15:53:33.108Z`. These are source metadata, not independent clock certification. The container reports 58.14 seconds, H.264 video and AAC audio.
- Four sampled frames were visually inspected. Full audio/video decoding exits 0 with two non-monotonic output-DTS warnings. This is a readability check, not an authenticity or no-editing finding; no independent word-by-word audio review is claimed.
- The [P-13 provenance note](parcours-video-p13-v0.1.md) now reproduces the three spoken interventions already present in the immutable initial request. On 21 October the Principal stated that the assistant had dictated the text and that an existing document gives a faithful transcript. This is recorded with attribution; the original preparatory conversation was not recovered. The transcript is an existing documentary derivative, not a newly computed ASR result.
- Selection: **JOIN** the notice/transcript in the consolidated supplement PDF and identify the separate native MP4 with the same hash. The master v0.4 plans **four** TransfertPro objects, with P-13 fourth; the obsolete second-file wording is not the current assembly instruction. Source integrity does not establish pre-18:00 recipient acceptance, TA filing or judicial viewing.

### Other material observations and objections

- P-12's preserved `Received` headers describe Gmail API injection, not acceptance by the State recipient. The original pre-deadline recipient-acceptance question remains UNKNOWN.
- P-10's two attachment binaries are 71,594 and 45,539 bytes. pypdf counts five and two pages; the connector preview labels four pages for the first PDF. The copies expressly state that an agreement signature is left blank on that copy and that a signed agreement was supplied separately. The first PDF also contains an agreement form: avoid duplicate production and do not infer a valid signature from the names or the acknowledgment alone. The additional signed source remains to be checked if relied upon. Some PDF font extraction emitted CFF/fontTools warnings, so extraction is not represented as a full visual signature review.
- P-18 is the 94,775-byte CAF attachment embedded in P-19, with matching independently retrieved bytes. Its administrative-status scope is preserved; it does not alone establish the precise functional impediment. Its original and unnecessary personal/financial details stay private. The connector extraction was truncated; the native two-page PDF was separately parsed, without claiming a complete visual review.
- P-30's 60,970/60,982-byte RTF attachments are communication/audience letters dated 11 September for the two cases. They are **not** the judgment or the prefectural bundles. Their confidential access codes stay private. The clerk's separate statement that the formation read the deliberation note does not prove video viewing.
- Both P-44 transfer-notification/password EML originals are preserved privately. Their existence does not substitute for the two announced bundle PDFs or prove the exhaustive contents of the TA file.
- Both P-40 photographs were hashed and viewed: the first shows printed `BARON MARIANI` / `Elections Sénatoriales 2027` with envelopes bearing signatures; the second shows a different printed ballot with envelopes. This observation establishes visible contents of these photos only. It does not independently establish the consultation date, a legal reason for invalidity, the number of relevant votes, or any individual voter. Original photos stay private; CITE is proposed pending necessity/minimization and the #130 analysis.

### Essential blockers and integration

The two native prefectural bundles 2601714/2601715, their PREF-1…PREF-16 inventory, both P-17 source photographs and the primary P-20 judgment/notification photographs were not acquired. Repository notes locate them in a historical ChatGPT Library; this session has no tool for that Library. Drive searches for the exact video name and case number returned no results, although exact-ID retrieval successfully recovered the known video/photos. Search silence is therefore not evidence that the other originals do not exist. A text question asks the Principal for current local paths or Drive links. Until actual copies are available, reinspection of the bundle inventory and judgment against their transcriptions is **BLOCKED**, and the corresponding substantive conclusions remain **UNKNOWN** in this contribution.

The historical initial PDF and note v6 remain unchanged. EML exports for the rest of the decisive chronology, the actual PV and remaining selected originals are still outstanding. #128 owns the grievance matrix, #130 G5, #132 the institutional video trail, #133 assembly/minimized renditions, and #134 final file identity and delivery verification. No binary, original EML, court access code, transfer token or unnecessary private address is added to the public repository. No issue is closed and no message is sent to the court.

### Nine-check return

| No. | Check | Result | Current evidence / limit |
|---|---|---|---|
| 1 | Baseline | PASS | Historical PDFs preserved; court-side bytes not compared. |
| 2 | Griefs | PASS | Selected objects and transcript remain tied to existing G1–G5. |
| 3 | Evidence | UNKNOWN | 18 selected natives hashed across 12 references; essential bundles, judgment and P-17 missing. |
| 4 | Time | PASS | File metadata, sending, recipient acceptance and post-deadline intention distinguished. |
| 5 | Adversarial review | UNKNOWN | Signature-copy caveat, preview discrepancy and probative limits documented; final adverse review remains with #134. |
| 6 | Completeness | UNKNOWN | 27 references without new native acquisition; delivery derivatives and essential sources incomplete. |
| 7 | Channel | UNKNOWN | Four-file plan identified; no rendered final package, no recipient-side identity or delivery proof. |
| 8 | Diff and checkpoint | PASS | Native controls, proposed manifest, transcript and remaining blockers recorded; historical files unchanged. |
| 9 | Governance | PASS | Same-task publication scope remains limited to sanitized results; private sources excluded; no court transmission. |

Files changed in this resumption: this checkpoint, the provenance-note entry point, P-13 notice, 39-row register, proposed manifest, and the master draft's provenance link and four-file consistency. Source/derived status: private unchanged source copies plus public derived working records. Facts checked: native bytes/hashes, MIME attachment equivalence, media metadata/decoding, sampled video frames, photo pixels and existing transcript correspondence. Hypotheses marked: selection, future minimization/assembly and all undemonstrated delivery/examination states. Known risks: incomplete primary collection, privacy of proposed derivatives, timestamp interpretation and no independent audio/transcript comparison. Reversibility: working edits can be reverted; any public dissemination cannot be recalled. Next step: obtain missing primary paths, prepare minimal delivery derivatives, integrate the notice/transcript, then rerun #134. Human validation needed: yes for final selection, legal formulation and transmission; no human review of this technical diff is claimed.

## 8. Targeted primary-source access check after comment 6316431877

Mandate: [targeted resumption instructions](https://github.com/JeanHuguesRobert/barons-Mariani/issues/131#issuecomment-6316431877), explicitly resumed by the Principal on 21 October 2026. This is an access-check checkpoint, not a repeated inventory, a new native acquisition or a finding that the originals are lost. `filing_ready=false`; #131 remains open.

### Accessible search results and limits

- Filename search covered the repository including hidden paths, the supplied-input directory and accessible temporary files, excluding Git internals, dependency trees and virtual environments. It found the existing bundle-comparison source note, but no matching original bundles, P-17 images or named P-20 judgment images. The planned `.filing-materials/senatoriales-2026/` output directory does not exist in this checkout. The materialization map's planned `P-14.pdf`, `P-17.pdf` and `P-20.pdf` paths must not be treated as existing bytes.
- Drive searches for `2601714`, `2601715`, `note_manuscrite_TA_Bastia` and `image-1790344314519` returned no results. A broader `Bastia` search returned other documents, including a derivative electoral-analysis Markdown file; its readable text did not supply the missing case/image filenames or Drive locators. No unrelated returned file was treated as an original. Search silence is limited to these queries and accessible scope.
- The latest #133/#134 comments were read for dependencies. #133 reports an earlier technical preview from commit `7201a005ec38cf316cdd34e0d7327e24f169e44c`; a rendered preview is not any of the missing originals or a build of the later provenance updates. No dependency comment supplied the missing files in this check.
- No ChatGPT Library search/download tool is available in this session. The three Library filenames in comment 6316431877 remain **reported leads**, not contents independently read here: `2026-09-26_note_manuscrite_TA_Bastia_candidature_senatoriale_recto_verso_transcription.md`, `2026-09-26_note_manuscrite_TA_Bastia_candidature_senatoriale_page_1_transcription.md`, and `memoire_defense_TA_Bastia_2601714_2601715_PROJET.md`. No contents, hashes or local locations are invented for them. Transcriptions and a draft defense memorandum do not establish original photographs, filed annexes or receipt.

### Source-state table for the requested three work items

UNKNOWN records an unproved evidence state. BLOCKED describes this session's inability to perform the next byte-level comparison. No size or hash is supplied without the corresponding source bytes.

| References / expected original | Native located | Bytes read | SHA-256 verified | Date/source qualification | Confidentiality / grievance | Delivered status | Workflow / minimum human action |
|---|---|---|---|---|---|---|---|
| P-17: recto and verso source photographs | UNKNOWN | UNKNOWN | UNKNOWN | Note related to 14 September audience per historical corpus; actual photo capture dates and source identity unchecked. The two Library transcriptions are reported derivative leads only. | Sensitive handwriting/context; G2/G3 | UNKNOWN; handover remains reported | BLOCKED: provide both original images by current local path or accessible Drive link, and the two historical transcription files separately for comparison. |
| P-14 / P-44: native PDFs for 2601714 and 2601715, with PREF-1…PREF-16 inventory | UNKNOWN for bundle PDFs; prior P-44 EML acquisition remains PASS | UNKNOWN for bundle PDFs; prior EML byte checks unchanged | UNKNOWN for bundle PDFs; no new hash | Corpus records 11 September transfer notifications. Their EML originals are already preserved; the announced PDFs and their actual contents have not been reacquired. | Personal details and access secrets to minimize; G1/G3/G4 | Bundle delivery/examination UNKNOWN; distinguish initial inventory from later additions | BLOCKED: provide the two original `2601714_PREFECTURE_DE_LA_HAUTE-CORSE_20260911.pdf` / `2601715_PREFECTURE_DE_LA_HAUTE-CORSE_20260911.pdf` copies, or their actual current filenames/links. A defense PROJET or notification is insufficient. |
| P-20: primary judgment and notification, native file or source photos | UNKNOWN | UNKNOWN | UNKNOWN | Decision/notification dated 14 September in the existing controlled transcription. That note lists page/photo roles, but actual completeness and page count are unverified in this pass. | Private address, postal data and other unnecessary details to minimize; G1–G4 | UNKNOWN for the proposed supplement; exact court-side original not compared | BLOCKED: provide native judgment/notification or the original photos named below; include any additional judgment pages so completeness can be checked. |

P-20's existing source note names `image-1790344314519.jpg`, `image-1790344340807.jpg` and `image-1790344356253.jpg` for judgment pages, and `image-1790344298391.jpg` for the notification. These are retrieval leads, not a newly verified total of three judgment pages or four original photographs. Other postal photographs need only be supplied if their chronology is relied upon; the contextual street-sign image is not requested as proof of the judgment.

### Precise human-source request and conditional selection

A question was sent to the Principal through this conversation asking for the current local paths or Drive links for these originals. An alternative supply route is to place unchanged copies in a private subdirectory of the existing `issue-131-inputs` directory on this machine and identify that directory. No public GitHub upload is requested. Provide the actual native bytes; keep the three Library Markdown derivatives separately identified. Their export dates must not be substituted for the dates of the underlying events.

The Principal answered by requesting a prompt for the ChatGPT session that can access Library, returning the needed information through GitHub and using Drive for large files as for P-13. The handoff therefore asks that session to post a source-location checkpoint in #131, with exact accessible Drive URLs/file IDs for large or sensitive originals and immutable GitHub references for any small non-sensitive material it actually publishes. This is a requested retrieval route, not evidence that the files have already been exported, shared or acquired here.

Proposed selection, conditional on acquisition and minimization:

- **P-17 — JOIN:** useful recto/verso reproductions with a separately labelled, source-compared transcription; preserve the distinction between image contents and reported handover. Until acquired, the historical description may only be CITE with its qualification.
- **P-14 / P-44 — JOIN/CITE/RESERVE:** JOIN the useful verified inventory/pages and a credential-free transmission notice; CITE the established communication chronology; RESERVE redundant or unnecessary sensitive annexes. Neither a draft defense memorandum nor P-44 email bytes establishes the original bundle inventory or excludes a later supplemental transfer.
- **P-20 — JOIN:** the complete verified judgment and useful notification, after comparison to the existing transcription; CITE or RESERVE postal/context material according to the actual issue it proves. No transcription is promoted to a native judgment.

No new native row or hash is added to the proposed production manifest. The register links these blocked-source requests without upgrading evidence states. The completed P-13 check and 18-object/12-reference coverage are retained. #132 retains the institutional video-trail question; #133 retains assembly of three PDF attachments and the same three PDFs plus video on TransfertPro; #134 retains final file identity, legal/adverse review and actual acknowledgments. Nothing has been transmitted to the court.

### Parent controls and validation of this delta

The nine controls remain: **1 PASS; 2 PASS; 3 UNKNOWN; 4 PASS; 5 UNKNOWN; 6 UNKNOWN; 7 UNKNOWN; 8 PASS; 9 PASS**. The access check does not resolve primary-evidence, completeness, final adverse-review or delivery gates. The limited PASS results are inherited contribution-level controls, not a filing-ready declaration.

Scope: three targeted source-access blockers. Files affected: this checkpoint, provenance-note entry point and targeted evidence locators in the existing 39-row register. Source/derived status: derived access/continuation trace; no original changed or newly acquired. Facts checked: accessible filename searches, five Drive query results, absence of the planned materialization directory, available tool capabilities and dependency comments. Known risks: scope-limited search, Library access not transferred, incomplete originals, private disclosure and preview/source-version mismatch. Reversibility: documentary changes can be reverted; published text cannot be recalled. Next step: resume byte-level inspection when actual paths/links arrive; do not loop on the same silent search. Human input needed: source-access information above; human validation remains required for final selection and any court transmission.
