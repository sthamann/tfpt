# Prozessrekonstruktion, Fixpunkte und die Auswahl der Dynamik

10. September 2026. Zwei ausgeschriebene mathematische Ergebnisse beantworten den neuen Vorschlag: eine tatsächlich ausgeführte minimale Rekonstruktion für die ursprüngliche U/V-Korrelationsquelle einschließlich eines aus den Daten bewiesenen Abschlusses; und genaue Gegenbeispiele gegen die Auswahl einer einzigen Dynamik durch Positivität, Zustand und Fixpunkte allein. Die allgemeinen Methoden sind klassische GNS-, Moment- und Realisierungstheorie. Eine neue physische Grundtheorie oder ein neuer allgemeiner Lösungsalgorithmus wird nicht behauptet.

## 1. Der richtige positive Rekonstruktionssatz

Seien eine unital C*-Algebra A und ein normierter positiver Zustand ω vollständig gegeben. Setze

\[
\mathcal N_\omega=\{a:\omega(a^*a)=0\},\qquad
\langle[a],[b]\rangle=\omega(a^*b).
\]

Quotient und Vervollständigung liefern den GNS-Raum Hω, die Darstellung πω(a)[b]=[ab] und den zyklischen Vektor Ω=[1]. Die C*-Abschätzung ω(b*a*ab)≤||a||²ω(b*b) stellt Wohldefiniertheit und Beschränktheit sicher. Die Darstellung reproduziert ω(a)=〈Ω,πω(a)Ω〉. Jede andere zyklische Darstellung desselben vollständigen Zustands ist durch [a]↦π′(a)Ω′ isometrisch und nach Vervollständigung unitär äquivalent.

**Damit ist die starke präzise Version der Nutzeridee richtig:** Vollständige Produkt-/Sternstruktur und vollständige positive Korrelationsdaten bestimmen eine minimale zyklische Darstellung bis auf unitäre Koordinatenwahl. Das Wort „vollständig“ darf dabei nicht durch eine endliche Liste passender Zahlen ersetzt werden. Bei einer rohen diskreten *-Algebra müssen außerdem die zulässige C*-Norm beziehungsweise Beschränktheitsrelationen und die Vervollständigung begründet werden.

Sind zusätzlich zustandserhaltende Automorphismen αt vorgegeben, so definiert

\[
U_t[a]=[\alpha_t(a)]
\]

die eindeutige Ω-fixierende unitäre Implementierung in dieser zyklischen Darstellung. Stetigkeit der Matrixelemente auf dem dichten algebraischen Bereich liefert starke Stetigkeit, dann einen selbstadjungierten Generator. Die Werte der Automorphismen auf den Generatoren sind hier tatsächliche Daten; die Aussage wählt diese Werte nicht eigenständig.

Die mathematische Verbindung von GNS und modularer Zeit wird in der Originalarbeit von [Connes und Rovelli](https://arxiv.org/pdf/gr-qc/9406019), §§2.1 und 3, beschrieben. Deren Identifikation modularer mit physischer Zeit ist ausdrücklich eine zusätzliche physische Hypothese.

## 2. Ausgeführt an den tatsächlichen ursprünglichen U/V-Operatoren

Die unveränderten Gauß-dyadischen 3×3-Matrizen U,V stammen aus der vorher geprüften Originalquelle. Es wird ausschließlich der mathematische Spurzustand τ(X)=Tr(X)/3 auf M3(C) verwendet, **nicht** der physische Seam-See-Zustand. Die neun Wörter

\[
B=(I,U,V,U^2,UV,VU,V^2,U^2V,UV^2)
\]

bilden eine Basis; die Determinante ihrer flachen Matrix ist −1/16. Definiere die zu beobachtenden Korrelationsmatrizen

\[
G_{ij}=\tau(B_i^*B_j),\qquad
D^{(g)}_{ij}=\tau(B_i^*gB_j),\quad g=U,V.
\]

Das sind 243 komplexe Tabelleneinträge von Operationswörtern bis Länge7. Konjugierte/inverse Generatoren zählen hier ebenfalls als Operationsbuchstaben. Die Einträge sind exakte Gauß-rationale Zahlen, erzeugt aus der vorhandenen mathematischen Quelle. Es wird nicht behauptet, 243 physische Messungen lieferten sie mit unendlicher Genauigkeit.

Der Rekonstruktor erhält nur diese Tabellen und setzt

\[
A_g=G^{-1}D^{(g)},\quad b=e_0,\quad \ell=e_0^*G.
\tag{R1}
\]

Er bekommt die ursprünglichen U,V-Matrizen nicht als Eingabe. Diese verbleiben ausschließlich beim Datengeber und bei der nachfolgenden unabhängigen Quellenkontrolle.

**Satz.** Für jedes endliche Wort w=g1…gn gilt

\[
\ell A_{g_1}\cdots A_{g_n}b=\tau(g_1\cdots g_n).
\tag{R2}
\]

Beweis: Sei S die lineare Abbildung x↦Σj xjBj. Weil die Bj ganz M3 aufspannen, liegen sämtliche gBj in ihrem Träger. Ihre Koordinaten a erfüllen Ga=Dg(:,j), daher SAg=LgS mit Lg(X)=gX. Induktion über die Wortlänge und S b=I beweisen (R2). Ferner ist G=S* S/3 positiv definit und

\[
\det G=\frac1{256\cdot3^9}=\frac1{5038848},\qquad A_g^*GA_g=G.
\]

Dies ist eine Garantie für alle endlichen Wörter aus dem ausgeschriebenen Intertwiner, keine Verallgemeinerung aus einer endlichen Trefferzahl. Die ausgeführte Kontrolle enthält zusätzlich alle Wörter bis Länge8 und drei längere Folgen, insgesamt514 Wortantworten. Der nächste Abschnitt zeigt stärker: Die Daten selbst schließen bei positiver Quelle und unitären Generatoren weitere erreichbare Dimensionen aus.

Die zyklische GNS-Dimension ist genau9: Der positive Spurzustand ist treu auf dem vollständig erzeugten M3, also gibt es keinen Nullquotienten. Auch die skalare Wortreihe w↦τ(w) hat Hankelrang9, denn die bilineare Spurpaarung (X,Y)↦τ(XY) ist auf M3 nicht entartet und die positiven Wörter spannen beide Faktoren. Eine lineare skalare Wortrealisierung kleinerer Dimension kann daher nicht sämtliche Antworten reproduzieren. Dies ist eine Aussage über den minimalen prädiktiven Zustand; der zugrunde liegende Einteilchenraum hat weiterhin Dimension3.

Die Anwendung der klassischen Hankel-/Realisierungsidee ist keine neue allgemeine Lernmethode. Eine primäre ausgearbeitete Erweiterung samt Minimalitäts- und Eindeutigkeitssätzen ist [Petreczky, Tóth und Mercère](https://arxiv.org/pdf/1601.02777). Hier wurde die begrenzte Version direkt bewiesen und an der bezeichneten Compilerquelle ausgeführt.

## 3. Der aus endlichen Daten bewiesene vollständige Abschluss

Eine bekannte obere Quelldimension ist hierfür **nicht nötig**. Sei irgendein positiver Zustand auf der von zwei unitären Generatoren u,v erzeugten C*-Algebra gegeben, der dieselben exakten Korrelationsdaten besitzt. In seiner GNS-Darstellung setze vi=πω(Bi)Ω, E=span{vi} und Tx=Σxivi. Weil G>0 ist T eine injektive Isometrie vom Koordinatenraum mit G-Metrik auf E. Sei P die orthogonale Projektion auf E.

Für jeden Generator g ist Ag=G−1Dg genau die Koordinatenmatrix von Pπω(g)T. Der gesamte Gram der nicht gesehenen Komponente lautet

\[
R_g=T^*\pi_\omega(g)^*(1-P)\pi_\omega(g)T
=G-(D^{(g)})^*G^{-1}D^{(g)}.
\tag{R3}
\]

Die erste Gleichheit zeigt Rg≥0. Die zweite verwendet die vorgegebene Unitarität, nicht einen vermuteten endlichen Rang der unbekannten Darstellung.

**Abschlusssatz.** Sind R_U=R_V=0, so liegt πω(g)E vollständig in E. Die Einschränkungen sind endlichdimensionale Isometrien und deshalb surjektiv; E ist daher auch unter den inversen Generatoren invariant. Da Ω=v0 in E liegt, enthält E alle vom bezeichneten Alphabet erzeugten zyklischen Wortzustände. Die GNS-Zyklizität liefert Hω=E. Jede positive unitäre Erweiterung genau dieser endlichen Daten besitzt deshalb dieselbe vollständige U/V-Korrelationsfunktion, bis auf die eindeutig angegebene unitäre Darstellung.

In der ausgeführten Rekonstruktion sind beide 9×9-Restgrammatrizen **exakt null**. Der Rekonstruktor prüft dies selbst und lehnt bei nichtverschwindendem Rest die Behauptung eines abgeschlossenen Modells ab. Er prüft außerdem die Normierung G00=1 und die Wortanker A_Bj b=e_j; damit reproduziert die konstruierte Darstellung tatsächlich auch die angegebene Wortbeschriftung der Tabellen. Es ist somit gelungen, in diesem Fall den ganzen erreichbaren Rest aus Strukturregeln und endlichen exakten Daten auszuschließen. Das ist der konkrete tragfähige Kern der Nutzeridee.

Der Alphabetumfang bleibt wesentlich: Falls eine größere Algebra zusätzliche, nicht gemessene Generatoren enthält, ist nur der zyklische U/V-Sektor abgeschlossen. Andere Prozessoperationen, räumliche Verschiebungen oder Primstellenantworten werden nicht mitbewiesen.

Ein Näherungssatz mit ausdrücklicher Restkontrolle ergänzt den exakten Fall. Falls Rg≥0 und

\[
\varepsilon_g^2=\sup_{x\ne0}\frac{x^*R_gx}{x^*Gx},
\]

so ist die ganze Kompressionsabweichung ||πω(g)T−TAg||≤εg in der G-Metrik. Ag ist dort eine Kontraktion. Teleskopieren ergibt für jedes Wort w=g1…gL aus dem gemessenen Alphabet bei normiertemΩ

\[
|\omega(w)-\ell A_{g_1}\cdots A_{g_L}b|
\le\sum_{k=1}^L\varepsilon_{g_k}.
\tag{R4}
\]

Das ist ein endlicher Vorhersagehorizont mit ausdrücklich begrenztem Rest. Für inverse Buchstaben benötigt der Näherungsfall deren eigene Kompressions- und Restschranken; im exakt abgeschlossenen Fall werden die Inversen bereits mitbestimmt. Für größere L muss der Fehler entsprechend kleiner sein. Die Formel setzt konsistente exakte oder rigoros eingeschlossene Gramdaten voraus; ein allgemeines verrauschtes Schätzverfahren wurde nicht implementiert.

Dieser Abschlussmechanismus gehört zur klassischen Theorie positiver Momentmatrizen und flacher Fortsetzungen. Als primäre fachliche Einordnung siehe [Burgdorf und Klep, The truncated tracial moment problem](https://arxiv.org/abs/1001.3679). Deren im Abstract beschriebene tracialen Darstellungssätze werden hier nicht als unbeprüfte Gleichsetzung der Voraussetzungen importiert: Der benötigte unitäre Spezialfall ist oben direkt bewiesen. Neu ausgeführt wurde die konkrete Rekonstruktion und Restprüfung der bezeichneten U/V-Quelle, kein allgemeiner Neuheitsanspruch auf GNS- oder Momenttheorie.

Ohne das Abschlusskriterium bleiben endliche passende Daten mehrdeutig. Für ein beliebig vorgegebenes K≥1 haben die Kreismaße

\[
d\mu_0=\frac{d\theta}{2\pi},\qquad
d\mu_1=\left(1+\frac12\cos(K\theta)\right)\frac{d\theta}{2\pi}
\]

dieselben Momente ∫einθdμ für |n|<K; beide sind normiert und strikt positiv. Bei n=K unterscheiden sie sich um1/4. Man kann daher jeden vorgegebenen endlichen Momenthorizont passieren und trotzdem eine spätere Antwort ändern. Die berechnete Kontrolle verwendet K=20; das Argument gilt für jedes K. Auf E=span{1,z,…,z8} besitzen diese beiden Modelle denselben Restgram diag(0,…,0,1). Sie passieren also gerade **nicht** das neue exakte Abschlusstor. Damit stehen Gegenbeispiel und positiver Satz nicht im Widerspruch.

Reale Messfehler würden zusätzlich Rangstabilität, Konditionierung und Fehlerfortpflanzung erfordern. Es wurde hier weder ein Rauschmodell noch eine experimentelle TFPT-Rekonstruktion behauptet. Ebenso entsteht kein neuer Faktor- oder SAT-Leser: Die Tabellen bilden die feste U/V-Wortalgebra ab, nicht die unbekannten Lösungen einer variablen arithmetischen Eingabe.

Ein konkreter arithmetischer Anschluss ist dennoch vollständig: Die rekonstruierten A_U,A_V besitzen Gauß-dyadische Einträge, hier mit Nennern höchstens2. Mit R=Z[i,1/2] liegt S in GL9(R), da detS=−1/16 eine Einheit ist. Die bewiesenen Identitäten SA_g=L_gS gelten daher bereits über R und bleiben unter jeder Reduktion nach (Z/NZ)[i] für ungerades N gültig. Damit erhält die rekonstruierte Darstellung sämtliche Wortkoordinaten auch in den ursprünglichen Faktorisierungsquotienten. Die positive Hilbertmetrik selbst wird dabei nicht als geordnete modulare Wahrscheinlichkeit ausgegeben. Insbesondere enthält die normierte Spur einen Faktor1/3; bei Charakteristik3 werden die vorher exakt gekürzten Prozessmatrizen reduziert, nicht unzulässig diese normierte Gramform. Die Verbindung liefert algebraisch dieselben erreichbaren Antworten und keine neue Häufigkeit informativer Faktorereignisse.

## 4. Derselbe Zustand und dieselben Fixpunkte lassen verschiedene Dynamiken zu

Nimm auf derselben Algebra M3

\[
\rho=\operatorname{diag}(1/2,1/3,1/6),\quad
H_1=\operatorname{diag}(0,1,3),\quad H_2=\operatorname{diag}(0,1,4).
\]

Beide selbstadjungierten Hamiltonoperatoren erhalten denselben treuen Zustand. Ihre Automorphismen haben genau dieselbe Fixpunktalgebra der Diagonalmatrizen. Dennoch sind ihre Frequenzen verschieden. H2 ist kein aH1+bI: Die ersten beiden Diagonaleinträge erzwingen b=0,a=1; der dritte widerspricht. Eine ρ-erhaltende unitäre Änderung kann dies ebenfalls nicht beheben, da ρ einfaches Spektrum besitzt und solche Unitaries diagonal sind.

Das Gegenbeispiel übersteht sogar die Forderung nach einem **eindeutigen attraktiven** Fixzustand. Für H=H1 oder H2 ist

\[
T_t^{(H)}(\sigma)=e^{-t}e^{-itH}\sigma e^{itH}
 +(1-e^{-t})\rho\operatorname{Tr}\sigma,\quad t\ge0,
\tag{D1}
\]

eine vollständig positive spurtreue Halbgruppe. Jeder Summand ist ein Kanal; die Halbgruppeneigenschaft folgt aus der ρ-Invarianz und der Idempotenz des Resetkanals. Für Zustände konvergiert sie in Spurennorm zu genauρ. Alle nichtstationären Generator-Eigenwerte haben Realteil−1, aber die kohärenten Frequenzen bleiben verschieden. Positivität, vollständige Positivität, eindeutiger Attraktor und gleiche Relaxationsrate bestimmen die Dynamik somit nicht.

Auch detaillierte Balance allein genügt nicht: Mit π=(1/2,1/3,1/6), symmetrischen positiven Leitwerten cij und qij=cij/πi entstehen reversible zusammenhängende Markovgeneratoren mit genau demselben stationärenπ. Die konkret geprüften Matrizen sind

\[
Q_1=\begin{pmatrix}-4&2&2\\3&-6&3\\6&6&-12\end{pmatrix},\quad
Q_2=\begin{pmatrix}-6&2&4\\3&-12&9\\12&18&-30\end{pmatrix}.
\]

Beide besitzen die gleiche vollständige Übergangstopologie und sind keine konstanten Zeitskalierungen voneinander. Die Leitwerte müssen durch weitere physische Daten bestimmt werden.

Diese Gegenbeispiele sagen nicht, dass vollständige spezifizierte Operatorregeln keine eindeutige Entwicklung definieren könnten. Sie zeigen präzise, welche schwächeren Eigenschaften diese Operatorregeln noch nicht ersetzen.

## 5. Was modulare Zeit tatsächlich schließt

Auf einer von-Neumann-Algebra mit treuem normalem Zustand existiert ein kanonischer modularer Fluss. In der hier zur nativen v239 passenden Zeitrichtung lautet er endlichdimensional

\[
\sigma_t(X)=\rho^{-it}X\rho^{it},\qquad K=-\log\rho.
\]

Die KMS-Identität beiβ=1 folgt für alle A,B exakt aus

\[
\operatorname{Tr}(\rho A\rho B\rho^{-1})
=\operatorname{Tr}(\rho BA).
\]

Der neue Prüfer kontrolliert alle81 Matrixeinheitenpaare; der allgemeine Beweis ist die Zyklizität der Spur. Damit ist die kanonische Konstruktion geschlossen, sobald Algebra und Zustand gegeben sind. Der Schritt „dieser Fluss ist der physische Zeitfluss“ bleibt ein zusätzlicher Identifikationssatz. Bei ρ=e−βH/Z liefert K=βH+logZI zunächst die dimensionslose KombinationβH.

Auf der in§2 verwendeten Spur τ ist der modulare Fluss sogar die Identität. Die nichttrivialen U/V-Operationen werden dadurch nicht ausgewählt. Eine Spurantwort, die eine gleichmäßige Sektornormierung liefert, darf daher nicht ungeprüft zugleich als der nichttriviale thermische Seezustand verwendet werden.

Die nativen Quellen wurden direkt gelesen: v239 formuliert die geometrische Boost-Identifikation ausdrücklich als offen; v343 trennt die kanonische Modulardynamik von der physischen Raumzeitbrücke; v723 untersucht und verwirft einen bestimmten stärkeren Vertrag aus einem Modulargenerator und konstanten Umrechnungen für mehrere exportierte Uhren. Dies sind belegte Aussagen dieser Quellen. Ihre historischen Statusetiketten ersetzen keine Prüfung möglicher späterer Schließungen des gesamten Projekts.

Der zustandsunabhängige äußere modulare Fluss aus dem Cocycle-Satz ist ebenfalls kein Ersatz für fehlende Observable-/Zustandsdaten: Bei M3 sind alle Automorphismen inner, die äußere Klasse also trivial. Dies widerspricht dem allgemeinen Satz nicht.

## 6. Simulation und Realität: eine genaue Beobachtungsgrenze

Erweitere eine Darstellung auf H um ein unzugängliches Hilbertsystem K. Setze Zuständeρω⊗η, zugängliche ObservablenA⊗I und DynamikU⊗V, wobei V beliebig ist. Alle zugänglichen Operationswörter und Messprotokolle behalten ihre Wahrscheinlichkeiten. Die Dimension und Dynamik von K sind aus diesen Antworten nicht bestimmbar.

Ein minimaler Prozess entfernt solche unbeobachtbaren Zusätze aus seiner Darstellung. Das beweist weder ihre physische Existenz noch ihre Nichtexistenz. Entsprechend entscheidet eine erfolgreiche Prozessbeschreibung allein nicht, ob die Welt auf externer Hardware simuliert wird. Für eine unterscheidbare Simulationshypothese wären zusätzliche abweichende Beobachtungsvorhersagen erforderlich. Ein mathematischer Fixpunkt ist auch kein Beweis für einen äußeren Konstrukteur oder für dessen Abwesenheit.

## 7. Kontrolle und tatsächliches Ergebnis

check_dynamics.py:105 exakte Kontrollen. reconstruct_process.py:528 exakte Kontrollen, darunter514 Wortantworten, beide vollständigen Restgrammatrizen und die entscheidenden Intertwiner. Die allgemeinen Garantien folgen aus§§2–3; die übrigen Nicht-Eindeutigkeitssätze sind oben ausgeschrieben. Alle verwendeten ursprünglichen lokalen Dateien sind mit SHA-256 dokumentiert; native Kampagnen wurden nicht ausgeführt.

Der praktisch funktionierende Teil ist die Rekonstruktion eines minimalen Prozessmodells aus exakten positiven Korrelationsdaten und unitären Operationsregeln; der vollständige Abschluss wird hier durch verschwindende Restgrammatrizen aus den Daten bewiesen. Anwendungen auf unbekannte physische Systeme, Materialdesign oder wissenschaftliche KI benötigen passende Daten, Operationsverträge und Fehlergarantien. Der vorliegende Lauf beweist keine solche Anwendung außerhalb der bezeichneten U/V-Korrelationsquelle und keine allgemeine Abkürzung für RH, Faktorisierung oder P versus NP.
