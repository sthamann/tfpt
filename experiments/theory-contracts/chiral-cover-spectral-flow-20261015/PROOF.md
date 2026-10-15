# Vier-Moden-Spektralfluss des chiralen Möbius-Cover-Fermions

Auftrag (Codex, 15.10.): Codex' Vorschlag T(p) = Pp + a im chiralen Achtfold prüfen. Außerdem
klären, ob und wo der originale CAR-Windungsoperator schon konstruiert ist und ob das
source-selected P1/Nahtprinzip die nötige neutrale Permutation bzw. Sektormarkierung liefert.
Die tatsächliche positive Operatorwirkung soll ausgewertet werden, ohne einen neuen freien
Operator zu wählen.

Status **PARTIAL**, keine Promotion. `python3 checker.py`: 3503 exakte Prüfungen
(sympy/Fraction; Stand nach Korrektur). Davon sind 2400 = 2× (150 Zustände × 8: B1–B7, C1)
Maya-Stichproben und 100 σ¹-Stichproben (C4); der Rest sind
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
e_i = F_aux(r_i) − a_i m. Dort ist der Komplementfaktor −a_i m **nicht** neutral: q(m) = 1, also q(−a_i m) = −a_i. Genau das
kompensiert q(r_i) = 1 + a_i. Er ist ungerade und am gesetzten Faktorpunkt massiv. Hier ist p* dagegen neutral
(q = 0), K-null und halbzahlig. Es gibt keine Gleichsetzung, nur die strukturelle Parallele. Hier ist es die
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
* Kompensierte periodische Clock g0 = e^{2πi Σ (m/8) :N_m:}: g0 U_T g0^{−1} = −i (−1)^Q U_T.
  Die **nackte** geometrische Segmenttranslation hat die Phase (m+α)/8, also
  t_α = e^{2πi α Q/8} g0 = e^{2πi K_α}, und
  t_α U_T t_α^{−1} = e^{2πi(¾ + α/2)} (−1)^Q U_T (C6). Die Viertelphase α bleibt sichtbar.
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

## Korrektur (15. Oktober 2026, nach Review)

* **Quelle des Faktors 2.** „Kernkreis 4l, doppelt überlagert vom Möbiusrand 8l“ steht nur in
  meinem eigenen Contract `moebius-clock-fold-20261014/PROOF.md:11–14`, als Faltungsgeometrie.
  In den Originalen ist die Naht die **Fixmenge** der Doppelinvolution, Seam = Fix(τ_dbl)
  (`_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex:115–118`), und nicht
  doppelt überlagert. Die Aussagen „σ² = primitive Kernwindung“ und „T = Kernwindung 2“
  (Abschnitt C) gelten nur unter dieser gewählten Geometrie. Als Quellenaussage nehme ich sie
  zurück.
* **Einheitswindung auf dem Quellenkreis θ** (θ = (x + 2πj)/8): Sie ist σ¹ = T1 mit
  T1(p) = (p7+1, p0, …, p6), T1⁴ = T und T1⁸ = τ_q. Das prüfen C4 und C5 (zusätzlich 104
  Prüfungen, jetzt 2796 inkl. C6/C7).
* **U_Σ.** Laut `_archive/paper-latex/tfpt-42.tex:5137–5140` ist U_Σ eine Parameterfamilie
  U_Σ(λ_Σ√ρ) mit L_Σ = −log det_adm(1 − U_Σ). SF(U_Σ) = 1 ist ihr Spektralfluss, keine
  angegebene Multiplikation mit e^{iθ}. Die Gleichsetzung mit T1 ist deshalb ebenfalls eine
  Identifikation, keine Quellformel.

## D – Kleinvorzeichen von W4 auf den D8-Strömen und Kriterium für W4 = U_s R (15.10.)

Die tatsächlichen CAR-Kleinfaktoren nehme ich als geordneten Kokzyklus
ε(x, y) = (−1)^{Σ_{i>j} x_i y_j} auf Z⁸, mit den Kanälen 0 < … < 7. W4 = U_T ist auf den
Kanalfermionen vorzeichenfrei (c_m → c_{m+4}). Daraus folgt (D0–D5, exakt):

* Für alle 112 D8-Wurzeln b = x + y gilt in der Gitterbasis e^b = ε(x, y)^{−1} ψ^x ψ^y:

      W4 e^b W4^{−1} = (−1)^{a·b} e^{Pb}   (mit der durch das K-Gesetz festgelegten Modenverschiebung).

  Das Vorzeichen hängt nicht von der Faktorreihenfolge ab.
* Auf D8 ist es die Zerlegung (−1)^{a·b} = (−1)^{s·b} (−1)^{r0·b}; s·b und r0·b sind ganz.
* ε∘P = ε auf D8. Auf Z⁸ gilt das nicht, Zeuge: (e0, e4).
* Die Modenverschiebung folgt allein aus U_T† K U_T = K + Q/2 + c_α. Sie stimmt deshalb mit der
  von U_s R überein, soweit dessen Zeitgesetz dasselbe ist. Offen bleiben nur Vorzeichen.

**Kriterium (Schur):** Der D8-Sektor ⊕_{p∈D8} F_p ist das Vakuummodul des D8-Gitter-VOA, also
irreduzibel. Zwei Unitäre, die darauf dieselbe Abbildung der Ströme e^b und der Oszillatoren
(beide wirken als P) induzieren, unterscheiden sich nur um einen Skalar. Daher gilt:

* **W4 = c · U_s R auf dem D8-Sektor** genau dann, wenn in **demselben** geordneten Kokzyklus
  χ_R(b) · σ_s(Pb) = (−1)^{a·b} für alle D8-Wurzeln gilt. Dabei ist χ_R das Vorzeichen aus
  R J(b,m) R^{−1} = χ(b) J(Pb, m + r0·b) und σ_s das Vorzeichen von U_s auf e^{Pb}.
* Andernfalls ist der Quotient ein Charakter von D8. Dann gilt W4 = c · e^{iπ λ·p̂} U_s R mit dem
  zugehörigen Toruselement.
* Die Konstante c legt die Vakuumkonvention W4|0⟩ = |a⟩ fest.

**Typgrenze:** Die Identität kann nur auf dem D8-Sektor gelten. Auf dem ungeraden CAR-Sektor
D8 + e1 ist U_s R nicht definiert, auf D8 + s ist W4 nicht definiert. Die ungeraden Felder
brauchen weiter Defekt- oder Spinsektoren bzw. den Komplementtransport. Der neutrale Test
β = e0 − e4 bleibt bestehen: T(β) − T(0) = −β, während τ_s(β) − τ_s(0) = +β.

## E – Unabhängige Gegenrechnung der gemeinsamen Liftkonstruktion (Codex-Kandidat, 15.10.)

Die Rechnung ist exakt, mit monomialen Operatoren auf C[Z⁸] und auf C[Ls], Ls = D8 ∪ (D8+s).
Die Phasen sind ganzzahlig ±1. Oszillatoren werden nur permutiert und tragen kein Vorzeichen bei.

* **E1:** P_CAR|n⟩ = η(n)|Pn⟩ mit η = (−1)^{A(n)B(n)} ist die vorzeichenfreie
  Fermionpermutation: P_CAR E_{e_j} P_CAR⁻¹ = E_{e_{Pj}} für alle j, auf ganz Z⁸.
* **E2:** W4 = Z_a E_a P_CAR ist vorzeichenfrei auf allen ψ_j, und W4|0⟩ = |a⟩ mit Phase +1.
  Das bestätigt Codex' Formel.
* **E3:** Das Modul C[Ls] mit X = E_s erfüllt X E_d X⁻¹ = (−1)^{s·d} E_d auf allen 112 Wurzeln und
  X² = −E_q.
* **E4:**
  - Für beide κ = ±1 gilt P̂² = 1.
  - P̂ E_d P̂⁻¹ = (−1)^{A(d)} E_{Pd}.
  - P̂ X P̂⁻¹ = κX.
* **E5:** R_c = Z_a X E_{−Pa} P̂ wirkt auf Ladungen exakt als ρ(p) = Pp + r0.
* **E6:** U_s R_c = X R_c = **−W4** auf dem D8-Sektor, für beide κ.
* **E7 (Präzisierung):** **R_c² = −κ · I.** Das Vorzeichen ist durch die Darstellung festgelegt:
  - X² = −E_q fixiert X bis auf ±1, und ein Vorzeichenwechsel von P̂ ändert R_c² nicht.
  - κ = −1 ergibt direkt eine Involution R_c² = I.
  - κ = +1 ergibt R_c² = −I. Dann ist R = iR_c die Involution, in derselben Struktur wie der
    Tits-Lift mit N² = −I und R = iN.
* **E8:** Q und K bleiben erhalten (Kρ = K). Der g_j-Charakter ändert sich nur um die Konstante
  e^{2πi ν·r0} = 1, mit ν·r0 = −1. Die Viertelphase bleibt also erhalten.

**Bedeutung von κ:** Beide Wahlen stimmen auf D8 überein. Sie unterscheiden sich um den Torusfaktor
Ω = e^{2πi e1·H0}, der auf D8 gleich +1 und auf D8+s gleich −1 ist. κ ist damit ein binäres Datum
**der Sektorerweiterung**. Die D8-Daten legen es nicht fest, und die Identifikation W4 ∝ U_s R auf
D8 sieht es nicht. P1 wählt es in den geprüften Stellen nicht aus.

**Grenzen:**

* Gezeigt ist eine Konstruktion im stipulierten Ls, keine P1-Herleitung.
* Auf dem ungeraden CAR-Sektor braucht es weiterhin die Spin- bzw. Defektmodule. Eine gemeinsame
  gewöhnlich lokale E8-plus-Vektoralgebra gibt es nicht.
* R_c ist nicht automatisch der frühere Tits-R. Beide können sich um einen Torus- bzw. Kleinfaktor
  unterscheiden.
