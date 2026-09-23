# Ergebnisse Q1 — Primitive-Operations-Ledger (Universalraum v1.4)

Stand: 14. September 2026. Contract:
`experiments/theory-contracts/universalraum-followup-solutions-20260914/`.

**Evidenzkonvention** (wie v1.4): `native_declared` = aus den Compiler-Primitiven
(Takt `C`, native Kopplung `t`) gesetzt; `derived_checked` = Operatoridentität
auf den tatsächlichen Matrizen nachgerechnet; `additional_resource` = erklärtes
externes Hilfsmittel, nicht aus den Primitiven 1–2 ableitbar. NON-RH. Keine
T1–T8-Schließung, keine Promotion in `verification/`, Ledger, Papers oder
Website. Theorievertrag = interne Konsistenz.

## 1. Ergebnis in einem Satz

**Von den zehn Kontrolloperationen des mikroskopischen Protokolls sind drei
native Primitive (Takt, Kopplung, Heralds), drei sind aus diesen plus erklärten
Ressourcen maschinell abgeleitet (13-Faktor-Filter, Resonanz-Aufzeichnungspuls,
Echo/End-Test), und vier bleiben zusätzliche Ressourcen — davon die
controlled-H-Entwicklung als der präzise verbleibende Kontrollschluss.**

## 2. Reproduktion

```sh
cd experiments/theory-contracts/universalraum-followup-solutions-20260914
python3 ops_ledger.py          # 1142 Bedingungen, ~0.5 s
```

Quellpin `ops_ledger.py` SHA-256 `f90675a2…`; Ergebnisse in `ops_ledger.json`.

## 3. Tabelle der Operationen

| # | Operation | Status | Konstruktion (Stichwort) | Kosten |
|---|---|---|---|---|
| 1 | lokaler Takt `C` | `native_declared` | 3-Zyklus (1,2,0,3) auf Träger 0; `tick = kron(C, I_64)` | 1 nativer Takt |
| 2 | Kanten-/Mediatorkopplung `t` | `native_declared` | 288×256-Kopplung `M`, `H = [[0, t M^T],[t M, Δ I_288]]`, `t/Δ = 1/20` | nativer Hamilton-Term |
| 3 | freie Zeitentwicklung `exp(-i τ H)` | `additional_resource` | exakte reelle Zeiten `τ_j = πℏ/(E_j−E_0)` | 3172.829634 ℏ/Δ pro Filter |
| 4 | controlled-H-Entwicklung | `additional_resource` | Hadamard-Test-kontrollierte Version von `exp(-i τ_j H)` | 13 pro Filter, 26 gesamt — **die Lücke** |
| 5 | 13-Faktor-Spektralfilter | `derived_checked` | geordnetes Produkt `A_j = (I + exp(−i τ_j(H−E0)/ℏ))/2` = `P0_dressed` auf vollem 544-Raum | 13 kontrollierte Entwicklungen, 3172.829634 ℏ/Δ |
| 6 | leere-Mediator-Herald | `native_declared` | Besetzungsmessung der 288-dim Mediatoren; `P_bare P0 P_bare = w P_Ω` | 1 Besetzungsmessung |
| 7 | Resonanz-Aufzeichnungspuls `U_res` | `derived_checked` | 22-dim `U = [[P+, −i W^T],[−i W, 0]]`, 44-dim `= kron(U, I_2)`; `U^† Q U = R ⊕ I_12` | 1 Resonanzpuls + 1 Besetzungsabfrage |
| 8 | Reset via Feedback-Kanal | `additional_resource` | `E(ρ) = KρK^† + Tr[(I−K^†K)ρ] ρ0`, `K = ∏_{j=1,2,3}(I−S_{0j})/2` | 556 Zyklen für 1e-6; 8 Farb- + 3 Record-Bits/Zyklus |
| 9 | Echo-/End-Test | `derived_checked` | gleicher mikroskopischer Filter am Start und Ende; Takt `C` plus ± Projektoren auf Träger (0,1) | 26 kontrollierte Entwicklungen, 6345.659268 ℏ/Δ |
| 10 | Amplifikation (optional) | `additional_resource` | 52 controlled-H-Aufrufe für zwei Schritte; `φ = arccos(1 − (3−√5)/(4a))`, `a = w/6` | 52 controlled-H-Aufrufe |

## 4. Maschinell geprüfte Identitäten (Auswahl)

- **Op 2 — 14-Niveau-Spektrum.** Alle 544 mikroskopischen Eigenwerte stimmen mit
  der analytischen Formel `E±(g) = (Δ ± √(Δ² + 4t²(6−2g)))/2` (g = 0, ½, …, 3)
  sowie dem dunklen Niveau `Δ` (Multiplizität 67) auf 1e-12 überein.
  Gram `M^T M = 6 I_256 − 2 G` auf 1e-13.
- **Op 5 — 13-Faktor-Filter.** Das geordnete Produkt über alle 13 nicht-Grund-Niveaus
  ergibt auf dem vollen 544-dim Raum exakt den gekleideten Grundprojektor
  `P0_dressed` (Norm < 1e-10). Skalarfilter hält das Grundniveau (`f[0] = 1`) und
  löscht alle 13 Nicht-Grund-Niveaus (< 1e-12).
- **Op 5 — negative Kontrolle.** Ein Filter über nur die 6 anderen *tiefen*
  Niveaus scheitert auf dem vollen Raum (`max|short[7:]| > 1e-5`): die oberen/dunklen
  Faktoren sind notwendig.
- **Op 6 — Herald.** `P_bare P0_dressed P_bare = w P_Ω` mit
  `w = (1 + 1/√(1+24t²))/2 ≈ 0.9856429312` (Norm < 1e-10).
- **Op 7 — Record-Puls.** `U_res^† Q U_res = R ⊕ I_12` ohne zusätzliche
  Viertel-Phasen (Norm 1.4e-15 < 1e-13). `W W^† = I_6` ( partielle Isometrie).
- **Op 8 — Feedback.** `K` fixiert `Ω` (< 1e-14); Kontraktions-Schranke
  `max eig(K^T K − |Ω><Ω|) ≤ β = (9+√17)/32 ≈ 0.4100970508` (mit 1e-13-Toleranz);
  Rate `r = 1−(1−β)/24 ≈ 0.97542071045`; `r^556 < 1e-6`;
  Fehlerboden-Multiplikator `1/(1−r) ≈ 40.6847`. 556 Einzelschritt-
  Gewicht- und Kontraktionsidentitäten逐一 geprüft.
- **Op 9 — Echo.** Bedingt gehalten `= w² ≈ 0.9714920`, frisch `= 17 w²/32 ≈ 0.5161051`;
  Präparationsrohwahrscheinlichkeit `= w²/6 ≈ 0.1619153`; unbedingtbeghalten
  `= w⁴/6 ≈ 0.1572994`, frisch `= 17 w⁴/192 ≈ 0.0835653`; Verhältnis frisch/gehalten
  exakt `17/32`; mittlere Versuche `≈ 6.1761`.
- **Op 10 — Amplifikation.** Zwei-Schritt-Verstärkungsidentität auf 2-Niveau-Toy:
  `|fin[0]|² = 1.0` (> 1 − 1e-13) mit `φ = arccos(1 − (3−√5)/(4a))`, `a = w/6`.

## 5. Gesamt-Ressourcenrechnung (Totals)

| Ressource | Wert |
|---|---|
| kontrollierte Entwicklungen (Start + Ende) | 26 |
| Gesamtfilterzeit | 6345.659268 ℏ/Δ |
| eine Filterzeit | 3172.829634 ℏ/Δ |
| kohärente Filter-Ancilla-Bits | 13 |
| Besetzungs-Heralds | 2 |
| Aufzeichnungspulse | 1 |
| mittlere Präparationsversuche | 6.1761 |
| Feedback-Zyklen für 1e-6 | 556 |
| Farb-Bits pro Reset-Zyklus | 8 |
| Record-Bits pro Reset-Zyklus | 3 |
| unabhängige Zellen (N = 4096) für globales 1e-6 | 890 Zyklen |

## 6. Die nicht-nativen Kontrollen — die Antwort auf Q1

Die folgenden Kontrollen sind **nicht** aus den nativen Primitiven (Takt `C`,
Kopplung `t`) ableitbar und bleiben zusätzliche Ressourcen. Diese Liste **ist**
die Antwort auf Q1:

1. **controlled-H-Entwicklung (Op 4)** — die Hadamard-Test-kontrollierte Version
   von `exp(−i τ_j H)` ist der präzise verbleibende Kontrollschluss. Sie wird weder
   vom Takt `C` noch von der nativen Kopplung `t` geliefert; ohne sie lässt sich der
   13-Faktor-Filter (Op 5) und damit das gesamte Protokoll nicht ausführen.
2. **Exakte reelle Zeiten `τ_j` (Op 3)** — die Wahl `τ_j = πℏ/(E_j − E_0)` ist ein
   erklärtes ideales Hilfsmittel; die Zeiten sind nicht aus Primitiven synthetisierbar.
3. **Mess- + Reset-Umgebung (Op 8)** — der Feedback-Kanal benötigt ein externes
   Bad mit Mess- und Reset-Fähigkeit (klassische Farb-Bits, Record-Bits).
4. **Resonanz-Abstimmung (Op 7)** — der Resonanzpuls muss auf den
   Record-Block-Übergang abgestimmt werden; die Resonanzbedingung ist ein
   zusätzliches Kalibrierungsdatum.

## 7. Ehrliche Abgrenzung

- `derived_checked` bedeutet **interne Konsistenz**: die Operatoridentität wurde
  auf den nachgebauten Matrizen nachgerechnet, nicht aus den Primitiven 1–2
  *hergeleitet*. Der Filter (Op 5) benötigt Op 3 + Op 4 + 13 Ancilla-Bits; der
  Record-Puls (Op 7) benötigt die Resonanzabstimmung; der Echo-Test (Op 9)
  benötigt zwei Filter plus Takt.
- `native_declared` (Op 1, 2, 6) sind die vom Compiler gesetzten Primitive bzw.
  die native physikalische Messung. Keine Aussage darüber, ob die physikalische
  Realisierung der Besetzungsmessung „kostenfrei" ist — sie ist als native
  Messung deklariert.
- Die controlled-H-Entwicklung (Op 4) ist **kein** Beweis, dass die Lücke
  unüberwindbar ist; sie ist die genaue Benennung dessen, was aktuell nicht aus
  Primitiven 1–2 folgt. Ein künftiger Konstruktionsschritt, der controlled-H aus
  Takt + Kopplung + freier Evolution synthetisiert, würde Op 4 nach
  `derived_checked` verschieben.
- Keine Aussage dieser Runde schließt T1–T8. Kein RH-, Faktorisierungs- oder
  P-vs-NP-Resultat.
