# Nachtrag A: Was am neuen v1.6.3-Erklärtext wirklich neu ist

## Urteil

**Ja, ein belastbarer neuer Rechenschritt ist enthalten:** Die zuvor fehlende
Norm ν5 liegt jetzt mit passendem Quellstand vor. Wir haben ν1 bis ν5 frisch
durch die ursprüngliche exakte Spurnetzwerkrechnung reproduziert und daraus
unabhängig strengere rationale Ritzgrenzen gewonnen. Die übrigen großen
Aussagen des Textes sind teils bereits bekannt, teils durch v1.6.7 korrigiert.
Besonders problematisch ist die Vermischung verschiedener Ritz-Zustände
zu einem vermeintlich vollständig bestimmten Grundzustand.

Die gesamte neue Anlage wurde gelesen. Sie stimmt mit der derzeitigen
`EINFACH_ERKLAERT.md` im Ordner
`/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/`
überein. Alle für den neuen Nachweis verwendeten Programme und Ergebnisse
sind separat unter `late_a/inputs/` eingefroren. Die vorhandenen v1.6.7- und
Mechanismus-Snapshots wurden nicht verändert.

## 1. ν5 ist jetzt ein Ergebnis, nicht mehr nur eine Programmeinstellung

Der v1.6.7-Snapshot hatte zu Recht festgehalten, dass damals
`norms_by_traces.json` und ein abgeschlossener zugehöriger Replay fehlten.
Dieser konkrete Quellenstand hat sich geändert. Der neue Checkerhash
`be72c728e128ae0ef605980a5bae88ea31049e29e2fd17c43167fbd6ad1d0c89`
passt jetzt zum Ergebnis; auch der Common-Hash stimmt. Die vorhandenen
normalen und optimierten Normausgaben sind byteidentisch. Der gespeicherte
JSON-Inhalt ist identisch; nur ein abschließender Zeilenumbruch unterscheidet
die Druckausgabe von der geschriebenen Datei.

Zusätzlich zu dieser Quellenprüfung wurde die wirkliche Rechnung in unserem
isolierten Paket normal und mit `-OO` frisch ausgeführt. Geändert wurde nur
der Tensorpfad auf das eingefrorene Originalarchiv; der eigentliche
Spurnetzwerkcode blieb unverändert. Ergebnis:

\[
(\nu_0,\nu_1,\nu_2,\nu_3,\nu_4,\nu_5)=
(1,480,439680,575078400,952296652800,1866738327552000).
\]

Die fünfte Norm benötigt 840 Wick-Netzwerke, die auf 93 Klassen unter
vorzeichenfreien Graphsymmetrien reduziert werden. Jede tatsächlich
ausgewertete Kontraktion benutzt dünnbesetzte Dictionaries und beliebig
große Python-Ganzzahlen. Hier wurde keine Float-Kontraktion oder Rundung
als exakte fünfte Norm ausgegeben.

Die Methode hat einen nachvollziehbaren Ursprung: Für die antisymmetrische
Paarmatrix M(z) liefert die fermionische Exponentialnorm
\(\det(I+M(z)^\dagger M(z))^{1/2}\). Nach Logarithmusentwicklung und
bosonischer Gaußintegration entstehen die im Quellcode benutzten
Spurzyklen, rationalen Faktoren und Wick-Permutationen. Die signierte
Φ-Kontraktion ist deshalb eine Normberechnung desselben Paartensors.

**Reproduktionsgrenze:** Das ist ein frischer Replay der geprüften
ursprünglichen Methode, keine zweite unabhängig neu erfundene Methode für
ν5. Die früheren ν1–ν4-Werte liefern unabhängige bekannte Vergleichspunkte.
Die Quelle vergleicht außerdem 39 kanonische Netzwerke nur bis n=4 mit
ihrem anderen dichten Pfad; daraus folgt kein zweiter n=5-Beweis. Der
Hilfsname `brute_force_nu2` ist irreführend: Sein Aufbau lässt explizite
CAR-Umordnungszeichen aus. Dieser Helfer wurde nicht als tragender
unabhängiger Normnachweis benutzt. Die signierten Spurnetzwerke bleiben
davon getrennt.

Das Gesamt-Replaymanifest der fremden Suite stand beim Einfrieren weiterhin
auf **RUNNING** mit leerer Laufübersicht. Wir erklären damit nicht die ganze
fremde Suite für abgeschlossen. Unser isolierter Norm-/Ritznachweis ist
hingegen abgeschlossen und reproduziert.

## 2. −1,138 ist eine echte bessere Variationsgrenze

Die Unterräume aus den normierten bosonweise geordneten Vektoren
\(v_k=T_+^kF\) sind nicht invariant, aber sie sind gültige Variationsräume.
Da unterschiedliche k orthogonal sind und H die Bosonzahl höchstens um
eins ändert, besitzt die Kompression auf v0,…,v5 exakt

\[
(H_6)_{kk}=k\Delta,\qquad
(H_6)_{k,k+1}=g\sqrt{\nu_{k+1}/\nu_k}.
\]

Aus der jetzt frisch geprüften ν5 wurde die charakteristische Gleichung
dieser **sechsdimensionalen reinen Leiterkompression** neu mit rationaler
Arithmetik aufgebaut. Eine unabhängige Sturm-Zählung beweist bei
g/Δ=1/20:

\[
\boxed{-1.13847420<E_{6}/\Delta<-1.13847419.}
\]

Die optional zusätzlich enthaltene Richtung w2 ergibt einen siebendimensionalen
Variationsraum. Ihre Norm ist weiterhin \(5001523200/229\). Ihre einzige
Kopplung innerhalb dieses Raums führt zu v3:

\[
\langle\widehat w_2,H\widehat v_3\rangle
=g\sqrt{\|w_2\|^2/\nu_3}.
\]

Die v1-Kopplung verschwindet durch w2⊥v2; alle anderen verschwinden schon
wegen der Bosonzahl. Der diagonale Wert ist 2Δ. Damit ist auch diese
Kompression vollständig bestimmt, ohne eine Schließung zu behaupten.
Ihre unabhängige rationale Wurzeleinschließung lautet

\[
\boxed{-1.13847610<E_{7}/\Delta<-1.13847609.}
\]

Nach Rayleigh–Ritz folgt die neue strenge Obergrenze

\[
\boxed{E_0<-1.13847609\Delta.}
\]

Die frühere Grundzustandsuntergrenze −1,158089Δ bleibt ein ausdrücklich
übernommener älterer exakter Eingang. Ebenso wird der ältere N=63-Floor
\(E_h>-1.121899\Delta\) übernommen. Zusammen ergibt sich neu

\[
\boxed{\epsilon=E_h-E_0>0.01657709\Delta.}
\]

Schon die reine Sechserkompression liefert ε>0,01657519Δ. Der Siebenerwert
ist etwas stärker; beide verbessern den v1.6.7-Floor 0,00773911Δ erheblich.
Der ältere N=63-Beweis und das große Grundzustandsarchiv wurden dabei nicht
erneut ausgeführt. Die neue Folgerung hängt ausdrücklich von diesem
beibehaltenen exakten Floor ab.

**Entscheidende Unterscheidung:** H6/H7 sind keine sechste oder siebte
Fortsetzung der in v1.6.7 berechneten vollständigen H-Lanczos-Kette. Schon
deren fünfter Vektor enthält v4+w2. Die Leiterkompression ist dennoch eine
gültige Ritzrechnung und darf deshalb ihre Energieobergrenze verbessern.
Ein kleines lokales Nichtschlussverhältnis oder eine flacher werdende
Ritzfolge beweist keine Konvergenz zum wahren Grundzustand. Die Behauptung
„nur sehr nahe an mit fünf Zahlen lösbar“ bleibt unbegründet.

## 3. Der Text vermischt drei verschiedene Näherungszustände

Die neuen kleinen Matrizen wurden unabhängig diagonalisiert. Sie bestätigen
die gespeicherten numerischen Ritz-Erwartungswerte, aber nicht deren
Umdeutung zu exakten Eigenschaften von Ω.

| Größe | Fünferbasis v0,…,v3,w2 | Sechserbasis v0,…,v5 | Siebenerbasis zusätzlich w2 |
|---|---:|---:|---:|
| Ritzenergie/Δ | −1,0942318710 | −1,1384741999 | −1,1384760929 |
| ⟨Nb⟩ | 0,8421158543 | 1,0177373262 | 1,0177445059 |
| Gewicht für Addition | 0,02631612045 | 0,03180429144 | 0,03180451581 |
| Gewicht für Entnahme | 0,97368387955 | 0,96819570856 | 0,96819548419 |
| Quadrat der F-Überlappung | hier nicht benötigt | 0,3498924448 | 0,3498903640 |
| Shannon-Entropie der Bosonzahl | hier nicht benötigt | 1,8712372972 Bit | 1,8712435534 Bit |

Die Werte **0,974/0,026 und 0,03Δ/1,15Δ gehören ausdrücklich zur kleineren
Fünferbasis**, wie `compute_charged_response` ab Zeile 900 und das Feld
`charged_response.basis` zeigen. Die höhere Norm allein macht diese
expliziten Vielteilchenvektoren nicht länger; die Funktion setzt Kc=min(3,Kmax).

Für einen G-Singulettzustand im N=64-Sektor gelten die exakten Summenregeln

\[
Z_\mathrm{add}=\langle N_b\rangle/32,\qquad
Z_\mathrm{rem}=1-\langle N_b\rangle/32.
\]

Damit sind die verschiedenen Tabellenwerte unmittelbar nachrechenbar.
Die Summe eins ist die CAR-Summenregel für das gesamte spektrale Gewicht;
sie bestimmt keine einzelne Spektrallinie und liefert noch kein natives
Präparations- oder Messinstrument. Der kleine Näherungswert Zadd≈0,026316
liegt sogar unter dem früheren exakten Ω-Floor
0,842846/32=0,0263389375. Er kann daher nicht als derselbe exakte
Grundzustandswert übernommen werden.

Die Shannon-Entropie der Bosonzahl ist wegen der verschiedenen Lochzahlen
eine Untergrenze für die Boson/Fermion-Verschränkungsentropie **dieses
jeweiligen reinen Ritz-Zustands**. Der Zahlenwert 1,87 Bit ist keine hier
bewiesene Untergrenze für den wahren nativen Grundzustand. Das gilt genauso
für die 35-Prozent-Überlappung.

### Die mittleren Antwortenergien lassen sich ohne riesige Zustandsdateien korrigieren

Aus den CAR folgen für jeden normierten G-Singulettzustand mit N=64:

\[
\begin{aligned}
\sum_r\langle f_r^\dagger Hf_r\rangle
&=\Delta(64\langle N_b\rangle-2\langle N_b^2\rangle)
+2g\operatorname{Re}\langle T_+(62-2N_b)\rangle,\\
\sum_r\langle f_rHf_r^\dagger\rangle
&=2\Delta\langle N_b^2\rangle
+2g\operatorname{Re}\langle T_+(2N_b)\rangle.
\end{aligned}
\]

Dabei folgt die erste Identität aus
Σf†T+f=T+(Nf−2) und Σf†T−f=T−Nf; die zweite aus den entsprechenden
CAR-Identitäten für f…f†. Die G-Invarianz macht alle 64 Modenantworten
gleich. Nb und die benötigten T+-Matrixelemente sind bereits in den
kleinen Ritzkompressionen enthalten.

Die separate kleine Rechnung `late_a/moment_audit.py` reproduziert so die
gespeicherten Fünferwerte 0,03107315818Δ und 1,14969200224Δ ohne Millionen
Besetzungsamplituden. Für den **Siebener-Ritz-Zustand** ergibt dieselbe
Rechnung stattdessen die mittleren Kosten

\[
\overline\epsilon_{\rm rem}\approx0.03479766990\Delta,\qquad
\overline\epsilon_{\rm add}\approx1.05931330814\Delta.
\]

Das korrigiert die Basisverwechslung und ist eine nützliche kleine
Ausleserechnung. Es sind numerische erste Momente eines Variationszustands,
keine neu bewiesenen Ω-Polenergien. Sie dürfen insbesondere nicht mit der
strengen unteren Entnahmeliniengrenze aus Abschnitt 2 gleichgesetzt werden.

## 4. Was bereits überholt ist

| Aussage der Anlage | Prüfung |
|---|---|
| Clock sei ein äußerer Handgriff, weil er Gewichte verschiebt | Bereits in v1.6.6/7 durch das explizite Spin(10)-Wort widerlegt. Nichtskalare Wirkung innerhalb eines Irreps bedeutet keine äußere Symmetrie. Die aktuelle Mechanismusprüfung reproduziert zudem den ursprünglichen Clock und seinen passiven Focklift. |
| Mit allen gewährten inneren Kontrollen bleiben im N=3-Sektor sieben Kommutantparameter | Bekannte bedingte Algebraaussage; beweist keine physische Verfügbarkeit dieser Griffe. Die Milliardenangaben sind Algebradimensionen, keine Zahl physischer Orte. |
| Auf der zweiten Bosonstufe gibt es einen zweiten Zustand | Richtig, aber unvollständig: v1.6.7 hat bereits genau vier Singulett-Richtungen und ihre vollständige Projektion berechnet. |
| Der N=64-Grundzustand sei bei g/Δ=1/20 nun wieder grundsätzlich offen | Die hier benutzten groben Konkurrenzschranken reichen dort nicht; das widerlegt den früheren stärkeren nativen Satz nicht. Der Quellwert g*≈0,02705688 gehört zu diesem schwächeren, numerisch ausgewerteten Schrankenverfahren. |
| Einheitlicher Vermittler müsse universell ein antisymmetrischer Tensor sein | Der Fünfzyklus ist ein echter bekannter Ausschluss der angegebenen binären Händigkeit auf primitiven Labels. Die Feldschlussfolgerung bleibt an diesen ableitungsfreien, unvergrößerten Ansatz gebunden; kein allgemeines relativistisches Wörterbuch wird klassifiziert. |
| Alle drei fundamentalen Vorfragen seien jetzt exakt beantwortet | Zu stark: Kontrollverfügbarkeit, tatsächliche Ω-Erwartungswerte und ein umfassender relativistischer Feldanschluss bleiben verschieden weit offen. |

## 5. Was daran spannend ist und was als nächstes trägt

Der gute neue Schritt ist **die tatsächlich abgeschlossene fünfte
Spurnetzwerk-Norm mit der daraus folgenden stärkeren strengen Energie- und
Entnahmeschranke**. Hinzu kommt unsere kleine CAR-Auswertung, die die
geladenen ersten Momente auf den richtigen größeren Ritz-Zustand hebt.
Das verbessert nachprüfbar die Rechnung im bestehenden nativen Modell.

Die Grundlage für die fundamentale Fortsetzung bleibt dagegen der gerade
in v1.6.8 präzisierte gemeinsame Prozess: ursprüngliches Operationsalphabet,
getypter Referenzträger, Zustand, gemeinsame Auslesung und überprüfbare
Interferenz. ν5 ersetzt weder den Herkunftsnachweis eines zusätzlichen
Griffs noch den neuen genauen Unterschied zwischen gemeinsamer Referenz-
dynamik und einem isolierten Systemantrieb.

## Reproduktionsbelege

`late_a/verify.py` prüft elf eingefrorene Eingaben, führt die ν1–ν5-
Spurnetzwerke frisch aus und baut beide Ritzpolynome unabhängig neu auf.
Es gibt **46 eigene Prüfbedingungen: 36 exakte beziehungsweise faktische
Prüfungen und 10 numerische Konsistenzprüfungen**, separat dazu 1239
ausgeführte Quellguards der Normkonstruktion. Die Guardzahl zählt keine
unabhängigen mathematischen Theoreme.

Normal/-OO laufen mit Warnungen als Fehler und liefern byteidentische
Ergebnisdateien mit SHA-256
`eaa83083d8232d17772d11f8c7c27015a9fe852162586a545d20d39a203f3471`.
Die zusätzliche Momentkontrolle benötigt nur kleine Matrizen und zwei
Quellenpins; sie führt den großen Norm- oder Grundzustandslauf nicht erneut
aus. Kein fremder Lauf wurde als abgeschlossen umetikettiert.

```sh
python3 -B -W error late_a/verify.py --output late_a/results_normal.json
python3 -OO -B -W error late_a/verify.py --output late_a/results_optimized.json
cmp late_a/results_normal.json late_a/results_optimized.json
python3 -B -W error late_a/moment_audit.py --output late_a/moments_normal.json
python3 -OO -B -W error late_a/moment_audit.py --output late_a/moments_optimized.json
cmp late_a/moments_normal.json late_a/moments_optimized.json
```
