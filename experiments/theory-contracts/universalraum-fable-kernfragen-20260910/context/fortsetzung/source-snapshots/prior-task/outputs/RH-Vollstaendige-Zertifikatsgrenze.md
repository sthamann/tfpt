# Die volle eingefrorene RH-Schalenlast scheitert: ein strenger Gegenzeuge

10. September 2026. Ergebnis: **REFUTED_SCOPED** für genau das unten
definierte vollständige native untere Zertifikat. Keine Widerlegung der
Weil-Positivität, keine RH-Entscheidung, keine globale Unmöglichkeitsaussage.

## 1. Exakter Gegenstand und Aussage

Setze

\[
 a=9/8,\quad b=6/5,\quad I=(-a,a),\quad J=(-b,b),\quad S=J\setminus I,
 \quad \delta=b-a=3/40,\quad\mu_0=10^{-100}.
\]

Alle Formen und Matrizen tragen unverändert die ursprüngliche
Weil-Normalisierung. Insbesondere ist die orthonormale physische Basis

\[
 \ell_n(x)=\sqrt{(2n+1)/(2a)}\,P_n(x/a),\qquad x\in I.
\]

Die eingefrorenen nativen Daten sind die vollständigen 320×80 Antwortspalten
\(W=Y-Z_0\), die positive 80×80 Matrix

\[
 M=\widetilde F-V-\tau Y^*Y,
 \qquad
 V=\widetilde E^*Z_0+Z_0^*\widetilde E-Z_0^*C_sZ_0,
\]

und die ganze positive Hochraumform \(C_s\ge(21/256-\mu_0)I\).
Das gleichnamige gemischte Zwischenprodukt \(U^*\widetilde E\) aus dem
früheren Assembly-Beweis wird **nicht** als diese Matrix M verwendet.

Mit dem vollständigen ursprünglichen Kreuzoperator \(X\) und
\(E=Q_{160}X\) lautet das zu prüfende Zertifikat

\[
 K(v)=8(W^*Xv)^*M^{-1}(W^*Xv)+8\langle Ev,C_s^{-1}Ev\rangle
 \ \le\ d_{\rm new}(v)=Q_S(v)-\mu_0\|v\|^2.                 \tag{1}
\]

**Satz für diese eingefrorenen Daten.** Der folgende einzelne rationale
Polynomzeuge \(v=1_SF\) verletzt (1). Bereits der erste positive Summand
ist größer als \(7.7\,d_{\rm new}(v)\). Insbesondere kann keine korrekte
Oberabschätzung derselben Last, bei irgendeinem Hochraum-Cutoff, (1)
bestätigen. Der Beweis braucht den zweiten positiven Summanden nicht
numerisch zu bestimmen.

Dies ist stärker als die schon bekannte Widerlegung
\(K\le(7/10)I\): Hier steht rechts die **vollständige wirkliche
Schalenergie**, nicht ihr konstanter unterer Boden.

## 2. Vollständig expliziter Zeuge und Formbereich

Auf J sei

\[
 F(x)=10^{-14}\sum_{j=0}^{9}n_jP_{2j+1}(5x/6),
\]

außerhalb J sei F null. Die ganzzahligen Koeffizienten sind der Reihe nach

```text
-44219800572275, 110963400480351, -119085514084369,
 77887040635077, -33368219264952, 9084763280613,
-1230048665750, -91264501485, 69205978538, -9641766922.
```

Dieser unveränderte Zeuge steht schon in
`work/fable-rh-continuation/witness.json`; die neue Rechnung bestimmt
seine tatsächliche Kopplung an die inzwischen eindeutig zugeordneten
ursprünglichen W/M-Daten.

F, \(f=1_IF\) und \(v=1_SF\) sind ungerade, beschränkt, kompakt
getragen und stückweise polynomial. Bei kleinen Verschiebungen u ist
\(\|v-v(\cdot-u)\|_2^2=O(u)\): außerhalb endlich vieler Streifen um
die Sprungstellen liefert die beschränkte Ableitung sogar O(u²), und
die Streifen haben Maß O(u). Mit \(k(u)\sim1/(2u)\) folgt endliche
vollständige logarithmische Gammaenergie. Die Sprünge sind daher im
richtigen Formbereich zulässig. Es wird kein H¹-Formbereich unterstellt.

## 3. Originale Form und vollständige räumliche Integration

Für reelle ungerade kompakt getragene g mit
\(C_g(u)=\int g(x)g(x-u)\,dx\) und \(N=C_g(0)\) ist die native Form

\[
 Q(g)=2\int_0^\infty k(u)[N-C_g(u)]\,du+a_0N
      -2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}C_g(\log n)
      -2\left(\int e^{x/2}g(x)\,dx\right)^2,             \tag{2}
\]

\[
 k(u)=\frac{e^{-u/2}}{1-e^{-2u}},\qquad
 a_0=-\gamma-3\log2-\pi/2-\log\pi.
\]

Die Summe in (2) enthält auf J genau
\(n=2,3,4,5,7,8,9,11\); \(\log12>2b\) wird im Checker streng
geprüft. Auf S bleiben nur die tatsächlichen überlappenden
Korrelationen; insbesondere wird der Prime-11-Beitrag integriert.

Schreibe \(\lambda_j=2j+1/2\) und für ganze \(s\ge2\), \(t\ge0\)

\[
 H_s(t)=\sum_{j\ge0}\frac{e^{-\lambda_jt}}{\lambda_j^s}.
\]

Alle hier verwendeten Reihen sind absolut konvergent und ohne Nullstellendaten
definiert. Die ausgewerteten Identitäten sind

\[
 H_s(0)=2^{-s}\zeta(s,1/4),\quad
 H_s(t)=2^{-s}e^{-t/2}\Phi(e^{-2t},s,1/4)\quad(t>0).       \tag{3}
\]

Hier ist \(\Phi\) die Lerch-Transzendente, nur bei reellem Argument
zwischen 0 und 1 und positiven Parametern. Die Implementierung verwendet
Arb/FLINT-Bälle über die dokumentierte
[python-flint-Schnittstelle](https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.lerch_phi)
und die [FLINT-Definition](https://flintlib.org/doc/acb_dirichlet.html#lerch-transcendent).
FLINT darf intern zwischen validierter direkter Reihe und
Konturintegration wählen. Es gibt hier keine räumliche Stichprobenquadratur,
keine kritischen Nullstellen, kein angenähertes
Abschneiden der Reihe ohne Rest und keine Annahme ihrer Zielpositivität.

### Vollständige Gamma-Kreuzantworten

Für ein beliebiges ungerades Polynom p auf I gilt

\[
 \langle p,X_\Gamma v\rangle
 =-2\sum_{j\ge0}
       \left(\int_{-a}^{a}p(x)e^{\lambda_jx}\,dx\right)
       \left(\int_a^b F(y)e^{-\lambda_jy}\,dy\right).      \tag{4}
\]

Der Faktor 2 kommt von den zwei durch Spiegelung gleichen Schalenarmen;
die Integration über ganz I erhält auch alle gegenseitigen Fernbeiträge.
Endlich oft partielle Integration liefert exakt

\[
 \int_{-a}^{a}p(x)e^{\lambda x}\,dx
 =\sum_{r=0}^{\deg p}\frac{(-1)^r}{\lambda^{r+1}}
   [e^{\lambda a}p^{(r)}(a)-e^{-\lambda a}p^{(r)}(-a)],
\]

\[
 \int_a^bF(y)e^{-\lambda y}\,dy
 =\sum_{s=0}^{19}\frac{1}{\lambda^{s+1}}
   [e^{-\lambda a}F^{(s)}(a)-e^{-\lambda b}F^{(s)}(b)].
\]

Setzt man diese beiden endlichen Identitäten in (4) ein, entsteht für
jedes r,s der Ausdruck

\[
 -2(-1)^r\{p^{(r)}(a)F^{(s)}(a)H_{r+s+2}(0)
 -p^{(r)}(a)F^{(s)}(b)H_{r+s+2}(\delta)
 -p^{(r)}(-a)F^{(s)}(a)H_{r+s+2}(2a)
 +p^{(r)}(-a)F^{(s)}(b)H_{r+s+2}(a+b)\}.                \tag{5}
\]

Für \(p=\ell_n\) werden
\(p^{(r)}(-a)=(-1)^{r+1}p^{(r)}(a)\) und

\[
 \ell_n^{(r)}(a)=\sqrt{\frac{2n+1}{2a}}
       \frac{(n+r)!}{2^r r!(n-r)!a^r}
\]

verwendet. Somit berechnet (5) ohne räumliche Approximation alle 160
ungeraden Antwortkoeffizienten bis Grad319, die für das ganze W benötigt
werden. Die hohen inneren Auslöschungen werden mit 4096 bzw.5120 Bit
und ihren vollständigen Intervallradien bezahlt.

### Vollständige Prim- und Pol-Kreuzantworten

Für jedes alte Primzahlpotenzereignis mit \(t=\log n\) gilt
\(\delta<t<2a\). Daher ist das vollständige übersetzte positive
Schalenintervall \([a-t,b-t]\) in I enthalten, und

\[
 \langle p,X_{\rm prime}v\rangle
 =-2\sum_{n=2,3,4,5,7,8,9}\frac{\Lambda(n)}{\sqrt n}
     \int_a^b p(y-\log n)F(y)\,dy.                     \tag{6}
\]

Das sind endlich viele Polynom-Integrale mit intervallgenauem log n.
Die Legendre-Rekursion in der auf [-1,1] normierten Schalenkoordinate
vermeidet unnötige monomiale Auslöschung. Da \(\log11>a+b\), hat der
Prime-11-Kanal exakt keinen I/S-Kreuzterm; sein Diagonalterm bleibt in (2).

Mit \(m_g=\int e^{x/2}g(x)dx\) ist die ungerade Polkopplung

\[
 \langle p,X_{\rm pole}v\rangle=-2m_pm_v.              \tag{7}
\]

Die Exponentialmomente werden über die endliche Polynomlösung
\(A'+A/2=F\) bzw. die oben ausgeschriebene Endpunktformel berechnet.
Die Konstante \(a_0\) und die Verschiebung \(\mu_0\) haben auf
disjunkten Trägern keinen Kreuzterm.

### Exakte ganze Schalenergie

Die Korrelation von v ist auf den durch
\(0,\delta,2a,a+b,2b\) getrennten Teilintervallen ein exakt rationales
Polynom. Der Checker konstruiert diese Polynome direkt aus sämtlichen
Intervallpaaren und prüft ihre Stetigkeit und das verschwindende äußere Ende.

Für \(J_0(u)=\int_u^\infty k(t)dt=\sum_j e^{-\lambda_ju}/\lambda_j\)
ergibt partielle Integration

\[
 Q_\Gamma(v)=-2\int_0^{2b}C_v'(u)J_0(u)du.
\]

Die Randterme verschwinden: \(C_v(u)-N=O(u)\) bei null, während
\(J_0(u)=O(|\log u|)\); außerhalb des Korrelationssupports fällt
\(J_0\) exponentiell. An inneren Teilpunkten heben sich die Randterme
wegen Stetigkeit der Korrelation auf. Die benötigten Monom-Momente sind

\[
 \int_l^h u^mJ_0(u)du
 =m!\sum_{k=0}^m
   \frac{l^kH_{m+2-k}(l)-h^kH_{m+2-k}(h)}{k!}.         \tag{8}
\]

Formeln(2),(3),(8) liefern die ganze Schalform einschließlich beider
Interfaces, Fernkopplung, Prime11 und negativem ungeradem Polterm.

## 4. Originaldaten, vollständige endliche Last und strenge Zeichen

Die Originalprodukte enthalten einerseits den gewichteten unteren Block
\(S_M=M-\Pi\) und die gesamte gewichtete Last \(\Pi\), andererseits
den flachen unteren Block \(M-G_0/c\) und das gesamte G_0. Daher bilden
beide Quellformeln **dieselbe definierte** Matrix M:

\[
 M=S_M+\Pi=(M-G_0/c)+G_0/c.
\]

Der Checker baut beide Ballmatrizen auf und prüft ihren eintragsweisen
Overlap als Konsistenzkontrolle. Der Overlap allein wäre kein Beweis
einer Identität zweier unabhängiger Matrizen; die Identität folgt aus den
angegebenen Originaldefinitionen. Alle ursprünglichen Fehlerladungen und
gemischten Produkte bleiben enthalten.

Das unveränderte vollständige rationale 80×80 Frame C aus dem nativen
Datensatz hat 1536-Bit-dyadische Einträge. Frisch wird nachgerechnet

\[
 \|C^*MC-I\|_\infty<10^{-6}=\eta,
 \quad (1-\eta)I<C^*MC<(1+\eta)I.                     \tag{9}
\]

Die tatsächliche berechnete Zeilensummen-Obergrenze ist ungefähr
\(4.322\cdot10^{-132}\). Die stärkere kleine Dezimalzahl wird für
den Beweis nicht benötigt. Da C quadratisch ist, beweist (9) auch seinen
vollen Rang und die Positivität von M; es wird kein kleiner Modus gelöscht.

Setze \(h_n=\langle\ell_n,Xv\rangle\), \(g=C^*W^*h\). Exakte
Kongruenz und Inversenordnung ergeben

\[
 (W^*Xv)^*M^{-1}(W^*Xv)
 =g^*(C^*MC)^{-1}g
 \ge\frac{\|g\|^2}{1+\eta}.                          \tag{10}
\]

Hier ist h lediglich der vollständige für W nötige Koordinatenvektor:
weil W exakt bis Grad319 unterstützt ist, lässt \(W^*h\) keinen
W-Beitrag aus. Die unendliche Hochraumantwort wird nicht als endlich
ersetzt. Ihre inverse Energie ist nichtnegativ und wird allein für
diese **untere** Lastschranke weggelassen.

Die beiden reproduzierten Ballrechnungen ergeben:

| Größe | Zertifizierte Größenordnung |
|---|---:|
| \(\|v\|^2\) | \(5.36178621791418\ldots\cdot10^{-10}\) |
| \(Q_J(F)\) | \(5.83043450799034\ldots\cdot10^{-14}>0\) |
| \(Q_S(v)\) | \(1.08275417946503\ldots\cdot10^{-9}\) |
| untere Schranke \(L=8\|g\|^2/(1+10^{-6})\) | \(8.40479012369746\ldots\cdot10^{-9}\) |
| \(L/Q_S(v)\) | \(7.76241762266858\ldots\) |

Für den Ausschluss genügen die tatsächlich streng geprüften rationalen
Schranken

\[
 Q_S(v)<1083\cdot10^{-12},\quad
 L>8404\cdot10^{-12},\quad
 L>(77/10)d_{\rm new}(v).
\]

Aus \(K(v)\ge L>Q_S(v)>d_{\rm new}(v)\) folgt der behauptete
Gegenzeugensatz. Die Verschiebung \(\mu_0\|v\|^2\) wird exakt
mitgeführt und würde den Ausschluss nur noch verstärken.

Als unabhängige Normierungs- und Vorzeichenkontrolle integriert der
Checker auch \(Q_I(f)\) aus seiner eigenen rationalen Korrelation und
expandiert das ursprüngliche f exakt in der alten Legendre-Basis.
Der Rest der vollständigen Polarisierungsidentität

\[
 Q_J(F)-Q_I(f)-Q_S(v)-2\langle f,Xv\rangle=0
\]

liegt bei 4096 Bit in \(\pm6.01\cdot10^{-1186}\), bei5120 Bit in
\(\pm3.89\cdot10^{-1494}\). Diese Kontrolle ergänzt den ausgeschriebenen
Beweis; bloße numerische Überlappung ersetzt ihn nicht.

## 5. Was mindestens repariert werden müsste

Für eine neue untere alte Schranke mit denselben W und M,

\[
 Q_I(Wu+w)-\mu_0\|Wu+w\|^2
 \ge c_{\rm low}u^*Mu+c_{\rm high}\langle w,C_sw\rangle,
 \qquad c_{\rm low},c_{\rm high}>0,
\]

wäre die entsprechende Last
\((1/c_{\rm low})(W^*Xv)^*M^{-1}(W^*Xv)+
(1/c_{\rm high})\langle Ev,C_s^{-1}Ev\rangle\).
Schon der erste Summand erzwingt für einen möglichen Erfolg

\[
 c_{\rm low}\ge
 \frac{(W^*Xv)^*M^{-1}(W^*Xv)}{d_{\rm new}(v)}
 \ge\frac{L}{8d_{\rm new}(v)}
 >0.9703022.                                             \tag{11}
\]

Dies verlangt mindestens etwa die7.762-fache Verbesserung gegenüber
\(c_{\rm low}=1/8\), bei unveränderten W/M-Koordinaten. Es ist eine
notwendige Bedingung, keine Existenzbehauptung einer solchen scharfen
unteren Schranke; die positive Hochraumlast würde zusätzlich bezahlt.
Bei geändertem W oder M muss der Vergleich neu aufgebaut werden.

Alternativ wäre die tatsächliche alte inverse Antwort mit einem echten
richtungsabhängigen Fehlerrest zu bestimmen. Der native untere alte
Operator und der wahre alte Operator dürfen dabei nicht gleichgesetzt
werden: ihre Inversenlasten sind im Allgemeinen verschieden. Das
Scheitern des unteren Zertifikats lässt das Vorzeichen der ursprünglichen
vollen Weilform offen. Der hier benutzte ganze F hat sogar strikt
positive Weilenergie.

## 6. Reproduktion, Provenienz und Grenze

Der Checker `check_full_load.py` setzt ein hartes CPU-Limit von240Sekunden.
Er berechnet jeweils genau denselben Zeugen; kein Sweep, keine GPU,
keine alte Kampagne, keine Ursprungsdatei wird verändert. Die beiden
akzeptierten Läufe dauerten rund14.3 und27.1Sekunden.

```sh
python3 work/universal-return/rh/check_full_load.py --precision 4096
python3 -O work/universal-return/rh/check_full_load.py --precision 5120 --output full_load_certificate_5120_optimized.json
```

Die vorhandene lokale Abhängigkeit ist python-flint0.9.0 unter
`/Users/stefanhamann/Documents/Codex/2026-09-10/scha/work/fable-rh-continuation/deps`.
Der System-Python3.14 wurde verwendet. Prüfungen sind explizite
Ausnahmen, keine durch `-O` entfernbaren `assert`-Anweisungen.

Die JSON-Resultate enthalten die SHA256-Pins der Originaldaten und aller
geerbten Daten-/Rezeptquellen. Diese Pins werden vor der Rechnung
gegen die nativen Receipts und am Ende gegen die unveränderten Dateien
geprüft. Das native ursprüngliche M wurde aus seinen gespeicherten
validierten Produkten rekonstruiert; diese älteren räumlichen Produkte
wurden hier nicht erneut integriert. Die neuen Kreuz- und Schalenergien
wurden dagegen aus den in diesem Beweis hergeleiteten Formeln frisch
integriert. Wiederholung und Quellenhashes sind kein formaler Lean-Beweis
und keine vollständige unabhängige Revision sämtlicher Vorgängertheoreme.

Wesentliche Originalquellen unter
`/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/`:

1. `rh_arithmetic_relative_correction_20260909/PROOF.md`, Zeilen10–39:
   richtige positive M-Definition; Zeilen117–137: vollständiges rationales
   Frame. Daten: `result_initial.json`, `selection.full_rational_frame`.
2. `rh_whole_odd_coercivity_20260909/PROOF.md`, Zeilen5–46:
   physische Normierung, W/M und ganze Formräume; Zeilen85–114: der
   ursprüngliche1/8-Split. `coercivity.py`, `load`: exakter W-Aufbau.
3. `rh_odd_saturation_20260908/saturation_core.py`, `odd_graph` und
   `response`: exakt dieselben Vorzeichen, dyadischen Einträge und
   Gradunterstützungen. Produkte: `fast_state/initial.stdout` sowie
   `WEIGHTED_FAST_RESULT.json`.
4. `rh_shell_attachment_20260910/PROOF.md`, Zeilen9–19,73–97,185–205:
   vollständige ursprüngliche Form, Kreuzoperator und Schalenkarte.
5. `rh_shell_coupling_certificate_20260910/PROOF.md`, Zeilen9–35:
   genau das in(1) widerlegte Zertifikat und die Hochraumpositivität.

Die aktuelle native Queue nannte genau diesen vollen Vergleich als
offenen Test. `triage.json` dokumentiert den aktuellen lokalen
check-new-Zweig, die reine gaps-Abfrage und die ausgewählten Graphwege.
Die Wege sind Navigation, keine Beweisimplikationen. Registrierung und
einmaliger Refresh werden vom koordinierenden Root durchgeführt.

Die hier neue Feststellung ist der quellspezifische strenge Ausschluss
des ganzen eingefrorenen Vergleichs(1), samt einer notwendigen
Reparaturschranke. Die verwendete Kongruenz-/Inversenordnung ist
klassische Algebra; es wird keine weltweite Neuheit dieser Identitäten
oder eine Lösung von RH behauptet.
