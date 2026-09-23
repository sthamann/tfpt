# Nachgereichte Texte: neue Norm, korrigierte Zustandszuordnung und Feldadapter

Die drei während der laufenden Prüfung nachgereichten Texte wurden vollständig gelesen und unverändert eingefroren. Sie sind keine Anweisungen, Ergebnisse ungeprüft zu übernehmen. Zwei Texte vereinfachen ältere Arbeitsstände stark; die dritte längere Forschungsnotiz enthält ausführlichere Beweise einer bereits bekannten grundsätzlichen Diagnose.

## A. Ein tatsächlich neuer Rechenwert trägt eine stärkere Schranke

Die Norm der fünften reinen Bosonstufe ist gegenüber dem hiesigen v1.6.7-Snapshot neu:

\[
\nu_5=1\,866\,738\,327\,552\,000.
\]

Die eingefrorene ursprüngliche Spur-/Wick-Rechnung wurde unabhängig erneut ausgeführt: alle Normen von ν1 bis ν5, bei ν5 genau 840 Wick-Netzwerke in 93 vorzeichentreuen Isomorphieklassen, mit Python-Ganzzahlen statt gerundeter Netzwerkarithmetik. Normaler und optimierter Lauf liefern identische Ergebnisbytes. Dies ist ein frischer Replay derselben Methode, keine zweite unabhängige Methode für ν5. Die kleineren Normen stimmen mit den bereits vorhandenen unabhängigen Zertifikaten überein.

Aus den sechs normierten Vektoren v0 bis v5 entsteht eine echte Variationskompression. Ihre Diagonale ist kΔ, ihre benachbarte Kopplung \(g\sqrt{\nu_{k+1}/\nu_k}\). Fügt man den bereits exakt konstruierten orthogonalen Zwei-Boson-Rücklaufrest w2 hinzu, ergibt sich eine siebendimensionale Kompression. Seine zusätzliche Kopplung liegt zu v3; sie ist \(g\|w_2\|/\sqrt{\nu_3}\). Die übrigen angegebenen Nullstellen folgen aus Bosonzahl und Orthogonalität.

Unabhängige rationale Sturm-Zählung liefert

\[
-1.13847420<E_{6,\rm Ritz}/\Delta<-1.13847419,
\]
\[
-1.13847610<E_{7,\rm Ritz}/\Delta<-1.13847609.
\]

Dies sind **keine invarianten Unterräume** und nicht die sechste bzw. siebte Stufe der vollständigen Hamilton-Lanczoskette. Sie sind dennoch gültige Variationsräume. Deshalb folgt streng

\[
\boxed{E_0<-1.13847609\Delta.}
\]

Zusammen mit dem beibehaltenen, in dieser Runde nicht vollständig neu bewiesenen N=63-Satz \(E_h>-1.121899\Delta\) erhält man die verbesserte Entnahmegrenze

\[
\boxed{\epsilon=E_h-E_0>0.01657709\Delta.}
\]

Sie ersetzt im aktuellen Stand die schwächere untere Schranke 0.00773911Δ aus v1.6.7. Die obere Grenze 0.039079764Δ und das bisherige Liniengewicht über 88.007628 Prozent werden dadurch nicht automatisch verändert. Es wurde kein exakter Zentralwert des Grundzustands oder Pols gefunden.

## B. Die einfache Darstellung vermischt zwei Näherungszustände

Die Werte um -1.138476Δ, mittlere Bosonzahl 1.0177445, Überlappung mit F von 0.3498904 und Bosonzahl-Shannonwert 1.8712436 Bit gehören zum größeren siebendimensionalen Ritz-Zustand. Die im selben Text genannten Gewichte 0.973684 und 0.026316 gehören dagegen ausdrücklich zu der älteren fünfdimensionalen Basis v0 bis v3 plus w2. Deren Energie liegt um -1.0942319Δ und ihre mittlere Bosonzahl um 0.8421159.

Die unterschiedlichen Werte wurden aus den beiden kleinen Matrizen unabhängig nachgerechnet. Für den **größeren selben Ritz-Zustand** folgen stattdessen die gesamten Entnahme-/Additionsnormen ungefähr 0.9681955 und 0.0318045. Keine dieser Näherungszahlen ist das Gewicht des isolierten Pols auf dem wahren stationären Grundzustand. Auch die angegebenen Entnahme-/Additionsenergiemittel aus der kleineren Basis sind keine exakten Polenergien.

Eine zusätzliche CAR-Summenregelrechnung bestimmt die ersten geladenen Momente aus genau denselben kleinen Matrizen, ohne Millionen Besetzungsamplituden neu zu konstruieren. Sie reproduziert die gespeicherten Mittelwerte der Fünferbasis und ergibt für den größeren Siebener-Ritz-Zustand stattdessen mittlere Entnahmekosten von etwa 0.03479766990Δ und Additionskosten von etwa 1.05931330814Δ. Das sind korrigierte numerische Variationszustandswerte, keine Ω-Polenergien. Die allgemeinen Identitäten und die reproduzierbare Auswertung stehen im ausführlichen Nachtrag A.

Die Aussage „unser schwächerer Sektorvergleich schließt die Lücke nicht“ ist korrekt. Sie widerlegt aber keinen stärkeren vorherigen Grundzustandssatz für denselben Modellvertrag. Das eingefrorene fremde Gesamt-Replaymanifest stand noch auf RUNNING. Deshalb wird hier nur unser abgeschlossener isolierter Norm- und Ritz-Replay behauptet, nicht der Abschluss der fremden Gesamtrunde.

Der Text nennt eine fast geschlossene Leiter. Der bereits bewiesene Rücklaufrest bleibt jedoch ungleich null. 33 mögliche Bosonzahlstufen bedeuten nicht 33 Vektoren für den gesamten Prozess. Auch alle 33 skalaren Normen würden zunächst einen bestimmten Variationsraum beschreiben, nicht automatisch die volle Antwort.

## C. Ein neuer entscheidender Test am Feldprojektor

Der Spin-1/2-Projektor im zweiten Text trägt unter einer bestimmten Händigkeit. Für

\[
(1,0)\otimes(1/2,0)=(3/2,0)\oplus(1/2,0)
\]

wurde eine explizite Epsilon-Auslese C samt Wiedereinsetzung R konstruiert. Alle gleichhändigen sl(2)-Intertwining-Gleichungen gelten, CR=I2 und RC=P1/2. Die Gram-Matrix der sechs verwendeten unnormierten Koordinaten ist diag(1,1,2,2,1,1); diese Metrik darf nicht durch die Einheitsmatrix ersetzt werden.

Wird der zweite Faktor jedoch als **wörtlich adjungiertes linkes Weylfeld** gelesen, hat er entgegengesetzte Händigkeit. Dann gilt

\[
(1,0)\otimes(0,1/2)=(1,1/2),
\]

ein irreduzibler Lorentzraum. Unter Drehungen gibt es weiterhin Spin 3/2 und Spin 1/2; der Rotationsprojektor ist aber nicht boostinvariant. Der neue exakte Prüfer findet

\[
[P_{1/2},J_z]=0,\qquad
\operatorname{rank}[P_{1/2},K_z]=4.
\]

Das ist ein konkreter Test, weshalb „das Feldwörterbuch ist fertig“ zu weit geht. Es ist **kein pauschaler Ausschluss des ursprünglichen Modenkomposits**: Ein Fock-Erzeuger f† ist nicht automatisch ein adjungiertes lokales Weylfeld. Eine linke Weylfeldentwicklung enthält bereits Erzeugungs- und Vernichtungsterme mit passenden Spinorwellenfunktionen. Eine unabhängige oder korrekt ladungskonjugierte gleichhändige Konstruktion bleibt möglich; sie benötigt den tatsächlichen Adapter mit Ladung, CAR, W und Dynamik. Die Konventionen entsprechen [Dreiner, Haber und Martin, Abschnitte 2 und 3](https://arxiv.org/abs/0812.1594).

Der nächste Test ist damit konkret: denselben geladenen Operator samt gepunkteten/ungepunkteten Indizes abbilden, sowohl Drehungen als auch Boosts verschränken, dann sein wirkliches Matrixelement am nativen Grundzustand bestimmen. Ein Projektorrang von zwei aus sechs ist kein zustandsunabhängiges Spektralgewicht von einem Drittel. Positive Zustände mit Gewicht null und eins sind explizit geprüft.

## D. Weitere Übernahmegrenzen

- Die Clock ist nach der späteren konkreten Konstruktion ein Element der inneren Spin(10)-Darstellung. Die ältere Formulierung „äußerer Handgriff“ wird nicht als neue Herkunftstatsache übernommen.
- Die große Kommutantdimension zählt nicht direkt physische Freiheitsgrade. Ein skalarer Kommutant bedeutet nicht automatisch beliebige dynamische Kontrolle. Als exakter Gegenzeuge haben Spin-1-Kontrollen einen skalaren Kommutanten, aber Lie-Dimension drei statt acht.
- Die Viererregel N=0 modulo vier ist eine notwendige Singulettregel. Ohne globalen Eindeutigkeitssatz darf sie tiefere entartete Nichtsingulett-Grundzustände nicht ausschließen.
- Das skalare Grassmann-Nullresultat ist korrekt in der angegebenen lokalen, ableitungsfreien, gleichhändigen Ein-Kopie-Klasse mit unverändertem W. Es verbietet nicht jede denkbare skalare Erweiterung mit anderen Feldern, Ableitungen oder unabhängigen Komponenten.
- Die angegebenen getrennten Casimire sind wertvolle minimale Sonden; nicht jede sinnvolle Kontrolle erfordert sofort die ganze Gruppe. Schon ein einzeln hinreichend trennender Casimir kann die betrachteten dunklen Typen unterscheiden.

## E. Die dritte Notiz: richtige Richtung, überwiegend bereits berücksichtigt

Die längere fundamentale Reduktion ergänzt den bereits eingefrorenen früheren Kommentar um die ausführliche Herleitung. Ihr stärkster Satz trägt: Bei invariantem H, invariantem Ω und irreduzibler innerer Entnahmefamilie gilt für die **gesamte** lokale Antwort

\[
T^\dagger F(H-E_0)T=\gamma_F I_{64},\qquad
C_{rs}(t)=\delta_{rs}c(t).
\]

Dieser Satz umfasst Nebenlinien. Beliebig genaues c(t) erzeugt deshalb keinen Ortsindex in den 64 inneren Labels. Er verbietet weder die neu geprüften N=2-Interventionen auf anderen präparierten Zuständen noch Bewegung auf zusätzlichen Multiplizitätsräumen.

Auch die Unterscheidung zwischen dem Kommutanten der inneren Symmetrie und demjenigen der verfügbaren Operationen ist richtig. Der eine lässt symmetrieverträgliche Dynamik auf unabhängigen Vorkommen zu, der andere beschreibt die Reichweite der gewährten Zugriffe. Viele Vorkommen sind noch keine räumlichen Orte.

Die bekannte Paritätsstruktur einer Bank wird korrekt eingegrenzt: Wenn Bosonen unverändert bleiben, erhält der verbundene Paargraph nur globale Fermionparität, keine echte Teilmengenparität. Unabhängig kopierte Banken können durch ihre gewählte Zusammensetzung neue lokale Erhaltungsgrößen bekommen. Deshalb ist die Herleitung einer globalen Kompositionsregel eine echte Alternative zur bloßen Ergänzung eines Links zwischen fertigen Kopien.

Die Zustandsfrage darf ebenfalls einfacher gestellt werden: Bei festem Gesamt-N ist μN nur ein skalares Energieglied. Eine fundamentale Theorie muss keine unbeobachtbare Energiekonvention auswählen. Sie muss aber den physisch relevanten Zustand oder die Randbedingung begründen. Dazu wird kein Experimentator außerhalb des Universums gebraucht, der das Universum aus dem leeren Fockzustand präpariert. Die interne Präparation eines konkreten Tests bleibt eine davon verschiedene Aufgabe.

Auch das konkrete Gegenbeispiel zur sektorübergreifenden Zustandswahl ist korrekt. Die beibehaltene Voll-Fock-Casimirschranke ergibt bei g/Δ=1/20 und μ/Δ=1/50

\[
H_\mu\ge\left(\mu-\frac{15g^2}{2\Delta}\right)N_f+2\mu N_b
\ge\frac{\Delta}{800}N.
\]

Der leere Zustand ist dann eindeutig energetisch bevorzugt. Die Quellenpins des früheren Zertifikats wurden abgeglichen; sein großer Lauf wurde nicht wiederholt. Der genaue Koeffizient 1/800 wurde erneut rational geprüft. In der Interventionsformulierung ist „nichtverschwindende Differenz“ die passende Bedingung; auch unser negativer Effekt ist ein Nachweis.

**Übernahmeentscheidung:** Diese Notiz trägt als Priorisierung. Eine zusätzliche globale Quell-/Kompositionsregel muss voneinander unterscheidbare Vorkommen, ihre Kopplung, den Zustand und die internen Instrumente gemeinsam liefern. Sie ist im Text noch nicht konstruiert. Der neu gelöste Dreizustandsversuch ist ein kleiner positiver Referenzvertrag, keine solche wachsende Welt. Den exakten lokalen Pol weiter zu verfeinern bleibt nützlich, ersetzt aber diese Herkunftsfrage nicht.
