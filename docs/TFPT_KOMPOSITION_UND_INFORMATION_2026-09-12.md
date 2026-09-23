# TFPT: Der einfache Prozess braucht einen vollständigen Zustand

12. September 2026. Fortsetzung des systematischen Ursprungs-Audits.
**Bedingte mathematische Ergebnisse, keine vollständige TOE-Lösung.**

## Was diesmal konkret herauskam

Drei parallele Gegenprüfungen und der Hauptstrang haben die zuletzt gefundene
Bell-Kopplung an ihrer Zusammensetzung, Auswahl und Informationsverteilung geprüft.
Das Ergebnis ist weder eine neue Zahlenliste noch ein identifiziertes Universalobjekt.
Es ist eine genauere Antwort darauf, wo Einfachheit bereits funktioniert und
wo wir beim Vereinfachen wichtige Information verlieren.

### 1. Eine einfache vollständige Operationsregel existiert

Die benachbarten Bell-Kopplungen erfüllen exakt die bekannten Temperley–Lieb-
Relationen. Dieselben drei Regeln funktionieren auf jeder endlichen Kettenlänge.
Sie erlauben eine bekannte Yang–Baxter-Konstruktion: verschieden angeordnete
lokale Operationen können unter einer präzisen Bedingung dieselbe Gesamtoperation
ergeben. Das ist eine echte algebraische Verbindung, keine Zahlenähnlichkeit.

Aber der dabei verwendete Spektralparameter ist nicht schon physische Zeit.
Unsere nichttriviale unitäre Familie erfüllt mit demselben Parameter gerade
nicht das Gesetz einer autonomen Zeitentwicklung. Graph, Energieskala und
physische Interpretation müssen weiterhin ausgewählt werden.

### 2. Nachbarschaft entscheidet mehr als Symmetrie allein

Auf drei Viererfaktoren lässt die volle angenommene Symmetrie sechs unabhängige
Operatorrichtungen zu. Auch die sehr einfache Vertauschung der beiden äußeren
Teile ist erlaubt. Erst wenn wir einen festen offenen Nachbarschaftsgraphen,
ausschließlich zweikörper-lokale Kopplungen, Spiegelgleichheit und einen
Bell-bevorzugenden Paargrundzustand verlangen, bleibt der gewählte
Bell-Kopplungstyp bis auf Energieskala und Nullpunkt übrig.

Das ist ein positiver bedingter Auswahlsatz. Es ist noch keine Herleitung
dieser Nachbarschaft oder der angenommenen vollen Symmetrie aus TFPT.

### 3. Die Entstehungsreihenfolge ist im verkürzten Code nicht wegdefinierbar

Wir haben dieselbe Dreiercodierung zweimal eingesetzt, aber an verschiedenen
Stellen. Die drei resultierenden Einbettungen in fünf Faktoren besitzen jeweils
vier logische Dimensionen. Gemeinsam benötigen ihre unveränderten Bilder jedoch
zwölf Dimensionen. Ein bloßer logischer Basiswechsel kann sie nicht gleichsetzen.

Entscheidender: Zwei dieser Einbettungen besitzen unter **demselben festen
Fünfer-Hamiltonoperator** verschiedene Energie-Erwartungswerte:

    69/40 gegenüber 39/20, Differenz 9/40.

Diese Werte gelten jeweils für jeden normierten logischen Eingang. Daher
kann keine mit diesem Hamiltonoperator kommutierende Unitäre die beiden
Codierungen ineinander überführen. Eine unbeschränkte Änderung des physischen
Zustands oder der Observable ist etwas anderes als dieselbe Beschreibung.

Bildlich: Zwei gleich aussehende Baupläne sind hier nicht dieselbe Maschine;
unter demselben Prüfgriff reagieren sie unterschiedlich. Die Reihenfolge
wegzuwerfen war eine zusätzliche Annahme, keine bereits bewiesene Vereinfachung.

### 4. Das Schattenbild lässt sich exakt berechnen

Eine feste Baumcodierung bewahrt den vollständigen Quantenzustand. Betrachtet
man dagegen nur einen bestimmten äußeren Endpunkt, schrumpft sein zugänglicher
nichttrivialer Zustandsanteil pro Stufe um den Faktor 3/5.

Nach vier Stufen kann dieser einzelne Ausgang keine Verschränkung mit einem
externen Referenzsystem mehr erhalten. Er enthält weiterhin klassische
Information. Die vollständige gemeinsame Ausgabe bewahrt dagegen die
ursprüngliche Quanteninformation.

Das ist ein exakter Unterschied zwischen vollständigem Zustand und lokalem
Schatten, kein Nachweis eines physikalischen Horizonts oder holographischen
Flächengesetzes. Andere Endpunkte und größere Ausgangsregionen sind damit
noch nicht vollständig klassifiziert.

## Konsequenz für die Suche nach dem fundamentalen Baustein

Der belastbare nächste Ansatz lautet: **Die einfache Operationsregel behalten,
aber den Zustandsraum nicht verkleinern, bevor seine relevanten Informationen
und seine Dynamik nachweislich erhalten bleiben.**

Ein größerer Zustandsraum macht das zugrunde liegende Gesetz nicht automatisch
kompliziert. Schon eine kurze rekursive Regel kann viele unterscheidbare
Zustände erzeugen. Ob TFPT genau diese Regel auswählt, bleibt zu beweisen.

Die nächsten entscheidenden Tests sind:

- Umgruppierungen müssen dieselben markierten Operatoren und die gewählte
  Dynamik erhalten, nicht nur Räume gleicher Dimension verbinden.
- Der ursprüngliche Compiler muss aktive Paarung, Nachbarschaft und
  Zustandsentwicklung auswählen; hinzugefügte Annahmen bleiben sichtbar.
- Ein Decoder für gemeinsame Ausgangsregionen muss tatsächlich ausführbar
  sein; abstrakte globale Rekonstruierbarkeit beweist noch keinen günstigen Zugriff.

Keines der acht physischen T1–T8-Tore wird dadurch geschlossen. RH,
Faktorisierung und P versus NP wurden in dieser Runde nicht neu untersucht;
die Ergebnisse werden nicht ohne eigene Brücken auf diese Probleme übertragen.

## Belege

[Vollständige Herleitung, Grenzen und Reproduktion](../experiments/theory-contracts/systematic-origin-audit-20260912/refinement/README.md).

Einordnung in bekannte Mathematik:
[Temperley–Lieb und Yang–Baxter](https://arxiv.org/abs/1601.04378),
[Entanglement-breaking-Kanäle](https://arxiv.org/abs/quant-ph/0302031).
Die Algebra und die Kanaltheorie sind nicht neu entdeckt worden; neu geprüft
wurde ihre konkrete Rolle und ihre Grenze in diesem bedingten TFPT-Kandidaten.

## Fortsetzung: Die Dynamiklücke ist im endlichen Modell repariert

Die nächste Runde ging über die Feststellung des Fehlers hinaus. Im gleichen
Fünferblock und mit unveränderten Kopplungen wurde eine exakt geschlossene
Beschreibung konstruiert. Dafür müssen wir fünf Paarungsrichtungen behalten,
jeweils mit dem vierdimensionalen logischen Zustand: insgesamt 20 Dimensionen.
Die bisherige gemeinsame 12-dimensionale Spanne reicht nicht.

**Dieser Teil ist wirklich gelöst:** Die rekonstruierte 20-dimensionale
Zeitentwicklung stimmt für alle Zeiten exakt mit der ursprünglichen
Zeitentwicklung in diesem Teilraum überein. Es ist keine bloße Näherung für
kleine Zeiten. Wir haben keine zusätzlichen Kräfte eingesetzt, sondern zuvor
verworfene Zustandsanteile mitgeführt.

Auch ein deterministischer Decoder ist konstruiert. Er kann denselben logischen
Zustand aus den drei verschiedenen Codierungen zurückgewinnen. Die Unterschiede
des Aufbaus verbleiben dabei in einem Hilfssystem mit mindestens drei
Dimensionen. Es wird keine Information einfach gelöscht. Die konkrete native
Ausführung, Ansteuerung und Energieversorgung dieses Hilfssystems fehlen noch.

Zwei kürzere Reparaturen wurden ebenfalls geprüft:

- Kopplungsgewichte anzupassen kann die mittleren Energien gleichmachen,
  aber nicht ihre Streuungen. Diese Variante bleibt dynamisch verschieden.
- Alle Codierungen auf denselben niedrigsten Sektor zu filtern funktioniert
  bedingt, aber nur mit Erfolgswahrscheinlichkeiten von etwa 88,8 % beziehungsweise
  60,4 %. Der alternative Decoder benötigt keine solche Nachselektion; dafür
  benötigt er das Hilfssystem und Kontrolle.

### Die neue, jetzt präzise Grenze

Die geschlossene 20-dimensionale Beschreibung erhält die gewählte Dynamik,
aber nicht alle Eingriffe. Bereits ein ursprünglicher lokaler Compiler-
Generator kann sie verlassen. Die Gegenprüfung ergab sogar einen allgemeinen
Satz für die vorausgesetzte offene Bell-Kette:

> Wenn die Dynamik und sämtliche Compiler-Operationen an nur einem Endpunkt
> exakt erhalten bleiben sollen, wird der gesamte Zustandsraum benötigt.

Beim Fünferblock sind das 1024 Dimensionen. Das ist eine Aussage über exakte
invariante Unterräume, keine Aussage darüber, dass jede Berechnung eine dichte
1024er-Matrix speichern muss, und kein Beweis effizienter universeller Steuerung.

Bildlich: Eine kleine Beschreibung kann die ungestörte Fahrt korrekt vorhersagen.
Sobald wir alle erlaubten Eingriffe am Steuer zulassen, brauchen wir auch die
Zustände, die dadurch erreichbar werden. Wir müssen daher **Gesetz, Zustand
und Zugriff** getrennt prüfen. Ein kurzes Gesetz darf einen großen Zustandsraum
haben; das ist kein Widerspruch zur gesuchten Einfachheit.

[Neue exakte Reparatur, Decoder, Zugangssatz und Prüfergebnisse](../experiments/theory-contracts/systematic-origin-audit-20260912/dynamical-refinement/README.md).
Die globale Grundenergie wurde zusätzlich im vollständigen 1024-dimensionalen
Raum numerisch kontrolliert; diese Zusatzdiagnose wird nicht als exakter
globaler Spektralbeweis ausgegeben. Weiterhin keine T1–T8-Schließung.

## Fortsetzung: Von einzelnen Blöcken zu beliebig langen Ketten

Die Reparatur ist jetzt allgemein bewiesen: Dieselbe lokale Paarungsregel
funktioniert auf jeder endlichen ungeraden Kettenlänge. Bei einer, drei, fünf,
sieben und neun Stellen ergeben sich 1, 2, 5, 14 und 42 Paarungsrichtungen.
Der zugehörige Teilraum hat bei Viererbausteinen Dimension 4, 8, 20, 56 oder 168.
Die allgemeine Formel ist bewiesen; diese fünf Größen sind nur zusätzliche Tests.

Das ist bekannte Temperley–Lieb-/Paarungsmathematik, hier konkret auf unseren
bedingten Kandidaten angewendet. Es wurde kein neuer universeller Zahlen-Code
entdeckt. Einfache Regeln und ein wachsender Zustandsraum passen zusammen.

### Ein wichtiger Unterschied wurde bisher zu streng behandelt

Eine neue Bell-Paarung einfach anzuhängen ist nicht dasselbe, wie ihre
Wechselwirkung korrekt einzuschalten. Der Unterschied bleibt auch bei längeren
Ketten bestehen. Für den allerersten Schritt gibt es jedoch einen ausdrücklich
konstruierten Aufbauweg: Die neue Kopplung wird allmählich eingeschaltet und
der gewünschte Zustandsraum bleibt dabei durch eine positive Energielücke vom
Rest getrennt. Daraus folgt noch keine autonome Uhr oder beliebig schnelle
beziehungsweise beliebig oft wiederholbare physische Präparation.

Für die Existenz einer unendlichen Dynamik brauchen wir diese starre
Zustands-Anhängeforderung aber gar nicht. Die passendere Frage lautet:

> Ändert sich die Antwort auf eine lokale Messung noch wesentlich, wenn wir
> den Rand immer weiter wegschieben?

Für die festgelegte eindimensionale Bell-Kette konvergieren diese Antworten
nach einem etablierten Satz tatsächlich. Die beschränkten, nächstbenachbarten
Kopplungen erfüllen seine Voraussetzungen. Damit ist eine konsistente
unendliche Dynamik dieses Modells begründet — keine bloße Vermutung aus
endlichen Tests.

Zusätzlich lässt sich die Existenz mindestens eines unendlichen Grundzustands
mit einer unitären Zeitentwicklung und nichtnegativer Anregungsenergie begründen.
Das ist ein Existenzbeweis, noch keine eindeutige Auswahl oder explizite
Berechnung dieses Zustands. Die verwendeten mathematischen Grenzwertsätze
sind etabliert; ihre Anwendung auf das festgelegte Modell ist hier geprüft.

**Das löst eine konkrete Existenzfrage, nicht die Auswahl der Naturgesetze.**
Die Kette, ihre physischen Faktoren und ihre Kopplung sind weiterhin Annahmen.
Die unendliche Kette ist keine hergeleitete 3+1D-Raumzeit. Ihr thermodynamischer
Grenzwert ist auch nicht automatisch ein Kontinuumsgrenzwert.

Die neue Orientierung ist damit genauer: Zuerst die **gemeinsame Algebra
lokaler Operationen mit konsistenter Dynamik**, dann ausgewählte Zustände und
deren geometrische Beschreibungen. Nicht den gesamten Ansatz verwerfen, weil
eine bestimmte kleine Zustandsdarstellung nicht auf jeder Stufe gleich bleibt.

[Allgemeine Kettenkonstruktion, Einschaltweg und unendlicher Grenzwert](../experiments/theory-contracts/systematic-origin-audit-20260912/chain-extension/README.md).

## Fortsetzung: Zurück zu den ursprünglichen Compiler-Regeln

Die neuere Prüfung unterscheidet jetzt genauer zwischen dem, was die
Compiler-Quelle vorgibt, und dem, was wir als Kopplung ergänzt haben.
Dabei lässt sich eine bisher stärkere Voraussetzung tatsächlich weglassen:
Für den eindeutigen Bell-Vergleichszustand brauchen wir nicht die gesamte
zusätzlich angenommene U(4)-Symmetrie. Die vier ursprünglichen Operationen
genügen, **wenn** ein System mit einem konjugierten Partner auf exakte
Übereinstimmung geprüft wird. Der physische Partner und diese
Übereinstimmungsforderung bleiben Voraussetzungen.

### Derselbe Ruhepunkt ist noch nicht dasselbe Bewegungsgesetz

Bildlich gibt es zwei einfache Bewertungsregeln:

- **Bestanden oder nicht bestanden:** Alle Abweichungen kosten gleich viel.
  Das war unsere bisherige flache Bell-Kopplung.
- **Abweichungen zählen:** Jede der vier verletzten Compiler-Vergleichsregeln
  trägt einen eigenen Betrag bei. Das ist die jetzt geprüfte primitive Kopplung.

Beide wählen dasselbe einzelne Bell-Paar aus. Verbinden wir drei Bausteine,
unterscheiden sich ihre Bewegung und ihr Grundzustandsraum jedoch bereits.
Für die primitive Regel haben wir jetzt das vollständige Spektrum und einen
passenden vierdimensionalen Grundzustandsraum exakt konstruiert. Seine
Überlappung mit dem alten beträgt ungefähr 98,99 Prozent — sehr ähnlich,
aber nicht gleich. Das genügt nicht, um die früheren exakten Kettenformeln
ungeprüft zu übernehmen.

Die neue Zusammenfassung erhält außerdem die Richtungen aller sechzehn
Compiler-Wörter. Sie schwächt diese aber unterschiedlich ab. Das ist ein
konkretes, strukturiertes Ergebnis: Die ursprünglichen Operationen sind
weiter erkennbar, ihre vollständige lokale Information bleibt nicht erhalten.
Die Stärke der Kopplungen und sogar ihr Verhältnis sind weiterhin nicht
eindeutig aus der Quelle ausgewählt.

### Ein besonders wichtiger Fallstrick beim Gedanken der „Schatten“

Eine mathematische Matrix kann je nach Darstellung Unterschiedliches bedeuten.
Die Bell-Matrix beschreibt in einer Darstellung den perfekten
Identitätsprozess: Information wird unverändert weitergegeben. Liest man
dieselben Einträge stattdessen als direkte Abbildung auf den Komponenten
eines Zustandsoperators, beschreibt sie vollständige Vermischung: Alle
Eingaben enden im gleichen Zustand. Die Umrechnung zwischen diesen beiden
Darstellungen darf nicht weggelassen werden.

Bildlich: **Ein Bauplan eines Motors ist kein zweiter Motor.** Ebenso ist ein
konjugierter Faktor, der beim Darstellen einer Operation auftritt, noch kein
Nachweis für ein zweites physisches System. Und Informationsverlust beim
Zusammenfassen ist nicht automatisch die fundamentale Zeitentwicklung.

Wir haben diese Unterscheidung mit den wirklichen Compiler-Matrizen geprüft:
Die primitive Rauschregel macht einen reinen Einzelzustand gemischt; eine
unitäre Bewegung des vollständigen angenommenen Paars erhält dagegen seine
Reinheit. Auch die neue räumliche Block-Zusammenfassung ist nicht einfach
ein Zeitschritt dieser Rauschregel.

### Was wir dadurch behalten und als Nächstes entscheiden müssen

Die allgemeinen Existenzsätze für eine unendliche lokale Dynamik gelten
auch für die primitive Kette: Ihre Kopplungen sind ebenfalls beschränkt
und reichen nur zum Nachbarn. Dafür benötigen wir die speziellen alten
Bell-Kettenidentitäten nicht. Weder die Kette noch eine 3+1D-Raumzeit oder
eine eindeutige physische Uhr sind damit aus TFPT abgeleitet.

Der nächste entscheidende Schritt ist deshalb eine **operationale Auswahl**:
Was ist ein physischer Zustand des Compilers, welche Eingriffe sind erlaubt,
und warum soll gerade eine bestimmte Verletzung Energie kosten? Die jetzt
exakt gelöste primitive Dreiergruppe liefert dafür einen konkreten
Vergleichskandidaten. Eine Antwort muss die gewählte Kopplung und ihre
Zusammensetzung festlegen — der richtige gemeinsame Ruhepunkt allein reicht
nicht. Die offenen T1–T8-Probleme bleiben ausdrücklich offen.

[Neue Quellenauswahl, exakte Dreierlösung und Darstellungsprüfung](../experiments/theory-contracts/systematic-origin-audit-20260912/source-selection/README.md).

Ein engerer Einfachheitsansatz ist jetzt ebenfalls präzisiert: Wenn Energie
eine **positive quadratische Vergleichsabweichung** misst und dabei keine
der vier Clifford-Richtungen bevorzugt, folgt genau die primitive Kopplung
mit gleichen Gewichten — bis auf eine gemeinsame Skala. Dafür brauchen wir
nicht die volle zusätzliche U(4)-Symmetrie. Der kleine bedingte Satz ist
bewiesen; seine Voraussetzungen sind noch nicht aus TFPT hergeleitet.
Insbesondere zeichnet TFPT bisher die vierte Richtung als Anker aus. Ob
diese Auszeichnung auch die Vergleichsenergie beeinflussen muss, ist jetzt
eine konkrete Auswahlfrage statt einer unbestimmten Suche nach mehr Komplexität.

## Fortsetzung: Die erste dynamische Korrektur trifft eine vorhandene Compiler-Struktur

Die neue Blockprüfung liefert einen konkreten Zusammenhang zwischen der
primitiven Dynamik und einer größeren Struktur der ursprünglichen Quelle.

Zunächst reproduziert sich die primitive Kopplung beim Zusammenfassen von
zwei Dreierbausteinen tatsächlich: Ihre Form bleibt in erster Ordnung gleich,
ihre Stärke erhält den Faktor 3/8, hinzu kommt eine konstante Energieverschiebung.
Das ist eine echte, genau berechnete Selbstähnlichkeit innerhalb des Modells.

Sie ist aber nicht vollständig. Die Verbindung kann innere Anregungen der
Bausteine erzeugen. Wenn diese Anregungen wieder verschwinden, hinterlassen
sie eine zusätzliche effektive Wechselwirkung. Diese zweite Ordnung haben
wir jetzt unter Einbeziehung aller relevanten Energiebanden exakt berechnet.
Sie lässt sich nicht allein durch eine andere Stärke der alten Regel ersetzen.

### Das Interessante: Die Ergänzung war algebraisch schon vorhanden

Im ursprünglichen Compiler gibt es eine größere Symmetrie, die zehn Operationen
zusammenfasst: die vier primitiven und sechs aus je zwei primitiven
Operationen zusammengesetzte. Bezeichnen wir die entsprechenden Vergleichsenergien
mit H4 und H10, gilt die einfache exakte Beziehung

    H10 = 5 H4 - H4².

Die berechnete dynamische Korrektur lässt sich genau als Beitrag dieser
H10-Struktur schreiben, ergänzt um Änderungen von H4 und des Energienullpunkts.
Der neue H10-Beitrag hat einen positiven, aus dem Modell berechneten Koeffizienten.
Er wurde nicht als passender Zusatz in die Rechnung eingesetzt.

Bildlich: Wir beobachten zunächst vier einzelne Bewegungen. Werden zwei
Bausteine verbunden, wirken auch kurze Kombinationen dieser Bewegungen mit.
Beim genaueren Hinsehen tauchen deshalb sechs zusammengesetzte Bewegungen auf —
und diese gehören bereits zur ursprünglichen Algebra.

**Das ist eine hergeleitete Verbindung im gewählten Modell, keine bloße
Zahlenähnlichkeit.** Noch folgt daraus weder, dass die Natur dieses Modell
wählt, noch dass jede weitere Zusammenfassung zur größeren Symmetrie führt.
Die Rechnung gilt als kontrollierte Entwicklung für schwache Verbindungen;
sie liefert keine vollständige Lösung bei beliebig starker Kopplung.

### Die Einfachheitsfrage ist damit präziser

Eine einzige Kopplungszahl genügt nicht für die genaue effektive Paar-Dynamik.
Die gefundenen Ergänzungen liegen aber in einem kleinen, geordneten Raum von
Compiler-Wechselwirkungen. Für die festgehaltene Blockabbildung reicht ein
fünfdimensionaler Paar-Termraum, um sämtliche gradabhängigen Paarungen
darzustellen und ihre direkte Kompression zu beschreiben. Das ist noch kein
Beweis, dass die gesamte Kette oder eine selbstkonsistente Wiederholung in
diesem kleinen Raum bleibt.

Auch die Quellenfrage ist jetzt sauber beantwortet: Die geprüften markierten
Compilerregeln erzwingen nicht, dass Familienrichtungen und Anker gleich viel
Energie kosten. Zwei verschiedene Gewichtungen erfüllen dieselben geprüften
Quellenbedingungen. Größere Symmetrien existieren bereits; offen ist, welche
von ihnen die physische Energie tatsächlich erhalten müssen.

Die nächste entscheidende Prüfung ist, was bei gemeinsam genutzten Verbindungen
mehrerer Blöcke entsteht, und ob eine kleine Wechselwirkungsfamilie diese
Beiträge konsistent erfasst. Parallel bleibt die ursprüngliche physische
Auswahl der Energie und Zeit zu begründen. Kein T1–T8-Problem wurde hier als
vollständig geschlossen eingestuft.

[Exakte erste und zweite Ordnung, ursprüngliche Symmetrien und Prüfprotokolle](../experiments/theory-contracts/systematic-origin-audit-20260912/primitive-renormalization/README.md).

Den ersten Fall gemeinsam genutzter Verbindungen haben wir anschließend
ebenfalls berechnet: Bei drei Blöcken vermittelt der mittlere eine zusätzliche
Kopplung zwischen den beiden äußeren. Ihr Koeffizient in der zweiten Ordnung
ist exakt 9√6/512, multipliziert mit den beiden schwachen Verbindungsstärken.
Die elementaren Operatoren bleiben dabei dieselben; die effektive Reichweite
wird größer. Das ist in der gewählten effektiven Darstellung ein vermittelter
Paarterm, kein neuer Drei-Körper-Term auf dieser Stufe.

Bildlich: A und C sind nur über B verbunden. Betrachtet man B nicht mehr
in allen Einzelheiten, erscheint ein berechenbarer direkter Einfluss von A
auf C. Deshalb genügt es nicht, beim Iterieren nur die Stärke derselben
Nachbarverbindung anzupassen. Die weiterführende Aufgabe ist jetzt eine
kontrollierte Beschreibung dieser zusätzlichen Reichweiten und Operatoren,
nicht mehr die bloße Vermutung, dass sie entstehen könnten.

## Fortsetzung: Ein einziger Mischungswinkel — und die tatsächliche Skalengrenze

Die neuen Wechselwirkungen verlangen lokal keinen unübersichtlichen Baukasten.
Im untersuchten Dreierblock lässt sich ihre gemeinsame Wirkung auf eine exakte
Zwei-mal-zwei-Matrix zurückführen. Jede ihrer beiden Koordinaten trägt denselben
vierdimensionalen logischen Baustein. Die Anpassung des bisherigen Grundzustands
ist damit durch **einen einzigen Mischungswinkel** vollständig beschrieben.
Das ist eine Aussage über diese Wechselwirkungsfamilie, nicht über alle
denkbaren Erweiterungen oder bereits über den fundamentalen Baustein der Natur.

Bildlich: Wir müssen das Instrument nicht neu bauen. Die hinzugekommenen
Kopplungen drehen seine innere Einstellung. Diese Drehung können wir exakt
berechnen, ebenso die Wirkung auf alle sechzehn ursprünglichen Compiler-Wörter.
Nahe dem Ausgangspunkt ist auch bewiesen, dass der angepasste Zustand wirklich
der tiefste Zustand des ganzen Blocks bleibt, nicht nur einer ausgewählten Ecke.

Dabei reagieren nicht alle beobachtbaren Größen gleich: Die vier primitiven
Richtungen ändern ihre Übertragung erst quadratisch mit dem kleinen Winkel.
Zusammengesetzte Richtungen ändern sie bereits linear. Eine innere Veränderung
kann also für manche Messungen zunächst unsichtbar sein, während andere sie
sofort erkennen. Das liefert einen konkreten, berechenbaren Sinn von
unterschiedlichen „Schatten“ desselben Zustands — ohne daraus eine universelle
Rekonstruktion zu behaupten.

### Von wenigen Blöcken zu beliebig langen endlichen Ketten

Für die erste Zusammenfassung ist die zweite Ordnung jetzt vollständig:
Zwei Eingriffe auf derselben Verbindung ergeben die Paar-Korrektur; zwei
benachbarte Verbindungen ergeben die Vermittlung über den mittleren Block.
Zwei getrennte Verbindungen können ihre jeweiligen inneren Anregungen nicht
gegenseitig wieder beseitigen und tragen auf dieser Stufe nichts bei.
Damit sind alle Fälle erfasst, unabhängig von der Zahl der Blöcke.

Ein etablierter Satz zur lokalen Vielteilchen-Störungstheorie liefert außerdem
eine Grundenergie-Fehlergrenze von der Form c N |epsilon|³. Hier zählt N die
Blöcke; c und die erlaubte hinreichend kleine Kopplungsstärke hängen nicht von
N ab. Der Fehler **pro Block** wird damit nicht allein durch eine längere Kette
schlechter. Die Voraussetzungen sind für unser ausdrücklich gewähltes Modell
nachgeprüft; konkrete Zahlen für die Schranke wurden noch nicht gewonnen.
Das ist eine analytische Anwendung des
[Satzes von Bravyi, DiVincenzo und Loss](https://arxiv.org/pdf/1105.0675),
kein Ergebnis eines Tests an nur wenigen Kettenlängen. Eine entsprechende
Kontrolle aller Zustände oder der Zeitentwicklung folgt daraus nicht.

### Warum die nächste Zusammenfassung trotzdem noch offen ist

Die erste Rechnung nutzt starke Verbindungen innerhalb eines Dreierblocks
und schwache Verbindungen zwischen den Blöcken. Danach sind die verbleibenden
Nachbarverbindungen alle von derselben Größenordnung. Fasst man erneut drei
zusammen, sind ihre Außenverbindungen nicht mehr automatisch schwächer als
ihre Innenverbindungen. Eine Änderung des Energiemaßstabs behebt das nicht.

Außerdem wird der bisherige Fehler dritter Ordnung nach der Normierung zu
einem Fehler zweiter Ordnung. Er konkurriert damit genau mit den nächsten
Korrekturen, die wir bestimmen möchten. Die exakte lokale Drehung allein
rechtfertigt deshalb keine beliebig oft wiederholte Näherung.

Der nächste tragfähige Schritt muss entweder eine weitere Größenhierarchie
aus der Quelle begründen oder die gleich stark gekoppelte Kette ohne diese
Schwachkopplungsannahme behandeln. Hinzukommen müssen eine Kontrolle der
beobachtbaren Größen und der über mehrere Schritte angesammelten Fehler.

### Die Zeitfrage ist von einer falschen Gleichsetzung befreit

Der ursprüngliche Anker ist im konstruierten Lorentz-Rahmen ein
Chiralitätsoperator, nicht die Zeitrichtung. Ein positiver Vergleich lässt
sich dennoch einfach formulieren, wenn eine mittransformierende zeitartige
Beobachterrichtung n gegeben ist: Q_n(x)=2(n·x)²−x·x. Im Ruhesystem dieses
Beobachters ist das die gewöhnliche positive quadratische Länge.
Noch nicht hergeleitet sind der physische Beobachter aus dem Compiler und
die Identifikation seiner Operationen mit Raumzeit und Zeitentwicklung.

Die drei neuen Prüfer bestehen zusammen 207 exakte Prüfaussagen je Durchlauf,
normal und unter Python-Optimierung mit identischem Ergebnis. Die vorherigen
448 Prüfaussagen je Durchlauf wurden ebenfalls erfolgreich wiederholt.
Diese Tests sichern die endlichen algebraischen Ergebnisse; sie ersetzen
nicht den analytischen Vielteilchensatz oder die physische Quellenableitung.
T1–T8 bleiben offen.

[Exakte Anpassung, Fehlerkontrolle, Zeitprüfung und reproduzierbare Protokolle](../experiments/theory-contracts/systematic-origin-audit-20260912/self-consistent-blocks/README.md).

## Fortsetzung: Die Gruppierung darf nicht mit der Quelle verwechselt werden

Die Untersuchung der gleich stark gekoppelten Kette liefert einen entscheidenden
Richtungsbefund: Unsere bisherige feste Dreier-Einbettung kann deren Grundzustand
nicht exakt beschreiben. Das ist jetzt eine bewiesene Schranke und nicht nur
das Scheitern einer Näherungsmethode.

Für periodische Ketten mit 12, 18, 24, ... Registern liegt die Energie pro
Register **jedes** Zustands in dieser Dreier-Einbettung mindestens bei

    (96−19√6)/48 ≈ 1,03041031.

Dabei dürfen die übrig gebliebenen logischen Register beliebig miteinander
verschränkt sein. Trotzdem erzielt bereits ein einfacher Zustand aus
abwechselnden Bell-Paaren die Energie pro Register 1. Der wahre Grundzustand
kann nicht höher liegen als dieser Vergleichszustand. Die feste Einbettung
verfehlt ihn deshalb um mindestens 0,03041031 Energieeinheiten pro Register.
Die Einheiten und die Aussage beziehen sich ausschließlich auf den festgelegten
primitiven Hamiltonoperator, nicht auf gemessene physikalische Energien.

Bildlich: Wir hatten versucht, das gesamte System in Dreierpakete zu verpacken.
Jetzt können wir zeigen, dass diese konkrete Verpackung selbst bei optimaler
Verbindung der Pakete unnötige Energie festhält. Schon eine einfache
Paar-Verpackung ist günstiger. Die schwach gekoppelten Dreier-Rechnungen waren
dadurch nicht falsch; ihre unveränderte Übertragung auf gleich starke
Verbindungen wäre falsch.

### Der vierdimensionale Baustein war kein Beweis für eine Dreierwelt

Auch das wiederkehrende vierdimensionale logische Objekt ist besser verstanden.
Die untersuchten elementaren Bindungsoperatoren besitzen auf jeder ungeraden
offenen Kette eine gemeinsame vierdimensionale Matrix-Symmetrie. Deshalb
erscheinen Energien mindestens in Vierer-Vielfachen — nicht nur bei drei
Registern, sondern auch bei fünf, sieben und so weiter.

Das ist ein exakter Zusammenhang für alle diese Längen. Es bedeutet aber nicht,
dass nur vier Zustände übrig bleiben oder die ganze Kette einfach gelöst wäre.
Der restliche Zustandsraum wächst weiterhin exponentiell. Die Wiederkehr der
Vier ist somit zunächst eine globale algebraische Symmetrie, keine bereits
hergeleitete Raumzeitdimension und kein Nachweis eines Größenordnungs-Fixpunkts.

### Ein bekanntes Modell gibt uns eine konkrete Vergleichsbasis

Nach einer exakt geprüften lokalen Basisänderung ist unsere uniforme Kette
ein Spezialfall eines Gamma-Matrix-Spinmodells. Die zugehörige Arbeit findet
numerische Hinweise auf Paarordnung; ihre exakt gelösten Paar-Grundzustände
betreffen jedoch ein abgeändertes Modell mit einer zusätzlichen Kopplung.
[Primärarbeit von Siew, Chandrasekharan und Kaul](https://arxiv.org/pdf/2406.04120).

Unsere unabhängige Quellenrechnung zeigt außerdem eine einfache Beschreibung
mit zwei erhaltenen Besetzungsarten. Deren Bewegungen beeinflussen sich
gegenseitig. Ein geschlossener Ablauf aus vier Bewegungen trägt ein negatives
Vorzeichen, das durch bloßes Umphasen nicht verschwindet. Das System besteht
also nicht einfach aus zwei unabhängigen freien Ketten. Sogar sein exaktes
Dreier-Spektrum widerspricht einer vollständigen Beschreibung durch
unbeschränkte freie Fermionen; eingeschränkte Teilsektoren bleiben möglich.

### Was eine alternative Beschreibung jetzt leisten muss

Wir haben einen exakt gelösten Paar-Vergleichsoperator unmittelbar aus den
Quellmatrizen rekonstruiert. Er dient als Prüfstein, nicht als Austausch unseres
eigentlichen Problems. Insbesondere stört der zuvor erzeugte H10-Beitrag seinen
einfachen Paar-Produktzustand auf eine Weise, die durch bloße Änderung zweier
anderer Kopplungsstärken nicht beseitigt werden kann.

Die nächste Beschreibung muss deshalb Paar-Korrelationen **und ihre
Veränderungen** enthalten. Sie soll den einfachen Vergleichszustand energetisch
verbessern und darf die erzeugten Wechselwirkungen nicht unterschlagen.
Eine bessere Näherung wäre ein weiterer Schritt, noch keine vollständige
Grundzustands- oder Kontinuumslösung.

Parallel bleibt die Quellenfrage präzise offen: Dieselben lokalen Compiler-
Symmetrien erlauben nachweislich unterschiedliche Graphen und unterschiedliche
Bindungsstärken. Ein interner Dreierzyklus bestimmt nicht automatisch eine
räumliche Dreiergruppierung. Die Quelle muss die physische Verknüpfung und
Zeitentwicklung zusätzlich begründen, statt sie aus einer praktischen
Rechenaufteilung zu übernehmen. Kein T1–T8-Problem ist damit geschlossen.

[Beweise, bekannte Modellidentifikation, Gegenprüfungen und Forschungsaufträge](../experiments/theory-contracts/systematic-origin-audit-20260912/uniform-chain/README.md).

### Bereits umgesetzt: Paare verbinden, ohne das Energiegesetz zu ändern

Die alternative Beschreibung ist inzwischen mehr als ein Vorschlag. Wir
beginnen mit den einfachen Bell-Paaren und verändern die Verbindungen zwischen
ihnen durch einen lokalen Filter F(t)=I−t h4. Dafür genügt ein einziger
veränderlicher Parameter. Der untersuchte Hamiltonoperator bleibt unverändert;
wir suchen lediglich einen günstigeren Zustand für ihn.

Die Kosten und Gewinne dieser Veränderung sind gemeinsam exakt berechnet.
Die vormals perfekten Paarbindungen werden etwas schlechter, dafür sinkt die
Energie zwischen den Paaren stärker. Für die einfache Wahl t=1/8 beträgt die
Energiedichte im Grenzwert einer langen Kette

    e = 5023/5476 ≈ 0,9172754,

statt 1 beim unveränderten Paar-Produktzustand. Es wurden weder Naturkonstanten
angepasst noch zusätzliche physische Kopplungen eingeführt. t ist hier ein
Variationsparameter zur Prüfung eines Zustands, keine hergeleitete Naturzahl
und keine physisch identifizierte Zeit.

Bildlich: Wir kleben die Paare nicht starr zusammen. Wir lassen jedes Paar
auf seine Nachbarn reagieren. Schon diese eine einfache Anpassung ist besser
als völlig unabhängige Paare und als die zuvor untersuchte feste
Dreierbeschreibung. Das erfordert keinen wachsenden lokalen Rechenapparat:
Die Beschreibung arbeitet mit vierdimensionalen Verbindungsindizes und einer
vollständig berechneten kleinen Transferabbildung.

Für den wahren Grundenergie-Grenzwert des festgelegten Modells haben wir damit
die gesicherte Einordnung

    (4−√6)/2 ≤ e_Grund ≤ 5023/5476,

also ungefähr 0,775255 ≤ e_Grund ≤ 0,917275. Die obere Grenze stammt von unserem
konkret konstruierten Zustand, die untere von einer Operator-Ungleichung.
Der Abstand zwischen beiden ist weiterhin offen. Eine gute obere Schranke
ist ausdrücklich keine vollständige Grundzustandslösung.

Auch der Grenzübergang des Kandidaten ist kontrolliert: Seine Transferabbildung
hat einen eindeutig dominierenden Eigenwert. Die Formel ist deshalb ein exakt
berechneter Grenzwert und keine Extrapolation weniger Kettenlängen. Endliche
Ringe besitzen zusätzliche Korrekturterme; und die endlichen Korrelationen
dieses Kandidaten beweisen noch keine Energielücke des Hamiltonoperators.

Der nächste quantitative Test lautet jetzt nicht mehr bloß „besser als 1“,
sondern: obere und untere Grenze weiter zusammenführen, die Stabilität der
Korrelationen prüfen und dabei mögliche Rand- oder Gruppierungsartefakte
ausschließen. Die davon getrennte Herleitung von physischer Geometrie und
Zeit aus dem Compiler bleibt erforderlich.

[Exakte Ein-Parameter-Konstruktion und Grenzübergang](../experiments/theory-contracts/systematic-origin-audit-20260912/uniform-chain/dimer_filter.md).

## Fortsetzung: Die unbekannte Grundenergie wird von beiden Seiten eingegrenzt

Das bisherige Intervall ist jetzt durch zwei unabhängige Rechnungen enger
geworden. Für dieselbe gleichförmige primitive Kette gilt nun

    3249/4000 ≤ e_Grund ≤ 254850665/279993289,

also ungefähr

    0,81225 ≤ e_Grund ≤ 0,910202762.

Die obere Grenze wurde durch einen besseren Zustand gesenkt. Die untere
Grenze wurde unabhängig davon für **alle** Zustände bewiesen. Sie darf nicht
mit der Energie eines besonders günstigen Kandidaten verwechselt werden.

### Die bessere Beschreibung bleibt klein

Zunächst genügte eine quadratische Ergänzung des Filters, um die obere
Schranke auf ungefähr 0,911672 zu senken. Die vollständige lokale Erweiterung
ist ebenfalls übersichtlich: Der Paar-Operator besitzt nur fünf verschiedene
Energien. Ein Filter, der ausschließlich von diesem Operator abhängt, wird
deshalb durch fünf reelle Gewichte beschrieben. Ein gemeinsamer Faktor spielt
nach der Normierung keine Rolle.

Für diese gesamte Filterfamilie konnten Norm, Bindungsenergien und die
Übertragung der Korrelationen exakt aus den ursprünglichen Quellmatrizen
bestimmt werden. Die vierdimensionale interne Verbindung der Zustandsbeschreibung
wächst dabei nicht. Der neue Zahlenwert ist ein exakt ausgewerteter rationaler
Prüfpunkt dieser Familie — keine behauptete globale Optimallösung, und seine
gewählten Gewichte sind keine hergeleiteten Naturkonstanten.

### Die untere Grenze ist kein numerisch geschätztes Minimum

Ein Fünferabschnitt lässt sich durch zwei erhaltene Besetzungszahlen in 36
Sektoren zerlegen. Zusammen enthalten sie sämtliche 1024 Zustandsdimensionen.
Wir haben keinen vermeintlich richtigen Grundzustandssektor vorausgewählt.

Für jede dieser Matrizen wurde mit exakter ganzzahliger Rechnung bewiesen,
dass ihre Energie größer als 3249/1000 ist. Summiert man dieselbe Aussage
über alle überlappenden Fünferabschnitte einer langen Kette, wird jede Bindung
viermal gezählt. Daraus folgt die untere Energiedichte 3249/4000.

Eine absichtlich knapp zu hohe Vergleichsgrenze, 13/4 für den Fünferabschnitt,
wird von demselben Verfahren zurückgewiesen. Das liefert zugleich eine
wichtige Arbeitsgrenze: Mit der identischen ungewichteten Fünferfenster-Methode
können wir die untere Schranke niemals bis 13/16=0,8125 erhöhen. Diese Zahl
ist **keine obere Schranke der wahren Grundenergie**, sondern die Grenze
dieser speziellen Methode. Weitere Dezimalstellen dort lösen das Problem nicht.

### Symmetrisch aussehen ist nicht dasselbe wie ungeordnet sein

Die unabhängige Zustandsprüfung trennt zwei Arten von Symmetrie. Der zuvor
konstruierte lineare Filterzustand erhält die internen Compiler-Symmetrien
einschließlich der kompakten Spin(4)-Symmetrie. Seine Bindungen wechseln aber
zwischen zwei verschiedenen Erwartungen. Jeder einzelne Registerzustand
sieht bereits vollkommen gleich aus; die Ordnung steckt in den Verbindungen.

Mitteln wir diesen Zustand mit seiner um einen Platz verschobenen Variante,
werden auch die mittleren Bindungsenergien gleich. Die langfristigen
Korrelationen verraten die Paaranordnung trotzdem weiterhin.

Bildlich: Zwei gegeneinander verschobene Streifenmuster ergeben im Mittel
eine gleichmäßig graue Fläche. Daraus folgt nicht, dass die zugrunde liegenden
Streifen verschwunden sind. Gemeinsame Messungen an verschiedenen Stellen
können ihre Anordnung noch erkennen.

Ein eigens auf den Kandidaten zugeschnittener Hamiltonoperator würde diesen
Zustand möglicherweise exakt bevorzugen. Das wäre jedoch ein anderer
Operator und würde den Grundzustand unseres vorgegebenen Modells nicht lösen.
Auch die schnelle Abnahme von Korrelationen eines Kandidaten beweist noch
keine Spektrallücke des ursprünglichen Hamiltonoperators.

Die nächsten entscheidenden Arbeiten sind deshalb größere oder besser
miteinander verträglich gemachte lokale Abschnitte für die untere Grenze,
zusätzliche Zustands- und Korrelationsprüfungen für die obere sowie weiterhin
die getrennte Herleitung von physischem Graphen, Kopplungen und Zeit aus
dem Compiler. T1–T8 bleiben offen; der eingegrenzte Teil betrifft das
explizit gewählte eindimensionale Modell.

[Neue Energieschranken, vollständige Filterfamilie und Symmetrieprüfung](../experiments/theory-contracts/systematic-origin-audit-20260912/energy-bracket/README.md).
