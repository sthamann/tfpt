# Geladene Felder und gemeinsame Zeitkorrelatoren aus der tatsächlichen QWZ-Quelle

Stand: 21. September 2026  
Verdict: **EXAKT/SYMBOLISCH innerhalb des vorhandenen einquelligen freien QWZ-CAR-Grenzsatzes; keine neue Kanal- oder E8-Herleitung.**

## 1. Tatsächliche mikroskopische Daten

Die Quelle ist kein gewünschter `Gamma`-/`Vaux`-Block, sondern der bereits
vorhandene QWZ-Zylinder

\[
h_N=h_{\rm QWZ}(N,8,m=1,r=1),\quad
P_N={\bf1}_{(-\infty,0)}(h_N),\quad
\Omega_N=\text{gefüllter Slaterzustand},
\]

\[
D_N={N\over2\pi}h_N,\qquad
\mathcal H_N=d\Gamma(D_N)-\operatorname{Tr}(P_ND_N),\qquad
Q_N=d\Gamma(1)-8N.
\]

Für eine glatte Kreisfunktion `f` ist die wirkliche lokale Einteilchenwelle

\[
(R_Nf)(x,y)=N^{-1/2}e^{-i\pi x/(2N)}f(x/N)\,
\delta_{y,7}\chi_+,
\]

und damit

\[
\Psi_N(f)=a_N(R_Nf),\qquad
\Psi_N^\dagger(f)=a_N^\dagger(R_Nf).
\]

Auf dem vollständigen mikroskopischen Fockraum gelten exakt

\[
[Q_N,\Psi_N(f)]=-\Psi_N(f),\quad
[Q_N,\Psi_N^\dagger(f)]=\Psi_N^\dagger(f),\quad
\{\Psi_N(f),\Psi_N^\dagger(g)\}=\langle R_Nf,R_Ng\rangle\,1.
\]

Der Zustand ist der eichinvariante quasifreie Zustand mit Kovarianz

\[
C_N=P_N,
\quad \omega_N(a_N^\dagger(u)a_N(v))=\langle v,P_Nu\rangle,
\quad \omega_N(a_N(u)a_N^\dagger(v))=\langle u,(1-P_N)v\rangle.
\]

Das ist mehr als ein Projektorname: `P_N` ist die Kovarianz des tatsächlich
gefüllten Quellvakuums. Er ist aber noch **keine Zeitentwicklung**.

## 2. Quelleigene Zeit und der Viertelladungsterm

Mit Heisenberg-Konvention

\[
\alpha_t^N(a_N^\dagger(u))=a_N^\dagger(e^{itD_N}u),\qquad
\alpha_t^N(a_N(u))=a_N(e^{itD_N}u)
\]

kommt die Zeit aus `D_N`, nicht aus `P_N`. Die oberen Randquasimoden haben
die Sinusdispersion mit einem im Originalsatz kontrollierten endlichen
Breitenfehler; sie sind bei endlichem N nicht als exakte Eigenmoden zu behandeln. Schreibt man
`r=1/2-j` (halbzahlig), dann wird

\[
{N\over2\pi}\sin\!\left({2\pi(r-1/4)\over N}\right)
\longrightarrow h(r)=r-{1\over4}.
\]

Die Grenzdaten sind daher

\[
\mathfrak h=\ell^2(\mathbb Z+1/2),\qquad
C={\bf1}_{r<0},\qquad h e_r=(r-1/4)e_r,
\]

und auf der endlichen Energie-Domäne

\[
H=d\Gamma_C(h)=L_0-{1\over4}Q.
\]

Für ein geladenes Erzeugungsfeld und sein Adjunkt bedeutet das ausdrücklich

\[
\alpha_t^H(\psi_r^\dagger)=e^{it(r-1/4)}\psi_r^\dagger
=e^{-it/4}\alpha_t^{L_0}(\psi_r^\dagger),
\]

\[
\alpha_t^H(\psi_r)=e^{-it(r-1/4)}\psi_r
=e^{+it/4}\alpha_t^{L_0}(\psi_r).
\]

Der vorhandene Quellenbeweis zeigt die gemeinsame Konvergenz von Feld,
Adjunkt und Generator auf jedem festen endlichen Energie-Core. Er liefert nur
**eine** komplexe CAR-Sorte mit ganzzahliger Ladung.

## 3. Zwei- und Vierzeitkorrelatoren

Wir verwenden `⟨u,v⟩=u†v` und setzen

\[
K_N((g,s);(f,t))
:=\omega_N\!\left(\alpha_t^N(\Psi_N^\dagger(f))
                    \alpha_s^N(\Psi_N(g))\right).
\]

Dann gilt schon für jedes endliche `N` exakt

\[
\boxed{K_N((g,s);(f,t))
=\langle e^{isD_N}R_Ng,\,P_Ne^{itD_N}R_Nf\rangle.}
\]

Der komplementäre Propagator ist

\[
L_N((f,t);(g,s))
=\omega_N\!\left(\alpha_t^N(\Psi_N(f))
                    \alpha_s^N(\Psi_N^\dagger(g))\right)
=\langle e^{itD_N}R_Nf,(1-P_N)e^{isD_N}R_Ng\rangle.
\]

Im Limes wird

\[
\boxed{K((g,s);(f,t))
=e^{-i(t-s)/4}\sum_{r<0}\overline{g_r}f_r e^{i(t-s)r}.}
\]

Damit ist die `-Q/4`-Phase im geladenen Propagator sichtbar. Für zwei
Erzeugungen und zwei Vernichtungen liefert Wick nicht nur eine Analogie,
sondern die exakte Determinante

\[
\boxed{\begin{aligned}
&\omega\bigl(\psi^\dagger(f_1,t_1)\psi^\dagger(f_2,t_2)
              \psi(g_2,s_2)\psi(g_1,s_1)\bigr)\\
&\qquad=\det\!\begin{pmatrix}
K((g_1,s_1);(f_1,t_1))&K((g_1,s_1);(f_2,t_2))\\
K((g_2,s_2);(f_1,t_1))&K((g_2,s_2);(f_2,t_2))
\end{pmatrix}.
\end{aligned}}
\]

Für eine beliebige Reihenfolge von vier linearen Feldern gilt äquivalent die
fermionische Wick-Summe

\[
\omega(F_1F_2F_3F_4)=
\omega(F_1F_2)\omega(F_3F_4)
-\omega(F_1F_3)\omega(F_2F_4)
+\omega(F_1F_4)\omega(F_2F_3).
\]

Da die vorhandene Quellenisometrie alle festen endlichen Wörter und endlich
viele Zeiten konvergieren lässt, folgt die Grenzdeterminante aus den wirklichen
mikroskopischen Determinanten. Es wird kein separates Wunschvakuum benutzt.

## 4. Same-source Paarprodukte und ein möglicher „Mediator“

Aus der einen wirklichen CAR-Sorte kann man ohne neue Quelle geladene
Zweifeldprodukte bilden:

\[
B^\dagger(f_1,f_2)=\psi^\dagger(f_1)\psi^\dagger(f_2),\qquad
[Q,B^\dagger]=2B^\dagger.
\]

Sie erfüllen die Produktidentitäten

\[
B^\dagger(f_1,f_2)=-B^\dagger(f_2,f_1),\qquad
B^\dagger(f,f)=0.
\]

Auf dem gefüllten Zustand hängt ein Teilchenpaar nur von
`u_i=(1-C)f_i` ab und ist der Keilvektor `u_1∧u_2`. Seine gemeinsame
Gramform ist deshalb

\[
\boxed{\langle u_1\wedge u_2,v_1\wedge v_2\rangle
=\det\!\begin{pmatrix}
\langle u_1,v_1\rangle&\langle u_1,v_2\rangle\\
\langle u_2,v_1\rangle&\langle u_2,v_2\rangle
\end{pmatrix}.}
\]

Mit verschiedenen Zeiten ist dieselbe Formel die Determinante aus den vier
komplementären Propagatoren `L`. Die Paarzeit wird nicht neu gewählt: Auf
`∧²((1-C)h)` ist

\[
h^{(2)}=h\otimes1+1\otimes h,
\]

also sind Gram, erster Jet und zweiter Jet vollständig aus der Einfeldquelle
geerbt.

Damit ergibt sich die ehrliche Mediatorentscheidung:

- Wird ein „Mediatorlabel“ auf **denselben** Keilvektor wie ein Paarlabel
  abgebildet, ist es eine Dublette. Der gemeinsame Gram hat eine Nullrichtung
  `(x,-x)`; Polarnormalisierung erzeugt daraus keinen zweiten Quellenzustand.
- Ein anderer Keilvektor kann als Hilbertraumzustand linear unabhängig sein.
  Er bleibt aber ein quadratisches Composite derselben CAR-Sorte, keine
  unabhängige elementare Mediator-Spezies.
- Ein neutrales Teilchen-Loch-Composite
  `M†(u,v)=ψ†(u)ψ(v)` hat Ladung null und ist zum geladenen `Q=2`-Paarsektor
  orthogonal. Es darf ohne zusätzliche Ladungsabbildung nicht als dessen
  Mediator ausgegeben werden.

Der neue enge Symbolcheck demonstriert beides ohne erfundene 64 Labels: In
einem Viermoden-Quellfenster besitzen vier Paar/Mediator-Dublettenlabels nur
Gramrang `2`; fügt man einen anderen Keilvektor hinzu, steigt der Rang auf
`3`. Das widerlegt weder alle Composite-Konstruktionen noch eine mögliche
spätere TFPT-Vervollständigung. Es trennt nur **Operatorprodukt**,
**unabhängigen Zustand** und **Labelraum-Isometrie**.

## 5. Vergleichsgrenze zum 2076-dimensionalen Polarkandidaten

Der neue Polarkandidat ist ein exakter bedingter Satz in seinem gewählten
zehnkanaligen Randmodell. Sein eigener Review stellt zugleich fest, dass die
Polarabbildung nicht als Produkt-, Adjunkt- oder CAR/CCR-Homomorphie nachgewiesen ist und neue
polarisierte Präparationen mischt. Daher darf sein Energiespektrum
`3^60,4^60,5^1956` nicht zuerst an die Einquellenenergie angepasst werden.

Der kleinste entscheidende Test ist in dieser Reihenfolge:

1. **Feldstatistik und Produkt:** Sind die Kandidatenbilder tatsächliche
   Operatorprodukte der einen `ψ,ψ†`, einschließlich Pauli-Nullen und Adjunkt?
2. **Ladung:** Gilt derselbe mikroskopische Ward-Kommutator mit ganzzahliger
   Ladung, oder wurde ein neues Ladungsdictionary gewählt?
3. **Gemeinsamer Gram und Zustand:** Stimmt die volle Block-Grammatrix der
   Operatorzustände mit der Determinante aus `C` und `1-C` überein?
4. **Erster und zweiter Zeitjet:** Für beide Polarisationen müssen
   \[
   C h^n,\quad (1-C)h^n,\qquad n=1,2,
   \]
   beziehungsweise im Paarsektor die geerbten Keiljets stimmen.
5. **Erst danach Energievergleich.** Gleiche Eigenwerte ohne diese
   Operatorabbildungen belegen keine gemeinsame mikroskopische Quelle.

Der Check enthält zudem ein exaktes Gegenbeispiel zur Gleichsetzung
„Zustandsprojektor = Zeit“: `h` und ein verändertes `h_alt` kommutieren beide
mit demselben `C`, haben denselben negativen Spektralprojektor und damit
denselben gefüllten Grundzustand, aber verschiedene erste und zweite Zeitjets.
Dieser alte strukturelle Einwand wird hier nur als Negativkontrolle wiederholt.

## 6. Reproduktion und Evidenzgrenze

Gezielt frisch ausgeführt:

- bestehende Quelltests: **19/19 PASS**, darunter voller QWZ-Slaterzustand,
  beide Adjunkte, Ladung, Generator und ein komplexes Vierzeitwort;
- bestehender Quellchecker: Status
  `ONE_SOURCE_INTEGER_CHARGED_CAR_EDGE_LIMIT`; volle Einteilchendimensionen
  `128/256/512` bei `N=8/16/32`, besetzte Ränge `64/128/256`;
- Polarisationfehler der vollen Quelle:
  `1.31e-15, 2.11e-15, 2.39e-15`;
- rohe Kovarianzfehler gegen den Grenzprojektor:
  `3.40e-2, 3.99e-3, 3.43e-4`;
- neuer enger Symbolcheck: alle CAR-, Ladungs-, `H=L0-Q/4`-, Zwei-/Vierzeit-
  und Composite-Paarprüfungen PASS.

Artefakte: `checker.py`, `certificate.json`, `source_checker_replay.json`.
Der große transitive Alt-Suite-Lauf wurde nicht als Evidenz verwendet; für
diese Frage genügt die gezielte 19-Test-Quellregression.

## 7. Ergebnis und erste offene Brücke

Die positive Quellenantwort ist vorhanden: ein wirkliches lokales geladenes
CAR-Feld, sein tatsächlicher quasifreier Zustand, sein ursprünglicher
QWZ-Generator samt kontrolliertem linearem Randgrenzwert und alle festen
gemeinsamen Mehrzeitmomente. Neu in
dieser Runde ist nur die explizite Korrelator-/Determinantenextraktion sowie die
same-source Composite-Paar-/Mediator-Grenze; der Feldexistenzsatz vom
9. September wird nicht als neu gezählt.

Im Vergleich dieser vorhandenen mikroskopischen Realisierung mit dem
Randkandidaten ist die ungelöste Brücke präzise: Konstruiere aus derselben
mikroskopischen CAR-Quelle eine adjungiert- und produktverträgliche Abbildung
in den gewünschten mehrkanaligen geladenen Feldraum, die gemeinsamen Gram,
Ward-Ladung und beide ersten Zeitjets bewahrt. Eine Labelraum-Isometrie oder
ein passendes Energiespektrum erfüllt diese Brücke noch nicht. Vor diesem
Kandidatenvergleich bleibt außerdem die Herkunft genau dieser mikroskopischen
Realisierung aus dem primitiven P1/P2-System offen; sie wird durch den
vorhandenen Einquellen-Grenzsatz nicht bewiesen.

T1–T8 bleiben offen.
