# Fortschritt · universalraum-common-parent-t1-t8-20260915

Stand: **2026-09-15** (Replay gelaufen, **PASS**, **kein Tor geschlossen**).

Hypothese: Das Paket bleibt research-only; `closed`-Flags default **false**, bis
ausführbare Gates sie belegen. Bestätigt: 0/8 Tore geschlossen, `toe_complete = false`.

## Physikalische Tore T1–T8

Alle Tore: **`status = partial`**, `closed_in_package = false`. Kein Tor durch
dieses Paket geschlossen. `closed_gate_ids = []`.

| Tor | Kurztitel | Status | Bewiesen (Auszug) | Fehlt (Missing) | Gekillte Route |
|-----|-----------|--------|--------------------|------------------|----------------|
| T1 | Ursprung und Auswahl | partial | primitive typing, target-derived mutation rejected | origin selection | derive-primitive-from-target |
| T2 | Half-Charge und E8-Feld | partial | J²=I, LᴴL=P, RᵀR=I (η=±1); same-vertex double action killed | **raw seam → W-bank intertwiner** (offen, nicht gekillt); Half-Charge; energy/adjoints; scaling | same-vertex double seam action |
| T3 | Gemeinsamer 3+1D-Parent | partial | shared local normalization; Gram-Det/Spektral-Invariant unterscheiden Charts | deklarierte 3+1D-Auswahl | local-norm-fixes-chart; local-norm-fixes-spectrum |
| T4 | Chirale Materie | partial | kommutierendes pᵀΣp verschwindet; 2D-Rotationsansatz nur ±I | fermionisches chirales Maß; interacting mirror gap außerhalb 2D-Ansatz | kommutierender Skalarbilinear; interacting mirror im 2D-Ansatz (scoped) |
| T5 | Kontinuum und Dynamik | partial | s_min(L)=1−cos(π/L) streng fallend, → 0, keine uniforme Lücke | Kontinuum-/thermodynamischer Limes; operator-state; scattering | naive-cycle-uniform-gap |
| T6 | Parameter und Spektren | partial | drei dark Blöcke teilen Casimir 45, haben bei fester Summe rang-eins verschiedene Casimir-Paare; 6 Kandidaten-Lifts | gemeinsames normiertes W[J]; gauge couplings aus einem W[J]; Massen/Neutrino aus einem W[J]; eindeutige Lift-Auswahl | (keine; Non-Uniqueness-Zeuge) |
| T7 | Gravitation (Spin-2) | partial | (1,0)+(0,1) ist antisym. 2-Form, nicht Spin-2; free Zeuge prescribed/conditional | dynamical massless spin-2; universal dynamic coupling | uniform-mediator-as-dynamical-spin-2 |
| T8 | Zustand und Instrumente | partial | ground margin 8223/31250 > 0; a²−b² = −7/25 ≠ 0 | state selection functional; native state/instrument/record | unique-gs-energy-gap-as-sufficient-selector |

Externe Statusreferenz: `docs/OPEN_PROBLEMS.md` — **All T1–T8 remain open**;
`TFPT.TOE.COMPLETE.01` offen. Keine Statusinflation, kein Fake-Closure.

## Replay-Ergebnis (2026-09-15)

- `status = PASS`, `toe_complete = false`, `closed_gate_ids = []`.
- 125 exakte Checks = parent 10 + seam 52 + T1–T4 24 + T5–T8 29 + cross 10.
- 21/21 Quell-Hashes verifiziert; normal und `-OO` byte-identisch.
- `parent_id = tfpt-universalraum-common-parent-t1-t8-20260915:0804f4a5bc73a17f`.
- Erster Fehlschlag: `Jᵀ D L = D` (falsche Kanten-Konvention + vermischte Spin-Vorzeichen).
  Korrektur: `|J|ᵀ D |L| = -D` für Kanten `e → e+1`; danach seam 52/52 PASS.
- Entscheidender nächster Satz: raw seam → four 64-mode W-bank intertwiner (T2, offen).

## Plan-Todos (Implementierung)

| # | Todo | Status | Anmerkung |
|---|------|--------|----------|
| 1 | Root-Scaffold (`README.md`, `PROGRESS.md`) | **done** | Init + Update nach Replay |
| 2 | `obligations.json` — T1–T8 autoritativ einfrieren | **done** | Schema mit Vertragsbezug |
| 3 | `provenance.json` — Quellen + SHA-256 | **done** | 2026-09-15, 21/21 verifiziert |
| 4 | `replay.py` + Manifest (Hash-Gate, Status RUNNING→PASS/FAIL) | **done** | PASS, 125 Checks, byte-identisch |
| 5 | Gate-Checker-Sammlung (Suite-Delegat + Spinlift/Native-Pins) | **done** | parent/seam/T1–T4/T5–T8/cross |
| 6 | `RESULTS.md` / `EINFACH.md` (Parent nach erstem Lauf) | **done** | 2026-09-15, ehrliche Verdikte |

## Nächste sichere Schritte (ohne Statusinflation)

1. Beweis (oder Widerlegung) des **raw seam → four 64-mode W-bank intertwiner**
   als entscheidendem nächsten Satz für T2.
2. Skalierung `s_min → 0` explizit im Kontinuums-/Thermodynamik-Limes behandeln (T5).
3. Eindeutige Lift-Auswahl aus den sechs Kandidaten für T6 prüfen.
4. Interacting mirror gap **außerhalb** des 2D-Rotationsansatzes für T4 angehen.
5. Native state/instrument/record am Parent für T8 konstruieren.

Kein Tor darf als `closed` markiert werden, bis ein ausführbarer Zeuge es belegt.
