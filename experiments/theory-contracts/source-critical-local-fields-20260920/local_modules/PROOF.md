# Lokale Module am gemeinsamen \(T(D_8)\)-Konkurrenzpunkt

**Verdikt: PARTIAL.** Für das fixierte mikroskopische Gitter \(\Gamma=\mathbb Z^{9,1}\), seine Parität, die gemeinsame Einbettung \(T(D_8)\) und die ausgewählte Konkurrenzmetrik \(V_c\) ist die Modulstruktur exakt. Das Ergebnis wählt weder ein leichtes geladenes Kontinuumsfeld aus noch liefert es eine vierdimensionale Interpretation.

## 1. Die Paritätstabelle gilt für alle Gitterfelder

Mit

\[
T(p)=\bigl(p,-a\!\cdot\!p/2,a\!\cdot\!p/2\bigr),\qquad
a=(1,1,1,-1,-1,-1,-1,-1)
\]

ist das gemeinsame orthogonale Gitter

\[
L_0=T(D_8),\qquad P_0=\mathbb Z n+\mathbb Z z,qquad
M=L_0\oplus P_0.
\]

Sein Index in \(\Gamma\) ist vier. Die vier Nebenklassen können durch

\[
0,\qquad f=T(e_1)+z/2,\qquad
b=T(s)+n/2,\qquad f+b,qquad s=(1/2)^8
\]

repräsentiert werden. Ihre \(T(D_8)\)-Projektionen sind die Diskriminantenklassen \(0,v,s,c\).

Das ist keine Zählung kurzer Vektoren. Das Gitter \(M\) ist ganzzahlig und gerade. Für jedes \(m\in M\) und jeden Repräsentanten \(r\) gilt daher

\[
(r+m)^2-r^2=2B(r,m)+m^2\in2\mathbb Z.
\]

Die Parität ist folglich auf jeder vollständigen Nebenklasse konstant. Aus

\[
f^2=1,\qquad b^2=2,\qquad B(f,b)=1,qquad(f+b)^2=5
\]

folgt exakt:

| gemeinsame \(T(D_8)\)-Klasse | \(0\) | \(v\) | \(s\) | \(c\) |
|---|---:|---:|---:|---:|
| mikroskopische Parität | gerade | ungerade | gerade | ungerade |

Die Tabelle ist phasen- und cocycleunabhängig, weil sie aus der quadratischen Form modulo zwei folgt. Bosonische Oszillator- und Stromnachkommen ändern diese Parität nicht.

## 2. Orientierte \(D_5+A_3\)-Verzweigung

Wir verwenden exakt die Quellkonvention: Die ersten fünf Koordinaten bilden \(D_5\), die letzten drei \(D_3\cong A_3\), und

\[
\lambda=(1/2,\ldots,1/2)
\]

liegt nach der echten Quellgradierung im Zweig \((\overline{16},\overline4)\). Der vorhandene Glue-Clock ist

\[
k(q)=2\sum_{j=1}^{5}q_j\pmod4.
\]

Auf den verdoppelten Halbgewichten hat die \(16\) in dieser Quellkonvention den Exponenten \(3\), die \(\overline{16}\) den Exponenten \(1\). Der \(A_3\)-Grad \(2(q_6+q_7+q_8)\bmod4\) bezeichnet Grad eins als \(4\) und Grad drei als \(\overline4\). Gerade Gesamtzahl von Minuszeichen definiert die Quellklasse \(s\); ungerade Gesamtzahl die konjugierte \(c\)-Klasse. Die Minusparitäten der ersten fünf und letzten drei Koordinaten sind deshalb in \(s\) gleich und in \(c\) verschieden. Damit folgt

\[
\begin{aligned}
v&\downarrow D_5+A_3=(10,1)+(1,6),\\
s&\downarrow D_5+A_3=(16,4)+(\overline{16},\overline4),\\
c&\downarrow D_5+A_3=(16,\overline4)+(\overline{16},4).
\end{aligned}
\]

Der Checker vergleicht die 128 \(s\)-Halbgewichte direkt mit der echten `spinor_root_order` des nativen Wörterbuchs und prüft die Gradkonvention gegen die vorhandene Quellverzweigung. Er erzeugt zusätzlich die 128 Gewichte der anderen Chiralität und erhält je \(64+64\) Gewichte in den angegebenen Zweigen. Damit ist der native E8-Spinorzweig \(s\) im **gemeinsamen \(T\)-Wörterbuch** gerade, während der gekreuzt chirale Zweig \(c\) ungerade ist.

## 3. Kleinste lokale Module an \(V_c\)

Setze

\[
u=(n+z)/2,\qquad v=(n-z)/2,
\qquad V_c=K+2Kvv^{\mathsf T}K.
\]

Die gemeinsame \(T(D_8)\)-Ebene ist bezüglich \(V_c\) orthogonal zur neutralen Ebene; dort haben \(u,v\) beide positiven \(V_c\)-Normwert eins. Für \(\alpha,\beta\in\mathbb Z\) haben die neutralen Koeffizienten in den vier Klassen die Formen

\[
\begin{array}{c|c|c}
0 &(\alpha+\beta,\alpha-\beta)&\min\|\cdot\|^2=0\\
v &(\alpha+\beta+1/2,\alpha-\beta-1/2)&\min\|\cdot\|^2=1/2\\
s &(\alpha+\beta+1/2,\alpha-\beta+1/2)&\min\|\cdot\|^2=1/2\\
c &(1+\alpha+\beta,\alpha-\beta)&\min\|\cdot\|^2=1.
\end{array}
\]

Die minimalen euklidischen \(D_8\)-Normen der Klassen sind \(0,1,2,2\). Da \(\Delta(x)=x^{\mathsf T}V_cx/2\), ergeben sich die exakten Modulminima

| gemeinsame Klasse | Parität | minimales \(\Delta\) an \(V_c\) | orientierter Inhalt |
|---|---:|---:|---|
| \(0\) | gerade | \(0\) | Vakuummodul |
| \(v\) | ungerade | \(3/4\) | \((10,1)+(1,6)\), mit neutralem Halbgitteranteil |
| \(s\) | gerade | \(5/4\) | \((16,4)+(\overline{16},\overline4)\), mit neutralem Halbgitteranteil |
| \(c\) | ungerade | \(3/2\) | \((16,\overline4)+(\overline{16},4)\), mit kritischem neutralem Dressing |

Die unteren Schranken werden erreicht. Für \(v\) ist ein Erreicher \(T(e_1)+z/2=f\). Für \(s\) ist es \(T(s)+n/2=b\). Für \(c\) kann man

\[
c_{\min}=(1/2,-1/2,1/2,\ldots,1/2),\qquad T(c_{\min})+u
\]

nehmen; dieser ganzzahlige Vektor liegt in der Nebenklasse \(f+b+M\). Der rohe Repräsentant \(f+b=T(e_1+s)+u\) ist nicht minimal: Er hat Lorentz-Norm \(5\) und \(\Delta_{V_c}=5/2\). Erst die Verschiebung um \(T(e_1+e_2)\in T(D_8)\) liefert den obigen Repräsentanten mit Lorentz-Norm \(3\) und \(\Delta_{V_c}=3/2\).

Damit sind die kleinsten **möglichen lokalen ungeraden** Module am diagnostischen Konkurrenzpunkt genau der \(v\)-Zweig bei \(\Delta=3/4\) und der gekreuzt chirale \(c\)-Zweig bei \(\Delta=3/2\). Der letztere ist algebraisch ein Spinorprojektionsanteil mit notwendigem neutralem kritischem Dressing. Weder \(u\) noch \(v\) allein ist ein ganzzahliger mikroskopischer Gittervektor. Daher ist der kritische Refermion kein unabhängiges lokales Quellfeld, und \(\Delta=3/2\) ist insbesondere keine vierdimensionale Weyl-Dimension.

Ein expliziter, vollständig integraler Erreicher macht den \(c\)-Befund konkret. Für

\[
p=(1/2,-1/2,1/2,\ldots,1/2)
\]

gelten

\[
T(p)+u=(1,0,1,0,0,0,0,0,1,0),\qquad
T(p)+v=(1,0,1,0,0,0,0,0,0,1).
\]

Beide Felder sind ungerade, haben \(\Delta_{V_c}=3/2\), \(q=3\), \(Y=1/3\) und gehören wegen ungerader D5-, aber gerader D3-Minusparität zum Zweig \((16,\overline4)\). Sie unterscheiden sich um den lokalen neutralen Vektor \(z\). Das zeigt Existenz und Typ eines möglichen lokalen \(S_-\)-Komposits, jedoch nicht seine dynamische Auswahl oder Leichtigkeit.

## 4. Unverzichtbare Einbettungsgrenze

Die obigen Gewichtsbezeichnungen gehören zur gemeinsamen Einbettung \(T(D_8)\). Für die andere Quellzerlegung gilt

\[
F_{\rm aux}(p)=T(p)-k_a(p)n,\qquad
B(F_{\rm aux}(p),x)=B(T(p),x)-k_a(p)B(n,x).
\]

Sie liefert auf allgemeinen \(x\in\Gamma\) daher eine andere Cartanwirkung. Konkret sind die ursprünglichen Elementarfelder

\[
e_i=F_{\rm aux}(r_i)-a_i m
\]

ungerade, obwohl \(r_i\) Spinorwurzeln des dortigen E8-Wörterbuchs sind. Das ist die kleinste direkte Kontrolle gegen eine unzulässige globale Verallgemeinerung. Die tatsächlichen Ladungsfunktionale \(q\) und \(Y\) werden auf der gemeinsamen Ebene durch \(T(\mathbf1_8)\) und \(T(Y_8)\) getragen; \(n,z\) sind neutral.

Das Ergebnis ist daher **kein universelles TFPT-No-Go** und kein Satz, dass jedes Spinorgewicht in jeder Einbettung bosonisch sei. Es ist die exakte lokale Moduldiagnose des fixierten Gitters am gewählten \(T(D_8)\)-Konkurrenzpunkt. Ob eines der ungeraden Module dynamisch leicht wird, lokal im gewünschten Kontinuum realisiert wird oder als vierdimensionales chirales Feld erscheint, bleibt offen.

## Reproduktion

```bash
python3 check_local_modules.py
python3 -OO check_local_modules.py
```

Beide Läufe müssen `PASS` liefern; der Checker verwendet keine `assert`-Anweisungen.
