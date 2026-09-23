# Unabhängige Strukturprüfung des Ein-Hintergrund-Satzes

20. September 2026

**Review-Verdict: bestätigt unter den in ONE_BACKGROUND.md genannten
Voraussetzungen.** Der Satz ist ein enger Darstellungssatz für eine
einwertige Funktion eines Familienvektors. Er ist kein vollständiger
Quellen- oder TFPT-No-Go-Satz.

## Geprüfte Aussage

Für

\[
F:\mathbb C^3\setminus\{0\}\longrightarrow\operatorname{Mat}_3(\mathbb C),
\qquad
F(gh)=\bar gF(h)\bar g^T,
\qquad
F(e^{it}h)=e^{it}F(h),
\]

gilt

\[
F(h)_{ij}=f(\|h\|^2)\epsilon_{ijk}h_k.
\]

Der Rang ist für \(h\ne0\) höchstens zwei: genau zwei bei nichtverschwindendem
Skalar \(f\), sonst null.

## Strukturprüfung

Bei \(h=re_3\) ist der Stabilisator
\(\{\operatorname{diag}(U,1):U\in SU(2)\}\). Seine Invarianten in
\((\bar{\mathbf2}\oplus\mathbf1)^{\otimes2}\) sind genau

\[
F(re_3)=
\begin{pmatrix}
a(r)\epsilon_2&0\\
0&b(r)
\end{pmatrix}.
\]

Für

\[
g_t=\operatorname{diag}(e^{-it/2},e^{-it/2},e^{it})
\]

trägt der obere Block unter \(\bar g_tF\bar g_t^T\) das Gewicht \(+1\), der
untere Skalar das Gewicht \(-2\). Der verlangte Phasengrad \(+1\) erzwingt
daher \(b(r)=0\). Die Transitivität von \(SU(3)\) auf jeder Sphäre liefert
die behauptete Form mit \(f(r^2)=a(r)/r\).

Die Konvention ist konsistent:

\[
A(h)_{ij}=\epsilon_{ijk}h_k
\quad\Longrightarrow\quad
A(gh)=\bar gA(h)\bar g^T.
\]

Auch der gemeinsame zentrale \(\mathbb Z_3\)-Anteil passt: Für
\(\omega^3=1\) ergibt \(g=\omega I\) auf beiden Seiten den Faktor \(\omega\).

## Voraussetzungen und Aussagegrenze

Analytizität, Stetigkeit und eine Störungsentwicklung werden nicht benötigt.
Der radiale Skalar \(f:(0,\infty)\to\mathbb C\) darf beliebig sein.
Diskontinuität, nichtpolynomiale Abhängigkeit oder \(h^\dagger\)-Abhängigkeit
aus \(h\) allein liefern keinen Ausweg, solange \(F\) eine wohldefinierte
einwertige äquivariante Funktion bleibt.

Der Satz setzt gemeinsam voraus:

- genau einen nichtverschwindenden Familienvektor \(h\),
- \(h\) in der fundamentalen \(\mathbf3\) von \(SU(3)\),
- den Zieltyp \(\bar{\mathbf3}\otimes\bar{\mathbf3}\),
- exakte \(SU(3)\)-Kovarianz und Phasengrad \(+1\),
- keine weitere orientierte Familienmarkierung und keinen zusätzlichen
  Zustands- oder Verlaufshintergrund.

Echte Auswege verlassen mindestens eine Voraussetzung: weitere
transformierende Familientensoren oder Spurions, mehrere unabhängige
Familienvektoren, ausgewählte Zustandsdaten, eine kleinere Symmetriegruppe,
ein anderer Zieltyp oder eine andere Indexkonvention. Phasengrad \(-2\)
würde beispielsweise den skalaren \(b\)-Kanal erlauben.

Die diskreten Compiler-Familienmarkierungen können daher relevant sein.
Damit sie den Schluss umgehen, müssen sie als zusätzliche Tensorargumente
mit konkreter Gruppenwirkung und konkretem Phasengrad eingehen. Ob die
vollständige TFPT-Quelle die Voraussetzungen erfüllt, ist hier nicht
entschieden.

## Checker

check_one_background.py bestätigt die Stabilisatoralgebra, den
phasenkorrigierenden \(SU(3)\)-Schritt, Rang zwei des generischen
antisymmetrischen Tensors und den falschen Phasengrad des scheinbaren
Rang-eins-Komplements. Normaler und optimierter Lauf ergeben jeweils
PASS_EXACT_STABILIZER_ALGEBRA mit 12 von 12 Prüfungen.

Der Checker bestätigt die endliche lineare Algebra. Er behauptet nicht, dass
die vollständige Compilerquelle die physikalischen Voraussetzungen erfüllt.
