# Globale Quellenauswahl vor der Kompression

10. September 2026. Unabhängige mathematische Fortsetzung auf dem Originalstand `66b91e40e245569f06ab440ead80f446c9be0ee5`; keine Änderung des TFPT-Repositoriums.

**Neues Ergebnis:** Die zusätzliche Freiheit des hohen Blocks in einem einzelnen ambient komprimierten Ring lässt sich durch eine global positive, kompatibel komprimierte Kopplungsform beseitigen. Die dafür benötigte Injektivität gilt auf geraden kubischen Tori bereits für den vollständigen U(1)-Rotorraum. Eine feste Hintergrundwahl oder ein gleichmäßig beschränkter inverser Adjazenzoperator sind nicht erforderlich. Ein expliziter endlicher Rotorvektor zeigt zugleich, warum die bisher zulässigen lokalen Gegenvarianten D=4I±A diese globale Fortsetzung nicht bestehen.

Dies ist ein Satz innerhalb des bezeichneten Quellenvertrags. Er leitet relative Positivität, das lokale Hochbudget oder die Zahlen des Parents nicht aus P1/P2 her. Er behauptet weder eine freie Diagonalisierung dynamischer Links noch eine vollständige physische Theorie.

## 1. Die tatsächlichen Originaldaten

Die aktuelle Quelle `experiments/theory-contracts/ground-state-loop-response/README.md:14–36` gibt auf kubischen Tori L≥5 den ungeschnittenen Rotor/CAR-Prozess ausdrücklich an: Die Einträge der selbstadjungierten Adjazenz \(A_U\) sind Funktionen der unabhängigen kompakten U(1)-Linkkoordinaten; die elektrischen Operatoren bleiben dynamisch. Mit
\[
A=aA_U,\qquad a=1/12,\qquad\|A\|\le1/2
\]
lautet der volle Materiekoeffizient
\[
h=\begin{pmatrix}A+A^2/4&A/2\\A/2&4I\end{pmatrix}.
\]
Alle Rückwege in A² gehören dazu; sie erzeugen auf dem kubischen Gitter die ursprüngliche niedrige Onsite-Zahl 1/96. Die Quellstelle betont, dass ihr Tr nur die endliche Ortsmatrixspur bezeichnet.

Der ursprüngliche Wandbeweis `tex-artefacts/toe_round4_proofs.tex:243–291` und `verification/v1027_signed_det_car_wall.py:2–13,50–55` geben die Gramstruktur und die onsite DET-CAR-Konstruktion an. Das ursprüngliche Fock-Bandargument wird ausdrücklich auf feste klassische Hintergründe begrenzt; operatorwertige Linkdiagonalisierung wird nicht als CAR-erhaltend vorausgesetzt. Diese Einschränkung bleibt bestehen.

Die Quellenherkunft ist getrennt: `origin_theory.tex:87–99` nennt P1/P2 und die bedingte physische Trägeridentifikation; `tfpt_4_frontier.tex:978–1000` lässt den gemeinsamen vollständigen Parent und die T1–T8-Abschlüsse offen. Die Untersuchung ergänzt diesen Quellenvertrag, ohne seine Einstufung zu ändern.

## 2. Der allgemeine positive Auswahlsatz

Seien A und D beschränkte selbstadjungierte Operatoren auf demselben Hilbertraum und \(\ker A=0\). Betrachte
\[
B(A,D)=\begin{pmatrix}A^2/4&A/2\\A/2&D-3I\end{pmatrix}.
\]
Dann gilt exakt
\[
\boxed{B(A,D)\ge0\quad\Longleftrightarrow\quad D\ge4I.} \tag{1}
\]

**Beweis ohne beschränkten inversen Operator.** Für beliebige x,y gilt
\[
\langle(x,y),B(A,D)(x,y)\rangle
=\|Ax/2+y\|^2+\langle y,(D-4I)y\rangle. \tag{2}
\]
Weil A selbstadjungiert und injektiv ist, ist ran A dicht. Für jedes feste y gibt es daher x_n mit Ax_n→−2y. Positivität von (2) und der Grenzübergang liefern D−4I≥0. Die Umkehrung folgt direkt aus (2). Die Normen der x_n müssen nicht gleichmäßig beschränkt sein: Es handelt sich um eine exakte Positivitätsprüfung, nicht um eine Aussage über günstige Präparation oder Konditionierung.

Das erweitert den endlichen invertierbaren Sättigungssatz aus der Pro-Analyse auf einen entscheidenden Fall ohne Spektrallücke bei null. Beispielsweise ist die freie kubische Adjazenz auf ℓ²(Z³) injektiv: Ihr Fouriersymbol \(2a(\cos k_1+\cos k_2+\cos k_3)\) verschwindet nur auf einer Lebesgue-Nullmenge. Trotzdem liegt null im kontinuierlichen Spektrum.

**Exakte Budgetauswahl.** Ist der Hilbertraum vollständig in Ortsblöcke zerlegt und gilt
\[
D_{xx}=4I\quad\text{für jeden Ort }x,
\]
so erzwingt (1) bereits D=4I. Denn K=D−4I≥0 besitzt ausschließlich verschwindende Diagonalblöcke. Aus \(\|K^{1/2}\iota_x v\|^2=0\) folgt K\(\iota_xv\)=0 für alle Ortsvektoren; diese spannen den ganzen Raum dicht auf.

Alternativ genügt \(\tau(D)=4\tau(I)\), wenn D in einer Algebra mit einer **treuen endlichen positiven Spur** τ liegt. Dann ist τ(K)=0 nur für K=0 möglich. Eine bloße asymptotische Energiedichte auf einer allgemeinen unendlichen Operatoralgebra genügt dafür nicht: Der lokale positive Defekt \(K=|\delta_0\rangle\langle\delta_0|\) hat verschwindende Spur pro Volumen, ist aber nicht null.

## 3. Warum der vollständige Rotorraum die Injektivität liefert

Sei G ein endlicher bipartiter Graph mit einem perfekten Matching, mit nichtverschwindenden festen Kantengewichten und einer tatsächlich unabhängigen U(1)-Phase je ungerichteter Kante. Die beiden Farbklassen besitzen dieselbe Größe. Nach einer Ortsordnung hat die Adjazenz die Form
\[
A(U)=\begin{pmatrix}0&C(U)\\C(U)^\dagger&0\end{pmatrix}.
\]
In det C(U) liefert jedes perfekte Matching sein eigenes Laurentmonom in den unabhängigen Kantenphasen. Verschiedene Matchings besitzen verschiedene Monome; wegen der nichtverschwindenden Gewichte kann mindestens ein Term nicht ausfallen. Somit ist det C ein nichttriviales trigonometrisches Polynom. Seine Nullmenge hat Haarmaß null. Dies folgt etwa induktiv mit Fubini aus der endlichen Anzahl von Nullstellen eines nichttrivialen Polynoms in einer Variablen, außerhalb der Nullmengen seiner Koeffizienten.

Also ist A(U) für fast alle U invertierbar. Der globale Multiplikationsoperator
\[
A:\mathbb C^{|G|}\otimes L^2(\mathbb T^{E(G)})
\longrightarrow\mathbb C^{|G|}\otimes L^2(\mathbb T^{E(G)})
\]
ist deshalb injektiv, selbst wenn einzelne Hintergründe Nullmoden haben und sein inverser Operator unbeschränkt ist.

Gerade kubische Tori mit L≥6 erfüllen diese Voraussetzungen: Schachbrettfärbung und paarweise Zuordnung benachbarter x-Orte liefern das Matching. Diese Volumenfolge liegt vollständig in der nativen L≥5-Quellenklasse. Ungerade Tori sind nicht durch diesen speziellen bipartiten Beweis abgedeckt; sie werden für den Satz nicht benötigt.

Damit liefert (1) zwei sauber getrennte Varianten:

1. **HH-Koeffizienten als Multiplikationsoperatoren.** Ist D eine beschränkte matrixwertige Funktion der Rotorwinkel, genügt neben B≥0 das gemittelte Budget
   \[
   (\operatorname{Tr}_{\rm Ort}\otimes\operatorname{Haar})(D)=4|G|.
   \]
   Diese Spur ist auf der matrixwertigen Multiplikationsalgebra treu. Es folgt D(U)=4I fast überall; für normstetige Hintergrundfamilien gilt die Gleichheit anschließend an jedem Hintergrund, auch an den singulären.

2. **Allgemeinere beschränkte HH-Operatoren.** D darf auch außerhalb dieser Multiplikationsalgebra liegen, sofern die stärkeren operatorwertigen lokalen Budgets D_xx=4I auf dem ganzen Rotorraum gelten. Der vorige Ortsblockbeweis benötigt keine Haarspur. Ein nur skalares Haarbudget reicht hier nicht.

Der ursprüngliche elektrische Term \(H_E=(\kappa/2)\sum_e E_e^2\) ist unbeschränkt und gehört in beiden Aussagen **zum subtrahierten gemeinsamen freien Parent**. Er wird weder in D aufgenommen noch mit einer endlichen Haarspur versehen. Der relative Materiekoeffizient B ist beschränkt. Die Aussagen sind daher keine freie Fock-Diagonalisierung des gesamten Rotor/CAR-Hamiltonoperators.

Auch die benötigte Positivität ist präzise: Verlangt wird die relative Koeffizienten-/Grampositivität der vollständigen Quelle vor der Gausssektor-Einschränkung. Positivität allein eines ausgewählten physikalischen Zustands, eines komprimierten Sektors oder des gesamten verschobenen Hamiltonoperators ersetzt diese Voraussetzung nicht.

## 4. Kompatible Kompression erhält die richtigen Randströme

Für eine räumliche Projektion P und Q=I−P setze
\[
A_P=PAP,\qquad C_P=QAP.
\]
Die tatsächliche Kompression von (1) lautet
\[
B_P=
\begin{pmatrix}
(A_P^2+C_P^\dagger C_P)/4&A_P/2\\
A_P/2&P(D-3I)P
\end{pmatrix}. \tag{3}
\]
Nach der globalen Auswahl D=4I hat sie die exakte Darstellung
\[
B_P=\widetilde W_P^\dagger\widetilde W_P,
\qquad
\widetilde W_P=
\begin{pmatrix}A_P/2&I_P\\C_P/2&0\end{pmatrix}. \tag{4}
\]
Der Randstrom ist erhalten. Er wird weder entfernt noch durch einen anderen freien Parent versteckt. Für verschachtelte Fenster S⊂T zerlegt sich seine Norm genau in den Zwischenraum T\S und den äußeren Raum T^c. Daher ergeben direkte und iterierte Kompression dieselbe Form.

Umgekehrt impliziert Positivität aller endlichen **Kompressionen eines gemeinsamen beschränkten B** dessen globale Positivität, weil endlich getragene Vektoren dicht liegen. Zusammen mit (1) und dem Budget folgt wiederum D=4I. Dieses gemeinsame B beziehungsweise ein äquivalenter konsistenter beschränkter Quellenvertrag ist wesentlich; unabhängig für jedes Fenster gewählte Matrizen liefern diese Folgerung nicht.

Der vorherige lokale Gegenfall bleibt somit richtig, wird aber eingeordnet: Ein einzelner kleiner Ring sieht wegen seines zusätzlichen niedrigen Randbudgets nicht alle kohärenten Testvektoren des vollständigen Prozesses. Ein globales Auswahlprinzip muss diese Vektoren einschließen.

## 5. Ein exakter endlicher Zeuge gegen die falsche globale Fortsetzung

Betrachte die beiden Varianten D=4I+ξA mit ξ=±1 auf dem kubischen Gitter beziehungsweise auf einem geraden Torus L≥6. Im einzelnen ambienten π-Fluss-Viererring waren beide relativ positiv und besaßen das gleiche hohe Spurbudget. Global setze jetzt
\[
x=\delta_0-\xi\delta_e,\qquad y=-Ax/2,
\]
wobei e der benachbarte Ort in x-Richtung ist. Der kanonische Gramstrom verschwindet exakt. Auf dem freien Hintergrund gibt es genau 15 Dreischrittwege von 0 nach e; daher gilt
\[
\langle(x,y),B(A,4I+\xi A)(x,y)\rangle
=-\frac{15}{2}a^3=-\frac5{1152}.
\]
Der Vektor benötigt nur die 12 Orte der beiden Nachbarsterne. Seine Norm ist
\[
\|(x,y)\|^2=2+3a^2=\frac{97}{48},
\]
und der normalisierte relative Erwartungswert beträgt exakt −5/2328. Der eigene Prüfer rekonstruiert die volle ambient komprimierte 24×24-Blockmatrix einschließlich sämtlicher äußerer Gramkanäle; sie liefert genau denselben Wert.

### Derselbe Ausschluss als echter ungeschnittener Rotorvektor

Eine eingefrorene Phase ist hierfür nicht nötig. Auf dem vollen Rotorraum verwende
\[
\phi(U)=\frac{1+U_e}{\sqrt2},\qquad
\Psi(U)=\left(x\phi(U),-A(U)x\phi(U)/2\right).
\]
Dies ist ein exakt normierbarer Vektor mit endlichem Fourierträger im vollständigen ungeschnittenen Rotorraum; er liegt auch im Bereich jeder elektrischen Energiepotenz. Es wird kein Operator auf einen elektrischen Cutoff komprimiert.

Von den 15 Dreischrittwegen reduzieren sich genau 11 auf den direkten Kantenmonom. Vier behalten drei unabhängige Kantenphasen und mitteln gegen |φ|² zu null. Der direkte Monom hat unter |φ|² den Erwartungswert 1/2. Damit folgt exakt
\[
\langle\Psi,B(A,4I+\xi A)\Psi\rangle
=-\frac{11a^3}{4}=-\frac{11}{6912},
\]
\[
\|\Psi\|^2=\frac{97}{48},\qquad
\frac{\langle\Psi,B\Psi\rangle}{\|\Psi\|^2}
=-\frac{11}{13968}. \tag{5}
\]
Der Prüfer behält alle unabhängigen Rotor-Laurentmonome der Wege und bestätigt die Zahlen rational.

Dieser Vektor prüft die vollständige relative Koeffizientenform. Er wird nicht als neutraler Gausszustand oder als negative Richtung des gesamten Hamiltonoperators bezeichnet. Widerlegt wird die globale relative Positivität der beiden vorgeschlagenen HH-Mutationen, nicht die ursprüngliche Quelle mit D=4I.

## 6. Was außerdem festgelegt wird — und was nicht

Sei B=W†W eine beliebige Gramrealisierung des ausgewählten globalen Blocks, mit W=(C,R). Dann sind
\[
C^\dagger C=A^2/4,\quad C^\dagger R=A/2,\quad R^\dagger R=I.
\]
Direkte Expansion ergibt
\[
(C-RA/2)^\dagger(C-RA/2)=0.
\]
Also gilt C=RA/2 und
\[
\boxed{W=R(A/2,I),\qquad R^\dagger R=I.} \tag{6}
\]
Damit ist der vollständige minimale Gramstrom bis auf eine gemeinsame linke Isometrie festgelegt. Zusätzliche orthogonale Hochkanäle mit eigener positiver Energie passen nicht mehr in das gesättigte Budget. Eine markierte Mess- oder Instrumentstruktur kann die verbleibende Isometrie allerdings unterscheiden; sie wird durch die Hamilton-Gramform allein nicht ausgewählt. Ebenso bleiben Anfangszustand und Quellenpräparation eigene Daten.

Eine nützliche robuste Variante gilt bei exakt festgehaltenen niedrigen und gemischten Blöcken: Hat K=D−4I eine feste räumliche Reichweite R und gelten statt des exakten Budgets 0≤K_xx≤εI, so folgt aus positiver Block-Cauchy–Schwarz ||K_xy||≤ε. Bei höchstens N_R möglichen Orten pro Zeile liefert der Schurtest
\[
\|D-4I\|\le N_R\epsilon.
\]
Für HH-Nächste-Nachbartransport im kubischen Gitter ist N_R=7. Dies ist eine volumenunabhängige Stabilität im erklärten Reichweitenvertrag; ein bloß gemittelter kleiner Haar-Spurexzess oder zusätzliche Fehler in den niedrigen Blöcken genügen für diese Normschranke nicht.

## 7. Was aus P1/P2 weiter fehlt

Der bewiesene Abschluss setzt folgende gemeinsam identifizierte Daten voraus:

1. den vollen ursprünglichen niedrigen und gemischten Quellkernel einschließlich aller Wege vor der räumlichen Kompression;
2. relative positive Kopplungsenergie gegenüber genau dem bezeichneten freien Parent, einschließlich korrekter Trennung des elektrischen Terms;
3. ein exaktes lokales Hochbudget beziehungsweise eine tatsächlich treue Spur auf der zugelassenen Koeffizientenalgebra;
4. einen gemeinsamen globalen beziehungsweise kompatiblen Quellenprozess.

Die ursprüngliche Gram-Wand erfüllt diese Bedingungen, weil sie mit dem unitären Hochreferenzstrom konstruiert wurde. Der Satz zeigt jetzt die umgekehrte Auswahl: Diese Bedingungen erzwingen den Hochblock und die minimale Stromform. Er zeigt nicht, dass P1/P2 genau diese Bedingungen oder die vorgegebenen Kopplungszahlen erzwingen. Das ist die verbleibende fundamentale Herkunftsfrage.

Es gibt damit einen konkreten positiven Fortschritt gegenüber der Konsolidierung: **Die Randkorrektur ist kein grundsätzliches Hindernis für Sättigung. Entscheidend ist, Sättigung am gemeinsamen vollständigen Quellenprozess zu verlangen und erst anschließend mit allen Randkanälen zu komprimieren.** Das lokale Gegenbeispiel kann diese globale Bedingung nicht erfüllen; der endliche Rotorzeuge (5) macht den Unterschied prüfbar.

## 8. Kontrolle und unabhängige Gegenprüfung

`check_global_completion.py` besteht 39 exakte Kontrollen: Rotor-Determinante und Matchingmonome, lokale positive Ringvarianten, vollständiger 12-Orte-Rand-Gram, negative globale und echte Rotor-Erwartungswerte, konsistente verschachtelte Kompression und minimale Gramfaktorisierung. Keine TFPT-Datei wird importiert; kein fremder Prüfer und keine native Kampagne werden ausgeführt. Diese endlichen Kontrollen ersetzen weder das Dichteargument noch den allgemeinen Matchingbeweis.

Der allgemeine Operatorsatz und das Rotor-Matchingargument wurden unabhängig von `spinor_audit` gegengeprüft; bestätigt wurden ausdrücklich die Dichte von ran A, das lokale Blockbudget, die Unabhängigkeit der Phasen und das Fehlen einer erforderlichen uniformen inversen Schranke.
