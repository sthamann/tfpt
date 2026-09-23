# Quellenzeit: direkter Generator und wiederholter Übergang

## Frage und Geltungsbereich

Kann das noch fehlende Verbot einer elementaren Doppelumwandlung aus Komposition, positiver Energie oder zeitlicher Reflexionspositivität folgen? Und welche tatsächlichen Quellenwerte würden nach der Stabilitätsreduktion genügen?

Verwendet wird die im Algebraaudit präzisierte volle endliche CAR/CCR-Darstellung mit stark Q-erhaltendem selbstadjungiertem H und den beiden globalen unteren Operatorantworten. Die folgenden Gleichungen werden auf einzelnen endlichen Q-Sektoren bewiesen. Sie sind keine Behauptung eines bereits konstruierten räumlichen Quellenmaßes.

## Die erste Ableitung unterscheidet beide Ereignisse

Sei T(τ)=exp(−τ(H−aI)) die euklidische Zeitentwicklung; a ist ein beliebiger skalarer Energiebezug. Sei P_{b,f} der Projektor auf genau b Bosonen und f Fermionen. Definiere die rechteckigen Blöcke

K₁(τ)=P_{1,0}T(τ)P_{0,2},

K₂(τ)=P_{2,0}T(τ)P_{0,4}.

Auf den endlichen Q=2- und Q=4-Sektoren ist T eine analytische Matrixfunktion. Deshalb gilt ohne Grenzwertproblem

C₁:=P_{1,0}HP_{0,2}=−K₁′(0),

C₂:=P_{2,0}HP_{0,4}=−K₂′(0).

Der Energieoffset fällt in diesen disjunkten Blöcken heraus. Unter den globalen unteren Antworten und globaler Semibeschränktheit bleiben allein einfache und doppelte reine Umwandlungen. Dann liest C₁ sämtliche einfachen Koeffizienten und C₂ sämtliche doppelten Koeffizienten einschließlich der normierten Bosonfaktoren aus.

Wenn C₁=gW und C₂=0, folgt für den zweiten Block

K₂(τ)=(τ²g²/2) P_{2,0}X²P_{0,4}+O(τ³).

Das ist kein Widerspruch: Ein direkter Generatorübergang ist linear in τ; zwei aufeinanderfolgende elementare Übergänge beginnen quadratisch in τ. Die quadratische Kinetik erhält die Bosonzahl und kann in zwei Hamiltonschritten keinen weiteren Beitrag zwischen diesen Endsektoren liefern, wenn C₂=0.

In Realzeit U(t)=exp(−it(H−aI)) gelten entsprechend i∂ₜ(PUP)|₀=C für die jeweiligen rechteckigen Blöcke und der Vorfaktor −g²t²/2 für die zweifache native Ausführung.

## Positive Energie und zeitliche Reflexionspositivität wählen C₂ nicht aus

Der native Gegenoperator H_η=H_W+η(X²+X†²) ist in einem offenen Bereich nichtverschwindender η selbstadjungiert und global nach unten beschränkt. Wähle a≤inf spec(H_η). Dann ist

T_η(τ)=exp(−τ(H_η−aI))

eine stark stetige Halbgruppe positiver selbstadjungierter Kontraktionen. Für beliebige endlich viele t_i≥0 und Vektoren ψ_i gilt exakt

Σ_{ij}⟨ψ_i,T_η(t_i+t_j)ψ_j⟩
=⟨Σ_iT_η(t_i)ψ_i,Σ_jT_η(t_j)ψ_j⟩≥0.

Damit besitzt die Zeitkernfamilie die angezeigte Reflexionspositivität, obwohl C₂≠0. Sie respektiert außerdem dieselben zuvor geprüften inneren Symmetrien und die Q-Erhaltung. Der Halbgruppenkompositionssatz allein kann somit eine elementare Doppelumwandlung ebenfalls nicht verbieten.

**Scope:** Dies ist eine Gegenprobe gegen die Auswahl durch Halbgruppe, Semibeschränktheit und diese zeitliche Gram-Positivität. Ein vollständiges Osterwalder–Schrader-Schwingerfunktional, räumliche Lokalität, dieselben Rohnaht-Korrelationen, P1/P2-Normierungen oder die gesamten T1–T8-Bedingungen wurden für H_η nicht hergestellt. Es wird keine Widerlegung eines solchen stärkeren gemeinsamen Quellenvertrags behauptet. Die klassische OS-Rekonstruktion setzt entsprechend weitergehende Bedingungen an eine Familie euklidischer Greenfunktionen voraus; sie ist kein Selektor eines speziellen W-Generators (Osterwalder–Schrader, 1975, Abstract und Rekonstruktionsthema: https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-42/issue-3/Axioms-for-Euclidean-Greens-functions-II-with-an-Appendix-by/cmp/1103899050.pdf).

## Welcher Quellenbeweis dadurch konkret möglich wird

Nach unabhängiger Herstellung des gemeinsamen kanonischen Quellenraums genügen für die Umwandlung in dieser stabilen Klasse die ersten Ableitungen in den Sektoren Q=2 und Q=4:

1. −K₁′(0)=gW mit g≠0;
2. −K₂′(0)=0.

Die untere Kinetik wird aus dem Einfermionblock (h) und dem Einbosonblock (Ω), jeweils nach Abzug der Vakuumenergie, bestimmt. Diese niedrigen Matrixelemente ersetzen allerdings nicht den globalen Beweis, dass die beiden unteren Antworten tatsächlich überall Zahlenmatrizen sind. Höhere gemischte, stabilisierende Operatoren könnten sonst den gesamten Q≤4-Bereich unverändert lassen.

Wenn diese Voraussetzungen erfüllt sind, bestimmt der rekonstruierte selbstadjungierte Generator auf der vollen Darstellung seine gesamte Zeitentwicklung. Mehrzeitdaten bleiben dann unabhängige Konsistenzprüfungen der Quellenabbildung; sie sind kein zusätzlicher frei wählbarer Generator. Die gemeinsame Zustandstransformation muss ebenfalls bewiesen sein.

Die konkreten Werte K₁′(0), K₂′(0), h und Ω wurden hier nicht aus der primitiven TFPT-Quelle bestimmt. Der Quellenbericht prüft, ob das dafür nötige kanonische Feld- und Transferobjekt bereits vorliegt. Das gezielte nächste Herkunftsproblem ist genau dieses Objekt; ein passend gewähltes exp(−τH_W) würde die gesuchte Antwort voraussetzen.
