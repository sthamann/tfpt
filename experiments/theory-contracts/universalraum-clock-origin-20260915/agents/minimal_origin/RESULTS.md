# Minimaler Ursprungsstrang: geteilte Moden und ein echter nativer Vierzustandskanal

Stand: 15. September 2026. Unabhängiger, begrenzter Forschungsstrang.

## Ergebnis und Reichweite

Es gibt zwei verschiedene Ergebnisse, die ausdrücklich nicht verwechselt werden dürfen:

1. **Ein exakt lösbarer Überlappungsbaustein:** Eine gemeinsame Fermionmode und ein gemeinsamer Bosonkanal werden in jedem festen positiven Ressourcensektor zu einer gewöhnlichen effektiven Fermionmode. Dafür ist keine direkte Endpunkt-Hopping-Wechselwirkung nötig. Dieser Dreierstern ist jedoch **kein Ausschnitt einer tatsächlichen nativen W-Zeile**.
2. **Ein tatsächlicher W-basierter Vierzustandskanal:** Im unveränderten 64-Fermion/60-Boson-Paartensor existiert ein exakt invariantes Vierzustandsystem, wenn ein **zusätzlicher reiner Bosonmischer** zwischen Kanal 0 und 1 zugelassen und ein bestimmter Zustand mit Gesamtladung 9 präpariert wird. Der vollständige native Hamiltonoperator plus dieser Mischer überträgt dort eine innere Fermionmarke mit einer streng abgesicherten Wahrscheinlichkeit von **mehr als 99,3 %**.

Das zweite Ergebnis benötigt keine Projektion, die die übrigen nativen Zustände künstlich wegschneidet: Der Vierzustandsraum ist unter allen 60 ursprünglichen Paaroperatoren plus dem Mischer exakt invariant. Es ist aber **weder eine Untersuchung der Entnahmeantwort des N=64-Grundzustands noch ein Transport zwischen zwei unabhängigen Banken**. Die Herkunft des Bosonmischers, die spezielle Präparation und die räumliche Bedeutung der Marken bleiben offen.

## 1. Warum eine Clockphase die bisherige Paritätsschranke nicht aufhebt

Seien zwei operational unabhängig definierte Banken mit lokalen Paritäten

\[
\Pi_x=(-1)^{N_{f,x}},\qquad \Pi_y=(-1)^{N_{f,y}}
\]

gegeben. Kommutiert jede ausführbare lokale Operation und jeder einzelne realisierte Messzweig mit beiden Paritäten, gilt dies auch für beliebige Produkte, Summen, Adjungierte und starke beschränkte Grenzwerte. Eine Clockoperation, die lediglich innerhalb jeder Bank Fermionmoden zahlenerhaltend permutiert, bleibt in dieser Algebra.

Ein echter Einfermiontransfer erfüllt dagegen

\[
\Pi_x f_y^\dagger f_x=-f_y^\dagger f_x\Pi_x,
\qquad
\Pi_y f_y^\dagger f_x=-f_y^\dagger f_x\Pi_y.
\]

Er kann daher nicht allein durch mehr Kompositionen jener Operationen entstehen. Eine bloß paritätskovariante CP-Abbildung ist nicht die gleiche Voraussetzung: Sie kann ungerade Krauszweige besitzen. Die Aussage gilt nur für den ausdrücklich geraden ausführbaren Operationssatz.

Bei geteilten Fermionmoden sind die beiden lokalen CAR-Algebren von Anfang an nicht unabhängig. Liegt dieselbe Mode s in beiden, kann sie nicht zugleich als zwei unabhängige antikommutierende Kopien behandelt werden: \(\{s,s^\dagger\}=1\). Auch lokale Ladungen, die s doppelt mitzählen, sind keine unabhängigen additiven Bankladungen. Überlappung widerlegt somit den Paritätssatz nicht, sondern ändert seine Voraussetzungen.

## 2. Exakter CAR-Baustein aus einem geteilten Boson und Fermion

Betrachtet werden drei CAR-Moden \(f_x,s,f_y\), ein CCR-Boson b und

\[
Q_x=b^\dagger s f_x,\qquad Q_y=b^\dagger s f_y,
\qquad
H_\star=\Delta N_b+g(Q_x+Q_y+Q_x^\dagger+Q_y^\dagger).
\]

Der Ressourcenzähler

\[
K=N_b+n_s
\]

kommutiert mit allen diesen Operationen. Auf jedem exakten K-Sektor mit ganzzahligem \(K\ge1\) setze

\[
c^\dagger=\frac{b^\dagger s}{\sqrt K},\qquad
c=\frac{s^\dagger b}{\sqrt K}.
\]

Direkt aus CCR und CAR folgen

\[
(c^\dagger)^2=c^2=0,\qquad
\{c,c^\dagger\}=\frac{N_b+n_s}{K}=1.
\]

Die Mode c antikommutiert mit beiden Endpunktmoden. Ferner

\[
N_b=K-1+n_c,
\qquad
N_f+2N_b=2K-1+n_x+n_c+n_y.
\]

Damit gilt exakt

\[
\boxed{
H_\star=\Delta(K-1)+\Delta n_c
 +g\sqrt K\big(c^\dagger f_x+c^\dagger f_y+\mathrm{h.c.}\big).
}
\]

Die gewöhnliche Drei-Moden-Transferkette wurde hier aus einer überlappenden Paarumwandlung erhalten. Ein nützlicher Operatorausdruck derselben Tatsache ist

\[
\boxed{[Q_y^\dagger,Q_x]=K f_y^\dagger f_x.}
\]

Das ist zunächst eine Operatoridentität. Die Verfügbarkeit getrennter Kommutator-Kontrollsequenzen folgt daraus nicht automatisch. Schon der konstante Summen-Hamiltonoperator zeigt jedoch Transfer. Der minimale positive Ressourcensektor K=1 benötigt am Anfang eine besetzte gemeinsame Fermionmode s und ein leeres Boson.

### Vollständige Transferrechnung im Vergleichsmodell

Im effektiven Einteilchenraum und bei K=1 lautet die Matrix

\[
\begin{pmatrix}0&g&0\\g&\Delta&g\\0&g&0\end{pmatrix}.
\]

Der antisymmetrische Endpunktzustand ist dunkel. Der symmetrische koppelt mit \(\sqrt2g\) an c. Für \(g/\Delta=1/20\), \(m=101\) und

\[
t=\frac{202\pi}{\Delta\sqrt{51/50}}
\]

verschwindet die mittlere Besetzung wieder exakt. Die Zielwahrscheinlichkeit ist

\[
p_\star=\sin^2\left[\frac\pi2\,101\left(1-\sqrt{50/51}\right)\right].
\]

Durch Quadrieren rationaler Schranken erhält man

\[
\frac{199}{200}<101\left(1-\sqrt{50/51}\right)<1.
\]

Mit \(|\sin u|\le|u|\) und \(\pi<355/113\) folgt

\[
p_\star>1-\left(\frac{355/113}{400}\right)^2>0.9999.
\]

Diese Zahl gehört **nur zum Vergleichsmodell mit gemeinsamem b**.

### Die direkte Quellen-Grenze

Die tatsächliche native W-Zeile enthält jeweils acht disjunkte Fermionpaare, also 16 verschiedene Marken. Eine einzelne Zeile enthält deshalb niemals zugleich \(s f_x\) und \(s f_y\) mit \(x\ne y\). Das ist an allen 60 Zeilen exakt geprüft.

Ein gemeinsamer-b-Dreierstern darf somit nicht allein wegen der Form \(b^\dagger f f\) als nativer Baustein bezeichnet werden. Insbesondere wäre ein Wechsel von zwei Bosonkanälen zu einer gemeinsamen Mode ohne Kontrolle des orthogonalen Kanals eine zusätzliche Modellannahme.

## 3. Exakter Vierzustandskanal mit dem vollständigen nativen W

Die gepinnte Quelle ist

`universalraum-native-ground-response-20260915/ground_replay/outputs/simple_core/spinor_tensors.npz`,

SHA-256 `3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

Die zwei relevanten Quellenzeilen sind

\[
\begin{aligned}
P_0={}&-f_{57}f_4+f_{56}f_5+f_{53}f_8-f_{52}f_9
       -f_{45}f_{16}+f_{44}f_{17}+f_{33}f_{28}-f_{32}f_{29},\\
P_1={}&-f_{58}f_4+f_{56}f_6+f_{54}f_8-f_{52}f_{10}
       -f_{46}f_{16}+f_{44}f_{18}+f_{34}f_{28}-f_{32}f_{30}.
\end{aligned}
\]

Die Konvention ist \(P_A=\sum_{i<j}W_{A,ij}f_jf_i\). Das gemeinsame aktive Fermion ist s=4; die Endpunktmarken sind 57 und 58.

Präpariert werden sieben unveränderte Pauli-Blocker

\[
S=\{8,16,28,32,44,52,56\}.
\]

Sei \(|S\rangle\) der geordnet erzeugte Fockzustand dieser Moden. Die vier Basiszustände sind

\[
\begin{array}{c|c|c}
\text{Zustand}&\text{besetzte Fermionmoden}&\text{Bosonen}\\\hline
L&S\cup\{4,57\}&0\\
B_0&S&1\text{ in Kanal }0\\
B_1&S&1\text{ in Kanal }1\\
R&S\cup\{4,58\}&0
\end{array}
\]

Jeder Zustand besitzt die native Gesamtladung \(N=N_f+2N_b=9\).

Zugelassen wird nun genau eine zusätzliche Hamiltonoperation,

\[
H_J=J(b_1^\dagger b_0+b_0^\dagger b_1).
\]

Alle ursprünglichen 60 nativen Paaroperatoren bleiben erhalten:

\[
H=\Delta N_b+g\sum_{A=0}^{59}(b_A^\dagger P_A+P_A^\dagger b_A)+H_J.
\]

Der Prüfer wendet sämtliche 480 signierten Paarkanäle einschließlich aller CAR-Vorzeichen und der Bosonfaktoren auf jeden der vier Zustände an. Es entstehen **keine Zustände außerhalb ihres linearen Spanns**. Die Pauli-Blocker verhindern insbesondere die sieben unerwünschten Rückpaarungen jedes aktiven Bosonkanals.

Es ergibt sich exakt

\[
\boxed{
H_4=\begin{pmatrix}
0&g&0&0\\
g&\Delta&J&0\\
0&J&\Delta&g\\
0&0&g&0
\end{pmatrix}_{(L,B_0,B_1,R)}.
}
\]

Ohne Mischer, J=0, zerfällt die Matrix in zwei getrennte 2×2-Blöcke. Dann ist \(\langle R|e^{-itH}|L\rangle\) zu jeder Zeit exakt null. Mit J ungleich null beginnt die Transferamplitude bei dritter Ordnung; die Wahrscheinlichkeit hat den führenden Term \(g^4J^2t^6/36\).

**Die Quelle enthält hier also die beiden Endstücke und eine exakt funktionierende Pauli-Blockierung, aber nicht die geprüfte Bosonverbindung als bereits verfügbare Operation.**

## 4. Strenge vollständige Transfergrenze im tatsächlichen W-Zeugen

Unter Spiegelung L↔R und B₀↔B₁ zerfällt H₄ in

\[
H_+=\begin{pmatrix}0&g\\g&\Delta+J\end{pmatrix},\qquad
H_-=\begin{pmatrix}0&g\\g&\Delta-J\end{pmatrix}.
\]

Wähle den vorhandenen Prüfquotienten \(g/\Delta=1/20\) und die ausdrücklich neu gesetzte Mischerstärke

\[
J=\Delta-\frac{2g}{\sqrt3}
 =\Delta\left(1-\frac1{10\sqrt3}\right),
\qquad t=\frac{\pi\sqrt3}{g}=\frac{20\pi\sqrt3}{\Delta}.
\]

Da \(0<J<\Delta\), bleiben die Eigenfrequenzen des Bosonmischers \(\Delta\pm J\) positiv. Es wurde **keine Nullfrequenz durch exakte Aufhebung von \(\Delta N_b\)** erzeugt. Auch auf dem ganzen Fockraum bleibt die hinzugefügte Hamiltonfamilie nach unten beschränkbar: Das Bosonquadrat ist strikt positiv und die endlichen Fermionoperatoren können durch quadratische Ergänzung kontrolliert werden. Das bedeutet nicht, dass ihr Grundzustand noch der unveränderte native Grundzustand ist.

Für H₋ ist \(\Delta-J=2g/\sqrt3\). Zu der gewählten Zeit kehrt dessen Endpunktkomponente exakt mit Phase −1 zurück, ohne mittlere Restbesetzung.

Für H₊ setze

\[
a=\Delta-\frac g{\sqrt3},\quad
\omega=\sqrt{a^2+g^2},\quad
w_- =\frac{1-a/\omega}{2}.
\]

Die Endpunktamplitude lautet

\[
A_+=(1-w_-)e^{i(\omega-a)t}+w_-e^{-i(\omega+a)t}.
\]

Mit \(\omega-a\le g^2/(2a)\), \(w_-\le g^2/(4a^2)\),
\(\cos u\ge1-u^2/2\) und
\(|A_+|^2\ge1-g^2/a^2\) folgt

\[
\begin{aligned}
p_{L\to R}
 &=\left|\frac{A_++1}{2}\right|^2\\
 &\ge1-\frac{g^4t^2}{16a^2}-\frac{g^2}{2a^2}\\
 &=1-\frac{3\pi^2+8}{6400(a/\Delta)^2}.
\end{aligned}
\]

Aus \(\sqrt3>17/10\) folgt \(a/\Delta>33/34\). Somit ergibt sich rein rational

\[
\boxed{
p_{L\to R}>
1-\frac{3(355/113)^2+8}{6400(33/34)^2}
=\frac{2009992727}{2022609600}
>0.9937620819>0.993.
}
\]

Die Aussage ist eine **analytische Schranke der vollständigen Dynamik auf einem exakt invarianten Quellen-Unterraum**. Es gibt hier keinen numerisch abgeschnittenen Restzustandsraum. Die 64-Fermion/60-Boson-Quelle ist nicht durch vier frei erfundene Matrixeinträge ersetzt worden: Ihre exakte Einschränkung wurde zuerst vollständig geprüft.

Die Zeit in Einheiten \(\hbar=1\) ist ungefähr \(108.83/\Delta\). Diese numerische Orientierung und die gesetzte Mischerstärke sind keine vorhergesagten Naturkonstanten.

## 5. Was dies für die fundamentale Suche ändert

Der konstruktive Anschluss ist klein: **Paarumwandlung → geteilte Zwischenressource → Paar-Rückumwandlung** kann einen Einfermion-Endpunktwechsel bewirken. Für die tatsächliche W-Quelle braucht man dazu weder einen neuen direkten Fermion-Hopping-Term noch die Kontrolle jedes einzelnen der 480 Paarmonome. Ein einzelner Bosonmischer plus eine spezielle Pauli-blockierte Präparation reicht im belegten internen Zeugen.

Offen bleiben aber genau die folgenden Herkunftsfragen:

1. **Operationssatz:** Ist der reine Mischer \(b_1^\dagger b_0+\mathrm{h.c.}\) tatsächlich verfügbar? Eine simultane Fermion-und-Boson-Symmetrie ist nicht automatisch eine unabhängige Bosonoperation.
2. **Präparation:** Wie wird der N=9-Blockerzustand mit dem zugelassenen Operationssatz erzeugt? Ladungserhaltende native Evolution präpariert ihn nicht aus dem N=64-Grundzustand.
3. **Operationaler Raum:** Sind die Endpunktmarken 57 und 58 überhaupt verschiedene räumliche Teile oder nur interne Marken derselben Bank? Die Rechnung allein liefert keine Raumposition.
4. **Gemeinsamer Grundzustand:** Besteht ein entsprechender Mechanismus für die ursprüngliche Entnahmeantwort des nativen N=64-Grundzustands, statt für diesen besonders präparierten Zeugen?
5. **Zwei Banken:** Eine Bosonverbindung zwischen wirklich unabhängigen Banken erhält deren lokale Fermionparitäten. Dieser interne Zeuge hebt jene Schranke nicht auf. Dafür wäre eine ursprünglich geteilte Fermionstruktur oder eine andere insgesamt gerade, lokal ungerade Quelloperation zu konstruieren.

T1–T8, das relativistische Feldwörterbuch und die Herkunft der Raumzeit sind damit nicht geschlossen. Das Ergebnis verkleinert eine konkrete Suche: Statt eines völlig beliebigen neuen Fermionlinks kann jetzt ein bestimmter Bosonmischer mitsamt seinem Quellen- und Präparationsvertrag geprüft werden. Die nachfolgende Quellenprüfung weist diesen Mischer jedoch ausdrücklich **nicht** als Synthese der bisher gewährten Kontrollen aus.

## 6. Anschluss des neuen Chart-/Glue-Vorschlags und exakter Quellen-No-go

Der neue Nutzeranhang vom 15. September 2026 wurde vollständig gelesen:

`/Users/stefanhamann/.codex/attachments/59dc0059-8914-48ca-953d-85933f66e00b/pasted-text.txt`,

SHA-256 `1a75e84b28868dd682e4b2337d6546f275f49321e489b3b23af4754a844d1ac4`.

Die Hypothese, Banken zunächst als überlappende lokale Beschreibungen einer gemeinsamen CAR-Struktur zu untersuchen, passt zum hier konstruierten gemeinsamen Fermion-/Boson-Zwischenraum. **Sie löst den Übergang von Überlappung zu Dynamik aber nicht automatisch.** Bereits zwei nichtorthogonale lokale Moden \(f_A=f_1\), \(f_B=\cos\theta f_1+\sin\theta f_2\) bei H=0 besitzen ein nichtverschwindendes Kreuz-Antikommutator \(\{f_A,f_B^\dagger\}=\cos\theta\), obwohl überhaupt keine Zustandsentwicklung stattfindet. Eine Änderung der Beschreibung und ein dynamischer Transfer müssen getrennt geprüft werden.

### 6.1 Eine nötige Korrektur des vorgeschlagenen Paritätstests

Der Anhang fordert für überlappende Charts einen Intertwiner, der lokal Paritäten ändert, aber mit \(\Pi_A\Pi_B\) kommutiert. **Bei Überlappung ist dieses Produkt nicht automatisch die Gesamtparität.** Im kleinsten gemeinsamen-Moden-Zeugen

\[
A=\{x,s\},\qquad B=\{s,y\}
\]

gilt

\[
\Pi_A\Pi_B=(-1)^{n_x+n_y},
\qquad
\Pi_{\rm global}=(-1)^{n_x+n_s+n_y}.
\]

Die gemeinsame Mode s wurde im Produkt zweimal gezählt und fällt heraus. Die Paarumwandlung \(b^\dagger s f_x\) ist bezüglich \(\Pi_{\rm global}\) gerade, kommutiert aber nicht mit \(\Pi_A\Pi_B\). Der vorgeschlagene Kill-Test würde hier einen legitimen global geraden Überlappungsmechanismus fälschlich aussortieren. Alle vier Identitäten wurden auf dem vollständigen Drei-Fermion-CAR-Raum exakt geprüft.

**Der korrigierte Test muss die globale Parität aus der gemeinsamen CAR-Darstellung selbst verwenden**, nicht aus einem ungeprüften Produkt lokaler Paritäten. Zusätzlich benötigt er eine definierte Anfangspräparation, dynamisch unterschiedliche Endpunktbeobachtungen und einen aus der Quelle stammenden Generator. Passive Chartwechsel allein reichen nicht.

### 6.2 Tatsächlicher endlicher Clock statt unterstellter voller Gruppe

Die Prüfung lädt den gepinnten ursprünglichen Clock-Konstruktor über

`sources/repo/experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/common.py`,

SHA-256 `2cc97522457ecc7e6774d96a25b2581b5d67cd051ae35e28a26f0e98e2adb994`.

Der Konstruktor kontrolliert seine ursprünglichen Quellenpins und die exakte W-Kovarianz. Er liefert tatsächlich

\[
p=(2,0,1,4,3),\qquad s_{\rm Clock}=-1,
\]

und auf Bosonmoden \(A=6k+c\)

\[
G_B e_{6k+c}=-e_{6(p(k\bmod5)+5\lfloor k/5\rfloor)+c}.
\]

Es wird **nicht** vorausgesetzt, dass der Clock der volle Spin(10)×SU(4)-Operationssatz ist. Sein endlicher, direkt reproduzierter Lift reicht für den folgenden Ausschluss.

Schreibe \(M_{ij}=|i\rangle\langle j|+|j\rangle\langle i|\) auf dem Boson-Einteilchenraum. Exakt gilt

\[
G_BM_{01}G_B^\dagger=M_{12,13},\quad
G_BM_{12,13}G_B^\dagger=M_{6,7},\quad
G_BM_{6,7}G_B^\dagger=M_{01}.
\]

Insbesondere

\[
\|[G_B,M_{01}]\|_F^2=4\ne0.
\]

Die native W-Kovarianz impliziert \([G,H]=[G,N_b]=0\) für den gemeinsamen Fock-Lift G. Auch ein gewährter getrennter Gesamt-Casimir von Spin(10) oder SU(4) kommutiert mit diesem tatsächlichen G. Daher liegt

\[
\operatorname{Alg}(H,N_b,G,C_{\rm Spin},C_{\rm Color})\subset\{G\}'
\]

und der spezifische Einzelmischer \(b_1^\dagger b_0+\mathrm{h.c.}\) liegt **nicht** in dieser erzeugten Algebra. Auf den endlichen Ladungssektoren gibt es dabei keine Domänenprobleme; für die volle Hilbert-Darstellung formuliert man dieselbe Aussage mit den erzeugten beschränkten Zeitentwicklungen und Spektraloperationen.

### 6.3 Clock-Mittelung ist möglich, aber der Farb-Cartan sperrt sie weiterhin

Der Clock-Ausschluss allein wäre zu schwach. Die Orbitsumme

\[
M_{\rm orb}=M_{01}+M_{12,13}+M_{6,7}
\]

kommutiert exakt mit \(G_B\). Ihre beiden zusätzlichen Linkblöcke wirken auf den vier Zuständen aus Abschnitt 3 null. Ein neu zugelassener globaler Bosonmischer \(J b^\dagger M_{\rm orb}b\) erzeugt deshalb **denselben** exakt invarianten Vierzustandskanal und dieselbe Transfergrenze. Ein neuer globaler Zusammenhang muss also nicht zwingend den endlichen Clock brechen.

Es gibt jedoch einen zweiten, stärkeren gemeinsamen Erhaltungssatz. Aus dem tatsächlichen Quell-Gewichtswörterbuch wählen wir die zweite SU(4)-Cartankomponente und definieren den gemeinsamen Ladungsoperator

\[
Q=\sum_r q_r n_{f,r}+\sum_A q_A n_{b,A}.
\]

Jeder ursprüngliche Paarterm erfüllt exakt \(q_i+q_j=q_A\); dies wird für alle 480 Quellenpaare geprüft. Der tatsächliche Clock wirkt auf dem Spinindex und lässt die SU(4)-Farbkomponente unverändert. Daher

\[
[Q,H]=[Q,N_b]=[Q,G]=0.
\]

Die getrennten Gesamt-Casimire kommutieren ebenfalls mit diesem Cartan. Diese Aussage erfordert **keine** Verfügbarkeit aktiver kontinuierlicher SU(4)-Kontrollen.

Auf den beiden Bosonkanälen gilt dagegen

\[
q_0=0,\qquad q_1=2,
\]

und auf dem ganzen Boson-Einteilchenraum

\[
\|[Q_B,M_{01}]\|_F^2=8,\qquad
\|[Q_B,M_{\rm orb}]\|_F^2=24.
\]

**Damit sind sowohl der Einzelmischer als auch seine Clock-invariante Orbitsumme aus dem genannten Operationssatz ausgeschlossen.** Die Mittelung beseitigt das Clock-Hindernis, nicht den separaten Farb-Cartan-Erhaltungssatz.

Die tatsächlichen Cartanladungen im Vierzustandsraum sind

\[
(Q_L,Q_{B_0},Q_{B_1},Q_R)=(7,7,9,9).
\]

Dieser Zeuge verändert also eine innere SU(4)-Quantenzahl. Er ist noch deutlicher als ein bloßer Markenwechsel vom Transport **derselben** niedrigenergetischen Fermionmode zwischen zwei räumlichen Banken zu unterscheiden.

### 6.4 Kleinste noch zu suchende Quellressource

Für den hier exakt spezifizierten Zeugen fehlt mindestens eine Operation, die nicht mit dem betrachteten Farb-Cartan des ursprünglichen Systems kommutiert, oder eine aus einer erweiterten globalen Quelle abgeleitete Kopplung mit einer **expliziten Ausgleichsressource für diese Cartanladung**. Ein zusätzlicher aktiver SU(4)-Generator wäre ein neuer Operationsvertrag; außerdem bewegt sein simultaner Fermion-/Boson-Lift im Allgemeinen auch die Blocker und ist nicht mit dem reinen Bosonmischer gleichzusetzen.

Die Befunde schließen nicht alle globalen Glue-Modelle aus. Sie zeigen präzise, warum der konkret schon gelöste Vierzustandstransfer noch keine Herkunftslösung ist und welche neue algebraische Eigenschaft eine echte Quellenfortsetzung besitzen müsste. Für eine überwiegend kinematische Chart-Interpretation muss zusätzlich gezeigt werden, dass diese Erweiterung eine tatsächliche Dynamik und nicht bloß eine Basisumbenennung erzeugt.

## Reproduktion und Status

`verify.py` prüft **307 Bedingungen**, verwendet keine Python-Assertions und reproduziert normal sowie mit `-OO` byteidentische JSON-Ergebnisse. Die Prüfung enthält:

- CAR und Ladungsbuchhaltung für den geteilten Baustein in K=1,2,3;
- die rationale Transfergrenze des klar getrennten Vergleichssterns;
- die Matching-Eigenschaft aller 60 nativen W-Zeilen;
- die volle symbolische Wirkung aller 480 nativen Paarterme auf alle vier Zeugen-Zustände;
- die zusätzliche Mischerwirkung, exakte Invarianz und vollständige Spiegelungszerlegung;
- die rationale Schranke größer 99,3 % bei strikt positiver Bosonfrequenz.
- den tatsächlich konstruierten Clock, den Einzelmischer-Ausschluss und die Clock-invariante Orbitsumme;
- die gemeinsame Farb-Cartan-Erhaltung aller Quellenpaare und den präzisen Ausschluss beider Mischinstrumente;
- das Gegenbeispiel gegen die Gleichsetzung lokaler Paritätsprodukte mit der globalen Parität bei überlappenden Charts.

Die analytischen Ungleichungen sind im Text hergeleitet; die Anzahl der Tests ist kein Ersatz für diese Herleitung und keine Anzahl gelöster Physikprobleme.
