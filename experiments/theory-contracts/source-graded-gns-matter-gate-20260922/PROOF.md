# Graduierte Quellenreparatur: Auswahl des Transfers und Materieanschluss

22. September 2026 · `UR.SOURCE.GRADED_GNS_MATTER_GATE.01` · **PARTIAL**

## Frage, Erfolgskriterium und Ergebnis

Die beiden neu eingereichten Texte konstruieren erst einen 16-dimensionalen GNS-Prozess und danach eine 32-dimensionale graduierte Fortsetzung. Zu prüfen ist, ob deren zusätzliche Auswahl aus dem ursprünglichen TFPT-Transfer folgt und ob dieselben Operatoren den vorhandenen Spin(10)-Materieträger realisieren.

Erfolg verlangt eine Herkunftsableitung und einen tatsächlichen markierten Feldintertwiner. Passende Zustandsdimensionen allein genügen nicht. Ein falscher Intertwiner oder eine nicht ausgewählte Zusatzregel beendet diese konkrete Identifikation; es wird nicht anschließend ein beliebig größeres passendes Weltmodell optimiert.

**Ergebnis:** Der algebraische Kern der Paritätsreparatur und der kubischen Formel ist richtig unter seinen erklärten Voraussetzungen. Es gibt aber eine zweite besonders direkte Fortsetzung der ursprünglichen sechs Kanalbeiträge:

\[
\widetilde T_*=I-N/6,\qquad H_*=-\log(I-N/6).
\]

Sie erhält alle geraden Antworten, ist vollständig positiv als einzelner Kanal auf der angegebenen Cliffordalgebra und besitzt in der GNS-Hilbertinterpretation einen eindeutigen Grundzustand. Sie braucht keine neue algebraische Zahl. Sie ist eindeutig **unter einer anderen, ausdrücklich zusätzlichen Regel**: Jeder vorhandene Kanalbeitrag erhält einen einzelnen Paritätslift, ohne Aufspaltung in eine weitere Paritätsmischung. Das ist keine aus P1/P2 abgeleitete physische Ausführungsregel.

Damit ist das kubische Minimum nicht das voraussetzungslose Minimum des Quellproblems. Es minimiert den Polynomgrad des Hamiltonoperators; die zweite Fortsetzung erhält die unaufgespaltenen Einzelschrittbeiträge. Beide Kriterien sind zu unterscheiden.

Zusätzlich wird ein tatsächlicher geladener CAR-Anschluss innerhalb des 32er-Raums angegeben. Ein anschließender Spin(10)-Zentraltest schließt aber die direkte Identifikation seiner gesamten Operatoralgebra mit den nativen Spinorfeldern aus. Dieser Ausschluss gilt für jeden Operatorgrad in diesem Raum und für das festgelegte Spin(10)-Wörterbuch. Er ist kein allgemeines TFPT-No-go.

## 1. Was aus den Originalquellen schon feststeht

Der ursprüngliche Transfer ist
\[
B=\frac1{18}\begin{pmatrix}13&1&4\\1&13&4\\4&4&10\end{pmatrix},\qquad T=B^6.
\]
`tfpt_1_architecture_e8.tex:648-700` und `tfpt_research_contracts.tex:3860-3895` enthalten die datierte Korrektur: Die sechste Potenz stimmt in der eingesetzten v221-Basis exakt. Die physische Ausführung als sechs lokale Quantenoperationen folgt daraus weiterhin nicht. Der Text bezeichnet den sechsfachen Exponenten als Clock-Exponent und die zehn-dimensionale Transportfortsetzung als Vorschlag.

Die M4-Karte
\[
\Phi(A)=p_0A+p_1\sum_{j=1}^5\Gamma_jA\Gamma_j,
\quad p_0=7/12,\ p_1=1/12
\]
ist die bereits geprüfte markierte Erweiterung. Sie setzt Pauli- und die bezeichnete S5-Kovarianz sowie die Zuordnung der Einzelschrittfaktoren zusätzlich voraus. Ihre Sektoren haben Multiplikatoren 1, 1/3, 2/3 auf 1, 5, 10. Der zugehörige CP-Prozess auf M4 ist von einem positiven Hilberttransfer und von seiner späteren unitären Zeitentwicklung zu unterscheiden.

`tfpt_1_architecture_e8.tex:1524-1555` bezeichnet Quadratic Boundary Locality ausdrücklich als Hypothese über bilineare Nahtdaten und die Auswahl K=2. Das ist nicht das neue Kriterium „kleinster Polynomgrad in der Quellenbesetzung N“. Eine solche Gleichsetzung ist im eingereichten zweiten Text zu Recht ausgeschlossen.

## 2. GNS und Parität: der positive Bestand

Auf L²(M4,tr/4) ist Φ positiv selbstadjungiert und invertierbar. Daher ist H=-log Φ wohldefiniert und hat den eindeutigen Nullvektor I. Linksmultiplikation bewahrt Produkte. Aus der konkreten Sektorfolge folgt
\[
C_{1221}=3^{-(t_1+t_3)}(2/3)^{t_2},\qquad C_{1221}(1,1,1)=2/27.
\]
Dies ist eine korrekte endliche Hilbertkonstruktion. Der Auswahlbeweis, dass die ursprüngliche Quelle diese Interpretation und diese Linksfelder verwendet, folgt nicht aus dem Logarithmus.

Die Identität Γ1Γ2Γ3Γ4Γ5=-I verhindert, alle fünf Γ gleichzeitig als ungerade Generatoren derselben M4-Algebra zu behandeln. Die volle Algebra Cl5(C)=M4⊕M4 behebt genau dieses Problem. Sie hat ungerade χj, eine zentrale ungerade Involution ζ und die gerade Einbettung Γj=ζχj. Der paritätsinvariante Spurzustand hat einen 32-dimensionalen zyklischen GNS-Raum. Die geordneten χ-Monome bilden eine orthonormale Basis.

Identifiziere diese Basis mit Λ^•C5; der Cliffordgrad ist die Quellenbesetzung N=0,…,5. Der Zustand Ω=I ist das leere Außenprodukt. Diese Identifikation beschreibt fünf Quellenmoden, nicht 64 native Materiemoden. Die ursprünglichen Γ-Einfügungen sind in dieser Reparatur gerade.

## 3. Warum die Zwei-Parameter-Klassifikation trägt

Schreibe ein Element als A+ζB. Parität wirkt als Vorzeichenwechsel auf B. Eine paritätserhaltende Erweiterung mit festgelegter gerader Karte besitzt die Form
\[
\widetilde\Phi(A+\zeta B)=\Phi(A)+\zeta\Psi(B).
\]
In den beiden zentralen M4-Blöcken sind ihre beiden Teilkarten (Φ+Ψ)/2 und (Φ-Ψ)/2. Vollständige Positivität der Gesamtabbildung ist äquivalent zur vollständigen Positivität beider Teilkarten.

Der Choioperator von Φ hat Träger in den sechs Vektoren vec(I), vec(Γj). Sind zwei positive Choioperatoren in Summe gleich diesem Operator, müssen beide auf seinem zehn-dimensionalen Kern verschwinden: Für einen Kernvektor ist die Summe zweier nichtnegativer Quadratformen null, also jede einzeln null. Die Spin(5)-Wirkung zerlegt diesen Träger multiplikationsfrei als 1+5. Daraus folgt
\[
\Psi(B)=c_0B+c_1\sum_j\Gamma_jB\Gamma_j,
\quad |c_0|\le p_0,\quad |c_1|\le p_1.
\]
Die Koeffizienten sind wegen Hermitizitätserhaltung reell. Auf den ungeraden Graden 1,3,5:
\[
r_1=c_0-3c_1,\quad r_3=c_0+c_1,\quad r_5=c_0+5c_1,
\quad r_1+r_5=2r_3.
\]
Für den positiven logarithmischen Hilberttransfer werden zusätzlich r1,r3,r5>0 verlangt. Ein eindeutiges Ω verlangt außerdem, dass kein ungerader Faktor eins ist.

Jedes ausschließlich gerade Feldwort aus Ω bleibt im geraden Teil. Deshalb stimmen alle diese Mehrzeitantworten für die ganze Klasse überein. Die allgemeine Unsichtbarkeit ungerader Zeitdaten ist im früheren Contract `source-charged-extension-selection-20260921` bereits vorhanden; neu ist hier die Prüfung dieser konkreten Klasse und ihrer beiden Auswahlregeln.

## 4. Die kubische Rechnung ist richtig, ihr Auswahlkriterium zusätzlich

Sei a=log 3, b=log(3/2). Die geraden Energien sind E0=0,E2=b,E4=a. Ein quadratisches H2(N) interpoliert sie eindeutig, verletzt aber den CP-Vertrag, weil
\[
e^{-E_1}>5/6,\qquad 64/243>(5/6)^8.
\]
Für H3=εN+u C(N,2)+v C(N,3) geben die geraden Energien
\[
u=b-2\epsilon,\quad v=a/4-3b/2+2\epsilon,
\]
\[
E_3=a/4+3b/2-\epsilon,\qquad E_5=5\epsilon+5a/2-5b.
\]
Setze t=e^-ε, A=e^(-a/4-3b/2), D=e^(-5a/2+5b). Die CP-Gleichheit wird
\[
Dt^6+t^2-2A=0.
\]
Mit t²=2Aξ und DA²=1/12 folgt exakt ξ³+3ξ-3=0. Die Ableitung 3ξ²+3 ist positiv. Die einzige reelle Wurzel liegt rational eingeschlossen zwischen 0,8177316738868235 und 0,8177316738868236. Sie erzeugt positive Koeffizienten und einen gültigen CP-Einzelschritt:

| Größe | Wert, neu berechnet |
|---|---:|
| ε | 0,195462288497288682394… |
| u | 0,014540531113587017190… |
| v | 0,057379986999358214670… |
| c0 | 0,582779345285855295663… |
| c1 | -0,079891671227764283397… |
| r1²·2/3 | 0,450954115058234931432… |

Damit stimmt der wesentliche algebraische Kern des zweiten Textes. Er beweist Eindeutigkeit nach Wahl des minimalen Polynomgrades, keine Auswahl dieser Regel aus P1/P2. Die beigefügten 61/39 Prüfgruppen konnten als ursprüngliche Laufartefakte nicht geprüft werden: Die Anhänge enthalten nur Prosa und nicht auflösbare chatgpt-content-reference-Platzhalter. Die hier dokumentierten Rechnungen wurden neu ausgeführt.

## 5. Eine zweite minimale Regel führt zur ursprünglichen Überlebensform

Jede Erweiterung der gegebenen sechs einzelnen Automorphismen kann zusätzlich die Parität θ anwenden. Für den Identitätsbeitrag gibt es id oder θ. Für einen Γj-Beitrag gibt es Ad(Γj) oder θ∘Ad(Γj). Spin(5)-Kovarianz bindet die fünf gleich gewichteten Richtungen an denselben Vorzeichentyp.

**Zusätzliche, präzise Testregel:** Keinen der sechs schon vorhandenen Beiträge in zwei Paritätsausgänge aufspalten. Diese Regel beschreibt vier Ecken (c0,c1)=(±7/12,±1/12) des vollständig klassifizierten Rechtecks. Sie ist kein behauptetes allgemeines Minimum aller möglichen Dilatationen.

| Vorzeichen von c0,c1 | r1,r3,r5 | Positiver Transfer, eindeutiges Ω? |
|---|---|---|
| -,- | -1/3,-2/3,-1 | nein |
| -,+ | -5/6,-1/2,-1/6 | nein |
| +,+ | 1/3,2/3,1 | zweiter Grundzustand ζ |
| +,- | 5/6,1/2,1/6 | ja |

Folglich bleibt unter dieser Regel eindeutig
\[
\widetilde\Phi_*=\frac7{12}\,id+
\frac1{12}\sum_{j=1}^5\theta\circ\operatorname{Ad}(\Gamma_j).
\]
Dies ist eine konvexe Summe von *-Automorphismen, also unital und vollständig positiv. Auf χi wirkt θAd(Γj) negativ genau dann, wenn i=j. Auf einem Monom vom Grad k geben k Beiträge minus und 5-k Beiträge plus. Daher
\[
\widetilde\Phi_*\big|_{\Lambda^k}=\frac7{12}+\frac{5-2k}{12}=1-k/6.
\]
Auf dem GNS-Raum folgt **die vollständige Operatorgleichheit**
\[
\widetilde T_*=I-N/6,\qquad H_*=-\log(I-N/6).
\]
Alle sechs Faktoren sind positiv; eins tritt nur bei N=0 auf. Die Energien sind
\[
(0,\log(6/5),\log(3/2),\log2,\log3,\log6).
\]
Die neutralen Energien und alle neutralen Mehrzeitantworten bleiben exakt unverändert. Die neuen Entscheidungstests lauten
\[
x=r_5=1/6,\qquad y=r_1=5/6,
\]
\[
C^\chi_{1221}(1,1,1)=25/54,
\quad C^\chi_{123321}(1,1,1,1,1)=25/162.
\]
Auf dem geraden Raum N=2n ist der Faktor 1-N/6 gerade 1-n/3; in sechs Schritten entsteht die ursprüngliche Überlebensform (1-n/3)^6. Die Erweiterung auf ungerade N ist der neue bedingte Schritt, nicht schon im ursprünglichen Dreizustandstransfer enthalten.

H* besitzt auf N=0,…,5 eine Newtonentwicklung bis Grad fünf mit nichtverschwindenden Koeffizienten vierten und fünften Grades. Es verliert also gegen H3 beim Polynomgrad, gewinnt aber bei der Regel „keine zusätzliche Aufspaltung vorhandener Paritätslifts“. Das ist eine genaue Entscheidung über den Minimalitätsbegriff, kein Widerspruch der beiden Rechnungen.

Im kubischen Kandidaten liegen beide Betragsungleichungen strikt innerhalb des Rechtecks. Seine vier Gruppen von Gewichten sind (p0±c0)/2 und (p1±c1)/2; alle sind positiv. Er mischt folglich die beiden möglichen Paritätslifts jedes ursprünglichen Kraus-Orbits. Das ist erlaubt, aber durch den ursprünglichen neutralen Transfer nicht ausgewählt.

## 6. Ein tatsächlicher geladener CAR-Anschluss auf demselben Raum

Für beide gerade überprüften Kandidaten steigen die Energien E0<…<E5 strikt. Ihre Spektralprojektoren Pk sind daher gleichzeitig die bekannten Gradprojektoren. Definiere ausschließlich mit vorhandenen χj und diesen Projektoren:
\[
a_j=\sum_{k=1}^5P_{k-1}\chi_jP_k,\qquad
a_j^\dagger=\sum_{k=0}^4P_{k+1}\chi_jP_k.
\]
Auf der geordneten Monombasis sind dies die üblichen signierten Lösch- und Einfügeoperationen. Daraus folgen exakt die CAR, χj=aj+aj† und ajΩ=0. Es werden keine Zustandsrichtungen hinzugefügt. Die Partner i(aj-aj†) sind in der ursprünglichen Cl5-Linksalgebra nicht enthalten, liegen aber in der durch χj und H erzeugten Algebra. Die CAR-Darstellung ist irreduzibel auf Λ^•C5, also
\[
\operatorname{Alg}^*\{\chi_j,H\}=M_{32}.
\]
Die Quellenzeit selbst macht hier die nötige Operatorerweiterung explizit. Das ist eine Verbesserung gegenüber einer bloßen Dimensionsidentifikation.

Auf dem so rekonstruierten CAR-Raum wirkt U(5) durch Γ(g)=Λ^•g. N und H=f(N) sind invariant. Mit dem **aus TFPT übernommenen, nicht hier ausgewählten** 3+2-Generator
\[
Y=\sum_jy_j a_j^\dagger a_j,
\qquad y=(-1/3,-1/3,-1/3,1/2,1/2)
\]
gilt [Y,aj†]=yj aj† und [Y,H]=0. Die geladenen Zweipunktantworten sind wirklich
\[
\langle\Omega|a_i e^{-\tau H}a_j^\dagger|\Omega\rangle
=\delta_{ij}e^{-\tau E_1}.
\]
Normierte geordnete k-Teilchen-Erzeuger besitzen entsprechend e^-τEk und die antisymmetrische Gram-Matrix. Für H* lautet der Einteilchenfaktor (5/6)^τ, für den kubischen Kandidaten exp(-0,195462…τ). Das sind verschiedene physische Antworten bei gleichem neutralem Bestand.

Auf Λ^even C5 reproduziert Y die standardmäßige 16er-Gewichtsliste: 6Y=(-4,-3,0,1,2,6) mit Häufigkeiten (3,2,1,6,3,1). Diese Aussage betrifft Trägerzustände. Sie erzeugt noch keine 16 ungeraden Spinorfeldoperatoren.

Eine weitere Grenze ist sichtbar: Die Cl5-Linksalgebra selbst bleibt unter dieser U(5)-Wirkung nicht geschlossen; bereits eine Phasendrehung eines Modus mischt χj mit seinem neuen Majoranapartner. Die U(5)-Fortsetzung gilt auf der größeren Operatoralgebra M32. Die ursprüngliche CP-Karte ist damit nicht automatisch als U(5)-kovarianter Kanal auf M32 bestimmt. Eine allgemeine CP-Erweiterung allein würde auch ihre Herkunft nicht auswählen.

## 7. Der Spin(10)-Materietest scheitert auf diesem einen Quellenraum

Die zehn Majoranas liefern auf Λ^•C5 die übliche Spin(10)-Diracdarstellung S+⊕S-. Das zentrale Element z=-1, eine volle 2π-Drehung in einer Cliffordebene, wirkt auf beiden Hälften als -I32. Deshalb wirkt es auf **jedem** Operator O∈End(C32) durch Konjugation trivial:
\[
\rho(z)O\rho(z)^{-1}=O.
\]
Auf dem nativen Spinorfeld F=(bar16,bar4) wirkt dasselbe Spin(10)-Element dagegen als -1. Für einen äquivarianten Feldtransfer J:F→End(C32) wäre somit
\[
J(-f)=\rho(z)J(f)\rho(z)^{-1}=J(f),
\]
also J=0. Dieser kurze Beweis erfasst auch beliebig nichtlineare Operatorwörter und die bereits vergrößerte volle Algebra M32. Eine skalare Familien-Determinantendrehung repariert diese zentrale Wirkung nicht.

Anschaulich trägt der Hilbertraum Spinorzustände; seine internen Übergangsoperatoren tragen Tensorwirkungen. Die 16 Zustände eines Halbspinors sind nicht die 16 unabhängigen Fermionfelder einer Fockbank. Das entspricht hier der Identität End(S+⊕S-)=Cl10 als Spin(10)-Modul mit Außenpotenz-/Tensordarstellungen.

### Auch ein anderer Spin(10)-Lift derselben Spin(5)-Wirkung genügt nicht

Der Ausschluss lässt sich über die kanonische Wahl hinaus absichern. Fixiert sei die in der Konstruktion verwendete diagonale Untergruppe Spin(5)⊂Spin(10), bei der der 10er-Vektor als 5⊕5 zerfällt. Der 32er-Quellenraum trägt dort
\[
\Lambda^\bullet\mathbb C^5=2\cdot1\oplus2\cdot5\oplus2\cdot10.
\]
Die einzigen nichttrivialen komplexen irreduziblen Spin(10)-Darstellungen mit Dimension höchstens 32 sind 10,16,bar16. Das folgt hier direkt aus der Weyl-Dimensionsformel: Die fünf Fundamentalgewichte haben Dimensionen (10,45,120,16,16). Die sechs Summen zweier der kleinen Fundamentalgewichte haben Dimensionen 54,144,144,126,210,126. Alle liegen über 32; die Formel ist in jedem dominanten Dynkinlabel monoton. Damit sind auch alle höheren Fälle ausgeschlossen.

Die Spin(10)-1 und -10 enthalten unter der festgelegten Spin(5)-Einbettung keine adjungierte Spin(5)-10. Jede Halbspinor-16 enthält genau eine, denn Λ^even C5=1⊕10⊕5 und Λ^odd C5=5⊕10⊕1. Um die beiden vorhandenen Spin(5)-10 zu erhalten, sind also zwei Halbspinoren nötig. Sie verbrauchen bereits alle 32 Dimensionen. Jede solche Spin(10)-Fortsetzung besteht aus zwei Halbspinoren und hat dieselbe zentrale Wirkung -I32.

Dies beseitigt die bloße Umwahl des Spin(10)-Lifts auf demselben Raum bei festgehaltener Spin(5)-Einbettung als Reparatur. Eine andere Untergruppeneinbettung oder ein anderes Materiewörterbuch wäre eine neue zu begründende Identifikation.

**Scope:** Ausgeschlossen ist der direkte Spin(10)-äquivariante Rückweg von diesem einzelnen Quellenraum in das festgehaltene native Materiewörterbuch, auch für andere Fortsetzungen derselben diagonalen Spin(5)-Wirkung. Nicht ausgeschlossen sind ein anders hergeleitetes SM-Wörterbuch, globale Sektorwechsel, projektive Endpunkte oder größere physisch begründete Feldräume. Sie werden hier nicht frei hinzugebaut. Der allgemeine Zentraltest war als Methode im bisherigen Quellenaudit bereits bekannt; neu geprüft wird seine Wirkung auf genau die vorgeschlagene 32er-Reparatur.

## 8. Konsequenz für den verlangten Gesamtabschluss

Die beiden Anhänge helfen, weil sie eine echte graduierte Quellklasse bestimmen. Aus ihr lässt sich jetzt sogar ein geladener CAR-Prozess ohne neue Hilbertraumrichtungen gewinnen. Sie liefern jedoch nicht die finale TFPT-Lösung.

Die konkrete nächste Herkunftsfrage ist zweistufig:

1. Wählt der ursprüngliche Collar-/Nahtprozess überhaupt diesen M4-Mikroschritt und dessen Paritätslift aus? Unaufgespaltener Lift sagt (x,y)=(1/6,5/6), kubische Minimalität sagt ungefähr (0,183321,0,822454). Diese Werte sind Kandidatentests; keines der Paare wird als universelle TFPT-Vorgabe gesetzt.
2. Wo erzeugt dieselbe Originalquelle Operatoren, auf denen das Spin(10)-Zentrum tatsächlich negativ wirkt? Innerhalb End(C32) ist dies unter der festgelegten Darstellung unmöglich. Genau dafür werden ein original begründeter Sektorwechsel oder der bereits vorhandene native Materieraum samt Quelloperator benötigt.

Die bisherige gemeinsame Verbindungsformel auf W_m und der Collar-/Familienholonomietest bleiben relevant. Die neuen Texte ersetzen deren fehlende Eingaben nicht. Auch T3-T8 verschwinden nicht, wenn eine endliche Quellenklasse eindeutig wird.

## 9. Prüfstand, Quellen und Firewall

`checker.py` berechnet Clifford-/CAR-Identitäten, die ursprüngliche gerade Karte, die vier unaufgespaltenen Lifts, die kubische Lösung, Spektral-Erzeuger, tatsächliche Ladungen und Mehrzeitantworten sowie den zentralen Operatorausschluss. Die Ganzzahlmatrizen werden exakt verglichen. Transzendente Zahlen werden mit 70 Dezimalstellen ausgewertet und als numerisch ausgewiesen; die eindeutige reelle Wurzel und ihr rationales Intervall sind zusätzlich exakt geprüft. Normal- und -OO-Ergebnis werden verglichen. Allgemeine Sätze beruhen auf den vorstehenden Beweisen, nicht auf einer endlichen Zahl Stichproben.

Primäre lokale Eingaben: beide Nutzeranhänge; ursprünglicher markierter CP-Bericht; die zitierten Architektur-/Contractstellen; `source-charged-extension-selection-20260921/PROOF.txt`; `source-operator-origin-20260920/family_intertwiner/PROOF.md`; `source-joint-spin-family-lift-20260922/PROOF.md`; `source-boundary-lift-selection-20260922/PROOF.md`. SHA-256-Pins stehen in `source_pins.json`.

Wissenschaftliche Primärliteratur für die Begriffsgrenzen:

- Lang, Liegener, Thiemann, *Hamiltonian Renormalisation I: Derivation from Osterwalder-Schrader Reconstruction*, [arXiv:1711.05685](https://arxiv.org/abs/1711.05685). Die Rekonstruktion bezieht Hilbertraum, Hamiltonoperator und Grundzustand auf passende vollständige euklidische Daten; sie wählt nicht die fehlenden TFPT-Quellenannahmen.
- Wolf, Eisert, Cubitt, Cirac, *Assessing non-Markovian dynamics*, [arXiv:0711.3172](https://arxiv.org/abs/0711.3172); Wolf, Cirac, *Dividing Quantum Channels*, [arXiv:math-ph/0611057](https://arxiv.org/abs/math-ph/0611057). Ein positiver diskreter Kanal und seine Einbettung in einen kontinuierlichen Kanalprozess sind verschiedene Anforderungen. Für die vorliegende Arbeit ist kein erneuter vollständiger Logarithmuszweig-Audit des ersten Anhangs beansprucht.

Keine neue unabhängige mathematische Begutachtung und keine erneute Ausführung der gesamten TFPT-Suite. Forschung innerhalb `experiments/`; keine Paper-, Ledger- oder Scorecard-Promotion. **Keine physischen T1-T8-Tore geschlossen.**
