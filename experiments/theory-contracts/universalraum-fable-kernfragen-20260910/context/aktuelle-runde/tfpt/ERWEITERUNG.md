# Die erste dynamische Erweiterung des physischen Wilson-Caps

10. September 2026. Konstruktive Fortsetzung von `WILSON-CAP-BEWEIS.md`, ohne Änderung des dortigen Parents, Codes oder der Quellenpins. Alle Aussagen betreffen den unveränderten endlichen U(1)-Rotor/CAR-Torus, L≥5, N=L³, ohne elektrischen Cutoff.

**Ergebnis:** Die erste ausgetretene Richtung wird ein kanonischer neuer Isometrieblock. Seine Kopplung und sein vollständiger komprimierter Hamiltonblock sind exakt berechnet. Danach erzwingt derselbe Parent zwei explizite zusätzliche physische Kanäle: onsite High-/Low-Austausch und zwei High-Teilchen mit zwei Low-Löchern. Die Reparatur erhält damit tatsächlich neue Prozessrichtungen, anstatt den Austritt wegzuprojezieren.

## 1. Aus der Leakage wird ein definierter neuer Raum

J=J₁₂ ist der bisherige 16-dimensionale Zwei-Plaquetten-Code. Setze Q=A_U, a=1/12, b=1/24, c=βa²=1/576, κ=1/100 und
\[
T=d^*Ql,\qquad
g=\sqrt{6Nb^2}=\sqrt{N/96},\qquad
h_0=J^*HJ=\epsilon_LNI+E_C,
\]
\[
E_C=2\kappa\,\operatorname{diag}_{r,s=0}^3(r^2+s^2),
\qquad \Gamma=(I-JJ^*)HJ=bTJ.
\]
Der vorige vollständige Quellenbeweis gab \(\Gamma^*\Gamma=g^2I\). Deshalb ist
\[
\boxed{\eta=\Gamma/g=(b/g)TJ}
\]
eine explizite Isometrie, J*η=0. Jeder ihrer Vektoren ist eine bezeichnete kohärente Summe der echten gerichteten Low–High-Hops. Der vergrößerte Raum
\[
V_1=(J,\eta):\mathbb C^{16}\oplus\mathbb C^{16}\to\mathcal H_{\rm phys}
\]
ist isometrisch, und
\[
\boxed{V_1^*HV_1=
\begin{pmatrix}h_0&gI\\gI&h_1\end{pmatrix},\qquad h_1=\eta^*H\eta.}
\]
Der Kopplungsblock √(N/96)I folgt vollständig aus den ursprünglichen b-Hops und deren orthogonalen Fockausgängen. Er ist kein neuer Parameter. Auch die Anfangspräparation wird nicht geändert: Ein ursprünglicher Codevektor ψ wird jetzt als (ψ,0) dargestellt.

## 2. Auch h₁ lässt sich vollständig ausschreiben

Sei F der offene Shift auf den vier Fluxwerten 0,1,2,3: F|r⟩=|r+1⟩ für r≤2 und F|3⟩=0. Definiere
\[
K=(F+F^*)\otimes I+I\otimes(F+F^*).
\]
Hier steht der tatsächliche komprimierte Wilsonloop, **kein zyklisch zurückgesetzter Ersatzshift**. Die vierte Potenz der vollen kubischen Adjazenz hat die exakte Ortsmatrixspur
\[
\operatorname{Tr}Q^4=66NI+4\sum_{\square}(W_\square+W_\square^*).
\]
Begründung: Die 90 geschlossenen Viererschrittwege pro Ort zerfallen in 66 Wege mit vollständig zurückgenommenem Flux und die orientierten Plaquettenwege. Jede Plaquette wird je Orientierung von vier Startpunkten gezählt. L≥5 verhindert zusätzliche kurze Torusumlaufwege. Ferner ist Tr Q³=0 und Tr Q²=6NI. Bei der Kompression in J bleiben von den nichttrivialen Plaquetten genau die zwei gespeicherten Loops übrig:
\[
J^*(\operatorname{Tr}Q^4)J=66NI+4K.
\]

Ein One-Pair-Zustand hat eine High-Besetzung und ein Low-Loch. Für h_L=aQ+cQ² gilt auf der All-Low-Quelle
\[
H_{LL}TJ=T(\operatorname{Tr}h_L)J-d^*Qh_LlJ.
\]
Die negative zweite Komponente ist die exakte CAR-Lochbewegung. Zusammen mit Tr Q³=0 liefert sie die normierte Korrektur −c(66NI+4K)/(6N). Der elektrische Anteil gibt E_C+κ/2: Für jedes Link treten beide gerichteten Fluxverschiebungen auf, sodass ihre linearen E-Terme sich in der Paarung aufheben. Die High-Onsite-Energie ist 4; das LH-Hopping ändert die High-Zahl und trägt nichts zur One-Pair-Kompression bei. Folglich
\[
\boxed{h_1=h_0+(4+\kappa/2-11c)I-\frac{2c}{3N}K.}
\]
Für den konkret geprüften N=125-Torus lautet dies
\[
h_1=h_0+\frac{57397}{14400}I-\frac1{108000}K,
\qquad g^2=125/96.
\]
Die Rechnung verwendet ausschließlich ursprüngliche elektrische Energie, CAR und ein-/zweischrittige Low-Hops. Eine Diagonalisierung operatorwertiger Links oder eine kanonische Fock-Rotation wird nicht vorausgesetzt.

## 3. Ein erster weiterer Kanal: onsite Austausch

Der Rest der neuen Spalte ist
\[
R=(I-V_1V_1^*)H\eta.
\]
Er ist nicht null. Ein besonders einfacher tatsächlicher Teilkanal ist
\[
Z_0=\frac1{\sqrt N}\sum_x d_x^*l_xJ.
\]
Diese Abbildung ist isometrisch: Die verschiedenen x tragen orthogonale Fockmuster. Sie ist orthogonal zu J und η, denn das High-Teilchen und das Low-Loch liegen jetzt am gleichen Ort. Alle Zustände sind Gauss-neutral; ihr Flux bleibt unverändert.

Die sechs Low–Low-Nächste-Nachbar-Rückwege schließen den ersten LH-Hop. Wegen des CAR-Lochvorzeichens liefern sie
\[
\boxed{Z_0^*H\eta=-\frac{6ab\sqrt N}{g}I
=-a\sqrt6I=-\frac1{\sqrt{24}}I.}
\]
Kein anderer ursprünglicher Term kann diesen Eintrag kompensieren: Elektrische/Onsite-Terme ändern das Fockmuster nicht, LH-Terme ändern die High-Zahl und die LL-Zweischrittkomponente bräuchte einen nicht vorhandenen geschlossenen Dreischrittweg. Das Minuszeichen wurde zusätzlich mit den tatsächlichen CAR-Operationen kontrolliert.

## 4. Ein zweiter weiterer Kanal: zwei echte Paare

Sei P₂ die physische Projektion auf genau zwei High-Teilchen. In diesem neutralen Sektor gibt es ebenfalls zwei Low-Löcher. Exakt
\[
R_2=P_2H\eta=\frac{b^2}{g}T^2J.
\]
Die beiden disjunkten LH-Monomiale sind gerade und kommutieren. Ihre zwei zeitlichen Reihenfolgen addieren sich. Es handelt sich um reale zusätzliche CAR-Zustände, nicht um zwei alternative Schreibweisen desselben One-Pair-Vektors.

Auf der gefüllten Low-/leeren High-Quelle ergibt die CAR-Expansion in Zweierminoren von Q
\[
J^*T^{*2}T^2J
=2J^*\big[(\operatorname{Tr}Q^2)^2-\operatorname{Tr}Q^4\big]J.
\]
Dies ist die Cauchy–Binet-Identität für die kommutierenden Rotor-Koeffizienten, direkt aus den Zweifermionen-Amplituden; keine quantisierte Linkdiagonalisierung. Daher
\[
\boxed{G_2:=R_2^*R_2
=b^2\left[(12N-22)I-\frac4{3N}K\right].}
\]
Da ∥K∥≤4, ist G₂ für jedes hier zugelassene N≥125 strikt positiv. Die nächste **kanalweise** Isometrie und ihre Kopplung sind damit explizit:
\[
\eta_2=R_2G_2^{-1/2},\qquad
\eta_2^*\eta_2=I,\qquad
\eta_2^*H\eta=G_2^{1/2}.
\]
Für N=125 ist
\[
G_2=\frac{739}{288}I-\frac1{54000}K.
\]
Die Wurzel ist eindeutige positive endliche Funktionalkalkulation. Die ursprünglichen materiellen und Wilson-Operationen bestimmen die gesamte Matrix.

Somit ist bereits \((J,\eta,Z_0,\eta_2)\) eine konkrete 64-dimensionale Isometrie. Die beiden neuen Kanäle liegen in orthogonalen physischen Bereichen. Als reine H-Krylov-Konstruktion könnte man stattdessen die gesamte Restspalte R durch \(R(R^*R)^{-1/2}\) zu einem einzigen neuen 16-dimensionalen Block bündeln. Das ist etwas anderes als die hier markiert erhaltenen onsite-/Zwei-Paar-Kanäle. Weitere One-Pair-Richtungen können in R vorhanden sein; ein Abschluss nach dieser Erweiterung wird nicht behauptet.

## 5. Welche Antworten sind jetzt tatsächlich repariert?

Mit \(\widehat H_1=V_1^*HV_1\) stimmen die komprimierten Momente vom ursprünglichen Code für Potenzen 0,1,2,3 exakt mit dem vollen Parent überein. Denn HJ liegt vollständig in ran V₁. Bei der vierten Potenz tritt die erste fehlende Antwort auf:
\[
\boxed{J^*H^4J-E_0^*\widehat H_1^4E_0=g^2R^*R,
\quad E_0\psi=(\psi,0).}
\]
Aus den zwei orthogonalen neuen Kanälen folgt bereits
\[
R^*R\ge\frac1{24}I+G_2>0.
\]
Der erste Block ist somit eine genaue Reparatur der ersten drei Momente und ein nachweislich unzureichender Ersatz für die ganze Geschichte. Der nächste notwendige Beitrag ist quantitativ benannt.

Alternativ bleibt die vollständige Antwort durch eine Feshbach-Selbstenergie erhalten. Für Im z≠0 und \(H_R=(I-V_1V_1^*)H(I-V_1V_1^*)\) auf dem reduzierten Definitionsbereich gilt
\[
J^*(z-H)^{-1}J
=\left[z-h_0-g^2\left(z-h_1-
R^*(z-H_R)^{-1}R\right)^{-1}\right]^{-1}.
\]
Die endlichen Projektionsbereiche liegen im Definitionsbereich von H; die aus ihnen herausführenden Blöcke sind beschränkt. Die Kompression des selbstadjungierten H auf das orthogonale Komplement ist dadurch wohldefiniert und selbstadjungiert. Diese Formel verliert keine Antworten, spart aber nicht automatisch die Berechnung des Rests.

## 6. Prüfung und Herkunft

`check_extension.py` besteht **11 exakte Kontrollen**. Eine neue unabhängige Zählung des vollständigen L=5-Torus findet 11.250 geschlossene Viererschrittwege: 8.250 mit trivialem Flux und die übrigen tatsächlichen Plaquettenbeiträge. Sie bestätigt die ganze komprimierte Tr-Q⁴-Matrix, h₁, G₂ und dessen strikte Positivität. Kleine direkte CAR-Rechnungen prüfen das Minuszeichen des Lochrückwegs und die Addition zweier disjunkter LH-Reihenfolgen. Es wird weder ein vorheriger Prüfer importiert noch eine alte Ergebnisdatei verändert.

Die endlichen Kontrollen stützen die ausgeschriebenen allgemeinen Beweise. Alle neuen Blöcke bestehen aus tatsächlichen ursprünglichen Feldoperationen. Die Wahl des ursprünglichen Codes und seiner Präparation bleibt dieselbe wie im Wilson-Cap-Beweis; eine Vakuumauswahl, ein endlicher Gesamtdynamikabschluss oder eine neue fundamentale Kopplungsauswahl folgt daraus nicht. Neue Quellen-/Artefaktpins stehen separat in `erweiterung-quellenmanifest.json`.
