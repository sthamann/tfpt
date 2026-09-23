# universalraum-parallel-closure-20260914 — C16-Nachfolgerlane

NON-RH. Theory contract (`experiments/`); keine Promotion nach `verification/`, Ledger, Papers oder Website.

Schließt oder schärft die drei offenen C16-Flags aus
`universalraum-paired-release-20260914/new-input-audit/singlet_f4.json` im Rahmen des
Hauptnachfolgervertrags: erste Anregungs-Multiplizität, 64-SU(4)-Sektor-F4-Konkurrenz bei
`|t|/Δ = 1/640`, und sechste-Ordnung-Rest (global vs. geschlossene Blöcke).

Zusätzliche Lane **History / U / Nicht-Identifizierbarkeit / native Phase** (gleicher Vertrag,
eigene Artefakte, C16-Quellcode unverändert).

## Quellpin (SHA-256 in `source_manifest.json`)

| Quelle | Rolle |
|---|---|
| `../universalraum-paired-release-20260914/new-input-audit/check.py` | Mikroskopische F4-Pfade, 544-Sternblock, Schur-Norm `160|t|` |
| `../universalraum-paired-release-20260914/new-input-audit/singlet_f4.{py,json}` | 24024-Singulett, F4-Projektion, ε²-Koeffizienten |
| `../universalraum-paired-release-20260914/new-input-audit/{verification,replay}.json` | Baseline 891 Checks, Mutanten-Protokoll |
| `../universalraum-fugen-20260914/clebsch_su4.{py,json}` | H-only alle 64 Irreps (Schur–Weyl, keine Kopie von Young/Swap) |
| `../universalraum-fugen-20260914/checker.py` | Fugen-Audit: `\|N_ab\|=1`, Traegerkern `K^+K=I-S` (nur Betrag, keine Bracket-Phasen-API) |
| `../compiler-origin-audit-20260913/context_instrument.py` | 240 phasenmarkierte Gaussian-Wurzeln, Paulis, Uhr — kein E8-Strukturkonstanten-Phasentableau |
| `../compiler-single-execution-20260914/{check.py,verification.json,replay.json}` | Referenz: 22D-U₀, Record ohne geordnete Farbhistory |

Keine duplizierte Young-/Swap-/F4-Implementierung: Matrizen und Kanten aus `clebsch_su4.py`,
F4-Matrixwirkung über dieselbe Kanten-/Label-Liste wie im Audit (Mediatoren aus `checker.py`).

## ε-Intervalle

- **`t/Δ = 1/640`**: globale Schur-Norm `‖V‖ ≤ Δ/4` (Satz B1, gepinntes Audit) — Zertifikat für
  H-only-Grundzustand und konservative F4-Korrektur `± c_max ε²` mit `ε² = 1/409600`.
- **`t/Δ = 1/20`**: Referenz für numerische sechste/vierte Ordnung im geschlossenen 544-Sternblock
  und für die in `singlet_f4.json` dokumentierte ε²-Lückenkorrektur (nicht als globale Schranke).

## Dateien

| Datei | Inhalt |
|---|---|
| `c16_parallel_closure.py` | C16-Prüflogik, schreibt `validation.json` |
| `run_checks.py` | C16: Normal / `-OO`, Mutanten, `replay.json` |
| `u_phase_audit.py` | History/Gram/U/Phasen-Lane, schreibt `u_phase_validation.json` |
| `u_phase_run_checks.py` | U-Lane: Normal / `-OO`, 6 Mutanten, `u_phase_replay.json` |
| `source_manifest.json` | Gehashte Quellbytes (C16 + U-Lane) |
| `validation.json`, `validation_optimized.json`, `replay.json` | C16-Ergebnisse |
| `u_phase_validation.json`, `u_phase_validation_optimized.json`, `u_phase_replay.json` | U-Lane-Ergebnisse |

## Reproduktion

```sh
cd experiments/theory-contracts/universalraum-parallel-closure-20260914
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B run_checks.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B u_phase_run_checks.py
# nur Schließungsprüfer:
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B c16_parallel_closure.py --output validation.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B u_phase_audit.py --output u_phase_validation.json
```

Laufzeit: Baseline-Import + Clebsch-JSON + Singulett-Lanczos (k≈12) typisch ~15–30 s;
U-Lane: Context-Replay + 40 Kanten ~5–15 s. Kein voller 64-Sektor-Neulauf (Daten aus gepinntem `clebsch_su4.json`).

## Flag-Erwartungen (Stand Implementierung)

| Flag | Typ |
|---|---|
| `exact_first_level_multiplicity` | `false`: W(D5)-Charakter und Lanczos stützen einen irreduziblen 4-Raum numerisch, ersetzen aber keinen exakten Eigenprojektor oder Inertia-/Minimalpolynom-Nachweis |
| `all_sector_f4_competition_at_640` | analytisch via H-only-Pin und voller Operatornorm `‖F4‖ ≤ 40·4 + 160·8 + 60·8 = 1920` |
| `global_t6_bound` | `false` ohne BD-Lokalschranke; `numerical_block_t6_scaling_544` separat |

## U-Lane (History / Phasenadapter)

| Ergebnis | Wert |
|---|---|
| `local K^+K` | `I-S`, Rang 6 |
| geordnete ab-History `L` | `L^+L = I-D`, Rang 12; `L^+L = K^+K` genau dann wenn `L=VK` (Isometrie-Einbettung) |
| `U_W` | 22D unitär; `H_bad`: K₄ Grundraum dim 24, Stern dim 108 |
| P1/P2-Nicht-Injektivität | zwei unitäre `U_θ`-Vervollständigungen gleicher lokaler Grammatik, gleicher erster Block-Readout, verschiedene Zwei-Schritt-Mediator-Wahrscheinlichkeit (Quellen-Unterbestimmung, kein Metatheorem) |
| `phase_adapter_verdict` | **`BLOCKED_MISSING_NATIVE_PHASE_DATA`** — Gaussian-Wurzel-/Clock-Phasen ≠ Lie-Klammer-Strukturkonstanten-Phasen; kein Zyklus-Holonomie-Vergleich ohne native signed Daten |
| `CAR_native_phase_equivalence` | **`false`** (Baseline); Comparator-Felder fehlen, keine geratenen ±1-Phasen |

Statusgrenzen: geschlossen sind endliche Gram-/U-Zeugen und 40-Kanten-Lokalregel; blockiert bleiben nativer TFPT↔CAR-Phasenvergleich und T1–T8.
