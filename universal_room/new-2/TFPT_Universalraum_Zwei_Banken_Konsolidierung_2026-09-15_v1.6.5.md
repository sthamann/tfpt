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


---

# Nachprüfung der beiden zuletzt eingegangenen Untersuchungen

Integrierter Nachtrag zu v1.6.5 · 15. September 2026

Quellen: die Anlagen `8e110ae1-19e2-4d47-bfc8-ebe4fe9ab81b` und
`b928b72a-6669-4c67-a75d-124095791c6f`, unverändert eingefroren. Zusätzlich
wurden die vier genannten Programme `t1_fixed.py`, `stabilizer.py`,
`t5_twobank.py`, `t5_varresp.py` vollständig gelesen und archiviert. Eine
eigene Nachrechnung prüft die kritischen Folgerungen; sie ist **kein
vollständiger Replay aller sechs Sonden** des fremden Arbeitsordners.

## 1. Übersicht: übernehmen, korrigieren oder offenlassen

| Neue Aussage | Ergebnis der Prüfung |
|---|---|
| Innerer Viererzyklus erhält alle 60 W-Kanäle | Bestätigt, jetzt einschließlich der richtigen Fermion-Vorzeichen und explizitem Bosonlift |
| Grundzustandseindeutigkeit/Singulett/Gaplücke weiterhin unbekannt | Überholter Stand: unter dem festgelegten nativen Vertrag bereits bewiesen; voller Vektor weiter unbekannt |
| Leerer Grundzustand für alle μ≥0 | Falsch; bei μ=0 liegt der eindeutige N=64-Grundzustand unter −1,129636Δ |
| Kommutant 7 als absolute Untergrenze | Nur im benannten blocktreuen erweiterten Operationsvertrag; siehe Hauptbericht Abschnitt 8 |
| Beliebige Einteilchenmatrix ist damit als natives Fock-Wort verfügbar | Nicht gezeigt; assoziative Matrixalgebra, Lie-Kontrolle und Fock-Lift sind verschiedene Fragen |
| Kanal-Variationszustand hat E=−0,0196Δ | Die angegebene Phase im Code ergibt gegen den gepinnten P=f_jf_i-Vertrag +0,05736Δ; ein relatives Vorzeichen korrigiert es |
| 99,892-%-Transfer bei t≈2484 | Numerisches Maximum eines Vierzustands-Paarmodells im untersuchten Zeitfenster; kein erster/globaler exakter Maximalsatz und kein nativer Einloch-Transfer |
| Gleiche Zweigableitungen genau bei ε=0 | Algebraisch richtig; die Eigenwertlücke bleibt dort √32·|g|, also kein allgemeiner „Kegel genau dann wenn gaplos“-Satz |
| SU(4)³-Anomalie =16 | Richtig unter A(4)=1 und der zusätzlichen Interpretation aller (16,4) als gleichhändige Weylfelder; Eichung ist eine weitere Voraussetzung |
| Gravitationsanomalie =64 | Keine reine perturbative Gravitationsanomalie in 3+1D; 64 kann bei zusätzlich deklarierter gleichgeladener U(1) die gemischte U(1)-Gravitationsanomalie zählen |
| Mit einer Ableitung kein (1,1)-Tensor bei Dimension ≤4 | Falsch: der Energie-Impuls-Tensor ist ein Gegenbeispiel; daraus folgt aber noch kein dynamisches Graviton |
| Kein lokaler kovarianter kinetischer Term für (1,0) | Zu pauschal: der bilineare Ein-Ableitungs-Term fehlt, ein Zwei-Ableitungs-Skalar existiert; Positivität/Constraints/Herkunft bleiben zu prüfen |

„Negativ geschlossene Route“ bedeutet nicht „T2, T3, T4 oder T7 geschlossen“.
Ein ausgeschlossener Ansatz beantwortet nicht die jeweilige physikalische
Existenzfrage. Die beiden gelieferten Texte widersprechen sich vor allem
beim bereits bewiesenen modellinternen Grundzustand; sie dürfen nicht als
gleichzeitig aktueller einheitlicher Status zitiert werden.

## 2. Positiver neuer Anschluss: der korrekt angehobene Viererzyklus

Die Abbildung der Fermionmarken lautet
\(p(4s+a)=4s+(a+1\bmod4)\). Auf Paaren ist zwingend das Exteriorvorzeichen
zu beachten: Falls \(p(i)>p(j)\), erhält das sortierte Paar ein Minuszeichen.
Der gelieferte `stabilizer.py` lässt dieses Zeichen weg. Das wäre im
Allgemeinen falsch; für den untersuchten Viererzyklus überlebt das positive
Resultat jedoch auch den korrekten Test.

Alle 60 W-Zeilen werden mit ihren Vorzeichen wieder auf W-Zeilen abgebildet.
Wir haben den zugehörigen signierten Bosonoperator \(R_b\) explizit gebildet
und exakt geprüft:

\[
 W'=R_bW,\qquad R_bR_b^T=I_{60},\qquad R_b^4=I_{60},
 \qquad R_b^2\ne I_{60}.
\]

Damit existiert ein **gemeinsamer nativer Tensor-Automorphismus** auf
Fermionen und Bosonen, nicht nur eine Übereinstimmung von Zeilenzahlen.
Die gleichzeitige Transformation erhält Paarwechselwirkung und Bosonzahl.
Sie beweist eine Ordnung-vier-Symmetrie, nicht deren operative Verfügbarkeit.

Dieser Permutationszyklus ist nicht die zentrale Matrix \(iI_4\) von SU(4).
Seine Determinante auf dem Viererfaktor ist −1. Mit einer zusätzlichen
Ladungsphase kann man geeignete Gruppenlifts vergleichen; die Permutation,
die zentrale Phase, der Clock und die geometrische Glue-Markierung sind
dadurch aber nicht schon identifiziert. Genau diese Intertwiner-Frage ist
ein sinnvoller neuer Anschluss, statt noch einmal nur vier zu zählen.

## 3. Warum der Einteilchen-Abschluss den Fock-Operationssatz nicht schließt

Die Irreduzibilität der Einteilchendarstellung kann ihre assoziative
Matrixalgebra zu \(B(\mathbb C^{64})\) machen. Daraus folgt nicht, dass jede
Matrix als ein zulässiges physisches Wort verfügbar ist, und auch nicht,
dass ihre zweite Quantisierung bereits erzeugt wird.

Ein kleinstes exaktes Gegenbeispiel zur falschen Liftregel:
\(A=|1\rangle\langle1|\), \(B=|2\rangle\langle2|\) auf zwei Moden.
Dann \(AB=0\), also \(d\Gamma(AB)=0\), aber
\(d\Gamma(A)d\Gamma(B)=n_1n_2\ne0\).
Der zweite Quantisierungsschritt ist ein Lie-, nicht ein assoziativer
Algebra-Homomorphismus dieser Art.

Auch \(\operatorname{diag}(i,1,1,1)\) und
\(\operatorname{diag}(i,i,1,1)\) haben Determinanten i beziehungsweise −1.
Ihre Zugehörigkeit zur **linearen Matrixalgebra** aus SU(4)-Generatoren und
Identität ist kein exaktes SU(4)-Gruppenwort. Projektive Gleichheit oder eine
zusätzliche U(1)-Phase kann helfen, muss aber mit der Bosonwirkung, Ladung
und Referenz gemeinsam ausgewiesen werden.

Der fremde Code folgert außerdem die Irreduzibilität des 37.888-dimensionalen
dunklen Dreifermionraums aus der vollen Einteilchenmatrixalgebra. Diese
Schlussregel ist nicht begründet. Bereits die im anderen neuen Text
angegebenen drei dunklen irreduziblen Typen widersprechen der pauschalen
Eins-Block-Lesart unter der bloßen Quellsymmetrie. Die Zahl 8.732.673 mag als
sehr schwache obere Schranke anderweitig verträglich sein; die im Code
angegebene Herleitung belegt sie nicht. Die SVD-/Toleranzprüfungen des Codes
sind zudem numerisch, nicht allein wegen „PASS“ exakte Lie-Beweise.

## 4. Zustandswahl: keine Rückkehr vor den abgesicherten Grundsatz

Der vorhandene native Satz beweist Eindeutigkeit, N=64, Singulett und
positive Lücke bei μ=0 im angegebenen Kopplungsbereich. Eine komplette
Clebsch-Gordan-Serie oder Voll-Diagonalisierung ist dafür nicht nötig;
Vergleichsungleichungen und Minmax waren gerade der einfache Ausweg.
Die physische Auswahl von H beziehungsweise μ=0 bleibt eine andere Frage.

Das grobe Sandwich \([-1.2,-.0196]\Delta\) ist nach einer Phasenkorrektur
zwar verträglich, aber wesentlich schwächer als
\((-1.158089,-1.129636)\Delta\). Es ist keine Verschärfung.

Im tatsächlich angegebenen Variationscode werden die Fermionen in der
Reihenfolge j, dann i gelöscht. Das liefert \(f_if_jF=-f_jf_iF\), während
der native Vertrag \(P_A=\sum W_{A,ij}f_jf_i\) verwendet. Bei unverändertem
\(g=+\Delta/20\) und den angegebenen Variationskoeffizienten folgt deshalb

\[
 E_{\rm Code}/\Delta=\frac12-\frac{23\sqrt3}{90}
 =+.057364793621\ldots,
\]

nicht der behauptete negative Wert. Mit korrigierter relativer Phase lautet
er \(1/2-3\sqrt3/10=-.019615242271\ldots\). Alternativ wäre eine konsequente
andere P/g-Phasenkonvention möglich; die Quelle muss sie dann überall führen.
Die gleichzeitige Einteilchendichte des einfachen Variationszustands bleibt
von dieser Phasenreparatur unberührt, weil seine Bosonzahlkomponenten
orthogonal sind. Sie ist keine dynamische Greenfunktion auf dem nativen
Grundzustand und ersetzt dessen schon kontrollierte Antwort nicht.

## 5. Feldtheorie: falsche Verbote entfernen, echte Bedingungen behalten

### 5.1 Anomalien

Für die zusätzlich angenommene 3+1D-Weylinterpretation lautet das lokale
Anomaliepolynom bis auf Konventionsvorzeichen

\[
 I_6=[\widehat A(T)\,\mathrm{ch}_R(F)]_6
 =\mathrm{ch}_3(F)-\frac{p_1(T)}{24}\,\mathrm{ch}_1(F).
\]

Der reine gravitative Anteil \([\widehat A]_6\) verschwindet; seine
Formgrade sind Vielfache von vier. Das ist die bekannte dimensionale
Unterscheidung bei [Álvarez-Gaumé und Witten](https://collaborate.princeton.edu/en/publications/gravitational-anomalies/).
Eine Spur-/Weylanomalie ist nochmals ein anderer Begriff.

Auf (16,4) ist der SU(4)-Kubikkoeffizient 16 bei Normierung A(4)=1.
Der exakte Test \(t=\operatorname{diag}(1,1,1,-3)\) hat
\(\operatorname{tr}t=0\), \(\operatorname{tr}t^3=-24\).
Ist SU(4) **dynamisch geeicht**, muss die vollständige Theorie diese
Eichanomalie kompensieren. Als globale Symmetrie kann sie eine
't-Hooft-Anomalie tragen; dann folgt keine pauschale Spiegelpflicht.
Ein vollständiger konjugierter Spiegel ist ein möglicher Ausgleich,
aber hier nicht als einzige oder allgemein minimale Lösung bewiesen.

„Gravitativ 64“ kann sinnvoll eine **gemischte U(1)-Gravitationsanomalie**
meinen, wenn alle 64 linksgetragenen Weylfelder explizit U(1)-Ladung eins
erhalten. Das muss samt Eich-/Globalstatus gesagt werden. Für SU(4) allein
ist der gemischte lineare Spurkoeffizient null. Die Quellenmarke N darf
nicht ohne Beweis in eine dynamisch geeichte chirale U(1) umgedeutet werden.

### 5.2 Der behauptete Spin-2-Ausschluss ist falsch

Die Lorentzdarstellungen liefern exakt

\[
 (\tfrac12,\tfrac12)\otimes(\tfrac12,\tfrac12)
 =(0,0)\oplus(1,0)\oplus(0,1)\oplus(1,1).
\]

Eine Ableitung des Vektorbilinears \(\psi^\dagger\bar\sigma_\mu\psi\)
kann daher einen symmetrischen spurfreien (1,1)-Tensor bilden. Insbesondere
hat der Energie-Impuls-Tensor
\(T_{\mu\nu}\sim i\psi^\dagger\bar\sigma_{(\mu}
\overleftrightarrow\partial_{\nu)}\psi\), mit passender Spurbehandlung,
Dimension \(3/2+3/2+1=4\). Ein Energie-Impuls-Tensor kann bereits in einer
festen Hintergrundraumzeit definiert werden; dynamische Diffeomorphismen
müssen nicht vorausgesetzt werden, um dieses Gegenbeispiel zu formulieren.

Das schließt **T7 nicht**. Ein vorhandener Tensor ist kein masseloser
Spin-2-Pol. Das sinnvolle Ziel ist später sein transversaler, spurfreier
Korrelator auf demselben räumlichen Parent, mit positiver Norm, beiden
Helizitäten und universeller Kopplung. Wir entfernen hier eine falsche
Darstellungsobstruktion, nicht die dynamischen Nachweispflichten.

### 5.3 (1,0)-Kinetik ist nicht generell verboten

Der bilineare Ein-Ableitungs-Term mit einem (1,0)-Feld und seinem Adjungierten
besitzt keinen Lorentzskalar. Mit zwei Ableitungen existiert aber etwa

\[
 \mathcal L_2\propto
 (\partial^{\alpha\dot\alpha}\Phi_{\alpha\beta})
 (\partial^{\beta\dot\beta}\bar\Phi_{\dot\alpha\dot\beta})
\]

für symmetrisches \(\Phi\). Alle Spinorindizes sind kontrahiert. Bei rein
zeitartigem Impuls ist sein Symbol proportional zu
\(\omega^2(|\Phi_{11}|^2+2|\Phi_{12}|^2+|\Phi_{22}|^2)\), also nicht
identisch null. Das ist ein Gegenbeispiel zum uneingeschränkten Satz „kein
lokaler kovarianter kinetischer Term“. Es beweist **nicht** Positivität des
vollen Hamiltonoperators, korrekte Constraints, gewünschte Freiheitsgrade
oder eine native Quelle. Diese bleiben die entscheidenden Tests.

## 6. Die Vierzustandsrechnung richtig lesen

Das Modell mit \(s=\sqrt8g\), Bosonverbindung η und Diagonalen (0,Δ,Δ,0)
erlaubt kohärenten **Paartransport**. Die exakte Identität
\((H^3)_{41}=8g^2\eta\) stimmt. Unsere unabhängige Fließkomma-Abtastung
reproduziert auf \([0,3000]\) mit Schrittweite .05 den größten gefundenen
Wert .998920021869 bei 2484.05. Der erste Gitter-Lokalhöchstwert liegt
bereits bei 6.05. Weder „erster Maximalzeitpunkt“ noch ein globales exaktes
Maximum ist damit bewiesen. Diese kleine Rechnung wird nicht mit dem
vollständigen Einloch-Satz des Hauptberichts verwechselt.

Für \(F_\pm(\epsilon)=(\epsilon\pm\sqrt{\epsilon^2+32g^2})/2\)
gilt \(F'_+-F'_-=\epsilon/\sqrt{\epsilon^2+32g^2}\). Bei ε=0 stimmen
die Ableitungen überein, aber die **Eigenwertlücke** beträgt
\(\sqrt{32}|g|>0\). Ein verschwindender nackter Vermittlerparameter und
eine verschwindende wechselwirkende Anregungslücke sind verschieden.
Ein allgemeiner relativistischer Kegelsatz oder ein zwingendes neues
Renormierungsprogramm folgt aus dieser Ableitungsidentität nicht.

## 7. Konsequenz für die nächste Forschungsrevision

Die sinnvollen positiven Anschlüsse sind jetzt schärfer:

1. Den expliziten Ordnung-vier-Lift mit dem tatsächlich markierten Clock
   und der Herkunft des A3-Index vergleichen: vollständige Intertwiner,
   Ladungsphase und Bosonwirkung, nicht nur Gruppennamen.
2. Einen Quellenoperator finden, der die lokale Parität beider operational
   bestimmten Teile gleichzeitig ändert. Die native Z4-Symmetrie selbst
   tut das nicht. Der kontrollierte Einloch-Transfer ist bereits als
   Akzeptanztest für einen solchen Operator verfügbar.
3. Den Zwei-Ableitungs-Feldkandidaten auf Positivität und Constraints prüfen,
   bevor er als relativistischer Adapter zählt. Ein bloßes Nichtnull-Symbol
   ist noch keine gesunde Feldtheorie.
4. Den Energie-Impuls-Tensor als zulässigen **Kandidaten** behalten, aber erst
   auf dem gemeinsam konstruierten räumlichen Träger nach einem dynamischen
   Spin-2-Pol suchen. Kein vorhandener Spin-2-No-go rechtfertigt hier das
   Aufgeben dieses Anschlusses.

62 zusätzliche Prüfbedingungen bestehen normal und optimiert identisch.
Exakte Identitäten, bedingte Darstellungsargumente und die numerische
Zeitfenstersuche sind im Ergebnisbericht getrennt. Der externe Status
„alle Restfragen geschlossen oder auf genau ein Stück reduziert“ wird
nicht übernommen. Die vollständige TOE bleibt offen.


---

# Historischer Beweisanhang: vollständiger nativer Herleitungsstand v1.6.4

Dieser Anhang bewahrt die frühere Herleitung vollständig. Seine damaligen Statussätze werden durch die aktuelle Konsolidierung und den Nachtrag oben ergänzt; er ist kein ungeprüft übernommener neuer Gesamtstatus. Die externe laufende Symmetrieergänzung wurde separat geprüft und ist nicht unbemerkt in diesen eingefrorenen Anhang eingegangen.

# TFPT / Universalraum: nativer Pol, Bewegungsgleichung und minimale Feldtypen

**Konsolidierte Forschungsfortsetzung v1.6.4 · 15. September 2026**

Diese Revision verbindet den während der Arbeit neu eingegangenen Polsatz
v1.6.3 mit einer unabhängig begonnenen Untersuchung der nativen
Bewegungsgleichung. Sie ergänzt die bisherigen Hauptdokumente; sie ist
keine verkürzte Neufassung des vollständigen Hauptbuchs. Die vorhandenen
Haupt- und Update-PDFs wurden in dieser Runde nicht verändert.

## 1. Ergebnis in einem Satz

Auf dem abgesicherten Grundzustand des festgelegten nativen Fockmodells
existiert eine isolierte ursprüngliche Fermion-Entnahmelinie; nach
Kombination beider Rechnungen trägt sie **mehr als 88,007628 % des gesamten
normierten Spektralgewichts pro Mode**. Die zusätzliche Antwort ist jedoch
nicht exakt auf eine einzige weitere Linie reduzierbar. Ihr erster
Rückwirkungsschritt wird direkt von derselben ursprünglichen Wechselwirkung
bestimmt.

Am Prüfpunkt \(g/\Delta=1/20\), ausdrücklich ohne \(\mu N\)-Zusatz:

| Größe | Eingegangene v1.6.3 | Konsolidierte strengere Grenze |
|---|---:|---:|
| Mittlere Bosonenzahl | \(0.77<\bar b<1.45\) | \(0.842846<\bar b<1.245656\) |
| Energie der niedrigen Entnahmelinie | \(0.007737<\epsilon/\Delta<0.062277\) | \(0.007737<\epsilon/\Delta<0.039079764\) |
| Gewicht dieser Linie im gesamten CAR-Maß | \(Z_{\rm low}>0.864972353\ldots\) | \(Z_{\rm low}>0.880076280689\ldots\) |
| Obere Gewichtsgrenze | \(Z_{\rm low}<0.9759375\) | \(Z_{\rm low}<0.9736610625\) |
| Übrige Entnahmeenergien | \(>0.379636\Delta\) | unverändert |
| Sämtliche Additionsenergien | \(>0.329636\Delta\) | unverändert |

Die Dezimalzahlen sind gerundete Darstellungen rationaler Schranken.
Es sind weder exakte Polpositionen noch angepasste Zentralwerte. Der Pol
steht im retardierten Spektrum bei negativer Frequenz \(-\epsilon\).
Das niedrige Niveau im N=63-Hilbertraum ist 64-fach entartet; jede
diagonale Modenantwort sieht dieselbe Linie.

**Nicht bewiesen:** die physische Herleitung des Hamiltonoperators, sein
vollständiger Operationssatz, native Präparation, räumliche Ausbreitung,
ein vollständiges relativistisches Feldwörterbuch oder eine TOE. T1–T8
bleiben als vollständige Aufgaben offen.

## 2. Ein unveränderter Modellvertrag

Es werden keine Hopping-, Massen-, Ladungs- oder Projektionsglieder zu H
hinzugefügt:

\[
H=\Delta N_b+g(Q_++Q_-),\quad Q_+=\sum_A b_A^\dagger P_A,
\quad Q_-=Q_+^\dagger,
\]
\[
P_A=\sum_{i<j}W_{A,ij}f_jf_i,\quad N=N_f+2N_b,
\quad WW^\dagger=8I_{60}.
\]

Es gibt 64 CAR-Fermionmoden, 60 CCR-Bosonmoden und 480 von null
verschiedene reelle W-Einträge mit ihren ursprünglichen Vorzeichen.
\(\Delta>0\), g ist reell; die Zahlen beziehen sich auf \(g/\Delta=1/20\).
Die Tensorquelldatei ist durch SHA-256
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`
fixiert.

Die Fockrealisierung, H, der sektorenübergreifende Energievergleich und
der Prüfparameter sind weiterhin Modellvoraussetzungen. Die geometrische
oder arithmetische Herkunft eines W-Tensors leitet diese Voraussetzungen
nicht allein her. Insbesondere sind die fünf elementaren CAR in einer
Spinor-Matrixkonstruktion nicht mit den hier verwendeten 64 Fockmoden
gleichzusetzen.

## 3. Was tatsächlich erneut geprüft wurde

### 3.1 Grundzustand: frische Berechnung statt bloßer Statusübernahme

Die ursprünglichen Programme wurden mit fixierten Dateihashes in eine
eigene Arbeitskopie übernommen. Die Paar-Konfigurationen wurden frisch
mit neu kompiliertem Quellcode berechnet:

| Ordnung | Vollständig enumerierte Bosonkonfigurationen | Normquadrat von \(Q_+^kF\) |
|---|---:|---:|
| 0 | analytischer Ausgangszustand | 1 |
| 1 | 60 Kanäle / 480 Paare | 480 |
| 2 | 1830 | 439680 |
| 3 | 37820 | 575078400 |
| 4 | 595665 | 952296652800 |

Zusätzlich wurden unabhängige Wortentwicklungen, Überlaufgrenzen, die
vollständige Zweikörper-Casimiridentität, rationale Sektorvergleiche und
die unabhängige Symmetriespurrechnung wiederholt. Die vier ausgewählten
ursprünglichen Zertifikate bestehen normal und unter `-OO` mit identischen
JSON-Bytes. Dies ist eine gezielte erneute Grundzustandsprüfung, nicht die
Behauptung, alle historischen Repository-Tests erneut ausgeführt zu haben.
Der unveränderte alte Normprüfer gibt unter dem aktuellen NumPy eine
ComplexWarning bei der Ganzzahlkonversion aus. Die neuen Prüfer bestätigen
vor jeder Konversion exakt verschwindende Imaginärteile und ganzzahlige
Realteile des gepinnten W. Die Warnung ist gespeichert und wird nicht
als verlorener Tensoranteil oder als unterdrückter Prüffehler ausgegeben.

Der modellinterne Satz bleibt bestehen: Für
\(0<|g|/\Delta\le1/20\) ist der globale Grundzustand \(\Omega\)
eindeutig, hat N=64 und ist Spin(10)×SU(4)-invariant. Am Zahlenprüfpunkt:

\[
-1.158089\Delta<E_0<-1.129636\Delta,
\qquad \operatorname{gap}(H)>0.007737\Delta.
\]

Der volle Grundzustandsvektor ist damit nicht ausgerechnet. Die fünf
Versuchsvektoren sind keine behauptete invariante Fünferbasis für H.

### 3.2 Das neu eingegangene Polergebnis

Der vollständige technische Bericht v1.6.3 und sein 248-zeiliger Prüfer
wurden gelesen; Quellen, Bericht, Ergebnismatrix und Prüfpaket wurden
unverändert archiviert. Der Prüfer wurde normal und optimiert wiederholt:
**317 Prüfbedingungen, identische JSON-Bytes auch zum gelieferten Bericht**.

Der Herkunftspin des Prüfers ist
`fdbcabd244450c302182086d67c68284634c994e3fee026200c42c508f731654`.
Er verwendet denselben ursprünglichen `verify_hole.py`-Quellstand wie
die bisherige Fortsetzung. Die neuen eigenen Sektorvergleiche wurden
zusätzlich unabhängig mit rationalen LDL-Pivots berechnet.

Die Prüfzahlen zählen auch Komponenten und Wiederholungen; sie sind
keine Zahl unabhängiger Entdeckungen. Die analytischen Argumente sind
ausgeschrieben, aber nicht vollständig in einem Beweisassistenten formalisiert.

## 4. Der einfache native Anschluss: Bewegungsgleichung statt Umdeutung

Erweitere jede W-Zeile zur antisymmetrischen Matrix \(M_A\) mit
\((M_A)_{ij}=W_{A,ij}\) für i<j. Definiere

\[
D_r=\sum_{A,j}(M_A)_{rj}b_Af_j^\dagger,
\qquad \phi_r=D_r/\sqrt{15}.
\]

Direkte CAR/CCR-Normalordnung liefert **Operatoridentitäten auf dem
endlichen Teilchenkern**, nicht nur Gleichheiten auf Testzuständen:

\[
\boxed{[H,f_r]=-gD_r,\qquad [H,f_r^\dagger]=gD_r^\dagger,}
\]
\[
[N,D_r]=-D_r,\qquad \{f_r,D_s^\dagger\}=0.
\]

Der neue Vergleichsoperator hat also dieselbe Ladung −1 wie f.
Er ist nicht das früher auf dem leeren Referenzzustand betrachtete
\(\chi^\dagger\sim b^\dagger f^\dagger\) mit Ladung +3.
Auf dem Grundzustand liegen \(f\Omega\) und \(D\Omega\) in N=63,
\(\chi^\dagger\Omega\) dagegen in N=67. Neutrale Zeitentwicklung
hebt diese Unterscheidung nicht auf.

Die Normalordnungsprüfung erfasst alle 64 ursprünglichen f-Operatoren
und die tatsächlichen W-Vorzeichen. Für die Kompositnorm gilt exakt

\[
\{D_r,D_s^\dagger\}=
\sum_{A,B,j,k}(M_A)_{rj}(M_B)_{sk}
\left(\delta_{AB}f_j^\dagger f_k+\delta_{jk}b_B^\dagger b_A\right).
\]

Mit \(\bar b=\langle N_b\rangle\) und der Grundzustandssymmetrie:

\[
\langle\{D_r,D_s^\dagger\}\rangle=\delta_{rs}S,
\qquad S=15-\frac7{32}\bar b.
\]

\(\phi\) hat entsprechend Norm \(1-7\bar b/480\), nicht globale
kanonische CAR. Der normierte Zustandserwartungswert ersetzt keine
Operatorrelation.

## 5. Dieselbe Antwort auf demselben Grundzustand

Für Im z>0 und \(H_n=H|_{N=n}\):

\[
G_{rs}(z)=\langle\Omega|f_r(z+E_0-H_{65})^{-1}f_s^\dagger|\Omega\rangle
+\langle\Omega|f_s^\dagger(z-E_0+H_{63})^{-1}f_r|\Omega\rangle.
\]

Die innere Symmetrie macht G diagonal und alle Diagonalelemente gleich.
Schreibe mit positiven Entnahme- und Additionsmaßen auf \(\epsilon>0\)

\[
G(z)=\int\frac{d\nu_+(\epsilon)}{z-\epsilon}
+\int\frac{d\nu_-(\epsilon)}{z+\epsilon}.
\]

Dann gelten exakt

\[
Z_+=\bar b/32,\quad Z_-=1-\bar b/32,
\quad a:=\int\epsilon\,d\nu_+=\int\epsilon\,d\nu_-
=\frac{\Delta\bar b-E_0}{64}.
\]

Für das gesamte signierte Spektralmaß:

\[
\boxed{m_0=1,\quad m_1=0,\quad m_2=g^2S,\quad
m_3=g^2(\Delta S+7a).}
\]

Die ersten beiden Momente und die Kanalgewichte stimmen mit der
eingegangenen unabhängigen Rechnung überein. **Das dritte Moment ist der
zusätzliche eigene Schritt dieser Revision.**

### 5.1 Herleitung des dritten Moments

Setze \(\mathcal L A=[A,H]\). Stationarität macht diesen Operator
symmetrisch in der positiven, nach Nullvektoren quotientierten Metrik
\((A,B)=\langle\{A^\dagger,B\}\rangle\). Direkte Normalordnung ergibt

\[
\sum_r\{[D_r,X],D_r^\dagger\}=-14Q_+.
\]

Die beiden Beiträge sind \(16Q_+\) und \(-30Q_+\). Ihre Koeffizienten
folgen aus den vollständig geprüften Kontraktionen
\(\sum_{rj}M_{A,rj}M_{B,rj}=16\delta_{AB}\) und
\(\sum_{Ar}M_{A,rj}M_{A,rk}=15\delta_{jk}\).
Mit \([D,N_b]=D\) und
\(\langle Q_+\rangle=(E_0-\Delta\bar b)/(2g)\) folgt die Formel.

Als unabhängige Kontrolle wurden sämtliche Formeln einschließlich m3
an der früher exakt geschlossenen N=4/N=5-Antwort symbolisch geprüft.
Diese Kontrolle verwendet den früheren Referenzzustand nur als Test
der Identitäten, nicht als Ersatz für den nativen Grundzustand.

Die allgemeine Methode, Spektralmomente aus Bewegungsgleichungen zu
gewinnen, ist etabliert; siehe
[Freericks und Turkowski, Phys. Rev. B 80, 115119](https://arxiv.org/abs/0907.1284).
Die hier angegebenen W-Kontraktionen und Konstanten wurden eigenständig
für dieses Modell berechnet; die zitierte Arbeit beweist keine TFPT-Aussage.

### 5.2 Neue engere Dichte- und Gewichtsgrenzen

Positivität der beiden Antwort-Grammatrizen beziehungsweise zweimal
Cauchy–Schwarz liefern

\[
m_2\ge a^2\left(\frac1{Z_-}+\frac1{Z_+}\right),
\]
\[
\boxed{(\Delta\bar b-E_0)^2\le
60g^2\bar b(32-\bar b)(1-7\bar b/480).}
\]

Mit der bereits bewiesenen Energieobergrenze und \(g/\Delta=1/20\)
muss das folgende rationale Polynom positiv sein:

\[
P(b)=\frac7{3200}b^3-\frac{61}{50}b^2
+\frac{317591}{125000}b-\frac{79754843281}{62500000000}>0.
\]

Seine beiden im alten zulässigen Bereich liegenden Nullstellen liegen
bei ungefähr 0.842846697 und 1.245655664. Exakte rationale Wurzelisolation
ergibt die nach außen gerundete strenge Schranke

\[
\boxed{0.842846<\bar b<1.245656.}
\]

Damit:

| Größe pro Mode | Strenges offenes Intervall |
|---|---:|
| Gesamtes Additionsgewicht | (0.0263389375, 0.03892675) |
| Gesamtes Entnahmegewicht | (0.96107325, 0.9736610625) |
| \(\langle\{\phi,\phi^\dagger\}\rangle\) | (0.981834183333…, 0.987708495833…) |
| Frühere \(\chi\)-Kompositnorm, nicht \(\phi\) | (0.040386370833…, 0.059687683333…) |

Das sind Erwartungswerte und integrierte Spektralgewichte, keine direkten
Nachweise von Produktionsraten oder von bereits verfügbaren Messinstrumenten.

## 6. Der Polsatz und seine zusätzliche Verschärfung

Der eingegangene Beweis verwendet
\(u_{k,r}=Q_+^kf_rF=f_rQ_+^kF\). Invarianz und Besetzung ergeben

\[
\langle u_{k,r},u_{k,s}\rangle=
\delta_{rs}\frac{64-2k}{64}\|Q_+^kF\|^2.
\]

Die Normen lauten 1, 465, 412200, 521164800, 833259571200.
Die daraus gebildete fünfdimensionale Variationsmatrix gibt 64 unabhängige
Richtungen unter \(-1.095812\Delta\). Das gesamte N=63-Komplement des
Nullbosonraums liegt über \(-3\Delta/4\). Minimax begrenzt den niedrigen
Raum auf genau 64 Dimensionen; seine injektive symmetrieverträgliche
Projektion auf die irreduzible duale 64 erzwingt ein einziges Energieniveau.

Das beweist Existenz und Isolation. Seine Sichtbarkeit folgt aus den
positiven Entnahmemomenten. Mit

\[
d=0.007737\Delta,\quad c=0.379636\Delta,
\quad a_{\max}=\frac{1.245656+1.158089}{64}\Delta
\]

gilt

\[
Z_{\rm low}>\frac{c(1-1.245656/32)-a_{\max}}{c-d}
=\frac{40912436089}{46487375000}
=0.8800762806891118\ldots.
\]

Außerdem ist der niedrige Pol die kleinste Entnahmeenergie. Daher
\(a\ge\epsilon_{\rm low}Z_-\), also bereits ohne vollständige
Polauswertung

\[
\frac{\epsilon_{\rm low}}\Delta
<\frac{1.245656+1.158089}{64-2(1.245656)}
=\frac{2403745}{61508688}=0.039079763821332\ldots.
\]

Diese Verschärfungen entstehen aus dem **Zusammenführen kompatibler
Beweise**, nicht aus einem neuen gewählten Parameter. Das Restgewicht
des gesamten CAR-Maßes ist somit kleiner als 0.119923719311… .

## 7. Einfache Organisation, aber keine falsche Zwei-Linien-Lösung

Die ersten zwei orthonormalen Operatoren sind f und \(D/\sqrt S\).
Die erste Resolventenreduktion hat deshalb die exakte Form

\[
\boxed{G(z)=\frac1{z-\displaystyle\frac{g^2S}{z-a_1-\Sigma_2(z)}}},
\qquad a_1=\Delta+\frac{7a}{S}.
\]

\(\Sigma_2\) ist die Resolvente des verbleibenden nativen Operatorraums,
gekoppelt an den dazu orthogonalen Rest von
\(\mathcal L(D/\sqrt S)\). Es wurde kein äußeres Bad hinzugefügt.
Dies ist eine genaue Ordnung der Rechnung, **keine abgeschlossene
Berechnung von \(\Sigma_2\)** und keine Vereinigung sämtlicher TOE-Aufgaben
in einer einzigen bereits gelösten Funktion.

### 7.1 Warum man die Rückwirkung nicht exakt weglassen darf

Angenommen, es gäbe nur je eine Entnahme- und Additionslinie mit
Energien \(\epsilon_-,\epsilon_+\). Symmetrie macht diese für alle r gleich.
Dann liefern die Bewegungsgleichungen auf demselben Grundzustand

\[
D_r\Omega=-\frac{\epsilon_-}{g}f_r\Omega,
\qquad D_r^\dagger\Omega=\frac{\epsilon_+}{g}f_r^\dagger\Omega.
\]

Summe nach Multiplikation mit \(f_r^\dagger\) beziehungsweise \(f_r\)
und N=64 ergeben

\[
H\Omega=\left[-32\epsilon_-+
(\Delta-\epsilon_++\epsilon_-)N_b\right]\Omega.
\]

Ein Eigenzustand mit negativer Energie kann keine feste Bosonenzahl haben:
Dann wäre \(\langle Q_++Q_-\rangle=0\) und seine Energie
\(\Delta\langle N_b\rangle\ge0\). Daher sind \(\Omega\) und
\(N_b\Omega\) unabhängig. Die angenommene Zweilinienform erzwingt
\(\epsilon_+-\epsilon_-=\Delta\).

Andererseits geben \(m_0=1,m_1=0\) für ein Zweilinienmaß
\(m_3/m_2=\epsilon_+-\epsilon_-\). Die exakt bestimmte Formel lautet
jedoch

\[
\frac{m_3}{m_2}=\Delta+7a/S>\Delta.
\]

Widerspruch. Damit ist \(\Sigma_2\not\equiv0\) bewiesen. Mindestens
ein Kanal besitzt mehr als eine Energielinie. Der dominante isolierte
Entnahmepol und diese unvermeidliche Reststruktur widersprechen einander nicht.
Eine Zweilinienform könnte höchstens eine zu zertifizierende Näherung sein.

## 8. Was der Operationssatz jetzt tatsächlich hergibt

| Vertrag | Mathematisch abgesichert | Nicht dadurch verfügbar |
|---|---|---|
| Markierter endlicher Matrixcompiler | Matrizen, Ordnungen, konkrete endliche Syntheseidentitäten | Vollständiges Fockinstrument, Präparation, physischer Zeitgenerator |
| H allein | Modellzeitentwicklung | Unabhängiges Schalten von X und \(N_b\) |
| X und \(N_b\), wenn als Kontrollen gewährt | N=3-Kontrollalgebra der Dimension 14 | Beliebige Modenoperationen |
| Zusätzlich dokumentierter vorzeichenrichtiger Clock-Lift | N=3-Kontrollalgebra der Dimension **84** | Vollständige Zustandsunterscheidung oder Ladung-eins-Instrument |

Die neue Clock-Rechnung wurde übernommen und reproduziert. Die fünf
Multiplizitätszeilen für die sechs Clockphasen sind:

| Teilraum | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| Dunkle F3 | 6384 | 6280 | 6280 | 6384 | 6280 | 6280 |
| Dunkle BF | 16 | 8 | 8 | 16 | 8 | 8 |
| Aktiv 7 | 560 | 440 | 440 | 560 | 440 | 440 |
| Aktiv 10 | 112 | 88 | 88 | 112 | 88 | 88 |
| Aktiv 12 | 80 | 40 | 40 | 80 | 40 | 40 |

Die aktiven Zeilen tragen zusätzlich einen Zweiniveaufaktor. Alle 45504
N=3-Zustände sind erfasst; der Kommutant hat weiterhin Dimension
240742144. Die alte Zahl 14 beschreibt den engeren Zweikontrollvertrag,
nicht den jetzt zusätzlich geprüften Clockvertrag.

### 8.1 Konkrete Präparationsgrenze

Alle genannten Fockkontrollen erhalten N. Ein Wort aus ihnen und jeder
einzeln zahlenerhaltende ausgewählte Messzweig bleiben im Ausgangssektor.
Sie können aus dem leeren N=0-Zustand **nicht** den N=64-Grundzustand
erzeugen. Diese Aussage betrifft zahlenerhaltende Krauszweige; eine bloß
U(1)-kovariante offene Dynamik kann sehr wohl geladene Krausoperatoren haben.

Auch aus dem voll besetzten F führt bloßes \(e^{-itH}\) nicht zur
Konvergenz auf \(\Omega\): Der Grundzustandsüberlapp bleibt konstant.
Normiertes \(e^{-\tau H}F\) konvergiert mathematisch mit der bewiesenen
Lücke, benötigt aber eine gesonderte Instrument- und Ressourcenherleitung.

### 8.2 Der kleinste konkrete Ladungstest

Ein Kandidat ist eine explizite Referenzmode c mit
\(T=\lambda(c^\dagger f_r+f_r^\dagger c)\). Sie erhält die gemeinsame
Ladung, verändert aber die Ladung der ursprünglichen Bank. Der endliche
Austausch- und Detuningtest ist exakt; **dieses T wurde nicht als neuer
nativer Hamiltonterm eingeführt**.

Für dieselbe N=64-Präparation unter \(H+\mu N\) gilt
\(G_\mu(z)=G_0(z-\mu)\), insbesondere \(m_1=\mu\).
Das misst nur gegen eine festgelegte Referenz: Ein gemeinsamer Zusatz
\(\mu(N_{\rm Bank}+N_{\rm Referenz})\) bleibt unsichtbar. Die Spektral-
schranken dieses Berichts gelten als Grundzustandsschranken nur für μ=0.

## 9. Relativistisches Wörterbuch: Ausschluss und zwei präzise Alternativen

Die Indexfrage darf nicht nachträglich durch einen Namen beantwortet werden.
Die Konventionen für Zweikomponentenspinoren wurden mit
[Dreiner, Haber und Martin](https://arxiv.org/abs/0812.1594) abgeglichen;
die folgenden speziellen W-Tests sind eigene exakte Tensorrechnungen.

### 9.1 Was nicht funktioniert

Für 64 gleichhändige Weylfelder mit innerem Index I und einen skalaren
Vermittler ist \(M_A\otimes\varepsilon_{\rm Lorentz}\) symmetrisch.
Die Grassmann-Antisymmetrisierung verschwindet daher identisch, für alle
60 W-Zeilen. Außerdem lässt die volle irreduzible innere Darstellung
\(16\otimes4\) auf denselben 64 Komponenten nach Schur keine zusätzliche
kommutierende nichttriviale Lorentzspinorwirkung zu.

### 9.2 Bereits bekannter nichtverschwindender Typ

Ein symmetrischer Lorentzspinortensor koppelt an das antisymmetrische M.
Der Vermittler hat dann einen passenden dualen (1,0)-Typ samt adjungiertem
Typ. Diese Variante besteht den algebraischen Nichtnulltest, aber noch
keinen vollständigen Kinetik-, Positivitäts-, Constraints- oder Herkunftstest.

### 9.3 Neue minimale skalare Alternative — ausdrücklich zusätzlich

Will man zugleich W, gleiche Weylhand, lokale Bilinearität und einen
skalaren Vermittler behalten, kann man einen **unabhängigen** Hilfsindex
a=1,2 mit alternierender Form einführen:

\[
b_A^\dagger(M_A)_{IJ}\varepsilon_{ab}
\varepsilon_{\alpha\beta}\psi_{I a\alpha}\psi_{J b\beta}
+\mathrm{h.c.}
\]

M und \(\varepsilon_{ab}\) sind jeweils antisymmetrisch; ihr Produkt
ist als innerer Kopplungstensor symmetrisch. Zusammen mit der Lorentz-
Epsilonform ist der Gesamttensor antisymmetrisch und nicht null.
Alle 60 Kanäle bestehen den Test. Eine nichtverschwindende alternierende
Form existiert nicht in Dimension eins; in Dimension zwei ist sie bis
auf Normierung eindeutig. **In dieser eng benannten Klasse von
Tensorfaktor-Reparaturen ist die binäre Ergänzung minimal.**

Das ist noch keine gefundene native Lösung: Sie verdoppelt die inneren
Weylkomponenten von 64 auf 128, zusätzlich zu deren Lorentzspinorindex.
Ein Double-Cover-Minuszeichen stellt nicht automatisch zwei unabhängige
Felder bereit. Auch Nambu-Umbenennung \((f,f^\dagger)\) genügt nicht:
Das gemischte Produkt hat Ladung null statt −2, sodass derselbe
\(b^\dagger ff\)-Ladungsvertrag nicht erhalten bleibt.

Der entscheidende Quellenauftrag ist daher eng: Gibt es diese zweite
gleichgeladene, CAR-unabhängige Komponente bereits im tatsächlichen
Compilerprozess? Und liefert ihre Projektion genau das bisherige H und
die geprüfte Antwort? Ohne beides bleibt die skalare Alternative ein
zusätzliches Modell, nicht eine Erklärung des ursprünglichen.

## 10. Nächste Schritte mit eindeutiger Erfolgskontrolle

1. **Native Quelle des Austauschoperators bestimmen.** Ein tatsächliches
   Operationswort mit Anfangszustand, Detektor, Adjungiertem, Ladungsbilanz
   und Record angeben. Ein weiteres neutrales Wort oder bloßer
   Algebraabschluss schließt diese Aufgabe nicht.
2. **Den Rest der nativen Antwort kontrollieren.** Das nächste Ziel ist
   \(\Sigma_2\) beziehungsweise sein erster Norm- und Momentkoeffizient,
   gemeinsam in N=63,64,65. Die vorliegenden Summenregeln und Polschranken
   sind zwingende Akzeptanztests. Den Rest auf null zu setzen ist exakt
   ausgeschlossen; eine Näherung braucht eine Restfehlergrenze.
3. **Die beiden Feldtypen an der Quelle entscheiden.** Entweder der
   symmetrische Vermittler mit korrektem Adjungierten und Kinetik, oder
   der skalare Typ mit wirklich nachgewiesener zweiter Komponente.
   Erst Nichtnullkopplung, Symmetrie, Ladung, CAR und positive Kinetik
   gemeinsam zählen als Feldadapter.
4. **Erst danach zwei operational bestimmte Teile verbinden.** Für einen
   tatsächlich hergeleiteten ungeraden Austausch wäre das projizierte
   Ein-Loch-Transfermatrixelement proportional zum jetzt eingeschlossenen
   Residuum. Ein solches formales Matrixelement beweist weder Verfügbarkeit
   des Austauschs noch einen isolierten Zweibank-Gesamtraum oder höhere
   Störungsordnungen. Eine räumliche Skalierung wurde hier nicht vorgezogen.

| Tor | Nutzen dieser Revision | Entscheidender verbleibender Nachweis |
|---|---|---|
| T1 | Exakter Clock-Kontrollabschluss und engere Ressourcenfrage | Ursprüngliches vollständiges Operations- und Rahmenwörterbuch |
| T2 | Geladene native Antwort, sichtbarer Pol, drittes Moment | Quelleneinbettung und renormiertes Half-Charge-Feld mit Energie/Adjungiertem |
| T3 | Präzise Anforderung an ungeraden Austausch | Gemeinsamer operationaler räumlicher, schließlich 3+1D-Träger |
| T4 | Falscher Skalartyp ausgeschlossen, minimale Alternativen | Chirales Maß, Anomalien, Spiegelkontrolle, vollständige Feldkinetik |
| T5 | Pole und Reststruktur lokal kontrolliert | Gemeinsamer wechselwirkender Grenzwert, Clusterstruktur, Streuung |
| T6 | Strengere interne/Lorentz-Indexbilanz | Familien, Massen und Kopplungen auf demselben physikalischen Träger |
| T7 | Keine neue Spin-2-Konstruktion | Dynamischer Spin 2, Helizitäten und universelle Kopplung |
| T8 | Eindeutiger Modellgrundzustand; Präparationslücke konkret | Primitive Zustandswahl, Ressourcen, Records und Instrumente |

## 11. Erratum und Versionsdisziplin

Im eigenen v1.6.2-Text fehlte in Abschnitt 5.2 zwischen Entnahme- und
Additionsresolvente ein Pluszeichen. Richtig ist auf der dortigen
N=4-Referenz
\(G=Z_h/(z+\epsilon_h)+a^\dagger(z+E_--H_5)^{-1}a\).
Die früheren Prüfrechnungen verwendeten die additive CAR-Gewichtsregel;
der Darstellungsfehler wird hier ausdrücklich korrigiert. Die archivierte
v1.6.2 wird nicht stillschweigend umgeschrieben.

Die zugelieferte v1.6.3 bleibt ebenfalls unverändert. Ihre Pol- und
Clockbefunde sind als übernommene und frisch reproduzierte Ergebnisse
kenntlich. Die engeren Schranken, das dritte Moment, der Ausschluss der
exakten Zweilinienantwort und die minimale skalare Hilfsindexalternative
sind die eigenen zusätzlichen Ergebnisse dieser Konsolidierung.
Kein literaturweiter Neuheitsanspruch, keine experimentelle Bestätigung
und kein Gesamtabschluss werden behauptet.
