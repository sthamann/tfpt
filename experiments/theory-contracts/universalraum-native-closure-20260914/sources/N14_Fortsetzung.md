# TFPT und Universalraum: neue endliche Abschlüsse und ihre Beweisgrenzen

**14. September 2026 · Forschungsfortsetzung für Stefan Hamann**

Eigene Herleitungen und unabhängig ausgeführte Prüfungen auf Grundlage der neun übergebenen Dateien. Nicht extern begutachtet. Keine Änderung eines Repositorys, eines Ledgers oder einer ursprünglichen Theoriequelle. Kein behaupteter Beweis von RH oder einer vollständigen TOE.

## 0. Ergebnis und genauer Prüfumfang

Diese Fortsetzung ergänzt die Anhänge um folgende Resultate:

1. Eine nach Vermittlerzahl gewichtete Normabschätzung zertifiziert im deklarierten endlichen C16 Modell bereits bei `t/Δ = 1/20` eine Trennung des niedrigen Besetzungsbands vom übrigen Spektrum um mindestens `Δ/4`. Die bisher benutzte Bedingung `‖V‖ < Δ/4` ist dafür nicht erforderlich.
2. Eine explizite Restschranke sechster Ordnung für den energieabhängigen Feshbachoperator wird angegeben. Daraus folgt außerdem eine quantitative spektrale Fehlerschranke der Entwicklung bis zur vierten Ordnung. Bei `1/640` ist sie klein; bei `1/20` zertifiziert diese konservative Schranke noch keine kleine innere Spektralstörung.
3. Alle 64 SU(4) Sektoren des führenden C16 Austauschoperators wurden unabhängig durch eine Suche nach ihren tiefsten Eigenpaaren untersucht. Das erste Singulettquartett und die Projektion des vollständigen Operators vierter Ordnung wurden reproduziert. Dies ist Gleitkommanumerik, keine vollständige Eigenwertauflistung und kein Intervallbeweis.
4. Für unverändert global geteilte Vermittler wird eine konkrete nicht extensive Skalierung bewiesen. Lokale Vermittler pro Zelle besitzen dagegen eine lineare Stabilitätsschranke. Damit ist die Modellgabel unter einer ausdrücklich geforderten thermodynamischen Stabilitätsbedingung entschieden.
5. Die Kohärenzbedingung wird von einzelnen Vertizes auf eine ganze Familie erweitert. Zusätzlich wird exakt gezeigt, warum der verstimmte mikroskopische Zweiblock nicht allein durch Warten die idealisierte vollständige Vermittlung `U₀` ausführt.
6. Ein exakter Spektralfilter für den angekleideten mikroskopischen Stern wird konstruiert. Er benötigt keine kommensurablen Energieabstände, aber ausdrücklich kontrollierte Zeitentwicklung, Register und Phasensteuerung.
7. Die bereits bekannte Fourierverteilung der quadratischen E8 Phasen erlaubt einen effizienten klassischen Simulator auch für klassisch adaptierte, zwischenzeitlich gemessene Takte. Diese konkrete Ausleseroute liefert damit keinen eigenen Quantenvorteil.

**Nicht geschlossen:** die native Auswahl der Architektur und ihrer Steuerzugriffe, der originale phasenmarkierte TFPT Adapter, die exakte globale Spektralordnung einschließlich aller höheren Ordnungen, die vollständige Weil Positivität, ein neuer schneller Faktorisierungsalgorithmus, der gemeinsame physikalische Kontinuumsgrenzwert und T1 bis T8 als Gesamtforderungen.

Die zwei Compiler PDFs mit und ohne `a` im Datumsnamen sind byteidentisch. Sie werden nicht als unabhängige Belege gezählt. Das Quellenmanifest enthält die Prüfsummen aller neun Eingaben.

### Quellenkürzel

| Kürzel | Übergebene Datei |
|---|---|
| S0 | `Eingefügter Text.txt`, offene Aufgaben A1 bis A8, B1 bis B4 und T1 bis T8 |
| S1 | `Konsolidierte_Fortsetzung.md` |
| S2 | `TFPT_Universalraum_Gesamtkonstrukt_2026-09-14.md` |
| S3 | `TFPT_Universalraum_Gesamtdarstellung_2026-09-14.pdf` |
| S4 | `TFPT_GEMEINSAME_AUSFUEHRUNG_TECHNISCH_2026-09-14_v1.0.md` |
| S5 | `TFPT_GEMEINSAME_AUSFUEHRUNG_2026-09-14_v1.0.md` |
| S6 | `TFPT_Compiler_Universalraum_2026-09-14_v1.2.md` und seine beiden identischen PDF Exporte |

S3, physische PDF Seite 25, enthält noch die überholte Dublettangabe. Die späteren Quellen S1, S2 und S4 unterscheiden bereits zwischen verschiedenen Mikromodellen, idealen Schaltungen und nativen Herkunftsfragen. Diese Unterscheidung wird hier beibehalten.

## 1. Unveränderter endlicher Quellenvertrag

Wir verwenden für die Bandrechnung das konkrete Modell aus S1, Abschnitt 5.1:

\[
H=\Delta N_b+t(B^\dagger+B),\qquad
B^\dagger=\sum_{e,A}b^\dagger_{r(e),A}K_{e,A},\qquad \Delta>0.
\]

Es gibt 16 Orte mit harter Belegung, vier Farben pro besetztem Ort, 40 Clebsch Kanten und 60 harmonische Vermittlermoden. Zehn Vektorlabels tragen jeweils sechs antisymmetrische Farbkanäle. Die Gesamtladung ist

\[
N_f+2N_b=16.
\]

Die Kanten sind die Paare der geraden Fünfbitwörter mit Hammingabstand vier. Ihr Vektorlabel ist die einzige Koordinate, in der beide Wörter übereinstimmen, einschließlich des dortigen Vorzeichens. Jedes der zehn Vektorlabels gehört zu vier disjunkten Kanten.

Im Farbwortregister hat ein aktiver Vertex genau die Amplituden `+1` beziehungsweise `−1` für die beiden vertauschten Farben. Zusätzliche CAR Vorzeichen verändern ihre Beträge nicht. Die folgende Normrechnung gilt deshalb sowohl mit diesen CAR Vorzeichen als auch für die in S2 deklarierte harte Tensorrealisierung mit denselben absoluten Matrixeinträgen. Sie beweist keine phasentreue Äquivalenz dieser Modelle.

`Q_n` bezeichnet den Sektor mit genau `n` Vermittlern, `n=0,…,8`, und `P=Q_0`. Im P Raum ist jeder Ort besetzt, daher

\[
\dim P=4^{16}=4\,294\,967\,296,\qquad PHP=0.
\]

Alle diese Räume sind bei fester Gesamtladung endlich. Keine Aussage dieses Abschnitts setzt einen thermodynamischen oder gravitativen Grenzwert voraus.

## 2. Neue Bandtrennung bis zum Betriebswert 1/20

### 2.1 Gewichtete Blockabschätzung

Setze

\[
B_n=Q_{n+1}B^\dagger Q_n.
\]

In einer Besetzungsbasis erhalten Zustände mit Bosonbelegungen `n_μ` das positive Gewicht

\[
w=\left(\prod_\mu n_\mu!\right)^{-1/2}.
\]

Beim Übergang `n_μ → n_μ+1` hebt das Gewichtsverhältnis den bosonischen Faktor `√(n_μ+1)` in der gewichteten Spaltensumme auf. Ein Eingang kann höchstens so viele Kanten abbauen, wie sein besetzter Ortsuntergraph Kanten besitzt. Schreibe `e_max(f)` für die größte Kantenanzahl auf `f` besetzten Orten.

In einer gewichteten Zeilensumme trägt die Rückkehr aus einer mit `n_μ` besetzten Mode den Faktor `n_μ`. Es gibt zwei mögliche Farbreihenfolgen. Zu einem festen Vektorlabel gehören höchstens vier disjunkte Kanten. Bei `2(n+1)` Löchern können höchstens `min(4,n+1)` dieser Kanten vollständig leer sein. Damit sind die gewichteten Summen beschränkt durch

\[
c_n=e_{\max}(16-2n),\qquad
r_n=2(n+1)\min(4,n+1).
\]

Der gewichtete Schurtest für die absolute rechteckige Matrix liefert

\[
\boxed{\|B_n\|^2\le \beta_n^2
=2(n+1)\min(4,n+1)e_{\max}(16-2n).}
\]

Die Herleitung des Schurtests ist hier elementar. Für eine Matrix `A`, positive Zeilen und Spaltengewichte `w_y,w_x` und eine Eingabe `v` gilt nach Cauchy Schwarz

\[
\sum_y\left|\sum_x A_{yx}v_x\right|^2
\le r\sum_x|v_x|^2\sum_y |A_{yx}|\frac{w_y}{w_x}
\le rc\|v\|^2.
\]

Die verwendeten Maxima wurden durch vollständige ganzzahlige Enumeration aller `2^16` Ortsmengen bestimmt:

\[
(e_{\max}(f))_{f=0}^{16}
=(0,0,1,2,4,5,7,9,12,14,17,20,24,27,31,35,40).
\]

Somit

\[
(\beta_n^2)_{n=0}^{7}=(80,248,432,544,480,336,224,64).
\]

Das Programm kontrolliert zusätzlich die Anzahl aller Teilmengen jeder Größe und liefert Zeugen für die Maxima. Die Maximalitätsaussage beruht hier auf einer vollständigen endlichen Enumeration, nicht auf einer Stichprobe.

### 2.2 Relative Norm statt zu grober Gesamtnorm

Auf `Q=I−P` normieren wir mit `H_{0,Q}=ΔN_b`. Dann

\[
\left\|H_{0,Q}^{-1/2}\,tQ(B^\dagger+B)Q\,H_{0,Q}^{-1/2}\right\|
\le |\epsilon|\,\|T\|,\qquad \epsilon=t/\Delta,
\]

wobei T eine reelle symmetrische 8×8 Matrix mit verschwindender Diagonale und folgenden quadrierten Nebendiagonaleinträgen ist:

\[
124,\quad72,\quad136/3,\quad24,\quad56/5,\quad16/3,\quad8/7.
\]

Eine numerische Kontrolle liefert `‖T‖≈14,769352608880`. Der eigentliche Nachweis verwendet jedoch eine exakte rationale LDL Zerlegung von `15I−T`. Deren Pivots sind

\[
15,\ \frac{101}{15},\ \frac{435}{101},\ \frac{5839}{1305},\
\frac{56265}{5839},\ \frac{3892891}{281325},\
\frac{56892965}{3892891},\ \frac{5942618197}{398250755}.
\]

Sie sind alle strikt positiv. Weil T durch einen alternierenden Vorzeichenwechsel zu `−T` unitär äquivalent ist, folgt aus `λ_max(T)<15` zugleich `‖T‖<15`.

Damit gilt für `|ε|<1/15`

\[
\boxed{QHQ\ge(1-15|\epsilon|)H_{0,Q}
\ge\Delta(1-15|\epsilon|)Q.}
\]

### 2.3 Spektralsatz

Sei `d=dim P`. Das Variationsprinzip auf dem d dimensionalen Unterraum P ergibt `λ_d(H)≤0`. Die Kompression auf den Unterraum Q von Kodimension d ergibt dagegen

\[
\lambda_{d+1}(H)\ge\lambda_1(QHQ)
\ge\Delta(1-15|\epsilon|).
\]

Folglich besitzt H genau d niedrige Eigenwerte, gezählt mit Multiplizität, unterhalb des positiven Vermittlerbands, und

\[
\boxed{\lambda_{d+1}(H)-\lambda_d(H)
\ge\Delta(1-15|\epsilon|).}
\]

Insbesondere:

\[
\boxed{|t|/\Delta=1/20\quad\Longrightarrow\quad
\text{Bandabstand}\ge\Delta/4.}
\]

Bei `1/640` liefert dieselbe Rechnung sogar `125Δ/128` statt der früheren konservativen `Δ/2`.

**Reichweite:** Der Satz umfasst alle SU(4) Sektoren, weil er auf dem vollständigen P und Q Raum gilt. Er beweist weder einen eindeutigen Grundzustand innerhalb des niedrigen Bands noch den inneren Singulettabstand. Er ist keine Behauptung, dass `‖V‖<Δ` bei `1/20` gelte.

Die führende Skala `J=2t²/Δ` beträgt bei `1/20` `Δ/200`, bei `1/640` `Δ/204800`. Der größere durch diese Bandrechnung zugelassene Wert entspricht einem Faktor 1024 in J. Daraus folgt ohne weitere Ressourcenrechnung kein Faktor 1024 in Rechengeschwindigkeit oder Hardwareleistung.

## 3. Explizite Restschranken und spektrale Fehlerkontrolle

### 3.1 Energieabhängiger Feshbachoperator

Setze, wie in S1,

\[
M=B_0,\quad N=B_1,\quad D=M^\dagger M,\quad C=NM.
\]

Aus Abschnitt 2 folgen

\[
\|D\|\le80,\qquad \|C^\dagger C\|\le80\cdot248=19840.
\]

Für `E≤0` ist der exakte Feshbachoperator auf P

\[
\Sigma(E)=-t^2M^\dagger(QHQ-E)^{-1}M.
\]

Die Neumannentwicklung des relativ normierten Q Resolventen ist für `ρ=15|ε|<1` absolut konvergent. Zwischen zwei Besuchen des Einvermittlersektors verschwinden ungerade Pfadlängen durch Vermittlerparität. Die ersten beiden Beiträge lauten daher

\[
\boxed{\Sigma(E)=
-\frac{t^2}{\Delta-E}D
-\frac{t^4}{(\Delta-E)^2(2\Delta-E)}C^\dagger C
+R_F(E).}
\]

Für den Rest gilt

\[
\boxed{\|R_F(E)\|
\le\frac{80t^2}{\Delta-E}\frac{\rho^4}{1-\rho^2}
\le80\Delta\epsilon^2\frac{\rho^4}{1-\rho^2}.}
\]

Dies ist bei festem endlichem Modell tatsächlich eine Restabschätzung der Ordnung `t^6/Δ^5`. Sie ist zunächst eine Aussage über den energieabhängigen Feshbachoperator, nicht über die Norm eines beliebig gewählten kanonischen effektiven Hamiltonoperators.

Eine schärfere skalare Wegmajorante erhält man mit

\[
a_8=8,\qquad a_n=n-\frac{\epsilon^2\beta_n^2}{a_{n+1}}
\quad(n=7,\ldots,1),\qquad r_1=1/a_1.
\]

Die Positivität der zugehörigen Jacobi Matrix folgt aus Abschnitt 2. Der Resolventenrest ist dann auch durch

\[
80\Delta\epsilon^2\left(r_1-1-\frac{\epsilon^2\beta_1^2}{2}\right)
\]

beschränkt. Diese Form zählt die möglichen Wege zwischen Vermittlersektoren enger, statt jede Weglänge nur durch dieselbe Normpotenz abzuschätzen.

### 3.2 Fehlerschranke für sämtliche niedrigen Eigenwerte bis vierter Ordnung

Der in S1 definierte kanonische Koeffizient vierter Ordnung ist

\[
F_4=D^2-\frac12C^\dagger C.
\]

Schreibe

\[
H_4=\Delta[-\epsilon^2D+\epsilon^4F_4],\qquad
G=I+\epsilon^2D,
\]

\[
A=-\Delta\epsilon^2D-\frac{\Delta\epsilon^4}{2}C^\dagger C,
\qquad H_{\rm gen}=G^{-1/2}AG^{-1/2}.
\]

Die symmetrische Normalisierung liefert

\[
\boxed{\|H_{\rm gen}-H_4\|
\le1\,305\,600\,\Delta\epsilon^6.}
\]

**Begründung.** Für den D Anteil verwendet man exakt

\[
-\frac{\epsilon^2D}{I+\epsilon^2D}
=-\epsilon^2D+\epsilon^4D^2
-\frac{\epsilon^6D^3}{I+\epsilon^2D},
\]

was die Schranke `80³ ε^6 = 512000 ε^6` gibt. Für den anderen Anteil folgt aus

\[
\|I-G^{-1/2}\|\le\frac12\epsilon^2\|D\|,\qquad\|G^{-1/2}\|\le1,
\]

die zusätzliche Schranke `(1/2)80·19840 ε^6 = 793600 ε^6`.

Jeder niedrige exakte Eigenwert erfüllt

\[
0\le -E_i/\Delta\le x:=\frac{80\epsilon^2}{1-\rho}.
\]

Für die Abweichung des exakten Feshbachoperators von `A−ε²ED` erhält man gleichmäßig auf diesem Intervall die dimensionslose Schranke

\[
\begin{aligned}
r(\epsilon)={}&
\frac{80\epsilon^2x^2}{1+x}
+19840\epsilon^4\left[\frac12-\frac1{(1+x)^2(2+x)}\right]\\
&+80\epsilon^2\frac{\rho^4}{1-\rho^2}.
\end{aligned}
\]

Die ersten beiden Terme sind die exakt abgeschätzten Energietaylorreste der beiden expliziten Nenner; der dritte ist der Resolventenrest.

Für die aufsteigend geordneten niedrigen Eigenwerte `E_i` von H und die geordneten Eigenwerte `h_i` von H₄ folgt

\[
\boxed{|E_i-h_i|\le
\Delta\left[r(\epsilon)+1\,305\,600\epsilon^6\right],
\qquad i=1,\ldots,4^{16}.}
\]

**Warum die Zuordnung der Eigenwerte gilt.** Die Matrix `Σ(E)−EI` ist streng fallend in E, denn `Σ'(E)` ist negativ semidefinit. Ihre Nullstellen unterhalb des Q Spektrums sind genau die niedrigen Eigenwerte des vollständigen Operators. Die Kongruenz mit `G^{-1/2}` erhält die Trägheit und verwandelt sie in `H_gen−EI` plus einen Fehler der Norm höchstens `Δr`. An der i ten Nullstelle begrenzt die Weyl Abschätzung deshalb den Abstand zum i ten Eigenwert von `H_gen`. Die oben kontrollierte Normalisierung liefert schließlich die angegebene Abschätzung gegenüber H₄.

Dies ist ein **spektrales Zertifikat**. Es wird nicht als bereits konstruierte Normschranke einer gemeinsamen kanonischen Intertwinerabbildung ausgegeben.

### 3.3 Konkrete Werte und klare Grenze

| Größe | ε=1/640 | ε=1/20 |
|---|---:|---:|
| Zertifizierter Abstand zum hohen Band | `125Δ/128` | `Δ/4` |
| Feshbachrest, grob, in Δ | `5,8967648572·10⁻¹¹` | `0,1446428571` |
| Feshbachrest, Wegmajorante, in Δ | `2,8308276844·10⁻¹¹` | `0,0657638846` |
| Spektralfehler von H₄, in Δ | `1,1533142188·10⁻¹⁰` | `0,2844855379` |
| Derselbe Spektralfehler, in J | `2,3619875202·10⁻⁵` | `56,8971075838` |

Bei `1/640` liegt damit eine konkrete kleine spektrale Fehlerschranke vor. Bei `1/20` ist das Band sicher getrennt, aber diese konservative Restschranke ist für die innere Lücke unbrauchbar. Aus einer zu großen oberen Schranke folgt nicht, dass der tatsächliche Fehler groß ist. Es folgt, dass ein genaueres Argument benötigt wird.

Die allgemeinen Methoden der effektiven Transformationen sind etabliert [W1]. Die besonderen Konstanten und die hier angegebene endliche Blockabschätzung wurden in dieser Arbeit hergeleitet.

### 3.4 Bedingter Transfer eines späteren rigorosen führenden Gaps

Liefert eine unabhängige rigorose Rechnung einen eindeutigen Grundzustand von `H_C/J` mit Gap mindestens `g_C`, so folgt aus `‖F₄‖≤1920` und Abschnitt 3.2 unmittelbar

\[
\operatorname{gap}(H_{\rm low})/J
\ge g_C-1920\epsilon^2-2\eta_4(\epsilon)/J,
\]

wobei `η₄` die absolute spektrale Fehlerschranke gegenüber H₄ bezeichnet. Bei `1/640` beträgt der gesamte Abzug höchstens ungefähr `0,00473473975`. Dieser Transfer ist bewiesen; der hier nur numerisch gefundene Wert für `g_C` wird dadurch nicht rückwirkend zu einem rigorosen Eingangszertifikat.

## 4. Alle 64 Sektoren, Singulettquartett und vierte Ordnung

### 4.1 Vollständige Sektoraufteilung, begrenzte Spektralnumerik

Schur Weyl Dualität zerlegt

\[
(\mathbb C^4)^{\otimes16}
=\bigoplus_{\lambda\vdash16,\,\ell(\lambda)\le4}
V^{SU(4)}_\lambda\otimes S^\lambda.
\]

Es gibt genau 64 zulässige Youngformen. Die Summe der Specht Dimensionen ist `6 952 660`; die größte ist `512 512`. Die mit den SU(4) Dimensionen gewichtete Summe ergibt exakt `4^16`. Der Singulettmultiplizitätsraum der Form `(4,4,4,4)` hat Dimension `24 024`.

Die Programme erzeugen die Standardtableaux neu und realisieren benachbarte Transpositionen in der orthogonalen Youngdarstellung. Daraus wird

\[
H_C/J=20I+\frac12\sum_{e\in E(C_{16})}S_e
\]

matrixfrei angewandt. Für jeden der 64 Sektoren wurden die tiefsten Ritzpaare gesucht; sehr kleine Sektoren wurden dicht gerechnet. Es handelt sich nicht um eine Auflistung sämtlicher Eigenwerte des vier Milliarden dimensionalen Gesamtraums.

Die niedrigsten gefundenen Sektorenergien sind:

| Youngform | SU(4) Dimension | Niedrigster gefundener Wert E/J |
|---|---:|---:|
| `(4,4,4,4)` | 1 | `11,045398337068445` |
| `(5,4,4,3)` | 15 | `12,133537149348134` |
| `(5,5,3,3)` | 20 | `12,322754353567715` |
| `(5,5,4,2)` | 45 | `12,875129642221417` |
| `(6,4,3,3)` | 45 | `12,981639540677609` |

Der kleinste gefundene Nichtsingulettabstand zum Grundzustand beträgt somit ungefähr `1,08813881228 J`. Der größte ausgegebene Eigenpaarrest über die 64 Rechnungen beträgt `2,356·10⁻⁹` in J Einheiten. Die Ergebnisdatei dokumentiert alle 64 Sektoren, ihre Dimensionen und Residuen.

**Was damit nicht bewiesen ist:** Ein kleiner Ritzrest beweist die Nähe zu einem echten Eigenwert, aber allein nicht das Fehlen eines tieferen, nicht gefundenen Eigenwerts. Deshalb wird die globale Ordnung weiterhin als numerischer Befund und nicht als rigoroser Nichtsingulettausschluss geführt.

### 4.2 Singulett und vollständiger F₄ Operator unabhängig reproduziert

Eine separate Rechnung mit zehn niedrigen Singulettvektoren ergibt

\[
E_{0,s}/J=11.045398337068429,
\]

\[
E_{1,s}/J\approx11.56176212280257
\]

mit vier orthogonalen Vektoren auf dem zweiten Niveau. Die Reste dieser fünf Zustände liegen unter `7,9·10⁻¹⁴`, die Orthogonalitätsabweichung der zehn Vektoren beträgt `8,8·10⁻¹⁵`.

Der vollständige vorgegebene Operator aus S1 lautet mit `E_e=I−S_e`

\[
F_4=2\sum_eE_e
+\sum_{e<f,\,e\cap f\ne\varnothing}\{E_e,E_f\}
-2\sum_{e<f,\,r(e)=r(f)}E_eE_fT_{ef}.
\]

Seine drei Klassen umfassen 40, 160 und 60 Beiträge. Dieser gesamte Ausdruck wurde in derselben unabhängig konstruierten Youngdarstellung ausgewertet. Es folgen

\[
\langle0_s|F_4|0_s\rangle=555.4885003638361,
\]

und vier Kompressionseigenwerte zwischen

\[
583.2920386663804\quad\text{und}\quad583.2920386663919.
\]

Damit ist die in S1 gemeldete Korrektur reproduziert:

\[
\Delta_s/J=0.516363785734\ldots
+13.901769151274\ldots\,\epsilon^2+O(\epsilon^4).
\]

Bei `ε=0,05` ergibt die Entwicklung erster Ordnung im Störparameter `ε²` ungefähr `0,55111820861 J`. Dieser Wert bleibt eine Entwicklung des verfolgten Singulettabstands, nicht die exakt zertifizierte mikroskopische Gesamtlücke.

Die Neuberechnung prüft die Auswertung der ausgeschriebenen F₄ Formel, nicht sämtliche ursprünglichen CAR Pfade ihrer Herleitung. Beide Prüfaufgaben bleiben unterschieden.

### 4.3 Algebraischer Mechanismus des Quartetts

Die Graphautomorphismen enthalten

\[
G=(\mathbb Z_2)^4\rtimes S_5,\qquad |G|=1920.
\]

Die exakte Charakterrechnung ergibt im Singulettspechtraum einen unter den Translationen invarianten Unterraum der Dimension 1764. Darin tritt die gewöhnliche vierdimensionale Standarddarstellung von S₅ mit Multiplizität 80 auf. Der entsprechende isotypische Block besitzt somit die Form

\[
\mathbb C^{80}\otimes\mathbb C^4,
\qquad H|_{\rm std}=A_{80}\otimes I_4.
\]

Jede einfache Eigenzahl von `A₈₀` ist daher innerhalb dieses Blocks exakt vierfach geschützt. Die numerisch gefundenen vier Vektoren sind translationsinvariant bis auf einen Fehler unter `2,8·10⁻¹⁴`; die vier erzeugenden Koordinatentranspositionen besitzen auf dem Quartett Spur zwei. Das passt zur Standarddarstellung, nicht zu ihrer mit dem Signum verdrillten Variante.

**Nicht überspringen:** Die exakte Charakterzerlegung erklärt einen algebraischen Schutzmechanismus. Sie beweist allein weder die Einfachheit der fraglichen Eigenzahl von `A₈₀` noch ihre Position gegenüber allen anderen Blöcken. Ein vollständiges exaktes Multiplizitätszertifikat des ersten angeregten Niveaus ist damit noch nicht erbracht.

## 5. Die Vermittlergabel: global geteilt oder lokal pro Zelle

### 5.1 Gegenbeweis gegen Extensivität bei unveränderter globaler Teilung

Betrachte m Kopien derselben C16 Zelle, aber dieselben 60 globalen Vermittlermoden und unveränderte Kopplung t. Die Gesamtladung beträgt `16m`.

Wähle in jeder Zelle dieselbe aktive Kante und denselben Farbkanal. Die übrigen 14 Orte bleiben fest besetzt. Auf der aktiven Kante sind ein normierter antisymmetrischer Paarzustand und zwei Löcher erlaubt. Der lokale Vertex koppelt sie mit Matrixelement `√2`.

Sei `|k⟩` die normierte symmetrische Superposition mit k leeren aktiven Paaren und k Bosonen in der gemeinsamen Mode. Sie liegt im vorgeschriebenen Gesamtladungssektor. Zwischen `|k⟩` und `|k+1⟩` beträgt das Matrixelement

\[
\sqrt2\,t(k+1)\sqrt{m-k}.
\]

Die Kompression des vollständigen Hamiltonoperators auf diese zwei Testzustände ist

\[
\begin{pmatrix}
\Delta k&\sqrt2t(k+1)\sqrt{m-k}\\
\sqrt2t(k+1)\sqrt{m-k}&\Delta(k+1)
\end{pmatrix}.
\]

Die übrigen Vertizes besitzen auf dieser zweidimensionalen Testmenge keinen Erwartungsbeitrag: Sie verändern die festgehaltenen Zuschauerbelegungen oder die gewählte Vermittlermode. Die Kompression muss kein invarianter Unterraum sein; für das Variationsprinzip genügt ein Testunterraum.

Damit gilt rigoros

\[
\boxed{E_0(m)\le\Delta(k+1/2)
-\sqrt{\Delta^2/4+2t^2(k+1)^2(m-k)}.}
\]

Für gerade m und `k=m/2` folgt

\[
\frac{E_0(m)}m\le\frac\Delta2-\frac{|t|}{2}\sqrt m+o(1)
\longrightarrow-\infty.
\]

Es existiert also für feste positive Δ und festes `t≠0` keine von m unabhängige untere Schranke `E₀(m)≥−Cm`.

Das schließt **diese** globale Realisierung als Kandidaten für den verlangten extensiven, thermodynamisch stabilen lokalen Vielzellenlimes aus. Es ist kein allgemeiner Satz, dass jede langreichweitige Physik oder Gravitation extensiv sein müsse.

Eine Skalierung `t_m∝m^(-1/2)` oder ein neuer Gegenoperator kann die Schlussfolgerung verändern. Beides ändert den Quellenvertrag; globale Kopplung wird dadurch zudem nicht automatisch lokale Ausbreitung.

### 5.2 Lokale Alternative mit Stabilitätsnachweis

Mit eigenen Vermittlern `b_{c,μ}` pro Zelle c und `K_{c,μ}=Σ_{e:r(e)=μ}K_{e,A}` gilt

\[
H_{\rm loc}
=\Delta\sum_{c,\mu}
\left(b_{c,\mu}^\dagger+\frac t\Delta K_{c,\mu}^\dagger\right)
\left(b_{c,\mu}+\frac t\Delta K_{c,\mu}\right)
-\frac{t^2}{\Delta}\sum_{c,\mu}K_{c,\mu}^\dagger K_{c,\mu}.
\]

Es gibt 60 Moden pro Zelle und `‖K_{c,μ}‖≤4√2`, somit

\[
\boxed{H_{\rm loc}\ge-1920m\,t^2/\Delta.}
\]

Mit einem positiv definiten lokalen Bosontransportoperator h und einer größenunabhängigen unteren Schranke `h≥Δ₀I>0` ergibt dieselbe quadratische Ergänzung `−1920m t²/Δ₀`.

Dies schließt die Stabilitätsfrage dieser Architektur. Es beweist noch nicht den Kontinuumsgrenzwert, masselose Anregungen, einen gemeinsamen Lorentzkegel oder drei ausgewählte Raumrichtungen. Die räumliche Verklebung muss weiterhin angegeben werden.

### 5.3 Warum der endliche Bandsatz nicht einfach größenuniform wird

Schon m völlig unabhängige lokale Zellen zeigen die Grenze einer globalen Bandargumentation. Jede Zelle hat negative niedrige Eigenwerte, außerdem symmetrische dunkle Zustände bei null und positive hohe Eigenwerte. Schreibe `e_g<0` für eine niedrige Grundenergie und `e_h>0` für eine hohe Zellenergie.

Das Produkt aller niedrigen Zellräume enthält einen Gesamtzustand bei Energie null. Ein Produktzustand mit einer hohen Zellenergie und sonst niedrigen Grundzuständen hat dagegen Energie

\[
e_h+(m-1)e_g.
\]

Für hinreichend großes m ist dieser Wert negativ. Die beiden durch ihre lokalen Besetzungsbänder definierten Klassen sind dann nicht mehr durch eine einzige globale Energiegrenze geordnet getrennt. Daraus folgt weder das Verschwinden des Grundzustandsgaps noch das Versagen lokaler effektiver Beschreibungen. Es zeigt aber, warum für T5 lokale Fehlerkontrolle und eine konkrete Zustands beziehungsweise Energiedichteklasse benötigt werden, nicht bloß eine Wiederholung des endlichen Gesamtbandarguments.

## 6. Globale Kohärenz ist mehr als die Summe lokaler Gramtests

Für eine endliche Familie von Abbildungen `K_a:X_a→Y` und `L_a:X_a→Z` gilt

\[
\boxed{L_a^\dagger L_b=K_a^\dagger K_b\quad\forall a,b}
\]

genau dann, wenn eine einzige Isometrie V auf `span_a im K_a` existiert mit

\[
L_a=VK_a\quad\forall a.
\]

**Beweis.** Betrachte `K=[K₁ … K_m]` und `L=[L₁ … L_m]` auf der direkten Summe aller Eingänge. Die vollständige Blockgramgleichheit ist `L†L=K†K`. Die Definition `V(Kx)=Lx` ist dann wohldefiniert und isometrisch. Die Umkehrung ist unmittelbar.

Der lokale Test `L_a†L_a=K_a†K_a` allein reicht nicht. Beispiel: `K₁=K₂=1`, dagegen `L₁=|0⟩`, `L₂=|1⟩`. Jeder lokale Normtest stimmt, aber die beiden kohärenten Summen besitzen Normquadrat vier beziehungsweise zwei.

Für einen ganzen kohärenten Ablauf müssen die relevanten zusammengesetzten Wörter denselben gemischten Gramkern besitzen. Bei eingeschränktem Zugriff kann ein schwächerer operationeller Vergleich genügen. Der obige Satz betrifft die Erhaltung aller tatsächlich zugelassenen kohärenten Vergleiche und ist kein Verbot absichtlich unterscheidender Messungen.

Im separat gewählten 832 dimensionalen sequenziellen Modell aus S4 wurden die sechs Kantenabbildungen auf dem vollen 256 dimensionalen Materieraum unabhängig überprüft. Es gilt für jede Kante `K_e†K_e=I−S_e` und `K_eK_e†=2I₉₆`. Die Makrooperation

\[
R=P_+\otimes I+P_-\otimes X
\]

wird durch die in S4 deklarierte U₀ Operation und eine Belegungsaufzeichnung auf allen 44 lokalen Dimensionen bestätigt. Daraus folgt noch kein Nachweis aller ursprünglichen TFPT Phasen oder aller virtuellen Pfade des gleichzeitig eingeschalteten C16 Hamiltonoperators.

## 7. Der mikroskopische Vermittler ist nicht automatisch das ideale U₀ Gatter

### 7.1 Nicht eindeutige SU(4) verträgliche Ausführungen

Der lokale Zustandsraum zerfällt als

\[
\mathbf{10}\oplus\mathbf6_{\rm Materie}\oplus\mathbf6_{\rm Vermittler}.
\]

Die SU(4) verträglichen Unitaries auf diesem Raum besitzen die Freiheit

\[
U(1)\times U(2).
\]

Die symmetrische Zehnerdarstellung trägt eine skalare Phase; die beiden äquivalenten Sechserdarstellungen können durch ein beliebiges 2×2 Unitary gemischt werden. Eine Minimalitätsforderung an den Hilbertraum und die SU(4) Symmetrie wählen daher keine einzige Ausführung. Zusätzliche Anforderungen wie ein festgehaltener Rückkanal oder ein unveränderter Nicht Ereigniszweig können diese Freiheit einschränken, sind aber zusätzliche Bedingungen.

Auch die unveränderte Algebra erzwingt nicht den dimensionslosen Parameter `t/Δ`. Seine unterschiedliche Wahl führt zu verschiedenen messbaren Antworten, obwohl Träger, Klammerkanal und Symmetrie dieselben bleiben.

### 7.2 Exakte Rabi Schranke

Im aktiven Paarsektor reduziert sich der vorhandene Hamiltonoperator auf

\[
h=\begin{pmatrix}0&g\\g&\Delta\end{pmatrix},\qquad g=\sqrt2t.
\]

Mit `Ω_R=√(Δ²+4g²)` ergibt sich

\[
p_{\rm med}(\tau)=
\frac{4g^2}{\Delta^2+4g^2}
\sin^2\left(\frac{\Omega_R\tau}{2\hbar}\right).
\]

Daher

\[
\boxed{p_{\rm med}^{\max}=\frac{8t^2}{\Delta^2+8t^2}<1\qquad(\Delta>0).}
\]

Bei `t/Δ=1/20` ist die maximale vollständige Paarvermittlung nur `1/51`, bei `1/640` `1/51201`. Die ideale Involution U₀ aus S4 transferiert den antisymmetrischen Paarraum dagegen vollständig. **Kein bloßes Warten unter diesem konstanten verstimmten Hamiltonoperator realisiert U₀.**

Das ist kein Ausschluss jeder gesteuerten Synthese des Recordgatters R. Es zeigt präzise, dass die Benutzung von U₀ nicht durch eine passende Wartezeit desselben konstanten H begründet ist. Resonante Steuerung, Belegungsphasen, zusätzliche Kontrollkopplungen oder andere explizite Syntheseverfahren ändern den Ressourcenvertrag.

Ein positiver Teil bleibt: Nach `τ_c=2πℏ/Ω_R` kehrt der Vermittler leer zurück und der antisymmetrische Paarsektor erhält die Phase

\[
z=\exp\left[i\pi\left(1-\frac\Delta{\Omega_R}\right)\right].
\]

So entstehen relative Phasen bereits durch die vorhandene Dynamik. Ihre exakte Nutzung für eine vollständige Schaltung samt Registerkopplung und Genauigkeit ist eine andere Frage als die Existenz einer solchen Phase.

### 7.3 Warum die nichtstabilisierende Ressource weiterhin real ist

Für das idealisierte Recordgatter gilt

\[
R(I\otimes Z)R^\dagger=S\otimes Z.
\]

S ist in der angegebenen Qubitkodierung kein Paulioperator. Ein erlaubter einfacher Quellinput erzeugt nach R genau 13 nichtverschwindende Rechenbasisamplituden; diese Zahl wurde unabhängig mit ganzzahligen Amplituden überprüft. Reine Stabilizerzustände haben eine Unterstützung von Zweierpotenzgröße. Die in S4 formulierte Abgrenzung gegenüber ausschließlich Cliffordoperationen, Stabilizerhilfen und Paulimessungen bleibt daher bestehen [W3].

Nicht die bloße mathematische Niederschrift von R, sondern sein nativer physikalischer Zugriff muss nachgewiesen werden.

## 8. Exakter Filter für den angekleideten mikroskopischen Stern

### 8.1 Das richtige Spektrum

Im ausdrücklich isolierten Viererstern kann aus einem vollen Eingang höchstens ein Vermittler erzeugt werden, weil alle drei Vertizes denselben Mittelpunkt entfernen. Der geschlossene mitgeführte Raum aus S1 besitzt Dimension 544 und

\[
H_\star=\begin{pmatrix}0&tM^\dagger\\tM&\Delta I\end{pmatrix},
\qquad M^\dagger M=6I-2H_{\star,\rm ideal}/J.
\]

Die Eigenwerte von `M†M` sind `d=0,…,6` mit Multiplizitäten

\[
35,90,15,40,45,30,1.
\]

Es gibt 221 aktive obere Richtungen und zusätzlich 67 dunkle Richtungen bei Energie Δ. Die verschiedenen Energien sind

\[
E_d^-=(\Delta-\sqrt{\Delta^2+4t^2d})/2,\qquad d=0,\ldots,6,
\]

\[
E_d^+=(\Delta+\sqrt{\Delta^2+4t^2d})/2,\qquad d=1,\ldots,6,
\]

sowie Δ. Für `t≠0` sind dies 14 verschiedene Niveaus. Das eindeutige Grundniveau ist `E_0=E_6^-`.

Die unabhängige direkte Diagonalisierung aller 544 Dimensionen bestätigt diese Liste und ihre Multiplizitäten bei `t/Δ=0,05` mit maximaler Abweichung unter `1,8·10⁻¹⁵Δ`.

### 8.2 Dreizehn Faktoren statt eines falsch übernommenen Achtpunktfilters

Für jede der 13 anderen Energien `λ>E₀` wähle

\[
\tau_\lambda=\frac{\pi\hbar}{\lambda-E_0},\qquad
F_\lambda(H)=\frac{I+e^{-i(H-E_0)\tau_\lambda/\hbar}}2.
\]

Jeder Faktor lässt den Grundzustand unverändert und vernichtet genau das zu λ gehörige Niveau. Alle Faktoren sind Funktionen desselben H und kommutieren. Daher gilt exakt

\[
\boxed{\prod_{\lambda\ne E_0}F_\lambda(H_\star)=P_{0,\rm dressed}.}
\]

Es wird keine gemeinsame Periodizität aller Energieabstände benötigt. Jeder Faktor ist mit einem im Pluszustand präparierten Kontrollqubit, kontrollierter Entwicklung, einer Referenzphase und einer Plusauslesung als Krausoperator realisierbar. Die übrigen Registerausgänge sind Fehlschläge; sie werden nicht als erfolgreiche Versuche gezählt.

Das ist eine vollständige Lösung der **endlichen mathematischen Filteraufgabe unter diesen Steuerressourcen**, nicht die Herleitung dieser Steuerressourcen aus TFPT. Eine mathematisch exakte kontinuierliche Phase ist außerdem nicht automatisch ein exakt realisierbares endliches Gatterwort eines diskreten Hardwarealphabets.

### 8.3 Zeiten, Ausbeute und Dressierung

Für `Δ=1`, `t=0,05` gelten

\[
E_0=-0.01478150704935,\qquad
\Delta_\star=0.00243396875137003,
\]

\[
w=\frac12\left(1+\frac1{\sqrt{1+24t^2}}\right)
=0.9856429311786321.
\]

w ist das Gewicht des Grundzustands im nackten Materieraum. Die Materiekomponente selbst ist Ω. Der volle Eigenzustand enthält zusätzlich Löcher und Vermittler.

Die längste notwendige Filterentwicklung dauert etwa `1290,7284 ℏ/Δ`. Die Summe der 13 Evolutionszeiten beträgt etwa `3172,8296 ℏ/Δ`, ohne Kosten von Kontrollgattern, Registerinitialisierung und Auslesung.

Die Erfolgswahrscheinlichkeit beträgt vom nackten einfachen Farbprodukt `|0123⟩` aus

\[
p=w/24\approx0.04106845547,
\]

und vom nackten Zweisingulettzustand χ aus

\[
p=w/6\approx0.16427382186.
\]

Die früheren Werte `1/24` und `1/6` dürfen hier also nicht unverändert übernommen werden. Ebenso dürfen ideale Echozahlen nicht ohne eine Definition der Tick und Recordoperationen auf dem vollständigen angekleideten Raum übertragen werden.

### 8.4 Kontrollierte ungenaue Filter

Weiche jeder realisierte Faktor in Operatornorm um höchstens `η_j` vom idealen Faktor ab. Sind alle Faktoren Kontraktionen, folgt durch Teleskopieren

\[
\|\widetilde F-P_0\|\le\eta:=\sum_j\eta_j.
\]

Für einen normierten Eingang mit `p_0=‖P₀ψ‖²` und `η<√p₀` gilt für den bedingten Ausgang

\[
1-F_{\rm conditional}
\le\frac{\eta^2}{(\sqrt{p_0}-\eta)^2}.
\]

Die unbedingte Erfolgswahrscheinlichkeit weicht um höchstens `2η+η²` ab. Dieses Fehlerbudget macht sichtbar, wie Zeit, Phasen und Gatterfehler in die Ausbeute eingehen.

## 9. Gemeinsames sequenzielles Protokoll erneut geprüft

Das in S4 definierte Protokoll ist eine andere, ausdrücklich gewählte Realisierung als der gleichzeitig eingeschaltete C16 Hamiltonoperator oder der angekleidete isolierte Stern. Es verwendet

\[
v_0=|0123\rangle,\qquad
K_\star=P^-_{03}P^-_{02}P^-_{01},\qquad p_N=\|K_\star^Nv_0\|^2.
\]

Die Berechnung auf dem vollen 256 dimensionalen Materieraum reproduziert mit exakten Brüchen:

| Runden N | Präparationsausbeute p_N | Bedingte Ω Fidelität | Echo behalten | Echo frisch, Dreierzyklus |
|---|---:|---:|---:|---:|
| 1 | `1/8` | `1/3` | `0,3984375` | `0,25` |
| 2 | `51/1024` | `128/153` | `0,8393698300` | `0,4434886259` |
| 4 | `175341/4194304` | `524288/526023` | `0,9967024178` | `0,5274997175` |
| 8 | `2932033221441/70368744177664` | `8796093022208/8796099664323` | `0,9999992449` | `0,5312581678` |
| Grenzwert | `1/24` | `1` | `1` | `17/32` |

Die beiden Echospalten sind auf erfolgreiche erste Präparation bedingt. Die unbedingten gemeinsamen Erfolgswerte stehen vollständig in der JSON Datei; im Grenzwert sind es `1/24` und `17/768`.

Die singuläre Konvergenz folgt aus dem ebenfalls unabhängig exakt gerechneten regulären S₄ Polynom

\[
\det(xI-K_\star^\dagger K_\star)
=\frac{x^{12}(x-1)(16x-1)^5(16x^2-9x+1)^3}{2^{32}}.
\]

Damit ist die in S4 angegebene Konvergenzschranke mit `β=(9+√17)/32` bestätigt. Die Schlussprüfung wird nicht durch eine kostenlose ideale Ω Messung ersetzt.

Ein Reset nach Fehlschlägen benötigt die in S4 angegebenen Messungen und Rückkopplungen. Ungelesene Austauschmessungen erhalten dagegen das Ω Gewicht und sind keine Kühlung. Die neue Rechnung hebt diese Unterscheidung nicht auf.

## 10. Was einen tatsächlichen Phasenadapter ausmachen würde

Für vollständig markierte endliche Basen lässt sich ein enger Teil der Adapterfrage exakt formulieren. Haben zwei Operatorfamilien dieselben nichtverschwindenden Matrixelemente und dieselben Beträge, setze auf jeder gerichteten Übergangskante

\[
r_{yx}=\frac{\widetilde K_{yx}}{K_{yx}}\in U(1).
\]

Eine gemeinsame diagonale Basisphase `D=diag(e^{iθ_x})` mit `K̃=DKD†` existiert genau dann, wenn sich `r_yx=e^{i(θ_y−θ_x)}` für alle Übergänge lösen lässt. Äquivalent: Das orientierte Produkt der Phasenverhältnisse entlang jedes geschlossenen Zyklus ist eins.

Der konstruktive Test setzt eine Phase pro Zusammenhangskomponente, propagiert sie über einen Spannbaum und prüft anschließend alle übrigen Kanten. Er muss für dieselbe Markierung, alle Generatoren, Adjungierten und relevanten Sektoren gleichzeitig gelten.

Dieser Satz gilt für den festgehaltenen diagonalen Phasengaugevertrag. Ein negatives Ergebnis ist kein Ausschluss beliebiger anderer nichtdiagonaler Darstellungswechsel. Ebenso reicht ein positiver endlicher Phasentest nicht für die analytischen Domänen, Energieschranken und Grenzwerte von T2.

Die übergebenen Dateien liefern nicht die vollständigen ursprünglichen Vertex und Cocycle Arrays dieses Vergleichs. Die Suche nach den benannten Originalprüfern ergab keinen ausführbaren Originaladapter. Ein verbundener GitHub Bestand wurde gefunden; der konkret referenzierte Pfad des neuen lokalen Audits war dort nicht erreichbar. Daraus wird weder Abwesenheit im gesamten Forschungsbestand noch eine erfolgreiche native Verifikation behauptet.

A6 bleibt deshalb offen. Der unabhängige Prüfcode dieses Pakets rekonstruiert die angegebenen mathematischen Modelle, nicht die fehlenden ursprünglichen Quellphasen.

## 11. Faktorisierung: ein präziserer Ausschluss für die gemessene Fourierroute

### 11.1 Fouriergesetz

Sei G eine ganzzahlige gerade unimodulare E8 Grammatrix und `q(x)=xᵀGx/2`. Der in S2 betrachtete Zustand lautet

\[
|\psi_t\rangle=N^{-4}\sum_{x\in(\mathbb Z/N)^8}e^{2\pi itq(x)/N}|x\rangle.
\]

Nach vollständiger Fourierauslesung gilt mit `d=gcd(t,N)`

\[
\Pr(b)=\begin{cases}(d/N)^8,&d\mid b_j\ \text{für alle acht Koordinaten},\\0,&\text{sonst}.\end{cases}
\]

**Kurzer Nachweis.** Das Betragsquadrat der Fourieramplitude wird durch `h=x−y` zu einer Charaktersumme. Die Summierung über y verschwindet, außer wenn `tGh=0 mod N`. Unimodularität ergibt `h=(N/d)z`. Wegen der Ganzzahligkeit von q verschwindet die verbleibende quadratische Phase modulo N. Die Summe über z liefert genau die Indikatorbedingung `d|b_j` und den Faktor `d^8`. Die argumentierte Ganzzahligkeit gilt auch für gerade N.

Die neuen unabhängigen FFT Kontrollen umfassen sämtliche Takte für `N=2,3,4,5`. Der allgemeine Satz beruht auf der Charakterrechnung, nicht auf diesen kleinen Zahlen.

### 11.2 Effizienter klassischer Simulator

Die genaue Verteilung kann ohne Quantenzustandspräparation erzeugt werden:

```text
Berechne d = gcd(t,N).
Ziehe acht unabhängige ganze U_j gleichverteilt aus 0,…,N/d−1.
Gib b_j = d U_j aus.
```

Der Aufwand ist polynomial in der Bitlänge von N. Werden spätere Takte durch einen klassischen Algorithmus aus bereits gemessenen Ergebnissen gewählt, kann der gleiche Simulator die vollständige Folge induktiv mit derselben gemeinsamen Verteilung erzeugen. Das gilt für jede polynomial lange Folge dieser Experimente und eine polynomial aufwendige klassische Steuerung.

**Folgerung:** Genau diese gemessene E8 Fourierroute stellt keine zusätzliche Quantenressource bereit. Das ist stärker als die Aussage, dass eine einzelne Verteilung bei teilerfremdem Takt gleichförmig ist.

Der Satz gilt nicht für eine kohärente Überlagerung der Takte mit weiteren Operationen vor der Messung, andere Präparationen oder ein allgemeines E8 Rechenmodell. Eine solche Alternative müsste neu spezifiziert und einschließlich aller Kosten analysiert werden.

### 11.3 Momentgewinnung bleibt die teure Stelle

Für versprochenes `N=pq` mit verschiedenen Primzahlen und `s=p+q` erfüllt

\[
M_4=\sum_{t=0}^{N-1}\gcd(t,N)^4
\]

die Identität

\[
s^4-Ns^3-4Ns^2+(3N^2+1)s+M_4-N^4+2N^2-N-1=0.
\]

Die Beispiele `15,35,143,899` wurden aus N und dem durch N ggT Aufrufe gewonnenen Moment invertiert. Die Faktoren werden zur Kontrolle, nicht als Eingang der Inversion verwendet. Aber bereits die Momentgewinnung ist exponentiell in `log N`, und jeder zwischendurch gefundene nichttriviale ggT verrät selbst einen Faktor.

Die bekannte positive Referenz bleibt Shors Verfahren mit kohärenter modularer Exponentiation und Periodenauslesung [W4]. Dieses Paket enthält keinen neuen Algorithmus mit vergleichbarem oder besserem Skalierungsbeweis.

## 12. RH: die arithmetische Identität bleibt der fehlende Schritt

Die in S2 definierte Weil Form lautet bei festgehaltener Mellinnormierung

\[
Q_\zeta(g)=\sum_\rho G(\rho)\overline{G(1-\bar\rho)}.
\]

Gesucht wäre eine unabhängig definierte positive Darstellung

\[
Q_\zeta(g)=\|Ag\|^2
\]

auf dem ganzen vorgeschriebenen Testraum. Sie muss sämtliche Normierungen, Randterme und gemischten Beiträge der expliziten Formel erhalten. Ein positives endliches C16 Gramobjekt ist nicht automatisch diese signierte arithmetische Form. Die Literatur zum Weil Kriterium und zu besonderen archimedischen Fällen bestätigt diesen Rahmen, nicht einen hier fehlenden allgemeinen Abschluss [W2].

### 12.1 Vollständiges Schurkriterium

Für einen möglicherweise singulären Block A gilt

\[
\begin{pmatrix}A&B\\B^\dagger&D\end{pmatrix}\ge0
\]

genau dann, wenn

\[
A\ge0,\qquad(I-AA^+)B=0,\qquad D-B^\dagger A^+B\ge0.
\]

Die mittlere Bildraumbedingung darf nicht entfallen. Das exakt geprüfte Gegenbeispiel

\[
A=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
B=\begin{pmatrix}0\\1\end{pmatrix},\quad D=1
\]

besitzt einen positiven scheinbaren Schurrest, aber die Gesamtmatrix ist indefinit.

Kompatible vollständige endliche Blöcke, ihre korrekte Schurkopplung und eine dichte stetige Fortsetzung würden eine positive Grenzform liefern. Zusätzlich müsste diese Grenzform aber nachweislich die vollständige Weil Form sein. Genau diese arithmetische Identität und die Positivität über sämtliche Stufen wurden aus den TFPT Daten hier nicht hergeleitet.

**Ergebnis zu B1:** Der Vertrag ist präzisiert und gegen falsche Schlüsse kontrolliert. Ein RH Beweis liegt in dieser Fortsetzung nicht vor. Die neue Bandrechnung ersetzt die fehlende arithmetische Gleichheit nicht.

## 13. Vollständige Zuordnung der Aufgaben aus S0

### 13.1 Rekonstruktion A1 bis A8

| Aufgabe | Ergebnis dieser Arbeit | Was nicht geschlossen ist |
|---|---|---|
| A1, native Auswahl | Explizite `U(1)×U(2)` Freiheit und messbar verschiedene Kopplungsantworten zeigen die verbleibende Unterbestimmung. | Auswahl von t/Δ, Statistik, Markierungen, globaler Familie und Zugriffsrechten aus derselben primitiven Quelle. |
| A2, globale Kohärenz | Notwendiger und hinreichender gemeinsamer Gramvertrag; sechs Kanten und vollständige Recordmakrooperation erneut geprüft. | Alle nativen Generatoren und zusammengesetzten TFPT Wörter, insbesondere der tatsächliche nichtstabilisierende Zugriff. |
| A3, Lokalität | Global geteilte Moden mit festem t besitzen keine extensive untere Energieschranke; lokale Zellmoden besitzen eine solche. | Native Auswahl und konkreter Transportgraph; der Kontinuumsgrenzwert folgt nicht aus Stabilität allein. |
| A4, Rest und Sektoren | Bandtrennung bei 1/20 rigoros; Rest sechster Ordnung und spektraler Fehler bis vierter Ordnung explizit; alle 64 führenden Sektoren numerisch untersucht. | Rigorose innere Spektralordnung und brauchbare Restkontrolle bei 1/20; größenuniformer Vielzellenbeweis. |
| A5, Dressierung | Exakter 13 Faktor Filter des isolierten mikroskopischen Sterns mit Ressourcen und Ausbeute. | Native Bereitstellung seiner Kontrollen und Anwendung auf das unverändert gekoppelte Gesamtmodell. |
| A6, Phasenadapter | Präziser gemeinsamer Gauge und Zyklustest formuliert. | Originale phasenmarkierte Arrays und tatsächlicher erfolgreicher Transport. |
| A7, Naht | Abstrakte E8 Vertexalgebra bleibt von ihrer nativen chiralen Ausführung getrennt. | Domänen, Energieabschätzungen, beide Adjungierten und derselbe Skalierungsgrenzwert. |
| A8, Reproduktion | Die neuen Rechnungen sind mit Code, Ergebnissen, Eingabehashes und Replaybefehlen beigefügt. | Kein vollständiger Neubau aller historischen Originalprüfer, keine Behauptung über lokale nicht synchronisierte Repositorydateien. |

### 13.2 Anwendungen B1 bis B4

B1 bleibt die vollständige arithmetische Positivitätsidentität. B2 erhält einen stärkeren Ausschluss der konkret gemessenen Fourierroute, aber keinen neuen schnellen Algorithmus. B3 erhält tatsächlich ausgeführte Hamiltonspektren, F₄ Antworten und vollständige endliche Echostatistiken. B4 bleibt wichtig: Rechenkomplexität, RH und Physik sind getrennte Beweisziele. Eine erfolgreiche mikroskopische Theorie würde sie nicht ohne zusätzliche Sätze gemeinsam lösen.

Die Spektren erlauben konkrete Modellunterscheidung. Der ideale Tetramer besitzt Gap `2J`, der ideale Stern `J/2`, der angekleidete Stern die Wurzeldifferenz aus Abschnitt 8. Identischer Ω Zustand bedeutet nicht identischer Hamiltonoperator. Die Records erlauben ihrerseits eine Diagnostik erreichbarer Kohärenz unter genau festgehaltenen Eingriffen.

### 13.3 Physikalische Tore T1 bis T8

| Tor | Präziser verbleibender Abschluss |
|---|---|
| T1 | Eine primitive Quelle muss nicht nur Vertizes erlauben, sondern Architektur, Parameter, Statistik und physische Zugriffe auswählen. Die heutigen Gegenfamilien zeigen, welche Zusatzdaten tatsächlich noch wirken. |
| T2 | Die abstrakte E8 Algebra muss durch denselben nativen chiralen Prozess mit wohldefinierten verschmierten Feldern, Domänen und Skalierung realisiert werden. Ein 2+1 Bulk mit 1+1 Rand ist nicht automatisch eine 3+1 Ableitung. |
| T3 | Die lokale Zellregel muss eine ausgewählte globale Größenfamilie und tatsächlich propagierende Sektoren mit gemeinsamem Lorentzkegel erzeugen. Unterschiedliche `Z^d` Verklebungen können denselben lokalen Zellbaustein benutzen. |
| T4 | Ein physischer interner Diracoperator muss genau drei gewünschte propagierende Familien, ihr Maß und die Entkopplung der Spiegel liefern. Die feste Belegung von Spinorgewichtsplätzen ist nicht unter beliebigen kontinuierlichen Spin(10) Mischungen invariant. |
| T5 | Die neue endliche Bandtrennung ist ein Fortschritt, aber noch kein größenuniformer lokaler Kontinuumsgrenzwert mit Wechselwirkungen und Streuung. Eine überall strikt gapped Produktphase liefert die verlangten masselosen Moden gerade nicht. |
| T6 | Kopplungen, Yukawas, Neutrinos, Massenschema, Schwellen, absolute Skalen und Unsicherheiten müssen durch denselben Transfer bestimmt werden. Keine nachträglichen freien Korrekturen ungünstiger Zahlen. |
| T7 | Ein abgeleiteter Korrelator muss einen positiven masselosen Spin 2 Pol mit zwei physischen Helizitäten, Ward Identitäten und universeller Kopplung besitzen. Die Determinante einer hermiteschen 2×2 Matrix erzeugt diesen Pol nicht. |
| T8 | Anfangszustand, Reservoir, Registerversorgung und kosmologisches Funktional müssen ausgewählt werden. Das endliche kontrollierte Präparationsverfahren ist kein autonomer kosmischer Attraktor; die verwendete Born Regel ist Voraussetzung. |

Die Probleme werden durch die neuen Resultate enger, aber keines dieser Tore darf als Gesamtforderung nur wegen eines erfolgreichen endlichen Untertests umgestellt werden.

### 13.4 Parameter und finale Querfragen

Die aus S1, S2 und S6 übernommenen historischen Vergleiche bleiben historisch: Der Formelwert `α⁻¹≈137,0359992168407` liegt gegenüber der dort ausdrücklich genannten CODATA Referenz 2022 um etwa 1,897 experimentelle Standardunsicherheiten höher. Diese Arbeit führt keinen neuen Transfer zur Thomson Kopplung und keinen aktuellen globalen Datenfit aus.

Ebenso bleiben die dokumentierten Abweichungen bei Leptonverhältnissen, im älteren Higgszweig und bei Protonlebensdauern bestehen. Bei Inflation gilt die Präzisierung aus S6: Der negative Punkt `N=51,4` widerlegt nicht den gesamten vorgeschlagenen Bereich `N=50,…,60`. Die Wahl `N≈56,13124` anhand einer eingesetzten Amplitude ist aber eine Kalibrierung, keine neue unabhängige Vorhersage.

Dunkle Materie benötigt einen konkreten stabilen Sektor, seine Kopplungen und kosmologische Produktion. Ein bloß ungelesenes Register ist kein solcher Nachweis. Materieüberschuss benötigt eine quantitative Erzeugungsrechnung. Starke CP benötigt den Schutz des tatsächlichen fermionischen Maßes einschließlich Massenphasen. Schwarze Löcher benötigen zuerst den gravitativen Sektor und danach Entropie, Verdampfung und Informationstransfer.

Für dunkle Energie lässt sich die verbleibende Freiheit besonders einfach demonstrieren: Der globale Zusatz `H→H+cI` ändert die normierten nichtgravitativen Zustands und Prozesswahrscheinlichkeiten eines vollständig betrachteten geschlossenen Systems nicht. Er verschiebt aber dessen absoluten Energiereferenzwert. Die heutigen endlichen nichtgravitativen Schatten wählen daher keine eindeutige absolute Vakuumenergiedichte. Eine physische gravitative Kopplung samt ihrem Zustand und radiativ stabiler Vakuumrechnung muss diese fehlende Verbindung leisten. Dies ist kein allgemeines Verbot kontrollierter relativer Energiemessungen; ein globaler Zusatz zum gesamten geschlossenen System ist von einer nur auf einen kontrollierten Zweig angewandten Energieänderung zu unterscheiden.

## 14. Reproduktion und Integrität

Das Paket enthält:

* `verify.py`: endliche ganzzahlige und rationale Prüfungen sowie klar bezeichnete numerische Kontrollen.
* `singlet_probe.py`: unabhängiger Singulettlauf, Symmetrieantworten und vollständige F₄ Kompression.
* `all_sectors_probe.py`: Suche nach niedrigen Eigenpaaren in allen 64 SU(4) Sektoren.
* `char_probe.py`: exakte Charakterrechnung; die S₁₆ Charakterzeile wird durch exakte Orthogonalität kontrolliert.
* JSON Dateien mit sämtlichen Ergebnissen und ein Manifest der ursprünglichen Eingaben.

Ausführung im entpackten Verzeichnis:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verify.py --output verification.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -OO verify.py --output verification_optimized.json
cmp verification.json verification_optimized.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python singlet_probe.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python all_sectors_probe.py
python char_probe.py
python young_controls.py
```

Die normale und optimierte Ausführung des endlichen Prüfers liefern byteidentische JSON Ausgaben. Die Prüfentscheidungen verwenden keine durch Python Optimierung entfallenden `assert` Anweisungen.

Ein zusätzlicher unabhängiger Vergleich (`young_controls.py`) rekonstruiert das gesamte Spektrum eines ungleich gewichteten Vierträgermodells sowohl im direkten 256 dimensionalen Tensorraum als auch über alle Youngblöcke. Die größte Abweichung beträgt `9,24·10⁻¹⁴`. Zusätzlich wurden die Coxeterrelationen der benachbarten Transpositionen an normierten Testvektoren für vier, acht und sechzehn Träger kontrolliert.

Die 64 Sektorrechnungen sind unabhängig von den ursprünglichen TFPT Quellprüfern. Sie benutzen dieselbe hier aus den Formeln rekonstruierte Youngdarstellung wie die separate Singulettrechnung, also nicht zwei voneinander unabhängige Implementierungen dieser Darstellung. Bei einem erneuten numerischen Lauf können letzte Nachkommastellen abhängig von Bibliotheken und Hardware variieren.

Es wurden weder die tatsächliche native TFPT Phasenfamilie noch ein RH Ledger, ein Lean Beweis, Hardware oder die vollständige physikalische Renormierung ausgeführt. Die zugehörigen Statusfelder bleiben ausdrücklich negativ beziehungsweise offen.

## 15. Gesamturteil

Die endliche mikroskopische Verbindung ist durch die neue Bandtrennung, explizite Restkontrolle, sämtliche führenden Sektorsuchen und den angepassten Filter tatsächlich weiter geschlossen. Die globale Vermittlerarchitektur ist unter einer geforderten extensiven Stabilität nicht mehr eine beliebige offene Gabel. Der Unterschied zwischen einem idealen Recordgatter und seiner behaupteten mikroskopischen Ausführung ist jetzt durch eine exakte Übergangsschranke messbar.

Die noch fehlende gemeinsame Lösung liegt dagegen weiterhin in der Auswahl und Identifikation: dieselben nativen Phasen, dieselben erlaubten Steuerungen, dieselbe lokale Größenfamilie, dasselbe Zustandsfunktional und ihre überprüfbaren physikalischen beziehungsweise arithmetischen Ausgaben. Eine neue positive Bandabschätzung ist dafür ein Baustein, kein Ersatz.

## Externe Primärliteratur

Die folgenden Arbeiten liefern den allgemeinen methodischen Rahmen. Sie bestätigen nicht die neuen speziellen TFPT Konstanten oder einen vollständigen Theorieabschluss.

[W1] S. Bravyi, D. P. DiVincenzo, D. Loss, *Schrieffer–Wolff transformation for quantum many body systems*, Annals of Physics 326 (2011), arXiv:1105.0675. https://arxiv.org/abs/1105.0675

[W2] A. Connes, C. Consani, *Weil positivity and trace formula, the archimedean place*, arXiv:2006.13771. https://arxiv.org/abs/2006.13771

[W3] S. Aaronson, D. Gottesman, *Improved Simulation of Stabilizer Circuits*, Physical Review A 70 (2004), arXiv:quant-ph/0406196. https://arxiv.org/abs/quant-ph/0406196

[W4] P. W. Shor, *Polynomial Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer*, SIAM Journal on Computing 26 (1997), arXiv:quant-ph/9508027. https://arxiv.org/abs/quant-ph/9508027
