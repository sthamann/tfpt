# Unabhängiger Review: gemeinsamer Spin(10)-SU(4)-Lift bei ungeradem \(c_1\)

## Ergebnis und genaue Reichweite

Die vorgeschlagene Verklebung ist **als gemeinsamer \(K\)-Lift und als globaler \((\mathbf{16},\mathbf4)\)-Träger exakt konsistent**. Sie repariert nicht den fehlenden separaten Spin(10)-Lift: Weder der Spinanteil noch der Familienanteil ist bei ungeradem Determinantenumlauf einzeln global definiert. Erst das Paar ist in
\[
K=(\operatorname{Spin}(10)\times SU(4))/\langle(z,i^{-1}I_4)\rangle
\]
eindeutig. Dabei sei die Halbspinorkonvention so gewählt, dass \(z\) auf der verwendeten \(\mathbf{16}=\Lambda^{\mathrm{even}}\mathbb C^5\) als \(i\) wirkt. Die Konstruktion beweist weder eine physische Identifikation der vier Familien noch eine räumliche oder zeitliche Quelle.

## 1. Abstieg in den Quotienten

Setze \(\delta=\det g\). Auf der universellen Überlagerung von \(U(5)\) wirken
\[
s(g)|_{\mathbf{16}}=\delta^{-1/2}\Lambda^{\mathrm{even}}g,
\qquad
A_m(g)=\operatorname{diag}\bigl(\delta^{m_1+1/2},\ldots,
\delta^{m_4+1/2}\bigr).
\]
Aus \(\sum_jm_j=-2\) folgt
\[
\det A_m=\delta^{\sum_jm_j+2}=1.
\]
Ein Wechsel des Zweigs von \(\delta^{1/2}\) multipliziert beide Faktoren mit \(-1\). Das gemeinsame Element ist
\[
(-1,-I_4)=(z,i^{-1}I_4)^2,
\]
also ein Element des herausgeteilten \(\mathbb Z_4\)-Kerns. Deshalb steigt das Paar zu einem wohldefinierten Homomorphismus \(\iota_m:U(5)\to K\) ab. Wichtig: \(s\) und \(A_m\) sind in dieser Schreibweise einzeln keine globalen Homomorphismen auf \(U(5)\).

Auf dem Tensorprodukt heben sich die Halbpotenzen auf. Der zugehörige globale komplexe Rang-64-Träger ist daher
\[
W_m=\Lambda^{\mathrm{even}}E\otimes
\bigoplus_{j=1}^4D^{m_j},\qquad D=\det E.
\]
Das ist die konstruktive Reparatur der ungeraden \(c_1(E)\)-Obstruktion für den gemeinsamen Träger.

## 2. Topologische Klasse, Ladungen und Eindeutigkeit

Für Rang fünf gilt mit den Chernwurzeln von \(E\)
\[
c_1(\Lambda^{\mathrm{even}}E)
=c_1(\Lambda^2E)+c_1(\Lambda^4E)=4c_1(E)+4c_1(E)=8c_1(E).
\]
Somit
\[
c_1(W_m)=\sum_j(8+16m_j)c_1(E)
=(32+16\sum_jm_j)c_1(E)=0.
\]
Auf \(S(U(3)\times U(2))\subset SU(5)\) ist \(\delta=1\). Die Determinantentwists verändern daher die üblichen lokalen SU(5)- beziehungsweise SM-Hyperladungen nicht.

Eine erzeugende Schleife von \(\pi_1(U(5))\) hat Determinantengrad eins. Ihre gehobenen Endpunkte sind unabhängig von \(m\)
\[
s(2\pi)=-1=z^2,\qquad A_m(2\pi)=-I_4=i^2I_4.
\]
Sie geht deshalb auf \((z,i^{-1}I_4)^2\), also auf **Klasse \(2\)** in
\(\pi_1(K)=\mathbb Z_4\), nicht auf einen Generator. Für \(c_1(E)=1\) liefern alle \(m\) damit topologisch dieselbe \(K\)-Hauptfaserung über \(S^2\). Die Homomorphismen und die aus einer festen \(U(5)\)-Verbindung induzierten Verbindungen sind dennoch verschieden: Ihre Gewichtslisten in der Determinantenrichtung stimmen nicht überein. Gleiche \(\pi_1(K)\)-Klasse bedeutet hier keine kanonische Eichäquivalenz der induzierten Verbindungen.

Schreibe \(x_j=m_j+\tfrac12\). Dann \(x_j\in\mathbb Z+\tfrac12\) und \(\sum_jx_j=0\). Daher
\[
\sum_jx_j^2\ge4(1/2)^2=1.
\]
Gleichheit verlangt zwei \(+1/2\) und zwei \(-1/2\), also genau
\(m=(0,0,-1,-1)\) bis auf Permutation. Für \(m=(0,0,0,-2)\) ist die Norm \(3\). Das Minimum ist eine zusätzliche Auswahlregel; Quotient, Topologie und unveränderte SM-Ladungen wählen es nicht aus.

## 3. Exaktes Splitting auf \(\mathbb{CP}^1\) und Dirac-Kerne

Für \(E=\mathcal O^4\oplus\mathcal O(1)\) ist \(D=\mathcal O(1)\) und
\[
\Lambda^{\mathrm{even}}E
=\Lambda^0E\oplus\Lambda^2E\oplus\Lambda^4E
=\mathcal O^8\oplus\mathcal O(1)^8.
\]
Damit erhält man exakt
\[
\begin{aligned}
m_A=(0,0,-1,-1):\quad
W_A&=\mathcal O(-1)^{16}\oplus\mathcal O^{32}
\oplus\mathcal O(1)^{16},\\
m_B=(0,0,0,-2):\quad
W_B&=\mathcal O(-2)^8\oplus\mathcal O(-1)^8
\oplus\mathcal O^{24}\oplus\mathcal O(1)^{24}.
\end{aligned}
\]
Beide haben Rang 64 und \(c_1=0\), aber verschiedene holomorphe Splittingtypen.

Mit der räumlichen Spinstruktur \(S^+=\mathcal O(-1)\) gilt für einen Summanden \(\mathcal O(k)\)
\[
\dim_{\mathbb C}\ker D^+=\max(k,0),\qquad
\dim_{\mathbb C}\ker D^-=\max(-k,0).
\]
Folglich besitzt \(W_A\) \(16+16=32\) und \(W_B\) \(24+24=48\) komplexe Dirac-Nullmoden; in beiden Fällen ist der Index null. Eine Umkehr der Orientierung oder der Benennung von \(S^\pm\) vertauscht nur die beiden Chiralitätszahlen. Die Rechnung liefert keine Majorana-Reduktion und keine physische Nullmodenbesetzung.

## Konventionsgrenze

Die Aussage über den Quotientengenerator benutzt ausdrücklich die Konvention, dass \(z\) auf der gewählten \(\mathbf{16}\) als \(i\) wirkt. Bei Wahl der konjugierten Halbspinordarstellung muss \(z\) durch \(z^{-1}\) und der diagonale Quotient entsprechend ersetzt werden. Das Quadrat bleibt \((-1,-I_4)\); die Klasse \(2\), die Chernklassen und die Nullmodenzahlen sind daher konventionsstabil.
