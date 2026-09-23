# F2: Zellbank gegen Kantenmoden — quellenbasierte Auswahl

14. September 2026. NON-RH. Nur `experiments/theory-contracts`.
Keine Promotion nach `verification/`, Ledger, Papers oder Website.

## Firewall

Lokalität allein wählt die Bank nicht. Eine Wahl nach angenehmerem Spektrum
(0,7 Δ gegen 0,4 Δ, Gapkoeffizient −11,96 gegen +13,90, F4-Grundwert) ist
keine Herleitung. Der Prüfer verbietet dem Selektor, Spektralzahlen zu lesen.

## Drei Architekturen

Auf L Tetramerzellen (je 4 Orte):

| | Bank | Paarterme | Lokal? |
|---|---|---|---|
| (i) | global, gleiche Moden über alle Zellen | `10*C(4L,2)` | nein (Stütze wächst mit L) |
| (ii) | eine Bank pro Zelle | `60L` innere Paarterme | ja, feste Zellgröße 4, endlichreichweitige Zwischenzellkopplung |
| (iii) | eine Bank pro Kante | keine disjunkten Paarterme | ja, Stütze 2 Orte |

Ohne Zwischenzellkopplung ist (ii) ein **exaktes extensives Gegenmodell** zur
behaupteten Auswahl von (iii) durch Lokalität: Energie ~ L, Gap intensiv,
Gapkoeffizient **+13.901769…** (zellgeteilt) gegen **−11.955494…** (kantenlokal).
Der Unterschied ist keine Umbenennung.

## Identische Quellen (C16)

Hartes C16-Modell, `Nf+2Nb=16`, `|t|/Δ ≤ 1/20`. Ortsmengenzensus auf allen
65536 Belegungen des Clebsch-Graphen:

`L(m) = (0,0,1,2,4,5,7,9,12,14,17,20,24,27,31,35,40)`.

Gewichteter Schurtest, `An = Q(n+1) B† Qn`, `Ln = L(16-2n)`:

- Zelle: `‖An‖² ≤ 2(n+1) min(4,n+1) Ln`
- Kante: `‖An‖² ≤ 2(n+1) Ln`, also `a² = (80,124,144,136,120,84,56,16)`

Rationale LDL-Pivots von `T − 7I/10` (acht Werte, alle > 0) ⇒ **0,7 Δ**
kantenlokal gegen **0,4 Δ** zellgeteilt. Negativkontrolle **0,8 Δ** scheitert
am 2. Pivot (`−7/20`). Das ist kein thermodynamischer Bandabstand und kein
innerer Singulettgap.

Feshbach-Rest bei `e ≤ 0`, `t/Δ = 1/20`: **13.1528 J → 1.71601 J**, weiterhin
zu groß für den inneren Gap (~0,486 J, trunkiert).

F4-Grundwerte (gepinnt, nicht Selektorinput):
555.4885003638373 (Zelle) gegen 732.1203109419222 (Kante);
auf den ersten vier Moden 583.292038666386 gegen 708.209322518918.

E8-Gittercocycle, diagonale ±1-Gaugeklasse: F2-Ränge **45** (lokale Antisymmetrie)
und **285** (kantenlokaler Adapter). Geteilte Bank in dieser Klasse **obstruiert**.
Komplexe oder nichtdiagonale Adapter sind damit nicht ausgeschlossen.

## Quellen-Selektor

Erhaltene lokale Ladung `Qv = nf(v) + Σ_{e∋v} ne`. Voll belegte Nullbosonquelle
⇒ `Qv = 1` ⇒ besetzte Bosonen bilden ein Matching. Allordentlicher CAR/Tensor-
Eichadapter existiert nur **kantenlokal ohne Hopping** (940D K4-Matching,
1584 Erzeugungsübergänge, 144 nichttriviale Vorzeichen).

Z4-Glue / uniforme Superaustausch-Stärke `J` auf jeder Clebsch-Kante betrifft
Graph und Kopplung, **nicht** die Bank: beide lokalen Varianten bleiben zulässig.

**Vorschrift:** Architektur **(iii), Bank pro Kante**.

**Offen:** komplexe/nichtdiagonale Adapter; Clock-Transport des Gittercocycles
in die TFPT-Quellbasis; Vermittlerhopping und andere Ladungssektoren.

**Kill des Selektors:** eine quellennative CAR/Tensor-Eichlösung für geteilte
Zellmoden in der tatsächlich benutzten Gaugeklasse; quellenerzwungenes
Vermittlerhopping; ein nativer Clock-Adapter, der geteilte Moden braucht;
eine Quellstelle, die K4-Zellen oder eine Kette erzwingt.

## Reproduktion

```sh
python3 -B checker.py validation.json
python3 -B -m unittest test_checker
python3 -B -OO -m unittest test_checker
```

Normal und `-OO` müssen bytegleiche Testergebnisse liefern.
F4-Zeuge: `spectrum_followup.json` (SHA-256 in `checker.py`).

Quellen: `universal_room/TFPT_Followups_2026-09-14_v1.4.md` Frage 2;
`TFPT_Universalraum_Ergebnisse_2026-09-14_v1.4.md` §§2–5;
`universalraum-five-source-frontier-20260914/RESULTS.md` §§2–5;
`TFPT_UNIVERSALRAUM_FUGEN_2026-09-14.md` §§3–6.
