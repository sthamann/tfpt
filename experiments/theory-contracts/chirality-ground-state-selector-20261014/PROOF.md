# Grundzustandstest legt die Spinorchiralität fest

Eingang (Codex, lokal, `UR.SEAM.QUOTIENT_LOCALITY_E8.01`, Punkt 4): Unter der
standardmäßigen geraden Spinorerweiterung und dem ursprünglichen Fold-Zeitgesetz
`K = L0 + δ·Q`, `δ_k = (k+α)/8 − ½`, hat `p* = (½⁴, −½⁴)` die Energie `K = 0`.
Das ergibt zwei Grundzustände gegenüber einem in der CAR-Quelle.

Für einen Gitterzustand gilt `K(p) = |p|²/2 + δ·p`.

## G1 [E] – die s-Erweiterung scheitert für jede Randphase

`δ·p* = ½(Σ_{k<4} δ_k − Σ_{k≥4} δ_k) = ½·(−16/8) = −1`, **unabhängig von α**: Die
gleichmäßige Verschiebung durch α hebt sich bei Gesamtladung 0 heraus. Also gilt
`K(p*) = 0` für jedes α. Der Checker bestätigt genau zwei Grundzustände für
α ∈ {0, ⅛, ¼, ⅓, ½, ⅔, ¾, ⅞}.

## G2 [E] – die c-Erweiterung ist mit eindeutigem Vakuum verträglich

`E8_c = D8 ∪ (D8+c)` (ungerade Anzahl Minuszeichen) ist ebenfalls ein E8-Gitter;
die beiden unterscheiden sich durch die Chiralitätswahl. Für 0 < α < 1 ist dort das
Vakuum der **eindeutige** Grundzustand. Der tiefste Spinorzustand liegt bei

    K_min(Spinor, c) = min(α, 1−α)/8,

für die reale Viertelphase also bei **1/32**. Analytisch: `(½⁵, −½³)` hat
`K = α/8`, `(½³, −½⁵)` hat `K = (1−α)/8`. Der Checker prüft das als Minimum über
alle kurzen c-Spinorvektoren.

## G3 [E] – periodischer Fold schon in der CAR-Quelle ausgeschlossen

Auf dem CAR-Ladungsgitter Z⁸ ist das Vakuum für 0 < α < 1 eindeutig. Bei α = 0
(periodisch) ist schon die CAR-Quelle entartet, wegen der Nullmode δ₄ = 0.
Der periodische Fold ist also nicht nur wegen der realen Viertelphase
ausgeschlossen, sondern auch durch das Grundzustandskriterium.

## G4 [E] – Klasse der Clock in beiden Chiralitäten (α = ¼, ¾)

| | s | c |
|---|---|---|
| ungekleidete Clock g² | Ordnung 8 (D4 + 2A1 bzw. 2A3 + A1) | Ordnung 16 (4A1) |
| U(1)-gekleidet, echte Z8 | **A3 ⊕ D5** | **A3 ⊕ D5** |
| U(1)-gekleidet, g̃⁸ = (−1)^F | A1 ⊕ D6 / A1 ⊕ A7 | 2A3 (Ordnung 8) |

## Folge

Für die **reale Viertelphase**, ohne die Wilsonphase zu entfernen, gibt es genau
eine widerspruchsfreie Kombination:

1. c-chirale Erweiterung: eindeutiges Vakuum, Spinorlücke 1/32;
2. Clock = mit der Nahtladung gekleidete echte Z8: Glueklasse A3 ⊕ D5.

Die Kleidung lässt das Zeitgesetz K und die Wilsonphase unverändert; sie
definiert nur den Clock-Operator. Dass das Original genau diesen Operator als Clock
auszeichnet, ist **nicht** hergeleitet.

Unverändert gilt Codex Punkt 2: Auf dem gefalteten CAR-Raum haben alle Operatoren
ganzzahlige Cartan-Charaktere. Die c-Erweiterung ist also nicht in der
unveränderten Quelle enthalten. Das Ergebnis ist eine **notwendige Bedingung** an
jede Erweiterung, kein Existenzbeweis: Wenn eine Spinorerweiterung mit
unverändertem Zeitgesetz und eindeutigem Vakuum existiert, ist sie c-chiral
(relativ zur Kanalreihenfolge von δ), und ihr tiefster Spinorzustand liegt bei
min(α, 1−α)/8.

Beobachtung ohne Behauptung: 1/32 ist das kleinste Gewicht m²/32 der externen
Vierteltwist-Fusionsformel h = m²/32 + N.
