# TFPT / Universalraum — Antworten auf die Follow-ups und offenen Fragen

14. September 2026. Grok-Runde 1. Forschungsstand, kein T1–T8-Abschluss,
keine Promotion nach verification, Ledger, Papers oder Website.

Die sechs Follow-ups aus `universal_room/TFPT_Followups_2026-09-14_v1.4.md`
haben jeweils eine ausführbare Entscheidung. Das schließt T1–T8, RH,
Faktorisierung und P versus NP nicht.

Verträge:

- `experiments/theory-contracts/universalraum-v14-F1-primitive-20260914`
- `experiments/theory-contracts/universalraum-v14-F2-architektur-20260914`
- `experiments/theory-contracts/universalraum-v14-F3-quartett-20260914`
- `experiments/theory-contracts/universalraum-v14-F4-fehler-skalierung-20260914`
- `experiments/theory-contracts/universalraum-v14-F5-gemeinsame-welt-20260914`
- `experiments/theory-contracts/universalraum-v14-F6-transfer-20260914`

---

## Kurzüberblick

| Frage | Entscheidung |
|---|---|
| 1 Wer bedient das Labor? | Primitive eingefroren: `U_e`, Zugriffsklasse, Born. Jeder Handgriff hat Umsetzung und Kosten. Filter sind Polynome von `H`, kein versteckter `Ω`-Projektor. `U` selbst nicht aus P1+P2. |
| 2 Welche Bauweise? | Lokalität wählt nicht. Quellen-Selektor (Qv=1-Matching, CAR/Tensor in diagonaler ±1-Klasse, kein Hopping) schreibt **Bank pro Kante** vor. Spektrum ist Folge, nicht Wahl. |
| 3 Vierfachstruktur? | Multiplizität der 4-Isotyp von `W(D₅)` ist exakt 4. Trunkiertes Quartett Kato-isoliert (Residuum `< 5·10⁻¹⁴`). Nacktes Nichtsingulettminimum und `H6`-Rest offen. |
| 4 Fehler und Größe? | Unabhängige Zellen brauchbar (556 / 890 Zyklen). Default-Kopplung `λ=J` liegt außerhalb des `10⁻⁶`-Fensters. |
| 5 Eine gemeinsame Welt? | Eine Familie `C16 × (ℤ/Lℤ)^d` trägt die Teiltests, nicht gleichzeitig Kegel, chirales Maß und Spin-2. Verdict: `NO_GO_MISSING_SELECTORS`. |
| 6 Dieselben Parameter? | Fixierte Branche gegen ACT: Spannung `≈ 3.51σ`. Flavour `Y = y·1`, keine Hierarchie. Status Spannung, kein nachträglicher Fit. |

---

## 1. Wer bedient das Labor?

**Antwort:** Drei eingefrorene Primitive, sonst nur Zusammensetzung.

| Primitive | Rolle |
|---|---|
| `U_e` | unitärer Vertex aus E8-Strukturkonstanten auf Materie × Vermittler × History |
| Zugriffsklasse | ob ein Historyfaktor später noch gelesen wird |
| Born | Auslese auf der deklarierten Algebra, nicht aus dem Compiler |

Jeder Handgriff hat Umsetzung und Kosten:

| Handgriff | Umsetzung | Kosten | Versteckter Projektor? |
|---|---|---|---|
| Isolierte Kante | Träger von `U_e`; Löcher der beiden Orte sind das Kantenlabel | 1 Vertex | nein |
| Belegungsabfrage | Born auf dem adressierten Vermittler | 1 Bit | nein |
| Record | History ist der Wertebereich von `U_e`; Makro `(U0⊗I)Q(U0⊗I)` | 1 `U0` + Kopie | nein |
| Kontrolliertes `H` | Virtuelle 2. Ordnung von `U_e`; `H_eff = (2t²/Δ) Σ P₊` | Zeit `τ`, `t/Δ` | nein |
| Resonanz / Filter | Fourier/Lagrange von `spec(H)` | 13 Zeiten, `Στ = 3172.829634 ℏ/Δ`; Start+Ende 26 Aufrufe | nein |
| Messung | Born auf der deklarierten Zugriffsalgebra | 1 Schuss | nein |
| Reset | Quellmessung plus Quell-Pauli | 8 Farbbits/Zelle plus Umgebung | nein |
| Präparation | Sternfilter von `H`, leeren Vermittler behalten | `w²/6 ≈ 16,19 %`, im Mittel 6,176 Versuche | nein |
| Record frisch/behalten | Zugriffsklasse auf `H_history` | Quotient `17/32` | nein |

Der Tetramerfilter

`(1/8) Σ_{r=0}^{7} exp(−iπ r H / 4J)`

ist 1 auf Energie 0 und 0 auf `{2,3,4,6}`. `Ω` ist der eindeutige Kern, aber
kein Eingabeprojektor. Sternfilter: 13 Zeiten, Präparation `w²/6 ≈ 16,19 %`.
Gesamterfolg etwa 15,73 % mit behaltenem und 8,36 % mit frischem Record.

Gleichlabelige Clebsch-Kanten sind ein 1-Faktor: vier paarweise disjunkte
Kanten. `Q` auf gemeinsamem Kanal kann sie auslöschen; die Löcher von `U`
bleiben orthogonal.

`U` selbst folgt nicht aus P1+P2. Deshalb bleibt T1 offen.
Vertrag: `universalraum-v14-F1-primitive-20260914` (84 Checks, 8 Tests).

---

## 2. Welche Bauweise ist vorgeschrieben?

**Antwort:** Bank pro Kante. Lokalität wählt das nicht.

Drei Architekturen auf L Tetramerzellen:

| | Bank | Paarterme | Lokal? |
|---|---|---|---|
| (i) | global, gleiche Moden über alle Zellen | `10·C(4L,2)` | nein |
| (ii) | eine Bank pro Zelle | `60L` innere Paarterme | ja |
| (iii) | eine Bank pro Kante | keine disjunkten Paarterme | ja |

Beide lokalen Varianten wurden am selben C16 gemessen (`Nf+2Nb=16`,
`t/Δ = 1/20`). Der Selektor liest kein Spektrum. Erzwingend sind:

- erhaltene lokale Ladung `Qv = nf(v) + Σ_{e∋v} ne`
- voll belegte Nullbosonquelle ⇒ `Qv = 1` ⇒ Matching
- allordentlicher CAR/Tensor in der diagonalen ±1-Klasse
- kein Vermittlerhopping

Geteilte Bank ist in dieser Klasse obstruiert (F2-Rang 45 lokal antisymmetrisch,
285 kantenlokal, geteilt inkonsistent). K4-Matching: 940D, 1584
Erzeugungsübergänge, 144 nichttriviale Vorzeichen.

`0,7Δ` gegen `0,4Δ` und die Gapkoeffizienten `−11.955494…` gegen
`+13.901769…` sind Folgen, keine Wahl. Feshbach-Rest sinkt von 13,15 J auf
1,72 J, bleibt zu groß für den inneren Gap (~0,486 J).

**Kill des Selektors:** quellennative geteilte CAR-Eichung, Hopping, oder
Clock-Adapter mit geteilten Moden; Quellzwang auf K4-Zellen oder eine Kette.

Offen: komplexe/nichtdiagonale Adapter; Clock-Transport des Gittercocycles.
Vertrag: `universalraum-v14-F2-architektur-20260914` (7024 Checks, 15 Tests).

---

## 3. Ist die Vierfachstruktur bewiesen?

**Antwort:** Die 4-Isotyp ist exakt vierfach. Isolation gilt für den
trunkierten Operator.

1. `|Aut(Clebsch)| = 1920 = |W(D₅)|`, 16 Translationen (gerade Vorzeichen).
2. Die Standard-4 von `S₅` hat `χ(id)=4`, `χ(Transposition)=2`; `2⁴` wirkt
   trivial. `S₅` hat keine Irreps der Dimension 2 oder 3.
3. Graphunabhängig: `Ee² = 2Ee`, `Σ_v Av = 2A`, daher
   `F4,edge = 2A + Σ_{Überlapp} {Ee,Ef} = Σ_v Av(Av−I) ≥ 0`.
4. Jeder Aut-invariante selbstadjungierte Operator erhält `W(D₅)`-Isotypen.
   `F4,edge` ist aus Kantenoperatoren gebaut, also Aut-invariant.
   `H0 + c F4` kann die 4-Isotyp nicht aufspalten.
5. Die dichte Singulettanalyse hat auf dem ersten angeregten Cluster
   `Σ_g |χ(g)|²/|G| = 1` und `χ(01) = +2`. Das ist die irreduzible
   Standard-4, nicht vier Zufallssingletts.

Trunkierte Neudiagonalisierung von `H0 + 0.00125 F4,edge` im 24.024D-Singulett:

- `E0 = 11.960507412663516`
- `E1 = 12.446984939669278`
- Gap `0.4864775270057624`
- acht Residuen, Maximum `< 5·10⁻¹⁴`

Kato: ein Eigenwert liegt in `[μ−‖r‖, μ+‖r‖]`. Die Residuenkugel um das
Quartett erreicht weder den Grundzustand noch den nächsten gerechneten
Cluster.

`f(h) = h + ε²(h²−76h+1440)/2` ist auf `[0,40]` bei `ε=1/20` streng steigend.
Das Bild der *berichteten* nackten Nichtsingulettuntergrenze `12.133537…`
liegt über der variationalen Quartett-Obergrenze `12.447`. Die eingesetzte
nackte Untergrenze ist **nicht** zertifiziert.

Offen: Intervall-/Inertia-Zertifikat des nackten Nichtsingulettminimums;
kanonischer `H6`-Rest; Lean.
Vertrag: `universalraum-v14-F3-quartett-20260914` (1989 Checks, 9 Tests).

---

## 4. Bleibt das Labor bei Fehlern und Größe brauchbar?

**Antwort:** Unabhängig ja. Gekoppelt beim Default `λ = J` nein.

Unabhängig bewiesen:

- CPTP-Attraktor mit einzigem Fixpunkt `Ω`
- Rate `r = 0.97542071045`
- Fehlerboden `40.6847 ε`
- 556 Zyklen für eine Zelle auf `10⁻⁶`
- 890 Zyklen für 4096 Zellen per Vereinigungsbound, auch bei verschränktem Start
- ungelesener unitaler Record kühlt nicht (Fixalgebra-Dimension 3876)
- Reset: bis zu 8 Farbbits/Zelle, 3 Austauschrecords/Zyklus, 26 kontrollierte
  `H`-Aufrufe für Start+Ende
- im Mittel 6,176 Präparationsversuche

Gekoppelt:

- Zweizellengap bleibt `> J/2` für alle getesteten `λ/J`, einschließlich
  `λ/J → ∞`
- Produktzustand-Brücke: Erwartungswert `5/8`, Varianz `15/64`
- Default `λ = J`, `t/Δ = 1/20` auf den deklarierten Record-/Filterzeiten:
  2-Zell-Boden `≈ 16`, Kette N=4096 global `≈ 1.58·10⁵` — beides außerhalb
  von `10⁻⁶`
- grobe Eindeutigkeit stirbt bei N=5, `λ=J`

Härteste Restressource: Zwischenellentkopplung oder extra Datum `λ ≪ J`.
8 Farbbits und `log N` Zyklen sind billig dagegen. Kein T8-Abschluss.
Vertrag: `universalraum-v14-F4-fehler-skalierung-20260914` (65 Checks, 10 Tests).

---

## 5. Entsteht eine gemeinsame Welt?

**Antwort:** Nein. Eine Familie reicht nicht.

Kandidat `F = C16 × (ℤ/Lℤ)^d` trägt Wärme, Overlap, Weyl und Tensor
gleichzeitig — dieselben Diagnostiken, ein Parameterblock.

| Teilresultat | Zahl |
|---|---|
| Wärmespur faktorisiert; t=8, L=64 ⇒ `ds ≈ 1.0167118 d` für d=1..4 | T3-heat |
| Overlap, Fluss 3 auf 8×8 und 10×10: 3 Nullmoden, Index −3 | T4-torus |
| Fluss 0: 2 Nullmoden, Index 0 | T4-Kontrolle |
| Freie Bilinear-Schwelle 2m; TT-Projektor Rang 2, kein Pol | T7-frei |
| Sinus-Weyl d=3: 8 Knoten, chirale Gesamtladung 0 | T7-Weyl |
| Clebsch dreiecksfrei: K4 nicht einbettbar | T5-negativ |

Fehlende Selektoren:

1. Familie+Kegel: dieselbe Familie gibt jede eingesetzte Dimension zurück.
2. Fluss/Geometrie: der Index ist der hineingesteckte Fluss.
3. 3+1D-Propagation + Spiegelgap: Overlap ist räumlich 2D; Weyl-Doubler
   löschen die Nettoladung.
4. Masseloser Spin-2: TT ist kinematisch; kein weicher Pol.
5. T5: K4 steckt nicht im Clebsch-Graphen.

Verdict: `NO_GO_MISSING_SELECTORS`. T3, T4, T5, T7 bleiben offen.
Vertrag: `universalraum-v14-F5-gemeinsame-welt-20260914` (115 Checks).

---

## 6. Stimmen dieselben Parameter?

**Antwort:** Nein. Status Spannung, kein nachträglicher Fit.

Fixiert: `c3 = 1/(8π)` (P1), einfache Inflationsbranche

`As(1−ns)² = c3⁷/(6π²)`, `r = 3(1−ns)²`.

ACT DR6 v2, Tabelle 5, Spalte P-ACT-LB2 (arXiv:2503.14452v2):

- `ns = 0.9752 ± 0.0030`
- `log(10¹⁰ As) = 3.062^{+0.010}_{-0.012}`

| Kalibrierung | N | Vorhersage | Abweichung |
|---|---|---|---|
| auf zentrale `As` | 56.62391 | `ns = 0.96467923`, `r = 0.003743` | **3.5069σ** in `ns` |
| auf zentrales `ns` | 80.64516 | Amplitude **2.02842×** zu groß | `r = 0.001845` |

Gemeinsames Treffen beider Zentralwerte würde `c3` um 9,61 % kleiner machen.
Das ist keine Reparatur: `c3` ist anderweitig fixiert. Joint-√χ² entlang der
Branche ≈ 3.39–3.70 (bei ρ=0: 3.50). Reheating verschiebt nur N entlang der
Invariante und schließt nicht.

Flavour im selben Overlap-Modell (Zweitorus, `m0=1`, U(1)-Fluss 3):
`Y_ab = y δ_ab`, Einheitsmatrix, keine Hierarchie. Ein Kosinus-Profil
spaltet Eigenwerte, ist aber neuer Input.

Fehlend: normierte gemeinsame Wirkung, abgeleitetes Higgsprofil, RG,
Theoriefehler.
Vertrag: `universalraum-v14-F6-transfer-20260914` (66 Checks, 12 Tests).

---

## Was bewusst ungelöst bleibt

| Ziel | Warum die sechs Verträge es nicht schließen |
|---|---|
| T1 | `U` ist gesetzt, nicht aus P1+P2 |
| T2 | native Halbladung mit Energie-/Adjungiertenkontrolle fehlt |
| T3–T5, T7 | eine Familie ohne Selektoren für Kegel, Index 3, Spin-2 |
| T6 | gemeinsame Wirkung, Higgsprofil, RG, Theoriefehler fehlen |
| T8 | Resetumgebung und Quellfunktional nicht aus `U` |
| RH / Faktor / P vs NP | endliche Labortests liefern das nicht |
| Dunkle Materie / DE / Baryogenese / starkes CP / BH | brauchen den fehlenden Feld+Gravitationssektor |

Die drei fundamentalen Unbekannten der Konsolidierung bleiben:

- **A** — die eine mikroskopische Regel `U` vollständig hinschreiben und
  danach nichts mehr wechseln (Kommutante auf dem harten C16-Belegungssektor)
- **B** — thermodynamischer Grenzwert mit drei Raumrichtungen und gemeinsamem
  Lichtkegel
- **C** — topologischer Vakuumsektor: Index 3 und masseloser Spin-2

Reihenfolge: A vor B vor C.

**Nächster lasttragender Schritt:** A2 der Konsolidierung (Kommutante von
`H_eff` auf dem harten C16-Belegungssektor) und ein zertifiziertes nacktes
Nichtsingulettminimum. Ohne das bleibt Spin(10) gegen `W(D₅)` eine offene
Architekturentscheidung.

---

## Reproduktion

```sh
cd experiments/theory-contracts
python3 -B universalraum-v14-F1-primitive-20260914/checker.py --output validation.json
python3 -B universalraum-v14-F2-architektur-20260914/checker.py validation.json
python3 -B universalraum-v14-F3-quartett-20260914/checker.py --output validation.json
python3 -B universalraum-v14-F4-fehler-skalierung-20260914/checker.py validation.json
python3 -B universalraum-v14-F5-gemeinsame-welt-20260914/checker.py validation.json
python3 -B universalraum-v14-F6-transfer-20260914/checker.py validation.json
```

Jeweils auch `python3 -B -m unittest test_checker` und `-OO`.
Keine Änderung an Ledger, Papieren, Website oder T1–T8-Markern.
