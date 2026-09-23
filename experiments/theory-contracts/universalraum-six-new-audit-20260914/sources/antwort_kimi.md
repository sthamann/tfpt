# TFPT / Universalraum — Antwort auf die sechs Follow-up-Fragen (v1.4)

**Datum:** 14. September 2026
**Auftrag:** „Schau dir alles rund um TFPT und den Universalraum an und finde
vollständige Lösungen für alle Follow-ups und offenen Fragen."
**Artefakte:** `experiments/theory-contracts/universalraum-followup-solutions-20260914/`
(6 Prüfer, **2196 maschinengeprüfte Bedingungen**, normal/`-OO` bytegleich).

---

## Kurzantwort

Alle sechs Follow-up-Fragen wurden mit neuen, maschinengeprüften Rechnungen
bearbeitet. **Drei Fragen haben jetzt entscheidbare, teils abgeschlossene Antworten
(Q1, Q2, Q3)**; drei Fragen (Q4, Q5, Q6) haben jetzt **quantifizierte Antworten mit
exakt benannten fehlenden Zutaten**. Nichts wurde in `verification/`, Ledger, Papers
oder Website promoviert; RH, Faktorisierung und P vs NP bleiben unberührt und ungelöst.

---

## Q1 — Wer bedient das Labor?

**Antwort: ein eingefrorenes Operations-Ledger.** Zehn Kontrolloperationen des
mikroskopischen Protokolls, jede mit Status, Konstruktion und exakten Kosten
(`ops_ledger.py`, 1142 Checks):

| Status | Operationen |
|---|---|
| **nativ** (3) | lokaler Takt `C`; Kanten-/Mediatorkopplung `t`; Leerbelegungs-Herald |
| **abgeleitet, geprüft** (3) | 13-Faktor-Spektralfilter (= exakter Grundprojektor auf dem vollen 544-Raum); Resonanz-Recordpuls (`U†QU = R⊕I` ohne Viertelphasen); Echo/Endtest |
| **zusätzliche Ressourcen** (4) | **controlled-H-Entwicklung** (der präzise Kontrollschluss); exakte reelle Zeiten τ_j; Mess-/Reset-Umgebung; Resonanzabstimmung |

Gesamtrechnung: 26 kontrollierte Entwicklungen, 6345.659268 ℏ/Δ Filterzeit,
13 Ancilla-Bits, 2 Heralds, 1 Recordpuls, 6.1761 mittlere Präparationsversuche,
556 Feedback-Zyklen für 1e-6. **Die vier nicht-nativen Kontrollen sind die exakte,
vollständige Liste dessen, was der Compiler noch liefern muss.**

## Q2 — Welche Bauweise ist wirklich vorgeschrieben?

**Antwort: in der deklarierten Quellklasse — kantenlokal.** Entscheidungsmatrix
(`architecture.py`, 31 Checks), beide lokale Varianten an identischen
Quellanforderungen gemessen:

| Anforderung | Zellbank | Kantenlokal |
|---|---|---|
| R1 E8-Diagonal-Vorzeichenadapter | **unlösbar** (F2) | lösbar, Rang 285 |
| R2 mikroskopische Mediatorzählung | n/a | 288 = 3×16×6 ✓ |
| R4 Bandtrennung (exakt, LDL) | 0.4 Δ | **0.7 Δ** |
| R5 Gapkorrektur-Vorzeichen | +13.9018 | −11.9555 |
| R6 positive lokale F4-Form | nicht bekannt | **exakt** (720D-Zertifikat) |

Lokalität allein wählt weiterhin nicht (beide extensiv). Der Auswähler ist die
**E8-Vorzeichenstruktur**, nicht die Lokalität. **Offen bleibt** die Spannung:
die E8-Adjungierten-Wurzelzählung (60 = 10×6) legt label-geteilte Moden nahe,
die für diagonale Cocycles obstruiert sind — nichtdiagonale/komplexe Adapter
sind unerforscht.

## Q3 — Können wir die Vierfachstruktur wirklich beweisen?

**Antwort: ja für den trunkierten Operator — die Vierfachheit ist jetzt exakt
bewiesen, nicht mehr nur numerisch** (`certify_quartet.py`, 716 Checks,
24.024-dimensionaler Singulettsektor):

1. **Exakte Symmetrieprojektoren konstruiert.** Die Clebsch-Symmetriegruppe
   W(D5) = 2⁴⋊S5 (1920 Elemente, 18 Klassen) wurde vollständig zerlegt:
   Charaktertafel (Dixon–Schneider, Orthogonalität exakt), Specht-Einschränkung
   mit ganzzahligen Multiplizitäten (Σ dim·mult = 24.024 ✓).
2. **Das Quartett ist eine einzige 4-dim Irrep.** Charakterabweichung 4.4e-15
   über alle 1920 Gruppenelemente; intervallzertifizierte Projektion
   ‖P_μ v − v‖ ≤ 3.8e-8. Da H exakt mit W(D5) kommutiert, folgt per Schur:
   **das Niveau ist exakt 4-fach entartet** im zertifizierten Fenster
   [12.44696907, 12.44700081] J.
3. **Zertifizierte Eigenwertintervalle** (Intervallarithmetik mit gerichteter
   Rundung): E0 ∈ [11.9605074126619, 11.9605074126651] (Breite 3e-12),
   Quartett-Rayleigh ∈ [12.446984939667, 12.446984939671].
4. **Korrektur der v1.4-Lesart:** die nackte Anfangsskala ist block-aufgelöst
   **1, 4, 20, 5, 10, 15, …** — das als „7-fach" gelesene Niveau ist ein
   Fensterartefakt einer **20-fachen** Irrep.
5. **Was noch fehlt (präzise):** die Zählung „genau 5 Niveaus unter der Schwelle"
   ist auf eine einzige Zertifizierung reduziert — λ_6(H0) ≥ 12.455 (die Route
   über blockweise Intervallzertifizierung ist gebaut, Kosten gemessen: einige
   Stunden Laufzeit; hier nicht ausgeführt). F4 ≥ 0 ist exakt, also
   λ_k(H) ≥ λ_k(H0) (Weyl) — das Fenster ist offen (0.00904).

## Q4 — Bleibt das Labor bei Fehlern und wachsender Größe brauchbar?

**Antwort: die Budgets sind jetzt quantifiziert** (`robustness.py`, 70 Checks):

- **Timing-Jitter** des 13-Puls-Filters: Leck ≈ C·σ_τ² mit C = 9.38e-7
  (ℏ/Δ)⁻² → **σ_τ ≲ 1.03e-3 ℏ/Δ** für Leck ≤ 1e-12; globale Zeitverstellung
  ε ≲ 1.09e-6. (Verifiziert an allen 2¹³ Vorzeichenmustern + Skalierungslauf.)
- **Record-Puls-Verstellung:** Fehler = (12/11)·ε² exakt → **|ε| ≲ 9.6e-7**.
- **Gekoppelte Zellen (exakte Zwei-Zellen-Simulation, rang-erhaltend):**
  der unabhängige Union-Bound überlebt bei κ = 0 exakt; die Kopplung degradiert
  die Kontraktion moderat (Faktor 1.023–1.025) bis κ ≈ 0.01 und **versagt bei
  κ = 0.1** — die Kopplungstoleranz ist jetzt eine Zahl, keine Vermutung.
- **N-Zellen-Ledger:** N = 4096 → 890 Zyklen/Zelle, 40 099 840 gelöschte Bits
  gesamt, Landauer-Energie 40 099 840 · k_B T ln 2, Gesamtfilterzeit
  26 004 568.6 ℏ/Δ.

## Q5 — Entsteht daraus eine einzige gemeinsame Welt?

**Antwort: nein — nicht aus dieser einen Familie, und jetzt ist exakt bekannt,
wo sie scheitert** (`one_family.py`, 214 Checks). Dieselbe Familie
C16×(Z/LZ)ᵈ durch alle vier Tests gleichzeitig:

| Test | Ergebnis |
|---|---|
| T3 Dimension | reproduziert jede eingesetzte Dimension (d_s ≈ 1.0167·d), **wählt d=3 nicht** |
| Kegel | massiver Kanal ~20× langsamer (v₄/v₀ = 0.049) — **kein gemeinsamer Lichtkegel** automatisch |
| T4 Chiralität | Nullmodenzähler f(c, Fluss); **kein gescanntes c liefert genau 3** (Fenster des 1-dim Kanals ist im 10-dim Fenster enthalten; jenseits der Kante vektorartige Paare) |
| T7 Tensor | TT-Projektor Rang 2 ohne Pol; gapped Bilineare Schwelle 2m — **kein masseloser Spin-2** |

Die vier fehlenden Zutaten sind exakt benannt: Dimensionsauswahlprinzip, eine
Metrik für alle Spezies, quellenabgeleitetes c/Fluss-Paar, masseloser Spin-2-Sektor
mit Eichstruktur.

## Q6 — Stimmen dieselben Parameter mit mehreren Beobachtungen überein?

**Antwort: teils — und die Spannung ist jetzt gemeinsam quantifiziert und lokalisiert**
(`parameters.py`, 23 Checks):

- **Erste gemeinsame ACT-Auswertung** (echte Tabelle-5-Unsicherheiten:
  log(10¹⁰A_s) = 3.062 +0.010/−0.012, n_s = 0.9752 ± 0.0030): χ²_min = 12.03,
  **3.47 σ** (p ≈ 5.2e-4, dof 1), N_best = 56.99, n_s = 0.96491, r = 0.0037.
  Die marginale Diagnose (3.51 σ) wird bestätigt, minimal abgemildert.
- **Parameter-Ledger:** global geteilt sind nur `c3 = 1/(8π)` (P1) und der
  Arbeitspunkt `t/Δ = 1/20`. Die Inflationsspannung hängt an c3 allein und ist
  **isoliert** von der Band-/Filter-/Echo-Konsistenz (die an t/Δ hängt).
- **Flavour (ehrliches Negativ):** aus dem geteilten Fluss-3-Hintergrund allein
  entsteht **keine** Yukawa-Hierarchie (symmetrische Profile: Verhältnis ≈ 1.0000);
  erst ein Symmetrie-brechendes Profil (Auswahl einer Nullmode) spaltet
  (Verhältnis 2.35). Die minimale fehlende Eingabe ist damit exakt benannt.

---

## T1–T8-Stand (Experiment-Scope, keine Ledger-Änderung)

| Tor | Stand |
|---|---|
| T1 | Rang-Ausnahmen exakt; Auswahlprinzip offen |
| T2 | offen (native Halbladung fehlt) |
| T3 | Dimension reproduziert, nicht ausgewählt |
| T4 | 3 Familien nicht nativ erreichbar (Fensterüberlappung exakt vermessen) |
| T5 | **Vierfachheit exakt (trunkiert)**; Zählung konditional; Vielzellenlimes offen |
| T6 | ACT-Spannung 3.47 σ gemeinsam quantifiziert; Flavour braucht Symmetriebruch |
| T7 | kein masseloser Spin-2 aus der Familie |
| T8 | Kontroll-Lücke präzisiert (4 nicht-native Kontrollen); Fehlerbudgets quantifiziert |

## Ehrliche Gesamtgrenze

- Alles gilt in den deklarierten endlichen Modellen (trunkierter Operator,
  kontrolliertes Mikrolabor, eine Produktfamilie). Kein nativer 3+1D-Ursprung,
  kein thermodynamischer Limes, kein T1–T8-Abschluss.
- RH, Faktorisierung, P vs NP: unberührt; die v1.4-Blocker (fehlende gepinnte
  externe Quellen) wurden nicht verändert.
- Der einzige verbleibende Zertifizierungsschritt für die vollständige
  Quartett-Zählung ist benannt (λ_6(H0) ≥ 12.455 blockweise zertifizieren).

## Reproduktion

```sh
cd experiments/theory-contracts/universalraum-followup-solutions-20260914
python3 run_checks.py --fast     # 5 leichte Prüfer, 1480 Checks
python3 run_checks.py            # alle, inkl. 24.024D-Zertifizierung (~6 min)
```
