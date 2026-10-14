# Möbius × Z4-Faltung eines einzigen chiralen Nahtkanals

Ausgangsfrage (Befund `UR.SEAM.MIXED_CURRENT_ORIGIN.01`, lokal beim Nutzer):
Der mikroskopische Nahtvertreter hat **einen** komplexen Kanal pro Rand; acht
Kopien sind nicht hergeleitet. Kann die vorhandene Geometrie (Doppeldeckung /
Möbius, vier Marken mit Viererclock) acht Kanäle aus einem erzeugen, ohne Kopien
einzusetzen? Und in welcher Lage stehen sie zum V16-Träger?

## F1 – Lift und Faltung [E]

Kern der Naht: Kreis aus vier Bögen der Länge l, Clock ρ = Drehung um l
(Ordnung 4). Der Rand eines Möbiusbands über diesem Kern ist ein Kreis der Länge
8l, der den Kern zweifach überlagert; die Decktransformation ist die Drehung um
4l. ρ hebt sich zur Drehung g um l: **g hat Ordnung 8 und g⁴ = Deck.**

Ein chiraler komplexer Kanal ψ auf diesem Randkreis wird auf einen Bogen
gefaltet: ψ_j(x) = ψ(x + jl), j = 0..7. Lokal (auf einem Bogen) sind das acht
unabhängige komplexe chirale Kanäle, c = 8, also 16 Majorana-Freiheitsgrade.
Fourierkanäle χ_k = Σ_j ω^{-jk} ψ_j tragen die Verdrillung k/8 (periodischer
Randkreis) bzw. (k+½)/8 (antiperiodisch), und g wirkt auf χ_k durch eine Phase.
Der Checker prüft dies am Gitterfermion exakt: Faltungsunitäre,
Blockdiagonalität, Spektrumsidentität, Clockeigenwerte, für beide Spinstrukturen.

Das ist die bekannte zyklische Überlagerungs-/Permutationsorbifold-Beziehung
(Kac–Longo–Xu, Solitonen in Permutationsorbifolds). Der ursprüngliche Vakuumzustand
entspricht dabei einem verdrillten Sektor der acht Basiskanäle, nicht deren
Vakuum.

## F2 – Klasse der geometrischen Clock in E8 [E, unter Existenz von E8]

Die Wirkung auf den Fermionen legt μ ∈ R⁸ modulo Z⁸ fest (Phase e^{2πiμ_a} auf
Kanal a). Als E8-Element bleibt der Spin-Lift μ ↦ μ + e₁ offen; geprüft werden
beide Lifts.

| Randkreis | Element | Zentralisator in E8 |
|---|---|---|
| periodisch | g² (beide Lifts) | **A3 ⊕ D5** |
| periodisch | g⁴ = Deck (beide Lifts) | D8 |
| antiperiodisch | g² | D6 ⊕ A1 bzw. A7 ⊕ A1 |
| antiperiodisch | g⁴ | E7 ⊕ A1 bzw. D8 |

Für den periodischen Randkreis stimmt die Gradverteilung der Wurzelströme unter
g² mit der TFPT-Gluegraduierung C überein: 52/64/60/64. Ordnung-4-Elemente von E8
mit Zentralisator vom Typ A3 ⊕ D5 bilden eine Kac-Klasse (Knoten mit Marke 4 im
affinen Diagramm); g² und C sind damit konjugiert (zitierte Klassifikation,
nicht im Checker formalisiert).

**Folge:** Die vorher nur als interne Gluegraduierung gelesene Z4-Wirkung lässt
sich als die geometrische Viererclock der gefalteten Naht realisieren –
ausschließlich bei periodischer Spinstruktur des Möbiusrands. Die antiperiodische
Wahl erzeugt nie die TFPT-Struktur.

## F3 – Lage des V16-Trägers [E]

In Faltungskoordinaten zerlegen sich die Fixfaktoren von g² in
Fermion-Bilineare und Spinorwurzeln:
A3 = 4 + 8, D5 = 16 + 24. Die vom Deck fixierte D8 besteht aus 48 Bilinearen und
64 Spinorwurzeln; sie ist nicht die Bilinear-D8 der gefalteten Kanäle. Die
TFPT-Gradierung C hat dagegen A3 ⊕ D5 ganz aus Bilinearen ihrer eigenen 16
Majoranas (V16).

**Folge:** Die V16-Fermionen sind nicht die gefalteten Nahtfermionen. Beide
Beschreibungen sind in E8 konjugiert (alle D8 in E8 sind konjugiert), also zwei
Fermionisierungen derselben bosonischen Theorie; der Übergang mischt Fermionen und
Spinfelder (Trialität auf D4 ⊕ D4). Schon die Grad-0-Struktur A3 ⊕ D5 verlangt
deshalb in der gefalteten Beschreibung die Spinorerweiterung. Damit ist Befund 3
(„die 128 Spinorströme sind eine echte lokale Erweiterung") verschärft: Ohne diese
Erweiterung entsteht aus der gefalteten Naht nicht einmal der Träger D5.

## Erste zusätzlich gewählte Geometrie

1. Ein **einziger chiraler** Kanal entlang des ganzen Möbiusrands. Der QWZ-Kragen
   ist ein Ring mit zwei Rändern entgegengesetzter Chiralität; ein
   Chern-Isolator auf einer nicht orientierbaren Fläche braucht eine Domänenwand.
   Ob die ursprüngliche Möbius-/Deckstruktur und Reflexion Θ diese Verklebung
   liefern, ist offen.
2. **Periodische Spinstruktur** des Randkreises. Eine mögliche, nicht geprüfte
   Herkunft ist der primitive Spektralfluss eins, der NS und R vertauscht.
3. Die E8-Erweiterung selbst (R-Sektor/GSO) wird von der Faltung nicht erzeugt.

## Gegenfälle im Checker

Antiperiodischer Randkreis (nie A3 ⊕ D5); TFPT-C gegen Faltungs-g² (gleiche
Klasse, verschiedene Bilinear-/Spinoranteile).
