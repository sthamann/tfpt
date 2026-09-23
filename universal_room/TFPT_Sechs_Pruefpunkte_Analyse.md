# TFPT und Universalraum: sechs Prüfpunkte, explizite Konstruktionen und Grenzen

**Stand: 14. September 2026.** Grundlage ist das hochgeladene Forschungsbuch `TFPT_Universalraum_Gesamtdarstellung_2026-09-14.pdf`, insbesondere die gedruckten Seiten 17 bis 20, 27 bis 34, 39 bis 45 und 48 bis 50. Die folgenden eigenen Rechnungen benutzen keine Originaldateien des darin beschriebenen Repositorys. Sie sind unabhängige endliche Rekonstruktionen und neue Anschlussrechnungen. Es wurde kein Hardwareexperiment ausgeführt.

## Ergebnis in einem Absatz

Die sechs Aufgaben sind sachlich richtig gestellt. Konkrete Fortschritte sind möglich: Eine ausdrücklich festgelegte Belegungsregel beseitigt die Kreuzterme verschiedener Bindungen in zweiter Ordnung; geteilte harmonische Vermittler erzeugen trotzdem einen berechenbaren Vierkörperbeitrag in vierter Ordnung. Ein isolierter Vermittlerbaustein liefert unter einer bestimmten Pulsfläche einen exakten Swap ohne verbleibende Vermittlerbesetzung. Im ausdrücklich kontrollierten idealen Austauschmodell besitzt ein nativer Viererstern einen exakten Spektralfilter, der die Präparation von Omega mit Wahrscheinlichkeit 1/6 statt 3/32 ermöglicht. Auf dem ursprünglichen Clebsch Graphen lässt sich eine tatsächliche Einanregungsausbreitung vollständig lösen. Die abstrakte E8 Naht kann einschließlich Gitterphasen, Adjunktion und Operatorprodukten angegeben werden. **Nicht gezeigt ist, dass diese algebraische Naht und eine gemeinsame Raumzeit aus demselben mikroskopischen Prozess entstehen.**

Das Paket trennt deshalb drei Rollen: einen mikroskopischen Vermittlungskandidaten, ein ideales endliches Austauschmodell und eine abstrakte chirale Gittertheorie. Sie sind keine drei austauschbaren Beschreibungen einer bereits bewiesenen gemeinsamen Quelle.

## 1. Quellenvertrag: festgelegte Regeln statt verborgener Stellschrauben

### 1.1 Was Eindeutigkeit hier bedeutet

Ein primitiver Vertrag darf Axiome besitzen. Seine Axiome müssen aber vollständig benannt sein. Eine feste Zahl als Eingabe ist etwas anderes als ein Parameter, der erst nach Kenntnis der Zielausgabe gewählt wird. Zusätzlich sind zwei Fragen zu trennen:

**Ausführbarkeit:** Bestimmt die gewählte Quelle die Antwort auf jedes ausdrücklich zugelassene Experiment?

**Herkunft:** Erzwingt die vorhandene TFPT Struktur gerade diese Quelle, oder wurde unter mehreren kompatiblen Möglichkeiten gewählt?

Das Forschungsbuch widerlegt die einfache Herkunftsbehauptung bereits anhand verschiedener symmetrischer Kontextgewichte und verschiedener Hamiltonoperatoren mit demselben Zustand Omega. Unsere Vermittlungsrechnung liefert einen weiteren Zeugen: Bei festem führendem Austausch J kann die Vermittlerenergie Delta geändert werden. Der Vierkörperbeitrag verändert sich dann, obwohl die führende Paarformel gleich bleibt.

### 1.2 Der explizite mikroskopische Kandidat

Die 16 Ortslabels sind

\[
\mathcal S=\{s\in\{\pm\tfrac12\}^5:\text{gerade Zahl negativer Einträge}\}.
\]

Die lexikografische Reihenfolge ist festgelegt. Zwei Labels bilden eine Kante, wenn ihr Hammingabstand vier beträgt. Das Kantenlabel ist r=s+s', also einer der zehn Vektoren ±e_i. Es entstehen 40 Kanten. Jeder der zehn Vermittlertypen wird von vier disjunkten Kanten benutzt.

An jedem Ort gibt es vier fermionische Farbmoden. Die kanonische Reihenfolge der 64 Moden lautet `4*site+color`. Der Zustandsraum ist der hart projizierte CAR Raum mit höchstens einem Fermion pro Ort. Dazu kommen 60 harmonische bosonische Vermittlermoden: zehn Vektorlabels mal sechs antisymmetrische Farbpaare. Fest ist der Gesamtladungssektor

\[
\sum_s n_s+2\sum_{r,A}n_{r,A}=16.
\]

Für i<j und a<b wird der Vertex vollständig festgelegt:

\[
K_{ij,ab}=c_{j,b}c_{i,a}-c_{j,a}c_{i,b}.
\]

Die CAR Vorzeichen folgen aus der angegebenen Modenreihenfolge. Jeder angezeigte Kantenkoeffizient ist in diesem Referenzmodell +t. Die harte Projektion wird bei den Operatoranwendungen berücksichtigt. Damit gilt im einfach besetzten Paarraum

\[
\sum_{a<b}K_{ij,ab}^{\dagger}K_{ij,ab}=I-S_{ij}=2P^-_{ij}.
\]

Der Hamiltonoperator lautet

\[
H_{\rm mic}=\Delta\sum_{r,A}b_{r,A}^{\dagger}b_{r,A}
+t\sum_{(i,j),A}\left[b_{r(i,j),A}^{\dagger}K_{ij,A}
+K_{ij,A}^{\dagger}b_{r(i,j),A}\right].
\]

Die Referenzwerte sind Delta=1 und t=1/20. Sie sind gesetzte dimensionslose Referenzdaten. Als Referenzdichte für die Elimination dienen einfach besetzte Orte mit Farbdichte `(I4/4)^tensor16` und Vermittlervakuum. Die Elimination selbst wird auf dem gesamten einfach besetzten Unterraum formuliert.

`microscopic_operator.py` implementiert die tatsächlichen Matrixspalten dieses Operators einschließlich sämtlicher Übergänge, Besetzungsfaktoren und CAR Vorzeichen. Es wird keine vollständige große Matrix angelegt. Eine Ressourcengrenze bricht ab, statt amplitudenweise zu truncieren. Getestet sind ausgewählte Matrixspalten, Ladungserhaltung, Besetzung, Hermitizität und eine vollständige Spalte der Rechnung in zweiter Ordnung.

**Nicht hergeleitete Eingaben:** fermionische Statistik, harte Besetzung, harmonische Vermittler, t/Delta, die vorgegebene Dichte und der physische Steuerzugriff. Die positiven Referenzvertizes sind nicht mit dem ursprünglichen phasentreuen TFPT Adapter identifiziert. Die Ortsinterpretation samt Besetzungsprojektion ist insbesondere kein Beweis voller kontinuierlicher D5 Kovarianz.

### 1.3 Die übrigen Rollen bleiben getrennt

Das ideale Spinmodell hat den exakten Operator

\[
H_C=J\sum_{(i,j)\in E(C)}P^+_{ij}
\]

auf 16 Ququarts mit ausdrücklich zusätzlichen Qubitregistern. Lokale Eingänge, Ticks, ausgewählte kontrollierte Austauschpulse, Registerinitialisierung und Born Auslesung sind primitive Zugriffe. Das ist eine vollständig deklarierte endliche Testquelle, aber bei endlichem t/Delta nicht identisch mit H_mic.

Die E8 Gittertheorie ist eine dritte, algebraische Referenz. Sie gibt vor, welche Naht eine behauptete physische Rekonstruktion tatsächlich reproduzieren müsste. Sie wird nicht einfach an das Spinmodell angehängt und anschließend als dessen abgeleiteter Grenzwert bezeichnet.

Der Prüfer ist an den SHA256 des genauen Quellenvertrags gebunden. Eine veränderte deklarative Annahme wird nicht stillschweigend ignoriert: Der Lauf verweigert dann die Prüfung bis zu einer bewusst überarbeiteten Version. Dies ist ein versionierter ausführbarer Prüfvertrag, keine universelle Sprache zum Interpretieren beliebiger neuer Theorien.

## 2. Vermittlung: zweite Ordnung, exakte Pulse und der Vierkörperterm

### 2.1 Z4 Typen und Besetzung

Die algebraischen Zielgrade sind

\[
\mathfrak g_0=(45,1)\oplus(1,15),\quad
\mathfrak g_1=(16,4),\quad
\mathfrak g_2=(10,6),\quad
\mathfrak g_3=(\overline{16},\overline4).
\]

Gleichgradige Spinorvertizes haben Grad 1+1=2; ein Spinor und sein konjugierter Grad haben 1+3=0. Eine passende Gradbuchhaltung allein beweist noch nicht die vollen E8 Intertwiner des gewählten physikalischen Fockmodells.

Sei P der Projektor auf einfach besetzte Orte ohne Vermittler. Nach einer Paarannihilation auf einer Kante e liegen genau an deren Endpunkten Löcher. Bei verschiedenen Kanten e und f unterscheiden sich diese Lochmuster. Wegen der festen Besetzung kann eine anschließende Paarerzeugung auf f das alte Muster nur für f=e wiederherstellen. Daher verschwinden die Kreuzbeiträge

\[
P K_e^{\dagger}K_fP=0\qquad(e\ne f)
\]

in der betreffenden zweiten Ordnung. Die gemeinsame Vermittlerbezeichnung löscht die Information über die Löcher nicht aus.

Daraus folgt

\[
H^{(2)}=-\frac{t^2}{\Delta}\sum_e K_e^\dagger K_e
=\frac{2t^2}{\Delta}\sum_eP_e^++\text{Konstante}.
\]

Das schließt die Belegungslücke dieser konkreten Rechnung. Es erklärt nicht, warum gerade diese Belegung fundamental gewählt sein sollte.

### 2.2 Konkurrierende Kanäle

Für einen isolierten antisymmetrischen Kanal mit W†W=P− ist

\[
 j(g,\Delta)=\frac{\sqrt{\Delta^2+4g^2}-\Delta}{2}.
\]

Gibt es zusätzlich einen unabhängigen symmetrischen Kanal, wird die relative Austauschenergie

\[
J_{\rm rel}=j(g_-,\Delta_-)-j(g_+,\Delta_+).
\]

Ihr Vorzeichen ist somit nicht durch den Namen E8 ausgewählt. Das Referenzmodell setzt den zusätzlichen symmetrischen Vermittler ausdrücklich auf abwesend. In einem vollständigen Ursprung wäre dessen Abwesenheit zu beweisen oder sein Beitrag mitzuführen.

### 2.3 Exakter Swap aus einem einzelnen Vermittler

Der isolierte 22 dimensionale Baustein ist

\[
H_{22}=\begin{pmatrix}0&gW^\dagger\\gW&\Delta I_6\end{pmatrix},
\qquad W^\dagger W=P^-.
\]

Im symmetrischen Zehnerraum passiert nichts. Jeder antisymmetrische Zustand bildet mit seinem Vermittlerzustand einen Zweiniveauraum. Setzt man

\[
g=\frac{\sqrt3}{2}\Delta,\qquad
\tau=\frac{2\pi\hbar}{\Delta},
\]

ist die Rabi Aufspaltung 2 Delta. Nach der Pulsdauer kehrt jede Vermittleramplitude auf null zurück; der antisymmetrische Eingang erhält das Vorzeichen minus eins. Deshalb wirkt auf dem ursprünglichen Paarraum exakt

\[
e^{-iH_{22}\tau/\hbar}=P^+-P^-=S,
\]

wobei die Gleichung als Wirkung auf Eingänge ohne Vermittlerbesetzung zu lesen ist, nicht als Identität der gesamten 22 dimensionalen Matrix mit einer 16 dimensionalen Matrix.

Ein Pointer, der diese Kopplung konditioniert, liefert entsprechend einen kontrollierten Swap. Hier ist keine niederenergetische Näherung nötig. Zusätzliche Voraussetzungen bleiben die Isolation der Kante, die konditionierte Amplitude und die Pulsfläche. Insbesondere ist der starke Puls nicht derselbe Betriebsmodus wie die schwache Referenz t/Delta=1/20.

### 2.4 Ein gemeinsamer Vermittler erzeugt einen echten Vierkörperbeitrag

Betrachte zwei disjunkte Kanten mit gleichem Vektorlabel und denselben sechs harmonischen Farbvermittlern. Jede besetzte antisymmetrische Kante trägt einen Sechserraum. Im niedrigen 36 dimensionalen Paarraum zerlegt die Vertauschung der beiden Sechserräume diesen in einen symmetrischen Teil der Dimension 21 und einen antisymmetrischen Teil der Dimension 15.

Für den symmetrischen Teil genügt der exakte Block

\[
M_s=\begin{pmatrix}
0&\sqrt2g&0\\
\sqrt2g&\Delta&2g\\
0&2g&2\Delta
\end{pmatrix}.
\]

Sein charakteristisches Polynom lautet

\[
E^3-3\Delta E^2+(2\Delta^2-6g^2)E+4\Delta g^2=0.
\]

Der niedrige Zweig ist

\[
E_s=-\frac{2g^2}{\Delta}+\frac{4g^6}{\Delta^5}+O(g^8).
\]

Im antisymmetrischen Teil gibt es keine entsprechende symmetrische Doppelbesetzung desselben Bosonenraums. Der niedrige Zweig ist

\[
E_a=\frac{\Delta-\sqrt{\Delta^2+8g^2}}2
=-\frac{2g^2}{\Delta}+\frac{4g^4}{\Delta^3}
-\frac{16g^6}{\Delta^5}+O(g^8).
\]

Ein einzelner besetzter Bond hat

\[
E_1=-\frac{g^2}{\Delta}+\frac{g^4}{\Delta^3}
-\frac{2g^6}{\Delta^5}+O(g^8).
\]

Nach Abzug der zwei getrennten Bondenergien verbleiben in vierter Ordnung die Beiträge minus 2g^4/Delta^3 beziehungsweise plus 2g^4/Delta^3. Als Operator auf den beiden antisymmetrischen Paarträgern ist dies

\[
\boxed{H^{(4)}_{\rm verbunden}
=-\frac{2g^4}{\Delta^3}S_6
=-\frac{8t^4}{\Delta^3}S_6.}
\]

S6 vertauscht hier die **zwei zusammengesetzten Sechserräume**, nicht zwei einzelne Ququarts. Außerhalb der beiden antisymmetrischen Paarträger wird dieser verbundene Beitrag mit null fortgesetzt. Das Vorzeichen hängt vom symmetrischen beziehungsweise antisymmetrischen kombinierten Zustand ab. Es wäre falsch, lediglich einen stets negativen Skalar mal P−P− daraus zu machen.

Der vollständige lokale Zweibondraum besitzt 129 Zustände: 36 ohne Vermittler, 72 mit einem Vermittler und 21 mit zwei Vermittlern. Seine numerischen Eigenwerte bestätigen die 21 plus 15 niedrigen Zweige. Die Reihenkoeffizienten sind zusätzlich symbolisch geprüft.

Bei festem führendem J=2t²/Delta lautet der Koeffizient -2J²/Delta. Delta bleibt also durch J allein unbestimmt und verändert eine physische Mehrkörperausgabe. Das ist ein konkreter Herkunftsgegenbeleg gegen die Gleichsetzung „gleicher führender Austausch = gleicher Ursprung“.

Dies ist eine Rechnung eines ausgewählten verbundenen Clusters, **nicht** der gesamte effektive Operator des voll gekoppelten C16 in vierter Ordnung. Weitere Cluster, Interferenzen und mögliche zusätzliche Vermittler sind dort nicht ausgewertet.

### 2.5 Eine exakte Form, die keine höheren Ordnungen versteckt

Für den gesamten endlichen Mikrokandidaten kann man ohne Truncierung den energieabhängigen Schurkomplementoperator verwenden. Mit Q=I-P und PHP=0 gilt bei existierender Resolvente

\[
H_F(E)=-PVQ(QHQ-E)^{-1}QVP.
\]

Die niedrigen Eigenwerte erfüllen H_F(E)u=Eu. Dieser Ausdruck hält sämtliche höheren Prozesse fest, statt sie nach dem Paarterm zu vergessen.

Eine konservative eigene Fehlerabschätzung ist möglich. Setze v=||V|| und nehme v<Delta an. Dann liegen die p=dim(P) niedrigen Eigenwerte bei E≤0, der Q Block ist mindestens Delta-v positiv und |E|≤v²/(Delta-v). Die Vermittlerparität lässt den Beitrag mit drei V Faktoren verschwinden. Die Resolventenidentität ergibt deshalb

\[
\|H_F(E)-H^{(2)}\|
\leq\frac{2v^4}{\Delta^2(\Delta-v)}.
\]

**Beweisskizze:** Schreibe B=QH0Q-E und VQ=QVQ. Dann

\[
(B+V_Q)^{-1}=B^{-1}-B^{-1}V_QB^{-1}
+B^{-1}V_QB^{-1}V_Q(B+V_Q)^{-1}.
\]

Der mittlere Beitrag verschwindet zwischen PVQ und QVP wegen der Parität der Vermittlerzahl. Der letzte Beitrag ist höchstens v^4/[Delta²(Delta-v)]. Der Unterschied von B^-1 zu (QH0Q)^-1 ist, nach Einsetzen der Energieschranke, durch denselben Betrag begrenzt. Die angegebene Summe folgt. Sie begrenzt insbesondere den Abstand eines solchen E zum Spektrum von H^(2).

Die Voraussetzung betrifft die **gesamte Operatornorm**, nicht lediglich einen kleinen Wert pro Kante. Für den voll gekoppelten Referenzwert t/Delta=1/20 wurde v<Delta nicht zertifiziert. Die Schranke darf dort deshalb nicht als bereits erfülltes globales Fehlerbudget ausgegeben werden.

Die allgemeine rigorose Einordnung von effektiven Hamiltonoperatoren und verbundenen Clustern liefert Bravyi, DiVincenzo und Loss [E1].

### 2.6 Kein erzwungener Vergleich mit dem falschen Graphen

Die Zweizellenformel des Buchs gehört zu zwei vollständigen Tetramern mit einer Brücke. Der Clebsch Graph enthält keine Dreiecke und daher keinen vollständigen Vierergraphen. Die Formel bleibt ein korrekter externer Vergleichsfall für einen tatsächlich so geschalteten Operator. Sie ist kein notwendiger Eigenwerttest des nativen Clebsch Modells. Auch eine gleichgewichtete Clebsch Kopplung ist keine uniforme eindimensionale Kette.

## 3. Exakte Präparation und vollständige Registerstatistik

### 3.1 Ein Viererstern existiert im ursprünglichen Graphen

Wähle einen Clebsch Knoten und drei seiner Nachbarn. Da keine Dreiecke existieren, ist der induzierte Graph ein Stern. Während der lokalen Präparation werden die übrigen Kopplungen durch den ausdrücklich angenommenen Kontrollzugriff ausgeschaltet.

Im idealen Spinmodell gilt

\[
H_\star=J(P^+_{01}+P^+_{02}+P^+_{03}).
\]

Sein vollständiges Spektrum, jeweils mit Multiplizität, lautet

\[
\{0^{[1]},(J/2)^{[30]},J^{[45]},(3J/2)^{[40]},
(2J)^{[15]},(5J/2)^{[90]},(3J)^{[35]}\}.
\]

Die Summe der Multiplizitäten ist 256. Der Kern ist genau C Omega. Der ganzzahlige Operator M=2Hstar/J erfüllt eine überprüfte Polynomidentität:

\[
\prod_{j=1}^{6}(jI-M)=720|\Omega\rangle\langle\Omega|.
\]

Damit ist der Kernprojektor nicht bloß numerisch identifiziert.

### 3.2 Ein exakter Filter mit drei Kontrollbits

Setze

\[
U=\exp[-i\pi H_\star/(2J)].
\]

Die möglichen Phasen sind achte Einheitswurzeln. Da M nur die Ganzzahlen 0 bis 6 enthält und nur ein Zustand den Wert null hat, folgt

\[
\boxed{\frac18\sum_{k=0}^7U^k=A_4=|\Omega\rangle\langle\Omega|.}
\]

Die Schaltung initialisiert drei Kontrollbits in 000, wendet auf jedes ein Hadamard an, führt die konditionierten Potenzen U, U² und U⁴ aus und wendet nochmals die drei Hadamards an. Alle Bits werden gemessen; allein das Ergebnis 000 zählt als Erfolg. Keine Fouriertransformation mit weiteren Phasen ist für diesen einen Erfolgszweig nötig.

Die übrigen Zweige sind ebenfalls fest:

\[
K_r=\frac18\sum_{k=0}^7(-1)^{r\cdot k}U^k,
\qquad \sum_rK_r^\dagger K_r=I.
\]

Das Skalarprodukt r·k ist das binäre Skalarprodukt der drei Bits, nicht gewöhnliche ganzzahlige Multiplikation.

### 3.3 Präparationsausbeute und Grenze

Für den Eingang des Buchs

\[
\chi_0=\frac{|01\rangle-|10\rangle}{\sqrt2}
\otimes\frac{|23\rangle-|32\rangle}{\sqrt2}
\]

gilt |<Omega|chi0>|²=1/6. Der neue Filter erreicht deshalb Präparationserfolg 1/6 und Misserfolg 5/6. Die acht vollständigen Kontrollausgänge haben in der dokumentierten Bitreihenfolge die Wahrscheinlichkeiten

\[
(1/6,1/6,0,0,1/6,1/6,1/6,1/6).
\]

Die Nullzweige zählen weiterhin zum festgelegten Instrument. Der Buchfilter hatte Kprep=(3/4)A4 und deshalb Erfolg 3/32. Die neue Ausbeute ist um den Faktor 16/9 größer.

Für jede Instrumentenfamilie, deren Krausoperatoren mit A4 kommutieren, kann die aufsummierte Erfolgswahrscheinlichkeit einer exakten Omega Ausgabe nicht über dem anfänglichen Omega Anteil liegen. Denn für alle Erfolgszweige mit Bild in A4 gilt K=A4 K A4; aus der Instrumentnormierung folgt die Grenze Tr(A4 rho). Der neue Filter saturiert diese Grenze für chi0. Sie gilt nicht für beliebige zusätzliche nichtinvariante Kühlung, Zustandsersetzung oder andere Hilfsressourcen.

### 3.4 Register und Endauslesung

Der binäre Pointer zeichnet den Swap mit

\[
V=H_R F_{R;01}H_R,\qquad V^2=I
\]

auf. Der erste reduzierte Schritt ist bei behaltenem und frischem Register gleich. Anschließend wird entweder ausdrücklich derselbe kohärente Pointer oder ausdrücklich ein zweiter frischer Pointer verwendet.

Der originale Dreierzyklus liefert weiterhin die bedingten Rückkehrwerte 1 und 17/32. Der lokale CNOT liefert 1 und 1/2. Die Varianten sind getrennte vorab definierte Experimente, keine nach dem Ausgang angepasste Registergeschichte.

Mit neuem Präparationsfilter und neuem **exakten A4 Endfilter** ergeben sich pro begonnenem Versuch:

| Variante | Präparation misslingt | Präparation gelingt, Endfilter misslingt | Beide Filter gelingen |
|---|---:|---:|---:|
| Pointer behalten | 5/6 | 0 | 1/6 |
| Frischer Pointer, ursprünglicher Tick | 5/6 | 5/64 | 17/192 |
| Frischer Pointer, CNOT Tick | 5/6 | 1/12 | 1/12 |

Jede Zeile summiert sich zu eins. Die bedingten Rückkehrwerte dürfen nicht mit der letzten Spalte verwechselt werden.

Die ursprünglichen Rohwerte aus dem Buch bleiben archiviert: 27/512 gegen 459/16384, beziehungsweise 27/512 gegen 27/1024 in der ausgeglichenen Variante mit den alten Filterfaktoren. Der neue Vorschlag ändert nicht nachträglich deren Vertrag.

### 3.5 Die Nichtstabilizer Ressource ist nicht verschwunden

Der neue Filter verwendet konditionierte kontinuierliche Austauschdynamik. Gerade diese ist eine zusätzliche Ressource gegenüber einem bloßen Clifford Baukasten. Die Schaltung leitet sie nicht aus E8 her. Ebenso sind die Registerinitialisierung, die lokale Zugriffserlaubnis und der Messprozess gesetzte Bestandteile des Referenzmodells.

Die mathematische Kompaktheit des Spektralfilters ist keine automatische Hardwarekostenreduktion: Kontrollierte Potenzen eines Hamiltonoperators können auf einer realen Plattform teuer und fehleranfällig sein. Das vollständige ursprüngliche Schaltungsexportpaket wurde hier nicht neu kompiliert.

## 4. Die E8 Naht: vollständiger algebraischer Zielgegenstand, fehlender physischer Ursprung

### 4.1 Gitter und Hilbertraum

Die konkrete Erweiterung ist

\[
L_0=D_5\oplus D_3,\qquad
L=L_0+\mathbb Z(\tfrac12,\ldots,\tfrac12).
\]

Das Gitter L ist positiv, gerade und unimodular vom Rang acht. Es hat 112 ganzzahlige und 128 halbzahlige Wurzeln der Norm zwei. Eine explizite Gitterbasis und die Grammatrix stehen in `results.json`.

Ein algebraischer Träger ist

\[
\mathcal H=\mathcal F_{\rm osc}^{(8)}\otimes\ell^2(L),
\]

mit orthonormaler Ladungsbasis |lambda>, positivem Oszillatorraum und Vakuum |0>. Der algebraische gemeinsame Definitionsbereich besteht aus endlichen Linearkombinationen von Zuständen mit endlich vielen Oszillatoranregungen.

### 4.2 Cocycles, Adjunktion und Operatorprodukte

Sei G die ganzzahlige Grammatrix der im Paket angegebenen Wurzelbasis. Definiere

\[
B=\operatorname{tril}(G,-1)+I,\qquad
\epsilon(m,n)=(-1)^{m^TBn}.
\]

Bilinearität liefert für alle Gitterkoordinaten die Cocycle Gleichung

\[
\epsilon(m,n)\epsilon(m+n,p)
=\epsilon(n,p)\epsilon(m,n+p).
\]

Weil B+B^T=G modulo zwei, ist der Kommutatorfaktor

\[
\epsilon(m,n)/\epsilon(n,m)=(-1)^{m^TGn}.
\]

Die Gitterverschiebung ist e_alpha|beta>=epsilon(alpha,beta)|alpha+beta>. Ihre Adjunktion lautet in dieser Konvention

\[
e_\alpha^\dagger=\epsilon(-\alpha,\alpha)^{-1}e_{-\alpha}.
\]

Dazu kommen a_n†=a_-n für die Oszillatoren. Diese Angabe betrifft ausdrücklich die Gitterverschiebungen; die radiale Feldadjunktion darf nicht ohne ihre Konventionsfaktoren mit einer vereinfachten Wurzelgeneratorregel verwechselt werden.

Die Vertexoperatoren werden durch

\[
V_\alpha(z)=
\exp\left(\sum_{n>0}\frac{\alpha\cdot a_{-n}}n z^n\right)
\exp\left(-\sum_{n>0}\frac{\alpha\cdot a_n}n z^{-n}\right)
e_\alpha z^{\alpha\cdot p}
\]

festgelegt. Ihre Operatorprodukte haben den führenden Faktor

\[
V_\alpha(z)V_\beta(w)
=\epsilon(\alpha,\beta)(z-w)^{\alpha\cdot\beta}
\left[V_{\alpha+\beta}(w)+\text{bestimmte Oszillatorterme}\right].
\]

Der Exponent, die Cocycle Phasen und die Oszillatorrelationen bestimmen nicht nur eine Zustandszählung, sondern die algebraischen Produkte. Der positive Gitterraum gehört zum etablierten Rahmen unitärer Gittervertexalgebren [E2, E3]. Seine Existenz ist keine neue TFPT Entdeckung; neu in diesem Paket ist die explizite, überprüfbare Ausführung der hier benötigten Markierungen.

### 4.3 Die vier Sektoren und die D5 Randbedingungen

Die Erweiterung ist

\[
\mathcal H_{E_8}=
\bigoplus_{k\in\mathbb Z_4}
\mathcal H_{D_5,k}\otimes\mathcal H_{A_3,k}.
\]

Die quadratischen Restklassenformen ergänzen sich zu k² modulo eins. Die nichttrivialen Sektoren besitzen Gesamtgewicht eins: 5/8+3/8, 1/2+1/2, 5/8+3/8. Man ergänzt diese Sektoren tatsächlich; eine bloße Projektion des alten Produktraums auf Invarianten ist nicht dieselbe Operation.

Die D5 Seite kann mit zehn reellen chiralen Fermionen beschrieben werden. Die Neveu–Schwarz Randbedingung ist antiperiodisch und liefert den geraden Vakuumsektor sowie den ungeraden Vektorsektor. Die Ramond Randbedingung ist periodisch und liefert die zwei Spinorparitäten. Die vier Sektoren müssen mit den passenden A3 Sektoren gemeinsam vorhanden sein. Zusätzliche Moden und Randbedingungen dürfen im nativen Aufbau nicht fehlen.

Die eigene Enumeration liefert

\[
\Theta_{E_8}=1+240q+2160q^2+6720q^3+\cdots,
\]

\[
\chi_{E_8}=q^{-1/3}(1+248q+4124q^2+34752q^3+\cdots).
\]

Geprüft sind außerdem alle 57.600 Wurzelpaare hinsichtlich des Cocycle Kommutatorfaktors und alle möglichen Wurzelsummen hinsichtlich ihrer Z4 Grade. Die Summen 1+1→2 ergeben 960 geordnete Paare, 1+3→0 ergibt 832 Wurzelsummen und 64 Gegenwurzelfälle mit Cartanziel.

### 4.4 Warum dies die native chirale Lücke nicht automatisch schließt

Die abstrakte Theorie wird mit cL=8 und cR=0 gewählt. Eine gewöhnliche kritische SU4 Kette besitzt dagegen linke und rechte Sektoren. Auch die Addition einer nichtchiralen D5 Theorie erzeugt nicht die Differenz cL-cR=8.

Bei einer strikt eindimensionalen lokalen Hamiltonrealisierung mit endlichem lokalen Hilbertraum ist die gravitative chirale Anomalie ein echtes Hindernis für das bloße Entfernen einer Laufrichtung. Die Voraussetzungen dieser Aussage dürfen nicht auf beliebige nichtlokale oder zusätzliche Raumarchitekturen verallgemeinert werden [E4].

Eine bekannte zusätzliche Architektur ist ein invertierbarer Bulk in 2+1 Dimensionen mit K=G_E8. Sein Rand kann die chirale E8 Theorie tragen [E5]. Damit wäre aber eine Bulkarchitektur vorausgesetzt. Sie ist weder aus C16 berechnet noch eine Ableitung von Raumzeit in 3+1 Dimensionen.

**Ergebnis:** Der algebraische Zielgegenstand ist erheblich vollständiger spezifiziert als nur c=8 und 248 Zustände. Die gemeinsame physische Herkunft, der native Skalierungsgrenzwert und die nötigen analytischen Energieabschätzungen des mikroskopischen Kandidaten sind weiterhin nicht gezeigt.

## 5. Tatsächliche Ausbreitung und eine genaue Dimensionsmehrdeutigkeit

### 5.1 Ein vollständig lösbarer Sektor desselben idealen Graphmodells

Für H_C=J sum P+ ist der vollständig polarisierte Zustand |0>^tensor16 ein stationärer Eigenzustand mit Energie 40J. Er ist bei positivem J **nicht** der antiferromagnetische Grundzustand.

Ersetze genau einen Ort durch eine der drei anderen Farben. Der Unterraum mit dieser einen Farbanregung bleibt unter H_C invariant. Wenn A die wirkliche Clebsch Adjazenzmatrix und L=5I-A ist, folgt direkt aus der Wirkung eines Swaps

\[
H_{\rm ein}=40J I-\frac J2L.
\]

Die Laplace Eigenwerte sind 0, 4 und 8 mit Multiplizitäten 1, 10 und 5. Die Projektoren lauten

\[
P_0=\frac{\mathbf1\mathbf1^T}{16},\quad
P_4=\frac{8L-L^2}{16},\quad
P_8=\frac{L^2-4L}{32}.
\]

Daher ist der tatsächliche Propagator relativ zur Polarisationsenergie

\[
U_{\rm ein}(t)=P_0+e^{2iJt/\hbar}P_4+e^{4iJt/\hbar}P_8.
\]

Ein lokaler Zweipunktoperator, der am Anfang die Farbänderung erzeugt und am Ende entfernt, hat genau diese Matrixelemente im polarisierten Referenzzustand. Es handelt sich also um einen Korrelationsprozess, nicht um eine nachträglich eingesetzte Weylmatrix.

Am Startort ist die Amplitude

\[
\mathcal A(t)=\frac{1+10e^{2iJt/\hbar}+5e^{4iJt/\hbar}}{16}.
\]

Die Wiederkehrperiode ist T=pi hbar/J. Bei T/2 ist die Rückkehrwahrscheinlichkeit exakt 1/16. Der Resolvent besitzt die drei entsprechenden kohärenten Pole bei relativen Energien 0, -2J und -4J. Alle drei einzelnen Farbdefekte teilen dieses Spektrum. Das ist kein Nachweis eines gemeinsamen Kegels sämtlicher später behaupteter Materiesektoren.

### 5.2 Die Raumdimension entsteht daraus nicht

Die Graphkugeln besitzen bei Radien 0, 1 und 2 die Größen 1, 6 und 16 und sind danach gesättigt. Der normierte Heat Trace ist

\[
h(s)=\frac{1+10e^{-4s}+5e^{-8s}}{16}.
\]

Die daraus definierte spektrale Dimension -2 d log h/d log s geht für große s gegen null. Das ist die endliche Sättigung, keine erzeugte dreidimensionale Welt. Eine andere Skalenauswertung einer einzigen kleinen Kurve beseitigt den fehlenden unendlichen Graphvertrag nicht.

### 5.3 Gleiches lokale Regelbuch, verschiedene große Dimensionen

Der Clebsch Graph hat Zyklusrang

\[
|E|-|V|+1=40-16+1=25.
\]

Man wählt einen Spannbaum. Seine 15 Kanten erhalten Verschiebung null. Von den übrigen 25 Kanten erhalten d ausgewählte Kanten die Einheitsverschiebungen eines Z^d; die übrigen null. Der resultierende periodische Überlagerungsgraph hat dieselben 16 lokalen Knotentypen und dieselbe lokale Inzidenz, aber eine große Ausdehnung in d Dimensionen. Weil die ausgewählten Schleifen die Basisverschiebungen erzeugen, ist der Überlagerungsgraph zusammenhängend.

Das Paket konstruiert ausdrücklich Beispiele mit d=1,2,3. Ihre niedrigste Bloch Laplace Bande hat jeweils eine positive quadratische Form. Analytisch folgt die nichtentartete Form auch daraus, dass keine nichttriviale Linearkombination der gewählten Schleifenverschiebungen ein reiner Potentialgradient sein kann. Die Matrixkoeffizienten wurden ergänzend numerisch berechnet.

Diese Beispiele sind Gegenmodelle gegen eine Dimensionsauswahl aus der bloßen lokalen Clebsch Inzidenz. Sie reproduzieren nicht sämtliche globalen Messungen des ursprünglichen endlichen C16 und werden auch nicht als dessen identische Fortsetzung behauptet. Gerade die zusätzliche globale Verklebungsregel ist das fehlende Datum.

Die skalare niedrigste Bande ist zudem quadratisch, nicht automatisch eine lineare Weyldispersion. Um eine Lorentzmetrik zu erhalten, muss ein geeignetes tatsächliches kohärentes Mehrkomponentenspektrum berechnet werden. Erst dann ist die bedingte Propagatorbrücke des Buchs anwendbar.

## 6. Vorhersagevertrag ohne nachträgliche Rettung

### 6.1 Historischer Alpha Vergleich

Die angegebene Quellgleichung wurde mit 80 Dezimalstellen Arbeitspräzision ausgewertet. Für

\[
c_3=1/(8\pi),\quad q=48c_3^4e^{-2\alpha},\quad
\phi_s=1/(6\pi)+q(1-q)^{-5/4}
\]

und

\[
\alpha^3-2c_3^3\alpha^2-\frac45\,41c_3^6\log(1/\phi_s)=0
\]

ergibt sich

\[
\alpha^{-1}=137.03599921684071250353786030380388037\ldots
\]

Die NIST Tabelle nennt für CODATA 2022 den Wert 137.035999177 mit Standardunsicherheit 0.000000021 [E6]. Der Abstand beträgt 1.8971768 dieser experimentellen Standardunsicherheiten.

Das ist ein historischer Konsistenzvergleich. Die Daten und diese Nähe waren bereits bekannt. Er ist keine neue unabhängige Vorhersage. Eine Fehlerangabe in vielen Dezimalstellen ersetzt auch keine hergeleitete Theorieunsicherheit oder den Transfer zur physikalischen Thomson Kopplung. NIST führt beim Abruf weiter die 2022 Werte; die nächste reguläre 2026 Anpassung ist dort angekündigt, nicht als bereits vorliegende neue Messung eingesetzt.

### 6.2 Belastende Zweige bleiben stehen

Die im Buch angegebenen Leptonverhältnisse dürfen ohne hergeleiteten Transfer nicht als Polmassenresultate beansprucht werden. Der dortige Myon/Tau Wert liegt ungefähr 2,2 Prozent über dem zum Vergleich genannten Polverhältnis. Der Elektron/Myon Ansatz weicht ebenfalls ab. Eine passende Skala darf nicht erst anhand der Abweichung gewählt werden.

Die alte Higgs Linie 129 bis 134 GeV passt nicht zum im Buch genannten beobachteten Bereich nahe 125 GeV. Der einfache Inflationszweig liegt bei N=51,4 mit As ungefähr 1,76 mal 10^-9 etwa 16 Prozent unter der dortigen Referenz 2,10 mal 10^-9. Für die angegebenen geeichten SO10 Protonzweige sind die Lebensdauern relativ zum verwendeten Bound ungefähr um die Faktoren 80, 3,4 und 2,4 zu kurz.

Dies sind erhaltene historische Spannungen der benannten Zweige, keine hier erneut ausgeführte globale Datenanalyse und kein Ausschluss jedes denkbaren TFPT Modells. Ebenso darf die Umrechnung einer dimensionslosen Formel mit einer externen Planckskala nicht als zusätzliche unabhängige Skalenherleitung gezählt werden.

### 6.3 Ein tatsächlich vor Beobachtungen formulierbarer Test

`experiment_contract.json` legt als primären endlichen Umsetzungstest die neue ausgeglichene Sternvariante fest: pro begonnenem Versuch p_behalten=1/6 und p_frisch=1/12. Beide Versuchsarme haben jeweils 10.000 begonnene Versuche. Sämtliche Präparationsfehlschläge bleiben im Nenner. Ein systematisches absolutes Wahrscheinlichkeitsbudget von höchstens 1/200 muss durch eine unabhängige Kalibrierung **vor** der Datenerhebung zertifiziert werden. Das Budget ist eine Voraussetzung des vorgeschlagenen Tests, kein hier gemessener Hardwarewert.

Unter stabilen unabhängigen Bernoulli Versuchen werden zwei exakte binomiale Intervalle mit jeweils 99,5 Prozent Überdeckung benutzt; die Bonferroni Garantie beträgt gemeinsam mindestens 99 Prozent. Liegt eines der Intervalle vollständig außerhalb der vorgegebenen Idealwahrscheinlichkeit samt zertifiziertem Fehlerbudget, wird das erklärte Modell einschließlich seiner Umsetzungsannahmen abgelehnt. Fehlt das Kalibrierungszertifikat, ist dieser Vertrag nicht auswertbar; das Fehlerbudget darf nicht nachträglich passend vergrößert werden.

`evaluate_experiment.py` erwartet echte Zählwerte und verweigert eine Auswertung ohne diese und ohne die festgelegten Kalibrierungsangaben. Es prüft die Deklarationen, nicht selbst die wissenschaftliche Gültigkeit des externen Zertifikats. Es wurden keine Versuchsdaten bereitgestellt oder erzeugt. Der Vertrag ist keine externe Studienregistrierung.

Dieser Versuch testet eine klar definierte Realisierung der endlichen Quantenquelle. Er identifiziert nicht allein einen fundamentalen Universalraum. Eine neue unabhängige Naturkonstante, die aus **derselben** vollständigen Quelle samt Transfer folgt, ist durch diese Untersuchung noch nicht gewonnen.

## 7. Was genau ausgeführt wurde

`verify.py` wurde normal und mit `python -O` ausgeführt. Die Ergebnisdateien waren bytegleich. Alle Prüfschritte verwenden explizite Fehlerbedingungen. Die Zahl vieler einzelner Wurzelbedingungen ist keine Zahl unabhängiger Entdeckungen.

Ausgeführt wurden die endliche Graphkonstruktion, die Gitterbasis und Wurzelgrade, die Cocycle Kontrollen, die niedrigen Gittercharakterkoeffizienten, der exakte isolierte Vermittlerpuls, die symbolische Zweibondreihe, die vollständige 129 dimensionale Zweibondmatrix, das 256 dimensionale Sternspektrum samt Projektorpolynom, alle acht Filterzweige, beide Pointervarianten samt Negativkontrolle, die 16 dimensionale tatsächliche Einanregungsausbreitung, drei explizite Überlagerungsgegenmodelle und die hochpräzise Alpha Nullstelle. Außerdem wurden die implementierten mikroskopischen Matrixspalten und eine Spalte der Elimination zweiter Ordnung gegengeprüft.

Nicht ausgeführt wurden die vollständige C16 Vielteilchendiagonalisierung, der vollständige effektive C16 Operator in vierter Ordnung, der native TFPT Phasenadapter, das ursprüngliche 20 Qubit Schaltungspaket, die ursprünglichen Schleifenrechnungen und Massentransfers, Hardwareexperimente oder ein analytischer Grenzübergang zu Raumzeit und Gravitation.

## 8. Abschlussbewertung der sechs Aufgaben

| Aufgabe | Erreicht | Nicht dadurch erreicht |
|---|---|---|
| Eine Quelle | Explizite versionierte endliche Referenzverträge und tatsächlicher mikroskopischer Matrixoperator | Eine eindeutige gemeinsame primitive Quelle aller behaupteten physikalischen Ansichten |
| Kopplung | Besetzung erklärt den Paarterm; exakter Puls; verbundener Vierkörperterm und konditionale Fehlerabschätzung | Globale Paarreinheit, voller C16 Operator in vierter Ordnung oder abgeleitete Parameter |
| Präparation | Exakter Sternfilter, vollständige Registerwahrscheinlichkeiten und alle Misserfolge | Ursprung der konditionierten Steuerung, reine Clifford Präparation oder Hardwarebereitschaft |
| Chirale Naht | Explizite abstrakte E8 Erweiterung mit Phasen, Adjunktion, Sektoren und Operatorprodukten | Physische chirale Realisierung aus dem gewählten endlichen Ursprung |
| Geometrie | Tatsächlicher berechneter Propagator und explizite Dimensionsgegenmodelle | Raumzeit in 3+1 Dimensionen, gemeinsamer Materiekegel oder gravitativer Sektor |
| Physikalische Ausgabe | Prospektiver endlicher Testvertrag; Alpha Vergleich und negative Zweige bleiben transparent | Neue unabhängige fundamentale Vorhersage aus einer geschlossenen gemeinsamen Theorie |

Der stärkste unmittelbare Gewinn ist nicht eine weitere Identifikation gleicher Zahlen. Er ist, dass zusätzliche Annahmen jetzt konkrete, berechenbare Folgen haben: Vermittlerbesetzung verändert Mehrkörperenergien; kontrollierte Spektren verändern Präparationsausbeuten; globale Verklebungen verändern Dimension und Ausbreitung. Eine gemeinsame Quelle muss diese Unterschiede auswählen, statt sie zwischen verschiedenen Kapiteln zu übergehen.

## Externe Primärquellen

Die Quellen liefern den mathematischen Hintergrund und Referenzdaten, nicht eine externe Bestätigung der eigenen TFPT Fortsetzungen.

[E1] Bravyi, DiVincenzo, Loss, *Schrieffer-Wolff transformation for quantum many-body systems*, Annals of Physics 326 (2011). https://arxiv.org/abs/1105.0675

[E2] Dong, Lin, *Unitary vertex operator algebras* (2013). https://arxiv.org/abs/1308.2361

[E3] Kac, Moseneder Frajria, Papi, Xu, *Conformal embeddings and simple current extensions*, IMRN (2015). https://arxiv.org/abs/1210.6602

[E4] Kapustin, Spodyneiko, *Absence of Energy Currents in an Equilibrium State and Chiral Anomalies*, Physical Review Letters 123, 060601 (2019). https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.123.060601

[E5] Plamadeala, Mulligan, Nayak, *Short-Range Entangled Bosonic States with Chiral Edge Modes and T-duality of Heterotic Strings*, Physical Review B 88, 045131 (2013). https://arxiv.org/abs/1304.0772

[E6] NIST, vollständige Tabelle der CODATA Anpassung 2022; abgerufen am 14. September 2026. https://physics.nist.gov/cuu/Constants/Table/allascii.txt
