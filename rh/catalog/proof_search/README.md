# Quellengebundener Lean- und RH-Suchplaner

Der Planer verwendet einen kleinen, expliziten AND/OR-Regelsatz und eine
begrenzte Konstruktionsgrammatik. Er ist **kein vollständiger automatischer
Theorembeweiser**, kein genetischer Operatorerfinder und kein RH-Beweis.
Sein Nutzen: bereits bewiesene Bausteine wiederverwenden und fehlende
Voraussetzungen sichtbar halten, bevor kostspielige Suchen beginnen.

## Arbeitsablauf

Aus `rh/catalog`, mit dem vorhandenen Python:

```sh
python3 -B search_rh.py audit
python3 -B search_rh.py controls
python3 -B search_rh.py index
python3 -B sync_research.py --refresh
python3 -B sync_research.py --check
python3 -B search_rh.py search selectedArchError
```

`audit` baut ausschließlich die transitive Projektabhängigkeit der
registrierten Regeln außerhalb des Repositories neu. Originale Lean-Dateien
und deren Build-Objekte bleiben unangetastet. Lean 4.29.1 und der installierte
Mathlib-Cache werden benutzt; keine Downloads oder API-Aufrufe. Module laufen
einzeln mit 8 GiB Lean-Speichergrenze, Zeitgrenzen je Modul und Gesamtlauf.
Ein fehlgeschlagener Lauf stellt keinen neuen Prüfnachweis aus.

`controls` versucht den echten nativen Positivitätsschritt einmal ohne FREQ
(muss an genau der fehlenden Voraussetzung scheitern) und einmal mit
eingesetzten Forschungsaxiomen (kompiliert, muss aber am Axiomenfilter
scheitern). Diese beiden adversariellen Lean-Fälle sind getrennt von den
Python-Regressionen und werden nach einer Änderung des Beweisnachweises
erneut verlangt. Die Reproduktion nutzt die isolierten frischen Build-Objekte;
sind diese temporären Objekte entfernt, muss zuerst `audit` erneut laufen.

Reine Änderungen an Beschreibungen können nach expliziter Prüfung mit
`search_rh.py review-metadata` übernommen werden. Das ist nur möglich, wenn
der vollständige erzeugte Lean-Eingabetext bytegenau gleich bleibt und alle
übrigen Quellen, Typen und Axiomenprotokolle unverändert sind. Dies spart
eine identische Neuübersetzung; es behauptet keinen neuen Beweis. Änderungen
an Typen, Regeln oder Beweiscode verlangen weiterhin `audit`.

`index` erfasst alle eigenen Lean-Quellen in `rh/lean`, im Carrier-Projekt und
unter `Documents/Codex`, ohne Abhängigkeiten oder Caches. Historische Kopien
werden anhand ihres Inhalts zusammengefasst, aber nicht gelöscht. Die
Datei-/Deklarationssuche ist eine lexikalische Navigation, **keine vollständige
Lean-Syntaxanalyse oder Axiomenprüfung aller Dateien**. Öffentlich sichtbare
Deklarationen aus den frisch importierten Modulen haben zusätzlich exakte
Lean-Typen in `generated/kernel_declarations.json`. Private Deklarationen
werden dort nicht exportiert; Compiler-Hilfsdeklarationen können enthalten sein.

`sync_research --refresh` aktualisiert Entwürfe, Katalog, Graph und Suchplan
gemeinsam. Neue Quellen bleiben ungeprüfte Entwürfe. Ein geänderter
Beweislieferant oder Adapter wird nicht automatisch erneut freigegeben:
dafür muss `audit` explizit bestehen. Die Werkzeuge starten selbst keinen
Hintergrundprozess. Der separate RH-Forschungs-Heartbeat ruft den Abgleich
periodisch auf; seine Aktivierung ist in Codex zu prüfen. Er darf einen
fehlenden oder veralteten Beweis-Audit nicht als bestanden deklarieren.

## Zulassung eines Beweisschritts

Jede ausführbare Regel hat in `knowledge.json` eine Liste **gemeinsam
erforderlicher** Ziele und ein Ergebnis. Daraus entsteht eine echte
Lean-Theorem-Signatur. Lean prüft den eingetragenen Beweis gegen genau diese
Signatur; der rekursive Axiomenaudit erlaubt nur `propext`,
`Classical.choice` und `Quot.sound`. `sorryAx`, Forschungsaxiome und native
Auswertungsaxiome bleiben außerhalb dieser Zulassung. Diagnostisch geprüfte
Sätze mit solchen Abhängigkeiten werden weiterhin sichtbar, aber nicht als
Beweisregeln verwendet.

Die tatsächliche Anwendung erfolgt als kleinster Fixpunkt der bewiesenen
Implikationen. Äquivalenzzyklen erhalten keinen Startfakt. Ungeprüfte
Rezeptlisten liefern nur Forschungspläne, einschließlich einer zusätzlichen
Pflicht, dass die Zutaten das behauptete Ergebnis wirklich implizieren.
Die numerische Fitness, Dateinamen, ein FORMALIZED-Status und Graphpfade
können niemals einen mathematischen Fakt hinzufügen.

## Suche und Grenzen

```sh
python3 -B search_rh.py plan --beam 8 --max-expansions 500
python3 -B search_rh.py check
python3 -B -m unittest -q test_proof_search test_research_sync
python3 -OO -B -m unittest -q test_proof_search test_research_sync
```

Die Planung liest den vollständigen aktuellen Katalog für lexikalische
Vorarbeitssuche, prüft die Zielzuordnung zum semantischen Graphen und bindet
die verwendeten Quellen per Inhaltsabdruck. Allgemeine Graphkanten werden
bewusst nicht als Beweise importiert. Die mathematisch geprüften
AND-Verbindungen stehen im kleineren Regelgraphen.

Die erste Grammatik erzeugt acht Konstruktionsvorlagen aus arithmetischer
Gabor-Zerlegung, vollständiger Randkontrolle und minimiererspezifischen
Schranken. Das sind **keine acht neuen expliziten Operatoren**. Die Ergebnisse
stehen in `generated/PLAN.md` und `generated/plan.json`. OPEN_CONSTRUCTION
heißt lediglich, dass die registrierten Filter die genaue Vorlage nicht
ausschließen; es ist keine Erfolgsaussage oder vollständige Literatursichtung.

Priorität und Kosten sind nachvollziehbare heuristische Angaben, keine
gemessenen Chancen auf einen Durchbruch. In dieser Version gibt es weder
automatische numerische Jobstarts noch eine automatische Formalisierung
neuer Kandidaten. Der nächste Ausbau braucht eine explizite mathematische
Konstruktionssprache, überprüfbare Zertifikate und unabhängige Reproduktion.
Eine größere Stichprobe allein erfüllt keine globale Beweispflicht.

Der Prüfnachweis ist ein lokaler Reproduktions- und Frischebeleg, keine
kryptografisch signierte Drittzertifizierung. Aktualisieren oder Manipulieren
von Quelltext und Nachweisen durch eine vertrauensunwürdige Person ist nicht
das Bedrohungsmodell; vor einer wissenschaftlichen Behauptung muss der Lauf
unabhängig wiederholt und die Modellbedeutung der Lean-Typen geprüft werden.

Keine Änderungen am versiegelten RH-Testprogramm, am Verifikations-Ledger,
an den ursprünglichen Lean-Beweisen oder an den Papers sind Bestandteil
dieser Katalog- und Planerergänzung.
