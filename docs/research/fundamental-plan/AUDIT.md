# Abgleich des fundamentalen Aufgabenplans

30. Oktober 2026. Auftrag: Plan gegen Atlas, Lean und Verifikationen prüfen, konkrete automatische Suchwege ergänzen und eine fortlaufende Bearbeitung sichern.

## Tatsächlich geprüfter Umfang

| Bestand | Prüfung in dieser Sitzung | Ergebnis |
|---|---|---|
| Gemeinsamer Atlas | Aktuelle Revision, Hauptakte, relevante Aufgaben und vollständige einzelne Befunde mit Originalquellen | Revision `7938a35e1bae3619e7920e62`; 569 Befunde in 19 Akten. Keine Behauptung einer erneuten Einzelprüfung sämtlicher 569 Beweise. |
| Zentrales Lean Paket | Vollständiges vorhandenes `scripts/audit.sh`, einschließlich Build, Axiomkontrolle, Satznamen und Signatursperren | `AUDIT: PASS`; 67 Quelldateien unter `TfptCarrier/`. |
| Geladene Lean Sätze | Satztypen und transitive Axiomabhängigkeiten aus der tatsächlichen Lean Umgebung exportiert | 794 Theoremdeklarationen einschließlich automatisch erzeugter Hilfssätze. 783 nur mit Standardaxiomen; 11 mit benannten Projektaxiomen. Kein `sorryAx`. |
| Weitere wissenschaftliche Lean Quellen | Alle acht eigenständigen Quellen außerhalb des Hauptpakets unter den durchsuchten Theory Contracts | Sieben direkt erfolgreich übersetzt. `FixedCertificate.lean` verlangt erzeugtes `CandidateData`; über den ursprünglichen Kandidatenprüfer ebenfalls erfolgreich. |
| Vollständiges Python Register | Alle 707 registrierten Quelldateien geparst und mit dem tatsächlichen Gesamtlauf abgeglichen | Register und `run_all.MODULES` enthalten dieselben 707 Module. Dies ist ein vollständiger Bestandsabgleich, keine Neuausführung aller Module. |
| Python Kernprüfung | Bestehende schnelle Prüfung tatsächlich ausgeführt | 89 Prüfungen bestanden. Die dort angezeigten Wolframzahlen sind Verweise, keine neue Wolframausführung. |
| Entscheidende Anschlussprüfungen | 20 gezielt ausgewählte Module tatsächlich ausgeführt | 455 Prüfungen bestanden. Darunter v252/v258/v259/v261, Nahtverträge, kontinuierliche Dynamik, Neutrinogrenzen, Spiegel und Materiekopplung. |
| TEL B Intervallbeweis | v1026 in vorhandener nativer Umgebung mit `python-flint==0.9.0` | 199 der genannten 455 Prüfungen. Anfangs fehlte flint im Systempython; mit der vorhandenen Umgebung erfolgreich reproduziert. |
| Matrixkonstruktion | Ursprünglichen eingebetteten Konstruktor rekonstruiert und ausgeführt, danach Darstellungen gemeinsam verglichen | 165 exakte und zwei numerische Originalprüfungen bestanden. A1 abgeschlossen. |
| Automatische Operatorsuche | Vorhandene CEGIS Suche erneut ausgeführt | 2.048 Klassen erzeugt; ein Gegenbeispiel verwirft den linearen Kandidaten; bekannte antilineare Abbildung wiedergewonnen. Werkzeugkontrolle. |
| Inverse Operatorsuche | Vorhandene exakte Beispielkontrolle ausgeführt | Gemeinsamen Intertwiner gefunden; antilinearen Zweig durch einen konkreten Konfliktsatz ausgeschlossen. Synthetische Funktionskontrolle. |
| Positive Wortkerne | Gespeicherte vollständige Kandidaten mit vorhandenem exaktem Prüfer erneut geprüft | Zwei Kerne reproduzieren je 2.245 Momente. Zehn unterscheidende Wörter von Länge fünf; beide endlichen Clusteringprüfungen bestanden. |

Die ganze Python Suite und Wolfram wurden nicht erneut ausgeführt. Der Unterschied zwischen dem vollständigen Inventar, tatsächlichen Rechenläufen und einem physikalischen Herkunftsnachweis bleibt in allen Statusangaben erhalten.

## Änderungen am Plan

### 1. A1 ist erledigt

Der Originalkonstruktor steht im Abschnitt Q4 von `_newest2/TFPT_Gesamtdokumentation2_20260927.md`, als eingebettetes Originalmitglied `TFPT_Rekursive_Bindung_20260926/audit.py`. Sein Text stimmt nach Normalisierung abschließender Leerzeilen mit der dort genannten SHA256 `4a19f8145d5ccaef08bfdc5893f64484feae630cf61e49639df52f89f56528c4` überein.

Der erneute Lauf erzeugt die relevanten Matrizen aus ihren ursprünglichen Konstruktoren. Die Codemetrik ist `diag(4,12,12,12,24)`. R hat Rang 10 und Spektrum `1^1,(4/9)^9,0^15`. Der rohe Kommutator mit dem bereits orthonormierten H hat Norm `0.08799397280486623`; nach korrekter Transformation von R beträgt sie `6.948443849206147e-16`. Die Spektralradien der korrigierten Produkte sind bei t=0,1,5,10 jeweils bis auf Rundung eins.

Damit ist die Matrixkorrektur reproduziert. Der ursprüngliche Konstruktor benennt die zusätzliche Kopplung selbst als gewählte endliche Modellannahme. Ihre Auswahl aus TFPT wird durch diese Rechnung nicht hergeleitet. Der neue Plan macht aus diesem abgeschlossenen Kontrollproblem keine neue Zellsuche.

### 2. A2 ist erledigt; B1 und B2 sind getrennte Anschlussaufgaben

`SOURCE-DICTIONARY.md` hält die aktuelle modulare Kompression und den archivierten geometrischen Decksplit auseinander. Ein Scheitern des alten Graduierungsvergleichs blockiert nicht automatisch den aktuellen modularen Quellenweg. B3 verlangt eine tatsächlich passende Realstruktur auf dem jeweils benutzten Weg.

### 3. Bewiesene Mathematik wird als erledigte Unteraufgabe geführt

| Vorhandene Aussage | Genaue Beweisgrenze | Konsequenz für den Plan |
|---|---|---|
| `Polarization.sixY_carrier_polynomial`, Hyperladung und ganzzahlige Ladungsrigidität | Aussagen über die gegebenen Projektoren, Ränge beziehungsweise primitiven Ladungen | Unter C3 erledigt; die Herkunft ihrer physikalischen Realisierung bleibt offen. |
| `GlueUniqueness` | Endliche Diskriminantenformen, zwei zyklische Gluegruppen und ihr Spinorswap | Unter C3 erledigt. Keine erneute Suche nach diesem endlichen Glue. |
| `AnchorLadder.rankgap_uniqueness` | Positive ganzzahlige Tripel mit dem gegebenen Rangabstand | Unter F2 erledigt. Die Voraussetzungen nicht als voraussetzungslos bewiesen behandeln. |
| `PascalLadder.ladder_unique_K2` | Der tatsächlich geladene Lean Satz setzt `1≤g≤40` voraus | Diese konkrete Formalisierung ist beschränkt. Der Atlas enthält zusätzlich den unbeschränkten analytischen Satz `finding:pascal-carrier-rank-unique-unbounded-source-proof`. Beide Resultate behalten ihren eigenen Umfang. |
| `SpectralGapAttractor` | Skalarer beziehungsweise endlicher diagonalisierbarer Fall bei gegebenen Raten | Mathematische Konvergenz unter C2 erledigt. Kein Selektor des physikalischen Generators. |
| `FullCollar.lean` | Algebraischer rationaler Graphkern und abstrakte Involutionsidentität | Unter B1/C1 erledigt. Unbeschränkte Domain und ursprüngliche Trägerkompression benötigen ihre eigenen Nachweise. |
| `StateExpectation.induced_positive` | Allgemeine endliche Wortpositivität aus dem gegebenen `CrossedData` | Unter C1/F1 erledigt. Keine vollständige C* Vervollständigung, Zustandsauswahl oder konkrete Finsupp Instanzierung allein durch diesen Satz. |
| `OperatorTransport` | Allgemeine algebraische Transportregeln | Als Zertifikatsbaustein der Suche verfügbar. Der Satz prüft nicht automatisch jede gefundene Matrix. |
| `SeamEquivChain`, `SeamScalingLimit`, `BWKeystone`, `SeamStandardPair` | Formale Komposition mit ausdrücklich benannten externen Sätzen und ursprünglichen Realisierungseingaben | C1/C2/E1 übernehmen die Schlussketten; die tatsächliche Anwendbarkeit bleibt als konkrete Herkunftsaufgabe erhalten. |
| `PositiveDescentMaster.exists_limit` | Summierbare Schrittweiten ergeben Konvergenz einer gegebenen Folge | Unter F1 als mathematisches Werkzeug vorhanden. Kein selbstständiger GNS oder Quellenwahlsatz. |
| `LorentzCongruence.lorentz_congruence` | Eine bestimmte endliche Matrixkongruenz | Unter E1 als algebraische Vorarbeit erledigt. Keine daraus abgeleitete physische 3+1 dimensionale Raumzeit. |
| Alpha Gleichung, 5/4 Antwort und vorhandener exakter Transfervertrag | Genau die jeweiligen festgelegten Eingaben und Antwortklassen | D1 sucht den konkreten elektromagnetischen Herkunftsanschluss; Wurzel, vorhandene Antwort und deren enger Transfer werden nicht neu verlangt. |
| v1013, v1034, v1035 | Dynamik in der gegebenen Hamiltonklasse; konkrete Spiegelhindernisse; Wardantworten auf vorgegebene Quellen | E1 bis E3 verwenden diese Aussagen. Wechselwirkender chiraler Grenzübergang und universelle Quantengravitation bleiben getrennt. |

Die 11 projektaxiomabhängigen Deklarationen führen insgesamt 39 unterschiedliche projektbezogene Namen in ihren Abhängigkeitslisten. Darunter sind abstrakte Propositionssymbole. Das sind deshalb nicht automatisch 39 unabhängige physikalische Annahmen. Der genaue Typ jedes Satzes und seine tatsächlichen Abhängigkeiten stehen im exportierten JSON.

### 4. Konkrete Suche ersetzt allgemeine Suchaufforderungen

`SEARCH-METHODS.md` ordnet jeder Suchaufgabe Kandidatenklasse, Eingaben, Constraints, Löser, exakten Prüfer und Abbruchkriterium zu. Bereits vollständig klassifizierte Räume werden wiederverwendet. Die bekannte 262.144 Klassen umfassende Phasensuche ist abgeschlossen; sie wird nicht ohne eine veränderte ursprüngliche Voraussetzung neu gestartet.

### 5. Fortsetzung ist dauerhaft angeschlossen

`PLAN.md` ist der kanonische Plan, `progress.json` der aktuelle Aufgabenstand und `RESULTS.md` das fortlaufende Ergebnisprotokoll. Die Projekteinstiege verweisen darauf. A1 und A2 sind erledigt; die vorhandenen mathematischen Teilresultate stehen als erledigte Unteraufgaben in den weiterhin offenen Herkunftsaufgaben. Nächste Aufgabe ist B1.

## Nachweise

Alle maschinellen Ausgaben liegen in `evidence/`. Das Verifikationsinventar erfasst alle registrierten Module samt Beschreibung, Ledgerzuordnung und Quellhash. Der Lean Export erfasst tatsächliche Satztypen und transitive Axiome der geladenen zentralen Umgebung. Die zusätzlichen isolierten Quellen und der erzeugte Kandidatenbeleg haben eigene Ausgaben.

Diese Prüfung ändert keine wissenschaftlichen Ledgerstatus und schreibt historische Originalquellen nicht um.
