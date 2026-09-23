# TFPT-Universalraum: Abschlussrunde zu den offenen Prüfpunkten A1–A8, B1–B4, T1–T8

Stand: 14. September 2026, 15:00. Forschungsnotiz, **kein** load-bearing Claim. NON-RH.
Keine Promotion nach `verification/`, Ledger, Papers oder Website.

Ausgangspunkt ist die priorisierte Liste vom 13:53 (A1–A8, B1–B4, T1–T8) auf Basis von
`TFPT_Universalraum_Gesamtkonstrukt_2026-09-14.md`, `Konsolidierte_Fortsetzung.md` und dem
`new-input-audit` in `experiments/theory-contracts/universalraum-paired-release-20260914/`.
Alle neuen Rechnungen liegen ausführbar in
`experiments/theory-contracts/universalraum-closure-20260914/` (README dort, fünf `validation_*.json`).

Evidenzkonvention wie in der Konsolidierung: *exakt* / *bedingt* / *offen* / *Gegenmodell* / *tot*.

---

## 0. Was heute tatsächlich geschlossen wurde — und was nicht

Geschlossen (endliche Rechnung, im Repo reproduzierbar):

1. **A4/B3, Multiplizität:** Das erste angeregte Clebsch-Singulett ist **exakt ein Quartett** — dichte
   Diagonalisierung des vollständigen 24 024-dim Sektors (kein Lanczos), und das Quartett ist die
   **Standarddarstellung von S₅ ≅ W(D₅)/2⁴**. Alle sieben tiefsten Singulettniveaus sind irreduzible
   W(D₅)-Darstellungen (1, 4, 20, 5, 10, 15, 5). Flag `exact_multiplicity_upper_bound` → erledigt.
2. **A4, alle Sektoren:** Alle 64 SU(4)-Sektoren (Σ dim = 6 952 660) mit F4-Korrektur in beiden
   Vermittlerkonventionen: Singulett bleibt Grundzustand, Quartett bleibt erste Anregung, Adjungierte (5,4,4,3)
   bleibt tiefstes Nichtsingulett. Flag `full_non_singlet_comparison` → erledigt.
3. **A3, Vermittlerlokalität:** entschieden durch Extensivität — geteilte Vermittlermoden erzeugen
   10·C(4L,2) ~ 8L² verbundene Paarterme (O(N²)); lokale Vermittler sind erzwungen. Konsequenz: der
   ε²-Koeffizient der Singulettlücke ist **−11.9555**, nicht +13.9018.
4. **A6, Phasenadapter (Tensorschicht):** aus dem Frenkel–Kac-Cocycle der E8 gerechnet. Jede native Kante ist
   nach einer Site-Farb-Vorzeichenwahl exakt der Antisymmetrisierer (Level 1, konsistent). Die uniforme
   Referenz ist unter **lokalen** Vermittlern exakt gauge-äquivalent (Level 2 lokal, konsistent); unter
   **geteilten** Vermittlern existiert eine ℤ₂-Flussobstruktion (6-Zyklus-Zeuge). Flag
   `CAR_native_phase_equivalence` (Tensorschicht) → **wahr unter lokalen Vermittlern**. A3 und A6 sind eine Frage.

Quantifiziert, aber offen:

5. **A4, Restschranke:** Cluster-Reihe konvergiert (6./4. Ordnung = 2–3 % bei t/Δ = 1/20; exakte Koeffizienten
   −2g⁴/Δ³ + 8g⁶/Δ⁵ bzw. +2g⁴/Δ³ − 12g⁶/Δ⁵). Eine thermodynamisch gleichmäßige Schranke braucht den lokalen
   Schrieffer–Wolff-Satz mit expliziten Konstanten; die konservative Pro-Ort-Stärke bei 1/20 ist ≈ 1.0 Δ und
   erfüllt dessen Voraussetzungen nicht. `higher_order_bound` bleibt offen.

Nicht geschlossen, weil nicht durch endliche Algebra schließbar (Abschnitt 4): A1 (Auswahlsatz), A2 (globale
Record-Kohärenz jenseits des Kriteriums L†L = K†K), A5 (angekleideter Filter, parallel in
`universalraum-closure-round-20260914/dressed_star.py`), A7 (Naht), A8 (externe Prüfer der Gen.-6-Dokumente),
B1 (RH), B2 (Faktorisierung), T1–T8.

---

## 1. Zahlen

### 1.1 Singulettsektor, dicht (Task `singlet-dense`)

| Niveau E/J | Multiplizität | W(D₅)-Darstellung | 2⁴ trivial | χ(Koordinatentransposition) |
|---|---|---|---|---|
| 11.045398337068423 | 1 | trivial | ja | +1 |
| **11.561762122802538** | **4** | **Standard von S₅ ([4,1])** | ja | +2 |
| 12.456023796267 | 20 | induziert (10er-Orbit, 2-dim) | nein | +2 |
| 12.690215501 | 5 | [3,2] von S₅ | ja | +1 |
| 12.778486704 | 10 | induziert | nein | −2 |
| 12.782757088 | 15 | induziert | nein | −3 |
| 12.795575028 | 5 | [3,2] von S₅ | ja | +1 |

Lücke 0.5163637857341143 J. Residuen ≤ 1.7·10⁻¹³; kleinster Abstand verschiedener Cluster unter den 60 tiefsten
Niveaus 4.27·10⁻³ J (Niveaus 10 und 15) — Multiplizitäten sind damit numerisch eindeutig. Σ|χ|²/|G| = 1 für alle
sieben Cluster (Irreduzibilität); tr H = 480 480 = 20·24 024 exakt (χ_{(4,4,4,4)}(Transposition) = 0).

Damit ist das „Dublett“ von Buch S. 18 nicht nur numerisch widerlegt (Konsolidierung R4), sondern die
Multiplizität 4 ist **symmetrieerzwungen**: sie ist die Dimension einer irreduziblen Darstellung der
Graphautomorphismen, und alle tieferen Entartungen sind ebenso erklärt. Ein Lanczos-Lauf mit k = 4 (Fugen-Contract)
konnte diese Struktur nicht sehen.

### 1.2 Alle 64 Sektoren mit F4 (Task `sectors-f4`, ε = 1/20)

| | nackt | korrigiert, geteilte Vermittler | korrigiert, lokale Vermittler |
|---|---|---|---|
| Singulett E₀ | 11.045398 | 11.739759 | 11.960549 |
| Singulett-Quartett E₁ | 11.561762 | 12.290877 | 12.447024 |
| Adjungierte (5,4,4,3), dim 15 | 12.133537 | 12.818330 | 12.990520 |
| Singulettlücke | 0.516364 | 0.551118 (+13.9018 ε²) | **0.486476 (−11.9555 ε²)** |
| magnetische Lücke | 1.088139 | 1.078571 | 1.029971 |

Ordnung der drei Niveaus in allen drei Spalten gleich. Max. Lanczos-Residuum über alle Sektoren 2.3·10⁻⁹;
F4-Hermitizitätsdefekt ≤ 2.6·10⁻¹². Die in `Konsolidierte_Fortsetzung.md` §6 als „erste numerische
Konsequenz“ genannte Korrektur +13.9018 ε² gehört zur Konvention geteilter Moden; unter der durch Extensivität
erzwungenen lokalen Konvention (1.3) kehrt sie das Vorzeichen um. Die Größenordnung (≈ 7 % der Lücke bei 1/20)
bleibt.

### 1.3 Vermittlerlokalität (Task `locality`)

Clebsch: 160 überlappende Kantenpaare (lokal), 60 disjunkte gleichlabelige Paare (nur bei geteilten Moden
gekoppelt). ℤ-Überlagerung mit L Kopien: 160 L überlappende Paare, aber 10·C(4L,2) gleichlabelige Paare —
L = 1…6: 60, 280, 660, 1200, 1900, 2760 (pro Ort 3.75 → 28.75). Mit |K₄|/J = 4(t/Δ)² pro Paar ist die
Energie vierter Ordnung bei geteilten Vermittlern O(N²). **Entscheidung:** lokale Vermittler. Die einzige
Alternative, Kavitätsnormierung t ~ N^{−1/2}, treibt J = 2t²/Δ → 0.

### 1.4 Phasenadapter (Task `phase-adapter`)

Cocycle ε(m,n) = (−1)^{mᵀBn}, B = tril(G,−1) + I in der Bourbaki-Basis der E8; Selbsttest: Cocycle-Identität,
Kommutatorfaktor (−1)^{mᵀGn}, Klammer-Antisymmetrie auf 3360 Wurzelpaaren. Native Vertexvorzeichen
ε(α_{s,a}, α_{t,b}) für 40 Kanten × 12 geordnete Farbpaare (48.3 % negativ in der Rohbasis).

| Gauge-Problem | Unbekannte | Gleichungen | Ergebnis |
|---|---|---|---|
| Level 1: jede Kante Antisymmetrisierer (η(s,a)) | 64 | 240 | **konsistent**, Rang 45, Nullität 19 |
| Level 2, geteilte Vermittler (η + ψ_μ, 60 Moden) | 124 | 480 | **inkonsistent**, Rang 115, Zeuge: 6-Zyklus 0–10–2–12–1–11 mit Farben (0,1), native Vorzeichen (+,+,−,−,−,+) |
| Level 2, lokale Vermittler (η + ψ pro Kante und Paar) | 304 | 480 | **konsistent**, Rang 285, Nullität 19 |

Alle 40 Quadrate haben trivialen Fluss; die Obstruktion liegt ausschließlich in der Relativphase verschiedener
Kanten mit **gemeinsamem** Vermittlerlabel — genau dem Freiheitsgrad, den die A3-Entscheidung abschafft.
Folge: Unter lokalen Vermittlern ist das native E8-Modell bis zur vierten Ordnung **derselbe Operator** wie das
uniforme Referenzmodell; die Fugen-Aussage „nach konsistenter Wahl lokaler Phasen gilt K_e†K_e = I − S_e“ ist
jetzt für alle 40 Kanten gleichzeitig bewiesen (Level 1). Nicht abgedeckt: die CAR-Schicht (fermionische
Jordan–Wigner-Vorzeichen bei zwei gleichzeitig offenen Lochpaaren) und der Adapter zwischen den Ebenen
Algebra → Mikrodynamik → Zustand → Beobachtung.

### 1.5 Restschranke (Task `remainder`)

Zweibond-Cluster, exakte Blöcke: verbundene Koeffizienten symmetrisch −2 g⁴/Δ³ + 8 g⁶/Δ⁵, antisymmetrisch
+2 g⁴/Δ³ − 12 g⁶/Δ⁵ (g = √2 t); Rest nach sechster Ordnung ≤ 2.7·10⁻⁹ bei g = 0.05. Verhältnis 6./4. Ordnung
bei t/Δ = 1/20: 2 % (sym), 3 % (asym). Globales Schur-Kriterium ‖V‖ < Δ: zertifiziert nur t/Δ ≲ 1/640.
Konservative Pro-Ort-Störstärke (5 Kanten, ‖K_e‖ = √2, ≤ 1 Vermittler): 20 t = 1.0 Δ bei 1/20. Der lokale
Schrieffer–Wolff-Satz (Bravyi–DiVincenzo–Loss 2011) verlangt kleinere Konstanten. **Offen**, jetzt mit Zahl.

---

## 2. Auflösung der Liste A1–A8

| Punkt | Status heute | Begründung / Verweis |
|---|---|---|
| A1 U-Regel ist Vorschlag, kein Auswahlsatz | **offen** (unverändert) | Auswahl von Belegung, Statistik, t, Δ, Zugriffen ist keine endliche Rechnung. Parallel: `universalraum-closure-round-20260914/selection_principle.py` (T1-micro, Kontextgewichte). Was heute dazukam: Level 1 zeigt, dass die Antisymmetrie *jeder* Kante aus E8 folgt und nicht gesetzt ist |
| A2 globale Record-Kohärenz | **teilweise** | Level 1 ist genau der Audit „alle Vertizes gegen K†K = I − S“ für die 40 nativen Kanten — bestanden. Die nicht-Cliffordsche Record-Ressource bleibt Zusatzannahme |
| A3 Vermittlerlokalität | **entschieden: lokal** | 1.3; blockiert T5 nicht mehr |
| A4 Rest + alle Sektoren | **Sektoren erledigt, Multiplizität erledigt, Rest quantifiziert** | 1.1, 1.2, 1.5 |
| A5 angekleidete Zustände / Filter | offen, parallel bearbeitet | `dressed_star.py` im Nachbar-Contract |
| A6 Phasenadapter | **Tensorschicht erledigt (unter lokalen Vermittlern)** | 1.4. Der Ebenenadapter „240 Wurzeln ≠ 240 CQ-Koordinaten“ bleibt offen und ist kein Vorzeichenproblem |
| A7 Naht | offen | keine endliche Rechnung; siehe Konsolidierung §6 C |
| A8 Evidenzlücken | **teilweise** | Die vier Flags des `new-input-audit` sind jetzt in-repo beantwortet; die externen Prüfer der Gen.-6-Dokumente fehlen weiterhin |

## 3. Auflösung der Liste B1–B4

- **B1 RH:** unverändert nicht gelöst. Nichts in dieser Runde berührt die fünf Teilschritte (kompatible Blöcke,
  Nullraumkopplung, Schur-Positivität über alle Stufen, dichte Fortsetzung, arithmetische Identität). Die heutigen
  Ergebnisse sind endliche Spektral- und Kohomologieaussagen über einen 16-Knoten-Graphen; sie liefern keine
  positive Darstellung von Q_ζ. Cholesky aus einer vorausgesetzten Positivität bleibt zirkulär.
- **B2 Faktorisierung:** unverändert. S_N(t) = N⁴gcd(t,N)⁴ ist verifiziert, die Auslese kostet O(N); kein Verfahren
  polynomial in log N steht.
- **B3 realistisch lösbar:** Punkt „C16-Spektralfrage“ ist erledigt (1.1, 1.2). Hamiltonoperator-Identifikation
  (Clebsch vs. Tetramer vs. Kette) ist über die jetzt exakt bekannten Spektren und Symmetriedarstellungen
  möglich: das Clebsch-Modell hat W(D₅)-Multipletts 1, 4, 20, 5, …; der vollständige Tetramer hat S₄-Multipletts
  1, 45, 40, 135, 35; die Kette hat Translations-/Reflexionsquantenzahlen — drei disjunkte Fingerabdrücke.
  Gedächtnisdiagnostik (1 vs 17/32, 1 vs 1/2) unverändert verfügbar.
- **B4 Reihenfolge:** bestätigt; A6 (Ebenenadapter) bleibt die Voraussetzung für B1.

## 4. T1–T8 nach dieser Runde

| Tor | Zugewinn heute | Bleibt |
|---|---|---|
| T1 | Kantenantisymmetrie ist E8-erzwungen (Level 1), nicht gesetzt; Vermittlerlokalität ist durch Extensivität festgelegt | Auswahl von Belegung, Statistik, t, Δ, Zugriffen |
| T2 | — | native chirale Naht |
| T3 | — | skalierende Geometrie, gemeinsamer Kegel |
| T4 | — | Index 3, Spiegelentkopplung, Spin(10)-Obstruktion (Konsolidierung §5.3) |
| T5 | Alle Sektoren, exakte Multiplizitäten, A3 entschieden, Rest quantifiziert (2–3 % Cluster) | thermodynamisch gleichmäßige Schranke, Vielzellenlimes |
| T6 | — | Transfer mit Unsicherheiten; Spannungen (α 1.897 σ, μ/τ, Higgs, A_s, Protonzweige) unverändert |
| T7 | — | Spin-2-Pol |
| T8 | — | Reservoir, Anfangszustand, Funktional |

Alle acht Tore bleiben offen. Die zentrale Integrationsfrage der 13:53-Liste („dieselbe unveränderte
mikroskopische Regel für Austausch, selektive Phasenoperationen und Rohstatistik“) ist um eine Stufe
präziser: Unter lokalen Vermittlern **ist** die native E8-Vertexregel und das Referenzmodell dieselbe Regel bis
zur vierten Ordnung (1.4). Was noch fehlt, ist nicht mehr die Kopplung, sondern Präparation, Record und
Auslesung aus derselben Regel.

## 5. Korrigierte Reihenfolge

1. **Referenzvertrag umstellen** auf lokale Vermittler: F4 ohne die 60 disjunkten Paarterme; Lückenkoeffizient
   −11.9555 ε² statt +13.9018 ε². `singlet_f4.py` und `Konsolidierte_Fortsetzung.md` §5.3/§6 entsprechend markieren.
2. **Restschranke** mit dem lokalen SW-Satz: benötigte Eingabe ist die tatsächliche Pro-Ort-Norm (nicht die
   konservative 20 t), berechenbar aus dem expliziten H_mic; Ziel ist eine zertifizierte obere Schranke für t/Δ.
3. **CAR-Schicht** des Adapters: fermionische Vorzeichen bei zwei offenen Lochpaaren gegen die Tensorkonvention
   auf dem 129-dim Zweibondcluster prüfen (endlich, exakt).
4. **A1/T1-Auswahlsatz** — jetzt der eigentliche Engpass; danach A5, A7.
5. B1 erst nach dem Ebenenadapter.

## 6. Reproduktion

```sh
cd experiments/theory-contracts/universalraum-closure-20260914
python3 test_closure.py                    # 5 Guard-Tests
python3 closure_checks.py all-light        # Phasenadapter, Lokalität, Rest (Sekunden)
python3 closure_checks.py singlet-dense    # ~30 min, ~20 GB RAM
python3 closure_checks.py sectors-f4 --k 8 # ~30 min
```

Ergebnisdateien: `validation_singlet_dense.json`, `validation_sectors_f4.json`, `validation_phase_adapter.json`,
`validation_locality.json`, `validation_remainder.json`. Umgebung: Python 3.14.3, NumPy 2.4.2 (Accelerate),
SciPy 1.17.0, SymPy 1.14.0; 32 Kerne, 550 GB RAM.
