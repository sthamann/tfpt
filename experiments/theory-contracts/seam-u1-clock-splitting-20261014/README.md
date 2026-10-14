# Die Viertelphase wird durch die eigene Nahtladung kompensiert (14. Oktober 2026)

Status: **PARTIAL**, keine Promotion. `python3 checker.py`: 31 exakte Prüfungen, ca. 7 s
(benötigt numpy, sympy).

**Einfach gesagt.** Mit Viertelphase am Rand ist die gehobene Clock nur bis auf
einen Ladungsfaktor eine Achteldrehung. Die Naht besitzt aber ihre eigene
erhaltene Ladung. Mit ihr lässt sich die Clock immer zu einer echten Achteldrehung
machen. Dann liegt sie für **jede** Randphase in der TFPT-Klasse A3 ⊕ D5. Die
Alternative, bei der die achtfache Clock gleich der Fermionparität ist, liegt nie
in dieser Klasse.

**Übrig bleibt ein Bit:** echte Z8 (Deck² = 1) oder durch (−1)^F erweiterte Z8.
Gleichwertig: Die Clock dreht die Nahtfermionen mit verdrilltem Spin. ψ wird
dabei zur Funktion, ψ† zur 1-Form. Genau dann sind die Nullmoden dieses **einen**
Feldes an den Marken die 5 Funktionen und die 3 Residuen, also die beiden
TFPT-Lesarten.

**Entscheidender Test.** Am tatsächlichen Nahtoperator die Wirkung der Clock samt
ihrer Phase auf einem ladungstragenden Feldwort bestimmen: `g̃⁸ψ = ψ` (TFPT) oder
`g̃⁸ψ = −ψ` (ausgeschlossen). Das ist eine einzelne, messbare Phase.

Details und Abgrenzung: `PROOF.md`.
