# Q6: Stimmen dieselben Parameter mit mehreren Beobachtungen überein?

Universalraum v1.4, Follow-up-Lösung vom 14. September 2026.
Prüfer: `parameters.py` (eigenständig, nur numpy/scipy/sympy; keine Importe fremder Research-Checker).
Konventionen übernommen aus `universalraum-five-source-frontier-20260914/frontier.py`
(`gravity_and_matching`, `geometry_and_chirality`) und `RESULTS.md` Abschnitt
„Parameter und Gravitation genauer". **Keine T1–T8-, RH- oder TOE-Promotion.**
Ergebnis ist ein regulatorischer Mechanismustest, keine Behauptung dreier nativer
Standardmodellfamilien.

**Prüfstand:** 23 `need`-Bedingungen, alle grün. `python3 -OO` bytegleich (kein
`assert`, alle Wächter verwenden `RuntimeError`). `checker_sha256` in `parameters.json`.

---

## (a) Gemeinsame (joint) Konsistenz der Inflationskurve gegen ACT DR6 Tabelle 5

### Extrahierte ACT-Werte (P-ACT-LB2-Spalte)

Quelle: `sources/ACT_table5.png` (Seite 31, ACT DR6 v2, arXiv:2503.14452v2).
`pypdf` und `pdftotext` sind auf diesem Rechner **nicht verfügbar**, daher wurde die
Tabelle aus der PNG-Beschreibung direkt abgelesen. Die Werte sind als `quoted`
geführt (genau wie gedruckt):

| Größe | Wert (P-ACT-LB2) | Quelle |
|---|---|---|
| `log(10^10 A_s)` | `3.062^{+0.010}_{-0.012}` | Tabelle 5, PNG |
| `n_s` | `0.9752 ± 0.0030` | Tabelle 5, PNG |
| `r` | **nicht in Tabelle 5** | Tabelle ist ΛCDM (r=0) |

Die Tabelle weist **keine Kovarianz** aus; daher wird **unkorrelierte Fehlerannahme**
verwendet (explizit markiert). Die asymmetrische `logAs`-Unsicherheit wird
symmetrisiert: `σ_logAs = (0.010 + 0.012)/2 = 0.011` (Mittel), konservative Variante
`0.012`. Eine `r`-Schranke steht in der zitierten Tabelle **nicht** zur Verfügung;
literaturbasierte ACT-BB-Schranken werden bewusst **nicht** herangezogen.

### Konvention (identisch zu `frontier.py`)

`frontier.py` liest `Aobs = exp(3.062) · 1e-10`, behandelt `3.062` also als
`ln(10^10 A_s)`. Nur mit dieser Konvention reproduzieren sich die verified v1.4-Fakten
(`N = 56.62391`, `n_s = 0.96467923`, `3.5069 σ` marginal). `logAs` wird konsistent als
`ln(10^10 A_s)` definiert; die Tabellen-Unsicherheiten (in `log10`) werden mit `ln(10)`
in den `ln`-Raum gewandelt (markierte Annahme).

Modellkurve (parametrisiert durch N):
`A_s(N) = N² c3⁷/(24 π²)`, `n_s(N) = 1 − 2/N`, `r(N) = 12/N²`,
`logAs(N) = 10·ln(10) + ln(A_s(N))`.

### Reproduktion der bisherigen marginalen Diagnose

- `N` aus `A_s` zentral: **56.62391** ✓
- `n_s(N)` = **0.96467923** ✓
- marginale `n_s`-Abweichung: **3.5069 σ** (nur `n_s`, wie bisher berichtet) ✓
- Invariante `A_s(1−n_s)² = c3⁷/(6 π²)`: Residuum `< 1e-23` ✓
- `n_s`-Kalibrierung erzwingt `A_s` um Faktor **2.02842** zu groß ✓
- gemeinsames Treffen beider Zentralwerte erfordert `c3`-Verschiebung **−9.61 %**
  (abgelehnt: `c3` durch P1 fixiert) ✓

### Joint 2D-χ² (uncorrelated, dof = 1)

`χ²(N) = ((n_s(N) − 0.9752)/0.0030)² + ((logAs(N) − 3.062)/σ_logAs)²`,
minimiert über `N`. Freiheitsgrad = 1 (ein Kurvenparameter `N` gegen zwei Daten).

| Variante | `σ_logAs` (ln) | `N_best` | `n_s(N_best)` | `logAs(N_best)` | `r(N_best)` | `χ²_min` | `σ-Abstand` | p-Wert (dof=1) |
|---|---|---|---|---|---|---|---|---|
| **Mittel (primär)** | 0.02533 | **56.990** | 0.96491 | 3.0749 | **0.00369** | **12.033** | **3.469** | **5.23e-4** |
| Konservativ | 0.02763 | 57.057 | 0.96493 | 3.0751 | 0.00368 | 11.984 | 3.462 | 5.36e-4 |

`r(N_best) ≈ 0.0037` — eine `r`-Schranke aus Tabelle 5 existiert nicht (ΛCDM), daher
kein direkter Tabellen-Vergleich; der vorhergesagte Wert liegt weit unter typischen
ACT/Planck-BB-Obergrenzen.

### Was die gemeinsame Auswertung ändert

- **Bisher:** nur marginale `n_s`-Diagnose → **3.5069 σ** (bei fest auf `A_s`
  kalibriertem `N = 56.62391`).
- **Jetzt (joint):** freie Minimierung über `N` gegen **beide** Datenpunkte
  (`n_s` und `logAs`) → **σ-Abstand ≈ 3.47 σ** (`χ²_min ≈ 12.03`, p ≈ 5.2e-4, dof=1).

Die gemeinsame Auswertung mildert die Spannung **minimal** (3.51 → 3.47 σ): bei
`N_best ≈ 57` rutscht `n_s` leicht näher an den beobachteten Wert, und `logAs` liegt
mit `3.075` nahe am Zentralwert `3.062`. Das Bild bleibt eine **≈3.5-σ-Spannung**,
dominant getrieben vom Tilt `n_s`. Die Kurve kann beide Zentralwerte **nicht**
gemeinsam treffen, ohne `c3` (P1) zu verschieben — die joint-Auswertung bestätigt das
marginale Ergebnis, schwächt es aber nicht ab.

## (b) Yukawa-Hierarchie aus dem gemeinsamen Fluss-3-Hintergrund

Overlap-Operator auf dem `L=8`-Torus, Fluss 3, `m0=1`, `γ5`-Overlap
`D = I + γ5 sign(γ5 D_W)` — identisch nachgebaut aus `frontier.py`:

- Plaquette-Uniformität ✓, Wilson-Hermitizität ✓, **GW-Defekt < 1e-10** ✓
- **genau 3 Nullmoden**, **Index −3** (erklärte Orientierung) ✓
- Nullmoden orthonormiert ✓

Higgs-Profil **abgeleitet aus demselben Fluss-3-Hintergrund** (kein neues Textur-Input
außer der explizit markierten Modenauswahl in Kandidat i). Yukawa-Matrix
`Y_ab = Σ_x φ(x)·⟨Z_a(x)|Z_b(x)⟩` (Spinor-Innerprodukt pro Ort).

| Kandidat | Profil | Art | Eigenwerte | Hierarchie `max/min` |
|---|---|---|---|---|
| konstant | `φ=1` | Kontrolle | degeneriert | **1.0000** (Y ∝ I) ✓ |
| (i) `|Z_1|²` | Dichte einer Nullmode | **explorativ** (bricht S₃) | 0.01006, 0.01319, 0.02369 | **2.353** |
| (ii) `Σ_a|Z_a|²` | Gesamtnullmoden-Dichte | symmetrisch | 0.046941, 0.046942, 0.046942 | **1.00002** |
| (iii) Landau-Grundzustand | skalarer magnetischer Laplacian, tiefster Landau-Level (Entartung = 3), Dichte summiert über 3 Grundmoden | symmetrisch, aus gemeinsamen Fluss-3-Links | 0.046917, 0.046917, 0.046918 | **1.00008** |

Dichte-Uniformität von Kandidat (iii): relative Variation `9.6e-2` (endlicher
`L=8`-Torus, nicht exakt uniform, aber die Eigenwerte bleiben fast degeneriert).

### Verdict

Eine Hierarchie aus dem **gemeinsamen Fluss allein** entsteht **nur** im explorativen
Kandidaten (i), der die Permutationssymmetrie der drei Nullmoden **explizit bricht**
(ein neuer, nicht-fluss-abgeleiteter Auswahlschritt). Die symmetrischen Kandidaten
(ii) und (iii) liefern **keine Hierarchie**: (ii) ist `Y ∝ I` (Verhältnis 1), und
(iii) hat eine (im Rahmen der numerischen Auflösung) nahezu uniforme Dichte und
damit ebenfalls keine Aufspaltung.

**Ehrliches negatives Ergebnis:** der Fluss allein bricht die Symmetrie nicht. Eine
Hierarchie braucht ein **Symmetrie-brechendes Profil**; der minimale solche Input
ist die Auswahl **einer** Nullmode (Kandidat i). Dies bestätigt und verschärft die
Aussage in `RESULTS.md`: ein kosinusförmiges Profil spaltet zwar, ist aber neuer
Input — hier auf die minimalste solche Eingabe (Modenauswahl) zurückgeführt.

Dies ist ein **regulatorischer Mechanismustest**, nicht die Behauptung dreier nativer
Standardmodellfamilien.

## (c) Maschinengeprueftes Parameter-Ledger

Welche Parameter gehen in welche v1.4-Vorhersage ein; symbolische Reproduktion der
Zahlen (alle Checks grün):

| Test | Vorhersage | eingehende Parameter | geteilt | numerischer Zeuge |
|---|---|---|---|---|
| Inflationskurve (N-eliminiert) | `A_s(1−n_s)²=c3⁷/(6π²)`, `r=3(1−n_s)²=12/N²` | `c3` (P1), `N` (eliminiert) | `c3` | `N=56.62391`, `n_s=0.96467923`, Invariante 0 ✓ |
| Fluss-3 Chiralität (Overlap, L=8) | 3 Nullmoden, Index −3, GW<1e-10 | `flux=3`, `m0=1`, `L=8` | — | Index −3, 3 Nullmoden ✓ |
| Bandabstand 0.7 Δ (kantenlokal) | `QHQ ≥ 7/10 Δ` (LDL-Pivots positiv) | `t/Δ=1/20`, `arch=edge-local`, `Δ=1` | `t/Δ`, `Δ` | `7/10` exakt ✓ |
| Vorbereitungswahrsch. `w²/6` | `w=(1+Δ/√(Δ²+24t²))/2` | `t/Δ=1/20`, `Δ=1` | `t/Δ`, `Δ` | `w=0.98564`, `p=0.16192` ✓ |
| Gapkoeffizient −11.955494 (F4) | `ε²`-Koeffizient des F4-Beitrags | `t/Δ=1/20`, `arch=edge-local` | `t/Δ` | `−11.955494211502` ✓ |
| Echo-Verhältnis `17/32` | fresh/retained des Records | abgeleitet aus `w` + Recordgeometrie (keine neuen Parameter) | `t/Δ` (über `w`) | `17/32` exakt ✓ |

Symbolische Reproduktionen (sympy, alle `== 0` bzw. exakt):
- `w = (1 + Δ/√(Δ²+24t²))/2` aus `t/Δ` ✓
- `A_s(1−n_s)² = c3⁷/(6π²)` symbolisch `0` ✓
- `r = 3(1−n_s)² = 12/N²` symbolisch `0` ✓
- Echo `17/32` exakt ✓; Bandabstand `7/10 Δ` exakt ✓

### Geteilt vs. pro-Test (Q6-Antwort-Skelett)

**Global geteilt** (über mehrere Tests):
- `c3 = 1/(8π)` — P1, fixiert; geht in die Inflationskurve (und die Gesamttheorie).
- `t/Δ = 1/20` — erklärter Arbeitspunkt; geht in Bandabstand, `w²/6`, Gapkoeffizient,
  Echo (über `w`).
- `Δ = 1` — Einheitenwaehlung.

**Pro-Test-Inputs** (nicht geteilt):
- `flux = 3` (nur Chiralität/Yukawa)
- `N` (eliminiert, nur Inflation)
- `m0 = 1`, `L = 8` (nur Overlap)
- `arch = edge-local` (Bandabstand, Gapkoeffizient)

**Schlüsselbeobachtung:** `c3` (P1) und `t/Δ = 1/20` sind die einzigen **global
geteilten** Parameter. Die Inflationskurve teilt `c3` mit der Gesamttheorie, nutzt
aber **keinen** der anderen geteilten Parameter (kein `t/Δ`). Bandabstand, `w²/6`,
Gapkoeffizient und Echo hängen alle am selben Arbeitspunkt `t/Δ = 1/20` — sie sind
untereinander gekoppelt, aber unabhängig von der Inflation. Damit ist die
Inflations-Spannung (~3.5 σ) **isoliert** vom Rest: sie belastet weder die
Band-/Filter-/Echo-Konsistenz noch umgekehrt.

---

## Zurück an den Aufrufer

- **Check-Anzahl:** 23 (alle grün; `-OO` bytegleich).
- **ACT-Sigmen (P-ACT-LB2, genau wie gedruckt):** `log(10^10 A_s) = 3.062^{+0.010}_{-0.012}`,
  `n_s = 0.9752 ± 0.0030`, `r` nicht in Tabelle 5 (ΛCDM). Quelle: `sources/ACT_table5.png`
  (`pypdf`/`pdftotext` fehlen).
- **Joint (primär, σ_logAs = 0.011·ln10):** `N_best = 56.990`, `χ²_min = 12.033`,
  `σ-Abstand = 3.469`, `r(N_best) = 0.00369`, p ≈ 5.2e-4 (dof=1). Keine `r`-Schranke in
  der Tabelle; marginal-only-Vergleich: 3.5069 σ → joint 3.47 σ (minimal schwächer,
  weiterhin ~3.5 σ, dominant von `n_s` getrieben).
- **Yukawa-Hierarchien:** konstant 1.0000; (i) Einzeldichte 2.353 (explorativ,
  bricht S₃); (ii) Gesamtdichte 1.00002; (iii) Landau-Grundzustand 1.00008.
  → Fluss allein bricht Symmetrie nicht; minimale Symmetrie-brechende Eingabe ist
  die Auswahl einer Nullmode.
- **Ledger:** global geteilt `c3` (P1) und `t/Δ=1/20` (Arbeitspunkt) sowie `Δ=1`;
  pro-Test `flux`, `N`, `m0`, `L`, `arch`. Inflation ist über `c3` an die Gesamttheorie
  gekoppelt, aber nicht an den Arbeitspunkt `t/Δ`; die ~3.5-σ-Inflationsspannung ist
  daher von der Band-/Filter-/Echo-Konsistenz isoliert.
