# Lokale Randrekonstruktion: Auswahl und einfacherer Spinor

20. September 2026 · **UR.SOURCE.BOUNDARY_SELECTION.01: PARTIAL**

Der neue Vorschlag ist eine konkrete lokale Kontinuumkonstruktion: Acht
rechte Randkanäle werden um ein rechtes und ein linkes Hilfspaar ergänzt;
eine geeignete Wechselwirkung lässt einen E8-Rand und ein massives Paar
übrig. Ich habe die Auswahl dieser Wechselwirkung geprüft und die
Konstruktion so vereinfacht, dass keine einzelne ursprüngliche Farbkomponente
ausgezeichnet werden muss.

**Neues Ergebnis:** Innerhalb dieser ausdrücklich erweiterten Modellklasse
lässt sich der gewünschte Spinor als lokales Produkt von **drei rechten
Fermionen und einem linken Hilfsfermion** darstellen. Bei einer passenden,
blockweise symmetrischen Energiematrix ist dieses Viererprodukt ein reiner
chiraler Strom mit Gewicht eins. Sein Ladungs- und Klebewörterbuch bleibt
erhalten. Die zusätzliche physische Randphase ist damit weiterhin eine
Voraussetzung; ihre Auswahl aus TFPT ist nicht bewiesen.

## Die Wechselwirkung ist weniger beliebig, als sie zunächst aussieht

Der vorgeschlagene Vektor

    n=(1,1,1,-1,-1,-1,-1,-1,-1,3)

ist eine minimale neutrale charakteristische Nullrichtung im angegebenen
Gitter mit neun rechten und einer linken Richtung. „Charakteristisch“ heißt
hier, dass seine Statistik den verbleibenden Quotienten gerade macht.
Aus Ganzzahligkeit und Nullnorm folgt: Die letzte Komponente muss mindestens
Betrag drei haben; im kleinsten Fall sind alle neun anderen Komponenten
Vorzeichen. Neutralität erzwingt davon genau drei Pluszeichen.

Die vollständige Auswahlkette lautet:

| Zusätzlich geforderte Eigenschaft | Verbleibende Kandidaten |
|---|---:|
| Minimal, neutral, charakteristisch; feste Orientierung | 84 |
| Die angegebene Vierergraduierung bleibt erhalten | 56 |
| Kopplungsvektor ist innerhalb der Farb-, schwachen und Familienblöcke symmetrisch | 2 |
| Das **orientierte** D8-/Spinorwörterbuch bleibt gleich | 1 |

Diese Bedingungen werden nicht aus P1/P2 behauptet. Die Tabelle zeigt, was
sie innerhalb des Kandidaten tatsächlich leisten. Ohne die benannte
Blocksymmetrie bleiben selbst mit der letzten Phasenbedingung 25 Kandidaten.

Die zwei vorletzten Möglichkeiten unterscheiden sich an einer wichtigen
Stelle: Einmal tragen die drei Farbkoordinaten das Pluszeichen, einmal die
drei Familienkoordinaten. Beide Quotienten sind abstrakt E8. Aber die zweite
Wahl kehrt die Spinorphase von i nach -i um, während die ganzzahligen
D8-Ladungen unverändert erscheinen. Ein Test allein an D8 hätte den
Unterschied übersehen.

Die ersten fünf Koordinaten sind der D5-Träger mit **Farbe 3 + schwach 2**;
die folgenden drei gehören zu A3/Familie. Die Drei im gelieferten Vektor
steht somit an den Farbplätzen. Sie darf nicht wegen der gleichen Zahl als
Herleitung dreier Familien ausgegeben werden.

## Die einfachere lokale Ausführung

Die Zusatzkanäle sind im Vorschlag bereits ausgezeichnet. Deshalb lässt
sich der rechte Zusatzkanal als Bezug verwenden. Mit e9 für diesen Kanal
und der Statistikmatrix K ist

    m=n+e9,
    V_aux=K+2 K m m^T K.

Diese vollständig ausgeschriebene positive Energiematrix hat dieselben
Eigenwerte wie die ursprüngliche Konstruktion und erhält die angegebenen
Permutationen innerhalb der drei Blöcke. Der ganzzahlige Basiswechsel hat
Determinante ±1; das gesamte lokale Operatorgitter bleibt erhalten.

Der bisher kürzere Vertreter

    b_aux=(1,1,1,0,0,0,0,0,0,1)

wird in dieser Darstellung zum **reinen E8-Spinorstrom**. Er hat keine
Komponente im massiven Paar. Der längere Vertreter des Eingangstextes
unterscheidet sich genau um die neutrale Wechselwirkungsrichtung n. Weil
das D8-Wörterbuch mittransformiert wird, bleiben Ladung, Spinorphase und
doppelter Ladungsübertrag konsistent.

Die Rechnung prüft die ganzzahligen Abbildungen aller 240 Wurzeln und
sämtliche 57.600 Wurzelpaarungen. Sie ersetzt keine erneute Prüfung aller
Kokzyklus- und mikroskopischen Clockbehauptungen des Eingangstextes.

## Der Relevanztest besitzt einen offenen Spielraum

Am exakt zerlegten Punkt hat n Skalendimension eins. Alle anderen
neutralen Selbstnullcosinusse haben mindestens Dimension vier. Eine
ausdrückliche kontinuierliche Verformung der Energiematrix des Hilfspaars
lässt diesen Abstand bestehen: Für |eta|<log(2)/2 bleibt nur ±n relevant.

Das ist ein allgemeiner Dimensionssatz für diese Störungsklasse, keine
Behauptung einer vollständigen Stabilität gegenüber beliebigen
Gitterwechselwirkungen. Die Parameter des Hamiltonoperators bleiben frei.

## Was dies für das Gesamtziel bedeutet

Der zuvor nur abstrakte Spinor kann in einer geeigneten gemeinsamen
Randphase ein lokales zusammengesetztes Feld sein. Die zusätzliche
Wechselwirkung muss also nicht einfach einen neuen elementaren Spinor
postulieren. Dieser Mechanismus ist aus der Forschung zu unterschiedlichen
Randphasen bekannt; siehe [Cano und Kollegen](https://arxiv.org/abs/1310.5708).
Hier wurden das konkrete TFPT-Wörterbuch, seine Orientierungsunterscheidung
und die symmetrische kurze Darstellung geprüft.

**Die offene Herkunft lässt sich dadurch genauer benennen:** Erzeugt der
TFPT-Ursprung diese Kanäle, diese physische Graduierung und Wechselwirkungen
in diesem Rekonstruktionsbereich? Ein nachträglich passender Gitterbasiswechsel
beantwortet das nicht. Die eigentlichen C/J-Wirkungen müssen außerdem auf
der Quelle selbst erhalten und mit derselben Zeit verknüpft werden.

„Spinor“ meint hier eine interne D8-Darstellung. Der gefundene
Gewicht-eins-Strom ist bosonisch und noch kein vierdimensionales
Spin-1/2-Teilchen. Auch die dynamische Raumgeometrie, das chirale
Standardmodell und die Gravitation folgen aus dieser Randrechnung nicht.

Die vollständige Herleitung einschließlich Gegenkandidaten und freier
Voraussetzungen steht in [PROOF.md](PROOF.md). Ein getrenntes Agentenreview
steht in `SELECTION_REVIEW.txt`; eine externe Begutachtung liegt nicht vor.
`checker.py` prüft die exakten endlichen Kontrollen und Quellenpins auch
unter `python3 -OO`. Es gibt keine Paper-, Physikledger- oder T1–T8-Promotion.

Der anschließende [Abgleich mit der gemeinsamen Quellwirkung](LANE_FUNCTIONAL.md)
ergibt einen weiteren konkreten Ladungstest: Soll das zusätzliche Paar ein
vektorartiges Farb-/schwaches Singulett sein und das ursprüngliche
Hyperladungswörterbuch erhalten, müssen seine Komponenten Hyperladung eins
tragen. Ein neutrales Zusatzpaar wäre mit der gewählten Wechselwirkung
unverträglich. Zugleich kürzt sich ein identischer massiver Faktor aus der
relativen Down-/Leptonphase heraus. Eine echte unterschiedliche Wirkung
verlangt unterschiedliche, aus derselben Quelle hergeleitete Deformationen.
