# Die fehlende HH-Regel ist die Onsite-DET-Wand: exakte Reduktion

10. September 2026. NON-RH-Forschung im Anschluss an die Universalraum-Konsolidierung
(Q046–Q050: Halbverhältnis, Minimax, fehlender HH-Term, Steigungstest −ξ/6).
Bedingt auf die v1027-Signed-DET-Wand (Ledger `CHIRAL4D.MIRROR.SIGNED.CAR.01`, `[C]`,
hash-gepinnt). **Keine Herleitung dieser Prämisse aus P1/P2, keine Zustandsauswahl,
kein T1–T8-Abschluss, keine RH-Aussage.**

## Ergebnis

Der native Viererring der Reihenfolge-/Minimax-Arbeiten ist exakt die zweite
Quantisierung der v1027-Wand `h(A) = (A ⊕ Δ) + λ W*W`, `W = (gA, 1)`, mit
`(λ, g, Δ) = (1, 1/2, 3)` und `A = a·Adj` (Umgebungsgrad 6). Daraus folgen exakt

    b = λ g a = 1/24,   c = λ g² a² = 1/576,   ε_L = 6c = 1/96,
    M = Δ + λ = 4,      δ = M − ε_L = 383/96,      also b² = c und b/a = λg = 1/2.

Der fehlende HH-Term ist in dieser Struktur kein separater Nullwert, sondern die
Aussage, dass die hohe Sorte **weder im freien DET-Parent `D_0` noch im Wandstrom `R`
räumlich transportiert wird**: `h_HH = D_0 + λR²` ist genau dann A-frei, wenn
`D_0 + λR²` konstant ist. Das ist die deklarierte DET-CAR-Prämisse (onsite even
unitary → `Δ·N_a` onsite). Sie legt zugleich die in Q050 §7 verlangte
Reichweitenklasse fest: LL ≤ 2 Links, LH = 1 Link, HH = 0.

Weitere exakte Punkte (alle in `checker.py`, `validation.json`):

- **Negative Kontrolle:** Die Signed-Determinanten-Eigenschaft `det h = M·A(1+cA)`
  allein erzwingt h=0 **nicht**: `D_0 = M0 − (r1²/g²)A`, `R = r0 + r1 A` hält die
  Determinante quadratisch und ist trotzdem HH-dispersiv. Die Onsite-Prämisse ist
  echt zusätzlich.
- **Kubischer Koeffizient:** Der niedrige Zweig der Wand ist
  `x + (3/16)x² − (1/64)x³ + …`; in Q050s Identifikation `ξ = 1 + 64 c3` gibt
  `c3 = −(λg)²/M² = −1/64` genau `ξ = 0`. Keine unabhängige Herleitung, aber eine
  exakte Konsistenz: Compiler-Herleitung von `c3` ⇔ Herleitung der Onsite-Prämisse.
- **Steigungstest:** `i⟨u,[K_ξ,Y]u⟩ = −2ξa = −ξ/6`; unter der Wand ist die
  Anfangssteigung exakt null, *vorhergesagt* vor Einsetzen eines H-Werts.
- **Minimax ≠ Wand:** Mit `c = g²a²` an `g` gebunden hat das Reihenfolgefehler-
  Funktional aus Q048 den Minimax-Punkt `g* = 1/2 − g*³a² = 0.49913…`, nicht 1/2
  (`J'(1/2) = 2a⁴ = 1/10368`). Das Halbverhältnis stammt aus der Wand, nicht aus
  dem Minimax-Prinzip.

## Was fundamental bleibt

Genau eine Quellprämisse: die hohe (DET-/Carry-)Sorte ist onsite. Ihre Herleitung
aus `c3 = 1/(8π)`, `g_car = 5` würde gleichzeitig `b/a`, `c = b²`, `ε_L = 6c`, die
Reichweitenklasse, `c3 = −1/64` und die Nullsteigung fixieren. Antrieb, Messgerät
und Zustand werden hier nicht geliefert.

## Reproduktion

    python3 -B checker.py validation.json
    python3 -B -m unittest test_checker      # auch mit -OO; Ausgaben bytegleich

Quellen: `verification/v1027_signed_det_car_wall.py` (SHA-256 in `checker.py`),
Universalraum-Konsolidierungsbericht 10.09.2026 (Q047 §1, Q048, Q049 §3, Q050 §§2–5),
`ground-state-loop-response/README.md` (gleiche Materie-Hamiltonfunktion).
Herleitung: `PROOF.md`.
