# Aufspaltung der projektiven Möbius-Clock durch die Nahtladung

Anschluss an `UR.SEAM.V16_OPERATOR_PULLBACK.01` (lokal beim Nutzer, noch nicht im
Repo). Dort: Die ursprüngliche Naht trägt eine Viertelphase; im Faltungsmodell
hat die Clock dann Ordnung acht statt vier. Eine kompensierende Wirkung mit
Ladung `Q' = 2(H3+H6)` passt, ist aber nicht aus der Quelle hergeleitet.

## Satz U [E]

Randholonomie `e^{2πiα}` auf dem Möbiusrand der Länge 8l. Die gehobene Clock g
(Verschiebung um l) erfüllt auf den Nahtfermionen `g⁸ = e^{2πiαN}`; N ist die
erhaltene U(1)-Ladung der Naht (Teilchenzahl des QWZ-Kragens). g erzeugt daher nur
eine projektive Z8-Wirkung. Jede Kleidung `g̃ = g·e^{2πicN}` ist wieder eine
Symmetrie, weil N erhalten ist und mit Verschiebungen kommutiert.

1. Ungekleidet, α = ¼: g² hat in E8 Ordnung 8 (bestätigt die externe Korrektur).
2. **Echte Z8-Wirkung**, `g̃⁸ = 1` auf den Fermionen, also Deck² = 1: Für jede
   geprüfte Holonomie (0, ¼, ½, ¾, ⅓, ⅛, 5/7), jede der acht Achtelwurzeln und
   beide Spinlifts gilt: g̃² hat Ordnung 4 und Zentralisator **A3 ⊕ D5**, das
   Deck g̃⁴ hat D8. Das ist die TFPT-Glueklasse.
3. Kleidung mit `g̃⁸ = (−1)^F` stattdessen: nie A3 ⊕ D5, sondern A7 ⊕ A1 oder
   D6 ⊕ A1.
4. Der kompensierende Erzeuger ist N selbst. In Faltungskoordinaten gilt
   `N = Σ H_a = 2 H_λ` mit der E8-Spinorwurzel `λ = (½)⁸`. Das ist dieselbe Form
   `2·H_Wurzel` (Norm 8) wie das externe `Q' = 2(H3+H6)`; die konkrete
   Weyl-Abbildung dazwischen ist nicht nachgerechnet.

Beweisidee: Die Kleidung verschiebt die Kanalphasen gleichmäßig um c. Echte Z8
heißt `8((k+α)/8 + c) ∈ Z`; das ist bis auf eine zyklische Umbenennung der
Kanäle der periodische Fall aus `moebius-clock-fold-20261014`. Die
(−1)^F-Variante ist der antiperiodische Fall. Der Checker rechnet alle Fälle
explizit.

**Folge.** Die Kompensation ist keine zusätzliche Annahme. Sie ist die eigene
erhaltene Ladung der Naht. Die Viertelphase ist für die Klasse unerheblich.
Übrig bleibt ein einziges Bit:

> **Wirkt die gehobene Clock auf den Nahtfermionen als echte Z8 (Deck² = 1)
> oder als durch (−1)^F erweiterte Z8 (Deck² = (−1)^F)?**

Nur die erste Wahl liefert die TFPT-Klasse.

## Gleichwertige Form des Bits [E Arithmetik, B Deutung]

Mit `g̃⁸ = e^{2πi(L0 − ηJ0)}` und den Nahtfermionen ψ, ψ† (Spin ½, Ladung ±1)
gilt `g̃⁸ = 1` genau für `η ≡ ½ (mod 1)`. Die Clock ist dann die
spin-ladungsverdrillte Drehung. ψ und ψ† erhalten die Rotationsgewichte 0 und 1:
ψ verhält sich wie eine **Funktion**, ψ† wie eine **1-Form** (bc-System mit λ = 1).
Die physikalische Energie wird dadurch nicht verändert. Die Verdrillung betrifft
nur, als welche geometrischen Objekte die Felder unter der Clock transportiert
werden.

## Die beiden TFPT-Lesarten als Nullmoden eines Feldes [E Rechnung, C Randbedingung]

Erlaubt man beiden Feldern einfache Pole an den d Marken auf P¹, so gilt:
* Gewicht 0: `H⁰(O(D))`, Dimension **d+1** (Konstanten und `1/(z−a_i)`).
* Gewicht 1: `H⁰(K(D))` = `{Σ r_i dz/(z−a_i) : Σ r_i = 0}`, Dimension **d−1**.
  Der ganzzahlige Residuenteil ist genau das Wurzelgitter **A_{d−1}**.

Für d = 4 sind das 5 + 3. Die Zählung stand schon in `QGEO.RR.01`, dort aber als
getrennte Lesart [C]. Neu ist: Dieselbe Bedingung, die die TFPT-Clockklasse
auswählt (echte Z8, η = ½), macht den **einen** Nahtfermion zu einem Paar aus
Funktion und 1-Form. Dessen Nullmoden sind dann die Funktionsseite `D_{d+1}` und
die Zyklenseite `A_{d−1}` derselben Vergleichsklasse `R_d`.

Nicht bewiesen: die Polbedingung an den Marken (gewählte Randbedingung); die
Clifford-Lesart der 5 Funktionsmoden (Index 5 − 3 = 2: nicht alle Moden paaren
sich); dass die Verdrillung physikalisch und nicht nur buchhalterisch ist.

## Geometrische Deutung des Bits (zitiert, nicht geprüft)

Für neutrale (Majorana-)Fermionen gibt es keine U(1)-Kleidung. Dann ist das Bit
die Wahl der Pin-Struktur der Möbiusnaht: Pin+ (Spiegelung quadriert zu +1,
periodischer Rand; Kirby–Taylor: Ω₁^{Pin+} = 0) gegen Pin− (antiperiodischer
Rand, Ω₁^{Pin−} = Z₂). Für geladene Fermionen erlaubt Spin^c beide Kleidungen.
Das Bit wird dann zu einer **Spin-Ladungs-Relation** der Clock. Die
Originalforderung in `v993` („glue group cyclic of order 4 … shadow of
U² = (−1)^F") betrifft die Ladungsklasse `[λ]² = [v]` und widerspricht dem nicht:
Auf dem bosonischen E8 wirkt (−1)^F der gefalteten Fermionen trivial.
