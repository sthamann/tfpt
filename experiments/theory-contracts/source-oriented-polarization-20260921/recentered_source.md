# Rezentrierter Kandidat des vorhandenen v210-Quelloperators

21. September 2026 · analytischer Ausbau ohne neue Kopplung

## Ergebnis

Die Medianwahl von v210 besitzt neben dem festen-Moden-Nullgrenzwert einen
nichttrivialen **lokalen Kandidaten**, wenn der Beobachtungsraum mit den beiden
Fermikanten `n≈+N/2` und `n≈-N/2` mitwandert. Die festen rezentrierten
Matrixelemente ergeben pro skalarer komplexer Einteilchenkomponente zwei
entgegengesetzt chirale Hardy-Zweige. Das ursprüngliche Viermarkenprofil ist
auf diesen Kandidatenzweigen durch periodische unitäre Phasen entfernbar.

Dieser Bericht beweist jedoch weder Norm-/Strong-Resolvent-Konvergenz der
vollen rezentrierten Operatoren noch die dafür nötige asymptotische
Medianlage und Konvergenz ihrer unstetigen Signprojektoren. Die
Identifikation als tatsächlicher spektraler Grenzwert ist daher **bedingt und
numerisch gestützt**. Besonders die Besetzung der zweidimensionalen
Nullmodenfläche hängt an einer mit `N` gegen null gehenden
Bragg-Aufspaltung. Der analytische von-Mises-Kandidat zeigt bei den
hochpräzise geprüften Cutoffs einen reflexionsgeraden endlichen Zustand;
daraus folgt kein regulatorstabiler Grenzprojektor und keine ursprüngliche
P1-Auswahl einer Orientierung.

Das widerspricht dem Contract `source-conformal-kernel-selection-20260921`
nicht: Dessen Nullgrenzwert verwendet die feste Fourier-Einbettung, während
hier ausdrücklich zwei mit `N` wandernde Fenster betrachtet werden. Der
Contract `source-rg-clock-bridge-20260920` findet für den dort separat
stipulierten QWZ-Quelloperator ebenfalls zwei Edge-Zweige. Das ist eine
Strukturparallele, keine Identifikation des skalaren v210-Kandidaten mit dem
QWZ-Modell oder mit P1.

## 1. Rezentrierte Operatoren

Schreibe für `N` durch 8 teilbar

\[
m=\frac N2\in4\mathbb Z,
\qquad
\Lambda_N=P_N(|D|+M_f)P_N,
\qquad
\delta_N=\mu_N-m-f_0,
\]

wobei das reale Viermarkenprofil nur Fouriermoden in `4 Z` besitzt. Mit
`V=f-f_0` und den Einbettungen

\[
W_{N,+}e_k=e_{m+k},
\qquad
W_{N,-}e_k=e_{-m+k}
\]

erhält man auf jedem vorher festgehaltenen Fourierblock sogar exakt, sobald
der Block im Cutoff liegt,

\[
\begin{aligned}
W_{N,+}^*(\Lambda_N-m-f_0)W_{N,+}&=D+M_V,\\
W_{N,-}^*(\Lambda_N-m-f_0)W_{N,-}&=-D+M_V.
\end{aligned}
\tag{1}
\]

Die Kreuzmatrix zwischen den Kanten enthält Koeffizienten
`f_(N+k-l)` und verschwindet für festes `k,l` nach dem
Riemann-Lebesgue-Lemma; beim analytischen von-Mises-Profil sogar schneller
als jede Potenz. Damit ist der Kandidat für den lokalen
Matrixelementgrenzwert

\[
H_{\rm edge}=H_+\oplus H_-,
\qquad
H_+=D+V,
\qquad
H_-=-D+V.
\tag{2}
\]

Für die Identifikation der Signkovarianzen muss zusätzlich
`delta_N -> 0` sowie geeignete Resolventen-/Spektralprojektorkonvergenz
bewiesen werden. Feste Matrixelemente allein liefern das nicht. Die
hochpräzisen endlichen Rechnungen unten stützen `delta_N -> 0`, ersetzen den
Operatorbeweis aber nicht. Für das originale Profil ist

\[
f_0=4e^{-4}I_0(4)=0.8280076848959467916\ldots.
\]

## 2. Das Markenprofil ist auf beiden Zweigen reines Gauge

Da `V` reell ist und Mittelwert null hat, existiert eine reelle periodische
Funktion

\[
F'(\theta)=V(\theta),
\qquad F(\theta+2\pi)=F(\theta).
\]

Wegen der `4 Z`-Fourierunterstützung ist sogar
`F(theta+pi/2)=F(theta)`. Setze `U=e^(-iF)`. Dann gilt exakt

\[
H_+=UDU^*,
\qquad
H_-=U^*(-D)U.
\tag{3}
\]

Beide Zweige haben daher ganzzahliges Spektrum. Das Profil ändert die
Wellenfunktionen, nicht die Dispersion. Die beiden normierten Nullmoden sind

\[
z_+=U1=e^{-iF},
\qquad
z_-=U^*1=e^{iF}.
\tag{4}
\]

## 3. Exakte Kandidatenkovarianz und offene spektrale Grenzfrage

Seien `P_>`, `P_<` die Spektralprojektoren von `D` auf strikt positive
beziehungsweise strikt negative ganze Moden. Der exakt aus dem
Kandidatenoperator (2) berechnete, von null getrennte Signanteil ist

\[
C_{\rm stable}
=UP_>U^*\ \oplus\ U^*P_<U.
\tag{5}
\]

Der erste Summand ist ein gerichteter Hardy-Zweig, der zweite der
entgegengesetzte. **Falls** die fehlende Resolventen-/Projektorkonvergenz
gezeigt wird, besitzt der spektrale Grenzwert daher zwei gegenläufige
chirale Fermikanten und keinen ausgewählten chiralen Randzustand. Diese
Zählung gilt zunächst pro komplexer skalarer Einteilchenkomponente; sie ist
noch keine physische Majorana-Zählung. Der Festblockcheck in Abschnitt 4
stützt genau diesen von null getrennten Kandidaten numerisch.

Auf

\[
Z=\operatorname{span}\{z_+\oplus0,\ 0\oplus z_-\}
\]

hat `H_edge` den Eigenwert null. Die unstetige Signfunktion bestimmt dort
nichts. Jeder lokal identifizierte Grenzpunkt der Kovarianzen hat auf diesem
Kandidatenraum höchstens die Form

\[
C_{\rm edge}=C_{\rm stable}+Q_Z,
\qquad 0\le Q_Z\le I_Z.
\tag{6}
\]

Auf einem endlichen, sauber isolierten Schwellenpaar hat die konkrete
Medianfolge Gesamtbesetzung eins. Wenn dieses zweidimensionale Teilbündel
kontrolliert mit `Z` identifiziert wird und seine Projektoren stark
konvergieren, wäre `Q_Z` ein Rang-eins-Projektor; bei einer exakten
Entartung verwendet `numpy.sign(0)=0` und liefert auf dem endlichen Paar
`I/2`. Ohne diese Kontrolle kann ein schwacher lokaler Grenzwert eines
Rang-eins-Projektors eine echte Kontraktion sein oder Masse aus dem
beobachteten Fenster verlieren. Weder `rank(Q_Z)=1` noch `tr(Q_Z)=1` wird
hier als Grenzsatz behauptet.

Für das exakte analytische, gerade von-Mises-Profil sind die beiden
Schwellenzustände in den geprüften endlichen Matrizen reflexionsungerade
beziehungsweise reflexionsgerade. Die obere, von v210 besetzte Kombination
war in der hochpräzisen Rechnung für `N=16,32,64` jeweils die gerade
Kombination, deren formaler rezentrierter Kandidat

\[
z_{\rm even}=\frac{z_+\oplus z_-}{\sqrt2}
\tag{7}
\]

Die zugehörige Aufspaltung kollabiert jedoch:

| `N` | Schwellenlücke | Reflexionsparität unten/oben |
|---:|---:|:---:|
| 16 | `3.9595984078e-6` | `-1 / +1` |
| 32 | `1.4513898817e-13` | `-1 / +1` |
| 64 | `4.1375935244e-30` | `-1 / +1` |

Die Tabelle belegt noch keinen Grenzwert der unstetigen Signprojektoren auf
`Z`; insbesondere wird hier **nicht** behauptet, dass
`Q_Z=|z_even><z_even|` für alle `N` oder regulatorunabhängig folgt. Gleichung
(7) beschreibt die in diesen Cutoffs beobachtete endliche Paritätsrichtung.
Schon die unveränderte Double-Precision-FFT verliert sie, sobald die
Aufspaltung unter die Rundungsgröße fällt. Der wohldefinierte Grenzbefund ist
daher (5) außerhalb von `Z` und die offene Nullflächenwahl (6).

## 4. Kleinster Check am unveränderten Original

Auf dem mitbewegten Block `k=-2,...,2` um beide Kanten stimmen die von der
Nullmode verschiedenen Einträge mit (5) überein. Der Operatornormfehler des
entsprechenden Teilblocks betrug

| `N` | Fehler gegen die gauge-transformierten Hardy-Zweige |
|---:|---:|
| 16 | `7.14e-7` |
| 32 | `1.95e-14` |
| 64 | `1.55e-14` |

Die zentralen `k=0`-Blöcke des unveränderten Double-Precision-Prüfers waren
dagegen näherungsweise

\[
\begin{array}{c|cc}
N=16&0.5000&0.4993\\&0.4993&0.5000\\ \hline
N=32&0.5024&0.4993+1.5\,10^{-5}i\\
    &0.4993-1.5\,10^{-5}i&0.4976\\ \hline
N=64&0.9903&-0.0753+0.0573i\\
    &-0.0753-0.0573i&0.0097
\end{array}
\]

Der von null getrennte Teil stimmt in diesen Festblöcken mit dem Kandidaten
überein; das ist numerische Evidenz, kein Operator-Konvergenzbeweis. Die
Nullrichtung ist bereits numerisch instabil. Ein Clock-Kommutator kann
trotzdem grün bleiben, weil beide Nullkombinationen im selben
Viererclockblock liegen.

## 5. Weder Orientierung noch Clock wählen in v210 eine Kante

Für `N` durch 8 teilbar ist `m=N/2` durch 4 teilbar. Die Viererclock wirkt
auf beiden lokalen Basen gleich:

\[
i^{m+k}=i^k,
\qquad
i^{-m+k}=i^k.
\]

Sie kann die beiden Zweige daher nicht unterscheiden. Die Reflexion tauscht
sie aus. Der v210-Operator verwendet ausdrücklich `|n|` und ein reelles,
gerades Profil; eine Orientierung ist in dieser Zustandskonstruktion nicht
als Vorzeichenoperator enthalten. Eine einseitige Naht könnte nur dann eine
Kante wählen, wenn ihre Orientierung quellenseitig in einen gerichteten
Operator, eine Calderónpolarisation oder eine äquivalente CAR-Realstruktur
übersetzt wird. Dieser Pfeil fehlt im vorhandenen Kandidaten.

## 6. Spinstruktur

Die Originalbasis von v210 hat ganzzahlige Fouriermoden. Nach Rezentrierung
um `m=N/2 in Z` bleiben die lokalen Moden `k in Z`; (2) ist daher bei einer
fermionischen Interpretation der **periodische/Ramond-artige** Sektor mit
je einem Nullmodus pro Zweig.

Ein NS-Sektor hätte halbzahlige Moden und keine Schwellen-Nullmode. Er kann
durch antiperiodische Randbedingungen oder eine halbzahlige
Fermikantenverschiebung entstehen. Beides ist eine weitere Spinstrukturwahl
und wird von `mark_sum`, der Medianregel oder der Viererclock nicht
hergeleitet. Insbesondere darf die Ramond-artige Rechnung nicht als Beweis
des zuvor gewünschten NS-Szegő-Kerns verwendet werden.

Schon die **Cutoffparität** erzeugt hier einen solchen formalen Wechsel. Für
flaches `f=0` und ungerades `N=2M+1` ist `mu_N=N/2=M+1/2`. Rezentriert man um
die Kante `c=N/2`, so sind die lokalen Abstände

\[
r=n-c\in\mathbb Z+\tfrac12.
\]

Der ungerade Cutoff sieht daher NS-artig aus und besitzt keine Nullmode; ein
gerader Cutoff sieht periodisch/R-artig aus und besitzt die oben diskutierte
Nullfläche. Eine physische Spinstruktur darf nicht von der Parität eines
UV-Regulators abhängen. Diese Beobachtung klassifiziert die beiden
Cutofffolgen, wählt aber keine von ihnen aus P1 aus.

## 7. CAR-Typisierung

Die Rechnung bis hierher lebt auf dem komplexen skalaren Einteilchenraum.
Für das reale Profil kommutiert der mathematisch exakte Operator mit der
Realstruktur

\[
(J\psi)_n=\overline{\psi_{-n}},
\]

und die rezentrierte Realstruktur tauscht die beiden Kanten. Das macht einen
einzelnen komplexen Zweig nicht automatisch zu einem Majoranafeld. Eine
selbstduale Majorana-CAR-Kovarianz `S` müsste zusätzlich

\[
S+JSJ=I
\tag{8}
\]

erfüllen. Wenn eine Kovarianz wie eine reelle Spektralfunktion von v210 mit
`J` kommutiert, würde (8) `S=I/2` verlangen; der nichttriviale
Signprojektor erfüllt dies nicht. v210 liefert deshalb ohne eine weitere
Verdopplung beziehungsweise Polarisation und zugehörige Realstruktur keine
fertige selbstduale Majorana-CAR-Darstellung. Insbesondere darf „ein
komplexer Hardy-Zweig“ nicht ohne diesen Schritt als „ein Majorana-Zweig“
gezählt werden.

## Verdict

- **EXAKT LOKAL:** Die festen rezentrierten Kompressionsmatrizen haben den
  Kandidaten `(D+V) direct-sum (-D+V)`; dieser Kandidat ist durch eine
  periodische Phase äquivalent zu `D direct-sum (-D)`.
- **BEDINGT/NUMERISCH GESTÜTZT:** Seine Identifikation als spektraler
  Grenzoperator und die Konvergenz der von null getrennten Signprojektoren
  benötigen noch ein Norm-/Strong-Resolvent- beziehungsweise Min-Max-
  Argument. Die Festblockdaten stimmen mit den zwei gauge-transformierten
  Hardy-Zweigen überein.
- **SCHWELLENABHÄNGIG:** Auf jedem kontrolliert isolierten endlichen
  Schwellenpaar ist die Medianbesetzung eins. Ohne kontrollierte lokale
  Nullsektoridentifikation muss ein Grenzpunkt weder Rang eins noch
  spurerhaltend sein. Der analytische Kandidat zeigt in den geprüften
  Cutoffs die gerade Kombination; ihre Lücke verschwindet extrem schnell.
- **REGULATORABHÄNGIG:** Gerade Cutoffs ergeben eine R-artige Nullfläche,
  ungerade Cutoffs halbzahlige, NS-artige lokale Moden. Das ist keine
  physische Spinstrukturableitung.
- **NICHT AUSGEWÄHLT:** v210 enthält keinen Operator, der aus der vorhandenen
  Nahtorientierung kanonisch nur eine Fermikante macht.
- **OFFEN:** Die physische Spinstruktur, CAR-Realstruktur und die
  quellenseitige Identifikation einer gerichteten Polarisation. Der
  rezentrierte Analyse liefert einen präzisen Kandidatenraum, aber keine
  ursprüngliche P1-Auswahl.

Dies ist keine neue Quellkopplung und keine E8-Erweiterung. Es analysiert nur
den bereits vorhandenen skalaren v210-Kandidaten unter einer ausdrücklich
mitbewegten Skalierung.
