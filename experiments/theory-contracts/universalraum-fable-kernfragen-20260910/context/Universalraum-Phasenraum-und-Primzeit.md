# Eine Phasensorte, vollständige Charakterquelle und aperiodische Primzeit

10. September 2026. Unabhängige mathematische Prüfung des neuen eingefügten Gesprächs an Γ=Z[i,1/2]³ und der zuvor konstruierten Inhaltsuhr. Die Aussagen gelten für diesen bezeichneten abelschen Compilerträger; seine Identifikation mit der gesamten physikalischen TFPT-Quelle wird nicht vorausgesetzt. Keine Änderung alter Ergebnisse, keine native Programmausführung und keine RH-Rechnung.

**Konstruktiver Befund:** Eine einzige Sorte komplexer Phase U(1) genügt, um alle Charaktere auszuwerten. Der vollständige Raum aller kompatiblen Phasenbelegungen ist aber Hom(Γ,U(1)), ein sechsdimensionaler dyadischer Solenoid. Er ist weder ein Kreis noch durch einen einzelnen Winkel beschrieben. Eine einzige reelle Zeitvariable kann dagegen durchaus eine dichte, aperiodische Dynamik erzeugen. Die bereits konstruierte positive Inhaltsuhr besitzt sogar einen unendlichdimensionalen kompakten Phasenabschluss. Die Zahl π ist in diesen Aussagen kein zusätzlicher Freiheitsgrad.

## 1. Quellstand und explizite Voraussetzungen

Der ursprüngliche REPORT.md unter outputs/compiler_solenoid_20260909 bezeichnet in Zeilen 93–128 die konkreten Gates U,V, Γ=Z[i,1/2]³ und X=Γ̂. Es motiviert die Zweierlokalisierung durch die tatsächlichen Gateeinträge; die physische Eindeutigkeit dieses Trägers wird dort ausdrücklich nicht behauptet. Seine Zeilen 130–140 wählen Haarwahrscheinlichkeit und den diskreten Koopman-Operator.

Die aktuelle Primzeitvorarbeit work/fundamental-continuation/prime-time/PROOF.md definiert in Zeilen 45–121 den ungeraden Inhalt c(γ), Γ\{0}=P×N_odd und Hδ_γ=log c(γ)δ_γ. Sie trennt die radiale Gibbs-Spur, den ganzen unendlich entarteten Hilbertraum, den profiniten Quotientenzensus und den affinen KMS-Anschluss ausdrücklich. Diese Grenzen werden hier erhalten.

Die Solenoidbeschreibung und das Charakterpaar sind in der Primärliteratur explizit ausgeschrieben: [Latrémolière–Packer, Definition 2.1 und Proposition 2.2](https://arxiv.org/pdf/1311.1193). Die reelle Windungslinie und der Quotient aus reellen und p-adischen Koordinaten stehen auch in [Carrillo Rouse–Guillaume, Abschnitt 2](https://arxiv.org/html/2503.13251v1#S2). Die folgenden Beweise spezialisieren und ergänzen diese Konstruktionen für den gegebenen Rang sechs.

## 2. Positiver vollständiger Rekonstruktionssatz für den abelschen Träger

Setze S=Z[1/2] und identifiziere Γ additiv mit S⁶. Für j=1,…,6, k≥0 bezeichne e_j/2^k die markierten Generatoren. Dann gilt als kompakte topologische Gruppe

\[
X=\widehat\Gamma\cong
\{(z_{j,k})\in U(1)^{6\times\mathbb N_0}:
z_{j,k+1}^{2}=z_{j,k}\}
=\varprojlim(\mathbb T^6,\;z\mapsto z^2).
\tag{1}
\]

**Beweis.** Ein Charakter x setzt z_jk=x(e_j/2^k); die Gruppenrelation erzwingt das Quadratgesetz. Umgekehrt definiert jede solche kohärente Folge

\[
x\big((a_1,\ldots,a_6)/2^k\big)=\prod_{j=1}^6z_{j,k}^{a_j}.
\tag{2}
\]

Das Quadratgesetz macht diese Definition unabhängig von der gemeinsamen Zweiernennerdarstellung. Sie ist multiplikativ bezüglich Addition in Γ. Beide Zuordnungen sind stetig für die punktweise Charaktertopologie beziehungsweise Produkttopologie; damit folgt die behauptete topologische Identifikation.

Die entsprechende universelle komplexe C*-Algebra ist

\[
C^*(\Gamma)\cong C(X).
\tag{3}
\]

Sie wird durch kommutierende Unitaries u_jk mit u_j,k+1²=u_jk erzeugt. Auf jeder festen Tiefe ist die freie Charakterbelegung ein ganzer Sechstorus; sämtliche Tiefen werden durch die bezeichneten Potenzabbildungen verklebt. Gleichung (2) identifiziert alle eindimensionalen Darstellungen, und die Charakterfunktionen trennen die Punkte von X. Der Gelfand-/Stone-Weierstraß-Abschluss liefert (3).

Damit lässt sich der kontinuierliche **abelsche** Antwortträger aus der diskreten markierten Gruppe und der ausdrücklich gewählten universellen C*-Vervollständigung rekonstruieren. Es muss keine besondere Dezimalzahl hinzugefügt werden. Dies rekonstruiert weder automatisch die nichtkommutativen Instrumentzweige noch ihren Zustand, den physikalischen Hamiltonian oder die gesamte TFPT-Prozessquelle.

## 3. Warum dieser vollständige Raum kein Kreis ist

Die Projektion auf die erste Tiefe gibt die exakte Sequenz

\[
0\longrightarrow\mathbb Z_2^6\longrightarrow X
\overset{p_0}{\longrightarrow}\mathbb T^6\longrightarrow0.
\tag{4}
\]

**Beweis.** Jede Phase besitzt kohärent gewählte Quadratwurzeln, also ist p₀ surjektiv. Ist z_j0=1, so lässt sich z_jk als exp(2πi a_jk/2^k) mit a_j,k+1≡a_jk mod2^k schreiben. Genau diese kompatiblen Reste sind sechs 2-adische ganze Zahlen.

Über einem kleinen offenen Winkelwürfel in T⁶ kann man die Winkel stetig heben. Dort ist (4) ein lokales Produkt aus diesem reellen Sechswürfel und Z₂⁶. Daraus folgt topologische Dimension sechs: Der lokale Raum enthält einen Sechswürfel; die inverse Folge sechsdimensionaler Tori liefert die obere Dimensionsschranke sechs. Der Raum ist kompakt und zusammenhängend, weil er inverse Grenze kompakter zusammenhängender Räume mit surjektiven Übergängen ist. Er ist wegen der nichttrivialen total unzusammenhängenden lokalen 2-adischen Faser nicht lokal zusammenhängend. „Eine zusammenhängende Komponente“ ist hier wahr, bedeutet aber keineswegs „eine kontinuierliche Koordinate“.

Eine besonders scharfe Gruppenobstruktion lautet

\[
\operatorname{Hom}_{\rm cont}(U(1),X)=\{0\}.
\tag{5}
\]

**Beweis.** Dual zu einem solchen Homomorphismus wäre ein Gruppenhomomorphismus φ:S⁶→Z. Für jedes γ und jedes k gilt φ(γ)=2^kφ(γ/2^k). Eine ganze Zahl, die durch alle Zweierpotenzen teilbar ist, ist null. Somit φ=0 und nach Charaktertrennung auch der ursprüngliche Homomorphismus null. Insbesondere kann keine einzelne Kreis-Untergruppe den vollen Träger erzeugen. Auch eine toruswertige Änderung der Koordinatennormierung behebt dies nicht. Demgegenüber existieren zahlreiche nichttriviale Charakterabbildungen X→U(1); die Richtung ist entscheidend.

Bereits die Verdopplung unterscheidet die Gruppen: Auf X ist z↦z² ein Automorphismus mit inverser Abbildung (z_k)↦(z_k+1). Auf U(1) hat die Verdopplung den zweielementigen Kern {1,−1}.

Selbst eine kontinuierliche surjektive Zustandsparametrisierung durch einen Kreis ist ausgeschlossen. Denn X ist nicht wegzusammenhängend: Jeder Weg vom Einselement projiziert nach T⁶ und besitzt dort einen reellen Winkel-Lift. Nach Abzug seiner kanonischen Windung in X bleibt ein Weg in der total unzusammenhängenden Faser Z₂⁶, also der konstante Weg. Die Wegkomponente des Einselements ist somit als Menge das Bild der Windung R⁶→X. Dieses Bild trifft die Faser über dem Einselement nur an den abzählbar vielen Windungen ganzzahliger Vektoren; die Faser selbst ist überabzählbar. Die Wegkomponente ist daher echt kleiner als X. Ein kontinuierliches Bild des wegzusammenhängenden Kreises kann nicht ganz X sein. Rein messbare Kodierungen sind eine andere Frage und bewahren dadurch weder diese Topologie noch die Gruppenoperationen.

**Exakter Verlust auf jeder endlichen Auflösung.** Setze in einer Koordinate

\[
\iota(t)_k=e^{2\pi i t/2^k}.
\]

Für beliebiges K≥0 stimmen iota(0) und iota(2^K) auf allen Tiefen k≤K überein, aber bei K+1 unterscheiden sie sich um das Vorzeichen. Daher bestimmen selbst alle Charakterantworten mit Nenner bis 2^K die vollständige Quelle nicht. Dies ist ein all-K-Beweis; die kleinen Kontrollen demonstrieren nur seine ersten Instanzen.

## 4. Ein einzelnes reelles t kann trotzdem eine vollständige dichte Bewegung tragen

Sei α∈R⁶ mit rational unabhängigen Koordinaten. Dann definiert

\[
\rho_t(\gamma)=e^{2\pi i t\,\alpha\cdot\gamma},\qquad
F_t(x)=x\rho_t
\tag{6}
\]

eine stetige einparametrige Translationsgruppe auf X. Ihr Bild ist dicht, ihre gemeinsame Periode ist nur null, und die Zeitmittel jeder stetigen Funktion entlang jeder Bahn konvergieren zum Haarmittel.

**Beweis.** Ein Charakter γ verschwindet auf dem Abschluss der Bahn genau dann, wenn exp(2πit α·γ)=1 für alle reellen t, also α·γ=0. Rationale Unabhängigkeit lässt dies nur für γ=0 zu. Die Charaktertrennung kompakter abelscher Gruppen macht den Bahnabschluss deshalb zu ganz X. Ist ρ_T=1, so gilt Tα_j/2^k∈Z für jedes k; somit Tα_j=0 und T=0. Für jeden nichttrivialen Charakter ist das normierte Zeitintegral der Exponentialfunktion höchstens 1/(πT|α·γ|), also konvergiert es zu null. Für die Konstante ist es eins. Gleichmäßige Approximation durch Charakterpolynome ergibt die Aussage für alle stetigen Funktionen. Insbesondere ist Haar die einzige unter dieser ganzen Flussgruppe invariante Wahrscheinlichkeit.

Ein konkretes Beispiel ist α=(1,√2,√3,√5,√6,√10). Die acht Vorzeichenautomorphismen von Q(√2,√3,√5) beweisen die rationale Unabhängigkeit der sechs verschiedenen Monome; ihre Vorzeichenspalten sind orthogonal. Ein numerisches Irrationalitätsexperiment ist nicht nötig.

Dieser Satz liefert eine mögliche Dynamik mit einer einzigen reellen Zeitvariable auf einem sechsdimensionalen, unendlich verfeinerten Träger. Er wählt diese α oder diesen Translationsfluss nicht aus TFPT aus. Sein Fouriergenerator hat auch positive und negative Frequenzen und ist nicht der positive Inhaltsgenerator aus dem nächsten Abschnitt. Die Definition einer Zeitvariable, die Dimension des Zustandsraums und die Periodizität sind getrennte Daten.

## 5. Die tatsächliche Inhaltsuhr hat keinen gemeinsamen Kreisabschluss

Die zuvor konstruierte Uhr auf ℓ²(Γ\{0}) lautet

\[
H\delta_\gamma=\log c(\gamma)\delta_\gamma,
\qquad U_t\delta_\gamma=c(\gamma)^{it}\delta_\gamma.
\tag{7}
\]

Für eine primitive Richtung v werden die Energien 0,log3,log5 durch v,3v,5v wirklich angenommen. Daher gilt

\[
U_T=I\quad\Longrightarrow\quad T=0.
\tag{8}
\]

**Beweis.** Bei T≠0 müssten Tlog3=2πr und Tlog5=2πs mit nichtverschwindenden ganzen r,s gelten. Damit wäre 3^s=5^r. Die 3- und 5-adischen Bewertungen erzwingen s=r=0, Widerspruch. Auch U_T=e^{iθ}I als gemeinsame bloße globale Phase ist unmöglich: Die tatsächlich vorhandene Energie null erzwingt e^{iθ}=1. Derselbe Schluss gilt für einen einzelnen primitiven Strahl und für eine Zeitautomorphie, welche die beiden nichtverschwindenden Skalierungsoperatoren durch 3^{it} beziehungsweise 5^{it} multipliziert. Einzelne Energiedifferenzen besitzen Perioden; eine gemeinsame Periode des ganzen Systems folgt daraus nicht.

**Positiver Satz über den vollständigen Phasenabschluss.** Der Abschluss von {U_t:t∈R} in der starken Operatortopologie ist kanonisch

\[
\prod_{p\ {
m ungerade\ prim}}U(1).
\tag{9}
\]

Zu z=(z_p) gehört die Diagonalwirkung

\[
D_z\delta_\gamma=
\left(\prod_p z_p^{v_p(c(\gamma))}\right)\delta_\gamma.
\]

**Beweis.** Jedes Produkt am einzelnen γ ist endlich. Produktkoordinatenkonvergenz von z impliziert daher punktweise Basiskonvergenz und wegen der einheitlichen Operatornorm eins starke Konvergenz. Umgekehrt wird jede Koordinate z_p an δ_pv sichtbar. Somit ist diese kompakte Produktgruppe genau ihre starke Diagonalrealisierung. Jede endliche Menge log p ist rational unabhängig: Eine ganzzahlige lineare Relation würde nach Exponentiation eine verbotene Primfaktorzerlegung von eins geben. Für jedes endliche Primzahlset ist die reelle Phasenbahn deshalb dicht im entsprechenden Torus, nach demselben Charakterargument wie in Abschnitt 4. Das beweist die Dichtheit in der gesamten Produktgruppe und (9).

Dies ist ausdrücklich ein starker beziehungsweise koordinatenweiser Abschluss, keine behauptete Dichtheit in Operatornorm. Der Raum in (9) ist außerdem der Phasenabschluss einer bereits gewählten Spektraldynamik; er wird nicht mit dem geometrischen Solenoid X identifiziert. Auf dem Fourierträger ist die Inhaltsenergie keine additive Funktion von γ. Beispielsweise haben e₁ und 2e₁ Inhalt eins, ihre Summe 3e₁ aber Inhalt drei. Eine Verlängerung von U_t auf den Konstantenmodus durch Energie null wirkt daher im Allgemeinen nicht multiplikativ auf den Charakterfunktionen und ist kein automatisch gegebener Koopman-Translationsfluss auf X.

Die Primärliteratur zeigt den klassischen Ursprung solcher logarithmischer Phasen: [Cuntz, Abschnitt 4, Proposition 4.2 und Theorem 4.3](https://arxiv.org/pdf/math/0611541) betrachtet n^{it} auf einer ausdrücklich definierten affinen C*-Algebra und mit ausdrücklich bestimmten KMS-Prämissen. Die spezielle Nichtnull-/Rangsechs-Realisierung in (7) ist die hier bereits vorhandene Quellenkonstruktion; sie wird nicht durch Namensgleichheit mit dem klassischen System gleichgesetzt.

## 6. Positivität, Haarzustand und ausgeschlossener Nullmodus

Eine normierte positive Charakterantwort φ auf Γ erfüllt

\[
\varphi(0)=1,\quad
\sum_{r,s}\overline{b_r}b_s\varphi(\gamma_s-\gamma_r)\ge0.
\]

Sie bestimmt eine eindeutige Wahrscheinlichkeitsmaßdarstellung auf X. Das folgt etwa durch GNS für die Gruppenalgebra, deren Generatoren aufgrund der Gruppenrelationen unitär wirken, und anschließend Riesz-Darstellung auf C(X). **Es gibt aber viele solche φ.** Haar liefert φ(γ)=δ_γ0; eine Punktmasse liefert einen einzelnen Charakter. Sogar treue Zustände bleiben nicht eindeutig: Für γ₀≠0 und |ε|<1 ist (1+ε Re χ_γ₀)dm_X eine strikt positive, normierte Dichte mit anderen Charakterantworten. Erst die zusätzliche Invarianz unter sämtlichen Translationen bestimmt Haar. Positivität allein wählt weder diese Invarianz noch den physikalischen Zustand.

Im Haar-GNS-Raum gilt L²(X,m_X)≅ℓ²(Γ), und der zyklische Vektor 1 entspricht δ₀. Γ\{0} in (7) ist deshalb die Entfernung des konstanten Fouriermodus, nicht die Entfernung eines einzelnen Raum-Punktes aus X. Das orthogonale Komplement zu 1 bleibt unter den ursprünglichen invertierbaren Gatepermutationen erhalten, aber nicht unter allen Charakter-Multiplikatoren: χ_γ·χ_−γ=1. Eine Kompression auf dieses Komplement ist keine unveränderte Darstellung der ganzen Multiplikationsalgebra. Die dortige positive Inhaltsuhr wird dadurch nicht ungültig; ihr voller Quell-/Zustandsanschluss braucht aber die bereits benannte zusätzliche Konstruktion.

Auch die verschiedenen Maßräume dürfen nicht verschmolzen werden. Der ungerade profinite Quotientenzensus K=∏_(p odd)Z_p⁶ ist total unzusammenhängend; X ist zusammenhängend. Der in der Vorarbeit bewiesene Inhalt unter Haar auf K hat Gesetz

    P(c=n)=n^(−6)/ζ_odd(6),      ζ_odd(6)=π⁶/960.

Das ist eine tatsächlich hergeleitete positive Normalisierung auf diesem Quotientenzensus. Sie ist keine Haar-Gibbs-Spur auf ganz ℓ²(Γ\{0}); dort hat die Energie null schon unendliche Entartung, etwa durch die unterschiedlichen primitiven Richtungen 2^(−k)e₁. Auf einem bezeichneten einzelnen primitiven Strahl ist dagegen Tr(e^(−βH))=ζ_odd(β) für β>1 korrekt. Diese Zustände haben unterschiedliche Definitionsräume. Für die vollständige affine Überdeckungsalgebra liefert der frühere KMS-Vergleich nur die notwendige Stelle β=6 bei der bezeichneten log-n-Zeit, keine automatische normale Gibbs-Familie auf dem Haarraum.

## 7. Was daraus für π und die neue Hypothese folgt

Die Gruppe U(1) kann ohne einen als Parameter eingegebenen π-Wert als {z∈C:z*z=1} oder als R/Z beschrieben werden. In der üblichen Exponentialkoordinate ist z=exp(2πi s); im Bogenmaß schreibt man θ=2πs. Normiertes Haarmaß lautet entsprechend ds oder dθ/(2π). Beide sind dieselbe Gruppe mit derselben Wahrscheinlichkeit. π ist hier eine mathematische Konstante der gewählten analytisch-geometrischen Darstellung und kein frei belegbarer kontinuierlicher Zustand.

Wenn man zusätzlich die euklidische Metrik des Einheitskreises bezeichnet, ergibt deren Umfang tatsächlich den mathematisch bestimmten Wert 2π. Die abstrakte kompakte Gruppe mit normierter Haarwahrscheinlichkeit allein bezeichnet jedoch keine physikalische Längeneinheit: Eine Skalierung einer invarianten Längenmetrik verändert den Umfang und lässt Gruppenstruktur und Haarwahrscheinlichkeit gleich. Auch aus einem Achtel-Sektor folgt erst dessen Haargewicht 1/8 beziehungsweise bei gewähltem Bogenmaß eine Winkellänge π/4. Ein spezieller Faktor π/8 oder 1/(8π) folgt nicht ohne die genaue zusätzliche Normierungsdefinition. Dass an einer anderen konkreten Stelle π⁶/960 folgt, ist ein überprüfbares mathematisches Ergebnis; es macht π nicht zum einzigen fehlenden ontologischen Baustein.

Der stärkste jetzt gerechtfertigte Satz lautet deshalb: **Die markierte diskrete additive Quelle besitzt eine kanonisch rekonstruierbare kontinuierliche Charakterdarstellung. Eine einzige Phasensorte genügt als Auswertungsziel, aber alle kohärenten Belegungen, die Zustandswahl und der Dynamikvertrag müssen erhalten bleiben.** Ein einzelner Kreis als vollständiger Träger und eine gemeinsame Kreiszeit sind für die hier tatsächlich verwendeten Konstruktionen widerlegt. Daraus folgt weder ein genereller Ausschluss kompakter Phasenbeschreibungen noch eine Anzahl fundamentaler Komponenten der Realität.

## 8. Kontrollen und Beleggrenzen

check_solenoid.py besteht mit **49 exakten Kontrollen**. Es prüft die kohärenten, auf jeder endlichen Tiefe ununterscheidbaren Charakterpaare; den inversen Verdopplungsschritt; das wohldefinierte Charakterpaar; die rationale Unabhängigkeit des ausgeschriebenen Flussbeispiels; den Bewertungsgrund des Periodizitätswiderspruchs; tatsächliche Inhalte 1,3,5,9,15; die unendliche Grundzustandsfamilie in ihren ersten Instanzen; die Rangsechs-Normalisierung und einen alternativen positiven Zustand. Die all-K-, all-t-, Dichtheits-, Dimensions- und Abschlussaussagen folgen aus den schriftlichen Beweisen und nicht aus endlich vielen Kontrollen.

checks.json pinnt die neue Analyse, den ursprünglichen Compilerbericht und die gelesene Primzeitvorarbeit. primary-sources.json dokumentiert die tatsächlich gelesene Primärliteratur. Keine alten Artefakte wurden geändert. Die Ergebnisse sind eine konkrete Charakter-/Dynamik-/Zustandsprüfung, kein RH-, Faktorisierungs-, P=NP- oder TOE-Abschluss.
