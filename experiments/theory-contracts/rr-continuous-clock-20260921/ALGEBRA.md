# Kontinuierlicher RR-Generator am nativen W

**Verdict:** `EXACT_CONDITIONAL_FINITE_CERTIFICATE` — der gepinnte endliche Tensor
trägt die kontinuierliche \(\mathfrak{gl}_5\oplus\mathfrak{gl}_4\)-Wirkung exakt.
Der daraus gebildete selbstadjungierte Generator \(K\) ist eine Erhaltungsgröße des
nativen Paar-Boson-Hamiltonoperators. Das Zertifikat identifiziert \(K\) nicht mit
der physischen Zeitentwicklung und behauptet keinen lokalen Feld-, Kontinuums- oder
4D-Abschluss.

## 1. Gepinnter endlicher Gegenstand

Verwendet wurde ausschließlich

`outputs/TFPT_RR_Quellenbruecke/native_tensor.npz`

mit SHA-256

`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

Der geladene Tensor ist

\[
W:\Lambda^2\mathbb C^{64}\longrightarrow\mathbb C^{60},
\qquad W\in\{0,\pm1\}^{60\times2016},
\]

hat 480 von null verschiedene Koeffizienten und erfüllt exakt
\(WW^\dagger=8I_{60}\). Die Spinbasis wird durch die 16 gepinnten geraden
Bitmasken des Archivs festgelegt. Die Reihenfolge ist

\[
\mathbb C^{64}=\Lambda^{\rm even}\mathbb C^5\otimes\mathbb C^4,
\qquad
\mathbb C^{60}=(\mathbb C^5\oplus\mathbb C^{5*})\otimes\Lambda^2\mathbb C^4.
\]

Dies baut auf `ARCH.RRCAR.01` und `ARCH.RRCAR.02` auf. Deren endliche
Riemann–Roch-/Clifford-Aussagen bleiben von der physischen Carrier-Identifikation
getrennt.

## 2. Vollständiger Lie-Algebra-Test

Für \(h\in\mathfrak{gl}_5\) setze

\[
A(h)=d\Gamma_{\rm even}(h)\otimes I_4,
\]

\[
B(h)=\bigl[\operatorname{tr}(h)I_{10}
 +\operatorname{diag}(h,-h^T)\bigr]\otimes I_6.
\]

Der Spurterm ist die Ableitung der bereits im endlichen RR-Test vorhandenen
Determinantenlinie
\(\det(g)\operatorname{diag}(g,g^{-T})\). Für alle 25 Matrixeinheiten
\(E_{ij}\) wurde mit ganzen Zahlen geprüft:

\[
\boxed{W\,d\Gamma_2(A(h))=B(h)W.}
\]

Für \(k\in\mathfrak{gl}_4\) wurde zusätzlich für alle 16 Matrixeinheiten geprüft:

\[
\boxed{W\,d\Gamma_2(I_{16}\otimes k)
=\bigl(I_{10}\otimes d\Gamma_2(k)\bigr)W.}
\]

Damit sind 40 Generatoren von
\(\mathfrak{gl}_5\oplus\mathfrak{sl}_4\) und zusätzlich der zentrale
\(\mathfrak{gl}_4\)-Generator geprüft, insgesamt 41 Basismatrizen. Je Matrix
wurden alle 120.960 Einträge verglichen: 4.959.360 exakte
Koeffizientenvergleiche, null Abweichungen. Wegen Linearität gelten die beiden
Identitäten für beliebige \(h\in\mathfrak{gl}_5\) und
\(k\in\mathfrak{gl}_4\). Eine dichte \(2016\times2016\)-Matrix wird dabei nicht
erzeugt; die äußere Zweierwirkung wird spaltenweise mit Fermionvorzeichen
ausgewertet.

## 3. Der konkrete Hardy-Generator

Nach der ausdrücklich vorgenommenen Normierung der Hardy-Basis lautet der
reelle selbstadjungierte Generator

\[
h=\begin{pmatrix}
2&2&0&0&0\\
2&2&0&0&0\\
0&0&2&0&0\\
0&0&0&1&0\\
0&0&0&0&3
\end{pmatrix},
\qquad \operatorname{tr}h=10.
\]

Sein Spektrum ist exakt \(\{0,1,2,3,4\}\). Der Checker konstruiert eine
ganzzahlige Eigenbasis und deren äußeren geraden Lift; es wird keine numerische
Eigenwertberechnung verwendet. Außerdem gilt exakt

\[
e^{i\pi h/2}=R_E=\operatorname{diag}(1,1,-1,i,-i).
\]

Damit ist der Viertelschritt der kontinuierlichen \(h\)-Wirkung genau die
vorhandene RR-Drehung. Der Familienzyklus ist hier nicht enthalten und wird
nicht mit dieser Hardy-/RR-Drehung gleichgesetzt.

Für

\[
h_F=d\Gamma_{\rm even}(h)\otimes I_4,
\qquad
h_B=\bigl[10I_{10}+\operatorname{diag}(h,-h^T)\bigr]\otimes I_6
\]

liefert der direkte Test wieder

\[
W d\Gamma_2(h_F)=h_BW
\]

ohne eine Abweichung. Die Spektren samt Multiplizitäten sind

\[
\operatorname{spec}(h_F):
0^4,1^4,2^4,3^8,4^8,5^8,6^8,7^8,8^4,9^4,10^4,
\]

\[
\operatorname{spec}(h_B):
6^6,7^6,8^6,9^6,10^{12},11^6,12^6,13^6,14^6.
\]

## 4. Exakter Erhaltungssatz

Auf der vollen Fockdarstellung definiere

\[
K=f^\dagger h_F f+b^\dagger h_B b.
\]

Schreibe

\[
j_F=(d\Gamma_{\rm even}(h)-5I_{16})\otimes I_4,
\qquad
j_B=\operatorname{diag}(h,-h^T)\otimes I_6,
\]

und

\[
\mathcal J(h)=f^\dagger j_Ff+b^\dagger j_Bb,
\qquad Q=N_f+2N_b.
\]

Dann folgt als reine Koeffizientenidentität

\[
\boxed{K=\mathcal J(h)+5Q.}
\]

\(Q\) zählt die bei der Umwandlung erhaltene Menge „zwei Fermionen oder ein
Boson“. Auf dem Ein-Boson-/Zwei-Fermion-Sektor haben Wechselwirkung und Ladung
die Blockform

\[
V=\begin{pmatrix}0&W\\W^\dagger&0\end{pmatrix},
\qquad
K_1=\begin{pmatrix}h_B&0\\0&d\Gamma_2(h_F)\end{pmatrix}.
\]

Die beiden geprüften Gleichungen

\[
h_BW=Wd\Gamma_2(h_F),
\qquad
W^\dagger h_B=d\Gamma_2(h_F)W^\dagger
\]

sind genau die beiden nichttrivialen Blöcke von \([K_1,V]=0\). In
zweiter Quantisierung folgt daher analytisch

\[
[K,b^\dagger P+P^\dagger b]=0.
\]

Da \(K\) die Bosonenzahl erhält, gilt auch \([K,N_b]=0\). Für

\[
H_W=\Delta N_b+g(b^\dagger P+P^\dagger b)
\]

folgt somit ohne Näherung

\[
\boxed{[K,H_W]=0.}
\]

Das ist der positive Satz: Die kontinuierliche RR-Wirkung ist eine echte
Symmetrie des vorhandenen nativen Hamiltonoperators.

## 5. Exakter kovarianter Antworttransport

Aus \([K,H_W]=0\) und \([K,f]=-h_Ff\) folgt für
\(H_\omega=H_W+\omega K\) unmittelbar

\[
f_{H_\omega}(t)=e^{-i\omega h_Ft}f_{H_W}(t).
\]

Ist der verwendete native Zustand \(\Omega\) unter der
\(\operatorname{Spin}(10)\times SU(4)\)-Wirkung invariant und daher seine
Antikommutatorantwort

\[
C_{H_W}(t)=c(t)I_{64},
\]

so wird dieselbe Antwort exakt zu

\[
\boxed{C_{H_\omega}(t)=c(t)e^{-i\omega h_Ft}.}
\]

Dies ist eine exakte kovariante Clock-Transportformel. Sie verändert den
nativen Anteil \(H_W\) nicht. Eine physische Auswahl von \(\omega K\) oder eine
Gleichsetzung dieses Symmetrieflusses mit der Zeit des ursprünglichen
Hamiltonoperators folgt daraus nicht.

## 6. Kleinster entscheidender Zeittest

Wähle den Bosonenmodus mit Trägerindex 3 und Familienpaar \((0,1)\), also
Archivzeile 18 in nullbasierter Zählung. Er ist ein Eigenvektor von \(h_B\) zum
Eigenwert 11. Wegen \(WW^\dagger=8I\) ist

\[
|p_\nu\rangle=\frac1{\sqrt8}W^\dagger|b_\nu\rangle
\]

ein normierter heller Fermionpaarzustand. Die Intertwineridentität gibt auch
\(d\Gamma_2(h_F)|p_\nu\rangle=11|p_\nu\rangle\). Auf dem von
\(|p_\nu\rangle,|b_\nu\rangle\) erzeugten Zweiraum gilt daher exakt

\[
H_W=\begin{pmatrix}0&\sqrt8g\\\sqrt8g&\Delta\end{pmatrix},
\qquad
K=11I_2.
\]

Für \(g\ne0\) ist die anfängliche Übergangsamplitude unter \(H_W\)
\(-i\sqrt8g\,t+O(t^2)\); unter \(K\) bleibt sie identisch null. Auch eine
skalare Verschiebung oder Zeitkalibrierung von \(K\) kann aus einer
Skalarmatrix keine Paar-Boson-Transition erzeugen. Somit ist an einem einzigen
exakten aktiven Block entschieden:

\[
\boxed{[K,H_W]=0\quad\text{bedeutet nicht}\quad K=H_W
\text{ oder gleiche physische Zeit}.}
\]

Dieser Zeuge benutzt keine Parametersuche und gilt für beliebiges \(\Delta\)
und jedes \(g\ne0\).

## 7. Metriktransport statt verschiedener endlicher Modelle

In der unnormalisierten angepassten RR-Basis ist

\[
h_{\rm raw}=\begin{pmatrix}
2&1&0&0&0\\4&2&0&0&0\\0&0&2&0&0\\0&0&0&1&0\\0&0&0&0&3
\end{pmatrix}.
\]

Eine positive diagonale, \(D_4\)-invariante Metrik
\(G=\operatorname{diag}(a,b,c,d,d)\) macht diesen Generator genau dann
selbstadjungiert, wenn \(a=4b\). Der Checker prüft als rationales Beispiel die
zweifach skalierte Hardy-Metrik

\[
G_H=\operatorname{diag}(4,1,2,2,2)
\]

und

\[
T=\operatorname{diag}(2,2,2,3,3),
\qquad
G'=T^T G_H T=\operatorname{diag}(16,4,8,18,18).
\]

\(T\) kommutiert exakt mit \(R_E,S_E,h_{\rm raw}\). Sein funktorieller Lift
\(\Gamma_{\rm even}(T)\) auf dem Spinorraum und
\(\det(T)(T\oplus T^{-T})\) auf dem Zehnerraum erhält außerdem das vollständige
W-Diagramm. Die verbleibenden positiven Metrikgewichte beschreiben für dieses
endliche \((R,S,h,W)\)-System daher unitär äquivalente Darstellungen, keine hier
nachgewiesenen verschiedenen endlichen Physiken.

Offen bleibt die entscheidende Herkunftsfrage: Welche dieser Metrik- und
Feldabbildungen wird durch die ursprüngliche Quelle ausgewählt, und wie wird sie
lokal samt Zustand und Zeit realisiert? Das Zertifikat leitet diese Auswahl
nicht aus P1 her.

## 8. Reproduktion und Grenzen

Ausgeführt wurden

```text
python3 -B checker.py
python3 -OO -B checker.py
```

Beide Ausgaben sind bytegleich. Ergebnis: `PASS`, 72 explizite exakte Checks,
null Intertwinerabweichungen. SHA-256:

- `checker.py`: `f36984b40e4055bd3b17d3240c99ded36bda100517136a90ee0916c5e653f095`
- `certificate.json`: `fa6be19a6bc511e4d65736240e9f996f6af8b11c021d73cec099053a5c703a4b`

Nicht behauptet werden eine Identität der physischen Zeiten, eine Auswahl der
Hardy-Metrik aus P1, eine lokale Feldrekonstruktion, ein Kontinuumsgrenzwert,
eine Gauß-Rekonstruktion oder ein vollständiger No-go-Satz. Die bereits
bekannten Grenzen „64 E8-Ströme sind nicht 64 freie komplexe CAR-Felder“ und
„das RR-K ist nicht durch Q1-Spektren mit \(H_W\) identisch“ werden nicht neu
aufgerollt.
