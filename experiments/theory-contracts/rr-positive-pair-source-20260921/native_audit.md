# Unabhängige Prüfung des positiven RR-Lifts am nativen W

## Ergebnis

Der endliche algebraische Teil des vorgeschlagenen positiven Lifts ist am unveränderten nativen Tensor exakt bestätigt:

\[
H_+=2\kappa N_b+\frac{\kappa}{\sqrt2}(X+X^\dagger)+\frac{\kappa}{4}D
=2\kappa\sum_A\left(b_A+\frac{P_A}{\sqrt8}\right)^\dagger
\left(b_A+\frac{P_A}{\sqrt8}\right),\qquad \kappa>0.
\]

Der geprüfte Tensor ist

`outputs/TFPT_Stabile_Quellenrekonstruktion/native_tensor.npz`

mit SHA-256

`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

Er hat Form `60 x 2016`, genau 480 Nichtnullen und erfüllt ganzzahlig

\[
WW^\dagger=8I_{60}.
\]

Der Checker führte 33 exakte Prüfungen und keine Gleitkommaprüfung aus. Normaler und `-OO`-Lauf waren bytegleich. Es wurde weder eine vollständige Fockmatrix noch die volle Q3-Hamiltonmatrix aufgebaut. Die größte gebaute Matrix war die dünnbesetzte ganzzahlige Gram-Matrix `3840 x 3840`.

## Direkt bestätigte Blöcke

Für den normierten hellen Paarzustand

\[
|p_A\rangle=P_A^\dagger|0\rangle/\sqrt8
\]

und den Einbosonzustand \(|b_A\rangle\) ergibt die tatsächliche W-Norm exakt

\[
H_+\big|_{\operatorname{span}\{|p_A\rangle,|b_A\rangle\}}
=\kappa\begin{pmatrix}2&2\\2&2\end{pmatrix}.
\]

Der Block hat Nullrichtung \((1,-1)\) und helle Energie (4\kappa). Die Koeffizienten der unteren Antworten sind

\[
C_1=\frac{\kappa}{\sqrt2}W,\qquad
C_{\rm el}=\frac{\kappa}{4}W^\dagger W=2\kappa\Pi_W,
\qquad C_2=0,
\]

mit

\[
\Pi_W=\frac18W^\dagger W,\qquad \operatorname{rank}\Pi_W=60.
\]

Die Projektoridentität wurde ohne die dichte `2016 x 2016`-Matrix auf

\[
(WW^\dagger)W=8W
\]

reduziert. Ebenso ist die Schur-Grenze exakt gesättigt:

\[
C_{\rm el}=C_1^\dagger(2\kappa I_{60})^{-1}C_1.
\]

Die Aussage (C_2=0) ist eine Strukturidentität des ausgeschriebenen Operators: Keine seiner Monome ändert die Bosonzahl um zwei.

## Die zusammengesetzten B sind nicht kanonisch

Für

\[
B_A=b_A+P_A/\sqrt8
\]

liefert die CAR-Norm jeder der 60 W-Zeilen

\[
[B_A,B_A^\dagger]|0\rangle=2|0\rangle,
\qquad
[B_A,B_A^\dagger]|F\rangle=0.
\]

Der Checker prüft beide Werte für alle 60 Kanäle. Damit darf die positive Quadratform nicht als 60 freie kanonische Bosonen umbenannt werden.

## Explizite besetzungsabhängige Antwort

Der Tensor enthält die Verbindung zwischen den nullbasierten Moden (4) und (57) genau einmal. Aus

\[
C_{\rm el}/\kappa=W^\dagger W/4
\]

wurde die zugehörige Spalte gebildet und anschließend (f_4) angewandt. Der einzige verbleibende ganzzahlige Zähler ist

\[
\{57:1\}.
\]

Somit gilt exakt

\[
R_{44}|0\rangle=0,
\qquad
R_{44}f_{57}^\dagger|0\rangle
=\frac{\kappa}{4}f_{57}^\dagger|0\rangle.
\]

Das widerlegt für diesen Kandidaten eine zustandsunabhängige Zahlenmatrixdarstellung der gesamten unteren Fermionantwort. Es ist kein Widerspruch zu einem Rekonstruktionssatz, der eine solche globale Antwort ausdrücklich voraussetzt.

## Vollständiges Q3-Spektrum ohne große Diagonalisierung

Der Checker baut die ganzzahlige Abbildung

\[
C_3:\Lambda^3\mathbb C^{64}\longrightarrow
\mathbb C^{60}\otimes\mathbb C^{64},
\]

mit Form `3840 x 41664` und 29.760 Nichtnullen. Für

\[
G=C_3C_3^\dagger
\]

wird exakt das annihilierende Polynom geprüft:

\[
G(G-7I)(G-10I)(G-12I)=0.
\]

Die Spuren der Lagrange-Spektralprojektoren liefern ohne numerische Eigenwertrechnung:

| Eigenwert von (G) | Multiplizität | Projektorzähler / Nenner |
|---:|---:|---:|
| 0 | 64 | -53.760 / -840 |
| 7 | 2.880 | 302.400 / 105 |
| 10 | 576 | -34.560 / -60 |
| 12 | 320 | 38.400 / 120 |

Damit ist \(\operatorname{rank}C_3=3776\) und \(\dim\ker C_3=37888\).

Im Q3-Sektor hat der Lift in der Ordnung `(3F, bF)` den Block

\[
\frac{H_+}{\kappa}=
\begin{pmatrix}
C_3^\dagger C_3/4 & C_3^\dagger/\sqrt2\\
C_3/\sqrt2 & 2I
\end{pmatrix}.
\]

Zu jedem positiven Gram-Eigenwert \(\lambda\) gehört ein zweidimensionaler Block mit Determinante null und Spur

\[
2+\lambda/4.
\]

Die 64 dunklen bF-Richtungen bei \(\lambda=0\) haben Energie (2\kappa). Zusammen ergibt sich das vollständige Spektrum:

| Energie | Multiplizität |
|---:|---:|
| (0) | 41.664 |
| (2\kappa) | 64 |
| (15\kappa/4) | 2.880 |
| (9\kappa/2) | 576 |
| (5\kappa) | 320 |

Die Summe ist 45.504. Der Nullraum besteht hier aus den 37.888 Richtungen in \(\ker C_3\) und je einer Nullrichtung für die 3.776 positiven Singularwerte, insgesamt

\[
37888+3776=41664=\binom{64}{3}.
\]

## Analytisch bewiesen, aber nicht durch eine volle Matrixzählung geprüft

Die globale Positivität folgt unmittelbar aus der Summe von Quadraten. Für den vollständigen Nullraum wird die Bosonkomponentenrekursion von

\[
\left(b_A+P_A/\sqrt8\right)|\Psi\rangle=0
\]

verwendet. Weil die geraden Paarvernichter (P_A) miteinander kommutieren, ist die Rekursion konsistent und jede bosonleere Fermionkomponente \(|\psi\rangle\) bestimmt genau einen Nullzustand

\[
e^{-X/\sqrt8}|0_b\rangle\otimes|\psi\rangle.
\]

Damit folgt analytisch

\[
\ker H_+=\operatorname{Ran}S,
\qquad \dim\ker H_+=2^{64},
\qquad
\dim(\ker H_+\cap\mathcal H_{Q=q})=\binom{64}{q}.
\]

Dieser globale Satz wurde bewusst nicht durch eine unmögliche volle Fockmatrix simuliert. Der exakte Q2- und Q3-Check sowie die konkrete (R_{44})-Antwort sind unabhängige endliche Kontrollen seiner lokalen Konsequenzen.

## Beweisgrenze

Bestätigt ist die endliche Algebra **unter der zusätzlich gewählten Liftregel** und dem gepinnten W-Tensor. Nicht hergeleitet sind:

- warum die ursprüngliche Quelle gerade diese Abbildung auf (b_A) und (P_A/\sqrt8) auswählt,
- warum diese Konstruktion der physische RR-Kanal ist,
- die Auswahl des Sektors (Q=64) aus dem global (2^{64})-dimensionalen Nullraum,
- ein lokaler chiraler 3+1D-Kontinuumsabschluss oder T1–T8.

Der präzise Fortschritt ist daher: Der positive RR-Formlift ist ein intern konsistenter, exakt positiver W-Kandidat mit zwingender elastischer Paarantwort. Er ist keine Herkunftsherleitung.

## Reproduktion

Im Ordner dieses Berichts:

```bash
python3 -B checker.py
cmp <(python3 -B checker.py) <(python3 -OO -B checker.py)
```

Der erste Befehl gibt bytegenau `certificate.json` aus; der zweite bestätigt den gleichwertigen Lauf mit deaktivierbaren Assertions entfernt. Der Checker selbst verwendet für fachliche Gates ausschließlich nicht abschaltbare `need(...)`-Prüfungen.

Für ein portables Hauptpaket verwendet der Checker eine danebenliegende `native_tensor.npz`, sobald sie vorhanden ist. Andernfalls fällt er auf den oben gepinnten archivierten Pfad zurück; in beiden Fällen erzwingt derselbe SHA-256-Pin identische Eingangsdaten.
