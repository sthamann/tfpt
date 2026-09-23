# Gemeinsamer Parent · T1–T8 (Forschung)

Abgetrenntes Paket unter `universal_room/new-3/`. **Nur Forschung** — kein Eintrag in
`verification/`, kein Ledger, kein Paper- oder Website-Update. Der Replay ist
gelaufen und PASS, **kein Tor geschlossen**, `toe_complete = false`.

## Idee in einem Bild

```
  P1/P2 + native W/Clock          experiments/-Firewall
         │                                  │
         ▼                                  ▼
   ┌─────────────┐                   ┌──────────────┐
   │ Parent-Spec │  ── replay.py ──▶ │ 125 Checks   │
   │  (3+1D-Ziel)│     (PASS)        │ 0/8 Tore zu  │
   └─────────────┘                   └──────────────┘
         │
         │  prüft (offen): T1 … T8
         ▼
   TFPT.TOE.COMPLETE.01  →  bleibt [O]
```

**Ein gemeinsamer Parent** heißt: dieselbe ausgewählte Mikrostruktur soll später
**alle acht physikalischen Tore** T1–T8 zugleich tragen — nicht acht getrennte
Toy-Modelle ohne Brücke. Das Paket hat eine gemeinsame **Prüfspezifikation**
mit durchgängiger Identität (`...0804f4a5bc73a17f`) etabliert, aber noch
keinen physikalischen gemeinsamen Parent und keine vollständige TOE.

## Was hier liegt

| Datei | Rolle |
|-------|--------|
| `obligations.json` | Eingefrorene T1–T8-Pflichten (Status: `open`) |
| `provenance.json` | SHA-256-Pins für Verträge, Suite-Module und Universalraum-Quellen |
| `parent_spec.json` | Parent-Spezifikation: Konstanten, Operatoren, `derived`, `absent`, `verdict` |
| `parent_model.py` | Parent-Modell-Checker (10 exakte Checks) |
| `seam_lift.py` | Seam-Lift-Checker (52 exakte Checks) |
| `gates_t1_t4.py` | Tore T1–T4-Checker (24 exakte Checks) |
| `gates_t5_t8.py` | Tore T5–T8-Checker (29 exakte Checks) |
| `cross_gate.py` | Cross-Gate-Integritäts-Checker (10 Own-Checks) |
| `replay.py` | Replay-Orchester: Hash-Gate + Modul-Delegation + Status RUNNING→PASS/FAIL |
| `REPLAY.json` | Ergebnis des letzten Replay-Laufs (Quelle für `RESULTS.md`) |
| `verification_normal.json` | Normale Modul-Ergebnisse (Quelle für `RESULTS.md`) |
| `verification_optimized.json` | `-OO`-Ergebnisse (byte-identisch zu normal) |
| `PROGRESS.md` | Tore + Plan-Todos mit echtem Lauf-Stand |
| `RESULTS.md` | Detaillierte deutsche Ergebnisse (Parent nach erstem Lauf) |
| `EINFACH.md` | Einfache, visuelle Erklärung für die ursprüngliche Frage |

## Replay ausführen

Vom Repository-Root:

```sh
python3 universal_room/new-3/universalraum-common-parent-t1-t8-20260915/replay.py
```

Der Replay prüft die 21 Quell-Hashes gegen `provenance.json`, delegiert an die
fünf Modul-Checker und schreibt `REPLAY.json` sowie die beiden
`verification_*.json`. **Keine** Promotion in die load-bearing Suite.

## Exakte aktuelle Ergebnisse (letzter Lauf 2026-09-15)

| Größe | Wert |
|-------|------|
| `status` | **PASS** |
| `toe_complete` | **false** |
| `closed_gate_ids` | **`[]`** (0/8 Tore geschlossen) |
| `total_exact_checks` | **125** = parent 10 + seam 52 + T1–T4 24 + T5–T8 29 + cross 10 |
| `source_hashes_verified` | **21 / 21** |
| `byte_identical` (normal vs. `-OO`) | **true** (alle 5 Module) |
| `parent_id` | `tfpt-universalraum-common-parent-t1-t8-20260915:0804f4a5bc73a17f` |

`status = PASS` heißt **Checker-Integrität**, nicht Tor-Abschluss
(`parent_spec.verdict.status_pass_means = "checker integrity only; no gate is moved"`).

**Erster Fehlschlag und Korrektur:** erste Replay-Behauptung `Jᵀ D L = D`
scheiterte an falscher Kanten-Konvention plus vermischten Spin-Vorzeichen.
Korrekte exakte Relation für Kanten `e → e+1`: `|J|ᵀ D |L| = -D` (Absolutbeträge,
Minus-Vorzeichen, Spin-Vorzeichen separiert). Danach seam standalone 52/52 PASS.

**Entscheidender nächster Satz:** raw seam → four 64-mode W-bank intertwiner
(offener Blocker für T2, nicht gekillt).

**Skalierung:** `s_min(L) = 1 - cos(π/L) → 0` (T5), keine uniform positive
Lücke — naive-cycle-uniform-gap-Route gekillt.

## Firewall

- Alles bleibt unter `universal_room/new-3/` bzw. `experiments/`.
- Geschlossene Flags (`closed: true`) sind **verboten**, bis ein ausführbarer
  Gate-Lauf sie belegt — aktuell 0/8.
- `docs/OPEN_PROBLEMS.md` und `tfpt_research_contracts.tex` bleiben die äußere
  Status-Wahrheit.
- Kein Eintrag in `verification/`, kein Ledger, kein Paper-/Website-Update.
- Keine `*_fixes.md`, keine zusätzlichen Tests, PDFs oder Manifeste.

## Lesen

- `RESULTS.md` — detaillierte deutsche Ergebnisse, Per-Gate-Status, Korrektur
- `EINFACH.md` — einfache visuelle Antwort auf die Ursprungsfrage
- `PROGRESS.md` — Tore und Plan-Todos mit echtem Stand
- `docs/OPEN_PROBLEMS.md` — ehrliche Frontier, alle T1–T8 offen
- `experiments/theory-contracts/RESEARCH_2026-09-09.md` — Konsolidierungskarte
- `tfpt_research_contracts.tex` — benannte Vertrags-IDs zu T2–T8 und 4D-Route

Stand des Replay-Laufs: **2026-09-15**.
