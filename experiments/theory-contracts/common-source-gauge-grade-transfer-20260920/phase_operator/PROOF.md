# Gemeinsame Quellenphase und relative Überlappungsphase

**Verdikt:** `COMMON_PHASE_EXACTLY_INVISIBLE__RELATIVE_DIAGNOSTIC_FIRST_SPECTRAL_HARMONIC_AT_ORDER_8`

## 1. Entscheidende Aussage

Der ursprüngliche 240-Wurzel-Hamiltonoperator sieht eine gemeinsame Phase

\[
\psi_\alpha(\theta)=e^{i\theta}\psi_\alpha
\]

überhaupt nicht. Alle Strahlenprojektoren, Reflexionen, lokalen Operatoren $L$ und $E$, die Bindung

\[
V(\alpha,\beta)=1-\operatorname{Re}\langle\psi_\alpha|\psi_\beta\rangle
\]

und damit der vollständige angegebene Hamiltonoperator bleiben exakt gleich. Die gemeinsame Periode erzeugt in diesem Modell daher keine kontinuierliche Antwort und keinen abgeleiteten Berry-Term.

Eine **relative** Quellenphase ist anders. Setzt man auf zwei Quellen unabhängig

\[
\psi_\alpha\mapsto e^{i\theta_1}\psi_\alpha,\qquad
\psi_\beta\mapsto e^{i\theta_2}\psi_\beta,
\]

dann bleiben $L$ und $E$ unverändert, während mit $\delta=\theta_2-\theta_1$

\[
V_\delta=1-\operatorname{Re}\!\left(e^{i\delta}z\right),
\qquad z=\langle\psi_\alpha|\psi_\beta\rangle .
\]

Diese Familie erkennt die relative Phase tatsächlich. Der erste Unterschied in den **vollständigen Quellenlabel-Spurmomenten dieser reellen Überlappungsdiagnose** erscheint aber erst im achten Moment. Das ist eine exakte Eigenschaft des vollständigen 240×240-Labelbestands, keine angenommene Folgerung aus den G31-Invariantengraden. Es ist keine Aussage, dass alle Observablen bis Grad 7 phasenblind wären: Das bereits vorhandene $W=\operatorname{Im}z$ und seine $\sigma_y$-Kompression sehen die gerichtete relative Quadratur unmittelbar.

## 2. Exakte gemeinsame Phaseninvarianz

Für jedes Label gilt

\[
|e^{i\theta}\psi_\alpha\rangle\langle e^{i\theta}\psi_\alpha|
=|\psi_\alpha\rangle\langle\psi_\alpha|.
\]

Deshalb bleiben die Materiereflexionen $r_\alpha=I-2|\psi_\alpha\rangle\langle\psi_\alpha|$ fest. Ebenso

\[
\langle e^{i\theta}\psi_\alpha|e^{i\theta}\psi_\beta\rangle
=\langle\psi_\alpha|\psi_\beta\rangle .
\]

Die in `compiler-domain-wall-core-20260919/PROOF.txt`, Abschnitt 1, definierten Terme erfüllen somit

\[
L(\theta)=L(0),\qquad E(\theta)=E(0),\qquad V(\theta)=V(0),
\qquad H(\theta)=H(0).
\]

Das ist stärker als Isospektralität: Es ist derselbe Operator auf demselben Hilbertraum.

Für jede vom übrigen Spektrum getrennte Spektralmenge $\Delta$ ist daher

\[
P_\Delta(\theta)=\mathbf 1_\Delta(H(\theta))=\mathbf 1_\Delta(H(0))
\]

konstant. Äquivalent liefert die Riesz-Formel

\[
P_\Delta(\theta)=\frac{1}{2\pi i}\oint_\Gamma
(w-H(\theta))^{-1}\,dw=P_\Delta(0).
\]

Damit ist die Kato-Verbindung $[\dot P,P]$ null und ihr offener Paralleltransport die Identität. Eine frei gewählte phasenabhängige Eigenbasis kann trotzdem eine Basis-Berryphase tragen; sie ist bei konstantem Projektor Eichwahl.

## 3. Endpunktvernähung ist zusätzliche Struktur

Aus $P(\theta)=P(0)$ folgt nur bei **identischer** Endpunktidentifikation triviale Holonomie. Wenn man nach einem Viertelumlauf zusätzlich einen Operator $S$ als Vernähung festlegt, wirkt auf dem festen Spektralraum $P S P$. Das kann nichttrivial sein, obwohl der Hamiltonoperator entlang des Weges konstant war.

Die native $\mu_4$-Struktur liefert diskrete Viertelphasen und Labelumordnungen. Sie liefert hier weder automatisch eine kontinuierliche $U(1)$-Bündelverbindung noch eine bestimmte Endpunktvernähung. Das frühere $a_0$-Ergebnis besitzt bedingt eine Periodenlinienmonodromie $t\mapsto it$, aber die Abbildung dieser Linie in denselben Quellen-Hamiltonraum ist offen. Deshalb wird hier weder „alle Berry-Holonomien sind null“ noch $a_0=\delta$ behauptet.

## 4. Vollständiges exaktes Überlappungshistogramm

Die 60 kanonischen Gaußstrahlen aus `source_channel.py` werden mit $1,i,-1,-i$ zu 240 orientierten Wurzeln ergänzt und durch 2 normiert. Für

\[
4z=A+iB
\]

ergibt die exakte Zählung über alle 57.600 geordneten Paare:

| $A$ | $B$ | Anzahl |
|---:|---:|---:|
| -4 | 0 | 240 |
| -2 | -2 | 2.880 |
| -2 | 0 | 7.680 |
| -2 | 2 | 2.880 |
| 0 | -4 | 240 |
| 0 | -2 | 7.680 |
| 0 | 0 | 14.400 |
| 0 | 2 | 7.680 |
| 0 | 4 | 240 |
| 2 | -2 | 2.880 |
| 2 | 0 | 7.680 |
| 2 | 2 | 2.880 |
| 4 | 0 | 240 |

Es werden nur Gaußzahlmultiplikation, ganze Zählungen und `Fraction` verwendet.

## 5. Fouriermomente der relativen Phase

Setze

\[
X_\delta=\operatorname{Re}(e^{i\delta}z)
=\frac{e^{i\delta}z+e^{-i\delta}\bar z}{2}.
\]

Dann ist exakt

\[
\mathbb E[X_\delta^m]
=2^{-m}\sum_{j=0}^{m}\binom mj e^{i(2j-m)\delta}
\mathbb E[z^j\bar z^{m-j}].
\]

Die vollständige Rechnung bis $m=8$ ergibt

| $m$ | $\mathbb E[X_\delta^m]$ |
|---:|---:|
| 0 | $1$ |
| 1 | $0$ |
| 2 | $1/8$ |
| 3 | $0$ |
| 4 | $3/80$ |
| 5 | $0$ |
| 6 | $1/64$ |
| 7 | $0$ |
| 8 | $35/4096+(7/5120)\cos(4\delta)+(1/4096)\cos(8\delta)$ |

Die tragenden gemischten Momente sind

\[
\mathbb E[z^8]=\frac1{32},\qquad
\mathbb E[z^6\bar z^2]=\frac1{160},\qquad
\mathbb E[|z|^8]=\frac1{32}.
\]

Damit ist Ordnung 8 die erste nichtkonstante Ordnung **dieser vollständigen Labelspurmomente**. Die möglichen G31-Grade $8,12,20,24$ waren nur die Vermutung; der Beleg ist das exakte Histogramm. Der Term $\cos(4\delta)$ stammt dabei aus dem gemischten Moment $\mathbb E[z^6\bar z^2]$, während $\cos(8\delta)$ aus $\mathbb E[z^8]$ stammt. Der Grad-8-Befund darf daher nicht auf ein rein holomorphes Invariant allein verkürzt werden.

Für $V_\delta=1-X_\delta$ sind die normalisierten Spuren bis Ordnung 7 ebenfalls phasenunabhängig. In Ordnung 8 gilt

\[
\frac1{240^2}\operatorname{Tr}V_\delta^8
=\frac{31011}{4096}+\frac7{5120}\cos(4\delta)
+\frac1{4096}\cos(8\delta).
\]

Insbesondere

\[
\frac1{240^2}\operatorname{Tr}V_0^8=\frac{9693}{1280},\qquad
\frac1{240^2}\operatorname{Tr}V_{\pi/4}^8=\frac{19379}{2560},
\]

und die unnormalisierte Quellenlabel-Differenz ist $315/2\neq0$. Die beiden endlichen Diagonaloperatoren haben also verschiedene Spektren.

Der vollständige Zwei-Quellen-Hamiltonraum besitzt zusätzlich die 64 Materiezustände von $A\otimes B\otimes C\cong(\mathbb C^4)^{\otimes3}$. Für

\[
H_\delta=A+\mu\,(V_\delta\otimes I_{64})
\]

ist die Differenz des $\mu^8$-Koeffizienten in $\operatorname{Tr}H_\delta^8$ daher

\[
64\cdot\frac{315}{2}=10080.
\]

Die Spurpolynome sind somit nicht identisch und unterscheiden sich für generisches $\mu$. Das behauptet weder, dass gemischte $A,V$-Wörter bei jeder festen Kopplung ausgeschlossen sind, noch wählt es einen physischen Wert von $\mu$.

## 6. Was das Ergebnis trägt

1. Die gemeinsame Phase ist im ursprünglichen Hamiltonoperator exakt redundant.
2. Eine relative Phase kann durch den bereits vorhandenen Realteil-Überlappungsterm diagnostisch sichtbar werden.
3. Der vollständige Labeltrace dieser Diagnose unterdrückt nichtkonstante Harmonische bis Grad 8; dann erscheinen $\cos(4\delta)$ aus einem gemischten Moment und $\cos(8\delta)$ aus dem holomorphen achten Moment. Das vorhandene $W=\operatorname{Im}z$ bleibt als gerichtete Observable früher sensitiv.
4. Die diskrete $\mu_4$-Periodizität bleibt sichtbar: alle berechneten Harmonischen haben Periode $\pi/2$.

Offen bleiben die Auswahl einer kontinuierlichen relativen Phase, ihre Dynamik, eine Endpunktvernähung, die Abbildung von $a_0$ in diesen Quellenraum und jede Yukawa-, CP- oder physische Feldidentifikation. Der Befund ist deshalb ein präziser Quellen-zu-Phasen-Diagnosetest, kein neues Axionmodell.

## 7. Reproduktion

```bash
python3 checker.py
python3 -OO checker.py
```

Beide Läufe müssen `PASS`, 130 Prüfungen, erste nichtkonstante vollständige Labelspurordnung 8, die Quellenlabel-Spurdifferenz (315/2) und die vollständige Zwei-Quellen-\(\mu^8\)-Koeffizientendifferenz 10080 melden. Die Quellen und Hashes stehen in `sourcepins.json`; die maschinenlesbaren Koeffizienten stehen in `result.json`.
