# TFPT / Universalraum: ausgeschriebene Beweise und Gegenproben

**Ergänzung zur Gesamtkonsolidierung vom 14. September 2026.**

Die folgenden Sätze sind eigenständige mathematische Aussagen mit jeweils angegebenen Voraussetzungen. „Hier hergeleitet“ bedeutet, dass die Rechnung für diesen Audit ausgeschrieben und geprüft wurde; es behauptet keine erstmalige Entdeckung in der mathematischen Literatur. Insbesondere sind unitäre Dilatation, Schur-Komplement und Amplitudenverstärkung etablierte Methoden. Die Beweise schließen weder RH noch die vollständige physikalische Herleitung von TFPT.

## A. Kohärente History und ein expliziter reversibler Vertex

### Satz A1: Ein unterscheidendes inneres Protokoll verändert den Austauschoperator

Sei V=C⁴⊗C⁴ mit Standardbasis |ab⟩, S|ab⟩=|ba⟩, und sei M=Λ²C⁴ mit orthonormaler Basis |a∧b⟩ für a<b. Definiere K:V→M durch

\[
K|ab\rangle=|a\wedge b\rangle\ (a<b),\qquad
K|ba\rangle=-|a\wedge b\rangle,\qquad K|aa\rangle=0.
\]

Dann gilt

\[
K^\dagger K=I-S=2P_-,\quad KK^\dagger=2I_6,\quad\operatorname{rank}K=6.
\]

Erweitere stattdessen den Ausgang um orthogonale geordnete Eingangslabels:

\[
\widetilde K|ab\rangle=K|ab\rangle\otimes|ab\rangle_h.
\]

Dann gilt

\[
\widetilde K^\dagger\widetilde K=I-D,
\qquad D=\sum_a|aa\rangle\langle aa|,
\qquad\operatorname{rank}\widetilde K=12.
\]

**Beweis.** Jeder ungeordnete Zweierblock besitzt für K die Zeile (1,−1). Deren Gram-Matrix ist [[1,−1],[−1,1]]. Die orthogonalen History-Zustände setzen ihr gemischtes Skalarprodukt auf null. Übrig bleibt I₂. Es gibt sechs disjunkte Zweierblöcke und vier Nullspalten. Das beweist sämtliche Formeln. ∎

Für die normierten Zustände |±⟩=(|ab⟩±|ba⟩)/√2 ergeben sich

\[
\|K|+\rangle\|^2=0,\quad\|K|-\rangle\|^2=2,
\qquad
\|\widetilde K|+\rangle\|^2=\|\widetilde K|-\rangle\|^2=1.
\]

Damit geht sowohl die Dunkelheit des symmetrischen Zustands als auch die entsprechende relative Energieabsenkung verloren. Für ein konkretes nichtdiagonales hermitesches X kommutiert I−D nicht mit X⊗I+I⊗X; I−S kommutiert dagegen mit jedem kollektiven U⊗U. Die veränderte Regel hat also nicht nur eine andere Normierung.

Der Satz betrifft genau das in D04 und D01 ausgeschriebene unterscheidende Label `ab`. Eine zusätzliche Operation, die diese Information vor der für den Austausch relevanten Rückkopplung kohärent entfernt, könnte den ursprünglichen K wieder herstellen. Diese zusätzliche Operation muss dann Bestandteil des angegebenen Gesamtvertices sein. Ein bloß behaupteter „unitärer Rückweg“ liefert sie nicht bereits als effektive Gram-Identität.

### Satz A2: Die genaue Interferenzbedingung

Ersetze die orthogonalen Labels im Zweierblock durch normierte Zustände r_ab und r_ba und setze η=⟨r_ab|r_ba⟩. Dann ist der Gramblock

\[
G_\eta=\begin{pmatrix}1&-\eta\\-\bar\eta&1\end{pmatrix},
\qquad\operatorname{spec}G_\eta=\{1-|\eta|,1+|\eta|\}.
\]

**Beweis.** Die Nebendiagonale ist das Produkt aus dem Vorzeichenwechsel des Vermittlers und dem History-Skalarprodukt. Die charakteristische Gleichung ist (λ−1)²−|η|²=0. ∎

Die ursprüngliche Phasenkonvention erfordert η=1. |η|=1 erhält einen dunklen Vektor, aber bei anderer Phase nicht notwendig den ursprünglichen symmetrischen Vektor. η=0 löscht die Aufspaltung vollständig. Diese Bedingung verallgemeinert sich: Jede ursprünglich nichtverschwindende gemischte Gram-Komponente muss durch das History-System mit demselben Skalarprodukt erhalten werden. Phasen dürfen nur durch eine ausdrücklich gemeinsame Änderung von Vertex- und Zustandskonvention absorbiert werden.

**Kanteninformation und innere Information sind verschieden.** Verschiedene Kanten in einem voll besetzten Ortsmodell erzeugen verschiedene Löcher und können deshalb orthogonal sein. Die inneren vertauschten Wege derselben Kante erzeugen dieselben Löcher; diese liefern gerade kein unerwünschtes inneres `ab`-Protokoll.

### Satz A3: Unitärer 22-dimensionaler Austauschbaustein

Setze W=K/√2, P₋=W†W und P₊=I−P₋. Für reelles θ ist

\[
U_\theta=\begin{pmatrix}
P_++cP_-&-sW^\dagger\\sW&cI_6
\end{pmatrix},\qquad c=\cos\theta,\quad s=\sin\theta
\]

auf V⊕M unitär. Außerdem gilt

\[
U_{\pi/2}^{\,2}\big|_V=P_+-P_-=S,
\]

wobei der Vermittler am Ende wieder leer ist.

**Beweis.** W verschwindet auf P₊V und identifiziert P₋V isometrisch mit M. Auf P₊V ist U die Identität; auf P₋V⊕M ist es die gewöhnliche reelle Rotationsmatrix [[c,−s],[s,c]], tensoriert mit I₆. Beide Aussagen folgen unmittelbar. Alternativ ergibt die Blockmultiplikation U†U=I₂₂, weil WW†=I₆, W†W=P₋ und P₊W†=0 gelten. ∎

Das ist ein expliziter Existenzbeweis eines reversiblen Bausteins mit der richtigen Interferenz. Es wählt weder θ noch eine Zeit- oder Energieskala noch die Zulässigkeit seiner kontrollierten Anwendung aus TFPT allein aus.

## B. Ein global kontrollierter Vermittlerkandidat

### Definition des Modells

Γ sei der Clebsch-Graph mit 16 Orten und 40 Kanten. Jeder Ort hat ℋₛ=C|∅⟩⊕C⁴, verschiedene Orte werden als gewöhnliche Tensorfaktoren zusammengesetzt. Ein Antisymmetrischer Paarzustand |A⁻⟩ₑ ist normiert. Für jedes der zehn Vektorlabels r gibt es sechs gewöhnliche Bosonmoden b_r,A. Setze

\[
K_{e,A}=\sqrt2\,|\emptyset\emptyset\rangle_e\langle A^-|_e.
\]

Der harte Gesamtladungssektor ist

\[
\mathcal Q=\sum_s n_s+2\sum_{r,A}n_{r,A}=16.
\]

Mit reellem t und Δ>0 sei

\[
H=H_0+V,\quad H_0=\Delta\sum_{r,A}n_{r,A},\quad
V=\sum_eV_e,\quad
V_e=t(B_e+B_e^\dagger),\quad B_e=\sum_A b^\dagger_{r(e),A}K_{e,A}.
\]

Alle Summen wirken innerhalb des Ladungssektors. Die Zahl der Bosonen ist höchstens acht, daher ist der Sektor endlichdimensional. Die Definition ist ein konkretes hartes Tensorproduktmodell. Eine Identifikation mit dem vollständigen fundamentalen Fermionmodell aus D06 erfordert zusätzlich dessen Statistik- und Phasenkonventionen und wird hier nicht behauptet.

### Satz B1: Globale Norm- und Bandkontrolle

Es gilt ‖Vₑ‖≤4|t| und ‖V‖≤160|t|. Für |t|/Δ=1/640 ist das von H₀=0 ausgehende niedrige Band vom übrigen Spektrum von H um mindestens Δ/2 getrennt.

**Beweis.** Bezüglich der beiden Kantenbesetzungen „beide besetzt“ und „beide leer“ ist Vₑ ein selbstadjungierter Offdiagonalblock. Auf dem ersten Raum trägt nur der antisymmetrische Sechseranteil bei. Sein Umwandlungsblock hat die Form

\[
B=\sqrt2\,(b_1^\dagger,\ldots,b_6^\dagger).
\]

Auf einem Ausgangsraum mit n_r Bosonen desselben Labels gilt

\[
BB^\dagger=2\sum_A b_A^\dagger b_A=2n_rI.
\]

Zuschauerorte und die übrigen Bosonlabels ändern diese Identität nicht. Weil n_r≤8, ist ‖B‖≤4. Die Norm eines selbstadjungierten Blocks [[0,B†],[B,0]] ist ‖B‖. Die Dreiecksungleichung über 40 Kanten liefert 160|t|.

H₀ hat einen Nullraum P und auf P⊥ Spektrum mindestens Δ. Schreibe v=‖V‖. Nach der Eigenwert-Störungsschranke liegen die ersten dim P Eigenwerte von H höchstens bei v, der nächste mindestens bei Δ−v. Die Trennung ist daher mindestens Δ−2v. Bei |t|/Δ=1/640 gilt v≤Δ/4 und somit die behauptete Schranke. ∎

Die Schätzung benutzt keine numerische Diagonalisierung eines riesigen Vielteilchenraums. Im Prüfer wird die bosonische Blockidentität zusätzlich in den ersten drei Besatzsektoren exakt rekonstruiert.

### Was dieser Satz kontrolliert

Er garantiert für den definierten endlichen Kandidaten einen von den Vermittleranregungen isolierten niedrigen Spektralraum. Auf diesem Raum kann eine exakte Spektralreduktion angesetzt werden. Der führende Austauschmaßstab beträgt J=2t²/Δ=Δ/204 800. Der Satz gibt noch keinen nützlichen relativen Restfehler gegenüber J, keine kleine globale Vierkörperkorrektur und keinen internen Grundzustandsgap des niedrigen Bands. Eine wachsende Familie muss ihre Norm-/Lokalitätskontrolle gesondert führen; die Konstante 160 gehört zum 40-Kanten-Graphen.

Für die frühere Wahl |t|/Δ=1/20 liefert dieselbe obere Schranke lediglich ‖V‖≤8Δ. Das reicht nicht für die Voraussetzung; eine grobe obere Schranke oberhalb Δ beweist aber auch nicht, dass die tatsächliche Norm oberhalb Δ liegt.

## C. Deterministische ideale Ω-Präparation

### Satz C1: Der Stern liefert den exakten Ω-Projektor

Auf vier Viererträgern sei

\[
H_\star=J\sum_{j=1}^3\frac{I+S_{0j}}2,\qquad M=2H_\star/J.
\]

Sein Spektrum mit Multiplizitäten lautet

\[
\operatorname{spec}M=\{0^{[1]},1^{[30]},2^{[45]},3^{[40]},4^{[15]},5^{[90]},6^{[35]}\}.
\]

Der Nullraum ist CΩ. Folglich

\[
\prod_{j=1}^6(jI-M)=720P_\Omega,
\quad
U_8=e^{-i\pi H_\star/(2J)}=e^{-2\pi iM/8},
\quad
\frac18\sum_{k=0}^7U_8^k=P_\Omega.
\]

**Beweis.** Die Nullraumbehauptung folgt aus dem verbundenen Graphsatz. Die Sternsumme ist die Summe einer Konstante und eines Jucys-Murphy-Elements; alternativ ist der hier verwendete endliche Operator direkt durch sechs zulässige positive Eigenwerte und seine Projektorpolynomidentität kontrollierbar. Der Prüfer multipliziert die sechs ganzzahligen 256×256-Matrizen und erhält genau 30 εεᵀ, wobei Ω=ε/√24 ist. Dies beweist die angegebene Projektoridentität unabhängig von numerischen Eigenvektoren. Die Spuren der sieben Lagrange-Spektralprojektoren werden ganzzahlig/rational berechnet und ergeben die vollständige Multiplizitätstabelle exakt; sie wird außerdem numerisch geprüft. Auf jedem Eigenwert m=1,…,6 verschwindet die geometrische Summe der achten Einheitswurzeln, auf m=0 ist sie acht. ∎

Die Aussage über den Filter benötigt die Multiplizitäten nicht; die exakte Operatorpolynomidentität und der eindeutige Nullraum reichen aus.

### Die selektive Ω-Phase ist konstruierbar

Definiere auf drei Kontrollqubits und dem System

\[
B=(H^{\otimes3}\otimes I)\Bigl[\sum_{k=0}^7|k\rangle\langle k|\otimes U_8^k\Bigr]
(H^{\otimes3}\otimes I).
\]

Hier bedeutet H in H⊗³ das Hadamard-Gatter, nicht einen Hamiltonoperator. Nach C1 gilt ⟨000|B|000⟩=PΩ. Für Ω selbst wirkt B auf |000⟩Ω als Identität. Für einen orthogonalen Systemzustand besitzt B|000⟩ψ keine Amplitude bei `000`.

Eine Phase z mit |z|=1 nur auf dem Kontrollzustand `000`, gefolgt von B†, realisiert daher

\[
B^\dagger\bigl[I+(z-1)|000\rangle\langle000|\otimes I\bigr]B\,
(|000\rangle\otimes\psi)
=|000\rangle\otimes R_\Omega(z)\psi,
\]

mit RΩ(z)=I+(z−1)PΩ. Der Kontrollspeicher wird genau zurückgesetzt. Eine vollständige Fouriertransformation auf dem Kontrollregister ist für diesen Nullraumtest nicht erforderlich.

SELECT(U₈ᵏ) besteht aus drei kontrollierten Potenzen U₈, U₈² und U₈⁴. Eine RΩ-Operation braucht daher sechs solche kontrollierten Potenzaufrufe einschließlich Rückrechnung. Eine Ressourcenbehauptung über ihre Synthese wird dadurch noch nicht geliefert.

### Satz C2: Zwei angepasste Schritte genügen exakt

Setze

\[
|\chi\rangle=\frac{|01\rangle-|10\rangle}{\sqrt2}\otimes
\frac{|23\rangle-|32\rangle}{\sqrt2},\qquad
s=1/\sqrt6,\quad c=\sqrt{5/6}.
\]

In einer geeigneten Phasenkonvention gilt |χ⟩=s|Ω⟩+c|β⟩ mit β⊥Ω. Sei

\[
R_\chi(z)=I+(z-1)|\chi\rangle\langle\chi|,
\quad R_\Omega(z)=I+(z-1)|\Omega\rangle\langle\Omega|.
\]

Für |z|=1 und Re z=(3√5−7)/2 bildet (RχRΩ)² den Zustand χ mit Wahrscheinlichkeit eins auf Ω ab.

**Beweis.** Der zweidimensionale Raum span{Ω,β} ist invariant. Darin ist

\[
v=\begin{pmatrix}s\\c\end{pmatrix},\quad
R_\chi=I+(z-1)vv^\top,\quad R_\Omega=\operatorname{diag}(z,1).
\]

Direkte Multiplikation ergibt für die unerwünschte β-Amplitude nach zwei Schritten

\[
\langle\beta|(R_\chi R_\Omega)^2|\chi\rangle
=\frac{c}{36}(z^4+14z^3+6z^2+14z+1).
\]

Mit u=Re z und z+z⁻¹=2u faktorisiert das Polynom zu

\[
z^4+14z^3+6z^2+14z+1=4z^2(u^2+7u+1).
\]

Die einzige Wurzel u in [−1,1] ist (−7+3√5)/2. Daher verschwindet die β-Amplitude exakt. Beide R sind unitär, also ist die verbleibende Ω-Amplitude vom Betrag eins. ∎

Numerisch ist φ=arg z≈1,7172169856477322. Der Prüfer bestätigt die Polynomidentität symbolisch und die ganze Wirkung zusätzlich auf den 256 ursprünglichen Komponenten, nicht nur auf dem reduzierten Zweiervektor. Die numerische Fidelity 1,0000000000000009 bedeutet Rundungsfehler in Größenordnung 10⁻¹⁵, keine Wahrscheinlichkeit oberhalb eins.

Rχ lässt sich aus einer bekannten Vorbereitung Aχ|0⁸⟩=χ durch Aχ, eine selektive Phase des Ursprungszustands und Aχ† realisieren. Die zwei Iterationen benötigen zwei Ω-Phasen und zwei χ-Phasen. Bei der obigen Realisierung sind das insgesamt zwölf kontrollierte U₈-Potenzaufrufe. Drei Kontrollqubits sind wiederverwendbar; Workspace für die konkrete Gatesynthese wird zusätzlich benötigt.

### Annahmen, Genauigkeit und Bedeutung

Das Verfahren benötigt kohärenten Zugriff auf kontrollierte Sternentwicklung und die besondere selektive Phase. Die Gleichgewichtsdynamik eines beliebigen festen Austauschgraphs stellt diese Kontrollen nicht von selbst bereit. Ohne diese Zusatzressource widerspricht C2 auch nicht der Erhaltung des Ω-Anteils unter reinem Austausch.

Werden die vier idealen Systemphasenoperationen jeweils durch unitäre Operatoren mit Normfehler höchstens ε ersetzt und ist χ exakt vorbereitet, liefert die Teleskopabschätzung einen Zustandsfehler höchstens 4ε. Damit ist die Zielwahrscheinlichkeit mindestens 1−16ε². Präparationsfehler oder Fehler der inneren kontrollierten Dynamik müssen in die Gesamtschranke aufgenommen werden. Diese bedingte Abschätzung ist keine Hardwaremessung und setzt keine kostenlose beliebige Präzision voraus.

Amplitudenverstärkung und angepasste Phasen sind etablierte Werkzeuge: [Brassard et al.](https://arxiv.org/abs/quant-ph/0005055), [Høyer](https://arxiv.org/abs/quant-ph/0006031). Der hier ausgeschriebene Beitrag ist die konkrete vollständige Ω-Spezialisierung und ihre transparente Ressourcengrenze.

## D. Die richtige lokale Symmetriefrage

### Satz D1: Lokale kontinuierliche Symmetrien des verbundenen Austauschmodells

Sei Γ ein verbundener einfacher Graph, Jᵢⱼ≠0 auf jeder Kante und

\[
H_2=\sum_{ij\in E}J_{ij}(I+S_{ij})/2.
\]

Für spurfreie hermitesche 4×4-Matrizen hᵢ sei X=Σᵢhᵢ, jeweils lokal eingebettet. Dann gilt

\[
[X,H_2]=0\quad\Longleftrightarrow\quad h_i=h_j\quad\text{für alle Orte}.
\]

**Beweis.** Jeder Kantenkommutator

\[
C_{ij}=[h_i\otimes I+I\otimes h_j,S_{ij}]
\]

hat partielle Spur null über jeden seiner beiden Orte. Deshalb sind Cᵢⱼ und Cₖₗ für verschiedene Kanten im Hilbert-Schmidt-Skalarprodukt orthogonal: An einem nur im ersten Paar enthaltenen Ort verschwindet bei der Spur das erste Element. Folglich kann die gewichtete Summe nur dann null sein, wenn jeder einzelne Kantenkommutator null ist.

Mit S(h⊗I)=(I⊗h)S folgt

\[
C_{ij}=\bigl[(h_i-h_j)\otimes I-I\otimes(h_i-h_j)\bigr]S.
\]

Verschwindet er, ist hᵢ−hⱼ skalar; wegen der Spurfreiheit ist die Differenz null. Verbundenheit propagiert die Gleichheit auf alle Orte. Die Rückrichtung folgt aus der Vertauschungsinvarianz kollektiver Transformationen. ∎

Beim Clebsch-Graphen hat die gerichtete Inzidenzmatrix Rang 15. Für jede der 15 inneren spurfreien Richtungen entstehen 15 unabhängige Gleichheitsbedingungen, also 225 Bedingungen auf 240 Parameter. Der verbleibende Raum ist die kollektive su(4) mit Dimension 15. Der Prüfer kontrolliert Inzidenzrang, den Rang der lokalen Kommutatorabbildung und die partiellen Spuren exakt.

### Warum dies keine Bestimmung der vollen Kommutante ist

Für jede hermitesche Matrix H mit Eigenräumen Eλ gilt

\[
\{X:[X,H]=0\}\cong\bigoplus_\lambda\operatorname{End}(E_\lambda).
\]

Die ganze Algebra enthält viel mehr als die lokal interpretierbaren inneren Symmetrien. Sie ist deshalb nicht der richtige Test für die Erwartung „nur SU(4) × W(D₅)“. Ortspermutationen bilden eine zweite, diskrete Frage. Eine vollständige H₂+H₄-Rechnung muss die Symmetrie des Gesamtoperators bestimmen; zufällige Kompensation bei einem einzelnen Kopplungswert wird durch den Satz nicht ausgeschlossen. Für eine Symmetrie, die in einer analytischen Kopplungsfamilie identisch gilt, muss allerdings jeder Koeffizient der Familie mit dem Generator kommutieren.

## E. Präziser RH-Vertrag und singuläre Verklebung

### Definition der Zielgröße

Für g∈C_c^∞(0,∞) sei G(s)=∫₀∞g(x)xˢ⁻¹dx. Setze

\[
Q_\zeta(g)=\sum_\rho G(\rho)\overline{G(1-\bar\rho)}.
\]

Die Summe verwendet die nichttrivialen Nullstellen mit Multiplizität. Bei glatten kompakt getragenen Tests erlaubt die schnelle vertikale Abnahme der Mellin-Transformierten die übliche konvergente Auswertung. Für f(x)=∫₀∞g(xy)\overline{g(y)}dy gilt

\[
\widetilde f(s)=G(s)\overline{G(1-\bar s)}.
\]

In der entsprechenden Normierung der expliziten Formel

\[
\widetilde f(0)-\sum_\rho\widetilde f(\rho)+\widetilde f(1)
=\sum_vW_v(f)
\]

ist daher

\[
Q_\zeta(g)=G(0)\overline{G(1)}+G(1)\overline{G(0)}-\sum_vW_v(f).
\]

Für G(0)=G(1)=0 entfallen die Randterme. Eine andere Mellin-/Fourierkonvention muss sämtliche Terme gemeinsam transformieren. Den klassischen Weil-Rahmen und die beschränkte archimedische Untersuchung erläutert [Connes–Consani](https://arxiv.org/abs/2006.13771). Diese Arbeit wird nicht als allgemeiner RH-Beweis benutzt.

### Satz E1: Singuläre Schur-Verklebung

Für einen endlichen hermiteschen Blockoperator

\[
M=\begin{pmatrix}A&B\\B^\dagger&C\end{pmatrix}
\]

gilt M≥0 genau dann, wenn

\[
A\ge0,\qquad\operatorname{ran}B\subseteq\operatorname{ran}A,
\qquad C-B^\dagger A^+B\ge0,
\]

wobei A⁺ die Moore-Penrose-Inverse ist.

**Beweis.** Aus M≥0 folgt A≥0. Für x∈ker A muss x†By=0 für jedes y gelten: Andernfalls besitzt die quadratische Form auf (λx,y) für eine passende Phase und hinreichend großes |λ| einen negativen Wert. Somit B†ker A=0 und im endlichen Raum ran B⊂ran A.

Unter dieser Bedingung gilt durch quadratische Ergänzung

\[
\begin{aligned}
\binom{x}{y}^\dagger M\binom{x}{y}
&=\|A^{1/2}x+A^{+1/2}By\|^2\\
&\quad+y^\dagger(C-B^\dagger A^+B)y.
\end{aligned}
\]

Die rechte Seite beweist Hinlänglichkeit. Für Notwendigkeit wähle x=−A⁺By; dann bleibt genau die Restform. ∎

**Gegenkontrolle.** Bei A=diag(1,0), B=(0,1)ᵀ und C=(2) ist C−B†A⁺B=(2)>0. Trotzdem hat M die Determinante −1 und ist nicht positiv, weil die Bildraumbedingung verletzt ist. Gerade bei Quotienten mit großen Nullräumen darf diese Voraussetzung nicht fehlen.

### Satz E2: Dichte Fortsetzung kompatibler positiver Blöcke

Sei D ein topologischer Testraum, Q eine stetige hermitesche quadratische Form darauf und D₁⊂D₂⊂… eine Familie endlicher Unterräume, deren Vereinigung dicht ist. Wenn Q auf jedem Dₙ positiv semidefinit ist, ist Q auf D positiv semidefinit.

**Beweis.** Für jedes g∈D und eine gegen g konvergierende Folge gₖ aus der Vereinigung gilt Q(g)=limₖQ(gₖ)≥0. Im üblichen glatten Testraum kann die Approximation auf kompakten Trägern und in allen erforderlichen Ableitungsseminormen organisiert werden. ∎

Es wird kein gleichmäßiger strikt positiver kleinster Eigenwert verlangt. Die Aussage benötigt aber die wirkliche Q auf jeder Stufe, die gemischten Einträge zwischen den Stufen, die richtige Topologie und einen Beweis für sämtliche Stufen. Eine endliche Liste positiver Matrizen erfüllt den Satz nicht.

### Anwendung als notwendiger Forschungsplan, nicht als RH-Beweis

Ein Universalraum-Vorschlag müsste entweder Qζ(g)=‖Ag‖² für alle vorgeschriebenen Tests exakt herleiten oder E2 samt den arithmetischen Identitäten und sämtlichen Schur-Bedingungen durchführen. Wird A erst als Quadratwurzel einer als positiv angenommenen Qζ definiert, ist die entscheidende Behauptung bereits vorausgesetzt.

Ebenso repariert eine zusätzliche orthogonale Geschichte keine negative ursprüngliche Form. Sie kann die gemischten Einträge verändern und damit eine andere positive Form erzeugen. Das einfache Beispiel [[1,2],[2,1]] hat positive Diagonalblöcke und Eigenwerte 3,−1; das Weglassen der Nebendiagonalen macht daraus I₂. Die Änderung ist keine Positivitätsherleitung für das Ausgangsobjekt.

Die früheren Katalogfehler r404 (**RESTATEMENT**), r613 (**WORLD_BLIND**) und r640 (**NO_BRIDGE**) bleiben einschlägig für solche bloßen Umdefinitionen. Die neue Ergänzung behauptet keine Wiederbelebung dieser Routen: Sie gibt die fehlende Bildraum- und Kohärenzbedingung ausdrücklich an und lässt ihre Erfüllung für die vollständige Weil-Form offen.

## F. E8-Fourier-Auslesung und Faktorrückgewinnung

### Satz F1: Die vollständige Ausgabeverteilung des quadratischen Zustands

Sei G eine symmetrische ganzzahlige Matrix mit gerader Diagonale und det G=±1. Setze q(x)=xᵀGx/2 auf (Z/N)ʳ. Die in diesem Audit verwendete E8-Matrix hat r=8 und det G=1. Für

\[
|\psi_t\rangle=N^{-r/2}\sum_xe^{2\pi itq(x)/N}|x\rangle
\]

und die normierte Fouriertransformation mit Exponent −2πib·x/N ist die Amplitude

\[
\widehat\psi_t(b)=N^{-r}\sum_xe^{2\pi i(tq(x)-b\cdot x)/N}.
\]

Mit d=ggT(t,N) gilt

\[
|\widehat\psi_t(b)|^2=(d/N)^r\,\mathbf1_{d\mid b_1,\ldots,b_r}.
\]

**Beweis.** Bezeichne die unnormierte Summe mit S(b). Schreibe im Betragsquadrat x=y+h. Wegen q(y+h)−q(y)=q(h)+yᵀGh folgt

\[
|S(b)|^2=
\sum_h e^{2\pi i(tq(h)-b\cdot h)/N}
\sum_y e^{2\pi it y^\top Gh/N}.
\]

Die innere Summe ist Nʳ genau dann, wenn tGh=0 modulo N, sonst null. Da G modulo N invertierbar ist, bedeutet dies th=0 modulo N. Schreibe N=dM und t=da mit ggT(a,M)=1. Dann sind genau h=Mz mit z∈(Z/d)ʳ erlaubt.

Für diese h gilt tq(h)=daM²q(z)=NaMq(z), also verschwindet die quadratische Phase modulo N. Übrig bleibt

\[
|S(b)|^2=N^r\sum_{z\in(\mathbb Z/d)^r}e^{-2\pi ib\cdot z/d}
=N^rd^r\mathbf1_{d\mid b}.
\]

Nach Division durch N²ʳ folgt die Aussage. Die Integrität von q ist der Grund, weshalb der Beweis auch bei geradem N funktioniert. ∎

Insbesondere beträgt die Zahl der unterstützten Ausgaben (N/d)⁸ und ihre gemeinsame Wahrscheinlichkeit (d/N)⁸. Die Gesamtwahrscheinlichkeit ist eins. Bei t=0 gilt d=N und nur b=0 tritt auf; auch dieser Grenzfall ist enthalten.

Die E8-Matrix des Prüfers ist 2I minus die Adjazenz des Dynkinbaums mit den Kanten (0,1), (0,2), (2,3), (0,4), (4,5), (5,6), (6,7). Ihre Positivität und Determinante werden exakt kontrolliert. Der allgemeine Beweis braucht nur die angegebenen Eigenschaften, nicht die spezielle Bezeichnung E8.

### Reichweite des Negativresultats

Für den bekannten Takt t kann ggT(t,N) direkt berechnet werden. Satz F1 zeigt, dass genau diese abschließende Fourier-Messung keine zusätzliche Verteilungsinformation über die Faktoren enthält. Er sagt nicht, dass der volle phasentragende Zustand für jede weitere Quantenoperation nutzlos wäre. Ein Vorschlag mit weiteren Operationen muss deren Wirkung und Kosten als neues Protokoll herleiten.

Die im Katalog r647 geprüfte stärkere Phasenidentität S_N(t)=N⁴ggT(t,N)⁴ wird hier an allen Takten für N=2,3,4,5 unabhängig exakt bestätigt. Satz F1 benötigt ihre besondere positive Phase nicht und wird direkt bewiesen. Daher wird die endliche Kontrolle der Gaußphase nicht zu einem neuen allgemeinen Phasenbeweis ausgeweitet.

### Satz F2: Exakte Rückgewinnung aus dem vierten ggT-Moment bei Semiprimen

Sei N=pq mit verschiedenen Primzahlen. Setze

\[
M_4(N)=\sum_{t=0}^{N-1}\gcd(t,N)^4,\qquad s=p+q.
\]

Dann gilt

\[
\begin{aligned}
M_4(N)= {}&N^4-s^4+Ns^3+4Ns^2-3N^2s\\
&-2N^2+N-s+1.
\end{aligned}
\]

Aus dem exakten M₄ kann man s als geeignete ganzzahlige Wurzel dieser Quartik gewinnen und anschließend

\[
p,q=\frac{s\mp\sqrt{s^2-4N}}2
\]

bestimmen, wobei ganzzahlige, nichttriviale Kandidaten durch Multiplikation geprüft werden.

**Beweis.** Es gibt (p−1)(q−1) teilerfremde Takte, q−1 Takte mit ggT=p, p−1 mit ggT=q und den Takt null mit ggT=N. Deshalb

\[
M_4=(p-1)(q-1)+(q-1)p^4+(p-1)q^4+N^4.
\]

Ersetze p+q durch s, pq durch N, p³+q³ durch s³−3Ns und p⁴+q⁴ durch s⁴−4Ns²+2N². Das ergibt die Quartik. Jede erhaltene positive ganzzahlige Lösung mit passender Quadratik und Produkt N liefert die Faktoren; aufgrund der Semiprimvoraussetzung ist das ungeordnete nichttriviale Faktorpaar eindeutig. ∎

Der Prüfer berechnet M₄ für N=15,35,143,899,10 403 durch eine Summe über t mit ausschließlich N als Eingang. Die erwarteten p und q werden erst zur abschließenden Kontrolle benutzt. Alle fünf Paare werden zurückgewonnen. Der Arbeitsaufwand zur Momentgewinnung beträgt N ggT-Berechnungen und ist deshalb exponentiell in log N. Die nachgeschaltete algebraische Inversion beseitigt diesen Aufwand nicht.

Für zufällige Takte beträgt die Wahrscheinlichkeit eines echten ggT (p+q−2)/N. Bei ausgeglichenen Faktoren braucht direkte Stichprobensuche von Größenordnung √N Versuche. Selbst eine ideale unstrukturierte Amplitudenverstärkung dieses Prädikats wäre von Größenordnung N¹/⁴. Diese Aussage ist auf dieses Suchprädikat beschränkt und widerspricht nicht [Shors polynomieller Periodenroute](https://arxiv.org/abs/quant-ph/9508027).

## G. Prüfprotokoll und genaue Evidenzklasse

Die Datei `verify_construct.py` baut ihre Matrizen unabhängig von Original-Forschungscode auf. Sie enthält explizite Fehlerabfragen, keine für die Akzeptanz entscheidenden wegoptimierbaren Assertions.

| Bereich | Art der Kontrolle |
|---|---|
| A | exakte Gram-Matrizen, Rang 6/12, dunkler Zustand, SU(4)-Gegentest, unitäre 22×22-Matrix |
| B | exakte bosonische Umwandlungsblöcke in drei Sektoren; exakte globale Referenzschranken |
| C | ganzzahlige 256×256-Projektorpolynome; exakte Phase und Fehlerpolynom; volle numerische 256-Komponenten-Wirkung |
| D | Clebsch-Inzidenzrang, starke Regularität und 15-dimensionaler lokaler Kommutatorrang |
| E | positive und negative Kontrollmatrizen, einschließlich verletzter Bildraumbedingung |
| F | E8-Grammatrix; exakte endliche Gaußphasen; fünf volle Fourierverteilungen; Quartikidentität und fünf faktorblinde Momentdurchläufe |
| Übernommener Zweizellensatz | symbolische Gap-Identität und numerische Formelwerte; kein erneuter vollständiger all-sector-Beweis im Prüfer |

Der letzte Stand besitzt **85 bestandene Bedingungen: 77 exakt und 8 numerisch**. Eine Aufspaltung in viele benannte Bedingungen macht die Aussagen nicht unabhängig. Insbesondere stehen hinter den allgemeinen Sätzen die ausgeschriebenen Beweise und Voraussetzungen; endlich viele Tests ersetzen deren Quantoren nicht.

Reproduktion mit Python, NumPy und SymPy:

```text
python3 verify_construct.py --output verification.json
python3 -OO verify_construct.py --output verification_optimized.json
```

Die beiden Ergebnisdateien wurden nach dem letzten Prüfstand auf Bytegleichheit verglichen. Verwendete Versionen und die Prüfsumme des Prüfers stehen im Ergebnis. Es wurden weder eine Quantenhardware noch ein neuer Lean-Adapter oder die vollständige RH-Suite ausgeführt. Der Forschungsindex besitzt die im Quellenmanifest dokumentierten Aktualitätslücken; ein grüner lokaler Identitätstest ersetzt diese Prüfung nicht.
