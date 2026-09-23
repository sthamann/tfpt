# Gemeinsamer Quellenanschluss: Reproduzierbarkeit

Einstieg: [deutsche Gesamtauswertung](ERGEBNIS.md).

Forschungsverdict **PARTIAL**. Exakte bedingte Algebra und begrenzte
Operatorreduktionen; keine vollständige physikalische Lösung und keine
Schließung von T1–T8.

Die Reproduktion erfolgt mit `python3 -B checker.py` in diesem Verzeichnis.
Benötigt werden Python, NumPy, SymPy, Git und die in `source_manifest.json`
gepinnten lokalen Originaldateien. Der Checker prüft diese vor und nach der
Rechnung und führt die fünf begrenzten Prüfungen normal sowie mit `-OO` aus.
Die Ergebniszertifikate beider Modi müssen bytegleich sein. Veränderte Quellen
werden abgewiesen; es gibt keine automatische Aktualisierung der Pins.

`joint/` enthält die gemeinsame Sektion, den Stabilisatorsatz und den
analytischen Spektralreduktionsbeweis. `flavor/`, `transfer/` und
`phase_operator/` enthalten Originalauswertungen der beauftragten Arbeiter
und ihre ausführbaren Prüfungen. Der mathematische Beweis einer allgemeinen
Aussage steht in den Proof-Dateien; endliche Checker ersetzen keinen
formalen Beweisassistenten und beweisen nicht die physikalischen Prämissen.

Das Paket ist ein lokaler Forschungsstand. Einige Eingangspfade sind absolut
auf den gemeinsam verwendeten TFPT-Checkout und vorige Ergebnispakete bezogen.
Die Daten dieser Quellen werden nicht durch dieses Paket veröffentlicht.
Das vollständige Paketmanifest prüft die gelieferten Dateiinhalte; es ist
von dem Manifest der unabhängigen Eingangsdaten getrennt.

Die Dateien der drei Arbeiter sind datierte Arbeitsnachweise. Ihr Hinweis
auf einen damals veralteten Graphen beschreibt den Recherchezeitpunkt;
den späteren Register- und Graphstatus hält `registration.json` fest.
