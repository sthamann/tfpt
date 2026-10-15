# Vier-Moden-Spektralfluss des chiralen Möbius-Cover-Fermions

Auftrag (Codex, 15.10.): Codex' Vorschlag T(p) = Pp + a im chiralen Achtfold prüfen. Außerdem
klären, ob und wo der originale CAR-Windungsoperator schon konstruiert ist und ob das
source-selected P1/Nahtprinzip die nötige neutrale Permutation bzw. Sektormarkierung liefert.
Die tatsächliche positive Operatorwirkung soll ausgewertet werden, ohne einen neuen freien
Operator zu wählen.

Status **PARTIAL**, keine Promotion. `python3 checker.py`: 2672 exakte Prüfungen
(sympy/Fraction). Davon sind 2× (150 Zustände × 9) Fock-Stichproben; der Rest sind
symbolische Identitäten und Quellpins.

## Eingabe (vorhanden, nicht neu gewählt)

`moebius-clock-fold-20261014/PROOF.md:16–21` gibt die Faltung. Ein chiraler komplexer Kanal ψ
läuft auf dem Möbius-Randkreis der Länge 8l. Die Fourierkanäle χ_k = Σ_j ω^{−jk} ψ_j enthalten
genau die Cover-Moden m = 8n + k. Das Faltungszeitgesetz lautet

    K_α = Σ_k (L0_k + δ_k p_k),   δ_k = (k+α)/8 − ½,   α ∈ {¼, ¾}.

Dass es **einen** chiralen Kanal entlang des ganzen Möbiusrands gibt, ist dort ausdrücklich
die erste zusätzlich gewählte Geometrie (`moebius-clock-fold-20261014/PROOF.md:70–75`). Der
QWZ-Kragen hat zwei Ränder entgegengesetzter Chiralität.

## Satz T (geprüft)

**A – Nullmoden, symbolisch in α und j.** Mit s = q/2, r0 = p* = (½⁴, −½⁴), a = s + r0 =
(1⁴, 0⁴) und P = Blocktausch k ↔ k+4 gilt:

* q(Tp) = q(p) + 4 und T²p = p + q.
* K(Tp) − K(p) = q(p)/2 + ¾ + α/2 = K(p+s) − K(p).
* ν·(Tp − p) − ν·s = r0·p − 1 mit ν_k = (k+j)/8. Für ganzzahliges p ist e^{2πi r0·p} =
  (−1)^{q(p)}. Der g-Charakter stimmt also auf D8 überein, auf ungeradem CAR kommt (−1)^Q
  hinzu. Für C = g² stimmt er.
* K(a) = K(s) = ¾ + α/2 ∈ {7/8, 9/8}, aber a ≠ s. T ist eine affine Permutation, keine
  Translation.

Alle Zahlen von Codex sind damit unabhängig reproduziert.

**A8 – Warum die Energien übereinstimmen.** Es gilt a = s + p*. Dabei gilt K(p*) = 0 für
jedes α, und s·p* = 0. Daraus folgt K(a) = K(s) + s·p* + K(p*) = K(s).

a liegt in D8. s und p* liegen beide in der Spinor-Nebenklasse D8 + s. Der Nullmodenteil von T
ist also P, gefolgt von der Translation um s + p*: eine E8-Spinortranslation mal der
K-nullen neutralen Spinortranslation p* (dem Partner im neutralen Doublet G0). Jeder Faktor
allein verlässt die CAR, ihr Produkt nicht.

Das ist die Achtfold-Entsprechung zu `source-graded-locality-20260920/PROOF.txt:111`,
e_i = F_aux(r_i) − a_i m. Dort ist der neutrale Faktor ein massives ungerades Paar, hier die
K-nulle Richtung p*. Gleichung (4a) wird im Checker reproduziert (G1, alle acht i, mit F aus
`source-flux-index-20260920`).

**B – volle Fockwirkung, Oszillatoren eingeschlossen (Maya-Diagramme).**

* T = σ⁴ mit c_m → c_{m+4}.
* K_α ist exakt der freie Cover-Hamiltonoperator Σ_m (m+α)/8 :N_m:. Er ist positiv mit dem
  eindeutigen Nullzustand m < 0.
* p(TS) = P p(S) + a und N_k(TS) = N_{Pk}(S): Die Oszillatoren werden nur permutiert.
* Für **jeden** Zustand gilt K(TS) − K(S) = Q(S)/2 + c_α mit c_α = ¾ + α/2. Daraus folgen

      U_T† K_α U_T = K_α + Q/2 + c_α,        U_T(t) = U_T e^{it(Q/2 + c_α)}.

  U_T bildet Moden auf Moden ab, also bleiben CAR und Bilineare exakt erhalten. Die Zeitphase
  hängt von der Ladung ab und ist keine einzelne skalare Frequenz. Sie ist identisch mit dem
  Heisenberggesetz der E8-Nullmodentranslation e^{s}.
* Geometrische Deckdrehung g (Translation um l): g U_T g^{−1} = −i (−1)^Q U_T.
* U_T ist gerade, hat Ladung 4 und erhält das Gitter Z⁸. Es erzeugt keine halbzahligen
  Cartanladungen.

**C – Potenzen.** Der Multiplikator e^{2πi w x/(8l)} steigt genau für gerades w auf den
Kernkreis (Länge 4l) ab, und zwar mit Kernwindung w/2.

* σ² ist der Pullback der primitiven Kernwindung:
  K(σ²S) − K(S) = Q/4 + (1+2α)/8.
* T = (σ²)² ist die Kernwindung **zwei**.
* σ¹ steigt nicht ab.

## Wo der originale Windungsoperator steht (Suche in den Originalen)

* **P1-Naht:** `_archive/paper-latex/tfpt-42.tex:2323, 2327`: [u_Σ] = 1 ∈ K¹(S¹),
  SF(U_Σ) = 1, Δ_Seam = 2π („one full turn“). Dazu
  `_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex:551`:
  d_0(B) = |SF(U_Σ)| als erste Defektkoordinate. P1 gibt damit eine **Klasse**
  (Spektralfluss 1), aber keinen Modenshift, keine Kanalordnung m = 8n + k und keine
  Permutation P.
* **Volles QWZ:** `source-driven-carry-20260920/PROOF.md:16–35` ist der echte Flusspump. Er
  ist zahlerhaltend (Gesamtzahl 8N), die zweite Kante kompensiert, und der Peierls-Antrieb ist
  eine externe Eingabe (Z. 32). Z. 273–276 sagt: Ein globaler Spektralfluss-Unitär liefert
  keine Oszillatordressierung bzw. lokale Produkte. Das ist nicht der chirale Implementer.
* **Chiraler Implementer:** Er ist nur bosonisiert vorhanden, als Nullmoden-Ladungsshift auf
  ℓ²(L_charge) (`articles/2026-08-30/mmst_charged_scaling_limit_en.tex:691, 762`, mit der
  Annahme „norm one“). Außerdem als U_α in `half-twist-grade-carry` §3. Ein mikroskopischer
  CAR-Windungsimplementer des Möbius-Cover-Fermions ist in den durchsuchten Dateien nicht
  konstruiert. Gesucht wurde nach spectral flow, Spektralfluss, loop group, Shale/Stinespring
  und Laughlin.
* **Ψ_{λ,N}** (`mmst…:69, 263`) ist :exp(iλ·φ_N): mit Ladung λ auf dem
  kantenprojizierten Bosonraum. Laut Z. 311 ist er kein Fermionbilinear. Mikroskopisch ist er
  offen (ALG-EXH/FE-GEN). Round 7 konstruiert Ecken nur mit einem Z4-Flussregister
  (Z. 1882–1885).
* In D8-Koordinaten wird λ zu s. T hat zwar Ladung 4 = q(λ), aber T(0) = a ≠ s. T ist daher
  weder Ψ_λ noch dessen Nullmodenshift.

## Antwort

1. **Codex' T ist korrekt und quellnah.** Es ist exakt σ⁴ des einen Cover-Fermions, also
   keine freie Wahl, **sobald** der einzelne chirale Möbiuskanal gegeben ist. P ist dann
   durch die Modenordnung m = 8n + k erzwungen. Die positive Operatorwirkung ist vollständig
   bestimmt: U_T† K U_T = K + Q/2 + c_α auf dem ganzen Fockraum.
2. **Nicht von P1 geliefert:**
   - der einzelne chirale Möbiuskanal (gewählte Geometrie, eine Domänenwand ist nötig);
   - die Potenz 4: P1 hat SF = 1. Auf dem Kernkreis ist das σ², auf dem Randkreis σ¹. T ist
     in beiden Lesarten nicht primitiv, sondern Kernwindung 2 bzw. vierfacher Randumlauf;
   - welcher Kreis U_Σ trägt. Das legen die Originalstellen nicht fest.
3. **Statistik:** T bleibt in der geraden CAR. Der E8-Spinorsektor entsteht aus T erst durch
   Abspalten des K-nullen Faktors p*. Das ist nicht in der CAR möglich: Es braucht genau die
   fehlende Sektorerweiterung D8 → D8 ∪ (D8+s).
4. **Erste nicht gegebene Quellformel:** Gesucht ist ein Operator, der auf der Quelle den
   p*-Faktor (die K-nulle neutrale Spinortranslation) als Sektorintertwiner realisiert, oder
   gleichwertig die chirale Ein-Rand-Einschränkung mit Kernwindung 2 als Quellbewegung.
   Keines von beiden steht in den geprüften Originalen.
