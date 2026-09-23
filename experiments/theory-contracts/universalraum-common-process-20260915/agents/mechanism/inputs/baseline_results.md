# TFPT / Universalraum: die richtige einfache Kette

## Vollständige Konsolidierung v1.6.7 - 15. September 2026

### Ergebnis und Leseschlüssel

Die zuletzt ergänzte Vogelperspektive steht im Teil B dieser Fassung:
**Gesucht wird der kleinste gemeinsame beobachtbare Prozess hinter den
verschiedenen Ansichten.** Ein nativer Rang-60-Kodierer ist bereits vorhanden.
Seine Informationsverluste, die minimalen symmetrieverträglichen Dynamiken
und der Unterschied zwischen Korrelation und kausalem Eingriff wurden neu
berechnet. Das verschiebt die fundamentale Priorität von weiteren lokalen
Näherungswerten zur Herkunft der Operationen und zur gemeinsamen Schattenkarte.

Die neue Runde schließt zwei kleine Strukturfragen vollständig: Der symmetrische
Zustandsraum bei zwei Bosonen hat exakt vier Dimensionen; der bisher unbestimmte
Rest von 4035 bilinearen Komponenten zerfällt vollständig in drei Darstellungen.
Die vier Zustandsrichtungen und ihre Kopplungen wurden zusätzlich am ursprünglichen
Tensor berechnet. Daraus folgt ein vollständiger sechs-dimensionaler Ausschnitt.

Die gewünschte einfache Kette existiert ebenfalls, aber anders als vorgeschlagen:
Man muss den **ganzen Hamiltonoperator** wiederholen, nicht Bosonzahl und
Iterationsnummer gleichsetzen. Die ersten fünf Lanczos-Glieder sind jetzt exakt
bekannt. Sie bestimmen zehn Energiemomente des gefüllten Startzustands und
verschärfen die obere Grundzustandsgrenze geringfügig.

**Das ist keine vollständige TOE.** Insbesondere fehlen die physische Auswahl
des Modellvertrags, ausführbare ursprüngliche Instrumente, derselbe geladene
Transport im gemeinsamen Träger und die relativistische Kontinuumskonstruktion.
Dass die bisherigen Grunddaten dafür noch nicht eindeutig genügen, wird unten
an einer einfachen Familie verschiedener Dynamiken nachgewiesen.

Kennzeichnungen: **exakt** bezeichnet eine bewiesene Aussage im genannten
Modell; **bedingt** eine Aussage mit zusätzlich gewährter Operation oder
bekanntem früherem Satz; **numerisch** eine Näherung; **offen** einen fehlenden
Nachweis. Komplexe Algebradimensionen zählen weder physikalische Raumrichtungen
noch unabhängig hergeleitete Teilchen oder ausführbare Operationen.

Die Fassung baut auf dem vollständigen Hauptdokument v1.6.6 auf. Die aktuelle
Gesamtdarstellung steht voran; die frühere Fassung einschließlich ihrer
Herleitungen, Gegenbeispiele und älteren Anhänge bleibt vollständig erhalten.
Alle sechs in dieser Runde eingesandten Texte werden unverändert dokumentiert und
hier mit überprüften Ergänzungen und ausdrücklich benannten Korrekturen gelesen.

## 1. Das Gesamtbild: Grammatik, Prozess, Zustand, Antwort

TFPTs Compiler beschreibt zunächst eine markierte algebraische Grammatik:
welche Bausteine zusammenpassen, welche Symmetrien gelten und welche Zahlen
innerhalb dieser Konstruktion folgen. Der Universalraum soll diese Grammatik
als einen ausführbaren Prozess realisieren. Der entscheidende Unterschied ist
der zwischen einem erlaubten Zusammenhang und einer tatsächlich erzeugten
physikalischen Entwicklung.

Im hier untersuchten Modell ist die Grundregel weiterhin sehr einfach:
**Zwei Fermionen können in einen Vermittler umgewandelt werden und zurück.**
Mit 64 Fermionmoden und 60 Bosonmoden lautet sie

\[
H=\Delta N_b+g(T_++T_-),\qquad
T_+=\sum_A b_A^\dagger P_A,\quad T_-=T_+^\dagger,
\qquad P_A=\sum_{i<j}W_{A,ij}f_jf_i.
\]

Es gelten \(\Delta>0\), reelles \(g\) und die erhaltene Ladung
\(N=N_f+2N_b\). Der Tensor W besitzt 480 Einträge mit Werten +1 oder -1,
acht disjunkte Paare pro Zeile, und \(WW^\dagger=8I_{60}\).
Seine innere Darstellung ist \((16,4)\) für Fermionen und \((10,6)\)
für Bosonen unter Spin(10) mal SU(4).

Die heutige Beweiskette sieht so aus:

| Verbindung | Was bereits trägt | Was dadurch nicht automatisch folgt |
|---|---|---|
| Compiler zu Paarregel | Konkreter Tensor, Symmetrie und Ladungserhaltung | Physische Wahl von Energie, Kopplung und Instrumenten |
| Paarregel zu Zustand | Früherer eindeutiger Grundzustandssatz im festgelegten Vertrag | Herleitung dieses Vertrags oder dessen Präparation |
| Zustand zu geladener Antwort | Isolierte niedrige Fermion-Entnahmelinie mit hohem Gewicht | Räumlich laufendes relativistisches Teilchen |
| Antwort zu Bewegung | Zusätzliche Links erlauben nachgewiesenen Transfer | Dass derselbe Link aus dem ursprünglichen Operationssatz entsteht |
| Bewegung zu Raumzeit | Prüfprogramm und bedingte Modelle | Gemeinsame 3+1D-Welt, chirales Maß und dynamische Gravitation |

Der endliche dokumentierte Clock gehört zur inneren Spin(10)-Symmetrie.
Er ist damit kein zusätzliches äußeres Symmetrieobjekt. Seine Periode sechs
ist aber auch noch keine Herleitung einer physikalischen Zeiteinheit oder
einer Raumzeit. Innere Spin(10)-Labels sind nicht von selbst Lorentzspin.

## 2. Was die beiden neuen Texte beitragen

### 2.1 Quellenstand und Reproduktionsgrenzen

17 ausgewählte Eingaben wurden mit SHA-256 eingefroren: beide Nutzertexte,
die zugehörigen Programme und Ergebnisdateien, der native Tensor sowie die
vollständige frühere Fassung mit Prüfpaket. Keine fremde Quelldatei wurde
verändert. Die Herkunftsdateien gehören zu parallel fortgeschriebenen
Arbeitsständen; Dateipins sind deshalb wichtiger als Versionsnamen allein.

Der neue Grundzustandslauf war beim ersten Blick noch ohne Ergebnisdatei.
Beim Einfrieren lag bereits sein fertiges Ergebnis vor: **382 Guards,
davon 379 exakt und drei numerisch**. Sein Quellenhash stimmt mit der
eingefrorenen Programmdatei überein. Er findet ebenfalls die Multiplizitäten
1, 1 und 4. Der Zwischenhinweis dieser Prüfung auf eine noch leere Datei
war bei der späteren Übernahme bereits überholt und wird hier korrigiert.

Das Operations-JSON enthält **306**, nicht die im Begleittext genannten
307 Guards; sein interner Checkerhash passt nicht zur gleichzeitig
eingefrorenen Programmdatei. Das ist ein Versionskonflikt des Berichts,
kein Beweis, dass seine Mathematik falsch ist. Die tragenden Aussagen
werden deshalb unabhängig geprüft, nicht als exakter Gesamtreplay
dieses fremden Programms ausgegeben. Das Feld-JSON meldet 2161 Guards
und besitzt einen passenden Quellenhash; es enthält dennoch den unten
korrigierten Normfehler und zu weit formulierte Interpretationen.

Mit den weiteren Texten und zugehörigen Auditdateien sind es insgesamt 24 eingefrorene Eingaben.
Unsere eigene neue Suite hat **822 exakte Prüfbedingungen pro Python-Modus**.
Normaler und optimierter Lauf erzeugen identische Ergebnisdateien; Warnungen
werden als Fehler behandelt. Zusätzlich wurde die ältere ganzzahlige
Kontraktionsrechnung frisch kompiliert und wiederholt, mit identischen Zahlen.
Die vier-Boson-Norm aus dem früheren Zertifikat bleibt ein gekennzeichneter
Eingang: Ihre vollständige Enumeration wurde in dieser Runde nicht wiederholt.
Auch die gesamten fremden Programme mit ihren Guards wurden nicht alle erneut
ausgeführt. Prüfzahl und Beweisumfang werden ausdrücklich getrennt.

### 2.2 Übernahmeentscheidung

| Aussage aus den Eingaben | Entscheidung für v1.6.7 |
|---|---|
| Korrigierter Anfangskommutant 3829536 / 1444233216 | Bestätigt; keine neue Größe gegenüber v1.6.6 |
| Nur SU(4) oder nur Spin(10) als zusätzliche Kontrollen | Übernommen; echte Zwischenstufen statt binärer Verfügbarkeit |
| Volle Gruppe plus alle Modenbesetzungen erzeugt volle Sektoralgebra | Unabhängig bestätigt, ausdrücklich bedingt |
| Clock außerhalb der zusammenhängenden Gruppe, weil nicht skalar | Verworfen; das explizite Spin-Wort aus v1.6.6 widerlegt den Schluss |
| Vier Singuletts auf der zweiten Bosonstufe | Unabhängig bestätigt und durch konkrete Zustandsprojektionen ergänzt |
| Eine Zustandsrichtung pro Bosonzahl könnte bis Stufe 32 genügen | Verworfen; schon Stufe zwei hat vier Richtungen |
| Feldnorm 24 bei quadrierter Norm 192 | Korrigiert: Norm ist 8 mal Wurzel 3 in derselben Konvention |
| 4035 bilineare Komponenten unbestimmt | Jetzt vollständig in drei innere Darstellungen zerlegt |
| Jeder relativistische Abschluss müsse den Tensorfeldkanal verwenden | Nur unter dem festgelegten gleichhändigen, ableitungsfreien Ansatz gültig |
| Schwächere Sektorschranken trennen N=64 nicht | Richtig für diese Sonde; widerlegt den stärkeren früheren Satz nicht |

Die Entropie von ungefähr 1,66 Bit im ersten Text gehört zum dortigen
Ritz-Näherungszustand. Die Blockdiagonalität der reduzierten Bosondichte
rechtfertigt die Shannon-Untergrenze für diesen Zustand, nicht ungeprüft
denselben Zahlenwert für den wahren nativen Grundzustand.
Ebenso ist eine Kreuzung mit dem leeren Zustand bei einem bestimmten
chemischen Potential kein Beweis für die vollständige Sektor-Stabilitätszone.

## 3. Vollständig gelöst: der erste verzweigte Singulettbereich

### 3.1 Warum vier und nicht eins?

Im Ladungssektor N=64 schreiben wir Zustände relativ zur gefüllten
Fermionreferenz \(F\). Bei k Bosonen gibt es 2k Löcher. Der Singulettbereich
auf dieser Stufe liegt in

\[
\mathcal S_k=
\left[\Lambda^{2k}(\overline{16\otimes4})
\otimes\operatorname{Sym}^k(10\otimes6)\right]^{G},
\qquad G=\operatorname{Spin}(10)\times SU(4).
\]

Die ersten Dimensionen sind **1, 1, 4**. Dies ist eine Aussage über alle
Singuletts dieser Stufen, nicht über vier verschiedene Grundzustände.
Ein eindeutiger Grundzustand kann durchaus in einem größeren Singulettbereich
liegen. Die Zentrumsregel N gleich 0 modulo 4 ist nur eine notwendige
Bedingung für Singuletts, kein Auswahlprinzip für N=64.

Der Beweis für k=2 benötigt keinen riesigen Matrixkern. Die Bosonseite zerfällt
nach der symmetrischen Cauchy-Identität in

\[
\operatorname{Sym}^2(10\otimes6)=
(1,1)\oplus(54,1)\oplus(1,20')\oplus(54,20')\oplus(45,15).
\]

Die Dimensionen 1, 54, 20, 1080 und 675 ergeben zusammen 1830.
Die vierte äußere Potenz der Fermionseite wird durch die fünf Partitionen
von vier beschrieben. Für die benötigten Überschneidungen reichen drei
Spinor-Schurfunktoren:

| Bosontyp | Spinor-Schurfunktor auf der Fermionseite | Anzahl gemeinsamer Typen |
|---|---|---:|
| (1,1) | Sym hoch 4 von 16 | 0 |
| (54,1) | Sym hoch 4 von 16 | 1 |
| (1,20') | S mit Partition (2,2) von 16 | 1 |
| (54,20') | S mit Partition (2,2) von 16 | 1 |
| (45,15) | S mit Partition (3,1) von 16 | 1 |

Die Charaktere wurden aus den fünf Konjugationsklassen von S4 mit ganzzahliger
Arithmetik aufgebaut, durch eine unabhängige Jacobi-Trudi-Rechnung kontrolliert
und mit der Weyl-Alternierung ausgewertet. Die volle äußere Potenz hat
635376 Dimensionen; der gemeinsame Singulettbereich hier nur vier.
Die Berechnung des anderen Workers über den vollständigen Gewicht-Null-Raum
kommt unabhängig auf denselben Wert.

### 3.2 Nicht nur gezählt: die vier Zustände und ihre Kopplungen

In der durch eine Bosonparität äquivalenten Lochdarstellung sei
\(v_k=(T_+)^kF\). Alle 108240 von null verschiedenen Koeffizienten von
\(v_2\) wurden neu berechnet, einschließlich der Boson-Fakultätsnormen.
Das ergibt \(\|v_2\|^2=439680\).

Sei \(P_R\) der orthogonale Projektor auf den jeweiligen inneren Typ der
Zwei-Boson-Seite. Dann sind die vier Vektoren \(P_Rv_2\) nicht null,
orthogonal und bilden wegen der bewiesenen Multiplizität eins die gesamte
Singulettbasis auf Stufe zwei. Ihre Normen und die Kopplungen vom normierten
Ein-Boson-Zustand lauten:

| Typ R | Normquadrat von P_R v2 | Quadrierte Kopplung geteilt durch g hoch 2 |
|---|---:|---:|
| (54,1) | 17280 | 36 |
| (1,20') | 7680 | 16 |
| (54,20') | 241920 | 504 |
| (45,15) | 172800 | 360 |
| Summe | 439680 | 916 |

Diese Zahlen sind abgeleitet, nicht angepasst. Die Projektoren benutzen
nur Symmetrisierung sowie die beiden vorhandenen invarianten Spurbildungen.
Die gemeinsame skalare Projektion (1,1) verschwindet identisch.

Nach Wahl der vier Basisphasen ist der Kopplungsvektor

\[
g\,(6,\,4,\,6\sqrt{14},\,6\sqrt{10}).
\]

Alle vier Richtungen sind in v2 enthalten, aber von Stufe eins wird nur ihre
eine feste Linearkombination angeregt. Drei dazu orthogonale Kombinationen
sind **nach unten** dunkel. Sie sind nicht deshalb auch gegenüber den
höheren Stufen entkoppelt.

### 3.3 Der vollständig bestimmte Sechszustands-Ausschnitt

Die Kompression auf alle Singuletts mit k kleiner oder gleich zwei ist exakt
äquivalent zu

\[
P_{\leq2}HP_{\leq2}\simeq
\begin{pmatrix}
0&g\sqrt{480}&0\\
g\sqrt{480}&\Delta&g\sqrt{916}\\
0&g\sqrt{916}&2\Delta
\end{pmatrix}
\oplus 2\Delta I_3.
\]

Damit ist dieser Ausschnitt vollständig gelöst. **Er ist nicht invariant:**
H führt von k=2 auch nach k=3. Seine Eigenwerte sind folglich nicht automatisch
Eigenwerte der ganzen Bank. Eine räumliche Interpretation oder zusätzliche
Wechselwirkung wurde für diese Reduktion nicht eingeführt.

Explizit besitzt die Kompression dreimal den Wert 2 Delta und die drei
reellen Nullstellen des Polynoms

\[
E^3-3\Delta E^2+(2\Delta^2-1396g^2)E+960\Delta g^2.
\]

## 4. Die richtige einfache Kette: Wiederholung von H

### 4.1 Der Fehler war die Gleichsetzung zweier verschiedener Stufen

Die Vektoren \(v_k=T_+^kF\) sind nach Bosonzahl geordnet. Schon bekannt ist

\[
T_-v_3=\frac{299520}{229}v_2+w_2,\qquad
\langle v_2,w_2\rangle=0,\qquad
\|w_2\|^2=\frac{5001523200}{229}>0.
\]

Diese Rechnung wurde frisch reproduziert. Aus einer kleinen relativen
Norm dieses Seitenzweigs folgt keine Konvergenz der gesamten Grundzustands-
oder Spektralrechnung. Insbesondere fehlt dann immer noch der große Übergang
nach v4.

Eine Lanczos-Kette entsteht stattdessen aus
\(F,HF,H^2F,\ldots\) durch Orthogonalisierung. Für einen selbstadjungierten
endlichen Hamiltonoperator beschreibt sie dessen zyklischen Teilraum exakt.
Das ist ein zulässiges einfaches Rechenbild, aber keine Behauptung, dass ihre
Indizes physikalische Orte oder Bosonzahlen seien. Auch die gesamte Bank muss
nicht mit diesem einen zyklischen Teilraum übereinstimmen.

### 4.2 Die ersten fünf Glieder sind jetzt exakt bestimmt

Für die normierte Lanczos-Basis \(u_n\) schreiben wir

\[
Hu_n=b_nu_{n-1}+a_nu_n+b_{n+1}u_{n+1},\qquad b_n>0.
\]

Die ersten Diagonalen lauten

\[
\frac{(a_0,a_1,a_2,a_3,a_4)}{\Delta}
=\left(0,1,2,3,\frac{105168998}{26292551}\right).
\]

Die ersten quadrierten Nebendiagonalen sind

\[
\frac{(b_1^2,b_2^2,b_3^2,b_4^2)}{g^2}
=\left(480,916,\frac{299520}{229},\frac{78877653}{47632}\right).
\]

Bis u3 stimmen die Vektoren, bis auf die Phase bei negativem g, mit den
normierten vk überein. Der nächste Vektor ist proportional zu \(v_4+w_2\).
Dabei liegen v4 und w2 auf verschiedenen Bosonstufen. Deshalb gilt

\[
\frac{b_4^2}{g^2}
=\frac{\|v_4\|^2+\|w_2\|^2}{\|v_3\|^2},
\qquad
\langle u_4,N_bu_4\rangle
=\frac{4\|v_4\|^2+2\|w_2\|^2}{\|v_4\|^2+\|w_2\|^2}.
\]

Die Bosonzahlvarianz dieses Vektors ist exakt

\[
\operatorname{Var}_{u_4}(N_b)
=\frac{63416178576}{691298238087601}>0.
\]

Die frühere Quotientenfortsetzung mit nur \(\|v_4\|^2/\|v_3\|^2\)
ließ den positiven Zusatz \(1809/47632\) weg. Die korrigierte Kette bleibt
einfach, verliert aber gerade deshalb nicht die wirkliche Mehrkanalstruktur.
Ihre Länge ist nicht durch die 33 möglichen Bosonzahlen festgelegt.

### 4.3 Zehn vollständige Energiemomente der gefüllten Referenz

Die Fünfer-Kompression bestimmt
\(\mu_n=\langle F,H^nF\rangle\) für n von 0 bis 9 exakt. Ein Weg, der
den nächsten nicht enthaltenen Lanczos-Vektor erreicht und nach F zurückkehrt,
benötigt mindestens zehn Schritte. Aus der Tridiagonalität folgt deshalb die
angegebene Momentengenauigkeit, ohne die übrige Kette zu erfinden.

Beispielsweise gilt

\[
\mu_0=1,\quad \mu_1=0,\quad
\mu_2=480g^2,\quad \mu_3=480\Delta g^2,
\quad \mu_4=480\Delta^2g^2+670080g^4.
\]

Vollständig lauten die Koeffizienten in
\(\mu_n/\Delta^n=c_2x^2+c_4x^4+c_6x^6+c_8x^8\),
mit \(x=g/\Delta\), für n von 2 bis 9:

| n | c2 | c4 | c6 | c8 |
|---|---:|---:|---:|---:|
| 2 | 480 | 0 | 0 | 0 |
| 3 | 480 | 0 | 0 | 0 |
| 4 | 480 | 670080 | 0 | 0 |
| 5 | 480 | 2219520 | 0 | 0 |
| 6 | 480 | 5527680 | 1510510080 | 0 |
| 7 | 480 | 12353280 | 10437173760 | 0 |
| 8 | 480 | 26213760 | 48253363200 | 4615972423680 |
| 9 | 480 | 54144000 | 187581404160 | 54295325184000 |

Diese Momente gehören **F**, nicht dem nativen Grundzustand Omega. Sie sind
auch nicht mit den geladenen Antwortmomenten aus der früheren Fassung zu
verwechseln. Sie machen eine endliche Modellrechnung genauer, beweisen aber
keine physische Präparation von F und keine Vollständigkeit des Feldwörterbuchs.

### 4.4 Kleine, rigorose Verschärfung der Energiegrenze

Am Prüfpunkt g geteilt durch Delta gleich 1/20 hat die niedrigste Eigenenergie
der Fünfer-Kompression die durch rationale Sturm-Zählung zertifizierte Lage

\[
-1.12963813<\frac{E_{\mathrm{Ritz},5}}{\Delta}<-1.12963811.
\]

Rayleigh-Ritz liefert für den wahren Grundzustand daher

\[
E_0<-1.12963811\Delta.
\]

Die frühere untere Schranke bleibt \(E_0>-1.158089\Delta\).
Zusammen mit dem früheren strengen N=63-Floor
\(E_h>-1.121899\Delta\) folgt nun

\[
\epsilon=E_h-E_0>0.00773911\Delta.
\]

Die Verbesserung gegenüber 0.007737 ist klein. Die obere Polgrenze
0.039079764 und das Gewicht über 88.007628 Prozent werden dadurch nicht
ungeprüft verändert. Auch die niedrigste Ritz-Energie ist kein berechneter
Zentralwert von E0.

## 5. Vollständig gelöst: die innere bilineare Zerlegung

Für den 64-dimensionalen Fermionträger gilt

\[
\operatorname{End}(16\otimes4)
=(1,1)\oplus(45,1)\oplus(210,1)
\oplus(1,15)\oplus(45,15)\oplus(210,15).
\]

Die sechs Dimensionen sind 1, 45, 210, 15, 675 und 3150. Der offene Rest ist
also nicht mehr unbestimmt:

\[
4035=210+675+3150.
\]

Eine kurze konkrete Konstruktion genügt. Auf dem chiralen 16er-Raum liefern
Cliffordprodukte der Grade 0, 2 und 4 genau 1, 45 und 210 unabhängige
Matrizen. Ihr ganzzahliger Hilbert-Schmidt-Gram ist \(16I_{256}\).
Unter Spin(10)-Konjugation bleiben diese Gradräume invariant. Auf der
Farbseite zerfällt End(4) in die skalare Matrix und die 15 spurlosen Matrizen.
Die Tensorprodukte ergeben die gesamte Zerlegung. Die Weyl-Multiplizitäten
wurden zusätzlich überprüft.

Die verwendete Spinorzerlegung ist etablierte Darstellungstheorie, keine neue
Vorhersage von 210 physikalischen Teilchen. Der Literaturabgleich bestätigt
die drei Spin(10)-Kanäle 1, 45 und 210; unsere Rechnung ordnet sie der
tatsächlichen 16-mal-4-Bank zu. Siehe
[Nath und Syed, vollständige Spinorkopplungen](https://arxiv.org/abs/hep-th/0109116).

Aus dieser Zerlegung folgt weder, dass alle Bilineare verfügbare Kontrollen
sind, noch, dass jede Darstellung ein propagierendes Feld ist. Produkte
einfacher Matrizen im Einteilchenraum dürfen insbesondere nicht automatisch
als dieselben Produkte ihrer Vielteilchen-Hamiltonoperatoren gelesen werden.

## 6. Welche Operationen wirklich verfügbar sein müssten

### 6.1 Die algebraische Frage ist präziser beantwortet

Im N=3-Sektor bleiben für verschiedene **angenommene** Operationsalphabete
folgende komplexe Kommutantdimensionen:

| Angenommenes Alphabet | Kommutantdimension |
|---|---:|
| X und Nb | 1444233216 |
| Zusätzlich dokumentierter Clock | 240742144 |
| Stattdessen zusätzlich SU(4)-Generatoren | 2247168 |
| Stattdessen zusätzlich Spin(10)-Generatoren | 1648 |
| Zusätzlich beide vollständigen Gruppen | 7 |
| Volle Gruppen und alle Modenbesetzungen | 1 |

Die physische Verfügbarkeit ist somit nicht auf eine binäre Alternative
zusammengeschrumpft. Es gibt geprüfte Zwischenstufen, darunter auch die in
v1.6.6 behandelten einzelnen Casimir-Auslesungen.

Die volle Algebra nach Hinzunahme aller Besetzungen wurde unabhängig mit
einem kleineren Beweis kontrolliert. Der Einteilchen-Supportgraph der
gewährten Gruppengeneratoren ist verbunden, ebenso der Bosongraph.
Ein verbundener Graph hat verbundene Besetzungsgraphen mit k ununterscheidbaren
Fermionen, solange 0 kleiner k kleiner 64. Der native Tensor verbindet die
Fermion- und Bosonseiten. Die Besetzungsoperatoren trennen alle Basiszustände.
Polynomiale Spektralprojektoren und die nichtverschwindenden Verbindungseinträge
erzeugen daher alle Matrixeinheiten.

So folgt bedingt die volle Algebra in N=2 und N=3. Gewährt man zusätzlich
geladene f-Instrumente, verbinden sich auch die beiden Sektoren. Das ist eine
vollständige **assoziativ-algebraische** Aussage, kein Nachweis beliebiger
unitärer Steuerbarkeit, effizienter Messung oder nativer Instrumentenherkunft.

### 6.2 Warum bloßes Lesen noch keine fehlende Bewegung erzeugt

Ohne die zusätzlich gewährten Gruppenkontrollen erhalten X, Nb, der Clock
und alle Modenbesetzungen weiterhin mindestens eine nichtskalare Farb-Cartanladung.
Jede Komposition dieser Operatoren behält diese Erhaltung. Die alleinige
Erlaubnis, mehr Moden zu unterscheiden, hebt das Hindernis also nicht auf.

Das ist die präzise Grenze zwischen **Auslesen** und **Eingreifen**.
Ein mathematisch definierter Projektor ist nicht schon ein physisch
ausführbares Messinstrument. Dass das Modell unter einer Transformation
symmetrisch ist, bedeutet nicht, dass es diese Transformation als kontrollierten
Eingriff erzeugt. Die bedingten Zwei-Banken- und Vierzustands-Transferbeispiele
aus v1.6.5 und v1.6.6 bleiben nützlich, aber ihre zusätzlichen Links bleiben
auch zusätzliche Voraussetzungen.

## 7. Feldwörterbuch: gesicherte Teile und korrigierte Reichweite

Für die unveränderte antisymmetrische Paarmatrix und gleichhändige Weylfelder
verschwindet die ableitungsfreie skalare Kontraktion. Die drei symmetrischen
Spinortensoren tragen einen nichtverschwindenden Kanal des Typs (1,0), mit
konjugiertem Typ (0,1). Das ist am gesamten ursprünglichen Tensor neu geprüft.

In der Konvention des gelieferten Programms hat jeder der drei Kanäle pro
Zeile Normquadrat 64. Die Summe ist 192 und die direkte Summennorm folglich
\(8\sqrt3\), **nicht 24**. Die Summe von drei einzelnen Normen darf nicht
mit der Norm ihrer orthogonalen direkten Summe verwechselt werden. Eine
anders normierte Vertexdefinition ändert diese Zahlen, nicht den Nullkanal.

Der Satz gilt unter den genannten Feld- und Ableitungsannahmen. Zusätzliche
unabhängige Komponenten oder Ableitungskopplungen sind andere Modelle und
nicht generell ausgeschlossen. Keine dieser Möglichkeiten ist dadurch
bereits aus der ursprünglichen Bank hergeleitet.

Auch die Zerlegung eines Vermittler-mal-Weyl-Komposits in die Lorentztypen
(3/2,0) und (1/2,0) ist eine Darstellungsaussage. Der Ranganteil 2/6 gleich
1/3 ist das Gewicht im maximal gemischten Zustand dieses Sechserraums.
Für allgemeine Zustände kann derselbe Projektor Gewichte von null bis eins
haben. Er liefert nicht automatisch ein Drittel des nativen Polgewichts.
Die frühere Ladungsunterscheidung bleibt bestehen: Die EOM-Größe D trägt
Ladung minus eins, das ältere erzeugende Komposit chi-dagger plus drei.

## 8. Die fundamentale Frage: was fehlt wirklich?

### 8.1 Ein überprüfbarer Unterbestimmtheitssatz

Betrachte bei festem W dieselbe Familie
\(H_{\Delta,g}=\Delta N_b+gX\). Alle diese Hamiltonoperatoren besitzen die
gleiche innere Quellsymmetrie, dieselbe Ladungserhaltung und denselben
kommutierenden endlichen Clock. Dennoch unterscheiden sie sich dynamisch.
Schon für dieselbe gefüllte Referenz F ist die dimensionslose Momentenkombination

\[
\frac{\mu_4\mu_2}{\mu_3^2}
=1+1396\left(\frac{g}{\Delta}\right)^2.
\]

Bei g geteilt durch Delta gleich 1/20 ist sie 4,49, bei 1/40 dagegen 1,8725.
Beide Parameterpunkte liegen im früher abgesicherten Grundzustandsintervall.
Weil die Größe dimensionslos ist, handelt es sich nicht lediglich um eine
Änderung der Maßeinheit. Die gleiche Grammatik und Symmetrie lässt also
unterschiedliche Antworten auf dieselbe Präparation zu.

**Damit ist die eindeutige physische Dynamik aus diesen Grunddaten allein
nicht ableitbar.** Das widerlegt nicht die Möglichkeit einer einfachen
zusätzlichen Ursprungsregel. Es identifiziert genau deren Aufgabe:
Sie muss den Prozess samt verfügbarem Operationssatz und Zustand auswählen,
statt nur seine Symmetrie zu benennen. Im fest gesetzten Prüfvertrag sind g
und Delta natürlich definiert; offen ist ihre physische Herkunft.

### 8.2 Der kleinste tragfähige Forschungsansatz

Für eine einzelne Antwortrechnung sollte der relevante Raum nicht von
vornherein der gesamte Fockraum sein. Der zyklische Raum der tatsächlichen
Operationen auf dem angegebenen Startzustand ist der kleinere Arbeitsraum.
Die H-Lanczos-Kette ist eine exakte Darstellung eines solchen Raums.
Mehrere Präparationen, Messungen oder Compileroperationen können jedoch einen
größeren gemeinsamen Prozessraum verlangen. Ihre Kompatibilität muss dann
nachgewiesen werden; getrennte kleine Modelle dürfen nicht einfach
zusammengefügt werden.
Eine vollständige Rekonstruktion des Grundzustands aus dieser Referenz
verlangt außerdem einen Nachweis ihrer nichtverschwindenden Überlappung
mit Omega; die Ritz-Obergrenze allein ersetzt ihn nicht.

Die nächste physikalische Schließung bleibt dieselbe konkrete Bedingung:
Auf einer gemeinsam hergeleiteten Quelle und demselben Zustand muss eine
verfügbare Operation eine geladene Anregung zwischen operational bestimmten
Teilen übertragen. Der Test muss die Mehrzeitantwort von bloßem Überlapp
unterscheiden und ein konsistentes relativistisches Feldwörterbuch verwenden.
Koordinatenwechsel, Gram-Überlapp oder ein innerer Clock allein erfüllen
diese Bedingung nicht.

## 9. Aktueller Stand T1 bis T8

Die folgende Tabelle ordnet die Beiträge dieser Runde den bisherigen offenen
Beweispflichten zu; sie benennt keine neue Definition der ursprünglichen Tore.

| Tor | Beitrag dieser Runde | Weiter fehlender entscheidender Nachweis |
|---|---|---|
| T1 | Exakte bedingte Kontrollalgebra; Auslese- und Eingriffslücke präzisiert | Tatsächlich erzeugbare Compileroperationen und Instrumente |
| T2 | Bessere lokale Struktur und Antwortgrenze in der endlichen Bank | Quellseitiges Half-Charge-Feld mit Energie- und Adjungiertenkontrolle sowie E8-/Clock-Zuordnung |
| T3 | Kleiner gemeinsamer Rechenraum innerhalb einer Bank | Gemeinsamer physischer 3+1D-Ursprung |
| T4 | Vollständige innere Bilineare; korrekte Feldkanäle | Vollständiges chirales Maß mit dynamischen Eichfreiheitsgraden |
| T5 | Exakter lokaler Hamilton-Lanczos-Anfang | Kontrollierter relativistischer Kontinuums- und Streuungsgrenzfall |
| T6 | Expliziter Nachweis, dass die bisherigen Grunddaten g/Delta nicht auswählen | Physische Kopplungs-, Skalen- und Spektralzuordnung, einschließlich offener Neutrinofragen |
| T7 | Keine neue Schließung | Aus derselben Quelle erzeugter dynamischer Spin-2-Sektor und universelle Kopplung |
| T8 | Unterscheidung Startzustand, Grundzustand und Ausleseinstrument verschärft | Gemeinsame physische Präparation, Aufzeichnung und Zustandsauswahl |

Alle acht Tore bleiben offen. Die heutigen Ergebnisse schließen begrenzte
mathematische Fragen innerhalb des Programms, nicht diese physikalischen
Gesamtnachweise. Frühere RH-, Faktorisierungs- oder P-versus-NP-Grenzen
werden durch die endlichen Rechnungen ebenfalls nicht verändert. Der begrenzte
RH-Registerabgleich und seine Aktualitätsgrenze sind in Teil B dokumentiert;
ein vollständiger Neuaudit dieser Arbeitsfronten fand nicht statt.

## 10. Die drei nächsten entscheidenden Untersuchungen

1. **Den minimalen Ursprungsvertrag auswählen.** Teil B klassifiziert die
   kleinen symmetrieverträglichen Terme und trennt echte Erweiterungen von
   einem bloßen Wechsel der Bosonvariablen. Der Compiler muss diese Auswahl
   und die relativen Parameter begründen. Symmetrie allein tut das noch nicht.
2. **Die gemeinsame Schattenkarte am vorhandenen Tensor prüfen.** Derselbe
   Zustand und dieselben Operationen müssen die verschiedenen Ausleseansichten
   tragen. Gesucht sind ergänzende statt nur duplizierte Informationen, ein
   kontrollierter gemeinsamer Kern und Vorhersagen ohne nachträgliche Anpassung.
3. **Einen echten Eingriffstransfer und denselben Feldadapter konstruieren.**
   Eine aus der Quelle abgeleitete lokale Operation muss später die unbedingte
   Statistik eines anderen operational bestimmten Teils verändern. Selbst
   zeitabhängige Kreuzkorrelation bei Anfangswert null reicht nicht; Teil B
   enthält ein exaktes Gegenbeispiel. Dazu müssen Ladung, Kinetik und
   relativistische Feldzuordnung passen, bevor räumliche Skalierung trägt.

Die korrekte H-Kette mit Restschranke bleibt eine nützliche parallele
Rechenaufgabe. Die zehn bekannten Momente sind feste Gegenprüfungen. Sie
ersetzt aber nicht die jetzt vorrangige Ursprungs- und Kompositionsfrage.

## 11. Reproduktion und Veröffentlichung

Das Prüfpaket enthält sechs neue Python-Prüfer, die eingefrorenen Quellen,
die alte und neu wiederholte Kontraktion, Ergebnisdateien, Quellenmanifest
und die vollständige v1.6.6 als historische Basis. `replay.py` prüft alle
Pins, beide Python-Modi und die C++-Kontraktion. Die ausgelieferte ZIP wird
nach dem Entpacken erneut geprüft.

Die vollständige Hauptfassung, das kurze Änderungsdokument und die einfache
Erklärung werden gemeinsam versioniert direkt in Documents abgelegt, jeweils
als Markdown und PDF. Die PDF-Ausgaben werden zusätzlich auf Darstellung,
Textabdeckung und Seitenaufbau geprüft. Frühere Fassungen bleiben erhalten.
Es erfolgt keine Änderung der zentralen TOE-Abnahmemarker, kein Commit,
kein Push und keine externe Web-Veröffentlichung.

Der Statusleitfaden beeinflusst die Trennung zwischen mathematischer
Struktur, angenommenen Ressourcen und nachgewiesener Fähigkeit. Der
Debugging-Leitfaden führte zur ausdrücklichen Sicherung reell-ganzzahliger
Tensorwerte vor der Typumwandlung; keine Imaginärteile werden still verworfen.

### Schluss in einem Satz

**Die einfache Regel ist vorhanden; ihr erster verzweigter Zustandsbereich
und die richtige kleine Rechenkette sind jetzt genauer gelöst. Was noch
fehlt, ist die aus dem Ursprung folgende Auswahl und Ausführung dieses
Prozesses als dieselbe physikalische Welt.**
