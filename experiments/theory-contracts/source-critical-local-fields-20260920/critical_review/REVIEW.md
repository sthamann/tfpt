# Unabhängige Prüfung der lokalen IR-Felder am `n/z`-Konkurrenzpunkt

**Verdikt:** `BEDINGT_BESTAETIGT_MIT_PRAEZISIERUNGEN`

**Korrektur der Erstfassung:** Der wörtliche Vertreter
`f+b=T(e1+s)+u` ist nicht minimal: \(|e_1+s|^2=4\), also trägt sein
\(D_8\)-Anteil \(h_R=2\), und der volle Vertex hat
\((h_R,h_L)=(5/2,0)\), nicht \((3/2,0)\). Die Dimension \(3/2\) gehört
zum minimalen Vertreter `x_c=f+b-T(e1+e2)=T(s-e2)+u`. Alle folgenden
Tabellen und Aussagen unterscheiden diese beiden Operatoren ausdrücklich.

Die vermuteten IR-Skalierungsdimensionen

\[
\Delta_f=\frac58,\qquad
\Delta_b=\frac98,\qquad
\Delta_{(f+b),\min}=\frac32
\]

folgen am bereits ausgewählten Konkurrenzpunkt `V_c` aus der Standard-
Refermionisierung des selbstdualen Sine-Gordon-Modells bei
\(\beta^2=4\pi\), **wenn** die beiden reellen Cosinus-Kopplungen passend
normiert gleich sind, genau eine Majorana-Kopie kritisch bleibt und der
massive Ising-Sektor in einem Sektor/Vakuum ausgewertet wird, in dem der
benötigte Ordnungs- oder Unordnungsoperator einen von null verschiedenen
Langdistanzanteil besitzt. Die Dimensionsaussage ist damit eine bedingte
1+1D-IR-Aussage. Weder `V_c` noch die Kopplungsgleichheit oder der
Vakuumsektor sind aus der Quelle ausgewählt.

Zwei Formulierungen der Vermutung müssen verschärft werden:

1. Die Ising-Twistfelder dürfen nicht als vom \(D_8\)-Sektor unabhängige
   lokale Faktoren behandelt werden. Ihre Semilokalität ist genau durch
   das globale Glue mit den \(D_8\)-Diskriminantklassen korreliert.
2. Beim minimalen Vertreter `x_c-z` ist nur der **neutrale** Majorana-Faktor
   linksbewegend. Der volle Operator enthält zusätzlich den rechtsbewegenden
   \(D_8\)-Cospinor mit \(h_R=1\) und ist daher nicht antichiral.

## 1. Festgehaltene Voraussetzungen

Diese Prüfung übernimmt ausschließlich die in `source-graded-locality-20260920`
bereits gesetzten Daten:

\[
K=\operatorname{diag}(1^9,-1),\quad
B(n,n)=B(z,z)=0,\quad B(n,z)=2,
\]

\[
u=\frac{n+z}{2},\qquad v=\frac{n-z}{2},\qquad
B(u,u)=1,\ B(v,v)=-1,
\]

und die vollständige lokale Gitterzerlegung

\[
\Gamma=\bigsqcup_{c\in\{0,f,b,f+b\}}
\bigl(T(D_8)\oplus \mathbb Z n\oplus\mathbb Z z+c\bigr),
\]

mit

\[
f=T(e_1)+\frac z2,\qquad b=T(s)+\frac n2.
\]

Am ausgewählten `V_c` sind die \(D_8\)- und neutralen Ebenen orthogonal.
Für einen neutralen Vertex \(a u+b v\) gelten daher

\[
(h_R,h_L)=\left(\frac{a^2}{2},\frac{b^2}{2}\right).
\]

Insbesondere besitzen \(n/2=(u+v)/2\) und
\(z/2=(u-v)/2\) beide die UV-Gewichte \((1/8,1/8)\).
Ein neutraler Vektor \(a u+b v\) ist genau dann ein ursprünglicher lokaler
Gittervertex, wenn \(a,b\in\mathbb Z\) dieselbe Parität haben. Daher sind
\(u\) und \(v\) einzeln nicht in \(\Gamma\).

## 2. Standard-Bosonisierung und der massive Ising-Faktor

Lecheminant, Gogolin und Nersesyan schreiben das \(\beta^2=4\pi\)-Modell
als zwei Majorana-Felder mit Massen

\[
m_1\propto g_n-g_z,\qquad m_2\propto g_n+g_z.
\]

Bei gleich normalisierten Kopplungen ist eine Kopie masselos und die andere
massiv. Sie betonen zugleich, dass zwei Ising-Kopien global nicht einfach
zwei unabhängige Majorana-Sektoren sind: Die Randbedingungen sind korreliert.

In einer Standardkonvention für zwei Ising-Kopien lauten die lokalen
Bosonisierungskorrespondenzen, bis auf nichtuniverselle Konstanten und
Konventionsphasen,

\[
\begin{aligned}
\sin(\sqrt\pi\,\Phi)&\sim\sigma_1\sigma_2,&
\cos(\sqrt\pi\,\Phi)&\sim\mu_1\mu_2,\\
\sin(\sqrt\pi\,\Theta)&\sim\sigma_1\mu_2,&
\cos(\sqrt\pi\,\Theta)&\sim\mu_1\sigma_2.
\end{aligned}
\]

Hier kann der Halbvertex von \(n/2\) mit
\(e^{i\sqrt\pi\Phi}\) und derjenige von \(z/2\) mit
\(e^{i\sqrt\pi\Theta}\) identifiziert werden. Somit

\[
\begin{aligned}
e^{i n/2}&\sim \mu_1\mu_2+i\sigma_1\sigma_2,\\
e^{i z/2}&\sim \mu_1\sigma_2+i\sigma_1\mu_2.
\end{aligned}
\]

Die Bezeichnungen `1` und `2`, ebenso die Zuordnung von \(\sigma\) und
\(\mu\), können durch Massenvorzeichen und Dualitätskonvention vertauscht
werden. Der invariant wichtige Inhalt ist:

* Ist die massive Kopie 2 ungeordnet, \(\langle\mu_2\rangle\ne0\), dann
  projizieren die beiden Halbvertices auf die komplementären kritischen
  Twistfelder \(\mu_1\) beziehungsweise \(\sigma_1\).
* Ist sie geordnet, \(\langle\sigma_2\rangle\ne0\), werden diese beiden
  Zuordnungen vertauscht.

Jedes kritische Twistfeld hat
\((h_R,h_L)=(1/16,1/16)\). Das Ersetzen des massiven Faktors durch seinen
Langdistanz-Erwartungswert erklärt den Fluss des neutralen Beitrags von
\(\Delta=1/4\) auf \(\Delta=1/8\).

Diese Projektion braucht eine Zustandsbedingung. Im geordneten massiven
Ising-Modell verschwindet \(\langle\sigma_2\rangle\) im endlichen Volumen
im symmetrischen Zustand. Man muss einen gebrochenen unendlichen
Volumensektor wählen oder die Aussage auf die entsprechende
Korrelationsasymptotik formulieren. Ohne diese Festlegung ist die
Ein-Feld-Projektion auf ein kritisches Twistfeld nicht bewiesen.

## 3. Korrekte Feldtabelle

Die \(D_{8,1}\)-Gewichte der vier Diskriminantklassen sind

\[
h(0)=0,\quad h(v)=\frac12,\quad h(s)=h(c)=1.
\]

Damit ergibt sich:

| lokale Klasse / Vertreter | \(D_8\)-Faktor | neutraler UV-Faktor | UV \((h_R,h_L)\) | führender IR-Faktor | IR \((h_R,h_L)\) | \(\Delta_{IR}\) | Spin \(h_R-h_L\) | Parität |
|---|---:|---:|---:|---|---:|---:|---:|---:|
| `0` | Identität | Identität | \((0,0)\) | Identität | \((0,0)\) | 0 | 0 | gerade |
| `f=T(e1)+z/2` | Vektor, \(h_R=1/2\) | \(e^{iz/2}\), \((1/8,1/8)\) | \((5/8,1/8)\) | Vektor \(\times\sigma_1\) oder \(\mu_1\) | \((9/16,1/16)\) | \(5/8\) | \(1/2\) | ungerade |
| `b=T(s)+n/2` | Spinor, \(h_R=1\) | \(e^{in/2}\), \((1/8,1/8)\) | \((9/8,1/8)\) | Spinor \(\times\mu_1\) oder \(\sigma_1\) | \((17/16,1/16)\) | \(9/8\) | 1 | gerade |
| rohes `f+b=T(e1+s)+u` | nichtminimaler Cospinor-Klassenvektor \(|e_1+s|^2=4\), \(h_R=2\) | \(e^{iu}\), \((1/2,0)\) | \((5/2,0)\) | affine Anregung \(\times\xi_R^{crit}\) | \((5/2,0)\) | \(5/2\) | \(5/2\) | ungerade |
| rohes `f+b-z=T(e1+s)+v` | nichtminimaler Cospinor-Klassenvektor \(h_R=2\) | \(e^{iv}\), \((0,1/2)\) | \((2,1/2)\) | affine Anregung \(\times\xi_L^{crit}\) | \((2,1/2)\) | \(5/2\) | \(3/2\) | ungerade |
| `x_c=f+b-T(e1+e2)=T(s-e2)+u` | minimaler Cospinor, \(|s-e_2|^2=2\), \(h_R=1\) | \(e^{iu}\), \((1/2,0)\) | \((3/2,0)\) | Cospinor \(\times\xi_R^{crit}\) | \((3/2,0)\) | \(3/2\) | \(3/2\) | ungerade |
| `x_c-z=T(s-e2)+v` | minimaler Cospinor, \(h_R=1\) | \(e^{iv}\), \((0,1/2)\) | \((1,1/2)\) | Cospinor \(\times\xi_L^{crit}\) | \((1,1/2)\) | \(3/2\) | \(1/2\) | ungerade |

Für `f` und `b` ist jeweils genau eines von \(\sigma_1,\mu_1\) gemeint;
die beiden Klassen erhalten komplementäre Twistfelder. Welches Feld welcher
Klasse zugeordnet wird, hängt am Vorzeichen der massiven Majorana-Masse und
an der gewählten Bosonisierungskonvention. Die Dimensionen ändern sich
dabei nicht.

Die letzten vier Tabellenzeilen gehören derselben Glueklasse an. Das
wörtliche `f+b` verwendet jedoch \(e_1+s\), dessen Normquadrat 4 ist. Es
ist daher nicht der minimale Cospinor-Vertreter. Mit der \(D_8\)-Wurzel
\(d=e_1+e_2\) erhält man

\[
c_{\min}=e_1+s-d=s-e_2,\qquad |c_{\min}|^2=2,
\]

und erst `x_c=f+b-T(d)` hat \(\Delta=3/2\). Die jeweiligen \(u\)- und
\(v\)-Vertreter unterscheiden sich um den lokalen Gittervektor \(z\);
ihre Spins unterscheiden sich um die ganze Zahl 1 und stimmen daher in
der topologischen Spinphase überein. Die Klasse allein wählt nicht zwischen
dem rechts- und linksbewegenden neutralen Majorana-Anteil.

Die Korrektur ist direkt in den zehnkomponentigen Vektoren sichtbar. Die
rohen Vertreter sind

\[
f+b=(2,1,1,0,0,0,0,0,0,1),\qquad B(f+b,f+b)=5,
\]

und

\[
f+b-z=(2,1,1,0,0,0,0,0,-1,2),\qquad B(f+b-z,f+b-z)=3.
\]

Beide haben am `V_c`-Punkt \(\Delta=5/2\). Nach Subtraktion von
\(T(d)=(1,1,0,0,0,0,0,0,-1,1)\) lauten die minimalen Vertreter

\[
x_c=(1,0,1,0,0,0,0,0,1,0),\qquad B(x_c,x_c)=3,
\]

\[
x_c-z=(1,0,1,0,0,0,0,0,0,1),\qquad B(x_c-z,x_c-z)=1.
\]

Mit
\(\Delta_{V_c}(x)=[B(x,x)+2B(v,x)^2]/2\) besitzen beide exakt
\(\Delta_{V_c}=3/2\). Alle vier Vektoren sind ganzzahlig in \(\Gamma\).
Das ist der konkrete Grund, weshalb ein **minimaler**
`Cospinor × u/v`-Vertreter lokal sein kann, obwohl die reinen neutralen
Vertices \(u\) und \(v\) nicht zum ursprünglichen Gitter gehören.

## 4. Globale Lokalität und OPE

Die exakte UV-Paarung ist

\[
B(T(e_1),T(s))=\frac12,\qquad
B(z/2,n/2)=\frac12,\qquad B(f,b)=1.
\]

Also tragen sowohl der reine \(D_8\)-Teil als auch der neutrale Teil bei
einer vollständigen Umkreisung die Phase \(-1\); nur ihr Produkt ist lokal.
Im IR ist dieselbe Struktur als Semilokalität von Ising-Ordnung und
-Unordnung sichtbar. \(\sigma_1\) und \(\mu_1\) dürfen deshalb nicht als
unabhängig kombinierbare lokale Primärfelder neben beliebigen
\(D_8\)-Modulen aufgefasst werden. Das geerbte Glue korreliert

\[
(D_8\text{-Vektor})\times(\text{ein Twistfeld}),\qquad
(D_8\text{-Spinor})\times(\text{das komplementäre Twistfeld}).
\]

Die zwei Minuszeichen heben sich auf. Vererbte Klein- und Cocycle-Faktoren
bestimmen weiterhin die graduierten Gleichzeit-Austauschzeichen; die
Monodromiegleichung allein sagt nicht, dass zwei ungerade Operatoren
kommutieren.

Diese Rechnung beweist die gegenseitige Lokalität der konkret geprüften
`f`/`b`-Paarung und die UV-Lokalität der expliziten ganzzahligen
minimalen `f+b`-Klassenvertreter. Sie konstruiert noch nicht den vollständigen modularen
IR-Hilbertraum und prüft daher nicht separat jedes Twistprodukt gegen jeden
weiteren zugelassenen Operator. Die Tabellenzeilen sind als Komponenten
des **geerbten korrelierten Glue-/Spinstruktur-Projektors** zu lesen. Eine
ungekoppelte Tensorprodukt-Theorie, in der `Spinor × Twist` unabhängig mit
allen Ising- und \(D_8\)-Modulen kombiniert wird, ist durch diese Prüfung
nicht legitimiert. Unter lokalem RG-Fluss bleibt die ursprüngliche
Operatorlokalität erhalten; für eine vollständige IR-CFT-Konstruktion wäre
aber zusätzlich der gesamte Sektor- und Randbedingungsprojektor anzugeben.

Die Fusion der komplementären Twistfelder enthält den kritischen
Majorana-Kanal. Man darf ihre Skalierungsdimensionen dabei nicht einfach
addieren: Der singuläre OPE-Koeffizient liefert den chiralen beziehungsweise
antichiralen Majorana-Zweig. Die direkten lokalen Gittervertreter
`x_c` und `x_c-z` zeigen exakt, welcher minimale \(D_8\)-Cospinor diesen Zweig
lokal kleidet.

## 5. Was nicht folgt

* Die neutralen \(u\)- und \(v\)-Majoranas sind keine eigenständigen
  mikroskopisch lokalen Vertices von \(\Gamma\). Ein lokaler ursprünglicher
  Operator trägt im betreffenden ungeraden Sektor zugleich den
  \(D_8\)-Cospinor beziehungsweise die vollständige globale Sektorbindung.
* Eine effektive kritische Majorana-Gleichung ist kein Spin(10)-Materiefeld
  und keine Identifikation mit einem 3+1D-Weyl-Fermion.
* \(h=3/2\) ist ein 1+1D-konformes Gewicht, keine Herleitung vierdimensionaler
  Chiraliät.
* Die Rechnung wählt weder `V_c` noch \(g_n=g_z\), das Massenvorzeichen,
  einen Ising-Vakuumsektor, eine Domänenstruktur oder eine physikalische
  Source-to-IR-Abbildung aus.
* Das Domain-Wall-Ergebnis von Cano et al. setzt räumlich arrangierte
  I8/E8-Phasen voraus und behandelt einen im ursprünglichen Elektronenraum
  nichtlokalen Majorana-Operator. Es stützt die bedingte Interface-Mechanik,
  liefert aber keine Quellselektion für den hier geprüften Konkurrenzpunkt.

## 6. Quellen und genaue Verwendung

1. P. Lecheminant, A. O. Gogolin, A. A. Nersesyan,
   *Criticality in self-dual sine-Gordon models*,
   arXiv:cond-mat/0203294, Abschnitt II.2. Verwendet für die
   \(\beta^2=4\pi\)-Refermionisierung, die Massenkombinationen, den
   einen massiven und einen kritischen Majorana-Modus sowie den Hinweis auf
   korrelierte globale Randbedingungen.
2. A. M. Tsvelik, *Universality classes of order parameters composed of
   many-body bound states*, Phys. Rev. B 94, 205141 (2016), Appendix B,
   Gleichung (B5). Verwendet für die expliziten vier
   Zwei-Ising-Bosonisierungskorrespondenzen. Nichtuniverselle Vorfaktoren
   sind für die Gewichtstabelle irrelevant.
3. J. Cano, M. Cheng, M. Barkeshli, D. J. Clarke und C. Nayak,
   *Chirality-Protected Majorana Zero Modes at the Gapless Edge of Abelian
   Quantum Hall States*, arXiv:1505.07825. Verwendet nur für die Bedingtheit der arrangierten
   I8/E8-Interface- und Majorana-Mechanik und die Nichtlokalität des
   undressierten Domain-Wall-Operators; nicht als Herleitung des hiesigen
   Konkurrenzpunkts.
