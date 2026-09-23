# Was wir beim Vereinfachen nicht verlieren dürfen

12. September 2026. Fortsetzung des Compiler-Neustarts, keine universelle Lösung.

## Der einfache Gedanke

Vielleicht benötigen wir nicht zuerst einen größeren Raum. Wir müssen zuerst
unterscheiden, was eine einzelne Operation ist und wie mehrere Operationen
tatsächlich stattfinden. Eine Zahl, ein Spektrum oder eine gemittelte Matrix
beschreibt nicht automatisch den vollständigen Ablauf.

Das lässt sich bildlich an einer Bewegung sehen: Eine einzige Bewegung mit
der durchschnittlichen Richtung ist etwas anderes als eine Folge wechselnder
Bewegungen. Selbst wenn die mittlere Richtung gleich ist, können die
Verteilungen der erreichten Orte verschieden sein. Das Bild erklärt nur den
Unterschied; die konkrete Quantenrechnung steht im technischen Bericht.

## Was jetzt tatsächlich geprüft wurde

Aus derselben vorhandenen TFPT-Kante und ihren sechs Clock-Ansichten wurden
zwei bedingte Modelle verglichen:

- Die sechs Generatoren zuerst mitteln und danach entwickeln.
- Jeweils eine Einzeloperation ausführen und danach die Ergebnisse mitteln.

Beide haben denselben ersten Entwicklungsterm. Der zweite Term unterscheidet
sich aber exakt. Im ersten Modell bleibt ein gewählter innerer Zustand
unsichtbar. Im zweiten entsteht bei kleinen Pulswinkeln ein zugänglicher
Anteil theta²/6. Nach anschließender ursprünglicher Dynamik erhält man auch
eine Antwort am ursprünglichen Rand; deren theta² tau²-Koeffizient ist 7/384.

Das sind gekoppelte mathematische Ausgaben derselben festgelegten Konstruktion,
keine gemessenen Naturkonstanten. Die Einzelereignisse und ihre Statistik sind
noch nicht als physischer TFPT-Prozess hergeleitet. Der Unterschied zwischen
gemitteltem Generator und Ereigniskanal war schon bekannt; neu sind hier die
vollständige zweite-Moment-Prüfung und die kontrollierte Verfeinerungsgrenze.

## Die entscheidende Gegenprobe

Wenn man die Ereignisse immer kürzer macht, ihre Gesamtdauer festhält und
nach jedem Schritt unabhängig neu auswählt, verschwindet der zusätzliche
Effekt im Grenzübergang. Die Entwicklung nähert sich dem gemittelten Modell.

Wählt man dagegen einmal eine Operation und behält diese Wahl bei, bleibt
die Verteilung der unterschiedlichen Entwicklungen erhalten. Gleiche
Einzelschritt-Statistik bedeutet also nicht denselben zeitlichen Prozess.

Deshalb ist „einfach immer wieder iterieren“ noch keine Lösung. Die Quelle
muss bestimmen, was wiederholt wird, welche Information zwischen den Schritten
erhalten bleibt und was die Schrittweite bedeutet. Ein physischer Zeitmaßstab
folgt nicht allein aus dem Iterationszähler.

## Welche fundamentale Frage daraus folgt

Der Kandidat für die gesuchte Einfachheit lautet als Arbeitsfrage:

**Ist das Grundobjekt eine Operation samt ihrer Kompositions- und
Informationsregel, während die bekannten Räume und Zahlen nur bestimmte
Ansichten dieses Ablaufs sind?**

Die Rechnung beweist diese universelle Hypothese nicht. Sie zeigt aber an einem
konkreten Beispiel, dass der Mittelwert eines Ablaufs zu wenig Information
enthält, um seine beobachtbaren Folgen eindeutig zu bestimmen.

Der nächste entscheidende Herkunftstest ist daher eng: Definiert der
ursprüngliche Compiler tatsächlich Einzelereignisse und deren Folge — oder
nur einen zusammengesetzten Operator? Falls Einzelereignisse vorkommen:
Woher kommen ihre zeitlichen Korrelationen, ihre Dauer und ihr Zustand?
Erst eine belegte Antwort erlaubt es, diese Dynamik an externe Phänomene
anzuschließen. Ein passender Zufallsprozess wäre sonst nur eine neue Annahme.

## Nachweise und Grenzen

21 exakte Prüfungen pro Ausführungsmodus, mit identischen Ergebnissen.
Die Grenzaussage ist zusätzlich durch eine ausgeschriebene Fehlerschranke
begründet. Keine neue unabhängige Messvorhersage, keine vollständige
Rekonstruktion des Compilers und keine Schließung von T1–T8.

[Technische Herleitung und Prüfbericht](../experiments/theory-contracts/primitive-transfer-selection-20260912/PROCESS_MOMENT_AUDIT.md).
Für den allgemeinen Hintergrund der Ensemble-Dynamik:
[Kropf, Gneiting und Buchleitner](https://arxiv.org/abs/1511.08764).

## Fortsetzung: Was die ursprüngliche Schleife wirklich macht

Die direkte Quellprüfung beantwortet die nächste Frage für die untersuchte
Konstruktion: Ihre Schleife baut eine Matrix auf. Sie definiert keine Folge
physischer Ereignisse. 30 Schreibvorgänge betreffen nur 15 verschiedene Kanten;
einige Einträge werden mehrfach identisch geschrieben. Alle 120 Reihenfolgen
der fünf Kanten-Umläufe ergeben exakt dieselbe Matrix. Die Wiederholungen als
Ereignishäufigkeiten zu lesen würde die relativen Kopplungen verändern.

Eine zweite exakte Gegenprobe zeigt, was ein Spektrum vergessen kann: Zwei
zusätzlich angenommene Kantenpulse in umgekehrter Reihenfolge haben dasselbe
vollständige Spektrum. Bei derselben festgehaltenen Präparation und Messung
liefern sie trotzdem Wahrscheinlichkeit 0 gegenüber 1. Dieser Test betrifft
Carrier-Zugriff, nicht eine bereits verfügbare Messung am ursprünglichen Rand.
Der ausgewählte Messfall wurde während der Rechnung gefunden, nicht blind
vorhergesagt.

Der einfache Kern ist damit genauer: Nicht nur der Operator, sondern seine
Beziehung zu Zustand, Messung und Reihenfolge muss erhalten bleiben. Wenn
man alles gemeinsam umbenennt, ändert sich nichts; wenn man nur die Abläufe
vertauscht und Präparation sowie Messung festhält, kann sich das Ergebnis ändern.

Das ist eine konkrete Grenze einer bloßen Spektralbeschreibung, keine
vollständige universelle Lösung. 371 exakte Kontrollen je Modus bestanden,
darunter viele kleine Prüfungen identischer Schreibzugriffe.
[Quellenprüfung und vollständiger Nachweis](../experiments/theory-contracts/primitive-transfer-selection-20260912/ASSEMBLY_NOT_HISTORY.md).
