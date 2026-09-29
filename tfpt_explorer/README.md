# TFPT Explorer

Eine lokale, ausführbare Gesamtrepräsentation der TFPT-Paper und der endlichen
Universalraum-Konstruktionen. Die Oberfläche liest die berechneten Matrizen,
Zustände, Spektren und Ausgaben aus dem Python-Rechenkern. Sie verwendet keine
animierten Ersatzwerte und benötigt keinen externen Dienst.

## Start

Aus dem Repository:

```sh
python3 -m tfpt_explorer
```

Oder `tfpt_explorer/Start_TFPT.command` im Finder öffnen. Die Anwendung läuft
unter `http://127.0.0.1:8787`. Ein anderer Port ist mit `--port 8790` möglich;
`--no-browser` startet nur den lokalen Server. Die Python-Abhängigkeiten stehen
in `requirements.txt`. Die vorhandene TFPT-Umgebung enthält sie bereits.

## Bedienung

**Flavor → α** (`#flavorpfad`) verbindet den ursprünglichen Familienumlauf
mit dem ganzen endlichen Flavoroperator. Zwei tatsächliche Halbwege der
v117-Fuchsverbindung liefern den Sechsertransport; die sieben anwählbaren
Ansichten zeigen Start bis vollständige Rückkehr. Der Rechenkern integriert
die Wege und prüft die Determinantenwindung sowie den ursprünglichen Kernel.
Darunter steht der neu berechnete neutrale Quellenzustand mit Normquadrat 48
und konformem Gewicht zwei. Sein Alpha-Port ist ausdrücklich bedingt durch
die angegebene Nahtkopplung und die konforme Fortsetzung. Die gemeinsame
Antwort im ursprünglichen Flavor-Defekthintergrund wird ebenfalls aus der
Originalverbindung berechnet; die Vakuumantwort wird nicht in diesen
Hintergrund kopiert. Die Schritte zählen Wege, keine physische Zeit.

Die Fortsetzung derselben Tour hebt die originale Einheitswindung auf die
geladene E₈-Quelle: Nach drei ganzen Familienumläufen bleibt ihr D₈-Deckzeichen,
nach sechs ist die Wirkung identisch. Die 120 geraden und 128 ungeraden
Stromrichtungen werden aus allen Originalwurzeln berechnet. Dieser interne
Spinlift wird von physischer Fermionstatistik und vom Zweifaseroperator getrennt.
Der anschließende Paarvergleich benutzt die ursprüngliche affine Algebra:
Das direkte Singletpaar ist bei Level eins null, der antisymmetrische Kanal
erscheint bei konformem Gewicht drei, der symmetrische Majorana-Paarkanal bei
Gewicht vier. Operator-Existenz und physische Kopplung/Kondensation bleiben
verschiedene Aussagen; der neue Spin-Z₄-Selektor wird auch gegen die bestehende
skalare Spinor-Higgs-Route geprüft.

**Gemeinsame Physik** (`#gemeinsame-physik`) verbindet jetzt auch die vollständigen Massentensoren,
die tatsächlichen Eichladungen und den neutralen Flavor-Defektkern.
`source_charge_response.py` berechnet die ungewichtete 48er-Antwort und die
hyperladungsgewichtete Antwort aus denselben Wurzeln. Der bekannte Faktor
41/10 folgt unter den ausgewiesenen vierdimensionalen Materie-/Higgsannahmen.
`source_neutrino_dictionary.py` übersetzt symmetrische Familientensoren samt
Phasen in die ursprünglichen Paaroperatoren und liest sie durch sechs komplexe
Amplituden wieder aus. Der schwere Majoranakanal und die über die vorhandene
Seesaw-Regel entstehende leichte Matrix behalten verschiedene Feldtypen.
Der Phasenumschalter zeigt berechnete Beispiele, bei denen gleiche Massen
unterschiedliche Interferenzantworten erlauben. Die ursprüngliche phasenoffene
Klasse wird vom bereits vollständig festgelegten Matrixansatz unterschieden.
`source_flavor_correlator.py` berechnet die verbundene neutrale Antwort aus
dem ursprünglichen RHP-Kernel und prüft außerdem den vorhandenen Markenport.
Die Auswahl des gemeinsamen physischen Zustands, seiner Kopplung und der
Raumzeitabbildung bleibt eine zu beweisende Herkunftsfrage.

**Geführte Tour** erklärt den Zusammenhang in 15 Stationen. Eine große Grafik
zeigt jeweils Eingang, Veränderung und Ergebnis. Die vier Blickwinkel
**Geometrie**, **Topologie**, **Mathematik** und **Physik** unterscheiden die Form,
die Verbindungen, die Rechnung und ihre physische Bedeutung. Jede Station sagt,
welchen Beitrag sie zur gesuchten Gesamtlösung leistet. Am Ende stehen die acht
gemeinsamen physischen Anforderungen T1–T8 mit vorhandenem Anschluss und noch
fehlendem entscheidendem Nachweis. Der Einstieg hält den älteren TFPT-Compiler
mit Flavor, Alpha und Gravitation sowie die neuen Codeprozesse zusammen.

**Gesamtbild** zeigt die typisierten Verbindungen. Ein Knoten hebt seine
Voraussetzungen und Folgen hervor; **Alle Verbindungen** zeigt wieder den ganzen
Graphen. **Ablauf** führt durch alle 24 implementierten Schritte, jeweils mit
Eingang, Operation, Ergebnis, Grafik und Originalquellen.

Die sechs Eingaben steuern Clocks, Transferdauer, Rekursionstiefe,
Inflationsdauer, Phase und Anfangszustand. **Neu berechnen** führt den Rechenkern
aus und markiert die veränderten Schritte. Der Phasenregler verwendet ganzzahlige
Schritte `b = n/144`, damit die ausgezeichneten Werte `0`, `1/18` und `2/9`
auch tatsächlich an den Rechenkern übergeben werden.

**Belege & Versuche** durchsucht den vollständigen erfassten Bestand.
**Bestand aktualisieren** übernimmt neue Laufprotokolle. **Neu prüfen** führt
ein einzelnes registriertes Originalmodul aus. Die Quellenansicht liest
Originaldateien mit Zeilennummern. **Lean** unterscheidet Originalbeweise,
Definitionen, Axiome, `sorry`-Stellen und wirklich ausgeführte Exporte.

**Zuse, Wolfram & Quellenregel** (`#graphen`) führt in sieben bedienbaren
Schritten durch den tatsächlichen Anschluss von Ereignissen, Untergittern und
geladenen Sektoren. Eine Auswahl zeigt alle 15 Hecke-Marken und ihre jeweils
vier nativen Ereignisse. Der Vergleich mit ausgeblendetem Spinoranteil macht
eine verlorene spätere Stromantwort sichtbar. Der nächste Vergröberungsschritt
vergleicht die geerbte Selbstpaarung mit den vollständigen Charaktertests.
Zustandsgraph, Untergittergraph, kausaler Ereignisgraph und räumliches Netz
behalten verschiedene Bedeutungen.

`hecke_source.py` berechnet die kanonische Abbildung aus allen 60 nativen
Reflexionen, die tatsächliche Transportwirkung auf 240 Wurzeln, den D₈-Index-2-
Unterraum samt geladenem Spinorkoset und dessen vollständige Rückverklebung.
Die duale Paarung liefert die nächsten Untergittertests. Über alle ersten
Kinder sind deren mögliche Vorzeichenfortsetzungen genau die vorhandenen
256 Charaktere; eine Fortsetzung ist nicht automatisch die physische Auswahl
des nächsten Ereignisses. Die Kreisrekonstruktion liefert dieselbe Quelle,
keine neuen räumlichen Orte.

Für jede endliche Tiefe berechnet `lift_sublattice_character(K,c)` die
Quellenphase `theta=K^(-T)c`. Dadurch gilt der gewünschte binäre Test exakt auf
dem gewählten Untergitter. Auf der ganzen Quelle können feinere Phasen nötig
sein: Die gezeigte Folge hat die Ordnungen 2, 2, 4, 4, 8. Ihre vollständigen
Spektralprojektoren und ein kohärenter Ergebnisträger sind ebenfalls berechnet.
Der geladene Verbraucher verschiebt bei jeder Feldwirkung zugleich die
gespeicherte Phasenadresse und erhält so exakt die ursprüngliche Wirkung.
Ein Regler in Schritt fünf zeigt die endliche Phasenfortsetzung. Acht Bits reichen für alle
ersten Kinder; für beliebige endliche Tiefe werden rationale Phasen benötigt.

`rewrite_coherence.py` verwendet die bereits berechneten SU(5)-KZ-Reste.
Überlappende Reste kommutieren nicht; ihre vollständige Verbindung ist exakt
flach. Die gebrochenen Phasen des physikalischen Fusionsblocks kompensieren
sich mit dem vorhandenen E₈-Partner. Dies beschreibt Quelltransport auf einer
gegebenen Einfügegeometrie. Es identifiziert weder diese Geometrie mit
Raumzeit noch KZ-Transport mit einer Hecke-Fortschreibung.

Der direkte Anschluss beider Rechnungen ist geprüft: Die fortgeschriebenen
Charakterphasen erhalten sämtliche geladenen E₈-Wurzelklammern, die invariante
Paarung und den diagonalen Casimir. Damit sind sie mit den vollständigen
Quellen-Wardidentitäten verträglich. Casimirbasierte KZ-Verbindungen sind dort
kovariant, wo ihre Modulvoraussetzungen gelten; die E₈-Ströme selbst sind
Vakuumnachfahren und keine adjungierten E₈-Level-1-Primärfelder. Die gesonderte
KZ-Prüfung oben betrifft ihre SU(5)-Primärfaktoren. Die Phasenaussage gilt
bei gemeinsamer Transformation aller Beteiligten; eine einzelne lokale
Phasenänderung bleibt wirksam. Eine echte Untergitterprojektion ersetzt diese
Automorphismen nicht und darf ihre ausgeschiedenen geladenen Felder nicht
stillschweigend löschen.

`cartan_source.py::build_cartan_clock_dictionary_data` prüft jetzt ausdrücklich
auch die ursprüngliche σ-Markierung. Die frühere volle M4-Identifikation war
nur unmarkiert korrekt: Original-σ hat Fixalgebra M2⊕C⊕C (Dimension 6),
Wort-σ dagegen M2⊕M2 (Dimension 8). Ein Basiswechsel repariert dies nicht.
Die korrekte native Verbindung ist der ursprüngliche σ-feste Zweierraum.
Er enthält zwölf Wurzeln bzw. drei μ4-Strahlen. Ihre Projektoren liefern mit
der eindeutig bestimmten Normierung 2/3 genau die bisherige Trine-POVM.
Die Auswahl/Präparation dieses Sektors ist damit noch nicht hergeleitet.

`marked_source_process.py` berechnet auf diesem tatsächlichen Träger die
Zeitantwort. Von allen 60 einzelnen Reflexionen erhalten sechs den Träger:
drei wirken identisch, drei sind die Trine-Reflexionen. Die Clock-Antworten
2/3 und 1/3 bestimmen ihre komprimierten Mischungsgewichte eindeutig als
(1/2, 2/9, 2/9, 1/18); die dritte Antwort G wird dabei gelöscht (q=0).
Produkte derselben drei Reflexionen realisieren jedoch genau die ursprüngliche
S3-Familie aus v976. Ihr vollständiger Gewichtsraum ist
w_t=(1/2+t,t,t,1/18−t,2/9−t,2/9−t), 0≤t≤1/18, mit q=6t.
Das ist keine neue Hilfsregel: Die ursprüngliche Verifikation ist jetzt mit
den tatsächlichen markierten Quellenereignissen verbunden. Innerhalb dieser
Klasse ist die GNS-Vierpunktfunktion mit linken Operator-Einsetzungen
F–A–A–F=q/9 (keine Instrument-Messwahrscheinlichkeit); die ältere Vorgabe 1/27 wählt q=1/3, sofern ihre
physische Quellenidentifikation unabhängig gesichert wird.

Die Forderung kontinuierlicher reversibler Sprünge auf genau S3 lässt sich
zusätzlich exakt prüfen. Der eindeutige selbstadjungierte Gruppenlogarithmus
hat nichtnegative Ereignisraten genau für 2/9≤q≤1/4. Bei q=1/3 ist die
p12-Rate log(3/4)/6 negativ. Das widerlegt weder den diskreten Prozess noch
seine kontinuierliche Quanten-Markov-Einbettung auf M2: Diese benötigt nicht
zu jeder Zwischenzeit eine positive Mischung derselben sechs Ereignisse.
Die diskreten S3-Worthistorien sind für die ganze Faser reflexionspositiv;
Reflexionspositivität allein wählt deshalb den Endpunkt ebenfalls nicht.

B wirkt hier exakt auf die Erwartungswerte der drei Effekte. B ist keine
Übergangsmatrix aufeinanderfolgender Messausgänge derselben Trine-POVM:
Jede ihrer Ausgangswahrscheinlichkeiten ist höchstens 2/3, während B die
Diagonaleinträge 13/18 besitzt. Der siebte Tourschritt zeigt den nativen
Anschluss, die Wirkung zusammengesetzter Ereignisse und diesen Unterschied.
Eine vollständige Quelle muss zusätzlich ihre Präparation, zulässigen
Eingriffe und gemeinsame räumliche und zeitliche Wirkung bestimmen.

Die Gesamteinordnung beginnt jetzt mit dem tatsächlich gemeinsamen geladenen
Quellenraum. `build_joint_charged_source_data` verwendet die ursprünglichen
E8-Chevalley-Klammern für X(i,a) und ihre kompakten Adjungierten. Diese Felder
tragen **bar5⊗4**; ihre physische P2-Ladung ist −y_i. Ihre Klammern erzeugen
die SU5- und SU4-Handlung innerhalb derselben A8-Unteralgebra. Mit den vier
ursprünglichen C-Feldern und allen Gegenfeldern entsteht die gesamte E8-
Stromalgebra: 48 → 140 → 240 Wurzelrichtungen plus acht Cartanrichtungen.
Der native
Quartik-Lift wirkt auf beiden Leseseiten innerhalb dieser einen Quelle.
Das behauptet keine Gleichheit mit der separaten Cartan-Gitterhebung.
Die Gesamtkarte am Anfang von `#prozesskern` zeigt diesen gemeinsamen Träger
und unterscheidet ihn von räumlichen Orten.

Der gemeinsame Anschluss lässt sich auf einen bedingten Generatorensatz verdichten:
Die ursprünglichen lokalen Ströme müssen auf einem gemeinsamen Energiecore die
vollständigen affinen Level-1-Relationen und Daggerstruktur erfüllen, ein normiertes
positives zyklisches Vakuum mit J_nΩ=0 für n≥0 besitzen und das gesamte betrachtete
lokale Netz erzeugen. Dann bestimmen Kommutatoren und Vakuum alle Wort-Grammatrizen
und nach Nullquotient den Level-1-Vakuummodul. Vakuumzustand und geometrische Zeit
sind in diesem Rahmen keine zusätzlichen unabhängigen Wahlen. Eine separat vorgegebene
physische Rohquellenzeit ist nur bei nachgewiesener geometrischer Verschränkung
mitidentifiziert. Die raw-Realisierung,
lokalen Operatorabschlüsse und ursprünglichen Markierungen bleiben nachzuweisen;
der Satz ist kein neuer Nachweis dieser Voraussetzungen oder einer 3+1D-Theorie.

Für das bereits gewählte lokale E8-Vakuumnetz bestimmt Netz plus Zustand die
geometrische Möbius-Zeit (Bisognano–Wichmann). Die Original-Viertelrotation ist
das Produkt der modularen Spiegelungen an den ursprünglichen Achsen 0 und
π/4. Diese literaturgestützte Aussage ist kein endlicher Matrizenbeweis eines
lokalen Netzes. Die normale lokale, zustandserhaltende Identifikation der
rohen P1-Quelle bleibt die ursprüngliche Herleitungsaufgabe. Die gedämpfte
Clock-Matrix ist keine geschlossene Automorphismenwirkung: Ihre physische
Auslese/Kompression und deren Gedächtnis müssen aus derselben Quelle folgen.
Der 4D-Gesamtvertrag verlangt anschließend ein einziges erzeugendes
Funktional samt Anfangszustand für die räumlichen, Flavor-, Kopplungs- und
Gravitationsantworten; der Randquellenanschluss ersetzt diesen Vertrag nicht.

## Was ausgeführt wird

- `core.py`: Anker, Naht und Funktionenraum, äußerer Träger samt Ladungen,
  tatsächliche D5+A3-Verklebung, E8-Wurzeln, Coxeter- und Galois-Matrizen,
  Flavor, Alpha-Fixpunkt, dokumentierter Transferrepräsentant, eingefrorene
  Formelvorhersagen und bedingte Gravitation/Kosmologie.
- `process.py`: Hamming-Wörter, Quellenstrahlen, Vierregistercode, Antwort-
  und Ladungsoperatoren, Quartik, Bindung, Blockisometrie und Rekursion,
  markierte Raumkonstruktion sowie die expliziten gemeinsamen 60 Amplituden
  der Register-/Codeantwort. Derselbe Vierertensor wird als Encoder und in
  seiner 60/40-Normzerlegung nachgerechnet. Der minimale gemeinsame
  Siebenerträger repariert ausschließlich die angegebenen C4-Clockwirkungen.
- `consolidation.py`: die neuen Anschlüsse aus der Konsolidierung vom 28.09.:
  Projektorgeometrie und Beobachtbarkeitsabschluss 10→20→25, der Normfehler
  10/9 auf dem antisymmetrischen Sektor, die sektorerhaltende algebraische
  Normreparatur sowie die ladungskovariante Dreierpfad-Montage im markierten
  A3-Netz. Die Rechnung verwendet für die Normreparatur einen gleichfaserigen
  Code-Lift; sie setzt diesen nicht mit der separaten Registerfamilie gleich.
- `tour.py`: quellengebundene verständliche Einordnung der Live-Rechnungen
  und der sieben neuen Dokumente, mit klar bezeichneten Quellenresultaten,
  die nicht erneut vollständig ausgeführt wurden.
- `evidence.py`: vollständiger vorhandener Theoriegraph, originales Ledger,
  Skriptregister, Forschungsversuche und experimentelle Scorecard. Status
  aus diesen Quellen und Ergebnisse eines frischen Laufs bleiben getrennt.
- `lean_bridge.py`: Erfassung der eigenen Lean-Quellen, Aufruf der bestehenden
  Build-Ziele, Ausführung importierter Originaldefinitionen, Axiomausgabe
  ausgewählter Beweise und automatische Adapter für einfache Nat-Definitionen.
- `server.py`: Berechnung, Export, lesender Quellenzugriff und begrenzter Aufruf
  registrierter Verifikationsmodule. Bindet ausschließlich an die lokale
  Schnittstelle; es gibt keinen Endpunkt für beliebige Shellbefehle.

Die Gesamtkarte unterscheidet eine berechnete Abhängigkeit, eine zusätzliche
Annahme und einen Strukturvergleich. Der Ablauf enthält exakte mathematische
Verträge und numerische Realisierungen. Ein angezeigtes `exact` bezeichnet den
mathematischen Vertrag der Quelle, nicht automatisch exakte Maschinenarithmetik;
die Methode und Abweichung jeder ausgeführten Prüfung stehen am Rechenschritt.

Insbesondere sind Rauminterpretation, dimensionaler Maßstab, physische
Feldidentifikation und Anfangszustandswahl ausdrücklich benannte Voraussetzungen.
Eine noch nicht implementierte physische Herleitung ist eine sichtbare offene
Schnittstelle. Eine bestandene endliche Prüfung schließt sie nicht stillschweigend.

## Eigene Rechnungen und Herkunft

Die Oberfläche zeigt die Originalquelle mit Zeilennummern. Die Berechnungen sind
neu organisiert; die ursprünglichen Verifikationsmodule und Forschungsdateien
bleiben unverändert. Der Quellenkatalog kennzeichnet auch Dokumente außerhalb
des erfassten Theoriegraphen. Eine thematische Suchzuordnung eines Belegs ist
keine neue mathematische Beweiskante. Alle 15 vom Nutzer genannten Dateien und
der eingefügte Text sind als eigene Dokumentquellen auffindbar. Die außerhalb
des Repositories liegende Konsolidierungs-PDF und der eingefügte Text liegen
unverändert in `sources/`; `sources/manifest.json` dokumentiert Herkunft und
Prüfsummen. Dokumentabdeckung bedeutet nicht, dass jeder Satz des Korpus bereits
als eigene Berechnungsfunktion implementiert ist.

Die Konsolidierungs-PDF nennt 177 plus 19 Prüfungen in `pruefe_tfpt.py` und
`pruefe_a3.py`. Diese beiden Originalprogramme lagen in den durchsuchten
Projekt- und Dokumentbeständen nicht vor. Die neuen Konsolidierungsrechnungen
sind deshalb unabhängige Rekonstruktionen der angegebenen Formeln und Tabellen;
die 196 dokumentierten Prüfungen werden nicht als erneut ausgeführt gezählt.

Der Transferrepräsentant aus `v56_unique_attractor.py` verwendet die dort gewählte
nichtorthogonale Basis. Seine Komponenten sind keine Wahrscheinlichkeiten. Der
Parameter `phase_b`, die Rekursionstiefe, der markierte Raumkandidat und die
Inflationsdauer haben unterschiedliche Rollen; ihre Regler werden nicht als
gemeinsam aus P1/P2 hergeleitete Freiheitsgrade ausgegeben.

## Zusammensetzung und Gesamtfolgern

Der **Prozesskern** beginnt mit den ursprünglichen Rückschleifen. `origin_closure.py`
berechnet Vierpunktdivisor, Träger/Familien, μ₄-Verklebung, E₈-Rang und Coxeterordnung
gemeinsam mit φ₀ und der α-Gleichung. Die ursprüngliche 60→8-Kaskade ist als
optionaler Zweig sichtbar und keine Bedingung der gemeinsamen Auswahl. Die Tour
behandelt P1/P2 entsprechend der expliziten Korrektur in `origin_theory.tex` (v350)
als rückbestimmte Daten innerhalb des ursprünglichen Abschlussrahmens. v487 legt
die lokale Transferregel unter Clock-Treue, Deckparität und Positivität fest.
Die Oberfläche zeigt beide Rückschleifen mit auswählbaren Stationen und Originalstellen.

`origin_transfer.py` transportiert die ursprüngliche dreidimensionale Clock auf
den geladenen Trimer. Die minimale Fortsetzung `C=I/2+S13/6+WW†/3` besitzt beide
originalen Raten und kommutiert mit den vervollständigten Paarbindungen. Deckwirkung,
Fixslot und Rate des restlichen Tensorraums sind ausdrücklich bezeichnete
Identifikationen. Eine Gegenfamilie auf dem 45-dimensionalen Rest zeigt, warum
die ursprüngliche Eindeutigkeit des Clock-Seeds noch keine Eindeutigkeit des
gesamten Tensortransfers ist. Iteration, Amplituden und Populationsraten bleiben getrennt.

`twisted_source.py` prüft zusätzlich die Verbindung zwischen Gaussian-E₈-Quotient
und verdrehtem Gittermodul: Die endliche Heisenberg-Paarung stimmt überein, die
native G31-Reflexionsdarstellung wird dadurch jedoch nicht identifiziert. Die
gesonderte Prüfung der Operatorwirkung verhindert, dass zwei vierdimensionale
Räume allein wegen ihrer Dimension gleichgesetzt werden.

`cartan_source.py` prüft den passenden unverdrehten Anschluss: Auf dem markierten
E₈-Cartanraum stimmen alle 60 Produkte `s_a s_Ja` exakt mit den nativen
G31-Reflexionen überein. Geladene Wurzelfelder behalten zusätzlich Liftphasen.
`torus_lift.py` prüft deren gleichzeitige Relationen über den ganzen Zahlen:
Ein Zeugnis `uA=0`, `ub=1` schließt eine globale Sektion auch bei kontinuierlichen
U(1)-Charakterkorrekturen aus. Der Geltungsbereich ist der markierte Gitter-VOA;
zusätzliche physische Randfreiheitsgrade werden nicht ausgeschlossen.

`source_process.py` führt genau diese geladene Quellenwirkung aus. Der Zustand
speichert Gitterwirkung und acht binäre Charaktermarken. Ein Ereignis aktualisiert
beides; Speichern/Laden benötigt keine vergangene Wortfolge. Die Tour spielt die
Wege `0,1,0` und `2,1,2` schrittweise ab: gleiche nackte Wirkung, aber der exakte
D5+A3-Deckcharakter auf geladenen Feldern. Die Ereignislabels sind vorgegeben;
ihre physische Auswahl wird nicht behauptet.

`quartic_selection.py` leitet die fünf Quartikkoordinaten als ersten nichtkonstanten
Grad des Pauli-Invariantenrings her. Die Minimalitätsforderung selbst bleibt eine
Quellenbedingung. `joint_constraints.py` prüft Ladung, Pfadentwicklung und alle
zugelassenen Folgeeingriffe gemeinsam. Der 80er-Träger ist nur unter eingeschränkten
Blockoperationen geschlossen; ursprüngliche Einzelverbindungen erreichen auch den
45er-Rest. Die tatsächlichen Spektren schließen die direkte Gleichsetzung der
Survival-Clock mit der euklidischen Pfadzeit aus. Das schließt ihre unterschiedliche
Verwendung als Filter und physische Dynamik nicht aus.

`charge_selection.py` verwendet den tatsächlichen P2-Polartransport: Vier der
15 Ereignisse erhalten den festen Marker Y. Die übrigen elf können durch einen
reinen Labelspeicher keine additive Gegenladung erhalten; dies folgt exakt aus
symmetrischen Ereignismatrizen und antisymmetrischen Kommutatoren. Die vorhandene
Paarbindung auf Fünfer und Gegenfünfer erhält dagegen die Gesamtladung exakt und
vermittelt den Austausch +5/6 gegen −5/6 zwischen realen Nachbarfaktoren. Das
Label-Record-Gegenresultat ist deshalb kein Ausschluss dieser Graphdynamik.

Die gemeinsame Paarselektion wird in `joint_constraints.py` direkt ausgeführt:
Die tatsächliche P2-Ladung verbindet die nativen Sektoren 5, 9 und 10 durch
zwei strikt positive Matrixgewichte. Volle kollektive native S6-Symmetrie plus
Erhaltung dieser Ladung erzwingt daher `H=cI+k(I-P_Omega)`. Positivität und
ein eindeutiger neutraler Nullzustand lassen `k>0` übrig. Das ist ein bedingter
Auswahlsatz für die Form, keine bloße Empfehlung einer SU5-Mittelung. Die Tour
vergleicht diese volle Symmetrieforderung mit der schwächeren markierten
Eichsymmetrie. Die physische Herkunft der vollen Hamiltonsymmetrie bleibt sichtbar.

`current_source_bridge.py` prüft einen konkreten Anschluss an den älteren
Quartik-E₈-Quellenlift: Der Spuranteil einer Paarmatrix wird auf das Vakuum,
der spurfreie Anteil auf die vorhandenen SU(5)-Ströme abgebildet. Norm,
alle 60 Ereignisse, Ladung und L₀-Wirkung intertwinen auf diesem ausgewählten
Teilraum. Er ist unter zusätzlichen Stromerzeugungen nicht geschlossen.
Auch die direkte Fortsetzung derselben L₀-Zeit auf den Originaltrimer scheitert
an dessen exakten Graddifferenzen 2/5 und 6/5. Diese Abbildung ist deshalb
kein vollständiger Quellprozess. Die geladenen E₈-Lifts werden getrennt:
Der Quartiklift hat adjungierte Spur 16 und Ordnung 8, die definierten
involutiven Cartanlifts haben Spur −8 oder 24 und Ordnung 2. Die Acht-Bit-
Fortschreibung gehört allein zum angegebenen Cartan-Zweig.

`current_block_geometry.py` verbindet die ursprüngliche Nahtgeometrie direkt
mit der Dreierkodierung. Die geordneten μ₄-Marken werden exakt auf
`(-1,0,1,infinity)` abgebildet. Die originale Chevalley-Stromrechnung liefert
dort den Vierpunktkorrelator `2(delta_ij delta_kl + delta_il delta_jk)`.
Als Dreierabbildung gelesen ergibt er nach Normierung genau den vorhandenen
W-Encoder. Als RP-Paarantwort mit der ursprünglichen Spiegelpaarung gelesen
ergibt derselbe Tensor `K=2I+10P_Omega` und damit `I-K/12=h_cov`.
Ein verschiebbarer Einfügepunkt zeigt in der Tour, weshalb gerade die
ursprüngliche Markierung den geraden W-Anteil auswählt.

Die gemeinsame Deutung bleibt geprüft und begrenzt: Bei gleicher Orientierung
liefert dieselbe Maximal-Eigenwert-Normierung `2h_same`; beide ursprünglichen
Paarstärken werden dadurch nicht gemeinsam hergeleitet. Der echte Vierstrom-
Korrelator auf vier offenen Nachbarzellen hat Energievarianz `2/147` und ist
damit kein stationärer Zustand dieser Nachbardynamik. Das schließt seine
Präparation mit anschließender Entwicklung nicht aus. Stromzuordnung der
rohen P1-Naht und physischer Zeitgenerator bleiben eigene Herkunftsfragen.

Dieselbe Stromrechnung wird außerdem auf zwei Dreiergruppen angewendet.
Im Koaleszenzgrenzwert schließt die normierte Sechsstromantwort exakt auf
`(W tensor Wbar) Omega`. Bei endlichem `t=epsilon/L` bleibt dagegen ein exakt
berechneter Normanteil außerhalb dieses Bildes. Die vorhandenen lokalen
Projektoren zerlegen ihn in WZ, ZW, ZZ, den 45er- und den 70er-Sektor. Der
Rest beginnt mit `t^2/3`; auch die 45er- und 70er-Anteile sind auf `0<t<1`
streng positiv. Die Tour zeigt die beiden Gruppen und alle sechs berechneten
Sektorgewichte mit einem Abstandsregler. Die Zwei-Cluster-Anordnung ist ein
erklärter Test der OPE-Zusammensetzung, kein bereits aus P1 ausgewähltes
Raumnetz. Der feste lokale Tensorraum und der unbeschränkte affine
Anregungsturm bleiben getrennt.

Die echte affine Gramrechnung prüft anschließend, ob die Quelle selbst diese
Sektoren tragen kann. Auf `J_-1 X` sind die normierten Gram-Eigenwerte
`6 (5fach), 2 (45fach), 0 (70fach)`; auf `J_-2 X` steigen sie exakt um eins.
Damit existiert ein graduierter SU(5)-Träger mit 5 im E8-Grad 1, weiteren 5
und 45 im Grad 2 sowie 70 im Grad 3. Die Rechnung importiert die ursprüngliche
v498-Affine-Implementierung und verwendet die tatsächlichen Quellenströme.
Sie belegt Sektorverfügbarkeit, keine bereits konstruierte Abbildung des
vollständigen Sechsstromzustands oder Gleichsetzung mit physischer Zeit.

Die Tour enthält eine auswählbare Wenn–Dann-Kette, zwei bedingte Gesamtarchitekturen
und die Prüfung der acht Aspekte des ergänzten Zuse-Texts. `synthesis.py` verbindet
diese Aussagen mit den Live-Daten und berechnet insbesondere die Ereigniskosten
`I-Ubar=G4+2/5 I` sowie die 30×30-Blochmatrix des tatsächlichen markierten Netzes.
Dieselbe räumliche Matrix kann verschiedenen Zeitgesetzen zugrunde liegen; die
Darstellung identifiziert ihre Eigenwerte deshalb nicht mit physikalischen Frequenzen.

`composition.py` konstruiert den Zweiblock-Encoder direkt mit ganzzahligen
Kroneckerdeltas. Eine rationale Leakage-Grammatrix bestimmt den einzigen
invarianten Strahl der angegebenen neun positiven Paarterme. Beide Orientierungen
schließen auf `H9 V=V(4I+h)`; kollektive Kovarianz macht dies auf beliebigen
vorgegebenen endlichen Blocknetzen gültig. Die schwachen Einzelkanten des alten
A3-Netzes sind davon verschieden und werden separat projiziert. Energieverschiebungen
bleiben sichtbar, weil sie bei veränderlicher Graphstruktur nicht global konstant sind.
Der gewählte Graph, die Neun-Port-Vervollständigung und die Identifikation mit einer
physikalischen Zeitregel werden nicht als aus der primitiven Quelle abgeleitet ausgegeben.

`history_kernel.py` verbindet das vorhandene Ereignisalphabet mit seinem positiven
Minimalgenerator und, unter der erklärten SU(5)-Symmetrievervollständigung, der
geladenen Paarbindung. Es konstruiert den normierten Geschichtskern für 15 und
225 Ereigniswörter, prüft dessen kausale Marginalisierung und erhält ihn durch
den W-Encoder. Die skalaren Aktionsphasen der Blockbindungen bleiben Bestandteil
des vollständigen Geschichtskerns. `kernel_narrative.py` ordnet die 17 Punkte des
zweiten eingefügten Texts und den nachfolgenden Rekonstruktions-/Fixpunktsvorschlag
in zwölf zusammenhängende Fragen ein. Die endliche GNS-Darstellung wird tatsächlich
ausgeführt. Ein gemischtes Ereignis-Link-Protokoll prüft die relative Phase mit
demselben Maßstab `J=2pi hbar/(5 tau0)`; die verlustfreie Rekodierung und der
primitive reduzierte Ereigniskanal bleiben getrennte mathematische Objekte.
Direkter Einstieg:
`http://127.0.0.1:8787/#prozesskern`.

`marker_selection.py` prüft alle 15 Matchingkandidaten exakt in der vorhandenen
nativen Polartransportbasis. Genau drei minimieren die Ladungsstörung und bilden
eine Familienklasse. Die Grafik zeigt jede Paarung mit ihrem berechneten Wert.
Das Mindeststörungsprinzip bleibt eine zusätzliche Quellenforderung. Alle drei
ergänzten Originaltexte sind unverändert in `sources/` mit Herkunft auffindbar.

`spatial_response.py` berechnet die räumliche Antwort veränderter positiver
Kantenraten mit dem harmonischen Korrektor der gesamten 30er-Zelle. Der Vergleich
mit der gewichteten Blochmatrix prüft eine tatsächliche Veränderung der Ausbreitung.
Die Einzelknoten-Momente des vorliegenden Netzes sind singulär; eine Lorentzmetrik
oder Gravitation wird nicht mit dieser räumlichen Antwort gleichgesetzt.

PDF-Quellenlinks öffnen die betreffende unverändert gerenderte Originalseite mit
Seitennavigation. Dafür nutzt `pdf_preview.py` pypdfium2/Pillow im aktiven Python oder
den vorhandenen gebündelten Codex-Python; die Originaldatei bleibt als Download zugänglich.

## Ein gemeinsames Quellgesetz

Im **Prozesskern** erklärt eine zusätzliche Tour in fünf Schritten den direkten
markierten E₈-Gitteraufbau, den identischen Zeitgenerator der alten und neuen
Zerlegungen, die gemeinsame Rekursion `W5 tensor W4`, verbundene Hypergraphantworten
und die verbleibende physische 3+1-Abbildung. Auf der Hypergraphseite lassen sich
alle ursprünglichen 24 Felder und ihre Adjungierten einsetzen und ihre rationalen
Positionen verändern; die Antwort wird tatsächlich neu berechnet.

`source_program.py` stellt die vollständige affine Ward-Regel für beliebige
endliche Stromwörter bereit. Die ursprüngliche Chevalley-Klammer behält sämtliche
Zwischenströme; das Programm ersetzt die Quelle weder durch Gaußpaarungen noch
durch einen isolierten Blockencoder. `connected_source_word` berechnet den
verbundenen Koeffizienten durch exakte endliche Teilmengenrekursion:

```python
from tfpt_explorer.source_program import connected_source_word

word = [{"kind": "X", "i": i, "a": a, "dagger": d}
        for i, a, d in [(0, 0, False), (1, 0, True), (1, 1, False),
                        (2, 1, True), (2, 2, False), (0, 2, True)]]
answer = connected_source_word(word, [-5, -2, -1, 1, 3, 7])
assert answer["value_exact"] == answer["connected_value_exact"] == "1/576"
```

Alle 62 nichtleeren echten Teilgruppen dieses Beispiels tragen nichtnull E₈-Ladung;
ihre Antworten verschwinden identisch. Die symbolische volle Sechspunktformel ist
ebenfalls geprüft. Das ist ein verbundener Antwortkoeffizient, kein zusätzlicher
Sechskörper-Hamiltonterm. Positionen sind Argumente desselben Quellenfunktionals.
Der lokale HTTP-Aufruf `POST /api/source-word` erhält `word` und `positions`; für
interaktive Antwortzeiten ist er auf acht Einsetzungen begrenzt. Die allgemeine
Python-Funktion hat diese Obergrenze nicht.

`source_unification.py` berechnet aus den Originalwurzeln die volle A₈-Unteralgebra,
die Gittererweiterung `E8/A8 = Z3`, ihre 72+84+84 Wurzelklassen sowie die C₄-Zuordnung
zu Λ₆. Orthogonale Projektoren auf denselben acht Heisenbergströmen beweisen
`T_E8 = T_A8 = T_A4 + T_A3 + T_u1 = T_D5 + T_A3`. Die gemeinsame Zeit folgt somit
aus demselben Virasorovektor. Der zusätzliche u(1)-Strom ist zur P2-Hyperladung
orthogonal; die Z₃-Erweiterung wird nicht mit der Familienmarkierung identifiziert.

Der direkte Gitter-VOA-Weg ist bereits ein Originalweg im Repository. FE-GEN und
ALG-EXH bleiben Verpflichtungen der besonderen CAR-Skalierungsrealisierung; sie
sind keine Voraussetzung jeder direkten Gitterquantisierung. Die zusätzliche
Herkunftshypothese lautet, dass die physische TFPT-Quelle gerade diese minimale
positive lokale Level-1-Vakuumquantisierung des markierten Ladungsgitters ist.
Die physische 3+1-Abbildung einschließlich chiraler Felder, Zustand und Zeit sowie
eines gemeinsamen Antwortfunktionals für alle Transfers bleibt gesondert zu
beweisen. Die bestehenden bedingten Existenzsätze für thermodynamische Dynamik
der angegebenen quasilokalen Hamiltonklasse werden dadurch nicht zurückgenommen.

## Lean direkt nutzen

```sh
python3 -m tfpt_explorer.lean_bridge             # Quelleninventar
python3 -m tfpt_explorer.lean_bridge --run       # Build und native Ausführung
```

Die Brücke erzeugt Import-/Ausführungsdateien unter `runtime/`. Dabei wird keine
Lean-Definition in Python nacherzählt: Lean kompiliert die originale Definition.
Der erste explizite Quercheck betrifft die Ankerleiter und ihre Ausgaben 240, 8,
248. Die automatische Erschließung probiert geeignete Nat-Konstanten und
Nat→Nat-Funktionen mit Eingaben 0 bis 8. Nur wirklich ausgeführte Aufrufe erhalten
den Status `executed`. Definitionsköpfe mit weiteren impliziten Voraussetzungen
bleiben `requires_adapter` und behalten das Lean-Diagnoseprotokoll.

Ein Beweis in `Prop` ist keine Simulationsregel. `noncomputable`, Axiome und
`sorry`-Stellen werden erfasst; der Build eines bedingten Satzes wird nicht als
Beweis seiner Voraussetzungen gewertet. `TfptCarrier.CIRoot` ist der im Projekt
vorgesehene Kern ohne die sehr großen WallLadder-Rung-Zertifikate. Diese werden
nicht durch den Brückenknopf erneut gebaut. Auch `lake build RH` ist kein
RH-Beweis. Einzelheiten zur Kompilierung:
[Lean-Referenz](https://lean-lang.org/doc/reference/latest/Elaboration-and-Compilation/).

## Prüfung und reproduzierbarer Export

```sh
python3 -m pytest -q tfpt_explorer/tests
python3 -m tfpt_explorer --export tfpt_explorer/runtime/snapshot.json
```

Die vollständige bestehende Python-Suite wird mit ihrem originalen Runner
`python3 -B verification/run_all.py` ausgeführt. Die strukturierten Ergebnisse
und ungekürzten Protokolle liegen in `runtime/`; ein registriertes Modul zählt
erst nach seinem tatsächlichen Abschluss als frisch geprüft. Unterbrochene,
fehlgeschlagene und noch nicht ausgeführte Arbeiten bleiben unterscheidbar.

Ein unterbrochener Gesamtlauf kann ohne Wiederholung abgeschlossener Module
fortgesetzt werden:

```sh
python3 -u tfpt_explorer/verification_runner.py
python3 tfpt_explorer/verification_runner.py --status
```

Der Runner erlaubt jeweils nur einen Supervisor und einen Arbeiter. Der hier
mitgelieferte Launchd-Aufruf ist ein temporärer Einmallauf: Die Plist liegt nur
unter `runtime/`, hat weder `KeepAlive` noch `RunAtLoad`, und die Registrierung
wird nach einem terminalen Ergebnis entfernt. Vom Lauf veränderte Ergebnis-JSONs
werden als Beleg nach `runtime/verification_generated_artifacts/` kopiert; der
Runner schreibt diese Originaldateien nicht zurück und setzt sie nicht zurück.

`runtime/` ist ignoriert und wird nicht als Paper- oder Ledgerpromotion behandelt.
Die Anwendung verändert keine Paper, keine Beweisstatus und keine experimentelle
Scorecard. Die JSON-Ausgabe dokumentiert die gewählte Konfiguration, die
berechneten Werte, ihre Quellen und den Zeitpunkt des Laufs.

## Forschungsfortsetzung: Auswahl, Felder und vollständiger Geschichtskern

Die folgenden APIs ergänzen den Rechenkern; der ältere 316er-Schnappschuss und
die Browser-Tour enthalten diese Fortsetzung noch nicht automatisch.

`source_selection.py` berechnet den affinen Vierstromtensor bei beliebigem
positiven ganzzahligen Level. Sein gemischtes Verhältnis ist `1/k`, während
die normierte Fünferrekursion denselben Levelunterschied nicht sieht.
`root_power_norm(k, 2) = 2*k*(k-1)` und die neutrale Restnorm
`120*(k-1)/(k+30)` geben zwei weitere genaue Selektoren. Diese Rechnungen
setzen tatsächliche unitäre affine Felder voraus. Eine aus Level eins
abgeleitete Antwort darf nicht als unabhängiger Ursprung für Level eins dienen.

`source_realization.py` verbindet die ursprünglichen X-Felder mit den
SU9-Matrixströmen `:psi_dagger_(5+a) psi_i:`. Ein unabhängiger elementarer
Fermion-Wick-Auswerter reproduziert die verbundene Sechserantwort `1/576`.
Die C-Felder benötigen die vorhandene geladene Z3-Erweiterung. Für **alle
endlichen C/X-Wurzelwörter** wertet `evaluate_lattice_word` das ursprüngliche
Gittervertexprodukt einschließlich Kokzyklus aus. Der Achtfeldzeuge
`C0 C1 C2 X00 X11 X22 X33 X43` hat bei `0,...,7` den Wert `-1/4032000`;
gewöhnliches Vakuum-Wick ohne die Erweiterung würde hier fälschlich null liefern.

```python
from tfpt_explorer.source_realization import (
    evaluate_lattice_word, evaluate_x_fermion_word,
    source_history_features, source_history_kernel, current_mobius_profile,
)

x = {"kind": "X", "i": 0, "a": 0}
xd = dict(x, dagger=True)
assert evaluate_lattice_word([x, xd], [0, 2]) == 1 / 4

# Gesamtladung, Amplitude und acht rationale Funktionen für ALLE Moden.
state = source_history_features([x], ["1/2"])
assert state["norm_squared"] == "16/9"

# Echter Hilbertkernel, unabhängig über radial adjungierte Ward-Wörter geprüft.
overlap = source_history_kernel([x], ["1/2"], [x], ["1/3"])

# r=tanh(s/2): exakte Modengewichte und nicht abgeschnittener Rest.
time_state = current_mobius_profile("1/2", displayed_grades=4)
assert time_state["survival_amplitude"] == "3/4"
```

Geschichtenpositionen sind reell-rational mit `1 > |z1| > ... > |zn| >= 0`.
Diese Daten bestimmen den unnormierten radialen Wurzelfeldzustand samt allen
Nachfahren. Sie sind keine Detektorwahrscheinlichkeiten und keine universell
begrenzte Speicherarchitektur; Polzahl und Zahlengröße können wachsen.
Die Möbiusentwicklung ist intrinsische geometrische Zeit und behandelt alle
internen Stromrichtungen gleich. Sie ist noch nicht die hergeleitete Laborzeit
oder ein Flavor-Massenspektrum. Die neun Hilfsfermionen sind keine neun
abgeleiteten Standardmodellteilchen.

Gezielte Reproduktion:

```sh
python3 -m pytest -q tfpt_explorer/tests/test_source_selection.py tfpt_explorer/tests/test_source_realization.py tfpt_explorer/tests/test_source_program.py
python3 -m tfpt_explorer.source_selection > tfpt_explorer/runtime/source_selection.json
python3 -m tfpt_explorer.source_realization > tfpt_explorer/runtime/source_realization.json
```

Der damalige gezielte Lauf umfasste 45 bestandene Tests; darunter sind die tatsächlichen
8000 X-Tripelklammern, 1152 vierstellige C/X-Ward-Vergleiche, die geladenen
Sechser-/Achterzeugen, der positive Kernel und die symbolische
Möbius-Generatorgleichung sowie die folgenden neuen Verbindungen.
Er ersetzt keinen erneuten Gesamtlauf der Originale.

### Originalträger und Replica-Antwort (29. September)

`native_spin_anomaly(m)` in `source_selection.py` berechnet für die ursprünglichen
gemeinsamen Lifts mit vier ganzen Einträgen und Summe −2 den globalen
Spin-Träger `E_R + Fix(Lambda² F)`. Seine Klasse ist
`lambda = d*c1(E)^2 - c2(E)`, `d = sum(m_j²)/2`. Unter der ausdrücklich
benannten tatsächlichen chiralen Dirac-/Pfaffian-Realisierung kommt
`-p1(T)/3` hinzu. Die P2-Restriktion liefert `5/12`, das Verhältnis `5/4`
gilt nur in der ursprünglichen Y-Normierung. Der Determinantenkreislevel ist
stets gerade und mindestens zwei; er ist nicht der einzelne Pump-eins-Kanal.
Der Test berechnet die 16 tatsächlichen komplexifizierten Gewichte mit freien
symbolischen Liftparametern, nicht nur ausgewählte Zahlenbeispiele.

`two_interval_replica_response(x)` in `source_realization.py` verwendet dieselbe
chirale E8-Vakuumquelle und exakt rationale Kreuzratios `0 < x < 1`.
Für die ursprünglichen Quadratmarken gilt `x=1/2`. Die Zweifach-Überlagerung
liefert `F2=1-x+x²`, `R2=F2/(1-x)`, somit `R2=3/2` und `I2=log(3/2)`.
Eine unabhängige Kontrolle benutzt elliptische Perioden, Eisenstein-q-Reihe
und Dedekind-Produkt; eine feste NS-NS-Fermionquelle prüft die Normierung.

Der echte Replica-Twist ist ein affines E8_2-Singulett/Ising-Fermion.
Seine signierten Vierpunktbeiträge ergeben am Quadrat `2/3, -1/3, 2/3`.
Das sind Beiträge zu **einem** Fusionsblock, keine drei Populationen oder
Wahrscheinlichkeiten. `6*I2` stimmt skalar mit der alten Clocklücke überein;
der Transferoperator und seine sechs Kompositionen sind dadurch nicht abgeleitet.
Der API-Wert ist eine normierte Twist-Ratio, nicht das vollständige
Zweiintervall-Modularspektrum. Beide neuen Ergebnisse stehen in den bestehenden
JSON-Buildern; die Browser-Tour übernimmt diese Ergänzungen nicht automatisch.

### Replica-Paarungen, native Clockoperation und Ereignisrecord

`replica_pairing_readout(x)` benutzt die ganze reale Familie der tatsächlichen
Wick-Beiträge `(1/x, 1/(1-x), -1)`. Ihre quadrierten Beträge sind bereits auf
das Quadrat ihrer Summe normiert. Mit der komplementären nativen Reflexion
pro Paarung und einer nichtselektiven Spektralmessung entsteht
`B(x)=I-L(x)/(2*G(x)^2)`. Am Quadrat ist das exakt die alte Matrix
`[[13,1,4],[1,13,4],[4,4,10]]/18`, ohne eingesetzten Clockeigenwert.
Die Messregel und die Paarungs-/Reflexionszuordnung bleiben erklärtes
Instrument, keine aus P1/P2 abgeleitete Auswahl.

`replica_luders_action(X,x)` in `marked_source_process.py` führt diese Operation
auf den tatsächlichen markierten Quellreflexionen aus. Am Quadrat ist sie
genau der vorhandene Punkt `q=0` der nativen Prozessfamilie; sie liefert
`FAAF=0`, während die zusätzliche historische Quellenbedingung `1/27`
den Punkt `q=1/3` verlangen würde. Die drei Trine-Effekte kommutieren nicht:
Ihre Erwartungen folgen B, ihre wirklich wiederholt gemessenen Ausgänge
folgen `QB` mit `Q=I/2+J/6`.

`replica_recorded_events(X,x)` realisiert denselben reduzierten Kanal durch
ein anderes Instrument: angewendete native Reflexionen mit klassisch
gespeichertem Ereignislabel. Damit ist die kontrollierte Rückführung des
Eingangszustands auf der markierten C2 exakt möglich. Bereits die Korrelation
mit Ereignisparität erhält die im gemittelten Readout verlorene G-Antwort.
Dagegen verlieren die klassischen rank-eins-Lüdersausgänge diese Antwort.
Gleiche reduzierte Matrix und gleicher Kanal identifizieren somit noch
nicht das ganze Instrument oder seine Zukunftsantworten.

Der aktualisierte gezielte Lauf besteht **58 Tests**:

```sh
python3 -m pytest -q tfpt_explorer/tests/test_source_selection.py tfpt_explorer/tests/test_source_realization.py tfpt_explorer/tests/test_source_program.py tfpt_explorer/tests/test_marked_source_process.py
```

Enthalten sind symbolische Norm- und Gegenidentitäten, eine unabhängige
Permutationsmischung, die nativen Krausoperatoren, wirkliche wiederholte
Messausgänge, der höhere Quellworttest und die exakte Recovery eines
allgemeinen symbolischen 2×2-Eingangs. Die neuen Ergebnisse stehen im
bestehenden `runtime/source_realization.json`; die ältere Browser-Tour
enthält diese neue Instrumentprüfung noch nicht.

### Anker, markierte Viertelphase und vollständige Ladungsfasern

`anchor_clock_readout(x)` führt beide Clockwege für die ganze reale
Vierpunktfamilie zusammen. Mit `f=1-x+x²` und
`v=(x,1-x,1)/sqrt(2f)` ergibt `U=I+(i-1)vv*` exakt
`abs(U_ij)²=B_ij(x)` aus der vorhandenen Replica-Paarungsrechnung.
Am Quadrat ist v der normierte ursprüngliche Anker (1,1,2).
Der tatsächliche markierte Quellencharakter wird aus den originalen
C-Wurzeln berechnet: `T_C=-diag(1,1,i,-i)`. Die Funktion gibt den expliziten
Intertwiner zur gewählten orthogonalen Dreierbasis mit aus. Die ursprüngliche
Auswahl dieser Detektorbasis ist weiterhin offen.

`anchor_clock_channel(X,x)` implementiert die erklärte Dephasierung vor und
nach U. Die kohärente Geschichte kehrt nach vier Schritten vollständig
zurück; die wiederholt dephasierte Geschichte liefert beim ersten Ausgang
die Rückkehr 211/486. Der gesamte rationale Gedächtniskern ist gegen den
Schurkomplement-Ausdruck der tatsächlichen 9×9-Operatorwirkung geprüft.

`native_trine_dilation()` in `marked_source_process.py` gibt die genaue
orthogonale Dreier-Erweiterung der älteren nativen C2-Trine an.
Nach einer Projektivmessung gehen bei Rückprojektion in die C2 nur 2/3
der Spur ein; die normierte Rückpräparation erklärt die zusätzliche Matrix Q.
Das ist eine Effektabbildung, kein Intertwiner der ganzen E8-Clockwirkung:
Die ursprünglichen Cartan-Stromzustände und die C-Wurzelstromzustände haben
verschiedene T-Wirkungen.

`family_charge_fibre()` erhält die Quelle in der exakten Gradingdarstellung
E8/D5=A3*. Der vierfache getrennte C-Weg ist im projizierten Dreiergitter
geschlossen, besitzt aber vollständige Ladung (-2,-2,-2,-2,-2;0,0,0),
Mindestgrad10, positive Norm und verschwindenden Vakuumüberlapp.
T und L0 erhalten die projizierte Koordinate. Der Quotient allein liefert
deshalb weder eine ausgewählte räumliche Bewegung noch eine lokale
relativistische Algebraordnung.

`affine_sewing_exclusion()` in `source_selection.py` zertifiziert für sämtliche
affinen Vakuumlevel k≥2 die rationale Schranke
`R_chi>114161/72900>3/2`. Der einzelne Vakuumblock und eine vollständige
positive linke/rechte Sektorsumme sind ausdrücklich unterschieden.
Der Selektor benötigt eine unabhängige Antwort des ursprünglichen Prozesses.

Der aktuelle gemeinsame Lauf der vier oben genannten Testdateien besteht
**67 Tests**. Die bestehenden JSON-Ausgaben wurden entsprechend erneuert;
der native Trine-Anschluss liegt zusätzlich in
`runtime/marked_source_process.json`. Die Browser-Tour wird durch diese
Dokumentations- und Rechenkernfortsetzung nicht automatisch aktualisiert.

### Gemeinsame Zeit und quelltreuer räumlicher Anschluss

Die Fortsetzung zum Anhang `f548f0d4-2ae2-4067-8f27-3b19b7c82ae4` verwendet
weiterhin dieselben tatsächlichen Quellenreflexionen. `shared_native_action`
wendet dasselbe native Ereignis auf alle Register an;
`shared_native_record_isometry` erhält den Ereignisrecord;
`native_word_distribution` berechnet alle ganzzahligen Faltungspotenzen.
Die Formeln gelten ohne Zwischeneingriffe und bei erneut gezogenen Ereignissen.

`shared_native_process_data` zeigt den Choi-Rangsprung 5→6 am historischen
q=1/3, die Bell-Rückkehr 1 gegenüber5/12 bei unabhängigen Ereignissen und den
negativen Choi-Zeugen der Hauptquadratwurzel. Darüber hinaus ist die ganze
hierarchische zeitunabhängige GKLS-Klasse exakt entschieden: 2/9≤q≤1/4.
Der allgemeine Beweis benutzt den Fixzustandssimplex und die einfachen Spektren
der neun Sektor-Hom-Blöcke des Zweiregisterkanals; er setzt den hypothetischen
Generator nicht schon als reversible Gruppenmischung an. Die Tests prüfen
diese algebraischen Prämissen; der allgemeine Beweis steht in der bestehenden
Gesamtsynthese, Abschnitt `sec:sharedtime`.

Diese Ereignisse sind gemeinsame klassische Zufälligkeit: Die lokale
Heisenberg-Algebra bleibt in jedem Register. Sie übertragen keine Intervention
zwischen Registern und erzeugen aus Produktzuständen keine Verschränkung.
Eine vollständige wechselwirkende Quelle wird dadurch nicht implementiert.

`native_walk_lift_obstruction` prüft die im Anhang vorgeschlagene Weylbewegung.
Gewöhnliche projizierte Shifts liefern einen unitären Lauf. Die unmittelbare
Ersetzung durch die vollständigen ursprünglichen C-Ladungsfaktoren samt
Kokzyklus und Feldphasen verletzt dagegen Unitarität. Ein genauer Restshift
mit physischer Ladung (0,0,0,0,0;0,1,1) hat Koeffizient [[0,0],[1/2,0]].
Die Faktoren sind ausdrücklich nicht die vollständigen Vertexfelder.

Die Quelle besitzt selbst lokalen chiralen Transport: Der dokumentierte
Strompuls W(εf)Ω liefert unter dem vorhandenen L0 exakt die spätere Antwort
ε σ(f,g_t) und Energie ε²/(4π)∫(f′)². Dieser allgemeine Quellenbefund wurde
analytisch abgeleitet; eine lokale Funktion wurde dafür nicht durch endliches
Fourierabschneiden ersetzt. Dies ist keine abgeleitete 3+1D-Welt oder Auswahl
des ursprünglichen Instruments. Simultane vakuumerhaltende Symmetrieantworten
können keine Ereignisgewichte auswählen; zeitlich eingefügte Eingriffe können
sie unterscheiden.

Der aktuelle gezielte Lauf derselben vier Testdateien besteht **75 Tests**.
Die gleiche Zahl eines im Anhang nur verlinkten externen Prüfpakets bezeichnet
eine andere, nicht mitgelieferte Testmenge. Die beiden bestehenden JSON-Dateien
`runtime/source_realization.json` und `runtime/marked_source_process.json`
enthalten die neuen Ergebnisse. Kein neuer Lean-Beweis wird behauptet.

### Konstruktiver Rückweg zur markierten Fermionenquelle

`source_realization.reconstruct_marked_fermion_source()` rekonstruiert aus den
ursprünglichen Glue-Klassen das D8-Unterobjekt. Dessen eindeutig fermionischer
Vektorsektor erweitert D8 zum ungeraden Gitter Z8, also zu 16 Majoranafeldern
mit ursprünglicher (10,1)+(1,6)-Wirkung. Der markierte Spinorsektor wird behalten;
seine bosonische Erweiterung ergibt wieder die ursprüngliche E8-Quelle.
Die Hilberträume H0+Hv und H0+Hs sind ausdrücklich unterschieden.

Der ursprüngliche duale Glue-Charakter ist auf den zehn Fünferseitenfeldern
ein Vorzeichenwechsel. Sein Spin-Lift hat Ordnung vier auf den ursprünglichen
Spinorfeldern. Geometrische Vierteldrehung, interner Glue-Charakter und
diagonaler Quotientsgenerator werden nicht gleichgesetzt.

Die zwei neuen Tests prüfen alle ursprünglichen Wurzelklammern gegen die
Glue-Graduierung, die tatsächliche Vektor- und P2-Wirkung sowie unabhängig
fermionische und bosonische Charaktere und den markierten E8-Rückweg.
Der gemeinsame Lauf der vier bisherigen Quellen-Testdateien besteht jetzt
**77 Tests**; nach Präzisierung des Glue-Lifts bestanden die zwei neuen Tests
erneut. Diese Mengen werden nicht addiert. Die bestehende JSON-Datei
`runtime/source_realization.json` enthält `inverse_marked_fermion_source`.

Der allgemeine lokale Rekonstruktionssatz steht in der bestehenden
Gesamtsynthese, Abschnitt `sec:inverseorigin`: 16 erzeugende, reelle, graduierte
lokale Primärfelder mit Gewicht 1/2 und eindeutigem positivem Vakuum bestimmen
CAR, Zustand, höhere Antworten und Konformalzeit gemeinsam. Der Beweis wurde
unabhängig gegengelesen. Die Rückkonstruktion gilt innerhalb der ausgewählten
markierten konformen Quelle. Ihre ursprüngliche P1/P2-Herkunft, der reale
Messprozess und eine 3+1D-Realisierung sind damit nicht behauptet.
