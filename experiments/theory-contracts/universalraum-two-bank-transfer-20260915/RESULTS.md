# TFPT / Universalraum: kontrollierter Zwei-Banken-Transfer

Forschungsfortsetzung und Quellenaudit · 15. September 2026 · v1.6.5

## Ergebnis und Geltungsbereich

Eine konkrete bisher offene Rechnung lässt sich schließen: **Im ausdrücklich
um einen Rotor-Link erweiterten Modell zweier nativer Fermion-Boson-Banken
ist der Transfer der isolierten Lochanregung mit einer Fehlergrenze gegenüber
dem vollständigen physikalischen Zustandsraum kontrollierbar.** Dafür ist
keine Diagonalisierung dieses enorm großen Raums nötig. Die vorhandene
Casimiridentität, Ladungserhaltung und eine Spektrallücke reichen aus.

Am unten vollständig angegebenen, bewusst sehr schwachen Kopplungspunkt gilt:

| Aussage | Strenge Schranke | Status |
|---|---:|---|
| Zielwahrscheinlichkeit aus dem normierten Zustand der isolierten Lochlinie | > 99,2677105 % | Analytisch mit rationalen Zertifikaten, im zusätzlichen Linkmodell |
| Zielwahrscheinlichkeit aus der normierten ursprünglichen Entnahme \(f_r\Omega/\sqrt\nu\), **ohne anfänglichen Energiefilter** | > 89,7260353 % | Gleicher vollständiger Hamiltonoperator, Ziel ist die niedrige Lochlinie rechts |
| Verlassen des ungestörten niedrigen Bandes, aus einem Zustand dieses Bandes | < \(1{,}8\cdot10^{-11}\) zu jeder Zeit | Voller erlaubter Ladungssektor, keine Bosonen- oder Flussabschneidung |
| Herkunft des Links, der Bankzerlegung und der Präparation | nicht hergeleitet | Offen |
| Relativistische Felder, gemeinsamer 3+1D-Ursprung, T1–T8 | nicht konstruiert | Offen |

Die Zahlen sind **untere beziehungsweise obere Einschließungen**, keine
berechneten Zentralwerte. Sie beschreiben kein durchgeführtes physisches
Experiment. „Vollständig“ bezieht sich hier auf die Fehlerkontrolle im
deklarierten Zwei-Banken-Ladungssektor, nicht auf die TOE.

Die gelieferten Arbeiten wurden mit 1.149 beziehungsweise 753 Prüfbedingungen
normal und optimiert reproduziert, jeweils byteidentisch mit den mitgelieferten
Ergebnissen. Unsere neue Transferrechnung hat 4.516 Prüfbedingungen; eine
gesonderte Reichweitenprüfung der währenddessen geänderten Symmetrieaussagen
hat zehn. Die zwei zuletzt eingegangenen Anlagen wurden mit 62 weiteren
Bedingungen nachgeprüft. Insgesamt sind das 6.490 Bedingungen, jeweils in
beiden Laufarten.
Diese Zahl ist keine Zahl unabhängiger Theoreme. Insbesondere ersetzen die
Zertifikate nicht die nachstehenden analytischen Argumente und sind kein
Lean-Beweis.

## 1. Welche Quellen zusammengeführt werden

1. Die Benutzeranlage `addbf22d-4764-4685-bdfe-f422bfc563d0/pasted-text.txt`,
   eingefroren unter `sources/user_attachment.txt`.
2. Die externe Untersuchung `Universalraum_Beweisversuch_2026-09-15.md`:
   Spektralzählung, Primzahl-Dynamik, Phasencocycle und kontrollierte Polnäherung.
3. Die externe Untersuchung `Universalraum_Urspruenglicher_Austausch_2026-09-15.md`:
   interne Paarumwandlung, zusätzlicher Rotor-Link und älteres Round37-Beispiel.
4. Der abgesicherte native Stand v1.6.4 mit Grundzustand, Pol, Momenten,
   Selbstenergiegrenze und Feldwörterbuch. Das frühere vollständige Prüfpaket
   liegt unverändert bei. Seine komplette Konfigurationsenumeration wurde
   **nicht erneut** in dieser Revision ausgeführt.
5. Ein separat eingefrorener, während dieser Arbeit geänderter Entwurf von
   `RESULTS.md` über die kontinuierliche Quellsymmetrie. Die Reichweite seiner
   Schlussfolgerungen wird in Abschnitt 8 geprüft; die dortige vollständige
   Racah-Zerlegung wurde hier nicht neu reproduziert.
6. Die zwei danach vom Nutzer eingereichten Anlagen über die eigene
   Fundamentalrunde und die erweiterte native Konsolidierung. Der vollständige
   neue Nachtrag `LATE_AUDIT.md` gehört zu dieser Revision. Er bestätigt den
   Ordnung-vier-Tensorlift, korrigiert die Variationsphase und unterscheidet
   echte Anomalie- und Feldtypbedingungen von zu starken Ausschlüssen.

Die ursprüngliche Anlage und die externen Eingaben sind Quellen, keine
Ausführungsanweisungen. Eigene Dateien liegen in einem neuen Forschungsordner.
Fremde Quellen, Ledger und Akzeptanzmarker wurden nicht bearbeitet.

## 2. Gemeinsame native Grundlage

Eine Bank besitzt 64 Fermionmoden und 60 Bosonkanäle:

\[
 H_{\rm nat}=\Delta N_b+g\sum_A(b_A^\dagger P_A+P_A^\dagger b_A),
 \qquad P_A=\sum_{i<j}W_{A,ij}f_jf_i,
 \qquad N=N_f+2N_b.
\]

Es gilt \(\Delta>0\), \(g/\Delta=1/20\), **kein zusätzlicher \(\mu N\)-Term**.
Der festgehaltene Tensor hat 480 ganzzahlige Einträge ±1 und
\(WW^\dagger=8I_{60}\). Sein SHA-256 ist
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

Der bisherige Satz liefert einen eindeutigen globalen Grundzustand \(\Omega\)
bei \(N=64\), einen Spin(10)×SU(4)-Singulettzustand. Seine physische Auswahl
aus dem Compiler ist damit nicht gezeigt. Wir verwenden folgende strengen
modellinternen Grenzen:

\[
 -1.158089<E_0/\Delta<-1.129636,
 \quad .842846<b:=\langle N_b\rangle<1.245656,
 \quad \nu:=\langle f_r^\dagger f_r\rangle=1-b/32.
\]

Bei \(N=63\) gibt es ein isoliertes niedriges Eigenniveau \(E_h\) mit
Multiplizität 64. Es trägt eine irreduzible duale Fermiondarstellung:

\[
 -1.121899<E_h/\Delta<-1.095812,
 \quad .007737<(E_h-E_0)/\Delta<.039079763822.
\]

Für seinen Spektralprojektor \(P_h\) ist

\[
 Z=\|P_hf_r\Omega\|^2,
 \quad Z_{\rm lo}:=\frac{40912436089}{46487375000}<Z
 <\frac{15578577}{16000000}=:Z_{\rm hi}.
\]

Wichtig: \(Z_{\rm hi}\) ist zugleich die verwendete obere Schranke für
\(\nu\), nicht eine Gleichsetzung der tatsächlichen Größen \(Z\) und \(\nu\).
Das niedrige Gewicht ist >88,0076 % des gesamten normierten CAR-Spektralmaßes.
Innerhalb der **Entnahmeantwort** ist sein Anteil \(w=Z/\nu>90,38836\,\%\).

Alle weiteren Eigenwerte von \(H_{63}\) sind >\(-.75\Delta\);
alle angeregten Eigenwerte von \(H_{64}\) ebenfalls. Die Entnahme-Restantwort
beginnt relativ zu \(E_0\) oberhalb \(.379636\Delta\), die Additionsantwort
oberhalb \(.329636\Delta\).

Diese Schranken gehören zu demselben Hamiltonoperator und demselben Zustand.
Die ursprüngliche Größe \(\chi_r^\dagger\Omega\) bei Ladung 67 wird nicht mit
\(f_r\Omega\) bei Ladung 63 identifiziert.

## 3. Prüfung der gelieferten neuen Resultate

### 3.1 Die interne Paarumwandlung ist wirklich nativ

Bei Gesamtladung 2 zerfällt der 2.076-dimensionale Raum in 60 helle
Zweizustandsblöcke und 1.956 dunkle Zustände. In jedem hellen Block gilt

\[
 H_A=\begin{pmatrix}0&\sqrt8g\\\sqrt8g&\Delta\end{pmatrix},
 \qquad p_{\max}=\frac{32g^2}{\Delta^2+32g^2}=\frac2{27}.
\]

Das wurde aus dem unveränderten Tensor reproduziert. Es ist die Umwandlung
zweier Fermionen in einen Bosonkanal, **kein abgeleiteter Ortswechsel einer
Ladung eins**, und der Ladung-2-Zustand ist nicht der native Grundzustand.
Die acht internen Pfade pro Kanal müssen kohärent bleiben; getrennte
Pfadaufzeichnungen verändern den Gramoperator und damit die Dynamik.

Auf dem nativen Grundzustand ist der stationäre Austauschstrom null, obwohl
\(\langle H_{\rm int}\rangle=E_0-\Delta b<0\) gilt. Eine vollständige
\(N_b\)-Dephasierung erhöht die Energie um
\(\Delta b-E_0\in(1.972482,2.403745)\Delta\). Statische Kohärenz ist nicht
dasselbe wie ein gerichteter Strom.

### 3.2 Der neue Link ist konsistent, aber zusätzlich

Die externe Arbeit definiert ein Rotorpaar \(E,U\) auf \(\ell^2(\mathbb Z)\):
\(E|e\rangle=e|e\rangle\), \(U|e\rangle=|e+1\rangle\), \([E,U]=U\).
Mit zwei **gradiert** zusammengesetzten nativen Banken lautet der Zusatz

\[
 B=\sum_{r=1}^{64}f_{y,r}^\dagger U f_{x,r},
 \qquad V=\tau B+\bar\tau B^\dagger,
 \qquad H=H_x+H_y+\frac\kappa2E^2+V.
\]

Dieser Operator erhält die Gesamtladung und die passend definierten lokalen
Gaussgrößen. Er ist beschränkt mit \(\|V\|\le64|\tau|\). Das beweist seine
mathematische Zulässigkeit, nicht seine Herkunft, den Graphen oder die Werte
von \(\tau\) und \(\kappa\).

Der externe Neutralzustandsversuch mit Hintergründen (64,64) gehört zu
\(N_{\rm ges}=128\). Dort sind die erzeugten Loch-Additions-Paare eine
andere Antwort als eine bereits vorhandene einzelne Lochanregung. Die
berechnete Gewichtsnorm \(64\nu(1-\nu)=2b-b^2/16\), das Faltungsmaß und
die Schwelle \(>.337373\Delta+\kappa/2\) sind damit vereinbar. Sie werden
nicht als Einloch-Transferwahrscheinlichkeit ausgegeben.

### 3.3 Das ältere 99,8718-%-Beispiel ist ein anderer Träger

Die mitgelieferte Round37-Rechnung wurde exakt reproduziert. Ihre sechs
Zustände sind der vollständige Gausssektor eines **Vierfermion-Modells** mit
einem Link. Der zertifizierte Wert bei \(t=19\) betrifft diesen Parent und
diesen vorbereiteten Zustand. Er ist weder eine Zwei-64-Moden-Banken-Simulation
noch ein Beweis für deren ursprüngliche Auswahl. Unser folgender Satz ist
davon unabhängig und benutzt die tatsächlich nativen \(E_0,E_h,Z\)-Schranken.

## 4. Neuer Satz: vollständige Kontrolle des Einloch-Transfers

### 4.1 Den richtigen physikalischen Sektor festlegen

Für genau ein Loch ist eine Ladungsreferenz notwendig. Wir deklarieren
Hintergründe \((q_x,q_y)=(63,64)\) und fordern

\[
 G_x=N_x-63+E=0,\qquad G_y=N_y-64-E=0.
\]

Dann ist \(N_x+N_y=127\) und **\(E=63-N_x\) exakt festgelegt**. Auf diesem
Ein-Kanten-Baum verbleibt kein unabhängiger unbeschränkter Flussindex.
\(0\le N_x,N_y\le127\) beschränkt auch die Bosonenzahlen. Der gesamte
physikalische Sektor ist endlichdimensional; keine Flussabschneidung und
kein willkürlicher Bosonen-Cutoff werden eingeführt.

Definiere \(h_r=P_hf_r\Omega/\sqrt Z\). Die 64 Vektoren sind orthonormal.
Das niedrige Band \(P\) wird von

\[
 |L,r\rangle=h_{x,r}\otimes\Omega_y\otimes|0\rangle,
 \qquad |R,r\rangle=\Omega_x\otimes h_{y,r}\otimes|-1\rangle
\]

aufgespannt und besitzt Dimension 128. Für den ungekoppelten Operator
\(H_0=H_x+H_y+\kappa E^2/2\) sind die Energien \(e_*=E_h+E_0\) und
\(e_*+\kappa/2\).

Nach einheitlicher Wahl der relativen Fermionphase wirkt die exakte
Kompression \(PHP\), abzüglich \(e_*\), wie

\[
 \begin{pmatrix}0&-\bar\tau Z\\-\tau Z&\kappa/2\end{pmatrix}
 \otimes I_{64}.
\]

Das Vorzeichen ist für die Population unerheblich. Das \(I_{64}\) zeigt,
dass die Rechnung für jeden normierten internen Überlagerungszustand gilt.
Die projizierten Fermionoperatoren sind Hubbard-Übergänge und keine
vollständige CAR-Algebra auf diesem 128-dimensionalen Band.

### 4.2 Die Lücke zum gesamten übrigen Raum

Die native, nicht nur perturbative Casimiridentität lautet

\[
 \sum_AP_A^\dagger P_A=\tfrac12(15N_f-C_{\rm Spin(10)}-C_{\rm SU(4)}).
\]

In einem Block \(N=n,N_b=b\) ist die rechte Seite höchstens
\(\tfrac{15}2(n-2b-\eta)\) mit \(\eta=n\bmod2\). Bei ungerader
Fermionzahl kommt der Casimir-Mindestwert 15 hinzu. Die Norm des
Boson-Erzeugungszeilenoperators auf dem Zielblock ist \(\sqrt{b+1}\).
Damit liefert die Blocknorm-Abschätzung eine skalare Jacobi-Untergrenze
mit Diagonale \(b\) und quadrierten Nebendiagonalen

\[
 a_b^2=\frac{15(b+1)(n-2b-\eta)}{800}
\]

in Einheiten \(\Delta=1\). Man nimmt negative Nebendiagonalen; die
Quadratformabschätzung benutzt die Normen der vollen Bosonzahlkomponenten
eines beliebigen Zustands, nicht einzelne Testvektoren.

Für **jedes \(n=65,\ldots,127\)** wurden sämtliche LDL-Pivots der
Vergleichsmatrix oberhalb \(-4/5\) exakt positiv nachgewiesen. Der erste
Bosonindex ist \(\lceil(n-64)/2\rceil\), der letzte \(\lfloor n/2\rfloor\).
Somit gilt \(H_n>-.8\Delta\) in allen 63 hohen Ladungssektoren.

Für alle \(n\le62\) liefert die Minimierung der Cauchy-Schwarz-Schranke

\[
 H_n/\Delta\ge-\frac{n-\eta}{4}(\sqrt{23/20}-1)>-1.121899.
\]

Jede andere Ladungsverteilung als (63,64) oder (64,63) enthält eine Bank
mit \(n\le62\) und eine mit \(n\ge65\). Ihre Gesamtenergie liegt also
oberhalb \(-1.921899\Delta\). Die elektrische Energie ist nichtnegativ.
Das obere Bandende von \(P\) ist kleiner als
\(-2.225448\Delta+\kappa/2\).

Für die beiden zentralen Ladungsverteilungen wurden außerdem die
Vergleichsmatrizen ab \(b=1\) bei \(n=63,64\) oberhalb \(-3/4\) erneut
rational geprüft. Durch Minmax mit Kodimension 64 beziehungsweise eins
ergeben sich die bekannten angeregten Energieböden; es wird nicht behauptet,
dass der exakte Spektralprojektor mit dem Null-Bosonenprojektor identisch ist.

Zusammen ergibt sich eine Lücke zwischen \(P\) und \(Q=I-P\) von mindestens

\[
 \boxed{\delta=.303549\Delta-\kappa/2>0.}
\]

Die anderen beiden Vergleichslücken sind
\(.345812\Delta-\kappa/2\) und \(.379636\Delta-\kappa/2\), also größer.
Diese Schranke umfasst **alle** Ladungsaufteilungen, Bosonzustände und
internen Moden des deklarierten physikalischen Sektors.

### 4.3 Gleichmäßige Auslaufkontrolle und endliche Transferzeit

Setze \(v=64|\tau|\) und fordere \(2v<\delta\). Sei \(a\) das obere
Eigenwertende von \(H_0|_P\). Minmax liefert ein Spektralband \(P'\) von
\(H\) derselben Dimension 128, dessen oberer Rand ≤\(a+v\) ist.
Die Kompression \(QHQ\) liegt ≥\(a+\delta-v\).

Mit \(Y=QP'\), als Abbildung aus \(\operatorname{Ran}P'\), gilt die
Sylvestergleichung

\[
 (QHQ)Y-Y(H|_{P'})=-QVP\,PP'.
\]

Die beiden Spektren sind geordnet und mindestens \(\delta-2v\) getrennt.
Die Lösung über das konvergente Exponentialintegral liefert
\(\|Y\|\le v/(\delta-2v)\): nach einem gemeinsamen Skalarshift ist der
Integrand durch \(v e^{-s(\delta-2v)}\) beschränkt. Wegen gleicher endlicher
Ränge gilt dieselbe Schranke für \(\|P'-P\|\).

Da \(P'\) mit \(H\) kommutiert, folgt zu **jeder** Zeit

\[
 \boxed{\|Qe^{-itH}P\|\le L:=\frac{2v}{\delta-2v}.}
\]

Aus der projizierten Schrödingergleichung und Duhamel folgt weiter

\[
 \|Pe^{-itH}\psi-e^{-itPHP}\psi\|
 \le |t|vL=:\eta(t),\qquad \psi\in P,\ \|\psi\|=1.
\]

Für den Zielprojektor \(P_R\subset P\) weichen die Wahrscheinlichkeiten
damit höchstens um \(2\eta(t)\) ab. Dies ist eine nichtperturbative
Fehlergrenze für die volle Entwicklung; nur der ausgewählte Kopplungsbereich
ist klein. Es handelt sich nicht um das Weglassen eines unbekannten
höheren Störungsterms.

### 4.4 Ein vollständig numerisch spezifizierter, rational zertifizierter Punkt

Mit \(\hbar=1\) wähle

\[
 \tau/\Delta=10^{-8},\quad \kappa/\Delta=10^{-10},
 \quad T:=t\Delta=169500000.
\]

Diese Zahlen sind ein konservativer Existenzpunkt, **keine aus TFPT
abgeleiteten Konstanten und keine Behauptung schneller oder optimaler
Übertragung**. Die physikalische Sekundenskala ist nicht bestimmt.

Die genaue komprimierte Rabi-Wahrscheinlichkeit ist

\[
 p_P(t)=\frac{|\tau|^2Z^2}{|\tau|^2Z^2+(\kappa/4)^2}
 \sin^2\!\left(t\sqrt{|\tau|^2Z^2+(\kappa/4)^2}\right).
\]

Für **jedes** zulässige unbekannte \(Z\) liegt der Winkel weniger als
0,08 von \(\pi/2\) entfernt. Das folgt aus \(Z_{\rm lo},Z_{\rm hi}\),
\(\sqrt{x^2+y^2}\le x+y^2/(2x)\) und rationalen Pi-Grenzen. Letztere
wurden zusätzlich mit der Machin-Identität und endlichen alternierenden
Arctan-Reihen eingeschlossen; Fließkomma-Pi ist keine Beweisvoraussetzung.

Mit \(\sin^2(\pi/2+u)\ge1-u^2\) folgt

\[
 p_P(T)>\left(1-\frac{\kappa^2}{16\tau^2Z_{\rm lo}^2}\right)
 (1-.08^2)>.993591982278.
\]

Die vollständigen Fehlergrenzen sind

\[
 L=\frac{25600}{6070954399}<4.216800\cdot10^{-6},
 \quad L^2<1.8\cdot10^{-11},
 \quad\eta(T)=\frac{2777088}{6070954399}<.000457438455.
\]

Also

\[
 \boxed{p_{\rm voll}(T)>p_P^{\rm lo}-2\eta(T)
 =\frac{25218291754002904578202303151726961}
 {25404324948782158166703488466197500}>.992677105368.}
\]

Die unbekannten \(E_0,E_h\) treten nur als gemeinsame Phase auf und müssen
für diese Schranke nicht genau ausgerechnet werden. Eine arbiträr hohe
Treue ist innerhalb des zusätzlichen Modells prinzipiell erreichbar: bei
bekanntem \(Z\), \(\kappa/|\tau|\to0\), \(|\tau|/\Delta\to0\) und
\(t\sim\pi/(2|\tau|Z)\) verschwinden sowohl Detuning als auch der Fehler
\(tv^2/\delta\). Das ist eine bedingte Grenzaussage mit wachsender Laufzeit,
kein ausführbares natives Optimierungsverfahren.

### 4.5 Dieselbe ursprüngliche Fermionantwort ohne anfänglichen Filter

Für
\(\psi_f=(f_{x,r}\Omega_x/\sqrt\nu)\otimes\Omega_y\otimes|0\rangle\)
gilt

\[
 \psi_f=\sqrt w\,|L,r\rangle+\sqrt{1-w}\,q,
 \quad q\in Q,\quad w=Z/\nu\ge Z_{\rm lo}/Z_{\rm hi}.
\]

Die Auslaufnorm in umgekehrter Richtung erfüllt ebenfalls
\(\|Pe^{-itH}Q\|\le L\), indem man die obige Schranke adjungiert und
die Zeit umkehrt. Der unerwünschte Anteil kann also nicht beliebig stark
destruktiv in das niedrige Zielband einstreuen. Mit der Dreiecksungleichung,
\(2\sqrt{w(1-w)}\le1\) und der gesondert geprüften Positivität vor dem
Quadrieren folgt

\[
 \boxed{\|P_Re^{-itH}\psi_f\|^2
 \ge w\,p_{\rm voll}^{\rm lo}-L
 >.897260353455>.897.}
\]

Damit ist **kein vorbereitender Projektor auf die isolierte Linie** nötig,
um eine starke Übertragungsaussage über die ursprüngliche Entnahmeantwort zu
erhalten. Noch benötigt werden die deklarierte geladene Präparation und der
zusätzliche Link. Die Aussage betrifft das niedrige Zielband; sie behauptet
nicht, dass die vollständige hochenergetische Restantwort ebenfalls formtreu
übertragen wird. Für diesen ungefilterten Anfangszustand gilt die extrem
kleine Auslaufwahrscheinlichkeit aus 4.3 nicht: Er startet bereits teilweise
außerhalb von \(P\).

## 5. Warum die Herkunftslücke nicht durch längeres Rechnen verschwindet

Sei \(\Pi_x=(-1)^{N_{f,x}}\) die lokale Fermionparität. Die bisher angegebenen
bankinternen Paarumwandlungen, Zahloperationen, zahlenerhaltenden
Symmetrielifts sowie reine Bosonverbindungen kommutieren mit jeder
\(\Pi_x\). Jede endliche Komposition, lineare Kombination, Adjungierung
und jeder durch solche Operatoren realisierte einzelne Messzweig tut das
ebenfalls. Starke beschränkte Grenzwerte bleiben im Kommutanten der Parität.

Der benötigte Link erfüllt dagegen
\(\Pi_xB=-B\Pi_x\) und \(\Pi_yB=-B\Pi_y\), während er die Gesamtparität
erhält. **Er liegt nicht in dieser bekannten lokalen geraden Algebra.**
Auch adaptives Wiederholen und Nachselektieren gerader Krauszweige kann
die Sektorgrenze nicht überwinden.

Die Voraussetzung „jeder realisierte Zweig ist gerade“ ist wesentlich.
Eine bloß paritätskovariante CP-Abbildung kann ungerade Krausoperatoren
besitzen. Der im Prüfer enthaltene Reset-Kanal auf einer Fermionmode ist
ein exaktes Gegenbeispiel zur unzulässigen stärkeren Behauptung.

Das beweist keinen universellen Unmöglichkeitssatz für den Compiler. Es
beweist, **welche neue Quelleneigenschaft gesucht werden muss**: eine
gerade Gesamtoperation, die bezüglich der zwei operational definierten
Teilbereiche ungerade ist, oder eine ursprüngliche Überlappung, durch die
die angenommene Zerlegung in unabhängig gerade Banken falsch war. Eine
andere bloße Clockphase oder weitere Boson-Paarumwandlung reicht nicht.

## 6. Was von der arithmetischen Untersuchung trägt

### 6.1 Eine einzelne endliche Bank ist nicht der volle Logarithmusgenerator

Quadratisches Ergänzen liefert mit der nativen Casimirnorm
\(\|\sum P_A^\dagger P_A\|\le480\)

\[
 H_{\rm nat}\ge\tfrac\Delta2N_b-C,
 \qquad C=960g^2/\Delta.
\]

Die externe Rechnung verwendet teilweise die schwächere Dreiecksgrenze
\(C=7680g^2/\Delta\), die ebenfalls gültig ist. Über Minmax, **nicht** eine
allgemeine Operator-Monotonie der Exponentialfunktion, folgen

\[
 N_H(E)\le2^{64}\binom{\lfloor2(E+C)/\Delta\rfloor+60}{60},
 \qquad \operatorname{Tr}e^{-\beta H}
 \le\frac{2^{64}e^{\beta C}}{(1-e^{-\beta\Delta/2})^{60}}.
\]

Das Zustandswachstum ist polynomial, während ein vollständiges Spektrum
\(E_*\log n+E_{\rm off}\), \(E_*>0\), exponentiell viele Zustände unter
wachsender Energie verlangt. Die ursprüngliche Bank kann dieses komplette
Spektrum daher nicht energieerhaltend mit nur affiner Skalenänderung tragen.
Diese Schranke widerlegt nicht jeden arithmetischen Untersektor, jede
nichtlineare Umparametrisierung oder jeden Nullstellenoperator.

Endlich viele solche Banken und endlich viele energetisch kontrollierte
Rotoren ändern den qualitativen Gegensatz nicht. Unendlich viele identische
Banken lösen ihn nicht automatisch: Bei gleichmäßig beschränkten lokalen
Anregungskosten divergiert bereits die globale Wärmespur. Ein geeigneter
relativer oder lokaler Spurbegriff wäre ein zusätzlicher Gegenstand.

### 6.2 Primzahlen können eine gewählte Dynamik organisieren, erzwingen sie aber nicht

Auf \(\ell^2(\mathbb N)\) kann man \(H_{\rm ar}|n\rangle=\log n|n\rangle\)
definieren. Die additive Primfaktorbesetzung erklärt dann die Eulerstruktur.
Der Definitionsbereich lautet \(\sum_n(\log n)^2|\psi_n|^2<\infty\).
Dass quantenstatistische Systeme mit Zeta-Zustandssumme existieren, ist
bereits ein Ergebnis von [Bost und Connes](https://alainconnes.org/wp-content/uploads/bostconnesscan.pdf).
Das ist ein relevanter Anschluss, nicht die fehlende native Herleitung.

Der gelieferte Cocycle \(c(m,n)=(-1)^{v_2(m)v_3(n)}\) ist assoziativ, weil
Bewertungen unter Multiplikation additiv sind. Für
\(T_m|n\rangle=c(m,n)|mn\rangle\) gilt
\(T_lT_m=c(l,m)T_{lm}\), insbesondere \(T_2T_3=-T_3T_2\).
Die unkontrollierten CP-Kanäle verlieren diese globale Phase und erfüllen
\(\mathcal E_l\mathcal E_m=\mathcal E_{lm}\). In kohärent kontrollierten
Wegen bleibt die relative Phase messbar. Das ist eine exakte Phasenstruktur,
aber kein Beweis einer Quellenauswahl dieses Cocycle oder von RH.

Strikt multiplikative Schritte \(m>1\) ergeben auch keine geschlossenen
Bahnen: \(n\mapsto mn>n\). Die Frequenz \(\log p\) eines Operators, eine
Bahnlänge \(r\log p\) und der Schwingungszeitraum \(2\pi/\log p\) müssen
auseinandergehalten werden. Hier hat der RH-Graph-Skill die Prüfung auf
Generator, Spur und Phase getrennt und eine bloße Analogieschließung verhindert.

### 6.3 Der RH-Zielsatz bleibt unbewiesen

Die vorgeschlagene Identität

\[
 \frac{\Xi(z)}{\Xi(0)}=\det(I-z^2A^{-2}),\quad
 \Xi(z)=\xi(\tfrac12+iz),
\]

für einen strikt positiven selbstadjungierten Operator \(A\) mit kompakter
Inverser und \(A^{-2}\) von Spurklasse wäre tatsächlich hinreichend:
Die gesamte rechte Funktion hat ihre Nullstellen nur bei reellen
\(\pm\lambda_j(A)\), einschließlich Multiplizitäten. Aber dieser Operator
und die gesamte Funktionsidentität sind **nicht konstruiert**. Ein Operator
mit lediglich den Imaginärteilen der Nullstellen wäre unzureichend.

Weder diese Prüfung noch die im externen Code bereits verwendete
Faktorisierung kleiner Testzahlen liefert einen neuen effizienten
Faktorisierungsalgorithmus, eine native Quantenoperation dafür oder eine
Lösung von P versus NP. Hylæan wurde in dieser Revision nicht neu geprüft.

## 7. Die lokale Polnäherung wird präziser, das relativistische Feld bleibt offen

Die externe Resolventenabschätzung ist korrekt: Im Kreis mit Radius
\(.1\Delta\) um den **tatsächlichen**, unbekannten negativen Pol \(-\epsilon\)
gilt

\[
 G(z)=\frac{Z}{z+\epsilon}+R(z),\qquad
 |R(z)|<.505213/\Delta.
\]

Der übrige Spektralträger ist mindestens \(.337373\Delta\) vom Pol entfernt.
Die relative Abweichung vom echten Polterm beträgt im Kreis unter 5,75 %.
Die Abschätzung setzt keine Intervallmitte anstelle von \(Z,\epsilon\) ein
und ist keine globale Vernachlässigbarkeit der Selbstenergie.

Aus v1.6.4 bleibt bestehen: Die exakte Zwei-Feld-Resolvente besitzt einen
nichtverschwindenden Rest \(\Sigma_2(z)\). Seine komplette Funktion ist
noch nicht bestimmt. Das neue kontrollierte Transportlemma benötigt sie
nicht vollständig, weil es den Rest durch eine Spektrallücke kontrolliert.

Ebenso bleibt der Feldtypentest bestehen: Der native antisymmetrische
Paartensor zusammen mit zwei gleichhändigen Weylfeldern und einem skalaren
Vermittler ergibt den verschwindenden Kanal. Ein symmetrischer Lorentz-
Spinortensor oder eine zusätzliche gleichgeladene zweidimensionale
Antisymmetriemarke eröffnet einen nichtverschwindenden Kanal, führt aber
zusätzliche Struktur ein. Ein internes Spin(10)-Spinorlabel ist kein
Lorentz-Weylindex. Der neue Link behebt diese Typfrage nicht.
Die Konventionen des bisherigen Tests sind mit der Primärübersicht von
[Dreiner, Haber und Martin](https://arxiv.org/abs/0812.1594) verbunden;
ein neuer vollständiger relativistischer Adapter wurde hier nicht konstruiert.

Die spätere Feldtypenprüfung in `LATE_AUDIT.md` zeigt außerdem einen
Lorentz-erlaubten Zwei-Ableitungs-Kandidaten für den symmetrischen
Spinortensor und widerlegt einen pauschalen (1,1)-Ausschluss: Der
Energie-Impuls-Tensor ist schon bei Dimension vier zulässig. Weder ein
gesunder nativer Feldadapter noch ein dynamischer Gravitonpol folgt daraus.

## 8. Während der Arbeit entdeckte Änderung: „Kommutant 7“ richtig einordnen

Die strikte Originalquellenprüfung stoppte korrekt, als eine andere Arbeit
den früheren nativen Bericht ergänzte. Der alte Stand mit Hash
`1062e13fe0fb79cce015657a7b4d40a61e9639922ff95fa60c689c0068c38ffc`
blieb eingefroren. Der gesonderte geänderte Entwurf hat Hash
`ab745e74b1232b1ddf35dd0e0d0da4ace0176c797d769e5db8bedd0010bcba6a`.
Die in dieser Revision verwendeten Energie- und Polzertifikate änderten
sich bei dieser Prüfung nicht. Der Fehlerbeleg wurde aufbewahrt.

Der neue Entwurf listet drei dunkle Darstellungstypen mit Dimensionen
24.000, 11.200, 2.688; drei helle mit 2.880, 576, 320; und einen χ-Typ mit 64.
**Unter Voraussetzung dieser Zerlegung** lässt sich seine Folgerung exakt
nachprüfen:

\[
 \mathcal H_{N=3}\simeq
 \bigoplus_{d\in D}V_d\ \oplus\
 \bigoplus_{b\in B}(\mathbb C^2\otimes V_b)\ \oplus V_\chi.
\]

Die Summe ist \(37888+2\cdot3776+64=45504\). Die drei hellen Typen
kommen im **vollen** Raum jeweils zweimal vor. Daraus folgen:

- Nur die Gruppenwirkung hat einen Kommutanten der Dimension
  \(3+3\cdot4+1=16\), nicht sieben.
- Werden zusätzlich die nichtverschwindenden hellen Paarmischungen und
  \(N_b\) als Operationen zugelassen, erzeugen sie die vollständigen
  \(M_2\)-Multiplizitätsalgebren. Dann bleiben sieben zentrale Skalare.
- Sieben ist **keine absolute Untergrenze für beliebige weitere Operationen**.
  Ein erlaubter Operator, der diese sieben Blöcke verbunden mischt, zwingt
  die sieben Skalarwerte zur Gleichheit und lässt nur einen übrig. Der
  endliche Inzidenzmatrix-Test hat Rang sechs und beweist dieses Gegenargument.
- Die Zerlegung allein beweist weder operative Verfügbarkeit der
  kontinuierlichen Symmetrie noch einen Einzelfermion-Link. Selbst alle
  bankinternen Symmetrieoperationen erhalten die lokale Fermionparität.

Der interessante Wert sieben wird dadurch nicht verworfen. Korrigiert
werden die Aussagen „voller N=3-Raum multiplizitätsfrei“, „absolute Grenze
für jede Operation“ und eine unbewiesene Gleichsetzung von Symmetrie und
verfügbarem Instrument. Die genaue Darstellungszerlegung selbst bleibt in
diesem Zusatz eine externe Voraussetzung, kein frisch reproduzierter Satz.

Der Debugging-Skill führte hier zur Versionsprüfung statt zum Ersetzen
eines Pins. Das neue Manifest trennt deshalb einen erfolgreichen
**eingefrorenen Quellenreplay** von `originals_unchanged=false`.

## 9. T1–T8: was dieses Ergebnis beiträgt und nicht beiträgt

Die Begriffe folgen der aktuellen offenen Problemliste und ihrer
Forschungszuordnung. Keine Akzeptanzmarkierung wurde heraufgesetzt.

| Tor | Fehlender Nachweis | Beitrag dieser Revision |
|---|---|---|
| T1 | Ursprung von P1/P2, Dimension, Compiler- und Zustandswahl | Bekannte gerade Operationsalgebra ist für Einzeltransport unzureichend; ursprüngliche Auswahl weiter offen |
| T2 | Tatsächlich halbgeladenes, markiertes E8-Feld samt Renormierung, Energie- und Adjungiertenkontrolle | Der Ladung-eins-Lochzustand ist kontrolliert, aber nicht mit dem fehlenden Half-Charge-Feld identifiziert |
| T3 | Ein gemeinsamer, aus TFPT ausgewählter lokaler unitärer 3+1D-Parent | Vollständiger bedingter Zwei-Banken-Transfertest; kein ausgewählter räumlicher Parent |
| T4 | Chirales SM-Maß, Anomalien/Index, gleichmäßige Spiegelentkopplung | Feldtyp-Widerspruch weiter sichtbar; kein chirales Maß |
| T5 | Wechselwirkender Kontinuumsübergang, Lorentzverhalten, Clustering, Confinement und Streuung | Endliche-Sektor-Fehlerkontrolle ist ein Baustein, aber kein räumlicher Grenzübergang |
| T6 | Interne Herleitung aller Eichkopplungen und vollständiger Neutrinotextur/-skala | Keine neue Herleitung; \(\tau,\kappa\) sind deklarierte Testparameter |
| T7 | Masseloser dynamischer Spin zwei, beide Helizitäten, universelle Kopplung im selben Parent | Offen; der neue pauschale Ausschluss eines Dimension-vier-(1,1)-Tensors wurde korrigiert |
| T8 | Physische Präparation/Anfangszustand und ein gemeinsames Quellfunktional aller Auslesungen | Anfänglicher Polfilter wird für >89,7 % unnötig; geladene Präparation und Messinstrument weiter offen |

## 10. Nächste entscheidende Arbeiten mit klaren Abbruchkriterien

**A. Die Quelle des geraden Gesamtlinks finden.** Nicht noch eine riesige
Kontrollmatrix bauen, sondern für jeden tatsächlich ursprünglichen Generator
\(O\) prüfen, ob \([O,\Pi_x]\ne0\) bei erhaltener Gesamtparität möglich ist.
Eine positive Antwort muss Generator, Teilbereichsdefinition, Hilbertraum,
Gaussreferenz und Matrixelement liefern. Bleiben alle Generatoren lokal
gerade, ist die Suche nach dem Link durch deren weitere Komposition beendet.
Dann muss die ursprüngliche Teilraumdefinition oder der Quellenvertrag
explizit geändert werden; man darf keinen Hopterm als Ergebnis ausgeben.

**B. Die ursprüngliche Entnahme als gemeinsames Instrument realisieren.**
Eine Referenzmode könnte Ladung erhalten, während \(f_r\Omega\) präpariert
und ausgelesen wird. Zu prüfen sind ihre Herkunft, Energiekosten,
Erfolgshäufigkeit und Erhaltung der internen Kohärenz. Der neue Satz entfernt
bereits die zusätzliche Pflicht eines perfekten anfänglichen Energiefilters.
Er entfernt nicht die Pflicht, ein geladenes Instrument auszuweisen.

**C. Den Feldtyp vor räumlichen Rechnungen entscheiden.** Entweder folgt ein
passender Lorentzträger wirklich aus derselben Quelle, oder der skalare
Weyl-Ansatz wird in seiner jetzigen Form verworfen. Eine bloße zusätzliche
Verdopplung ohne Herkunft ist ein Modellvorschlag, keine Ableitung.

**D. Erst dann viele Banken.** Der nächste räumliche Test benötigt dieselbe
Quelle, einen bestimmten Graphen, Lokalisierung der Operationen und mit dem
Volumen verträgliche Fehler- und Energiebounds. Ein einziges neues Linklemma
liefert weder Raumdimension noch Lichtkegel, chirale Materie oder Gravitation.

**E. Arithmetik getrennt scharf halten.** Eine echte Verbindung müsste eine
gemeinsame Quellabbildung mit Generator, Zustands-/Spurstruktur, Phasen und
Domänen liefern. Die volle signierte Weilform oder die ganze Determinanten-
identität bleibt das Beweisziel. Der bloße Auftritt von Primzahlen erfüllt
keines davon. Der globale RH-Index ließ sich wegen einer fehlenden
historischen Quelle und veränderter Review-Quellen nicht vollständig
aktualisieren; die gezielte Originalquellenprüfung ist enger als ein
frischer Gesamtindex. Es wurde kein RH-Abschlusskandidat registriert.

## 11. Reproduktion und ehrliche Liefergrenze

`replay.py --frozen-only` führt die fünf Prüfer normal und mit `-OO` aus,
vergleicht beide JSON-Ergebnisse und die zwei externen Originalberichte,
prüft alle eingefrorenen Quellen und protokolliert Änderungen der
Originalorte gesondert. Ein Fehler führt zu FAIL. Der zuvor aufgetretene
Live-Quellenfehler bleibt in `source_drift_failure_receipt.json` sichtbar.

Die abgesicherten Zahlen stehen vollständig rational in
`two_bank_transfer_normal.json`; Dezimalwerte dienen nur der Lesbarkeit.
Die analytische Beweiskette steht in Abschnitt 4. Das Paket umfasst die
unveränderten externen Arbeiten, deren Programme, die native v1.6.4-Abhängigkeit
und alle neuen Berichte. NumPy, SymPy und für das ältere native Paket dessen
separat dokumentierte Voraussetzungen sind zu unterscheiden.

Die versionierte ausführliche Markdown-Lieferung enthält zusätzlich den
vollständigen eingefrorenen nativen Herleitungsbericht v1.6.4 als historischen
Anhang. Daneben gibt es ein kurzes Update und eine bildliche Erklärung.
**Die großen TFPT-Haupt-PDFs und die Webseite werden in dieser Revision nicht
als aktualisiert ausgegeben. Es gab keinen Commit oder Push.**
