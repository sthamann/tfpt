---
title: "TFPT und Universalraum"
subtitle: "Rekonstruktion, exakte Fortsetzungen und der verbleibende TOE Vertrag"
author: "Für Stefan Hamann · Analyse und Gegenrechnung: ChatGPT"
date: "14. September 2026"
lang: de-DE
---

# Ergebnis und Reichweite

Diese Fortsetzung untersucht die 90 Seiten der bereitgestellten Gesamtdarstellung [Q]. Sie ersetzt das Original nicht. Die stärkste zusätzliche Herleitung betrifft dessen präzise definierte Zweizellenaufgabe: Der bekannte niedrige Eigenzweig ist für **jede** endliche Brückenkopplung $\lambda\geq0$ der eindeutige globale Grundzustand. Die erste Anregungsenergie und damit die tatsächliche Lücke lassen sich ebenfalls exakt bestimmen. Die bisherige Zertifizierungsgrenze $\lambda<8J$ entfällt.

Dazu kommen ein explizites Belegungsmodell für die Vermittlung, eine darin sichtbar werdende Unverträglichkeit mit ungebrochener kontinuierlicher Spin(10) Symmetrie, ein idealer Spektralfilter auf Basis desselben Tetramergenerators, eine konkrete Gitterphase und eine Gegenfamilie gegen die eindeutige Auswahl dreier Raumdimensionen aus der internen TFPT Struktur.

**Status:** mathematische Eigenherleitungen und bedingte Modellkonstruktionen, nicht begutachtet. Kein vollständiger TOE Nachweis. Insbesondere werden kein nativer vierdimensionaler Raumzeitgrenzwert, kein vollständiges chirales Standardmodellmaß und kein quantisierter gravitativer Sektor behauptet. Diese Grenze folgt hier nicht aus dem historischen Status der Probleme, sondern aus den ausdrücklich fehlenden Quelldaten und den konstruierten Alternativmodellen.

Eine fundamentale Theorie darf Axiome besitzen. Sie muss nicht jede Ausgangsannahme aus dem Nichts beweisen. Eine neu gesetzte Dynamik darf aber nicht als Konsequenz eines älteren, schwächeren Axiomensystems ausgegeben werden. Zu unterscheiden sind deshalb:

* **Existenz:** Ein konsistentes mathematisches Modell lässt sich angeben.
* **Auswahl:** Die festgelegten primitiven Regeln bestimmen gerade dieses Modell oder seine beobachtbare Äquivalenzklasse.
* **Physik:** Dasselbe Modell besitzt die benötigten Grenzwerte und besteht unabhängige empirische Prüfungen.

Der beigefügte unabhängige Prüfer bestätigt 56 benannte Bedingungen: 43 mit ganzzahliger, rationaler oder symbolischer Rechnung, 13 mit Gleitkommarechnung. Die numerischen Spektraltests durchlaufen sämtliche erlaubten Youngsektoren der acht Viererträger an elf Kopplungswerten. Die allkopplige Aussage für alle $\lambda$ beruht auf dem folgenden Beweis, nicht auf der endlichen Stichprobe. Die Zählung ist keine Anzahl unabhängiger Entdeckungen oder physikalischer Bestätigungen.

# Was aus dem Original erhalten bleibt

## Die interne algebraische Rekonstruktion

Die markierten Gitter $D_5$ und $A_3\simeq D_3$ haben Determinante vier und eine Diskriminantengruppe $\mathbb Z_4$. Mit der Konvention $q(x)=\lVert x\rVert^2/2\pmod1$ besitzen die passenden Klassen die Formen

$$q_{D_5}(k)=5k^2/8,\qquad q_{A_3}(k)=3k^2/8.$$

Die diagonalen Klassen sind isotrop, weil ihre Summe $k^2$ ganzzahlig ist. Die Erweiterung vom Index vier hat Determinante eins. Positivität, Geradheit und Rang acht identifizieren das resultierende Gitter als $E_8$. Dies rekonstruiert eine reale mathematische Struktur, nicht lediglich die Zahl acht. [Q, Kapitel 3.3]

Die komplexe Generatoralgebra zerfällt typgerecht als

$$\mathfrak e_8=(45,1)\oplus(1,15)\oplus(10,6)
\oplus(16,4)\oplus(\overline{16},\overline4).$$

Der Grad ist additiv modulo vier. Deshalb liefert der Kanal $1+1$ den Grad zwei, der Kanal $1+3$ hingegen den Grad null. Eine Adjungierte ist weiterhin nicht der volle Mehrteilchenraum. Insbesondere folgt aus einer fehlenden Darstellung in der 248 kein generelles Verbot entsprechender Tensorproduktzustände. [Q, Kapitel 3.4 und 7.6]

## Der passive Prozess und seine Kompression

Der feste Prozess auf 60 Strahlen besitzt

$$T=\frac1{28}(C^TBC+F^TF),\qquad \operatorname{rank}T=30.$$

Der Kontextschatten entwickelt sich mit $K=B/7$, der Paulischatten mit dem Faktor $3/7$. Allgemeine Kontextblöcke, passive separate Marginalien und kohärente Register verlangen verschiedene Beschreibungsgrößen. Keine dieser Zahlen darf ohne Angabe des Zugriffs als universelle Minimaldimension verwendet werden. [Q, Kapitel 4 und 5]

Eine nützliche ergänzende Rechnung präzisiert die Auswahl von $1/7$. In der inzidenzerhaltenden Familie

$$K_a=aI+\frac{1-a}{6}(B-I),\quad 0\leq a\leq1$$

ist der entsprechende Strahlenprozess

$$T_a=\frac{7(1-a)}6T+\frac{7a-1}6I_{60}.$$

Dies folgt direkt aus der einzigen Selbstübergangswahrscheinlichkeit und den zwölf übrigen möglichen Strahlübergängen jeder Spalte. Die Eigenwerte sind

$$1^{[1]},\quad ((1+5a)/6)^{[9]},\quad ((3a-1)/2)^{[5]},$$
$$((1+2a)/3)^{[15]},\quad ((7a-1)/6)^{[30]}.$$

Damit ist $a=1/7$ innerhalb dieser Familie die eindeutige Wahl mit minimalem Rang 30. Bei $a=1/3$ sinkt der Rang lediglich auf 55; sonst ist er 60. Ein **zusätzliches** Prinzip maximaler einmaliger Kompression würde also die gewünschte Regel auswählen. Dass gerade dieses Prinzip fundamental gilt, wird dadurch nicht bewiesen. Der alternative Wert $a=1/2$ bleibt unter bloßer Symmetrie und Inzidenz zulässig. Diese Unterscheidung schließt die Auswahlfrage relativ zu einer zusätzlichen Bedingung, nicht aus Symmetrie allein.

## Die Vierträgerzelle

Mit $P^+_{ij}=(I+S_{ij})/2$ lautet der vollständige Tetramer

$$H_{\mathrm{tet}}=J\sum_{1\leq i<j\leq4}P^+_{ij},\qquad J>0.$$

Sein eindeutiger Grundzustand ist

$$|\Omega\rangle=\frac1{\sqrt{24}}\sum_{\pi\in S_4}\operatorname{sgn}(\pi)
|\pi(0)\pi(1)\pi(2)\pi(3)\rangle.$$

Das Spektrum ist $J\{0^{[1]},2^{[45]},3^{[40]},4^{[135]},6^{[35]}\}$. Die einzelnen Reduktionen sind $I_4/4$, die Paarreduktionen $(I-S)/12$. Ein zusammenhängender Vierergraph kann denselben Kern besitzen, ohne dasselbe Anregungsspektrum zu haben. Die Ergebnisse des vollständigen Tetramers werden deshalb nicht auf Pfad, Kette oder Clebsch Graph übertragen. [Q, Kapitel 6]

# Vollständige Lösung der niedrigen Zweizellenspektren

## Satz und Voraussetzungen

Es seien $A$ und $B$ zwei disjunkte vollständige Tetramer mit demselben $J>0$. Genau eine Brücke verbindet einen Träger $a\in A$ mit einem Träger $b\in B$:

$$H=H_A+H_B+\lambda V,\qquad V=P^+_{ab},\qquad \lambda\geq0.$$

Definiere

$$R=\sqrt{16J^2-2J\lambda+\lambda^2},\qquad Q=\sqrt{4J^2+\lambda^2}.$$

Dann gilt für alle endlichen $\lambda\geq0$:

$$\boxed{E_0=\frac{4J+\lambda-R}{2}}$$

ist der eindeutige globale Grundwert und

$$\boxed{E_1=3J+\frac\lambda2-\frac Q2}$$

ist der erste angeregte Energiewert. Insbesondere

$$\boxed{\Delta=E_1-E_0=J+\frac{R-Q}{2}>\frac J2.}$$

Bei $\lambda=0$ ist $\Delta=2J$. Im Grenzfall $\lambda\to\infty$ gelten $E_0\to5J/2$, $E_1\to3J$ und $\Delta\to J/2$. Es tritt keine Grundzustandskreuzung bei $\lambda=8J$ auf.

Die Grundwertformel war bereits in [Q, Kapitel 8] enthalten. Neu gegenüber dieser Darstellung sind der globale Nachweis für alle positiven Kopplungen, die explizite erste Anregung und die exakte Lücke. Es wird keine Prioritätsbehauptung gegenüber der gesamten Literatur erhoben.

## Die irreduziblen Einzelzellensektoren

Die Zerlegung der vier Träger ergibt:

| Youngform | SU(4) Dimension | Multiplizität | Energie in $J$ |
|:--|--:|--:|--:|
| $(1,1,1,1)$ | 1 | 1 | 0 |
| $(2,1,1)$ | 15 | 3 | 2 |
| $(2,2)$ | 20 | 2 | 3 |
| $(3,1)$ | 45 | 3 | 4 |
| $(4)$ | 35 | 1 | 6 |

Die Energie folgt aus der zentralen Transpositionssumme:

$$E_\mu/J=3+\frac14\sum_r\mu_r(\mu_r-2r+1).$$

Mit $H_0=H_A+H_B$ gibt es unterhalb $4J$ nur das Produktsingulett bei null, sechs Kopien der Adjungierten bei $2J$ und vier Kopien der zwanzigdimensionalen Darstellung bei $3J$.

## Der Singulettsektor

Setze $|0\rangle=|\Omega\rangle_A|\Omega\rangle_B$ und

$$|1\rangle=\frac{4S_{ab}-I}{\sqrt{15}}|0\rangle.$$

Die beiden Zustände sind orthonormal und spannen einen sowohl unter $H_0$ als auch unter $V$ invarianten Raum. Darauf wirkt

$$H_{\mathrm s}=\begin{pmatrix}
5\lambda/8&\sqrt{15}\lambda/8\\
\sqrt{15}\lambda/8&4J+3\lambda/8
\end{pmatrix}.$$

Der untere Wert ist $E_0$. Der obere Wert ist mindestens $4J$. Im orthogonalen Singulettkomplement liegt schon $H_0$ mindestens bei $4J$; die positive Brücke kann diesen Wert nicht senken. Damit konkurriert kein weiterer Singulett mit $E_0$.

## Scharfe Schranke im gesamten adjungierten Sektor

Sei $P$ die Projektion auf den $2J$ Eigenraum von $H_0$ innerhalb des global adjungierten Sektors. Da dieser Sektor keine $3J$ Zustände enthält,

$$H_0\geq4JI-2JP.$$

Entscheidend ist die Kompression der Brücke:

$$PVP\geq\frac12P.$$

Hier ist die vollständige kleine Rechnung. Wähle einen spurfreien hermiteschen Generator $A$ mit $\operatorname{Tr}(A^2)=4$. Die Zustände $A_i|\Omega\rangle$ einer Zelle haben Gramwerte eins auf der Diagonale und $-1/3$ außerhalb. Ihre Summe ist null; sie bilden die drei Multiplizitätsrichtungen der lokalen Adjungierten. Die beiden Zellen liefern sechs solcher Richtungen. Mit

$$S_{ab}=\frac14\sum_{u=0}^{15}P_u^{(a)}P_u^{(b)}$$

hat $PVP$ die Diagonalblöcke $5I/8$. Sein zellübergreifender Block ist ein Rang eins Operator vom Betrag $1/8$ auf den durch die Brückenträger markierten Richtungen. Deshalb lautet sein Spektrum pro adjungierter Komponente

$$\{1/2,5/8,5/8,5/8,5/8,3/4\}.$$

Die SU(4) Invarianz überträgt diese Multiplizitätsmatrix auf alle 15 adjungierten Komponenten. Der beigefügte Prüfer kontrolliert das charakteristische Polynom der Kompression rational aus den vollständigen ganzzahligen Tensoren.

Für zwei Projektionen $P$ und $V$ besitzt ein nichttrivialer kanonischer Zweierblock zu $p\in\operatorname{spec}(PVP)$ die Form

$$P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
V=\begin{pmatrix}p&\sqrt{p(1-p)}\\\sqrt{p(1-p)}&1-p\end{pmatrix}.$$

Der untere Wert von $4JI-2JP+\lambda V$ ist dann

$$3J+\frac\lambda2-\frac12\sqrt{4J^2+4J\lambda(1-2p)+\lambda^2}.$$

Aus $p\geq1/2$ folgt die Untergrenze $E_1$. Die eindimensionalen Schnittblöcke erfüllen dieselbe Schranke. Somit liegt der gesamte adjungierte Sektor nicht unter $E_1$.

## Die Schranke wird erreicht

Für einen normierten Generator wie oben definiere

$$|L_A\rangle=\frac{A_a-A_b}{\sqrt2}|0\rangle,
\qquad |H_A\rangle=S_{ab}|L_A\rangle.$$

Diese Zustände sind orthonormal. Es gilt

$$H_0|L_A\rangle=2J|L_A\rangle,\qquad
H_0|H_A\rangle=4J|H_A\rangle.$$

Eine Erklärung der zweiten Gleichung ohne Diagonalisierung: Die auf den beiden Brückenträgern erzeugten lokalen Zustände liegen jeweils in $1\oplus15$, also bei Energie null oder $2J$. Der vertauschte Vektor besitzt keinen $2J$ Anteil, weil $(2PVP-P)|L_A\rangle=0$. Er ist global adjungiert und besitzt deshalb auch keinen Nullenergieanteil. Damit bleibt nur $4J$.

In diesem Raum ist der Hamiltonoperator

$$H_{\mathrm{adj}}=\begin{pmatrix}
2J+\lambda/2&\lambda/2\\
\lambda/2&4J+\lambda/2
\end{pmatrix}.$$

Sein niedriger Eigenwert ist genau $E_1$. Die globale Adjungierte besitzt damit einen realisierten Zustand an der scharfen Untergrenze.

## Ausschluss aller übrigen Sektoren

Alle globalen Darstellungen außer Singulett und Adjungierter beginnen unter $H_0$ frühestens bei $3J$. Wegen $\lambda V\geq0$ bleiben sie darüber. Für jedes endliche $\lambda$ gilt $E_1<3J$.

Außerdem ist $E_0<5J/2$. Schließlich folgt

$$R^2-(Q-J)^2=11J^2+2J(Q-\lambda)>0.$$

Da $Q-J>0$, ist $R>Q-J$, also $\Delta>J/2$. Dies schließt eine Kreuzung mit dem adjungierten Sektor aus. Zusammen ist der globale Satz bewiesen.

## Zahlen und Konsequenzen

| $\lambda/J$ | $E_0/J$ | $E_1/J$ | $\Delta/J$ |
|--:|--:|--:|--:|
| 0 | 0 | 2 | 2 |
| 1 | 0,563508327 | 2,381966011 | 1,818457684 |
| 2 | 1 | 2,585786438 | 1,585786438 |
| 6 | 1,837722340 | 2,837722340 | 1 |
| 8 | 2 | 2,876894374 | 0,876894374 |
| $\infty$ | $5/2$ | 3 | $1/2$ |

Die Entanglementformel aus [Q, Kapitel 8.4] beschreibt damit für alle positiven Kopplungen den tatsächlichen Grundzustand:

$$q=\frac12\left(1-\frac{4J-\lambda/4}{R}\right),\qquad
\operatorname{spec}\rho_A=\{1-q,(q/15)^{[15]},0^{[240]}\}.$$

Im starken Grenzfall ist $q\to5/8$. Die 16 nichtverschwindenden Schmidtgewichte werden dann $3/8$ und fünfzehnmal $1/24$. Diese Werte folgen durch Grenzwertbildung; sie bedeuten keine maximal gemischte Zelle und keine neue Raumzeitdimension.

# Vermittlung mit expliziten Belegungen

## Ein bedingter mikroskopischer Kandidat

Für jeden Clebsch Knoten $s$ und jede Farbe $a=1,\ldots,4$ nehme man fermionische Moden $c_{sa}$. Hier sind Fermionstatistik, Ortsinterpretation und Tensorstruktur **gesetzte** Daten. Sei

$$n_s=\sum_a c^\dagger_{sa}c_{sa},\qquad
H_U=\frac U2\sum_s(n_s-1)^2,\quad U>0.$$

Der Niedrigenergieraum besitzt einen Fermion pro Knoten. Für ein gemeinsames Vektorlabel $v$ und einen antisymmetrischen Farbindizes $A$ werde ein bosonischer Vermittler $b_{vA}$ mit Energie $\Delta_b>0$ zugelassen. Die Gesamtzahl

$$N_{\rm tot}=\sum_s n_s+2\sum_{v,A}b^\dagger_{vA}b_{vA}$$

wird festgehalten. Damit ist bei einem endlichen Graphen auch die Vermittlerbelegung beschränkt.

Auf einer orientierten Kante $e=(i,j)$ definiere für $a<b$

$$K_{e,ab}=c_{jb}c_{ia}-c_{ja}c_{ib}.$$

Auf dem einfach besetzten Paarraum gilt

$$\sum_{a<b}K^\dagger_{e,ab}K_{e,ab}=I-S_{ij}=2P^-_{ij}.$$

Mit den aus der gewählten Kanalstruktur übernommenen Phasen $\kappa_e$ und Beträgen $|\kappa_e|=1$ lautet der bedingte Übergang

$$V=t\sum_{v,A}b^\dagger_{vA}\sum_{e:\,v(e)=v}\kappa_eK_{e,A}
+\text{Adjungierte}.$$

Die Gradbuchhaltung ist $-2+1+1=0\pmod4$. Ein tatsächlich E8 äquivarianter vollständiger Focklift folgt aus dieser Typverträglichkeit noch nicht. Insbesondere müssen Normierung, Statistik und die in Abschnitt 5 diskutierte Symmetriefrage gesondert erfüllt sein.

## Warum in zweiter Ordnung keine fremden Kanten bleiben

Das Entfernen der beiden Teilchen erzeugt zwei Löcher und einen Vermittler. Die Zwischenenergie ist

$$\Delta_{\rm eff}=\Delta_b+U.$$

Zwei verschiedene Kanten erzeugen verschiedene Lochmuster. Bei der Rückprojektion auf den ursprünglichen einfach besetzten Raum gilt daher

$$P K^\dagger_{e,A}K_{f,A}P=0\qquad(e\neq f).$$

Ein gemeinsam benutztes Vermittlerlabel löscht diese Unterscheidung nicht. Im Prüfer wird dies sowohl für überlappende als auch für disjunkte Kanten direkt im fermionischen Fockraum kontrolliert.

Die effektive Wechselwirkung zweiter Ordnung ist deshalb

$$H_{\rm eff}^{(2)}=-\frac{2t^2}{\Delta_b+U}\sum_eP^-_e
=\frac{2t^2}{\Delta_b+U}\sum_eP^+_e+\text{Konstante}.$$

Der Faktor zwei entspricht der Normierung $K^\dagger K=2P^-$. Bei $W=K/\sqrt2$ wird er durch eine entsprechend umbenannte Amplitude ersetzt. Die kontrollierte Störungsentwicklung gehört zur Schrieffer und Wolff Methode [W1].

Diese Rechnung entscheidet die konkrete Frage nach Kreuztermen in zweiter Ordnung. Sie verbietet nicht generell die Mehrkörperterme höherer Ordnung. Sobald mehrere virtuelle Übergänge denselben Endbelegungszustand auf verschiedenen Wegen erreichen, können verbundene Beiträge verbleiben. Ein vollständiger Vielteilchenvergleich muss daher die nächsten Ordnungen und die Norm der vernachlässigten Beiträge kontrollieren. Für unbeschränkte wachsende Systeme genügt eine kleine globale Norm nicht; erforderlich ist eine lokale Störungsabschätzung.

Symmetrische Vermittler würden einen zusätzlichen Beitrag $-J_+P^+$ liefern. Das relative Austauschgewicht wäre dann $J_--J_+$. Der Name E8 allein legt sein Vorzeichen nicht fest. Der oben gewählte Kandidat enthält solche zusätzlichen Vermittler nicht; ihr Ausschluss ist Teil seiner Definition und keine neue Herkunftsherleitung.

# Ein zusätzlicher Symmetriekonflikt

## Die Belegungsregel erhält nicht die volle Ortsmischung

Die Interpretation „Spinorgewicht ist Ort“ verwendet die 16 Komponenten einer Spin(10) Darstellung als 16 getrennte Plätze. Eine kontinuierliche Spin(10) Transformation mischt jedoch diese Gewichtskomponenten. Ein typischer Bestandteil ihres Generators ist

$$T_{ss'}=\sum_a c^\dagger_{sa}c_{s'a},\qquad s\neq s'.$$

Auf dem Sektor mit $n_s=1$ für jeden Ort erzeugt ein nicht blockierter Transfer eine leere und eine doppelt besetzte Stelle. Deshalb

$$P T_{ss'}P=0,\qquad [H_U,T_{ss'}]P=U T_{ss'}P.$$

Die zweite Gleichung ist nicht null. Dass ein vollständiger Lie Generator mehrere Gewichtstransfers enthält, beseitigt den Konflikt nicht: Die verschiedenen Belegungsdefekte liegen in unterscheidbaren Sektoren. Die Rechnung wurde zusätzlich an zwei Orten mit vier Farben exakt kontrolliert.

Folglich besitzt der so definierte Hamiltonoperator nicht gleichzeitig die behauptete feste Ortsbelegung und eine ungebrochene kontinuierliche Spin(10) Wirkung als gewöhnliche interne Symmetrie dieses Niedrigenergieraums. Das ist eine Aussage über diesen Kandidaten, kein allgemeiner Ausschluss von Spin(10) Modellen, emergenter Symmetrie oder Konstruktionen mit zusätzlichen Eichfreiheitsgraden.

## Zwei konsistente Lesarten

**Clebsch als endliches Kopplungslabor.** Die 16 Orte und ihre diskrete Graphsymmetrie bleiben erhalten, der lokale innere Viererträger trägt SU(4). Die Herkunft aus Spinorgewichten ist eine kombinatorische Konstruktion. Daraus wird nicht automatisch ein dynamischer Spin(10) Eichsektor.

**Spinor als innere Materie.** An einem unabhängig definierten räumlichen Träger $x$ gibt es ein Feld $\psi_{x,\alpha}$ mit innerem Spinorindex $\alpha=1,\ldots,16$. Dann kann Spin(10) intern wirken. Die räumlichen Träger und ihre Nachbarschaften müssen aber aus einer anderen, ausdrücklich gemeinsamen Quellregel hervorgehen.

Für die TOE Fortsetzung ist die zweite Lesart strukturell sauberer. Sie löst den Typkonflikt, aber nicht die Entstehung des räumlichen Netzes. Eine dritte Möglichkeit mit Symmetriebrechung oder emergenter Wiederherstellung verlangt einen eigenen Mechanismus und darf nicht nur die beiden ersten Lesarten sprachlich vermischen.

# Präparation, Aufzeichnung und Zeit

## Exakter Energieprojektor aus demselben Tetramer

Das bekannte Tetramerspektrum liefert unmittelbar

$$P_\Omega=\frac{(H_{\rm tet}-2J)(H_{\rm tet}-3J)(H_{\rm tet}-4J)(H_{\rm tet}-6J)}{144J^4}.$$

Die gleiche Projektion besitzt eine kohärente Achtpunktdarstellung:

$$\boxed{P_\Omega=\frac18\sum_{k=0}^7\exp\left(-\frac{2\pi i kH_{\rm tet}}{8J}\right).}$$

Alle angeregten Energielabel $2,3,4,6$ liegen von null verschieden modulo acht. Die geometrische Summe ist auf ihnen null und auf dem Grundzustand eins.

Ein ideales Verfahren benutzt drei Kontrollqubits, kontrollierte Potenzen von

$$U_8=\exp[-2\pi iH_{\rm tet}/(8J)]$$

und eine inverse Fouriertransformation. Die Anzeige 000 realisiert den Krausoperator $P_\Omega$, nicht $(3/4)P_\Omega$ wie der in [Q, Kapitel 10] verwendete 32 Zweige Filter.

Die physikalische Implementierung erfordert kontrollierte Zeitentwicklung, die passende Pulsdauer $\tau=\pi\hbar/(4J)$, Fourieroperationen und ein initialisiertes Register. Deren Verfügbarkeit ist nicht bereits durch das unkontrollierte $H_{\rm tet}$ bewiesen. Ebenso ist aus weniger mathematischen Kontrollzuständen keine kleinere reale Gatterzahl abzulesen. Es wurde keine neue vollständige Hardwarekompilation ausgeführt.

## Alle Erfolgswahrscheinlichkeiten

Für den ursprünglichen Eingang

$$|\chi_0\rangle=\frac{|01\rangle-|10\rangle}{\sqrt2}
\otimes\frac{|23\rangle-|32\rangle}{\sqrt2}$$

ist $|\langle\Omega|\chi_0\rangle|^2=1/6$. Der ideale Energieprojektor besitzt daher Präparationserfolg $1/6$, gegenüber $3/32$ beim ursprünglichen LCU Filter. Diese ideale Projektionsausbeute war bereits als möglicher Verbesserungsweg angesprochen; die Achtpunktformel macht ihre Bindung an den Tetramergenerator explizit.

Mit demselben idealen Projektor am Ende ergeben sich:

\Needspace{9\baselineskip}

| Protokoll | Behalten | Frisch | Rohwahrscheinlichkeiten |
|:--|--:|--:|:--|
| Ursprünglicher Dreierzyklus | 1 | $17/32$ | $1/6$ und $17/192$ |
| Ausgeglichener CNOT Tick | 1 | $1/2$ | $1/6$ und $1/12$ |

Die Rückkehrwerte sind auf erfolgreiche Präparation bedingt; die letzte Spalte bezieht sich auf jeden begonnenen Versuch und beinhaltet beide Filter. Alle nicht aufgeführten Ausgänge sind Misserfolge. Diese Variante ersetzt nicht nachträglich den ursprünglichen festgelegten Test. Sie ist ein separates Experiment mit einer anderen Filterressource.

## Was das Zeitproblem dadurch gewinnt

Derselbe gesetzte Tetramergenerator legt nun das Energiespektrum, die Isolierung des Zielzustands und die notwendige Filterperiode relativ zu $J/\hbar$ fest. Das ist stärker als drei voneinander unabhängige Formeln.

Eine autonome Präparation beliebiger Eingänge folgt trotzdem nicht. Jede ausschließlich aus Swaps erzeugte zellinterne Entwicklung erhält den Singulettanteil. Noch allgemeiner kann eine geschlossene unitäre Entwicklung nicht alle unterscheidbaren Eingangszustände in denselben reinen Zustand überführen: Sie erhält Skalarprodukte beziehungsweise Spurdistanzen. Ein Register, ein Reservoir oder Erfolgsselektion muss die fehlende Information übernehmen. [Q, Kapitel 6.5 und 10.2]

Auch ein Grundzustand tickt unter seinem eigenen Hamiltonoperator nicht. Ein lesbares Signal entsteht aus einer nichtstationären Präparation, einer relationalen Uhrkonditionierung oder einer expliziten Kopplung an Aufzeichnungen. Die existierende Zweizellenoszillation und die Page und Wootters Konstruktion bleiben gültig in ihrer jeweiligen Ausführung. Ihre Uhrbasis, der Anfangszustand und die Zugriffsklasse sind weiterhin Quelldaten. [Q, Kapitel 8.5 und 9]

# Phasen und die abstrakte chirale Naht

## Eine konkrete Gitterphase statt beliebiger Markierungen

Wähle eine geordnete ganzzahlige Basis des rekonstruierten geraden Gitters $L=E_8$ und deren Grammatrix $G$. Definiere die ganzzahlige Dreiecksmatrix

$$B_{ii}=G_{ii}/2,\quad B_{ij}=G_{ij}\ (i>j),\quad B_{ij}=0\ (i<j).$$

Für Gitterkoordinaten $m,n\in\mathbb Z^8$ setze

$$\epsilon(m,n)=(-1)^{m^TBn}.$$

Die Bilinearität liefert exakt die Cocyclebedingung

$$\epsilon(m,n)\epsilon(m+n,p)=\epsilon(n,p)\epsilon(m,n+p).$$

Da $B-B^T$ modulo zwei mit $G$ übereinstimmt,

$$\frac{\epsilon(m,n)}{\epsilon(n,m)}=(-1)^{m^TGn}.$$

Die verdrehten Gitteroperatoren erfüllen daher

$$e_m e_n=\epsilon(m,n)e_{m+n}.$$

Für benachbarte einfache Wurzeln mit innerem Produkt $-1$ entsteht eine relative Phase $-1$ zwischen den beiden Kompositionsreihenfolgen. Ein Basiswechsel der zentralen Erweiterung kann den Cocyclevertreter ändern; die entsprechende Kommutatorphase bleibt erhalten. Diese Konstruktion ist Standardmathematik und wurde für eine explizite E8 Grammatrix symbolisch kontrolliert. Sie benötigt keine willkürliche Zuordnung von Primzahlen zu Paulioperatoren.

Die adjungierte Wirkung auf der verdrehten Gitterbasis wird durch

$$e_m^\dagger=\epsilon(m,-m)^{-1}e_{-m}$$

festgelegt. Damit ist die Linksverschiebungsdarstellung unitär. Für die volle Vertexalgebra gehören zusätzlich die üblichen Oszillatoradjunktionen und die konforme Involution dazu; sie werden nicht durch die kurze Gruppenalgebraformel ersetzt. [W2, Abschnitt 4.4]

## Das abstrakte E8 Objekt ist konstruierbar

Die positive gerade Gitterstruktur liefert die unitäre Gittervertexalgebra

$$V_{E_8}=\mathcal F_8\otimes\mathbb C_\epsilon[E_8].$$

Dabei steht $\mathcal F_8$ für den Fockraum der acht Heisenbergoszillatoren. Der Gradierungsoperator ist

$$L_0=N+\lVert\alpha\rVert^2/2.$$

Im Gewicht eins stehen acht Oszillatorzustände und 240 Wurzelzustände, insgesamt 248. Die vier Glueklassen organisieren die Erweiterung von $D_{5,1}\otimes A_{3,1}$. Die Wurzeloperatoren besitzen das führende Operatorprodukt

$$V_\alpha(z)V_\beta(w)\sim
\epsilon(\alpha,\beta)(z-w)^{(\alpha,\beta)}V_{\alpha+\beta}(w)+\cdots.$$

Positivität und die unitäre Struktur positiver gerader Gittervertexalgebren sind etabliert [W2, Theorem 4.12]. Damit ist die abstrakte Existenz der passenden chiralen Algebra kein freies Wunschobjekt. Das ist jedoch nicht gleichbedeutend mit einem Nachweis des nativen Skalierungsgrenzwertes aus dem Clebsch Modell oder der ursprünglichen markierten Compilerimplementierung. Dafür fehlen weiterhin konvergente Korrelationsfunktionen, eine nachgewiesene chirale Architektur und ein phasentreuer Abgleich der Markierungen.

Eine nichtchirale SU(4) Kette besitzt nicht durch Addition eines ebenfalls nichtchiralen D5 Systems plötzlich chirale Differenz acht. Ein passender Rand eines höherdimensionalen Modells ist eine mögliche Architektur. Die zusätzlich gebaute Dimension ist dabei ausdrücklich eine Annahme und noch keine Herleitung unserer vierdimensionalen Raumzeit. [Q, Kapitel 11]

# Viele Zellen und die Dimensionsfrage

## Die schlechte Schranke proportional zur Zellzahl ist nicht fundamental

Die ursprüngliche Abschätzung

$$\Delta\geq2J-\frac58(N-1)\lambda$$

kontrolliert die Summe aller Brücken mit einer globalen Norm. Sie wird bei großem $N$ unbrauchbar, beweist aber keine tatsächliche Schließung der Lücke. [Q, Kapitel 8.6]

Für eine zusätzlich festgelegte translationsinvariante Familie auf $\mathbb Z^d$ mit endlicher Wechselwirkungsreichweite kann jeder Tetramer als ein lokaler Träger der Dimension 256 behandelt werden. $\sum_xH_{{\rm tet},x}$ ist in der lokalen Energieeigenbasis ein klassischer Produkthamiltonoperator mit eindeutigem Grundzustand und Lücke $2J$. Hinreichend kleine lokale Brückenterme fallen dann unter Stabilitätssätze für perturbierte gapped Produktsysteme. Sie liefern eine von der Systemgröße unabhängige positive Lücke und einen thermodynamischen Grundzustand [W3, Theorem 1 und Example 2].

Das ist eine bedingte Lösung der thermodynamischen Stabilitätsfrage für eine präzise definierte schwach gekoppelte Familie. Es ist kein hier numerisch ermittelter universeller Grenzwert für $\lambda/J$, kein Resultat für beliebige Graphen und keine Fortsetzung des allkoppligen Zweizellensatzes auf beliebig viele Zellen.

Die physikalische Konsequenz ist wichtig: Ein strikt positiver thermodynamischer Gap in allen Sektoren schließt gerade die benötigten beliebig energiearmen propagierenden Photon und Gravitonmoden aus. Ein vollständiger Vakuumkandidat benötigt deshalb einen geeigneten lückenlosen Sektor, eine kritische Skalierung oder weitere dynamische Freiheitsgrade. Ein stabiles Tetramerprodukt ist ein kontrolliertes Ausgangsmodell, nicht automatisch das physikalische Vakuum.

## Explizite Gegenfamilie gegen eine eindeutige Dimension

Für jedes $d\geq1$ bilde die kartesische Graphfamilie

$$\Gamma_{d,L}=(\mathbb Z/L\mathbb Z)^d\mathbin\square\Gamma_{\rm Cl}.$$

An jedem räumlichen Gitterpunkt sitzt derselbe Clebsch Baustein. Der Laplaceoperator ist

$$\mathcal L=\mathcal L_{d,L}\otimes I_{16}+I\otimes\mathcal L_{\rm Cl}.$$

Die normierte Wärmerückkehr faktorisiert. Mit dem exakt bekannten Clebsch Spektrum

$$P_{\rm Cl}(\tau)=\frac{1+10e^{-4\tau}+5e^{-8\tau}}{16}$$

und der unendlichen Gittergrenze

$$P_{\mathbb Z^d}(\tau)=[e^{-2\tau}I_0(2\tau)]^d
\sim(4\pi\tau)^{-d/2}$$

ergibt sich

$$P_d(\tau)\sim\frac1{16}(4\pi\tau)^{-d/2},\qquad d_s\longrightarrow d.$$

Hier wird zuerst $L\to\infty$ genommen. Für große endliche Systeme entspricht dies dem Bereich $1\ll\tau\ll L^2$. Die Familie ist ein **Gegenmodell**, kein nativer Ursprungsvorschlag: Die innere TFPT Struktur bleibt dieselbe, die großskalige Dimension ist beliebig gewählt.

Daraus folgt exakt, dass die interne Struktur allein die Dimension nicht auswählt. Eine zusätzliche gemeinsame Gesetzmäßigkeit muss Graphfamilie, Zustand und Propagation bestimmen. Der positive Hermitesche $2\times2$ Kegel oder die Anzahl dreier Paulioperatoren beseitigen diese Nichtidentifizierbarkeit nicht.

## Was eine echte Geometrieherleitung messen müsste

Ein nativer Kandidat muss lokale korrelierte Anregungen besitzen. Erst deren inverser Propagator

$$G^{-1}_r(\omega,q)=Z_r^{-1}\big[(\omega-w_r\cdot q)I-
\sigma^aV_{r,aj}q_j\big]+\cdots$$

liefert einen physikalischen charakteristischen Kegel. Die verschiedenen Sektoren $r$ müssen nach zulässigen gemeinsamen Koordinatenänderungen und Renormierung kompatible Kegel besitzen. Ein bloß individuell invertierbares $V_r$ reicht nicht für universelle Geometrie. [Q, Kapitel 13]

Die überprüfbare Aufgabe lautet daher: tatsächliche Pole, positive Residuen, räumliche Volumenskalierung, Spektraldimension, lokale Ausbreitung und ein gemeinsamer Zustand aus demselben Generator. Eine bereits eingesetzte dreidimensionale Weylmatrix ist ein Kontrollbeispiel, keine Rekonstruktion.

# Materie, Gravitation und physikalische Parameter

## Chirale Materie

Die Ladungstabelle einer 16 von Spin(10) besitzt die passenden endlichen Anomalieauslöschungen. Drei Kopien dieser Tabelle sind noch kein Nachweis dreier propagierender chiraler Familien. Ein verbindlicher Abschluss braucht einen konkreten Diracoperator, einen Index oder einen anderen quantitativen Schutz der Familienzahl, ein konsistentes fermionisches Maß und die kontrollierte Entfernung unerwünschter Spiegelpartner. [Q, Kapitel 3.2 und 14.1]

Zwei mögliche Regulierungswerkzeuge sind Operatoren mit Ginsparg und Wilson Relation sowie Konstruktionen mit getrennten physikalischen und Spiegelrändern. Lüscher liefert eine nichtperturbative Konstruktion für anomaliefreie **abelsche** Gittereichtheorien [W4]; diese Reichweite darf nicht still auf den gesamten hier verlangten nichtabelschen Aufbau übertragen werden.

Eine aktuelle Arbeit von Araki und Mitautoren untersucht symmetrische Massenerzeugung für Randfermionen numerisch auf einem **zweidimensionalen euklidischen** Gitter [W5]. Sie ist ein konstruktiver Hinweis für Spiegelentkopplung, aber kein vierdimensionaler TFPT Nachweis. Ein hier verwendeter Mechanismus müsste zusätzlich vermeiden, dass die gewünschten physikalischen Familien ebenfalls verschwinden, oder dass unerwünschte langlebige topologische Sektoren bleiben.

Der SU(4) Faktor $A_3$ als Partner von $D_5$ darf nicht mit dem Pati und Salam Farbfaktor $SU(4)_c\subset\operatorname{Spin}(10)$ verwechselt werden. Eine diagonale Identifikation wäre eine neue Brechungsannahme. [Q, Kapitel 13.3]

## Gravitation

Aus

$$\det(tI+\mathbf x\cdot\boldsymbol\sigma)=t^2-|\mathbf x|^2$$

folgt eine Lorentzform, kein dynamischer Graviton. Der nötige gravitative Test ist ein positiver masseloser Spin zwei Pol im geeigneten physikalischen Korrelator, mit genau zwei Helizitäten, passenden Eichidentitäten und gemeinsamer Kopplung an sämtliche Materiesektoren. [Q, Kapitel 13.5]

Eine mögliche diagnostische Form nach Auswahl physischer transversaler Moden wäre

$$\langle h_{\mu\nu}h_{\rho\sigma}\rangle(p)
\sim\frac{Z_g\,\Pi^{(2)}_{\mu\nu,\rho\sigma}(p)}{p^2+i0},\qquad Z_g>0.$$

Diese Formel ist ein Testziel, keine Behauptung, dass ein entsprechendes $h_{\mu\nu}$ bereits aus den Tetramern konstruiert sei. Unter Lorentzinvarianz, passender Polstruktur und **vorhandenem** masselosem Spin zwei Teilchen schränkt das weiche Emissionsargument die Kopplung auf universelle Form ein [W6]. Es beweist nicht rückwärts die Existenz dieses Teilchens.

Eine Spektralwirkung könnte das effektive Ziel organisieren. Ein Diracoperator, seine Darstellung, die Spektralfunktion, deren Momente und eine bereits vorausgesetzte Mannigfaltigkeit sind dann aber neue Daten, solange sie nicht im nativen Prozess identifiziert wurden. Kein solcher neuer Gravitationsgenerator ist in dieser Fortsetzung bewiesen.

## Kopplungen, Massen und Vergleich mit Daten

Die angegebene elektromagnetische Wurzel

$$\alpha^{-1}=137{,}0359992168407125\ldots$$

ist ein präziser Wert der in [Q, Kapitel 14.2] festgelegten Gleichung. Der datierte CODATA Vergleich 2022 beträgt $137{,}035999177(21)$; die entsprechende Tabelle ist weiterhin als 2022 Tabelle gekennzeichnet [W7]. Der Abstand liegt in der im Original angegebenen Größenordnung 1,9 experimenteller Standardabweichungen.

Der entscheidende offene Punkt ist nicht eine weitere Nachkommastelle. Es fehlen die Herleitung des physikalischen Kopplungsschemas, der Übergang zur Thomson Kopplung und eine kontrollierte Theorieunsicherheit. Dieselbe Forderung betrifft sämtliche laufenden Massen, Schwellen und Mischungsmatrizen.

Ein brauchbarer gemeinsamer Ausgabevertrag muss für jede Größe festlegen: Quelldefinition, Renormierungsskala und Schema, extern gemessene Inputs, Transferformel, theoretischen Fehler und vorab fixiertes Ablehnungskriterium. Eine Quellmasse darf nicht je nach Passung einmal als Polmasse und einmal als laufende Masse gelesen werden. Der Parameter $\Lambda_{f,j}$ im historischen Massenansatz ist keine Vorhersage, solange er frei ist.

Die im Original dokumentierten ungünstigen Leptonverhältnisse, der historische Higgsbereich, die Inflationsamplitude und die zu kurzen Protonlebensdauern bestimmter geeichter SO(10) Zweige bleiben negative Informationen. In dieser Arbeit wurde kein neuer vollständiger Schleifenlauf, kein hadronischer Transfer und keine globale Datenauswertung ausgeführt. Eine Erklärung muss diese Punkte gemeinsam beheben; die Eichgruppe erst nach dem Protonvergleich auszutauschen wäre keine Vorhersage. [Q, Kapitel 14.3 bis 14.6]

# Zustand, Quantenauslesung und kosmologische Fragen

## Ein gemeinsames positives Prozessfunktional

Sind Algebra, Hamiltonoperator, Anfangszustand und Instrumente vollständig festgelegt, ist die Mehrzeitstatistik berechenbar. Für eine gewählte Folge von Ergebnissen und Kontrollen sei $K_h$ das entsprechende Produkt aus unitären Entwicklungen und Krausoperatoren. Dann

$$p(h)=\operatorname{Tr}(K_h\rho_0K_h^\dagger).$$

Die Gramwerte $\operatorname{Tr}(K_u\rho_0K_v^\dagger)$ tragen zusätzlich relative Phasen. Das liefert eine konkrete positive Prozessstatistik, sobald die genannten Daten tatsächlich aus demselben Quellenvertrag stammen. GNS und Prozesstensorrekonstruktion erklären ihre minimale Darstellung; sie wählen $\rho_0$ und die Operationen nicht aus. [Q, Kapitel 12]

In dieser Fassung ist die Quantenmechanik ausdrücklich vorausgesetzt. Ein Anspruch, auch die Born Regel herzuleiten, verlangt zusätzliche operationelle Axiome und eine Rekonstruktion des gesamten Zustands und Kompositionsraums. Der Nachweis von Mermin Kontextualität, CHSH Werten oder quadratischer Interferenz ist keine unabhängige Herleitung der bereits eingesetzten Born Regel. [Q, Kapitel 18]

## Zeitpfeil und Messung

Ein unbeschränktes Registerband kann reduzierte irreversible Dynamik mit einer global reversiblen Entwicklung vereinbaren. Der besondere einlaufende Zustand und die Zugriffsbeschränkung bleiben jedoch eine Anfangsbedingung. Eine reine Definition „Zeit ist Gedächtnis“ ersetzt sie nicht.

Ebenso erklärt Dephasierung die Unterdrückung zugänglicher Interferenz, aber wählt für sich kein einzelnes Ereignis aus. Eine vollständig operationelle Theorie kann ihre Wahrscheinlichkeitsregel als Axiom verwenden. Eine zusätzliche objektive Kollapsdynamik müsste dagegen selbst im Generator stehen, Energie und Lokalitätsfragen kontrollieren und abweichende Vorhersagen besitzen. Diese Fortsetzung entscheidet nicht zwischen solchen Interpretationen. [Q, Kapitel 18.6]

## Dunkler Sektor, Baryogenese und schwarze Löcher

Die offenen Fragen verlangen jeweils dieselbe Quellbuchhaltung, nicht neue metaphorische Bezeichnungen:

**Dunkle Materie.** Ein Sektor muss Stabilität, gravitative Kopplung, geringe sichtbare Wechselwirkung, kosmologische Produktion und Verteilung gemeinsam besitzen. Ein nicht ausgelesenes Register erfüllt diese Bedingungen nicht durch seine Unsichtbarkeit. Ein konkreter neuer Kandidat wird hier nicht hergeleitet.

**Dunkle Energie.** Eine kleine Zahl für $\rho_\Lambda$ benötigt eine effektive Wirkung und Stabilität gegen quantenmechanische Korrekturen. Ein frei addierter Vakuumterm würde die gewünschte Größe einstellen, aber nicht erklären. Der historische Exponentialansatz ist keine neue Berechnung des Vakuumfunktionals.

**Materieüberschuss.** Eine Baryonendichteformel ersetzt keinen Prozess, der aus den Anfangsbedingungen die Asymmetrie erzeugt. Erforderlich sind passende Symmetrieverletzung, Nichtgleichgewicht und eine quantitativ berechnete Ausbeute.

**Starke CP Frage.** Eine interne Pfaffianstruktur muss in das physikalische Maß, die Quarkmassenphasen und deren Renormierung übertragen werden. Ein Zeichenargument ohne diesen Transfer genügt nicht. Ein Schutzmechanismus oder ein Axionsektor wäre eine konkrete Zusatzkonstruktion, deren Parameter und Kosmologie ebenfalls stammen müssen.

**Schwarze Löcher.** Erst ein gravitativer Sektor mit Horizonten erlaubt die Frage nach Flächenentropie, Verdampfung und rekonstruierbaren Algebren. Die Entropie eines endlichen Registers ist dafür kein Ersatz. Ein allgemeiner Flächenterm aus dem vorliegenden Zellmodell wird hier nicht nachgewiesen.

Diese Aussagen präzisieren die Anschlussanforderungen des Originals [Q, Kapitel 20]; sie sind keine Behauptung, die genannten physikalischen Probleme bereits durch das Zweizellenergebnis gelöst zu haben.

# Arithmetik und die gemeinsame Quelle

Die E8 Schalenidentität $N(2n)=240\sigma_3(n)$ und der zugehörige Dirichletausdruck $240\zeta(s)\zeta(s-3)$ sind echte arithmetische Beziehungen. Sie verwandeln einen beliebigen positiven Zustandskern trotzdem nicht in die benötigte signierte Weil Form. Dafür muss das gesamte Funktional einschließlich Pol und archimedischem Beitrag exakt identifiziert werden. [Q, Kapitel 17]

Die in Abschnitt 7 festgelegte Gitterphase löst die Auswahl einer kohärenten Kompositionsphase **auf dem Gitter**. Eine Verbindung zu sämtlichen Primzahlen benötigt zusätzlich eine Abbildung von arithmetischen Operationen in diese Algebra, die Multiplikation, Adjunktion, Norm und Auslesung gemeinsam erhält. Eine willkürliche Tabelle $p\mapsto\alpha_p$ wäre eine weitere freie Eingabe.

Aus multiplikativer Additivität und Monotonie folgt $e(n)=c\log n$. Der Beweis im Original ist korrekt. Er bestimmt weder einen lokalen vierdimensionalen Hamiltonoperator noch eine physikalische Realisierung aller Primmoden. Auch die Nenner und die Präzisionskosten einer Eta Auslesung bleiben Teil der Ressourcenrechnung. Eine kleine normierte Amplitude ist noch kein zertifiziertes Nullstellensignal.

Die Gaußsummenidentität des Faktorisierungszweigs ist nicht automatisch ein effizienter Algorithmus. Kosten in $N$ müssen in der Eingabelänge $\log N$ bilanziert werden. Keine der hier konstruierten Filter oder Gitterphasen liefert einen bewiesenen allgemeinen Faktorisierungsgewinn, RH Beweis oder P gleich NP Satz. Eine physikalische TOE müsste diese separaten mathematischen Probleme auch nicht automatisch lösen, um ihre physikalischen Vorhersagen zu tragen.

# Der vollständige TOE Vertrag nach dieser Fortsetzung

## T1: Primitive Quelle und Auswahl

Erhalten bleiben die exakten Konsequenzen des markierten Ausgangsobjekts. Neu ist eine konkret ausgewiesene Rangbedingung, die $a=1/7$ auswählen würde. Die native Notwendigkeit dieser Bedingung, der Ortsinterpretation, Statistik, Energien, Hilfsregister und Zustandswahl ist weiterhin nicht hergeleitet. Ein gemeinsamer Quellenvertrag muss diese Daten entweder als Axiome ausweisen oder aus einer ausdrücklich stärkeren Regel ableiten.

## T2: Native chirale E8 Naht

Die abstrakte unitäre Gittervertexalgebra einschließlich Cocycle und Gradierung ist konstruktiv beschrieben. Offen bleiben der phasentreue native Adapter, die ursprüngliche Halbladungsmarkierung im selben Modell, die analytischen Operator und Energiebedingungen sowie der Skalierungsnachweis aus dem physikalischen Generator. Die Standardkonstruktion ersetzt diese Herkunft nicht.

## T3: Lokaler unitärer Ursprung in drei Raumrichtungen und einer Zeit

Der Einzelschritt, die endlichen Kopplungen und der Lorentzkegel sind konkrete Bausteine. Die Gegenfamilie zeigt jetzt ausdrücklich, dass dieselbe innere Struktur mehrere räumliche Dimensionen zulässt. Eine native Auswahl des Graphen, ein geeigneter kohärenter Grenzwert und universelle Kegel sind noch erforderlich.

## T4: Chirales Standardmodellmaß

Die endlichen Anomaliesummen sind sinnvoll. Die Belegungsprüfung verhindert eine unbemerkte Gleichsetzung von Spinorgewichtsplätzen und innerer Spin(10) Materie. Benötigt bleiben der tatsächliche chirale Diracoperator, die Familienauswahl und ein nichtperturbativ konsistentes Maß mit Spiegelentkopplung.

## T5: Wechselwirkender Kontinuumsgrenzwert

Der Zweizellenzweig ist nun für alle positiven Kopplungen exakt kontrolliert. Schwach gekoppelte translationsinvariante Tetramerfamilien besitzen unter den genannten Literaturvoraussetzungen einen stabilen thermodynamischen Bereich. Das liefert noch keinen relativistischen vierdimensionalen lückenlosen Wechselwirkungsgrenzwert mit der geforderten Streuung und Clusterstruktur.

## T6: Kopplungen und vollständiger Massensektor

Der Vermittlungskoeffizient ist im expliziten Belegungsmodell in zweiter Ordnung bestimmt. Seine primitiven Energien und Amplituden bleiben Inputs. Die präzisen historischen Zahlenformeln benötigen ihren gemeinsamen physikalischen Transfer. Vollständige Eichkopplungen, Neutrinotextur und Massenskala sind dadurch noch nicht ausgewählt.

## T7: Quantisierter Spin zwei Sektor

Weder der Kegel noch der exakte Gap erzeugen einen masselosen Spin zwei Pol. Ein entsprechender positiver physikalischer Sektor, seine zwei Helizitäten und universelle Kopplung bleiben aus der Quelle zu konstruieren. Diese Fortsetzung behauptet dafür keinen Abschluss.

## T8: Physikalischer Zustand und gemeinsames Funktional

Ein genauer idealer Energieprojektor und sämtliche bedingten und rohen Echoergebnisse sind konstruiert. Das löst eine Präparationsaufgabe im festgelegten endlichen Experiment, nicht den Ursprung des kosmologischen Zustands, der Aufzeichnungen und des Zeitpfeils. Die positive Prozessstatistik ist nach Wahl der Daten bestimmt; ihre gemeinsame physische Auswahl ist weiterhin offen.

# Konkrete Konsequenzen für die weitere Rekonstruktion

Das Zweizellenkapitel kann unmittelbar um den allkoppligen Grundzustandssatz, die adjungierte erste Anregung und $\Delta>J/2$ ergänzt werden. Die bisherige Marke $8J$ sollte ausdrücklich als Grenze eines alten Beweises gekennzeichnet werden, nicht als vermuteter physischer Übergang.

Die Präparationsvariante sollte als eigenes Protokoll mit kontrolliertem $U_8$ geführt werden. Vor einem Hardwarevergleich sind kontrollierte Simulationskosten, Pulsfehler, Energieauflösung und Registerfehler zu berechnen. Die ursprünglichen Rohwahrscheinlichkeiten und die neue Variante dürfen nicht vermischt werden.

Beim mikroskopischen Ursprung steht als nächste Architekturentscheidung an, ob die 16 Spinorkomponenten räumliche Gewichtsplätze oder innere Materiefreiheitsgrade sind. Die direkte feste Belegung lässt nicht beide Rollen gleichzeitig unverändert zu. Diese Entscheidung liegt logisch vor der weiteren Eich und Raumzeitrekonstruktion.

Die anschließende gemeinsame Rechnung sollte auf genau einem festgelegten Hamiltonoperator und Zustandsvertrag beruhen. Dessen zweiter und vierter Ordnungsanteil, Ein und Mehrzeitkorrelatoren, endliche Größenfolge und verschiedene Materiekegel müssen dieselbe Quelle verwenden. Ein unabhängiger rechnerischer Erfolg in jeweils einem anderen Modell wird als solcher behalten, aber nicht zu einer gemeinsamen TOE addiert.

**Gesamtbefund:** Die endliche Dynamik ist jetzt an einer wesentlichen Stelle vollständig gelöst. Mehrere zusätzliche Anschlüsse sind konstruktiv und reproduzierbar. Die vollständige Theorie unserer Realität ist damit nicht bewiesen. Ihre verbleibenden Lücken sind insbesondere konkrete Quell und Grenzwertfragen, nicht bloß fehlende algebraische Kosmetik.

# Reproduktion und Quellen

## Ausführung und Prüfumfang

Zum Paket gehören der Prüfer `verify_reconstruction.py` und dieses Dokument. Die Ergebnisse stehen in `verification_results.json` sowie in der optimierten Kontrollausgabe `verification_results_optimized.json`. Die Anleitung steht in `README.md`. Ausführung:

```bash
python3 verify_reconstruction.py --output verification_results.json
python3 -OO verify_reconstruction.py --output verification_results_optimized.json
cmp verification_results.json verification_results_optimized.json
```

Beide Läufe wurden ausgeführt; ihre Ergebnisdateien sind bytegleich. Verwendet wurden Python 3.13.5, NumPy 2.3.5 und SymPy 1.14.0. Der Prüfer importiert weder ursprünglichen TFPT Code noch ursprüngliche Spektraltabellen. Explizite Fehlerbedingungen bleiben unter Optimierung aktiv.

Die exakt geprüften Tensoridentitäten verwenden 65 536 Komponenten, aber keine dichte Matrix dieser Größe. Die spektrale Gegenrechnung verwendet orthogonale Youngdarstellungen aller Partitionen von acht mit höchstens vier Zeilen. Die Summe ihrer mit SU(4) Dimensionen gewichteten Größen beträgt exakt $4^8$. Gleitkommawerte dieser Blöcke sind keine exakten algebraischen Eigenwerte; ihre Rolle ist die unabhängige Kontrolle der ausgeschriebenen Herleitung.

Nicht ausgeführt wurden: ein vollständiger ursprünglicher Repositorylauf, eine Lean Formalisierung, die originale Clebsch Vielteilchendiagonalisierung, eine vollständige neue Schaltungssynthese, Hardwareversuche, vierdimensionale Gitterchiraldynamik, Schleifenläufe, ein Gravitationsgrenzwert oder ein RH Beweis. Der Zustandsfilter ist algebraisch verifiziert, nicht als vollständige Gatefolge exportiert. Die allgemeinen Dimensionsgrenzwerte und der globale allkopplige Satz werden analytisch bewiesen; die endlichen Kontrollen ersetzen diese Beweise nicht.

## Quellenverzeichnis

**[Q]** Bereitgestellte Gesamtdarstellung: *TFPT und der Universalraum. Von einer gemeinsamen mathematischen Struktur zu einer möglichen Physik der Veränderungen und Aufzeichnungen*, Version 1.1, 14. September 2026, 90 PDF Seiten. Dateiname `TFPT_Universalraum_Gesamtdarstellung_2026-09-14.pdf`. SHA256:

`320f2643426902ec8bede279636bf72601cf529089ab3a1e26fd65e7ebceb9b0`

Die Kapitelverweise beziehen sich auf diese Datei. Ihre Originalprüfer und alle elf zugrunde liegenden Einzelquellen wurden in dieser Fortsetzung nicht als vollständige Originalsuite ausgeführt.

**[W1]** S. Bravyi, D. DiVincenzo, D. Loss, *Schrieffer-Wolff transformation for quantum many-body systems*, Annals of Physics 326 (2011), 2793–2826. arXiv:1105.0675. Allgemeiner Rahmen kontrollierter effektiver Hamiltonoperatoren; keine Quelle des hier verwendeten nativen TFPT Hamiltonoperators.

**[W2]** C. Dong, X. Lin, *Unitary vertex operator algebras*, arXiv:1308.2361, insbesondere Abschnitt 4.4 und Theorem 4.12. Positive gerade Gitter liefern unitäre Gittervertexalgebren. Die Anwendung auf das bereits rekonstruierte E8 Gitter ist von einer nativen physikalischen Grenzwertkonstruktion zu unterscheiden.

**[W3]** D. A. Yarotsky, *Ground states in relatively bounded quantum perturbations of classical lattice systems*, Communications in Mathematical Physics 261 (2006), 799–819; arXiv:math-ph/0412040. Insbesondere Theorem 1, Theorem 2 und Example 2. Verwendet wird nur der Bereich hinreichend kleiner lokaler, translationsinvarianter Störungen endlicher Reichweite auf einem bereits festgelegten Gitter.

**[W4]** M. Lüscher, *Abelian chiral gauge theories on the lattice with exact gauge invariance*, Nuclear Physics B 549 (1999), 295–334; arXiv:hep-lat/9811032. Die abelsche Reichweite ist wesentlich.

**[W5]** S. Araki, H. Fukaya, T. Onogi, S. Yamaguchi, *Symmetric Mass Generation for Domain-Wall Fermions*, arXiv:2608.29963, eingereicht am 30. August 2026. Preprint; numerische Untersuchung auf einem zweidimensionalen euklidischen Gitter, kein hier verifizierter vierdimensionaler Abschluss.

**[W6]** S. Weinberg, *Photons and Gravitons in S-Matrix Theory: Derivation of Charge Conservation and Equality of Gravitational and Inertial Mass*, Physical Review 135 (1964), B1049. DOI 10.1103/PhysRev.135.B1049. Verwendet werden die ausdrücklichen Annahmen über Lorentzinvarianz, Polstruktur und vorhandene masselose Teilchen.

**[W7]** NIST, *2022 CODATA adjustment, Fundamental Physical Constants*, offizielle Texttabelle `physics.nist.gov/cuu/Constants/Table/allascii.txt`, aufgerufen am 14. September 2026. Datierte Referenz, nicht als neue Messung von 2026 bezeichnet.
