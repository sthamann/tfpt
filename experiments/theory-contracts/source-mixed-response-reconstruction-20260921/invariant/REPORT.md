# Native invariante Alternative: gemischter Antwortzeuge

**Verdict:** `EXACT_CONDITIONAL_DIAGNOSTIC_COUNTEREXAMPLE`  
**Entscheidung:** Die bekannten Symmetrie-, Niedrigantwort- und (Q\le3)-Prüfungen implizieren die gemischte Operatoridentität **nicht**.

Dieser Befund ist eng. Er betrifft eine Implikation innerhalb der gepinnten endlichen nativen Fockalgebra. Er ist weder ein neues TFPT-Modell noch ein Gegenbeispiel zur vollständigen TFPT-Selbstkonsistenz.

## 1. Geprüfte Alternative

Verwendet wird unverändert der native Paartensor

\[
W\in\mathbb Z^{60\times2016},\qquad WW^\ast=8I_{60},
\]

mit SHA-256

`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

Für

\[
P_A=\sum_{i<j}W_{A,ij}f_jf_i,
\qquad
X=\sum_A b_A^\dagger P_A
\]

definiere

\[
V_6=X^2+X^{\dagger 2},
\qquad
H_\eta=H_W+\eta V_6,
\qquad \eta\in\mathbb R.
\]

Der Checker bestätigt die tatsächliche Archivstruktur:

- jede der 60 Zeilen von (W) enthält genau acht Koeffizienten in \(\{\pm1\}\);
- die acht unterstützten Fermionpaare jeder Zeile sind paarweise disjunkt;
- es gibt daher (60\binom82=1680) unmittelbare Vierfermionzeugen;
- alle 1.680 Fock-Vorzeichen stimmen mit der analytischen Formel überein.

Die bereits vorhandene kontinuierliche Symmetrieprüfung wurde über ihr Zertifikat mit SHA-256 `3875e566ae7cd9c8946b1b5303cff2a68a3c3f7cbcc3602f6a4fd4f35ed2719c` gepinnt. Sie umfasst alle 25 \(\mathfrak{gl}_5\)- und 16 \(\mathfrak{gl}_4\)-Matrixeinheiten, insgesamt 4.959.360 verglichene Einträge bei null Abweichungen. Diese große Rechnung wurde hier nicht wiederholt.

## 2. Warum die Alternative die nativen Invarianten erbt

Der native Tensor ist ein Intertwiner von Fermionpaaren zum 60-dimensionalen Bosonkanal. Deshalb transformiert (P_A) kontragradient zu (b_A^\dagger), und ihre Kontraktion

\[
X=\sum_A b_A^\dagger P_A
\]

ist ein Skalar der nativen \(\operatorname{Spin}(10)\times SU(4)\)-Wirkung. Das gepinnte kontinuierliche Zertifikat prüft dazu die volle \(\mathfrak{gl}_5\oplus\mathfrak{gl}_4\)-Unteralgebra am konkreten (W). Damit sind auch (X^2), (X^{\dagger2}) und (V_6) invariant.

Für die native Ladung

\[
Q=N_f+2N_b
\]

hat (X) die Verschiebungen

\[
(\Delta N_f,\Delta N_b,\Delta Q)=(-2,+1,0).
\]

Also kommutieren (X), (V_6) und (H_\eta) mit (Q). Dieselbe Intertwineridentität gibt für den zertifizierten RR-Generator (K)

\[
[K,X]=0,
\qquad
[K,V_6]=0.
\]

Damit bewahrt die Alternative die volle native innere Symmetrie, (Q) und die RR-Erhaltungsgröße (K).

## 3. Warum die beiden niedrigeren Antworten blind bleiben

Die beiden Rekonstruktionsantworten seien

\[
R^{(f)}_{ij}[V]=\{[f_i,V],f_j^\dagger\},
\qquad
R^{(b)}_{AB}[V]=[[b_A,V],b_B^\dagger].
\]

Für (V_6) verschwinden beide als Operatoren:

\[
\boxed{R^{(f)}_{ij}[V_6]=0},
\qquad
\boxed{R^{(b)}_{AB}[V_6]=0}.
\]

Der Grund ist rein algebraisch. (X^2) enthält vier Fermionvernichter und zwei Bosonerzeuger; (X^{\dagger2}) enthält die adjungierten Wörter. Die erste Fermionklammer lässt im einzigen möglichen Beitrag drei reine Fermionerzeuger zurück, deren Antikommutator mit einem weiteren Erzeuger null ist. Außerdem gilt

\[
[b_A,V_6]=2XP_A,
\]

und dieser Ausdruck kommutiert mit jedem (b_B^\dagger).

Auch die niedrigen Ladungssektoren sind vollständig blind:

\[
\boxed{V_6|_{Q\le3}=0}.
\]

(X^2) benötigt mindestens vier Fermionen, (X^{\dagger2}) mindestens zwei Bosonen. Beide Voraussetzungen beginnen bei (Q=4). Daher ist (H_\eta) in sämtlichen Sektoren (Q\le3) exakt gleich (H_W), nicht nur spektral ähnlich.

## 4. Der erste gemischte Zeuge

Für

\[
\Gamma_{Aij}[V]
=
\left\{\left[[b_A,V],f_i^\dagger\right],f_j^\dagger\right\}
\]

folgt aus \([b_A,V_6]=2XP_A\). Wähle zwei verschiedene unterstützte Paare ((i,j)) und ((k,l)) derselben Zeile (A). Da alle acht Paare dieser Zeile disjunkt sind, ergibt die tatsächliche Fockordnung

\[
\boxed{
\langle b_A|\Gamma_{Aij}[V_6]|kl\rangle
=4W_{A,ij}W_{A,kl}.
}
\]

Der Checker hat diese Gleichung für alle 1.680 Möglichkeiten geprüft: null Abweichungen.

Ein konkreter Zeuge mit nullbasierten Moden ist

\[
A=0,\quad (i,j)=(4,57),\quad (k,l)=(5,56),
\]

mit

\[
W_{0,4,57}=-1,
\qquad
W_{0,5,56}=+1.
\]

Dann gilt

\[
P_0^2|4,5,56,57\rangle=-2|0\rangle,
\]

\[
\boxed{
\langle2b_0|V_6|4,5,56,57\rangle=-2\sqrt2
},
\]

und

\[
\boxed{
\langle b_0|\Gamma_{0,4,57}[V_6]|5,56\rangle=-4.
}
\]

Für (H_\eta) ist der zusätzliche Matrixeintrag daher (-4\eta\). Die rechte Seite der behaupteten skalaren Identität (gW_{A,ij}I) hat zwischen einem Fermionpaarzustand und einem Einbosonzustand dagegen Matrixelement null. Für jedes \(\eta\ne0\) ist die Identität somit verletzt.

Die äußeren Zustände dieses Gamma-Zeugen haben (Q=2). Das Operatorwort erzeugt jedoch vor der Wirkung von (V_6) zwei weitere Fermionen und erreicht damit erstmals einen (Q=4)-Zwischenzustand. Genau deshalb kann derselbe Beitrag in allen nackten (Q\le3)-Hamiltonrestriktionen fehlen und dennoch in der gemischten Antwort sichtbar werden.

Auf dem Vakuum bleibt die gemischte Antwort blind:

\[
\Gamma_{Aij}[V_6]|0\rangle=0,
\qquad
\langle0|\Gamma_{Aij}[V_6]|0\rangle=0.
\]

Ein reiner Vakuumtest hätte den Gegenzeugen also ebenfalls verpasst.

## 5. Positiver exakter Trennscore am vollgefüllten Zustand

Der einzelne Zeuge beweist bereits die Nichtidentität. Zusätzlich trennt der vollgefüllte Fermionzustand

\[
|F\rangle=f_0^\dagger f_1^\dagger\cdots f_{63}^\dagger|0\rangle
\]

mit Bosonvakuum sämtliche verbleibenden Gamma-Monomiale durch eine positive Norm. Definiere

\[
E_\Gamma(H;F)
=
\sum_{A,\,i<j}
\left\|
\bigl(\Gamma_{Aij}[H]-gW_{A,ij}I\bigr)|F\rangle
\right\|^2.
\]

Der Checker wendet ausschließlich die 480 tatsächlichen Paarwörter an. Die zweite Anwendung von (X) besitzt 216.480 nichtverschwindende geordnete Rohwörter. Nach dem Zusammenfassen bleiben

- 106.560 Zustände mit zwei verschiedenen Bosonmoden und vier Fermionlöchern;
- 1.680 Zustände mit zweimal derselben Bosonmode und vier Fermionlöchern.

Alle zusammengefassten Polynomkoeffizienten sind \(\pm2\). Für verschiedene Bosonmoden ist die Boson-Focknorm eins; für \((b_A^\dagger)^2|0\rangle\) ist sie zwei. Deshalb folgt exakt

\[
\begin{aligned}
\|X^2F\|^2
&=106560\cdot2^2
+1680\cdot2!\cdot2^2\\
&=426240+13440\\
&=\boxed{439680}.
\end{aligned}
\]

Die Gamma-Norm wurde zusätzlich direkt aus den zusammengefassten Koeffizienten differenziert. Jedes Vierfermionmonom besitzt \(\binom42=6\) mögliche Einfügungspaare. Bei zwei verschiedenen Bosonen gibt es zwei Bosonableitungen mit Koeffizient eins. Bei einer doppelt besetzten Bosonmode hat die Ableitung Koeffizient zwei; gegenüber der ursprünglichen Focknorm (2!) ergibt das denselben relativen Faktor zwei. Daher gilt für jedes Monom und damit für die vollständige Summe

\[
\boxed{
E_\Gamma(V_6;F)=12\|X^2F\|^2=5276160.
}
\]

Da (H_W) die native Identität \(\Gamma_{Aij}[H_W]=gW_{A,ij}I\) erfüllt, ist der exakte Trennscore der Deformation

\[
\boxed{
E_\Gamma(H_\eta;F)=5276160\,\eta^2.
}
\]

Er ist für jedes reelle \(\eta\ne0\) strikt positiv. Das ist ein positiver Quellen-Diskrepanztest: Er benennt nicht nur ein Gegenmonom, sondern misst die gesamte Abweichung dieses nativen Zustands mit einer Summe von Normquadraten.

## 6. Untere Schranke und Selbstadjungiertheit

Jede Zeile enthält acht Paarwörter, und jedes einzelne Paarwort hat Operatornorm höchstens eins. Daher

\[
\|P_A\|\le8,
\qquad
C:=\sum_A\|P_A\|^2\le60\cdot8^2=3840.
\]

Für einen Vektor im endlichen Teilchenkern gilt

\[
\|X\psi\|^2
\le C\langle\psi|(N_b+60)|\psi\rangle,
\]

\[
\|X^\dagger\psi\|^2
\le C\langle\psi|N_b|\psi\rangle.
\]

Für normiertes \(\psi\) und (n_b=\langle N_b\rangle) folgt

\[
|\langle V_6\rangle|
\le2\|X\psi\|\,\|X^\dagger\psi\|
\le C(2n_b+60).
\]

Der lineare Term lässt sich mit der Young-Ungleichung absorbieren:

\[
|g\langle X+X^\dagger\rangle|
\le
\frac\Delta2(n_b+60)+\frac{2C|g|^2}{\Delta}.
\]

Für \(\Delta>0\) erhält man deshalb

\[
\langle H_\eta\rangle
\ge
\left(\frac\Delta2-2C|\eta|\right)n_b
-30\Delta
-\frac{2C|g|^2}{\Delta}
-60C|\eta|.
\]

Die konkrete hinreichende Bedingung

\[
\boxed{
0<|\eta|<\frac{\Delta}{4C}
=\frac{\Delta}{15360}
}
\]

liefert daher eine uniforme untere Schranke.

Da (Q) erhalten ist, zerfällt die Fockdarstellung in feste (Q)-Sektoren. Jeder dieser Sektoren ist endlichdimensional: höchstens 64 Fermionen und eine feste endliche Bosonzahl, verteilt auf 60 Moden. Die orthogonale direkte Summe der endlichen hermiteschen Blöcke definiert somit eine selbstadjungierte Realisierung; die algebraische Summe endlich vieler (Q)-Sektoren ist ein Kern.

## 7. Schluss und Grenze

Für jedes hinreichend kleine reelle \(\eta\ne0\) besitzt (H_\eta) gleichzeitig:

1. dieselbe native \(\operatorname{Spin}(10)\times SU(4)\)-Invarianz;
2. dieselben Erhaltungsgrößen (Q) und (K);
3. dieselben beiden niedrigeren Operatorantworten;
4. exakt dieselbe Dynamik in allen Sektoren (Q\le3);
5. eine untere Schranke und eine selbstadjungierte Blockrealisierung.

Trotzdem unterscheidet sich seine gemischte Antwort ab dem (Q=4)-Zwischenkanal. Die geprüften Voraussetzungen reichen daher nicht aus, um

\[
\Gamma_{Aij}=gW_{A,ij}I
\]

zu erzwingen.

Der vollgefüllte Zustand liefert dazu den strikt positiven exakten Score

\[
E_\Gamma(H_\eta;F)=5276160\eta^2.
\]

Nicht gezeigt sind derselbe wechselwirkende Grundzustand, dieselben höheren nativen Momente, eine Herkunft von \(\eta\), ein räumlicher Kontinuumsgrenzwert oder irgendeine vollständige TFPT-Selbstkonsistenz. (H_\eta) dient ausschließlich als symmetrie- und positivitätsverträglicher Diagnosezeuge für die fehlende logische Implikation.

## 8. Reproduktion

Ausgeführt wurden ausschließlich die gezielten Läufe

```text
python3 checker.py
python3 -OO checker.py
```

Beide Ausgaben sind bytegleich: jeweils 5.172 Bytes, SHA-256 `e88dca14b7320f7cc37ba5ab2156a3daca41e469b8e4cc77e9690c5d2d1999a8`. Das Zertifikat meldet 2.193 exakte Checks, 1.680 gemischte Zeugen und null Abweichungen. Zusätzlich wurden 216.480 sparse Rohwörter für (X^2F) ausgewertet. Eine Vollsuite und eine große Sektormatrix wurden nicht ausgeführt.
