# Residuenbrücke zwischen RR-Träger, Markenquartett und Familienaugmentation

**Verdict:** `PASS_EXACT_SCOPED`. Auf der bereits verwendeten markierten Geometrie
\((\mathbb P^1,\mu_4)\) existiert eine exakte gemeinsame lokale Datenbrücke:

\[
0\longrightarrow \mathbb C\,1\longrightarrow
E=H^0\!\left(\mathbb P^1,\mathcal O(\mu_4)\right)
\xrightarrow{q}F_4\otimes\chi\longrightarrow0,
\qquad \chi(R)=1,\quad\chi(S)=-1.
\]

Sie ist relativ zur markierten Koordinate \(z\) und zu
\(R:f(z)\mapsto f(iz)\), \(S:f(z)\mapsto f(1/z)\) kanonisch gespalten.
Der echte logarithmische Familienraum ist dagegen die **unverdrehte**
Augmentation von \(F_4\). Die beiden Räume stammen somit aus demselben Divisor
und demselben Residuenquartett, sind aber bei festem \(R,S\) nicht dieselbe
\(D_4\)-Darstellung.

Der entscheidende Zeittest fällt präzise negativ aus: Der vorhandene
Hardy-Generator steigt nicht auf den Quotienten \(E/\mathbb C1\) ab. Er koppelt
genau eine uniforme Markenrichtung an die konstante Linie. Das dunkle
Augmentationstripel bleibt kontinuierlich invariant. Diese Rang-eins-Rückkopplung
ist im vorhandenen Fünferraum enthalten; dafür wurde kein Bad und kein neuer
Freiheitsgrad ergänzt.

## 1. Quellen- und Statusrahmen

Geprüft wurden zuerst die Originalstellen:

- `origin_theory.tex`, Zeilen 89–105: derselbe Divisor \(D=\mu_4\) liefert
  \(h^0\mathcal O(D)=5\) und \(\operatorname{rank}H_1(\mathbb P^1\setminus D)=3\);
  die physische Carrier-Identifikation bleibt `[C]`.
- `tfpt_research_contracts.tex`, Zeilen 208–280: die Formen
  \(z^{k-1}dz/(z^4-1)\), \(k=1,2,3\), tragen die drei nichttrivialen
  \(\mu_4\)-Charaktere; die Nahtrealisation bleibt offen.
- Der aktuelle Theoriegraph ist frisch: 5944 Knoten, 63981 Kanten,
  254 Contracts. `ARCH.RRCAR.01` enthält die exakte RR-Arithmetik und die
  getrennte physische `[C]`-Lesart; `rr-continuous-clock-20260921` steht auf
  `PARTIAL`.

Der gepinnte native Tensor
`outputs/TFPT_RR_Quellenbruecke/native_tensor.npz` hat SHA-256
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`,
Form \(60\times2016\), 480 von null verschiedene Einträge und
\(WW^\dagger=8I_{60}\). Er wurde hier nur auf Integrität geprüft. Die unten
auftretende geometrische Selbstenergie wird ausdrücklich **nicht** mit einer
nativen \(\Sigma_2\) gleichgesetzt.

## 2. Exakte Hauptteilfolge und ihre Richtung

Setze \(P(z)=z^4-1\) und \(D=\mu_4=\{1,i,-1,-i\}\). Für \(f\in E\) definiere

\[
q_a(f)=\operatorname{Res}_a\!\left(f\frac{dz}{z}\right)
=\frac{\operatorname{Res}_a(f)}{a}.
\]

Die vier Funktionen

\[
\ell_a(z)=\frac{a}{z-a}+\frac12
\]

erfüllen \(q_b(\ell_a)=\delta_{ab}\). Außerdem ist

\[
\ell(f)=\frac{f(0)+f(\infty)}2,
\qquad \ell(\ell_a)=0,
\]

und jedes \(f\in E\) besitzt die eindeutige Zerlegung

\[
f=\ell(f)\,1+\sum_{a\in\mu_4}q_a(f)\ell_a.
\]

Damit sind Surjektivität, Kern und Split exakt:

\[
\ker q=\mathbb C1,
\qquad \ker\ell=\operatorname{span}\{\ell_a\}_{a\in\mu_4},
\qquad q|_{\ker\ell}:\ker\ell\overset\sim\longrightarrow\mathbb C^4.
\]

Die Richtung der Markenpermutation ist wichtig. Schreibe einen Markenvektor als
\(v=(v_a)_{a\in\mu_4}\). Dann

\[
(R_4v)_a=v_{ia},
\quad\text{äquivalent}\quad e_a\mapsto e_{-ia},
\qquad
(S_4v)_a=v_{a^{-1}},
\quad\text{äquivalent}\quad e_a\mapsto e_{a^{-1}}.
\]

Direkt an den Cauchy-Funktionen gilt

\[
R\ell_a=\ell_{-ia},
\qquad S\ell_a=-\ell_{a^{-1}},
\]

und daher

\[
q(Rf)=R_4q(f),
\qquad q(Sf)=-S_4q(f).
\]

Das Minuszeichen ist kein Konventionsrest: Bei \(z\mapsto1/z\) gilt
\(d(1/z)/(1/z)=-dz/z\). Deshalb ist der Quotient
\(F_4\otimes\chi\) mit \(\chi(S)=-1\). Die Abbildung \(\ell\) ist der
\(D_4\)-Reynoldsprojektor auf die einzige triviale Linie. Das macht den Split
kanonisch relativ zu \(z,R,S\); ohne diese Markierung ist er keine
Möbius-intrinsische Zusatzstruktur.

## 3. Der Familienrang drei ist die logarithmische Augmentation

Für logarithmische Einsformen gilt die globale Residuenfolge

\[
0\longrightarrow H^0(\Omega^1)=0
\longrightarrow H^0(\Omega^1(\log D))
\xrightarrow{\operatorname{res}}\mathbb C^4
\xrightarrow{\sum}\mathbb C\longrightarrow0.
\]

Somit

\[
H^0(\Omega^1(\log D))\cong
F_4^0:=\{v\in\mathbb C^4:\sum_av_a=0\},
\qquad \dim F_4^0=3.
\]

Für

\[
\omega_k=\frac{z^{k-1}dz}{P(z)},\qquad k=1,2,3,
\]

ist der Residuenvektor \((a^k/4)_{a\in\mu_4}\). Genau deshalb verschwinden die
Summen, die drei Spalten haben Rang drei, und

\[
R^*\omega_k=i^k\omega_k,
\qquad S^*\omega_k=\omega_{4-k}.
\]

Hier wirkt die Spiegelung **ohne** Vorzeichentwist. Ihre Spur auf dem
Familienraum ist \(+1\); auf dem dunklen Teil des RR-Quotienten
\(F_4^0\otimes\chi\) ist sie \(-1\). Der gemeinsame Ursprung im selben
Vierpunktdivisor ist damit eine wirkliche lokale Datenbrücke. Eine direkte
\(D_4\)-Identifikation beider Dreidimensionalen würde den expliziten
\(\chi\)-Twist unterschlagen und ist ausgeschlossen.

## 4. Der vorhandene Hardy-Generator und die einzige Rückkopplung

Der rohe Operator \(z\partial_z\) ist auf \(E\) kein Endomorphismus: Er macht
aus einem einfachen Pol im Allgemeinen einen Doppelpol. Der bereits verwendete
Hardy-Transport

\[
Jf=Pf,
\qquad
H=J^{-1}(z\partial_z)J
=z\partial_z+\frac{4z^4}{P(z)}
\]

erhält dagegen \(E\). In der Basis \((1,\ell_a)\) lautet er exakt

\[
H=
\begin{pmatrix}
2&\mathbf1^T\\
\mathbf1&M
\end{pmatrix},
\qquad
M_{aa}=2,
\qquad
M_{ab}=\frac{a+b}{2(a-b)}\quad(a\ne b).
\]

Insbesondere

\[
H1=\frac{4z^4}{P(z)},
\qquad q(H1)=\mathbf1=(1,1,1,1)^T.
\]

Damit ist \(\ker q=\mathbb C1\) nicht \(H\)-invariant; derselbe Generator kann
auf \(E/\mathbb C1\) keine Zeit definieren. Zugleich gelten

\[
[H,R]=0,
\qquad SHS=4I-H.
\]

Die Hardy-Gram-Matrix in derselben Basis ist

\[
G_H=\operatorname{diag}\!\left(2,\,4I_4-\frac12J_4\right),
\qquad H^\dagger G_H=G_HH.
\]

Der normierte konstante Vektor und die normierte uniforme Markenrichtung
\(u=\mathbf1/2\) spannen den hellen Block

\[
H_{\rm hell}=\begin{pmatrix}2&2\\2&2\end{pmatrix}.
\]

Auf dem dunklen Raum \(\sum_av_a=0\) verschwindet die Kopplung zur Konstante.
Dieser Raum ist dreidimensional, kontinuierlich invariant und hat die exakten
Frequenzen \(1,2,3\). Das volle Spektrum ist \(0,1,2,3,4\). Somit koppelt nur
die uniforme Richtung des Markenquartetts; das Augmentationstripel, das den
Familienrang trägt, bleibt dunkel.

## 5. Exakter projizierter Resolvent und Aus-/Rückfluss

Eliminiert man die konstante Linie nur rechnerisch, ergibt der Schur-Komplement

\[
P_F(\lambda-H)^{-1}P_F
=\left[\lambda-M-\frac{J_4}{\lambda-2}\right]^{-1}.
\]

Die geometrische Rückkopplung ist daher

\[
\Sigma_{\rm geom}(\lambda)
=\frac{J_4}{\lambda-2}
=\frac{4P_u}{\lambda-2},
\]

also exakt Rang eins. Sie ist der Speicherkanal über die bereits vorhandene
konstante RR-Linie.

Für \(U(t)=e^{-itH}\) ist die komprimierte Amplitude der uniformen Richtung

\[
A_u(t)=e^{-2it}\cos(2t),
\]

die Amplitude in die konstante Linie

\[
A_{u\to1}(t)=-i e^{-2it}\sin(2t),
\]

und der Verlustoperator auf dem Markenraum

\[
I-(P_FU(t)P_F)^\dagger(P_FU(t)P_F)
=\sin^2(2t)P_u.
\]

Zwei Zeiten entscheiden die Interpretation:

- Bei \(t=\pi/4\) ist die uniforme Markenkomponente vollständig in die
  konstante Linie geflossen.
- Bei \(t=\pi/2\) ist sie vollständig zurückgekehrt und
  \(e^{-i\pi H/2}=R^{-1}\).

Darum schließt die diskrete Vierteldrehung auf dem Quotienten exakt, obwohl die
kontinuierliche Projektion zwischen zwei Viertelschritten offen ist.

## 6. Die Leckage ist unter den Clock-Annahmen unvermeidlich

Der Nichtabstieg ist nicht auf die konkrete Hardy-Matrix beschränkt. Sei
\(H'\) ein beliebiger Endomorphismus mit

\[
e^{i\pi H'/2}=R,
\qquad SH'S=\beta I-H'.
\]

Der \(R=-1\)-Raum ist eindimensional, \(\operatorname{span}(z^2/P)\), und
\(S\)-ungerade. Daher wirkt \(H'\) dort mit \(\beta/2\), also
\(e^{i\pi\beta/4}=-1\). Wäre die konstante, \(S\)-gerade Kernlinie invariant,
müsste \(H'1=(\beta/2)1\) gelten; wegen \(R1=1\) folgte zugleich
\(e^{i\pi\beta/4}=+1\). Das ist ein Widerspruch. Für den Hardy-Generator ist
\(\beta=4\).

Unter den zusätzlichen expliziten Voraussetzungen, dass \(H'\) selbstadjungiert
und die Metrik \(D_4\)-unitär ist, ist sogar der vollständige Austausch bei
\(t=\pi/4\) universell. Schreibe \(\beta=2c\). Im normierten \(R=1\)-Block aus
konstanter \(S\)-gerader und uniformer \(S\)-ungerader Linie hat man

\[
H'_{R=1}=\begin{pmatrix}c&v\\\bar v&c\end{pmatrix}.
\]

Der \(R=-1\)-Raum erzwingt \(c=2\pmod4\). Auf dem \(R=1\)-Block müssen beide
Eigenwerte \(c\pm|v|\) in \(4\mathbb Z\) liegen. Folglich
\(|v|=2\pmod4\) und

\[
\cos\!\left(\frac{\pi|v|}{4}\right)=0.
\]

Jeder selbstadjungierte kompatible Logarithmus mit dieser affinen
Zeitspiegelung tauscht bei \(t=\pi/4\) die beiden hellen Linien vollständig
aus. Eine andere kompatible Norm oder ein anderer solcher Logarithmus kann die
uniforme Quotientenleckage daher nicht reparieren. Ohne die angegebene affine
Zeitspiegelung wird dieser allgemeinere Satz nicht behauptet.

## 7. Was neu ist und was Standard bleibt

Standardgeometrie sind die Hauptteilfolge von \(\mathcal O(D)\), die globale
Residuenfolge von \(\Omega^1(\log D)\) und der Residuensatz. Neu für die hier
verwendete TFPT-Struktur ist ihre gemeinsame, vollständig ausgerichtete
Auswertung mit den **tatsächlichen** \(R,S\)-Wirkungen und der vorhandenen
Hardy-Zeit:

1. Der Fünferträger und das Markenquartett sind durch eine exakte Residuenkarte
   verbunden, einschließlich des notwendigen Spiegelungstwists.
2. Das echte Rang-drei-Familienmodul ist die unverdrehte logarithmische
   Augmentation; dieselbe Zahl \(3\) allein wäre keine Identifikation.
3. Der kontinuierliche Clock-Anschluss besitzt genau einen kanonischen
   Speicherkanal. Das dunkle Tripel bleibt geschlossen, die uniforme
   Markenrichtung nicht.
4. Die diskrete \(D_4\)-Kovarianz verbirgt diesen Verlust, weil der vollständige
   Rückfluss genau beim Viertelschritt erfolgt.

Das Ergebnis liefert eine notwendige lokale Datenbrücke. Es liefert keine
Quanten-CAR, keine Raumzeitkoordinaten, keine lokalen Eichfelder, keine
unabhängigen physischen Familien und keinen 3+1D-Kontinuumsabschluss. Die
frühere ausgeschlossene Hodge-/Familienquellenbrücke wird nicht wieder geöffnet.
Auch die bloßen Zählungen \(5,4,3\) werden nicht als physischer Fortschritt
gewertet; der Fortschritt ist die exakte Karte samt Twist und der entschiedene
Zeittest.

## 8. Reproduktion

Ausgeführt wurden

```text
python3 -B checker.py
python3 -OO -B checker.py
```

Beide Läufe erzeugen bytegleiches `certificate.json`.

- Ergebnis: `PASS_EXACT_SCOPED`, 10 Prüfblöcke, 0 Fehler.
- `checker.py` SHA-256:
  `6ca88f9ee59d5b71bf8621c6a9827092035e8897d8b7885f1e79493c3448201f`
- `certificate.json` SHA-256:
  `b7870867f3b302d8e67e269e7e03a80aec5ee753c1d32040993083bcd9a1f395`

Kein Repository-, Ledger-, Paper- oder Claimstatus wurde verändert.
