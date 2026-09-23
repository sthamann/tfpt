# Drei Wege zum gemeinsamen TFPT-Motor

9. September 2026. Forschungsversuche am gepinnten Stand
`66b91e40e245569f06ab440ead80f446c9be0ee5`.

**Alle drei Ansätze wurden bearbeitet. Ein gemeinsamer TFPT-selektierter
Motor ist noch nicht konstruiert; T1–T8 bleiben offen.** Die Ergebnisse
sind absichtlich nicht als geschlossene TOE oder als neue experimentelle
Vorhersagen ausgewiesen.

## Das wichtigste Ergebnis in einfachen Worten

Wir können jetzt im vorhandenen Rotor-Testmodell zeigen und ausrechnen,
wie Bewegung und Rückwirkung zusammenhängen: Eine zweite Ladungsverteilung
ändert die Energiekosten desselben Transports, obwohl sein ursprünglicher
Kopplungskoeffizient unverändert bleibt. Dafür wurde kein neuer
Vierfermion-Term eingesetzt.

Bei E₈ ist das Ziel ebenfalls konkreter geworden: Ein passender
Halb-Twist-Bauplan benötigt sechzehn **gleichgerichtete chirale Felder**,
nicht lediglich sechzehn endliche Majorana-Variablen. Die Zielgeometrie
und der nötige Ladungsübertrag stimmen algebraisch zusammen. Die Felder
und ihr gemeinsamer physikalischer Ursprung müssen aber noch entstehen.

Der Belastungstest zeigt außerdem, was eine gemeinsame Dynamik zusätzlich
leisten muss: Die tatsächlichen Zieloperationen J und sigma erlauben
in einer diagonalen Energieklasse noch zwei verschiedene
Geschwindigkeiten — sechs Richtungen gegen zwei. Die volle gleiche
Energie der E₈-Wurzelanregungen verlangt innerhalb dieser Klasse, dass
diese beiden Geschwindigkeiten gleich sind. Das ist ein konkretes
zusätzliches Ableitungsziel, kein Beweis, dass ansonsten nur eine einzige
TOE-Aufgabe übrig wäre.

**Eine Verbindung zwischen den Aufgaben:** In genau diesem Ansatz hat der
Halb-Twist die Energie `(3a+b)/4`, eine ganzzahlige Wurzel der ersten sechs
Richtungen die Energie `a`. Wenn beide aus der Quelle als gleichenergetische
Teile desselben Strommultiplets hervorgehen, folgt bereits `a=b`. Der
fehlende Halb-Twist könnte also zugleich diese relative Skala binden.
Die Gleichenergetik ist hier eine klar benannte Bedingung, noch kein
bewiesenes Ergebnis der mikroskopischen Dynamik.

## 1. Vorwärts: eine tatsächlich entwickelte kleine Zelle

Verwendet wird das unveränderte [Round37-Modell](../local-window-round37/checker.py):
vier Ecken eines offenen Quadrats, acht komplexe Low/High-Fermionmoden,
vier kompakte U(1)-Rotoren, alle 32 Hoppingterme einschließlich Zwei-Link-
Pfaden. Die sechsfachen Umgebungsbeiträge der ursprünglichen Onsite-Energie
bleiben erhalten. Ein magnetischer Term wird nicht ergänzt.

Das Gauss-Gesetz wird vor der numerischen Entwicklung exakt gelöst. Die
elektrische Energie zerfällt dann in einen ladungsabhängigen Anteil und
einen umlaufenden Fluss. Dessen ganzzahliger Parameter darf nicht durch
eine frei minimierbare reelle Zahl ersetzt werden.

**Konkreter Rückwirkungszeuge:** Für den ursprünglichen Low-Transport
von Ecke 0 nach Ecke 1 bleibt die Amplitude `1/12`. Eine zweite,
disjunkte Ladungsverteilung an den Ecken 2 und 3 ändert jedoch seine
diagonalen Energiekosten von `+1/200` auf `−1/200`. Beide verglichenen
Zustände erfüllen Gauss und erlauben denselben Transport. Dies ist eine
exakte Rechnung innerhalb des deklarierten Parents, keine Vorhersage
einer gemessenen Teilchenkopplung.

Für eine weitere feste neutrale Anfangspräparation wurde die ganze
Zustandsentwicklung zu den Modellzeiten 1, 2 und 4 ausgeführt. Beim
Fluss-Cutoff 10 hat der physikalische Raum 1.412 Zustände. An Ecke 1 wächst
die Low-Besetzung von 0 auf `0.198532077539` bei Zeit 4. Norm, Gesamtzahl
und Energie bleiben erhalten; die Zeitumkehr rekonstruiert den Anfang.

Grenze: Dies ist ein kleiner Ausschnitt eines bereits **gewählten**
Rotor-Parents, keine Herleitung dieses Parents aus den TFPT-Axiomen und
keine Identifikation mit dem Compiler-Clock. Zwei High-Besetzungen sind
eine deklarierte Testpräparation, nicht der selektierte kosmologische Zustand.

## 2. Rückwärts: E₈ legt präzisere Eingangsbedingungen fest

Aus dem tatsächlichen Zielgitter wird die Zerlegung
`D8 ∪ (D8+s)`, `s=(1/2,...,1/2)`, rekonstruiert. Die 112 ganzzahligen und
128 halbzahligen Wurzeln ergeben mit acht Cartan-Richtungen die 248
Zielströme. Jeder rekonstruierte Wurzelvektor wird gegen die originale
Gitterbasis und die bereits vorhandene Wurzelliste geprüft.

Die Halbsektor-Komposition behält ihren **ganzzahligen Übertrag**:
zweimal s ist nicht null. Zusätzlich wird ein Operator-Bauplan mit
`S²=pi(u)` und korrekter verdrehter Kovarianz geprüft. Ein bloßer Zwei-
Zustands-Flip fällt als Negativkontrolle durch. Die endliche Matrixprüfung
ist ausdrücklich kein Aufbau eines chiralen E₈-Netzes.

Die externe Anschlussstelle ist Abschnitt 7.3 von
[Jones–Sopenko–Thorngren, Version 1](https://arxiv.org/html/2608.26456v1#S7.SS3):
Sechzehn chirale Majorana-Felder, Parität und glatte Halb-Twists liefern
dort einen E₈-Netz-Bauplan. Abschnitt 4.1 verbindet geeignete invertierbare
lokale Algebren mit QCA-Klassen nach Erweiterung um Hilfsfreiheitsgrade.
Das Ergebnis liefert weder unseren Quelloperator noch eine eindeutig
ausgewählte physikalische Zeitentwicklung. Lokale Räume sind dort
unendlichdimensional; das E₈-Beispiel führt zu einem zweidimensionalen
räumlichen QCA, nicht zu unserer benötigten 3+1D-Theorie. Ausgewählte
Abschnitte wurden gelesen, kein vollständiger unabhängiger Beweischeck
ausgeführt.

## 3. Robustheit: numerisch stabil, dynamische E₈-Gleichheit nicht automatisch

| Prüfung | Ergebnis | Aussagegrenze |
| --- | --- | --- |
| Fluss-Cutoffs 2, 3, 4, 6, 8, 10 | Die letzten Zustandsvergleiche stimmen bis zur numerischen Genauigkeit überein. | Keine räumliche Verfeinerung oder Kontinuumskonstruktion. |
| Unabhängige Matrixdiagonalisierung gegen Exponentialentwicklung | Zustandsdifferenz `2.16e-14` im kleinen Vergleich. | Kein Intervallbeweis aller Rundungsfehler. |
| Elektrische Dynamik aus, bei sonst gleichem Modell und Anfangszustand | Low-Besetzung bei Zeit 4 ändert sich um bis zu `6.74e-6`. | Ein gezielter numerischer Rückwirkungszeuge, nicht allein ein Beweis einer verbundenen Streuamplitude. |
| Elektrischer Koeffizient und High-Energie jeweils ±10 Prozent | Bewegung bleibt vorhanden; die getesteten Low-Besetzungen ändern sich nur wenig. | Endlicher Sensitivitätstest, kein Universalitätssatz. |
| Diagonale Geschwindigkeiten bei unverändertem E₈-Gitter | Ungleiche Geschwindigkeiten spalten die Zielenergien. | Die Gitteralgebra selbst bleibt bestehen. |
| Dieselbe Prüfung unter den tatsächlichen J-/sigma-Symmetrien | `diag(a,a,a,a,a,a,b,b)` bleibt zulässig. | Gleiche E₈-Energien brauchen innerhalb dieses Ansatzes zusätzlich `a=b`. |

Die übernommene analytische Fluss-Fehlerschranke beträgt bei Cutoff 10 und
Zeit 4 `4.57e-9` für normbeschränkte Readouts. Zwei solche Schranken sind
mehr als hundertmal kleiner als die gemessene Änderung beim Ausschalten
der elektrischen Dynamik. Die numerische Rundung wird separat durch
Gegenrechnungen geprüft, nicht als rigoros eingeschlossen bezeichnet.

## Die drei Wege müssen sich noch treffen

Das Quadrat liefert keine bereits identifizierte E₈-Randalgebra. Die
E₈-Rückwärtskonstruktion liefert keinen bereits identifizierten Rotor-
Hamiltonian. Stabile kleine Rechnungen machen diese beiden Objekte nicht
automatisch zu demselben System.

Der nächste gemeinsame Versuch sollte deshalb **einen quellenbegründeten
Halb-Twist samt Energie- und Adjungiertenkontrolle** mit dem dynamischen
Transport verbinden und dabei die tatsächliche Clock-Markierung erhalten.
Parallel dazu ist die Geschwindigkeitsgleichheit aus der vollen
Quelloperatoralgebra zu prüfen. Sie nur in die Energie einzusetzen wäre
eine weitere Annahme. Im bereits bearbeiteten diagonalen Zielansatz ist
die verbleibende relative Skala jetzt ausdrücklich sichtbar.

## Dateien und Reproduktion

- [PROOF.md](PROOF.md): exakte Ableitungen und Geltungsbereiche.
- [validation.json](validation.json): kompletter normaler Lauf aller drei Wege.
- [validation_optimized.json](validation_optimized.json): Wiederholung mit `-OO`.
- [test_engine.py](test_engine.py): unabhängige Kontrollen und absichtliche Fehlvarianten.
- [TEST_RESULTS.md](TEST_RESULTS.md): tatsächlich ausgeführte Prüfungen.

Aus dem Repo-Root:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/common-engine-threeway/run.py --output /tmp/tfpt-threeway.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/common-engine-threeway -p test_engine.py -v
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/common-engine-threeway -p test_engine.py -v
```

Vorhandene Quellen, fremde Änderungen, Paper, Webseite und globale
Statusmarker wurden in diesem Versuch nicht verändert. Kein Commit/Push
gehört zu dieser Forschungsrunde.
