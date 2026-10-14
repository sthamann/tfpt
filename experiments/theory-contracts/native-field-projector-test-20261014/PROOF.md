# Feldprojektor 6 → 3 für die nativen Bosonamplituden

Präzisierung (Codex): Die sechs `β_F = e_i + e_j − ½·1` sind **Gewichtslabels** in einem
3D-Cartanraum. Die L/S-Abbildung mit den Spalten ±h_i hat Rang 3; sie ist keine
komplex-lineare Isometrie der sechs unabhängigen Bosonamplituden in Λ²4. Gegenüber
liegende Labels sind nicht derselbe b†-Fockzustand mit Minuszeichen. Hier wird der
tatsächliche Operatorvergleich geführt.

## F1 [E] – Welche Darstellung der h-Raum trägt
⟨M, U⟩ aus v117 hat Ordnung 24 und enthält Elemente der Ordnung 4: eine treue
dreidimensionale irreduzible S4-Darstellung. Die Elemente mit Spur 1 haben Ordnung 4,
also ist es **std ⊗ sgn**, die orientierungsgetwistete Darstellung. Das passt zum
E⊗det(E)-Wörterbuch in `source-native-clock-flavor-bridge-20260922` §1.

## F2 [E] – Der einzige clockkovariante Feldprojektor
Unter Markenpermutationen hat Λ² der Viermarkendarstellung den Charakter
(6, 0, −2, 0, 0) = std ⊕ std⊗sgn. Daher gibt es bis auf einen Skalar **genau eine**
S4-äquivariante Feldabbildung `Λ²4 → h-Raum`: die Projektion auf Λ² des
Summe-null-Unterraums (mit `4 = 1_konst ⊕ 3_Summe-null` ist
`Λ²4 = Λ²3_sz ⊕ (3_sz ∧ 1)`, und `Λ²3_sz ≅ std⊗sgn`). Der Summand `3 ⊗ 1` (std)
wird nach Schur auf null abgebildet.

## F3 [E] – Kein Projektor ist zugleich clock- und ladungskovariant
* Alle sechs Gewichte von Λ²4 sind von null verschieden. Eine torus-äquivariante
  Abbildung der Amplituden in den Cartanraum (Gewicht 0) ist daher null.
* Keine Gerade in C⁴ ist zugleich torus- und S4-invariant: Die Konstantengerade ist
  nicht torusinvariant, die Markenkoordinatengeraden sind nicht S4-invariant.
  Jede 3⊕1-Zerlegung bricht also entweder die Ladungs- oder die Clockkovarianz.
  Eine Markengerade e_m ist ladungskovariant und bricht S4 → S3_m; die
  Konstantengerade ist S4-kovariant und bricht den Ladungstorus. Der ε-Intertwiner
  `Λ²3 → 3*` bezieht sich auf eine solche gewählte Zerlegung und transportiert
  Feldkoeffizienten, nicht Cartanlabels.

## F4 [E] – Die kovariante Abbildung von Bosonzuständen auf Cartanvektoren
Die Abbildung, die torusinvariant und S4-kovariant von Bosonzuständen in den
Cartanraum führt, ist die Impulsabbildung
`μ(b) = Σ_w |b_w|² w`, also der Erwartungswert der Cartanladungen. Für einen Zustand
mit einem einzigen Gewicht liefert sie genau dessen Label β_F. Sie ist **quadratisch**
in den Amplituden, nicht linear.

## Folge für die Kette
* `h_geom` darf **nicht** als lineare native Bosonamplitude verwendet werden.
* Zwei korrekt typisierte Lesarten sind möglich, jede mit eigener Wahl:
  1. **Ladungserwartung:** `h ∝ μ(b)` (Erwartung von H_t im Bosonzustand). Kovariant
     unter Torus und S4. A(h) ist dann quadratisch in den Bosonamplituden, also ein
     anderer Vertextyp als die lineare Kopplung `g b†P`.
  2. **Linearer Feldprojektor:** nur nach Wahl einer 3⊕1-Zerlegung, die Ladungs- oder
     Clockkovarianz bricht. Der clockkovariante Projektor ist eindeutig (F2), aber
     nicht ladungskovariant.
* Der geometrische Ein-Clock-/CP-Grenzsatz (gemeinsames h aus den drei
  Residuenachsen) gilt **nicht** automatisch für native Bosonfelder, solange ihr
  Feldintertwiner nicht hergeleitet ist.

**Erste nötige Quellenauswahl:** welche Lesart die Quelle trägt – Ladungserwartung
(Zustandsdatum) oder ein Feldprojektor samt gebrochener Kovarianz und ihrer Begründung.
Eine Realitätsbedingung (z. B. über die reelle Struktur J₆ der selbstdualen 6) ist
nicht ausgeschlossen, müsste aber mitgebracht werden.
