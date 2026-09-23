# TFPT: Ein gemeinsamer Versuch statt drei getrennter Bausteine

14. September 2026 · Version 1.0 · Anschlussarbeit nach dem PDF-Export v1.2.

## Kurz gesagt

Wir haben jetzt eine ausdrücklich festgelegte kleine Maschine, bei der
**Aufzeichnen, Präparieren und der Verlauf über mehrere Zeitpunkte aus derselben
Kopplung berechnet werden**. Sie verwendet tatsächliche Zustände und Operationen
des TFPT-Compilers. Die noch zusätzlich notwendige Kopplungsoperation ist jetzt
genau benannt und gegen den alten Compiler abgegrenzt.

Das ist keine vollständige TOE. Es löst aber die vorher nur formulierte
endliche Zusammensetzungsaufgabe innerhalb klar genannter Zusatzannahmen.

## Das Bild dazu

Zwei Bausteine treffen aufeinander. Ein Vermittler kann einen gemeinsamen
Zustand kurz aufnehmen. Ein kleines Kontrolllämpchen merkt sich nur:
**„Vermittlung passiert“ oder „nicht passiert“.**

Das Lämpchen darf nicht verraten, welcher vertauschte Farbweg benutzt wurde.
Sonst zerstört es genau die Interferenz, aus der die gewünschte Bindung entsteht.
Nach dem Rückweg des Vermittlers sind die ursprünglichen Bausteine wieder da,
und das Lämpchen enthält eine korrekt berechnete Aufzeichnung.

Wird dieselbe Aufzeichnung kohärent ein zweites Mal benutzt, lässt sie sich
rückgängig machen. Wird stattdessen eine frische Aufzeichnung angelegt und die
alte behalten, bleibt eine andere gemeinsame Geschichte zurück. Daher können
gleiche erste Momentaufnahmen unterschiedliche spätere Antworten liefern.

## Was konkret gelungen ist

**1. Eine vollständige lokale Operation.** Die korrigierte 22-dimensionale
Operation plus binärem Record ist für alle Eingänge normerhaltend. Beide
Ausgänge sind berechnet. Ein gemeinsamer 832-dimensionaler Träger trägt
alle sechs möglichen Kanten; das gewählte Protokoll hat höchstens einen
aktiven Vermittler. Diese Zahl ist eine Laborbuchhaltung, keine behauptete
Dimension unseres Universums.

**2. Präparation aus einfachen Compilerzuständen.** Ausgangspunkt sind vier
unverschränkte, tatsächlich vorhandene Quellzustände. Die gleiche Aufzeichnung
wird auf drei Sternkanten wiederholt. Akzeptiert man die jeweils passenden
Records, nähert sich der Zustand dem gewünschten antisymmetrischen Zellzustand.
Ein schon fertig präparierter Zielzustand oder ein neuer Kühl-Hamiltonoperator
wird dafür nicht eingesetzt.

Nach acht Runden beträgt die bedingte Zielfidelität rund **99,9999245 %**.
Die Wahrscheinlichkeit, diese ganze Recordfolge zu erhalten, beträgt rund
**4,16667 %**. Das sind unterschiedliche Größen: hohe Qualität im Erfolgsfall
ist nicht gleich hohe Ausbeute pro Versuch.

**3. Fehlschläge sind mitgerechnet.** Vorhandene Compiler-Messungen und
ausgangsabhängige Pauli-Operationen können nach einem Fehlschlag den
einfachen Ausgangszustand erneut erzeugen. Damit braucht man höchstens
24 Versuche im Mittel. Die Beendigung ist fast sicher, aber nicht nach einer
festen Maximalzahl garantiert. Das benötigt einen Controller und einen Reset,
nicht schon einen kosmologischen Entstehungsmechanismus.

**4. Die tatsächliche Compiler-Uhr ist angeschlossen.** Eine dreizyklische
Quelloperation wurde auf allen 240 phasenmarkierten Wurzeln geprüft und in
denselben Versuch eingesetzt. Nach Vorbereitung, Tick, zwei Aufzeichnungen,
Rück-Tick und derselben Schlussprüfung ergeben sich:

| Registerverwendung | Nach acht Vorbereitungsrunden | Im idealen Präparationsgrenzfall |
|---|---|---|
| Dieselbe Aufzeichnung kohärent erneut benutzen | Rückkehr ca. 99,9999245 % | 100 % |
| Eine neue Aufzeichnung anlegen | Rückkehr ca. 53,1258168 % | 17/32 = 53,125 % |

Diese Rückkehrwahrscheinlichkeiten gelten **nach erfolgreicher erster
Präparation**. Die erste Ausbeute von etwa 4,17 % ist nicht verschwunden.
Die endlichen Werte wurden als exakte Brüche berechnet. Weil die echte
lokale Uhr den kleineren Präparationssektor verlässt, wurde ihr Versuch im
vollen 256-dimensionalen Materieraum gerechnet.

## Was uns jetzt noch fehlt

Die neue Austausch-Aufzeichnung lässt sich nicht allein mit der bislang
nachgewiesenen Clifford-/Stabilizer-Klasse des Compilers realisieren.
Das ist ein präziser Ausschluss, nicht nur ein fehlender Programmiertrick:
Auf einem zulässigen einfachen Eingang erzeugt sie einen Zustand mit
13 nichtverschwindenden Amplituden, außerhalb dieser Zustandsklasse.

Wir haben also jetzt **eine konkrete Maschine und ihren Test**, aber noch
nicht den vollständigen Nachweis, dass TFPT selbst genau diese zusätzliche
Kopplung und ihren Belegungszugriff erzeugt.

Auch macht die Maschine ohne Auswahl und Reset nicht von allein den richtigen
Zustand: Ungelesene Austauschmessungen erhalten sein vorhandenes Gewicht.
Ihre ganze Fixpunktalgebra ist ausdrücklich nicht eindimensional. Die
kontrollierte Präparation darf daher nicht als autonome Kühlung ausgegeben werden.

## Der nächste entscheidende Schritt

Der bisherige diffuse Satz „Es fehlt Dynamik“ wird jetzt zu einer konkreten
Aufgabe: **Eine tatsächliche phasenmarkierte Quelloperation muss genau die
benötigte kohärente Vermittlung samt Rückweg und Belegungsaufzeichnung tragen.**

Ein Kandidat muss die beiden Recordausgänge, den 13-Amplituden-Test,
die Präparationsausbeute und die endlichen Echozahlen gemeinsam reproduzieren,
ohne einen fremden Hilfszustand zu verstecken. Erst anschließend sind eine
skalierende Raumzeitfamilie, ein vollständiges chirales Maß und ein dynamischer
Spin-2-Sektor sinnvoll als nächste Stufe zu verlangen. Diese T1–T8-Nachweise
sind weiterhin nicht konstruiert.

## Belege und Einordnung

231 eigene exakte Prüfpunkte, zusätzlich 1073 Quell-Präfixprüfungen.
Normale und optimierte Ausführung sind bytegleich. Fünf absichtlich eingebaute
Fehler werden erkannt. Allgemeine Aussagen beruhen auf ausgeführten
Operator- und Konvergenzbeweisen, nicht auf der bloßen Anzahl dieser Tests.

Die ausführlichen Herleitungen, Ressourcenannahmen, exakten Brüche und
Replay-Dateien liegen im
[technischen Forschungsbericht](../experiments/theory-contracts/compiler-single-execution-20260914/README.md).

Die zuvor exportierte Gesamt-PDF v1.2 enthält TFPT-Basics, Clocks,
Standardmodell-Zuordnungen, Zahlen und den Sechs-Quellen-Audit. Dieser Text
dokumentiert die ausdrücklich danach ausgeführte neue Forschungsarbeit.
