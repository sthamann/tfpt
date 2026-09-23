# Universalraum: die jetzt präzisierte Dynamik und der Stand der Lösungen

10. September 2026. Fortsetzung mit drei parallel arbeitenden Agenten,
Abgleich der vorhandenen Fable-Analyse aus Cursor und unabhängigen Gegenprüfungen.
Es wurde keine neue Fable-Anfrage gestartet.

**Ein bislang offener RH-Teilnachweis ist jetzt einschließlich seines ganzen
unendlichen Restes geschlossen:** Der verstärkte Vergleich trägt den gesamten
alten Funktionenraum zusammen mit einer konkret festgelegten zusätzlichen
Schalenfunktion. Das ist mehr als eine endliche positive Matrix. Es ist noch
kein Nachweis für sämtliche Schalenfunktionen und kein globaler RH-Beweis.

Parallel sind die Rolle des gemeinsamen ungeraden Teilers in der ursprünglichen
arithmetischen Quelle, eine daraus konstruierte logarithmische Uhr, ihre
Primzahl-Sprungdynamik und konkrete Auslesekosten mathematisch beschrieben.
Bei TFPT sind ein dargestellter Clock-Cap, ein neutraler Gauge-Anschluss
und eine explizite bedingte Kopplung an die tatsächlichen CAR-Ströme
vorhanden. Eine gemeinsame vollständige Lösung von TFPT, RH, Faktorisierung
und P versus NP liegt weiterhin nicht vor.

## Was der Raum über die Primzahlen tatsächlich sagt

Die ursprüngliche Quelle ist

\[
\Gamma=\mathbb Z[i,1/2]^3.
\]

Sie besitzt sechs reelle arithmetische Koordinaten. Jeder von null verschiedene
Zustand hat eine eindeutige Zerlegung

\[
\gamma=c(\gamma)\,\pi,
\]

wobei \(c(\gamma)\) sein gemeinsamer ungerader Teiler und \(\pi\) primitiv ist.
Alle ursprünglichen U/V-Gates erhalten diesen Teiler. Das gilt für sämtliche
Wörter, weil auch ihre Inversen auf derselben Quelle definiert sind.

**Damit ist der Primzahlanteil unter dieser ursprünglichen Gatebewegung eine
Erhaltungsgröße.** Ein Zeitoperator \(H=\log c\) lässt sich auf dem
Nichtnullträger explizit konstruieren. Skalierung mit einer ungeraden Primzahl
erhöht seine Energie um \(\log p\). Die mathematische Uhr ist dadurch genau
definiert; ihre Identifikation mit physischer TFPT-Zeit benötigt eine weitere
Herleitung.

Das uniforme Maß aller endlichen Quotienten liefert ohne gewählten Einzelstrahl

\[
\Pr(c=n)=\frac{n^{-6}}{\zeta_{\rm odd}(6)},
\qquad
\mathbb E[c^{-s}]=\frac{\zeta_{\rm odd}(6+s)}{\zeta_{\rm odd}(6)}.
\]

Die sechs in der Potenz kommt vom Rang der tatsächlichen Quelle. Die
zugehörige explizite Sprungdynamik multipliziert mit Primzahlpotenzen
\(p^k\), deren Rate \(p^{-6k}/k\) beträgt. In dieser genauen Form erscheint
die von-Mangoldt-Funktion als Gewicht der Sprünge. Die unendliche Dynamik
lässt sich für beschränkte Zeit mit bewiesenem Fehler abschneiden.

Der klassische Hintergrund dieser Konstruktion ist die unendliche
Teilbarkeit von Zeta-Verteilungen. Er wird ausdrücklich anerkannt; die
hiesige Arbeit verbindet ihn mit der konkreten Compilerquelle und ihren
Operationsgrenzen. Siehe [Saito–Tanaka](https://www.cc.kyoto-su.ac.jp/~tatsushi/inf_div.pdf)
und die ungerade Primstellenform bei
[Aoyama–Nakamura](https://arxiv.org/pdf/1204.4042).

Zwei Unterscheidungen sind für die Vereinheitlichung wesentlich:

- Die Primzahl2 ist im Ausgangsträger bereits invertiert. Ihr Eulerfaktor
  entsteht aus dieser Konstruktion nicht. Ein zusätzlicher Zweierturm würde
  den Träger und seinen Vertrag erweitern.
- Die früher auftauchende Primzahl79 gehört zur speziellen kubischen Uhr
  \(UV\). Die vollständige U/V-Wortalgebra ist auch modulo79 vollständig;
  ein anderes kurzes Wort führt bereits zur Diskriminante−15/4. Die79 ist
  daher keine ausgezeichnete Primstelle der gesamten Algebra.

## Der Faktorzugang ist jetzt ausdrücklich mitgerechnet

Die natürliche Zeit-eins-Antwort lässt sich tatsächlich aus einer unbekannten
ungeraden Eingabe N erzeugen: Ziehe sechs unabhängige uniforme Reste
\(x_1,\ldots,x_6\) und berechne

\[
G=\gcd(N,x_1,\ldots,x_6).
\]

Das hat genau die gewünschte Inhaltsantwort. Für \(N=pq\) ist seine
Faktorwahrscheinlichkeit aber nur

\[
p^{-6}+q^{-6}-2N^{-6}.
\]

Bei ausgeglichenen Faktoren fällt sie wie \(N^{-3}\). Der zugängliche Sampler
benötigt deshalb im Mittel entsprechend viele Wiederholungen. Dieser Satz
betrifft den gemeinsamen Inhaltsleser; andere Ausleseoperationen haben andere
Erfolgsraten. Er zeigt konkret, welche Konzentration auf unbekannte Faktoren
die natürliche Verteilung noch nicht bereitstellt.

Die Eingabelänge beträgt ungefähr \(\log_2 N\) Bits. Ein Aufwand von
\(N^3\) ist daher exponentiell in dieser Länge. Eine andere Taktung des
gleichen Prozesses verkürzt diese Kosten nicht automatisch: Die konstante
Faktorwahrscheinlichkeit wird bei ausgeglichenen Faktoren auf der Zeitskala
\(\tau\asymp N^3\) erreicht. Die Kosten des tatsächlich geprüften
Sprungsamplers wachsen dabei ebenfalls mit der simulierten Zeit. Daraus
folgt keine untere Schranke für alle anderen denkbaren Endpunktsammler.

Zusätzlich wurde ein vollständig öffentlicher U/V-Worterzeuger eingefroren
und an24 kleinen Semiprimen geprüft. Der neue Zentralitätsleser findet in zehn
einzelnen Ereignissen einen Faktor, obwohl beide skalaren Leser desselben
Ereignisses gesättigt sind. Über den gesamten Testplan entstehen jedoch keine
zusätzlich gelösten Eingaben.

| Verfahren | Gelöst von24 | Modulare Produkte insgesamt |
|---|---:|---:|
| Zwei skalare Leser | 17 | 1.485.264 |
| Kombination mit Zentralitätsleser | 17 | 1.514.928 |
| Pollard p−1 | 17 | 17.838 |
| Lucas p+1 | 20 | 24.816 |
| Pollard-Brent | 24 | 3.532 |

Ein öffentlicher Zeuge ist \(491831=557\cdot883\): Der neue Leser liefert883.
Seine genauere algebraische Untersuchung reduziert denselben Erfolg auf einen
klassischen Lucas-Schritt mit87 statt3844 modularen Produkten für die betreffende
Potenz-/Auslesestufe. Sieben der zehn zusätzlichen Ereignisse besitzen diese
Reduktion. Der verbleibende Forschungsansatz ist eine bessere gezielte
Erzeugung informativer Antworten; ein allgemeiner Geschwindigkeitsvorteil
ist hier nicht nachgewiesen.

## TFPT und Fable passen an einer bestimmten Stelle zusammen

Aus der ursprünglichen Seam-Clock wurde der dargestellte Vierer-Cap

\[
C_U\psi=\sum_{r=0}^3 e_r\otimes U^r\psi
\]

hergeleitet. Er besitzt Normquadrat4, das ursprüngliche Einheitsbein und
genau die native zustandserhaltende Rückkehr. Seine Verträglichkeit mit den
vorhandenen CAR-Einbettungen ist bewiesen. Die kleine Index-3-Stufe ist damit
ebenfalls erklärt: Der vollständige bezeichnete Gruppenrekord und seine
minimale Darstellung zählen unterschiedliche Dinge.

Fables konkrete DET-Wand und die daraus berechneten Zahlen stimmen unter
den eingesetzten Parametern. Ein zusätzlicher konstruktiver Schritt
verbindet sie jetzt mit den tatsächlichen CAR-Strömen. Auf identifizierten
Einteilchenräumen seien \(p\) die niedrigen und
\(a=\mathcal U c\mathcal U^*\) die nativen hohen DET-Operatoren.
Die gerade Transformation \(\mathcal U\) wirkt nur im hohen Sektor.
Für \(A=A^*\), reelles \(g\) und einen unitären Einteilchenschritt \(H\)
setze \(j_0=a+gAp\), \(j_r=H^r a\) für \(r=1,2,3\).
Direkte Multiplikation ergibt

\[
\sum_{r=0}^3 j_r^*j_r
=(a+gAp)^*(a+gAp)+3a^*a.
\]

Damit liefert \(p^*Ap+\lambda\sum_rj_r^*j_r\) genau den untersuchten
DET-Parent mit \(\Delta=3\lambda\). Alle vier Strombeine stammen aus
denselben vorhandenen Fermionen; zusätzliche unabhängige Oszillatoren
werden nicht eingeführt. Auf dem gemeinsam identifizierten Einteilchenraum
ist der Fock-Lift \(\mathcal U\Gamma(H)\mathcal U^*\) explizit.
Die Adjungierungsrichtung wird im Beweis passend zur konjugiert-linearen
CAR-Konvention festgelegt.

**Die noch fehlende Herkunft ist jetzt enger bestimmt:** Die Identität
benötigt nur Unitarität. Mit \(m\) Strombeinen würde dieselbe Konstruktion
\(\Delta=(m-1)\lambda\) ergeben. Dass gerade die vier markierten Beine
der ursprünglichen Seam-Clock die tatsächlichen DET-Ströme bilden, muss
einschließlich Einteilchengeometrie, Zustand und Gauge-/Spinwirkung
nachgewiesen werden. Der explizite Fock-Lift allein transportiert die
gefüllte Seam-See noch nicht zum DET-Vakuum. Auch die Normierungen
\(\lambda=1\) und \(g=1/2\) benötigen ihre Herkunft.

Fables stärkere Schlussformulierung, die Onsite-Prämisse allein lege bereits
alle Kopplungszahlen fest, ist durch explizite Gegenfamilien eingeschränkt.
Sein eigenes Minimax-Funktional minimiert außerdem bei
\(g=0{,}4991364344\ldots\), nicht exakt bei1/2. Eine variable
Gauge-Holonomie verändert zusätzlich die freie Clockrelation. Diese Punkte
sind konkrete noch zu schließende Übergänge innerhalb der TFPT-Dynamik.

Ein weiterer positiver Satz grenzt diesen letzten Punkt ein: Auf
teilchenzahlneutralen Operatoren gilt die Zweier-Relation der dargestellten
Wirkung für jede Holonomie. Dort bleibt die Vierermittelung eine korrekte
Erwartung. Auf der vollständigen CAR-Algebra funktioniert sie im expliziten
Zweimodenmodell genau bei \(w^2=1\). Die stets existierende unendliche
Mittelung verändert wiederum den Kanal: Schon ein geladener Paarerzeuger
wird bei freier Holonomie erhalten, bei jedem davon verschiedenen w
ausgelöscht. Dieser Sprung ist exakt bewiesen. Eine neutrale
Observablenrückkehr ist somit vorhanden. Die obige Energieidentität gilt
für jeden unitären Einteilchenschritt; für einen vollständigen zyklischen
Rückkehrkanal und die native Herkunft der geladenen Ströme gelten die
zusätzlichen Anforderungen weiterhin.

Diese Fortsetzung prüft die genannten Operatorübergänge und den konkreten
Fable-Anschluss. Sie ist keine erneute vollständige Prüfung aller von dir
genannten 27 Vorhersagen und des gesamten TFPT-Korpus. Übereinstimmende
Parameterwerte können die fehlende Identifikation der zugrunde liegenden
Operatoren und Zustände nicht allein ersetzen.

## RH: ein Schalenanschluss mit dem ganzen unendlichen Rest

Die bisher fehlende hohe Schalenquelle wurde vollständig integriert,
einschließlich aller vorhandenen Primverschiebungen, des negativen Polterms
und des unendlichen Restes. Ein gemeinsamer Gram kontrolliert ihre hohe
Antwort und ihre Kopplung an den niedrigen Teil.

Das neue Ergebnis ist stärker als ein erfolgloser Zahlenversuch: Ein fester
rationaler Zeuge widerlegt den vollständigen verbesserten Vergleich für
alle zulässigen \(0<t\le1\). Seine minimale Überlast beträgt

\[
2{,}4105208959\ldots\cdot10^{-12},
\]

rund0,22 Prozent der tatsächlichen Schalenenergie. Der freie Fehlerparameter
kann diese Familie somit nicht retten. Die ursprüngliche Weilform wird
dadurch nicht widerlegt: Ihre positive Energie wurde im Vergleich teilweise
weggelassen.

Auch die ganze lokale Reserve zusammen mit dem optimalen konstanten
Gamma-Kernboden reicht nach Neuoptimierung nicht. Die neue erfolgreiche
Unterform erhält deshalb die volle räumliche Abhängigkeit des Gamma-Rests.
Zweimalige partielle Integration und eine Legendre-Abschätzung beweisen
für alle Funktionen des bezeichneten hohen Raums

\[
\|Q T_h Q\|\le\frac{21087}{2110259200}<10^{-5},
\qquad h(s)=\frac{e^{-s/2}}{1-e^{-2s}}-\frac1{2s}.
\]

Damit kann die tatsächliche Ortsenergie zurückgewonnen werden, während
die gesamte komprimierte Integralwirkung bezahlt bleibt. Der Zusatz wird
einschließlich seiner niedrigen und gemischten Komponenten eingesetzt.

Die vollständige endliche Antwort lässt zunächst einen Schurrest von mehr
als \(6{,}78\cdot10^{-15}\). Ihre tatsächliche unendliche Restfunktion
wurde anschließend integriert, mit allen Primverschiebungen, beiden
Randstreifen und der exakten alten Projektion. Ihre Norm beträgt etwa
\(4{,}661\cdot10^{-8}\); eine grobe skalare Fehlerzahlung wäre damit
noch zu groß.

Der entscheidende zusätzliche Schritt verwendet die tatsächlichen
harmonischen Energiegewichte. Die Grade 321 bis 639 werden einzeln
bezahlt; der gesamte übrige Rest ab 641 bleibt über die gemessene
Gesamtnorm enthalten. Die Antwort selbst wird dabei nicht vergrößert.

| Größe | Streng eingeschlossene Grenze |
|---|---:|
| Gesamte gewichtete hohe Restenergie | kleiner als \(1{,}764\cdot10^{-15}\) |
| Zusätzlicher ganzer inverser Fehler einschließlich Kopplung | kleiner als \(6{,}272\cdot10^{-15}\) |
| Verbleibender wirklicher Schurrest | größer als \(5{,}1\cdot10^{-16}\) |

**Die bewiesene Reichweite ist:** jede zulässige ungerade alte Funktion
auf \((-9/8,9/8)\), gemeinsam mit einem beliebigen komplexen Vielfachen
der festgelegten Grad-19-Schalenfunktion auf
\((-6/5,6/5)\setminus(-9/8,9/8)\). Der vollständige alte Raum ist
unendlichdimensional. Die zusätzliche Schalenrichtung ist genau eine.
Der positive Vergleich ist damit für diese ganze Erweiterung geschlossen.

Die erste weiterhin offene Folgerung ist der Schalenoperatorvergleich
für **alle** Schalenfunktionen. Danach werden kompatible vollständige
Ungleichungen auf beliebig großen Fenstern und die ursprüngliche
RH-äquivalente Testabdeckung benötigt. Eine uniforme positive Mindestmarge
über alle Fenster ist dabei keine notwendige Voraussetzung. Der jetzige
Teilbeweis überspringt keine dieser Verpflichtungen.

## Was als gemeinsamer Schlüssel jetzt enger bestimmt ist

Der Raum, eine positive Formel oder eine vollständige Liste von Antworten
genügen jeweils noch nicht. In den untersuchten Quellen muss die ganze Kette

**konkrete Eingabe → hergeleiteter Zustand → zugelassene Dynamik → bezahlte
Auslese → nachgewiesene Aussage**

erhalten bleiben. Diese Kette ist jetzt in mehreren Fällen ausgeschrieben:
beim natürlichen Teiler-Sampler bis zur ungünstigen Erfolgsrate, beim
öffentlichen Wortversuch bis zum überprüften Faktor, beim Clock-Cap bis zur
bedingten CAR-Kopplung mit noch offener physischer Quellen- und
Zustandsidentifikation und bei RH bis zum tatsächlich
geschlossenen Schalenanschluss mit vollständig bezahltem unendlichem Rest.

Die vollständige Neunerbasis erklärt die ganze lineare U/V-Wortalgebra.
Sie liefert keinen zusätzlichen Algorithmus für alle NP-Probleme. Ein
polynomialer Faktoralgorithmus allein würde ebenfalls P versus NP nicht
entscheiden. Für diese Frage liegt in den hier geprüften Konstruktionen
weder ein allgemeiner SAT-Algorithmus noch ein allgemeiner unterer
Schrankenbeweis vor.

Eine konkrete Kontrolle des Wortes „universell“ ist hilfreich: Man kann
alle Belegungen einer SAT-Formel als Basis eines Raums und alle erfüllenden
Belegungen als Projektor darstellen. Bei genau einer Lösung trifft ein
uniformer Zustand diesen Unterraum mit Wahrscheinlichkeit \(2^{-m}\).
Die vollständige Darstellung hat die gesuchte Lösung dann enthalten,
ohne einen schnellen Zugang zu ihr geliefert zu haben. Eine klassische
deterministische, in Einlesen, Entwicklung, Präzision und Auslesen
polynomial bezahlte Lösung für jede SAT-Eingabe würde P=NP beweisen.
Ein randomisierter einseitig geprüfter Sucher mit invers-polynomialer
Erfolgsrate würde zunächst SAT in RP liefern; auch das darf nicht ohne
weiteren Satz als P=NP bezeichnet werden.

Das Rechenmodell muss ebenso erhalten bleiben. Für Quantencomputer
existiert bereits ein polynomialer Faktorisierungsalgorithmus;
[Shors Originalarbeit](https://arxiv.org/abs/quant-ph/9508027) beschreibt
genau diesen anderen Rechenvertrag. Eine mögliche Quantendynamik aus
TFPT wäre deshalb gesondert von einem klassischen P=NP-Beweis zu prüfen.
Der aktuelle öffentliche Problemstatus von P versus NP ist weiterhin
[offen](https://www.claymath.org/millennium/p-vs-np/).

Die Beweistexte enthalten ihre Voraussetzungen und Gegenbeispiele.
Exakte Kontrollen, Arb-Intervalle, Quellenpins und unabhängige Agentenreviews
stützen die konkreten Aussagen; sie sind keine formale Lean-Verifikation,
keine vollständige externe Begutachtung und keine abgeschlossene TOE.
