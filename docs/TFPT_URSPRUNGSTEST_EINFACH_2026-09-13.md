# Zurück zum Compiler: Eine Regel ist schon da — was beschreibt sie vollständig?

13. September 2026. Drei unabhängige Arbeitsstränge plus direkte Gegenrechnung.
Die vollständige TOE ist nicht gelöst. Keine neue räumliche Kette hinzugefügt.

## Aktuell: Was der Baustein ist und wie er sich zusammensetzt

Die Messkonstruktion wurde bis zu einer einfachen gemeinsamen Operation
zwischen Register und System zerlegt: Passende Basispositionen erhalten
ein Minuszeichen, alle anderen nicht. Diese Kopplung lässt sich durch
zwei registerübergreifende kontrollierte Phasengates und lokale Operationen
darstellen. Sie ist allerdings eine echte zusätzliche Wechselwirkung;
vorhandene getrennte Einzelspiegelungen erzeugen sie nicht automatisch.
Die benötigten kontrollierten Phasengates sind als einzelne Gate-Typen
selbst schon ursprüngliche Spiegelungen. Offen ist ihre Anwendung zwischen
verschiedenen Registern: Der Baukasten enthält das Teil, aber die erlaubte
Verbindung mehrerer Träger muss ebenfalls aus der Quelle folgen.

Der Zusammensetzungstest zeigt, warum das Register keine Nebensache ist:
Nach dem ersten Schritt kann das System allein vollständig gemischt
aussehen, obwohl seine Information gemeinsam mit dem Register erhalten
ist. Derselbe Schritt mit demselben noch kohärenten Register stellt den
ursprünglichen reinen Zustand wieder her. Mit frischen Registern entsteht
dagegen die erwartete Folge von Messungen. Beide Abläufe sind exakt geprüft.

Auch die Reihenfolge hat zwei Gesichter. Werden alle Ergebnisse vergessen,
bleiben bei mehreren dieser Kontextmessungen nur die gemeinsam erhaltenen
Pauli-Komponenten übrig; diese gemittelten Abbildungen sind vertauschbar.
Das Ergebnisprotokoll kann die Reihenfolge trotzdem erkennen: Ein festes
Paar von Ergebnissen hat in einem Quellbeispiel Wahrscheinlichkeit 1/2
in der einen und 1/4 in der umgekehrten Reihenfolge.

**Die schärfere Arbeitshypothese:** Die Geometrie organisiert die möglichen
Fragen und Operationen. Die tatsächliche Dynamik benötigt zusätzlich die
Kopplung und einen Vertrag darüber, wie Aufzeichnungen entstehen, erhalten
bleiben oder abgegeben werden. Das ist im geprüften endlichen Modell
konkret, noch keine universelle Ableitung von Naturgesetzen.

Der nächste Herkunftstest muss genau diese gemeinsame Kopplung und die
Registerbereitstellung in der mikroskopischen Quelle finden. Einfach nur
dieselbe Matrix weiter zu potenzieren genügt nicht, um eine dauerhafte
irreversible Entwicklung zu begründen.

[Vollständiger Kompositionsbeweis und Prüfer](../experiments/theory-contracts/compiler-origin-audit-20260913/RECORD_COMPOSITION.md).

## Neueste Fortsetzung: Ein konkreter gemeinsamer Prozess ist konstruiert

**Der stärkste neue Anschluss:** Die vier ursprünglichen Wurzelspiegelungen
einer Messbasis ergeben bei gleichmäßiger zufälliger Anwendung exakt dieselbe
Zustandsänderung wie deren Messung mit vergessenem Ergebnis. Dafür braucht
es keine neue Kopplungsmatrix. Diese besonders kurze Identität funktioniert
hier gerade aufgrund der vier Basiszustände.

Die Ergebnisse selbst werden dadurch noch nicht bestimmt: Das Protokoll
„welche Spiegelung wurde benutzt?“ ist nicht das Protokoll „welches
Messergebnis trat auf?“. In einer expliziten kohärenten Realisierung wandelt
eine weitere schon vorhandene Compiler-Spiegelung die Auslesebasis des
Hilfsregisters so um, dass genau die Born-Messzweige entstehen. Die nötige
kohärente Steuerung und das reale Auslesen sind damit mathematisch
beschrieben, aber nicht aus dem mikroskopischen Ursprung hergeleitet.

Der Rückgang zur Quelle hat eine bereits vorhandene, bisher hier nicht
ausgenutzte Bedeutung der Labels hervorgeholt: Jedes Label steht für eine
vollständige Messbasis mit vier möglichen Ergebnissen. Die insgesamt
60 Zustandsstrahlen liegen bereits im ursprünglichen E8-Compiler vor.

Wenn diese Basen nach den Regeln der Quantenmechanik scharf und wiederholbar
gemessen werden, ist der Zustandswechsel eindeutig. Kombiniert mit der
vorhandenen Wahlregel K ergibt das einen genau bestimmten endlichen Prozess.
Von jedem Strahl aus bleiben nur 13 mögliche Nachfolger: derselbe mit
Wahrscheinlichkeit 1/7 und zwölf weitere mit jeweils 1/14.

Das gibt ein konkretes Beispiel für deine Idee der verschiedenen Schatten:

- Nur die Messfragen betrachtet: Es erscheint wieder die ursprüngliche
  15-Label-Regel K.
- Den mittleren Quantenzustand betrachtet: Seine nichttrivialen Komponenten
  werden pro Schritt um den Faktor 3/7 abgeschwächt.

Beides folgt exakt aus derselben Konstruktion, für beliebig viele Schritte.
Warum 3/7? Von den sieben möglichen nächsten Messbasen erhalten jeweils
drei eine bestimmte aktuelle Pauli-Komponente. Die übrigen löschen sie.

Das ist eine positive bedingte Lösung einer zuvor offenen endlichen
Verbindungsfrage. Die Messbasen wurden aus den ursprünglichen Wurzeln
nachgerechnet, nicht passend ausgewählt. **Noch nicht hergeleitet ist,
warum der physische Ursprung überhaupt genau diese wiederholbaren
Messungen und diese Kontextwahl ausführt.** Auch die Born-Regel wird hier
vorausgesetzt, nicht erklärt. Der endliche stationäre Zustand ist kein
bereits hergeleitetes Vakuum unseres Universums.

[Vollständiger Beweis und genaue Annahmen](../experiments/theory-contracts/compiler-origin-audit-20260913/CONTEXT_INSTRUMENT.md).

Die folgenden Abschnitte dokumentieren die davorliegende Gegenprüfung.

## Die wichtigste Korrektur

Wir sollten nicht immer wieder eine neue Bewegungsregel erfinden und sie
anschließend optimieren. Im älteren Compiler steht bereits eine sehr einfache:
Es gibt 15 Labels, und von jedem führen sieben gleich gewichtete Übergänge
weiter. Diese Regel heißt mathematisch K=B/7.

Das ist ein vorhandener endlicher Prozess, kein neues Universalobjekt.
Die offene Frage ist: Sind diese Labels Zustände, mögliche Operationen oder
Messkontexte? Und was passiert bei einem Übergang mit den Informationen,
die in dieser Labelbeschreibung gar nicht vorkommen?

## Das einfache Bild: gleicher Reiseplan, anderes Gedächtnis

Stell dir zwei Maschinen vor, die exakt denselben Reiseplan befolgen.
Bei jeder Kontrolle an einer Station sieht man dieselben Häufigkeiten.

- Die erste Maschine liest an jedem Schritt ein Etikett und verwirft die
  Quantenphasen zwischen den Etiketten.
- Die zweite ordnet die Etiketten zufällig um, erhält dabei aber einen
  bestimmten gemeinsamen kohärenten Zustand.

Beide führen exakt die vorhandene klassische Übergangsregel aus. Eine
zusätzliche Interferenzmessung unterscheidet sie jedoch: Für denselben
präparierten Zustand erhält man Wahrscheinlichkeit 1/15 oder 1.
Auch die volle Symmetrie der zugrunde liegenden Labelgeometrie entfernt
diesen Unterschied nicht.

Das sind mathematisch konstruierte Erweiterungen eines klassischen Registers.
Wir haben damit weder eine physische Apparatur hergeleitet noch behauptet,
dass beide Erweiterungen den vollständigen Compiler erfüllen. Insbesondere
sind seine 15 nichttrivialen Wörter keine 15 orthogonalen Zustände seines
vierdimensionalen Spinorträgers.

**Der konkrete Befund:** Gleiche sichtbare Übergänge bestimmen nicht, was
mit der vollständigen Quanteninformation passiert. Auch ein eindeutiger
klassischer Endzustand bestimmt nicht den Endzustand jeder solchen Erweiterung.

## Beim Vereinfachen verschwindet sogar ein Teil des Takts

Die ursprüngliche Regel enthält fünf unabhängige Kontrastmuster, deren
Vorzeichen sich bei jedem Schritt umkehrt und deren Stärke abnimmt.
Nach zwei Schritten ist das Vorzeichen wieder gleich.

Bildlich: Betrachtest du einen abwechselnd hellen und dunklen Takt nur bei
jedem zweiten Schlag, übersiehst du die Alternation. Deshalb ist es wichtig,
nicht das Zweischrittbild mit dem vollständigen Einzelschritt gleichzusetzen.

Die genaue Rechnung ist hier besonders aussagekräftig: Der einzelne Schritt
kann auf demselben geschlossenen klassischen Zustandsraum nicht aus einem
reellen autonomen kontinuierlichen Markovgenerator entstehen. Für zwei
Schritte existiert dagegen eine exakte kontinuierliche Interpolation.
Das beweist weder fundamentale diskrete Zeit noch die Notwendigkeit eines
bestimmten größeren Raums. Es zeigt, welche Information eine vermeintlich
einfachere Beschreibung verloren hat.

## Hilft mehr Symmetrie?

Ein gesonderter Test am ursprünglichen Vierer-Spinorregister wurde vollständig
klassifiziert. Selbst unter einer bewusst stärkeren Symmetrieforderung
bleiben zwei unabhängige Rauschstärken erlaubt. Nach Festlegung der Zeiteinheit
bleibt ihr Verhältnis frei. Die Symmetrie allein wählt also auch in diesem
engen Test keinen eindeutigen Prozess aus.

Diese Zusatzannahmen sind nicht als Naturgesetze hergeleitet. Der Befund sagt
nicht, dass eine einfache zusätzliche Quellregel unmöglich ist.

## Was wir jetzt gezielt suchen sollten

Die bessere Frage lautet vorerst nicht „Welcher noch größere Raum enthält
alles?“, sondern:

> Welche ursprüngliche Regel legt fest, was ein Ereignis ist und welche
> relativen Informationen bei seiner Ausführung erhalten bleiben?

Eine brauchbare Antwort muss drei Dinge gemeinsam liefern:

1. **Was sich ändert:** die Verbindung zwischen ursprünglichen Labels,
   Operatoren und tatsächlichen Zuständen.
2. **Was erhalten bleibt:** eine aus der Quelle abgeleitete Regel für
   Phasen und Messantworten. Ein frei gewähltes Löschen der Phasen zählt nicht.
3. **Was ein Schritt bedeutet:** diskrete Aktualisierung, offene Dynamik
   oder Abtastung eines größeren Prozesses — einschließlich einer begründeten Uhr.

Das könnte eine kurze Regel sein. Dass es eine solche gemeinsame Regel gibt,
ist aber eine Forschungsfrage, nicht durch Eleganz schon entschieden.

Der nächste entscheidende Erfolg wäre, aus den ursprünglichen Seam- und
Compiler-Operationen eine feste Interferenzantwort abzuleiten und damit
zwischen den expliziten Gegenmodellen zu unterscheiden. Danach müsste
dieselbe Konstruktion Komposition und Zeitinterpretation bestehen.

## Was tatsächlich gesichert ist

Die [technische Herleitung und reproduzierbaren Prüfer](../experiments/theory-contracts/compiler-origin-audit-20260913/README.md)
liegen im Repo. Beide Prüfer liefen normal und mit `-OO`; fünf absichtlich
beschädigte Varianten wurden erkannt. Die alten Kettenresultate wurden
nicht verworfen, aber in dieser Runde auch nicht als Hauptspur fortgesetzt.

Keine T1–T8-Aufgabe ist dadurch geschlossen. RH, Faktorisierung, P versus NP
und Hylæan wurden hier nicht neu untersucht. Die Stärke dieses Schritts liegt
in einer konkreten Herkunftsfrage mit unterscheidbaren Antworten, nicht in
einer weiteren Behauptung, schon den universellen Schlüssel gefunden zu haben.
