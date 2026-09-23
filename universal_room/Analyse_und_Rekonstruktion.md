# TFPT und Universalraum: Analyse, Gegenproben und bedingte Rekonstruktion

**Stand: 14. September 2026. Forschungsnotiz für Stefan Hamann.**

## 0. Reichweite und Ergebnis

Diese Untersuchung trennt vier Arten von Aussagen: Ergebnisse der bereitgestellten Manuskripte, hier unabhängig nachgerechnete endliche Identitäten, hier formulierte bedingte Konstruktionen und weiterhin offene physikalische Herkunftsfragen. Eine Konstruktion unter ausdrücklich gewählten Voraussetzungen ist kein Nachweis, dass die Natur diese Voraussetzungen auswählt.

Die stärkste gemeinsame Formulierung beider Forschungsrichtungen lautet:

> Der Universalraum ist ein phasentreuer, komponierbarer Zusammenhang zulässiger Prozesse. TFPT beschreibt eine ausgezeichnete algebraische Auslesung davon. Aus hinreichend vollständigen Auslesedaten lässt sich die minimal beobachtbare Prozessdarstellung rekonstruieren, nicht ohne Weiteres eine einzigartige verborgene Mikrophysik.

Die konkreten Fortschritte dieser Untersuchung sind:

1. Der Unterschied zwischen einem harten Verbot symmetrischer Paarzustände und ihrer energetischen Unterdrückung wird präzisiert. Ein explizites Vermittlermodell erzeugt die gewünschte positive Austauschenergie.
2. Auf demselben Vierträgerzustand wird eine relationale Uhr mit vier orthogonalen Anzeigen konstruiert. Ihr diskreter Tick verwendet nur Pauli und CNOT. Das ist ein anderer Clockoperator als der ausgezeichnete Familienzyklus.
3. Der passive Prozess auf 60 Strahlen wird exakt auf 30 lineare Koordinaten komprimiert. Das präzisiert die Reichweite der behaupteten Minimalität des vollen CQ Zustands.
4. Die Rückrichtung von markierten D5 und A3 Faktoren über eine diagonale Z4 Verklebung zu E8 wird explizit formuliert und ihre Wurzelzahlen unabhängig nachgerechnet.
5. Ein bedingter Rekonstruktionssatz für vollständige Operationskorrelationen wird angegeben. Er identifiziert präzise, welche Daten noch fehlen: insbesondere die Auswahl des positiven Quellfunktionals und der Zusammensetzung.

Keine dieser Aussagen schließt die physikalischen Bedingungen T1 bis T8.

## 1. Quellen und Versionsgrenze

**S1:** `tfpt_compiler_universalraum_2026-09-13.pdf`, 21 Seiten, tatsächlich vorliegende Version 1.0. Relevante Stellen: Architektur S. 4 bis 8; empirische Grenzen S. 9 bis 12; Prozess S. 13 bis 17; Abschlussbedingungen S. 18 bis 19.

**S2:** `tfpt_anschluss_zellen_seam_2026-09-14.pdf`, 7 Seiten. Relevante Stellen: Hüllensatz und Uhr S. 2 bis 3; Ketten S. 4 bis 5; Rekonstruktion des Ringgenerators S. 5; Verklebung und Anschlussaufgaben S. 6.

**S3:** `TFPT_UNIVERSALRAUM_INVERSION_2026-09-14.md`. Relevante Abschnitte: 4 zur Autonomie; 5 zur Kontextregel; 6 zur Clockblockade; 7 zu Registern und Rekurrenz; 8 zur Faktorisierung.

S2 bezieht sich auf eine erweiterte Manuskriptversion 1.1 und auf Quellprüfer, die nicht Bestandteil der drei vorliegenden Dateien sind. Die hier ausgeführten Rechnungen sind daher **keine Wiederholung dieser Originalprüfer**. Sie rekonstruieren die in den Dokumenten angegebenen endlichen Modelle eigenständig. Insbesondere wurden die numerischen Kettenrechnungen bis 16 Träger, die Rechnung des Rotor/CAR Modells und die zweischleifige Kopplungsentwicklung nicht erneut ausgeführt.

Die Eingabedateien sind in `manifest.json` mit SHA256 festgehalten. `audit.py` konstruiert die Standardkontexte zweier Qubits aus Paulimatrizen. Das entspricht der im Manuskript identifizierten Stabilizergeometrie, ist aber kein erneuter phasentreuer Import des ursprünglichen E8 Quellcodes.

## 2. Was TFPT bereits leistet

Der fünfteilige komplexe Träger liefert

\[
S^+=\Lambda^{\mathrm{even}}\mathbb C^5,
\qquad \dim S^+=1+10+5=16.
\]

Die passende gerade Verklebung von D5 und A3 besitzt Rang acht, Index vier und Determinante eins. Das ist strukturell wesentlich mehr als eine Dimensionsgleichheit. Die adjungierte E8 Darstellung zerfällt als

\[
248=(45,1)+(1,15)+(16,4)+(\overline{16},\overline4)+(10,6).
\]

Die in S1 angegebenen Ladungen einer Spin(10) Familie und ihre Anomaliesummen sind endliche algebraische Aussagen. Sie ersetzen kein chirales wechselwirkendes Feldmaß. Insbesondere folgt aus der Rechnung `(16−1)/5=3` für sich allein keine Existenz dreier propagierender Familien.

Auch eine exakt berechnete Kopplungsformel muss von ihrer physikalischen Identifikation unterschieden werden. S1 nennt für den Modellwert von alpha invers `137.0359992168407...` und vergleicht ihn ausdrücklich mit CODATA 2022, nicht mit einer unabhängigen Messung von 2026. Leptonverhältnisse, einzelne Neutrinowinkel und die skalare kosmologische Normierung enthalten dokumentierte Spannungen. S2 berichtet zusätzlich eine Spannung des untersuchten SO(10) Zweiges beim Protonzerfall; diese Rechnung ist bedingt durch Eichentscheidung, Schwellenbehandlung und den dortigen eingeschränkten zweischleifigen Lauf.

Die Universalraumrekonstruktion muss dieselben Ausgaben aus demselben Ursprung erzeugen. Sie darf vorhandene negative Befunde nicht durch beliebig neue Übertragungsregeln neutralisieren.

## 3. Die zwei Richtungen sind unterschiedliche Rekonstruktionspfeile

Schreibe B für die markierte TFPT Auslesung und U für einen vollständigen Prozess. Dann sind zwei Abbildungen zu unterscheiden:

\[
\mathcal P:U\longmapsto B,
\qquad
\mathcal R:B\longmapsto \widehat U.
\]

Die erste ist eine Auslesung, die zweite eine Rekonstruktion aus gegebenen Daten. Dass U ontologisch grundlegender sein könnte, steht nicht im Widerspruch dazu, dass wir U erkenntnistheoretisch aus B rekonstruieren.

Eine sinnvolle Zielbedingung lautet

\[
\mathcal P\mathcal R(B)\simeq B.
\]

Die umgekehrte Identität

\[
\mathcal R\mathcal P(U)\simeq U
\]

verlangt dagegen vollständige, prozessunterscheidende Daten. Aus den heute verwendeten eingeschränkten Schatten folgt sie nicht.

Ein allgemeiner Gegenbeweis gegen uneingeschränkte mikroskopische Eindeutigkeit ist einfach: Ergänze jeden Kandidaten um einen ungekoppelten Faktor K und lasse sämtliche zugelassenen Operationen und Messungen dort trivial wirken. Alle zugelassenen Antworten bleiben gleich. Deshalb ist Eindeutigkeit zunächst nur für die **minimal beobachtbare Darstellung** erreichbar.

Dieser Zusatzfaktor ist kein physikalischer Vorschlag. Er ist eine Gegenprobe gegen zu starke Rekonstruktionsbehauptungen.

## 4. Die Kontextregel: richtige Konstruktion, noch kein Auswahlprinzip

S3 konstruiert eine Faktorisierung

\[
B=\sum_{j=1}^{7}P_j
\]

in Permutationsmatrizen. Wenn G die Symmetriegruppe von B ist, gilt unmittelbar

\[
\frac{1}{7|G|}\sum_{g\in G}\sum_{j=1}^{7}gP_jg^{-1}
=\frac{1}{7|G|}\sum_{g\in G}gBg^{-1}
=\frac B7.
\]

Diese Identität erklärt den kovarianten Abschluss. Sie erklärt nicht unabhängig, warum die sieben Summanden gleich gewichtet und in der angenommenen Weise ausgeführt werden sollen.

Schon die Familie

\[
K_a=aI+\frac{1-a}{6}(B-I),\qquad 0\leq a\leq1,
\]

ist stochastisch, kovariant und ausschließlich auf der erlaubten Inzidenz getragen. Der Punkt `a=1/7` wird durch diese Bedingungen allein nicht ausgewählt.

Der Fortschritt in S3 ist daher eine konkrete symmetrische Realisierung des gewählten Übergangs. Die verbleibende Herkunftsfrage umfasst nicht nur den kohärenten Lift, sondern auch das physikalische Prinzip, das diese Mischung und ihre Gewichte auswählt.

## 5. Autonomie: drei Prozessklassen dürfen nicht vermischt werden

### 5.1 Der passive Prozess auf 60 Strahlen

Für die 15 vollständigen Pauli Kontexte C und ihre Projektoren Pi(C,s) definiert S1

\[
T_{(D,t),(C,s)}=\frac{B_{DC}}7\operatorname{Tr}(\Pi_{D,t}\Pi_{C,s}).
\]

C bezeichnet im Folgenden auch die Aggregationsmatrix für Kontextwahrscheinlichkeiten. E dekodiert eine Strahlverteilung als Dichteoperator. Es gilt exakt

\[
CT=KC,\qquad ET=\mathcal DE,
\]

mit

\[
\mathcal D(\rho)=\frac37\rho+\frac17I\operatorname{Tr}\rho.
\]

**Auf diesem Zustandsbereich und unter genau dieser Fortsetzung besitzt der Systemschatten also eine autonome Dynamik.** Das ist bereits eine Aussage von S1.

### 5.2 Explizite Kompression auf 30 Koordinaten

Schreibe den nach einer Kontextmessung vorhandenen CQ Zustand als

\[
X=\bigoplus_C\rho_C,
\qquad
\rho_C=\sum_s p_{C,s}\Pi_{C,s}.
\]

Jeder Block ist in seinem eigenen Kontext diagonal. Setze

\[
q_C=\operatorname{Tr}\rho_C,
\qquad
r_v=\operatorname{Tr}\left(P_v\sum_C\rho_C\right)
\]

für die 15 nichttrivialen Paulis. Dann ergibt ein Schritt

\[
\rho_D'=\frac14\left[(Kq)_D I+
\frac17\sum_{v\in D}r_vP_v\right].
\]

Begründung: Ein Pauli v ist in genau drei Kontexten enthalten. Alle Kontexte, die v enthalten, sind untereinander inzident. Die Koeffizienten dieser Richtung werden deshalb von der nächsten Kontextmessung in einer einzigen Summe zusammengeführt.

Die Auslesung der einzelnen Ergebnisse lautet

\[
p'_{D,t}=\frac{(Kq)_D}{4}
+\frac1{28}\sum_{v\in D}r_v\operatorname{Tr}(P_v\Pi_{D,t}).
\]

Damit schließen sich die Gleichungen

\[
q'=Kq,\qquad r_v'=\frac37r_v.
\]

Es reichen 15 Kontextgewichte und 15 Pauliwerte, insgesamt 30 lineare Koordinaten oder 29 freie reelle Parameter nach Normierung. Der zulässige Bereich ist eine beschränkte konvexe Teilmenge, nicht ganz R hoch 29.

Unabhängig exakt geprüft:

\[
\operatorname{rank}T=30,
\quad \operatorname{rank}\binom CE=30,
\quad \ker T=\ker C\cap\ker E.
\]

Das Spektrum ist

\[
1^{[1]},\ (3/7)^{[15]},\ (2/7)^{[9]},\ (-2/7)^{[5]},\ 0^{[30]}.
\]

Die Kompression betrifft passive Fortsetzungen unter T. Sofortige zusätzliche Messungen oder neue Eingriffe können Informationen verlangen, die diese Beschreibung nicht enthält. Insbesondere wird nicht behauptet, dass ein allgemeiner kohärenter Prozess nur 29 Parameter hätte.

### 5.3 Allgemeine CQ Zustände und kohärente Register

Bei beliebigen CQ Blöcken, die nicht bereits in ihren jeweiligen Kontexten diagonal sind, müssen System und Kontextmarginalie die nächste Ausgabe nicht festlegen. Korrelationen können relevant sein. Ein solches Zeugenpaar widerlegt eine bestimmte Kompression, aber beweist allein keine globale Minimalität von 240 linearen Koordinaten.

Bei kohärenter Wiederverwendung eines Aufzeichnungsregisters kommen außerdem Offdiagonalelemente zwischen Registerwerten hinzu. Dieser größere Zustand ist im Allgemeinen **kein CQ Zustand**. Deshalb kann der volle CQ Zustand nicht pauschal als autonome Hülle auch dieser kohärenten Ausführungen bezeichnet werden.

Die korrekte Aussage der Inversion lautet: Der einzelne Systemzustand bestimmt nicht alle Fortsetzungen, wenn korrelierte oder kohärent aufbewahrte Register zugelassen sind. Das ist eine konkrete Gedächtnisaussage, keine alleinige Entscheidung darüber, was ontologisch fundamental ist.

## 6. Der Hüllensatz: gültiger Satz, zusätzliche physikalische Prämisse

Für `P+_ij=(I+S_ij)/2` gilt:

\[
P^+_{ij}\psi=0\ \text{für alle Paare}
\quad\Longrightarrow\quad
\psi\in\Lambda^N\mathbb C^4.
\]

Für N=4 ist der Raum eindimensional; für N mindestens fünf verschwindet er. Dieser Satz ist korrekt. Er gilt auch für gemischte Zustände, wenn deren Träger in den gemeinsamen Kern fällt.

Nicht aus ihm folgt, dass die fehlende Darstellung Sym²(4) in der **adjungierten Lie Algebra** alle symmetrischen **Mehrträgerzustände** verbietet. Ein Lie Klammerkanal, eine Darstellung der Generatoren und ein Tensorproduktraum physikalischer Zustände sind verschiedene Objekte.

Außerdem existieren antisymmetrische Räume auch für N=1,2,3. Genau vier Träger folgen als maximal gefülltes eindeutiges Singulett erst mit der entsprechenden Vollständigkeitsbedingung.

### 6.1 Harter Ausschluss gegen weiche Energieauswahl

Wird die Paarbedingung als hartes Verbot aller anderen Zustände verstanden, bleibt der isolierten Zelle nur `C Omega`. Ein lokaler Tick c erzeugt nach S2 jedoch

\[
\langle P^+_{1j}\rangle=5/8,
\qquad
\langle H_{\mathrm{tet}}\rangle=15J/8.
\]

Dieser Zustand liegt außerhalb des hart erlaubten Raums. Man kann nicht gleichzeitig jede solche Komponente verbieten und genau diesen Eingriff als erlaubte physikalische Dynamik verwenden.

Das schließt eine relationale Beschreibung eines festen Gesamtzustands nicht aus. Es verbietet den angegebenen lokalen Tick als Operation innerhalb der harten eindimensionalen Zellhülle.

Die konsistente dynamische Alternative ist eine **weiche energetische Auswahl**: Omega ist der Grundzustand, symmetrische Paaranteile sind erlaubte Anregungen mit positiver Energie. In dieser Lesart ist J ein Energiemaß. Seine absolute Kalibrierung und seine Relation zu anderen Kopplungen bleiben physikalisch relevante Eingaben, solange sie nicht abgeleitet sind.

### 6.2 Derselbe Zustand wählt nicht denselben Generator

Schon die drei Kanten eines zusammenhängenden Sterns erzwingen auf vier Trägern dieselbe vollständige Antisymmetrie. Daher besitzen

\[
H_{\mathrm{voll}}=J\sum_{i<j}P^+_{ij}
\]

und

\[
H_{\mathrm{Stern}}=J(P^+_{01}+P^+_{02}+P^+_{03})
\]

denselben eindeutigen Grundzustand Omega. Ihre Lücken sind aber `2J` beziehungsweise `J/2`.

Allgemeiner genügt jeder zusammenhängende Graph mit positiven Kantengewichten für den gemeinsamen antisymmetrischen Kern, weil seine Kantentranspositionen die ganze symmetrische Gruppe erzeugen. Der Zustand allein bestimmt weder den Graphen noch seine Gewichte.

Dies widerlegt nicht die in S2 ausdrücklich eingeschränkte Ringrekonstruktion innerhalb einer eingefrorenen lokalen Operatorliste. Es zeigt, warum diese Einschränkung nicht weggelassen werden darf.

### 6.3 Robustes Zustandszertifikat

Aus der Lücke des vollständigen Tetramers folgt

\[
H_{\mathrm{tet}}\geq2J(I-|\Omega\rangle\langle\Omega|).
\]

Für jeden gemischten Zustand rho ergibt sich

\[
1-\langle\Omega|\rho|\Omega\rangle
\leq\frac{\operatorname{Tr}(H_{\mathrm{tet}}\rho)}{2J}
=\frac12\sum_{i<j}\langle P^+_{ij}\rangle.
\]

Das macht die sechs Paarantworten zu einem robusten Zertifikat des Zellzustands. Sie zertifizieren nicht automatisch den Generator.

## 7. Expliziter Vermittler: die energetische Auswahl lässt sich konstruieren

Dies ist eine **neue bedingte Modellkonstruktion dieser Untersuchung**, keine bereits bewiesene Herkunft aus TFPT.

Sei der niedrige Paarraum

\[
\mathcal H_L=\mathbb C^4\otimes\mathbb C^4
=\mathcal H_+\oplus\mathcal H_-,
\qquad \dim\mathcal H_+=10,\quad\dim\mathcal H_-=6.
\]

Führe einen virtuellen Raum `H_M` der Dimension sechs mit positiver Energie Delta ein. W sei die natürliche partielle Isometrie vom antisymmetrischen Paarraum auf diesen Vermittler:

\[
W^\dagger W=P_-,\qquad WW^\dagger=I_6.
\]

Der SU(4) kovariante Paarhamiltonoperator ist

\[
H=\begin{pmatrix}
0_{16}&gW^\dagger\\
gW&\Delta I_6
\end{pmatrix},\qquad\Delta>0.
\]

Die zehn symmetrischen Zustände bleiben bei Energie null. Jeder antisymmetrische Zustand bildet mit seinem Vermittlerpartner denselben Zweierblock:

\[
\begin{pmatrix}0&g\\g&\Delta\end{pmatrix}.
\]

Seine Eigenwerte sind

\[
E_\pm=\frac{\Delta\pm\sqrt{\Delta^2+4g^2}}2.
\]

Im niedrigen effektiven Band, nach einer gemeinsamen Energieverschiebung, ergibt sich genau

\[
H_{\mathrm{eff}}=J_{\mathrm{eff}}P_+,
\qquad
J_{\mathrm{eff}}=\frac{\sqrt{\Delta^2+4g^2}-\Delta}{2}>0.
\]

Für kleine `g/Delta` gilt

\[
J_{\mathrm{eff}}=g^2/\Delta+O(g^4/\Delta^3).
\]

Die antisymmetrische Struktur bestimmt hier den zugelassenen Vermittlungskanal; die energetische Absenkung dieses Kanals erklärt das positive Vorzeichen der relativen symmetrischen Energie.

**Was gewonnen ist:** ein expliziter Mechanismus statt eines bloßen Vorzeichens oder eines Verbots. **Was nicht gewonnen ist:** die quellenseitige Auswahl des Vermittlers, seines Abstands Delta, seiner Stärke g, des Graphen und der übrigen möglichen virtuellen Kanäle. Das Modell enthält nicht die vollständigen Spin(10) Freiheitsgrade des E8 Zweiges. Bei mehreren gleichzeitig gekoppelten Kanten sind höhere Ordnungen und zusätzliche Mehrkörperterme gesondert zu kontrollieren.

### 7.1 Korrektur des in S2 formulierten Anschlusskanals

Auf S. 6 von S2 steht im nächsten Schritt ein gemischtes Produkt mit Trägeranteil `4 tensor bar4`, das auch in `(10,6)` landen soll. Das kann als SU(4) Tensorprodukt so nicht stimmen:

\[
4\otimes\overline4=1\oplus15,
\qquad4\otimes4=6\oplus10.
\]

In der Z4 Gradierung von E8 gilt

\[
\mathfrak g_0=(45,1)\oplus(1,15),\quad
\mathfrak g_1=(16,4),\quad
\mathfrak g_2=(10,6),\quad
\mathfrak g_3=(\overline{16},\overline4),
\]

und damit

\[
[\mathfrak g_1,\mathfrak g_1]\subset\mathfrak g_2,
\qquad
[\mathfrak g_1,\mathfrak g_3]\subset\mathfrak g_0.
\]

Ein mehrstufiger Austausch kann beide Arten von Vertizes enthalten. Die Vertizes dürfen aber nicht als derselbe direkte Tensorproduktkanal behandelt werden.

## 8. Eine funktionierende relationale Uhr mit vier Anzeigen

S3 untersucht einen bestimmten Generator auf den drei übrigen Trägern, aufgebaut aus gleichen Paarvertauschungen. Dieser besitzt nicht die nötige Energieaufspaltung für die dort gewählte Viererlesart. Das ist eine Einschränkung dieses Ansatzes, kein allgemeines Verbot einer Viereruhr auf dem Tetramer.

### 8.1 Diskrete Konstruktion mit vorhandenen Gattern

Sei

\[
R|j\rangle=|j+1\bmod4\rangle.
\]

In der Zweiqubitkodierung `j=2a+b` ist

\[
R=(I\otimes X)\,\mathrm{CNOT}_{b\to a}.
\]

Es werden also nur ein Pauli X und ein CNOT innerhalb des Viererträgers verwendet. `R^4=I` und `det R=−1`.

Zerlege das Singulett nach dem ersten Träger:

\[
|\Omega\rangle=\frac12\sum_{t=0}^{3}|t\rangle_C|\chi_t\rangle_S.
\]

Die vier Zustände chi sind normiert und paarweise orthogonal. Jede Anzeige tritt mit Wahrscheinlichkeit ein Viertel auf.

Für jedes Viererunitär A gilt

\[
A^{\otimes4}|\Omega\rangle=\det(A)|\Omega\rangle.
\]

Für R folgt daher

\[
R^{\otimes3}|\chi_t\rangle=-|\chi_{t+1}\rangle.
\]

Definiere

\[
U_C=R,\qquad U_S=-R^{\otimes3}.
\]

Dann gelten exakt

\[
(U_C\otimes U_S)|\Omega\rangle=|\Omega\rangle,
\qquad
U_S|\chi_t\rangle=|\chi_{t+1}\rangle.
\]

Der Gesamtzustand ist stationär, während die bedingten Systemzustände eine geordnete Viererfolge bilden. Die Anzeigen sind die computationalen Basiszustände, also ein vorhandener Pauli Kontext. Die Permutationsidentitäten wurden im Prüfer mit ganzen Zahlen kontrolliert.

**Ausdrückliche Grenzen:** R ist nicht der ausgezeichnete Familienzyklus mit projektiver Periode drei. Diese Konstruktion zeigt Verfügbarkeit einer alternativen relationalen Viereruhr, nicht deren physikalische Auswahl. Das Tensorprodukt mehrerer Träger wird bereits vom untersuchten Zellmodell vorausgesetzt. Eine Zeit in Sekunden, die Präparation von Omega und ein selbsttätiger Mechanismus zur Uhrabfrage folgen nicht. Eine Folge realer, aufgezeichneter Messungen muss zusätzlich im gemeinsamen Registerprozess beschrieben werden.

### 8.2 Kontinuierliche Erweiterung und ihre zusätzliche Freiheit

Für jeden hermiteschen spurfreien Viereroperator h gilt

\[
\left(\sum_{i=0}^{3}h_i\right)|\Omega\rangle=0.
\]

Wähle beispielsweise in einer geeigneten Basis

\[
h=\varepsilon\,\operatorname{diag}(-3/2,-1/2,1/2,3/2).
\]

Mit `H_C=h_0`, `H_S=h_1+h_2+h_3` und

\[
|t\rangle_C=e^{-ih t/\hbar}|+_4\rangle
\]

gilt für die normierten bedingten Zustände

\[
|\psi(t)\rangle_S=e^{-iH_St/\hbar}|\psi(0)\rangle_S.
\]

An den vier Zeitpunkten `t_n=n*pi*hbar/(2 epsilon)` sind die Clockzustände orthogonal. Diese Beispielwahl ist eine kontinuierliche Erweiterung in einer anderen Basis, nicht die Behauptung, dass genau dieser Hamiltonoperator bereits vom endlichen Compiler ausgezeichnet wird.

Gerade weil viele h funktionieren, entscheidet das Singulett allein nicht über die physikalische Zeit. Die Existenzlücke wird kleiner; die Auswahllücke bleibt.

## 9. Umkehrbarkeit und exaktes Abklingen

Ein endlicher, geschlossener, autonomer unitärer Prozess erzeugt Beobachtungsfolgen als endliche Summen von Phasenfaktoren. Eine nichtverschwindende solche Folge kann nicht für alle diskreten Zeiten exakt wie `(3/7)^n` abklingen. Dabei sind identische Frequenzen vor dem Argument zusammenzufassen. Diese Präzisierung verhindert, dass sich formal verschiedene Terme vollständig wegheben.

Die Register brauchen dabei nicht außerhalb eines gedachten Universums zu liegen. Ein unbeschränkter innerer Vorrat oder ein thermodynamischer Grenzprozess kann die Aufzeichnungen tragen. Die Auswahl seines Anfangszustands bleibt dann die entscheidende physikalische Zusatzinformation.

Eine explizite reversible Erweiterung des **abstrakten quantenmechanischen Schattens** ist

\[
V|\psi\rangle=\sum_{a=0}^{15}\sqrt{p_a}\,P_a|\psi\rangle\otimes|a\rangle,
\]

mit

\[
p_0=13/28,\qquad p_a=1/28\quad(a\ne0).
\]

Es gilt `V†V=I`. Nach Weglassen des Registers entsteht exakt

\[
\operatorname{Tr}_E(V\rho V^\dagger)=\frac37\rho+\frac17I\operatorname{Tr}\rho.
\]

Mit jeweils frischen Registern iteriert dieser Kanal. V kann auf einem größeren Raum zu einer unitären Operation ergänzt werden.

Dies ist eine konkrete mögliche Erweiterung, **nicht** der Nachweis, dass sie mit allen Kontextkorrelationen des vollständigen 60 Strahlenprozesses übereinstimmt oder dass ihre Pauliwahrscheinlichkeiten physikalisch ausgewählt sind. Sie illustriert sowohl die Möglichkeit globaler Umkehrbarkeit als auch die verbleibende Mehrdeutigkeit des Lifts.

## 10. E8 in der Rückrichtung rekonstruieren

### 10.1 Diskrete Gitterrekonstruktion

Angenommen, ein tieferer Prozess liefert zwei ausgezeichnete positive Gitterfaktoren D5 und A3 einschließlich ihrer Bilinearformen und Ladungsmarkierungen. Beide Diskriminantengruppen sind Z4. Mit geeigneten Generatoren lauten die quadratischen Formen modulo eins

\[
q_{D_5}(k)=5k^2/8,\qquad q_{A_3}(k)=3k^2/8.
\]

Auf der diagonalen Untergruppe ergibt sich

\[
q_{D_5}(k)+q_{A_3}(k)=k^2=0\pmod1.
\]

Die diagonale Verklebung ist daher isotrop und liefert eine gerade Überlattice des Index vier. Ihre Determinante ist

\[
\det L=\frac{4\cdot4}{4^2}=1.
\]

Das positive gerade unimodulare Gitter vom Rang acht ist E8. In seiner Standardrealisierung wurden die 240 Wurzeln unabhängig mit ganzzahligen, verdoppelten Koordinaten enumeriert:

| Sektor | Wurzeln |
| :-- | --: |
| D5 | 40 |
| A3 | 12 |
| gemischter Vektorsektor | 60 |
| erste Spinorklasse | 64 |
| zweite Spinorklasse | 64 |

Mit acht Cartangeneratoren ergeben sich 248 Generatoren.

Dieser Rückweg ist exakt **unter den genannten markierten Ausgangsdaten**. Er erklärt noch nicht, warum der fundamentale Prozess D5, A3 und gerade diese Ladungsverknüpfung auswählt.

### 10.2 Chirale Erweiterung

Auf Stufe eins besitzen die relevanten chiralen Sektoren die Gewichte

\[
h_{D_5}(16)=5/8,\quad h_{A_3}(4)=3/8,
\]

sowie

\[
h_{D_5}(10)=1/2,\quad h_{A_3}(6)=1/2.
\]

Die gemeinsamen Felder `(16,4)`, `(bar16,bar4)` und `(10,6)` haben folglich jeweils Gewicht eins. Die diagonale Z4 Erweiterung ergibt die bekannte Gitteralgebra von E8 mit zentraler Ladung acht.

Die abstrakte Erweiterung ist mathematisch kontrollierbar. Davon zu unterscheiden ist der Nachweis, dass genau die native TFPT Naht einschließlich ihrer renormierten Felder, Domänen, Adjunktionen und Cocyles diesen Skalierungsgrenzwert besitzt. Der in S1 formulierte Vertrag T2 bleibt deshalb bestehen.

### 10.3 Die Kette ist noch nicht die chirale Naht

S2 berichtet für uniforme SU(4) Ketten die erwarteten Signaturen einer SU(4) Theorie auf Stufe eins. Die dortige Lückengleichung enthält ausdrücklich `h+bar h`.

Eine gewöhnliche periodische kritische Kette besitzt im Kontinuum linke und rechte Sektoren. Für diese SU(4) Kette gilt `c_L=c_R=3`, also verschwindende chirale Differenz. Die übliche aus Grundenergie oder Entropie bestimmte Zentralzahl wird dabei als c=3 angegeben, nicht als sechs.

Eine rein chirale E8 Naht hat dagegen chirale Differenz acht. Die Übereinstimmung eines A3 Faktors liefert deshalb noch keine Realisierung der vollständigen chiralen Naht. Zusätzlich sind die Auswahl der Händigkeit, der D5 Faktor, die Z4 Erweiterung und eine konsistente Behandlung der chiralen Anomalie erforderlich. Insbesondere ist ein passender zwei plus eins dimensionaler invertierbarer Bulk nicht gleichbedeutend mit einer vierdimensionalen Raumzeit.

## 11. Der eigentliche Rekonstruktionssatz

### 11.1 Operative Minimalität

Sei h eine zugelassene Vergangenheit und e ein zugelassenes zukünftiges Experiment. Definiere

\[
F_h(e)=\Pr(e\mid h).
\]

Zwei Vergangenheiten sind äquivalent, wenn alle zugelassenen Zukunftsexperimente dieselben Antworten liefern:

\[
h\sim h'\quad\Longleftrightarrow\quad
F_h(e)=F_{h'}(e)\quad\text{für alle zugelassenen }e.
\]

Sind die Experimente unter erlaubten Fortsetzungen abgeschlossen, ist diese Äquivalenz mit der Fortsetzung verträglich. Die Äquivalenzklassen bilden eine autonome prädiktive Beschreibung. Jede andere exakte prädiktive Beschreibung muss alle Klassen unterscheiden, die ein Zukunftsexperiment unterscheiden kann.

Diese Aussage hängt vollständig davon ab, welche Eingriffe, Registerrückführungen und Interferenzversuche zugelassen sind. Ohne diese Liste ist das Wort „minimal“ unbestimmt.

### 11.2 Phasentreue Rekonstruktion

Eine bloße Liste klassischer Ereigniswahrscheinlichkeiten muss die komplexen Phasen nicht enthalten. Benötigt wird eine komplexe Operationsalgebra A mit Einheit und Adjunktion, ihren vollständigen Relationsregeln und einem positiven normierten Funktional omega:

\[
\omega(1)=1,\qquad\omega(a^\dagger a)\geq0.
\]

Bei beschränkten Generatoren kann A als geeignete C Stern Algebra behandelt werden. Bei unbeschränkten Generatoren sind zusätzliche Domänen und Stetigkeitsbedingungen nötig.

Für Operationswörter u,v ist

\[
G(u,v)=\omega(u^\dagger v)
\]

der phasentreue Korrelationskern. Auf endlichen formalen Linearkombinationen von Wörtern definiert er ein positives semidefinites Skalarprodukt.

Setze

\[
\mathcal N=\{a:\omega(a^\dagger a)=0\},
\qquad
\mathcal H_\omega=\overline{A/\mathcal N}.
\]

Durch Linksanwendung entsteht die Darstellung

\[
\pi(a)[b]=[ab],\qquad |\Omega_\omega\rangle=[1].
\]

Dann gilt

\[
\omega(a)=\langle\Omega_\omega|\pi(a)|\Omega_\omega\rangle.
\]

Für einen anderen zyklischen Aufbau mit denselben vollständigen Momenten definiert `[a] -> pi'(a)Omega'` eine Isometrie auf einem dichten Raum. Sie erweitert sich zu einer unitären Äquivalenz. Das ist die bekannte GNS Konstruktion, hier ausdrücklich als Rekonstruktion aus vollständigen Operationskorrelationen angewendet.

**Bedingter Satz:** Ein vollständiges positives Funktional auf einer vollständig festgelegten Operationsalgebra bestimmt seine minimale zyklische Darstellung bis auf unitäre Äquivalenz.

Damit sind Zustandsdarstellung und dargestellte Operationen rekonstruierbar. Noch nicht bestimmt sind ein außerhalb der Algebra hinzugefügter Tensorbegriff, ein ausgewählter Zeitfluss, eine lokale Raumzeit oder das positive Funktional selbst. Diese Daten müssen entweder Bestandteil der primitiven Prozessstruktur sein oder aus ihr folgen.

Insbesondere leitet diese Konstruktion die Quantenmechanik nicht allein aus E8 ab. Komplexe Linearität, Positivität und die Verknüpfung des Funktionals mit beobachtbaren Wahrscheinlichkeiten sind bereits starke Voraussetzungen. Eine noch tiefere Herleitung müsste diese operational rechtfertigen; bekannte informationstheoretische Rekonstruktionen zeigen mögliche Axiomensysteme, nicht deren bereits bewiesene TFPT Herkunft.

### 11.3 Prozesse statt nur Zustände

Für kontrollierte Mehrzeitexperimente ist die passende Auslesung eine Familie von Prozesstensoren beziehungsweise Quantenkämmen. Sie ordnet Folgen erlaubter Instrumente gemeinsame Ergebniswahrscheinlichkeiten zu und enthält zeitliche Korrelationen. Positivität und kausale Normierungsbedingungen ersetzen die naive Annahme, dass ein einzelner Dichteoperator stets alle zukünftigen Antworten bestimmt.

Eine tomographisch vollständige Instrumentenfamilie rekonstruiert einen endlichen Prozesstensor. Sie wählt nicht ohne weitere Minimalitätsbedingungen eine einzigartige verborgene Umwelt oder eine gesamte unendliche Mikrophysik.

### 11.4 Ein ausführbarer Auswahltest

Fixiere zunächst eine endliche Wortlänge L und die tatsächlich hergeleiteten Relationen. Unbekannt sind die Einträge des Momentenkerns G bis zur passenden Ordnung. Fordere Positivität aller geprüften Momentenmatrizen, Normierung, Adjungiertentreue, Kontextrelationen, vorgegebene Symmetrien und die belegten Auslesungen.

Für eine noch nicht bestimmte Observable O löse anschließend zwei Optimierungsprobleme: minimiere und maximiere omega(O) über die zulässige Menge. Bleibt ein Intervall offen, ist O ein konkreter Unterscheidungstest zwischen kompatiblen Rekonstruktionen. Kollabiert das Intervall, ist diese Ausgabe innerhalb der geprüften Relaxation festgelegt.

Ein endliches positives Momentensystem garantiert noch keine konsistente unendliche Erweiterung. Rangstabilität und geeignete Erweiterungsbedingungen müssen separat nachgewiesen werden. Das Verfahren ist dennoch nützlich: Es ersetzt verbale Eindeutigkeitsvermutungen durch explizite Alternativen und nächste Zeugen.

## 12. Raum, Zeit, Materie und Gravitation aus demselben Objekt

### 12.1 Teilsysteme

Gegeben seien paarweise kommutierende volle Matrixunteralgebren `A_i`, die zusammen die gesamte endliche Operatoralgebra erzeugen. Dann induzieren sie eine Tensorproduktzerlegung, bis auf die entsprechenden lokalen Basiswechsel und Umbenennungen.

Der offene inverse Schritt ist die Auswahl dieser Unteralgebren aus den zugelassenen Wechselwirkungen. Die 105 Qubitpaarungen in S3 sind ein endlicher Test in einer vorgegebenen Kodierung, kein Satz über alle Faktorisierungen eines 256 dimensionalen Raums.

### 12.2 Geometrie und Kausalstruktur

Eine Kandidatengeometrie muss aus derselben Operationsstruktur entstehen. Beziehungen zwischen Unteralgebren, mögliche Signalübertragung und die Ausbreitung ursprünglich lokaler Operatoren sind dafür geeigneter als die bloße Dimension eines Trägers.

Der bekannte positive Kegel

\[
H=tI+x\sigma_x+y\sigma_y+z\sigma_z\geq0,
\qquad
\det H=t^2-x^2-y^2-z^2
\]

liefert eine exakte Lorentzkinematik. Damit daraus Raumzeit wird, muss gezeigt werden, warum diese Matrixkoordinaten die Relationen realer Ereignisse beschreiben, wie die entsprechenden Kegel lokal verklebt werden und wie dieselbe Dynamik eine gemeinsame Signalausbreitung bestimmt.

Drei räumliche Dimensionen folgen weder aus der Zahl vier eines Qudits noch aus der Existenz dieses Kegels. Eine mögliche Prüfung müsste im kontrollierten Grenzprozess Volumenwachstum, Spektraldimension, lokale Propagation und relativistische Dispersion zusammenbringen.

### 12.3 Zeit

Die Operationsreihenfolge liefert zuerst eine Ereignisordnung. Eine relationale Uhr kann diese Ordnung in einem geeigneten Zustand auslesen. Die Rekurrenz und der Umgang mit Aufzeichnungen bestimmen, welche irreversible effektive Beschreibung möglich ist. Ein numerischer Wert in Sekunden verlangt zusätzlich eine kalibrierte Energie oder Zeitreferenz.

Die endliche Kontextmatrix K besitzt negative Determinante. Sie ist deshalb kein Exponential einer reellen Matrix auf demselben klassischen Zustandsraum. Ein formal eingeführtes `−log K` kann nicht ohne Weiteres als Energieoperator gelten. Dass K² einen Markovgenerator besitzt, beseitigt die verlorene Einzelschrittinformation nicht.

### 12.4 Materie und Wechselwirkung

Materie wäre in diesem Ansatz nicht jede vorkommende Darstellung, sondern ein stabiler oder kontrolliert propagierender Anregungssektor desselben lokalen Prozesses. Der Nachweis muss Spektrum, Ladungen, chirale Ausbreitung, erlaubte Vertizes und die Entkopplung unerwünschter Spiegelzustände zusammenführen.

Das Vermittlermodell in Abschnitt 7 ist eine konkrete lokale Rechnung in dieser Richtung. Es ersetzt nicht das chirale Standardmodellmaß.

### 12.5 Spektrale Geometrie und Gravitation

Die Spektraltripelroute ist eine präzise mathematische Brücke, sobald eine geeignete Algebra, Darstellung und ein Diracoperator vorliegen. Die Distanzformel

\[
d(\varphi,\psi)=\sup_{\|[D,a]\|\leq1}|\varphi(a)-\psi(a)|
\]

zeigt, warum der Operator D und nicht nur das Eigenwertinventar entscheidend ist.

Connes' Rekonstruktionssatz verlangt starke Voraussetzungen und rekonstruiert im kommutativen Fall eine glatte kompakte Riemannsche Mannigfaltigkeit. Er erzeugt nicht aus einem beliebigen endlichen Matrixraum automatisch eine lorentzsche vierdimensionale Welt.

Für eine physikalische Anwendung müsste D aus demselben primitiven Prozess hervorgehen. Eine ausgewählte Spektralwirkung müsste dann dieselben Kopplungen und denselben Zustand verwenden. Die Wahl einer Funktion in der Spektralwirkung, ihrer Momente, einer Skala oder einer internen Algebra darf nicht nachträglich als bereits hergeleitet gelten.

Ein masseloser quantisierter Spin zwei Sektor mit zwei Helizitäten und universeller Kopplung bleibt eine zusätzliche, explizite Forderung. Weder der Lorentzkegel noch die Identität `c3 inverse = 8 pi` erfüllt sie für sich allein.

## 13. Prioritäten für die nächste Runde

**Erste Priorität: die primitive Prozessquelle einfrieren.** Erlaubte Einzeloperationen, Zusammensetzung verschiedener Träger, Adjungierte, Phasen, Registerpräparation und zulässige Auslesungen müssen als eine einzige überprüfbare Eingabe feststehen. Nicht hergeleitete Regeln bleiben als Annahmen markiert.

**Zweite Priorität: energetische Zellselektion statt hartem Ausschluss.** Die korrekten E8 Vertizes sind in ein gemeinsames Vermittlermodell einzusetzen. Gesucht sind nicht nur das Vorzeichen, sondern die Energielücken der Vermittler, reduzierte Matrixelemente, Graph und konkurrierende Kanäle. Der 22 dimensionale Paarbaustein ist dafür ein kontrollierbarer Ausgangstest.

**Dritte Priorität: ein gemeinsamer phasentreuer Prozessprüfer.** Die ursprüngliche Familienuhr, die neue Viereruhr, frische und wiederverwendete Register sowie verschiedene Kontextmischungen müssen im selben Programm verglichen werden. Gleiche Momentzustände dürfen nicht zur Gleichsetzung unterschiedlicher Geschichten führen.

**Danach: die chirale Naht vor der vierdimensionalen Interpretation.** Zuerst den D5 Faktor, die Z4 Verklebung und die chirale Differenz gemeinsam kontrollieren. Die numerische SU(4) Kette ist eine wertvolle Vergleichsrechnung, aber kein Ersatz für diesen Schritt.

Der entscheidende Abschluss würde so aussehen: Eine einzige primitive Regel wählt ein positives Quellfunktional und eine Komposition aus; die minimal rekonstruierte Darstellung liefert die markierte TFPT Naht, die dynamische Zelle, ihre Aufzeichnungen und schließlich einen kontrollierten gemeinsamen physikalischen Grenzprozess. Die hier erreichten endlichen Ergebnisse schließen mehrere konkrete Teilfragen, aber noch nicht diese gesamte Herkunftskette.

## 14. Literatur zur externen Einordnung

Die folgenden Arbeiten werden zur Einordnung mathematischer Werkzeuge herangezogen, nicht als Bestätigung von TFPT:

* F. A. Pollock et al., *Non Markovian quantum processes: complete framework and efficient characterisation*, Physical Review A 97, 012127 (2018), arXiv:1512.00589. Prozesstensoren und experimentelle Rekonstruktion.
* F. A. Pollock et al., *Operational Markov Condition for Quantum Processes*, Physical Review Letters 120, 040405 (2018), arXiv:1801.09811. Operational unterscheidbares Gedächtnis.
* S. Bravyi, D. DiVincenzo, D. Loss, *Schrieffer Wolff transformation for quantum many body systems*, Annals of Physics 326, 2793 bis 2826 (2011), arXiv:1105.0675. Kontrollierte effektive Hamiltonoperatoren.
* C. Marletto, V. Vedral, *Evolution without evolution, and without ambiguities*, Physical Review D 95, 043510 (2017), arXiv:1610.04773. Relationale Zeit nach Page und Wootters.
* P. Zanardi, D. Lidar, S. Lloyd, *Quantum tensor product structures are observable induced*, Physical Review Letters 92, 060402 (2004), arXiv:quant-ph/0308043. Operational bestimmte Teilsysteme.
* G. Chiribella, G. M. D'Ariano, P. Perinotti, *Informational derivation of Quantum Theory*, Physical Review A 84, 012311 (2011), arXiv:1011.6451. Quantenrekonstruktion mit expliziten operationalen Postulaten.
* A. Connes, *On the spectral characterization of manifolds*, arXiv:0810.2088. Voraussetzungen und Reichweite der geometrischen Rekonstruktion.
* V. G. Kac, P. Möseneder Frajria, P. Papi, F. Xu, *Conformal embeddings and simple current extensions*, arXiv:1210.6602. Allgemeiner Rahmen konformer Einbettungen und einfacher Stromerweiterungen; kein in dieser Notiz behaupteter eigenständiger Beweis der spezifischen TFPT Naht.
* L. Eberhardt, *Wess Zumino Witten Models*, YRISW PhD School (2019). Linke und rechte Ströme, Sugawara Konstruktion und konforme Gewichte.

## 15. Reproduktion

Benötigt werden Python 3, NumPy und SymPy. Der Prüfer verwendet keine Originaldateien aus dem TFPT Repository und verändert keine Quellen oder Statusdateien.

```sh
OPENBLAS_NUM_THREADS=1 python audit.py --output results.json
OPENBLAS_NUM_THREADS=1 python -OO audit.py --output results_optimized.json
cmp results.json results_optimized.json
```

Beide Läufe wurden in dieser Untersuchung ausgeführt und erzeugten identische Ergebnisdateien. Die Prüfbedingungen verwenden explizite Ausnahmen statt wegoptimierbarer assert Anweisungen.

Rationale Identitäten, Ränge und Permutationsgleichungen werden exakt geprüft. Numerische Spektren werden ausdrücklich als Gleitkommarechnungen ausgewiesen. Diese Prüfung bestätigt die angegebenen endlichen Modelle; sie ersetzt keine unabhängige Begutachtung ihrer physikalischen Interpretation.
