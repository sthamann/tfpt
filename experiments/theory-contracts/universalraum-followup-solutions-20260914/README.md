# TFPT / Universalraum — Follow-up-Lösungsrunde (14.09.2026)

Contract zu den sechs Follow-up-Fragen der Universalraum-Revision v1.4
(`universalraum-five-source-frontier-20260914`). Forschungsstand, **kein**
T1–T8-Abschluss, **keine** Promotion nach `verification/`, Ledger, Papers oder
Website; Theorievertrag = interne Konsistenz, nicht Scorecard-Evidenz.

## Fragen und Antworten im Überblick

| # | Frage | Antwort dieser Runde | Artefakte |
|---|---|---|---|
| Q1 | Wer bedient das Labor? | **Operations-Ledger**: 3 native Primitive, 3 abgeleitet-geprüft, 4 zusätzliche Ressourcen; controlled-H ist der präzise Kontrollschluss | `ops_ledger.py` (1142 Checks), `RESULTS_Q1.md` |
| Q2 | Welche Bauweise ist vorgeschrieben? | **Entscheidungsmatrix**: in der deklarierten Quellklasse (diagonaler E8-Cocycle + mikroskopische Sternzählung + positives F4) wird **kantenlokal** ausgewählt; Zellbank fällt an der F2-Obstruktion | `architecture.py` (31 Checks), `RESULTS_Q2.md` |
| Q3 | Vierfachstruktur beweisbar? | **Ja für den trunkierten Operator**: exakte W(D5)-Projektoren + Schur-Entartung + intervallzertifizierte Eigenwertfenster; Zählung auf eine präzise konditionale Aussage reduziert | `certify_quartet.py` (716 Checks), `CERTIFICATION_Q3.md` |
| Q4 | Fehler und Größe? | Jitter-/Verstellungs-Budgets quantifiziert (σ_τ ≲ 1e-3 ℏ/Δ; Record-Detuning |ε| ≲ 1e-6, Koeffizient exakt 12/11); exakte Zwei-Zellen-Kopplung: Union-Bound überlebt κ=0, moderate Degradation bis κ≈0.01, Versagen bei κ=0.1; N-Zellen-Ledger | `robustness.py` (70 Checks), `RESULTS_Q4.md` |
| Q5 | Eine gemeinsame Welt? | **Nein für die Familie C16×(Z/LZ)ᵈ**: alle vier Tests in einem Objekt, exakte Fehlerkarte; kein `c` liefert genau 3 chirale Moden | `one_family.py` (214 Checks), `RESULTS_Q5.md` |
| Q6 | Parameterübereinstimmung? | Gemeinsame ACT-Auswertung: **3.47 σ** Spannung (p ≈ 5.2e-4), isoliert vom Arbeitspunkt t/Δ; Yukawa aus geteiltem Fluss: **keine** Hierarchie ohne Symmetriebruch (ehrliches Negativ) | `parameters.py` (23 Checks), `RESULTS_Q6.md` |

## Kernresultate neu in dieser Runde

1. **Q3 (Flaggschiff):** Die Vierfachheit des ersten angeregten Niveaus des
   trunkierten Operators ist **exakt bewiesen**, nicht mehr nur numerisch:
   die vier Ritz-Vektoren spannen eine einzige 4-dimensionale Irrep von
   W(D5) = 2⁴⋊S5 (Charakterabweichung 4.4e-15 über alle 1920 Elemente;
   intervallzertifizierte Projektion ‖P_μ v − v‖ ≤ 3.8e-8). Da H exakt mit der
   Gruppe kommutiert, ist das Niveau per Schur **exakt 4-fach entartet** im
   zertifizierten Fenster [12.44696907, 12.44700081] (J-Einheiten).
   Zertifiziert: E0 ∈ [11.9605074126619, 11.9605074126651].
   Die exakte Singulett-Zerlegung in 18 W(D5)-Isotypiken ist vollständig
   berechnet (Multiplizitäten ganzzahlig, Σ dim·mult = 24.024 ✓).
   Die nackte Anfangsskala ist block-aufgelöst: **1, 4, 20, 5, 10, 15, …** —
   das v1.4-"7-fache" Niveau ist ein Fensterartefakt einer **20-fachen** Irrep.
   Verbleibender Schritt für die volle Zählung: λ_6(H0) ≥ 12.455 zertifizieren
   (Route und gemessene Kosten in CERTIFICATION_Q3.md §4).

2. **Q2:** Die E8-Vorzeichenstruktur (diagonaler Standard-Cocycle) ist mit der
   zellgeteilten Bank **unverträglich** (F2-System unlösbar) und mit kantenlokalen
   Vermittlern lösbar (Rang 285). Zusammen mit der mikroskopischen
   Mediatorzählung (288 = 3×16×6, pro Kante) und der positiven F4-Form wählt
   die deklarierte Quellklasse die kantenlokale Bauweise. Offen bleibt die
   Spannung, dass die E8-Adjungierten-Wurzelzählung (60 = 10×6) label-geteilte
   Moden nahelegt — nichtdiagonale/komplexe Adapter unerforscht.

3. **Q4:** Erste exakte Fehlerbudgets: Timing-Jitter σ_τ ≲ 1.03e-3 ℏ/Δ und
   globale Zeitverstellung ε ≲ 1.09e-6 für Filter-Leck ≤ 1e-12; Record-Puls-
   Verstellung |ε| ≲ 9.6e-7 (quadratischer Koeffizient exakt 12/11).
   Zwei-Zellen-Kopplung exakt simuliert (rang-erhaltend): Kontraktion
   degradiert moderat (Faktor 1.023–1.025) für κ ≤ 0.01 und versagt bei
   κ = 0.1 — die Kopplungstoleranz ist jetzt quantifiziert.

4. **Q6:** Erste **gemeinsame** (statt marginale) ACT-Auswertung mit den echten
   Tabellen-5-Unsicherheiten (log(10¹⁰A_s) = 3.062 +0.010/−0.012):
   χ²_min = 12.03, N_best = 56.99, n_s = 0.96491, r = 0.0037, p ≈ 5.2e-4.
   Die Spannung bleibt ≈3.5 σ (Tilt-dominiert) und ist nachweislich **isoliert**
   von der Band-/Filter-/Echo-Konsistenz (kein gemeinsamer Parameter außer c3).

5. **Q5 (ehrliches Negativ):** die einzelne Familie C16×(Z/LZ)ᵈ besteht **keinen**
   der vier Welt-Tests nativ; die vier fehlenden Zutaten sind exakt benannt
   (Dimensionsauswahl, eine Metrik für alle Spezies, quellenabgeleitetes
   c/Fluss-Paar, masseloser Spin-2-Sektor mit Eichstruktur).

6. **Q1:** Das Operations-Ledger friert die zehn Kontrollen ein und benennt die
   vier nicht-nativen (controlled-H, exakte Zeiten, Mess-/Reset-Umgebung,
   Resonanzabstimmung) mit exakten Kosten — die Antwortstruktur auf "wer bedient
   das Labor".

## Ausführen

```sh
cd experiments/theory-contracts/universalraum-followup-solutions-20260914
python3 ops_ledger.py        # ~1 s
python3 architecture.py      # ~1 min (F2-Algebra + 720D-Zertifikat)
python3 parameters.py        # ~1 min
python3 one_family.py        # ~3 min
python3 robustness.py        # ~5 min (Zwei-Zellen-Simulation)
python3 certify_quartet.py   # ~6 min (24.024-dim, Intervallzertifizierung)
```

Alle Prüfer sind eigenständig (nur numpy/scipy/sympy), überleben `python3 -OO`,
und schreiben jeweils ihr JSON mit `checker_sha256` und `T1_T8_closed: []`.

## T1–T8-Stand nach dieser Runde (Experiment-Scope, keine Ledger-Änderung)

| Tor | Stand nach dieser Runde |
|---|---|
| T1 | Rang-Ausnahmen exakt; Auswahlprinzip weiter offen (kein Auslesevertrag) |
| T2 | unverändert offen (native Halbladung fehlt) |
| T3 | Familie reproduziert Dimension, wählt sie nicht (Q5) |
| T4 | Nullmoden gezählt als f(c, Fluss); 3 Familien nicht nativ erreichbar (Q5) |
| T5 | **Vierfachheit exakt (trunkiert)**; Zählung konditional; Vielzellenlimes offen |
| T6 | Gemeinsame ACT-Spannung 3.47 σ quantifiziert; Flavour braucht Symmetriebruch-Input |
| T7 | kein masseloser Spin-2 aus der Familie (Q5) |
| T8 | Kontroll-Lücke präzisiert (Q1); Fehlerbudgets quantifiziert (Q4) |

RH, Faktorisierung und P vs NP bleiben unberührt und ungelöst; die v1.4-Blocker
(gepinnte externe Quellen) wurden nicht verändert.
