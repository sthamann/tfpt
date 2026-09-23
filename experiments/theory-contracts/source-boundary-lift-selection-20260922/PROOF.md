# Die gemeinsame Randquelle: Operatorformel, Familienauswahl und analytische Reparatur

22. September 2026 · `UR.SOURCE.BOUNDARY_LIFT_SELECTION.01` · **PARTIAL**

## Ergebnis und konkrete Forschungsfrage

Der vorige Contract konstruiert den globalen gemeinsamen Spinor-/Familienträger. Hier wird der nächste Pfeil geprüft: Bestimmt die ursprüngliche APS-/Calderón-Konstruktion dessen geladenen Randoperator und wählt sie seinen Lift aus?

Das Ergebnis hat einen konstruktiven Teil: Sobald eine tatsächliche Trägerverbindung vorliegt, ist ihre Fortsetzung auf den gemeinsamen Träger explizit. Bei festem Hauptsymbol ist diese Kopplung analytisch kontrollierbar. Außerdem bestimmt der Kommutant der tatsächlichen Familienholonomie, welche Lifts eine parallel erhaltene Familienwirkung zulässt. Dafür ist nicht immer die vollständige Monodromiematrix nötig; ihre Irreduzibilität kann schon ausreichen.

Die ursprüngliche Quellenauswahl folgt daraus noch nicht. Die herangezogene archivierte v4.5-Konstruktion enthält zwei konkret falsche Zwischenschritte: einen allgemeinen Erstordnungs-Störungssatz und eine angeblich erzwungene Vierpunkt-Monodromieformel. Beide werden unten unmittelbar geprüft. Die aktuelle TFPT-Fassung benennt die Mehrdeutigkeit der Monodromie bereits und trennt sie von den exakten Flavorverhältnissen. Die Mehrdeutigkeit selbst ist deshalb kein neu entdeckter globaler TFPT-Mangel.

Die begrenzte Entscheidungsfrage für die Matrixprobe lautet: Erzwingen die im archivierten Satz ausdrücklich angegebenen lokalen Spektren, SU(3)-Unimodularität, Vierpunktrelation und D4-Symmetrie genau eine Monodromie? Ein Erfolg müsste Eindeutigkeit liefern. Zwei nicht konjugierte gültige Darstellungen widerlegen diese Behauptung. Nach diesem Test werden keine neuen Quellmodelle optimiert. Zusätzliche volle TFPT-Admissibilität, parabolischer Splittingtyp und der ursprüngliche Zustand werden für die Gegenbeispiele nicht behauptet.

## 1. Was Calderón hier tatsächlich voraussetzt

Die operative Quelle beginnt mit `(A_loc, tau_t, Theta, omega, [u_Sigma], D_coll)`. Algebra, Zeit, Zustand und Collaroperator sind somit schon Bestandteile des Startdatums. Die v4.5-Fassung sagt ausdrücklich, dass `D_coll` den Randoperator bestimmt (`01_boundary_kernel_source.tex:480–520`).

Der APS-Satz startet seinerseits mit einem gegebenen geometrischen Diracoperator und einem adaptierten Randoperator. Im Nullsektor muss eine geeignete Randuntermenge gewählt werden (`ibid.:353–407`). Das anschließende Upgrade benutzt `C(D_b)`, also den Calderón-Projektor des bereits verdoppelten Operators (`04_qft_source.tex:374–404`). Es gibt dort keine Koeffizientenformel für eine neue Spin(10)-SU(4)-Verbindung auf dem `(16,4)`-Träger.

Diese Richtung entspricht der analytischen Standardstruktur: Adaptierte Randoperatoren haben ein durch das Hauptsymbol festgelegtes Hauptsymbol, ihre Terme nullter Ordnung sind damit noch nicht eindeutig. Siehe Bär–Ballmann, *Guide to Boundary Value Problems for Dirac-Type Operators*, Abschnitt 3.2 und Bemerkung 3.3 der verlinkten Fassung: [Primärquelle](https://arxiv.org/pdf/1307.3021).

Ein weiterer logischer Punkt im archivierten Upgrade-Beweis: Dieselbe elliptische Klasse allein bedeutet nicht dieselbe konkrete Operatordomäne. Auf `[0,2π]` besitzt `-i d/dx` die selbstadjungierten Domänen
\[
\mathcal D_\alpha=\{f\in H^1:f(2\pi)=e^{2\pi i\alpha}f(0)\},
\qquad \operatorname{spec}D_\alpha=\mathbb Z+\alpha.
\]
Die Domänen variieren in einer stetigen Familie regulärer Fredholm-Randprobleme; `D_0` enthält konstante Funktionen, `D_{1/2}` nicht. Eine tatsächlich behauptete Gleichheit der Graphdomänen verlangt deshalb mehr als elliptische Äquivalenz. Das Beispiel widerlegt diese allgemeine Schlussregel, nicht jede mögliche spezielle Calderón-Konstruktion.

## 2. Die konkrete Verbindungsformel auf dem gemeinsamen Träger

Sei `E` der gegebene unitäre Rang-5-Träger, `D=det E`. Aus dem vorherigen Contract:
\[
W_m=\Lambda^{\rm even}E\otimes\bigoplus_{j=1}^4D^{m_j},
\qquad \sum_jm_j=-2.
\]
Schreibe lokal die tatsächliche Trägerverbindung als `nabla_E=d+i A_E`, mit hermitescher Matrix-Einsform `A_E`, und setze `a=tr A_E`. Dann ist die von dieser Verbindung induzierte Verbindung exakt
\[
\boxed{
A_{W_m}=\rho_{\Lambda^{\rm even}}(A_E)\otimes I_4
       +I_{16}\otimes M_m\,a,
\qquad M_m=\operatorname{diag}(m_1,m_2,m_3,m_4).
}
\tag{1}
Hier bezeichnet `rho` die abgeleitete Lie-Algebrawirkung auf der Außenalgebra. Die Formel folgt aus der Produktregel und der Determinantenverbindung. Die halben Determinantenbeiträge des Spin- und Familienlifts heben sich auch auf Verbindungsebene auf:
\[
\left(\rho_{\Lambda^{\rm even}}(A_E)-\tfrac12a I_{16}\right)\otimes I_4
+I_{16}\otimes\left(M_m+\tfrac12I_4\right)a=A_{W_m}.
\]
Dies definiert die Fortsetzung einer **gelieferten** Trägerverbindung; es wählt diese Verbindung nicht aus der bloßen Windung. Zusätzliche unabhängige Familienverbindungen oder Endomorphismusterme werden durch (1) nicht automatisch beseitigt.

Auf einem bereits gegebenen geometrischen Cliffordmodul `S` lautet der zugehörige Differentialoperator
\[
D_{m,\Phi}=c\circ\nabla^{S\otimes W_m}+\Phi.
\tag{2}
Erst dessen tatsächliche Collarform bestimmt den tangentialen `B_Sigma(W_m)`. Die interne Spin(10)-Darstellung und das geometrische Cliffordmodul `S` sind verschiedene Strukturen. Weder `S`, der Zusatzterm `Phi`, CAR-Statistik noch ein Quantenzustand werden durch (1) neu hergeleitet.

## 3. Der gültige analytische Existenzschritt

Der archivierte Satz behauptet, jede symmetrische Störung erster Ordnung mit beschränkten Koeffizienten sei infinitesimal relativ zum Diracoperator beschränkt. Das ist falsch.

Setze auf `[0,π]`
\[
D_0=-i\sigma_1\partial_x,\qquad
\mathcal D(D_0)=\{\psi\in H^1([0,\pi],\mathbb C^2):\psi_1(0)=\psi_1(\pi)=0\}.
\]
Die Randwerte bilden eine maximale isotrope Untermenge für die Randform; direktes partielles Integrieren ergibt dieselbe Domäne für den adjungierten Operator. `D_0` ist selbstadjungiert mit diskretem Spektrum. Für jedes positive ganze `n` ist
\[
\psi_n(x)=\pi^{-1/2}(\sin nx,-i\cos nx)^T,
\qquad D_0\psi_n=n\psi_n.
\]
Wähle `V=-D_0`. Es hat konstante, also beschränkte Koeffizienten und ist symmetrisch erster Ordnung. Die behauptete Schranke müsste
\[
n\le\varepsilon n+C_\varepsilon
\]
für alle `n` erfüllen. Für jedes `epsilon<1` ist dies unmöglich. Der relative Bound beträgt genau eins. `D_0+V=0` auf der echten H1-Domäne ist nicht einmal geschlossen; seine Nullfortsetzung auf den ganzen Hilbertraum wäre nicht Fredholm.

**Reparatur für den hier benötigten Anschluss.** Bei festem Bündel, Clifford-Hauptsymbol und einer bereits gültigen selbstadjungierten Randdomäne unterscheiden sich glatte Verbindungen auf einem kompakten Cutoff durch eine beschränkte Matrix-Einsform. Ihr Beitrag `c(nabla_1-nabla_0)` ist eine beschränkte symmetrische Störung nullter Ordnung. Daher bleibt `D_0+V` auf derselben Domäne selbstadjungiert; der kompakte Resolvent bleibt erhalten. Dies ist die tatsächlich benötigte Form des Kato–Rellich-Schritts, siehe Satz 6.4 bei [Teschl](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf). Beim Vergleich verschiedener Bündel muss vorher eine passende globale Identifikation gegeben sein; lokale Matrizen reichen dafür nicht.

Damit ist die analytische Zulässigkeit einer gewählten glatten Verbindung repariert. Sie beweist weder ihre Auswahl noch unveränderte Nullität oder Spektren. Eine nachträglich neu gewählte APS-Domäne darf ebenfalls nicht ohne Nachweis mit der vorher fixierten Domäne identifiziert werden.

## 4. Exakter Test der als Familienquelle angeführten v4.5-Formel

In `03_em_flavor_source.tex:1077–1190` stehen
\[
\omega=e^{2\pi i/3},\quad D=\operatorname{diag}(1,\omega,\omega^2),\quad
P=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix},
\]
\[
M_0=D,\quad M_1=PDP^{-1},\quad M_2=P^2DP^{-2},\quad
M_3=(M_0M_1M_2)^{-1}.
\]
Direkt folgt `M_0 M_1 M_2=I_3`, also **`M_3=I_3`**. Seine Spur ist drei, während die verlangte lokale Klasse `{1,omega,omega²}` Spur null hat. Außerdem gilt `P³=I`, aber `P⁴DP⁻⁴ != D`; die dort behauptete Vierer-Konjugationswirkung schließt nicht.

Diese konkrete Formel kann somit nicht als bereits ausgewählte Familienverbindung in (1)–(2) übernommen werden. Das ist ein Befund über den angegebenen archivierten Quellensatz, keine Widerlegung der gesamten aktuellen Flavorherleitung.

## 5. Zwei konsistente, nicht konjugierte D4-Pakete

Die Matrixprobe liefert zugleich eine konstruktive Antwort auf die Frage, ob die ausdrücklich genannten Symmetrien allein genügen. Setze für `j=0,1,2,3` allgemein `M_j=R^j D_0 R^{-j}`. Die Reflexion kehrt die Orientierung der kleinen Punktumlaufwege um. Es werden exakt geprüft:
\[
R^4=S^2=I,\quad SRS=R^{-1},\quad
S M_j S=M_{-j}^{-1},\quad M_0M_1M_2M_3=I.
\]
`R` hat Ordnung vier und `S` liegt nicht in seiner zyklischen Gruppe, also ist die D4-Faserwirkung treu. Alle Matrizen sind unitär mit Determinante eins. Alle vier Monodromien haben die verlangten Eigenwerte `{1,omega,omega²}`.

**Abelsches Paket A:**
\[
D_A=\operatorname{diag}(1,\omega,\omega^2),\quad
R_A=\begin{pmatrix}1&0&0\\0&0&i\\0&i&0\end{pmatrix},\quad
S_A=\begin{pmatrix}-1&0&0\\0&0&i\\0&-i&0\end{pmatrix}.
\]
Die Monodromien sind `(D_A,D_A^{-1},D_A,D_A^{-1})`. Der Kommutant der Monodromien hat komplexe Dimension drei; zusammen mit den markierten `R_A,S_A` verbleibt Dimension zwei, entsprechend `1+2`.

**Nichtabelsches Paket N:**
\[
D_N=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix},\quad
R_N=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix},\quad
S_N=\begin{pmatrix}0&-1&0\\-1&0&0\\0&0&-1\end{pmatrix}.
\]
Der gemeinsame Monodromiekommutant hat komplexe Dimension eins, also ist diese unitäre Darstellung irreduzibel. Ein direktes Konjugationsinvariant trennt beide Pakete:
\[
\operatorname{tr}(M_0M_1M_0^{-1}M_1^{-1})=
\begin{cases}3,&A,\\-1,&N.\end{cases}
\]
Damit sind sie nicht durch einen globalen SU(3)-Basiswechsel identisch. Die Standardkonstruktion aus der universellen Überlagerung liefert zu jeder dieser unitären Fundamentalgruppendarstellungen ein flaches hermitesches Rang-3-Bündel mit trivialer Determinantenholonomie. Das ersetzt nicht die ursprüngliche Quelle, sondern entscheidet die vorab benannte Eindeutigkeitsfrage.

Insbesondere wird nicht behauptet, dass das abelsche Paket einen zusätzlich geforderten irreduziblen/stabilen TFPT-Zweig erfüllt. Auch der TFPT-parabolische Splittingtyp, die volle Admissibilität und ein bestimmter Zustand sind für keines der beiden Pakete hier abgeleitet. Gegenbeispielumfang sind genau die oben ausgeschriebenen Symmetrie- und lokalen Spektralbedingungen.

## 6. Daraus folgt ein genauer Auswahltest für den gemeinsamen Lift

Die entscheidende zusätzliche Voraussetzung wird ausdrücklich genannt: **Die Determinantenrichtung soll die feste markierte Familienverbindung parallel erhalten.** Mathematisch muss ihr Generator `beta` dann mit deren Holonomien und Markierungsoperatoren kommutieren. Das ist kein automatisch geltendes P1-Axiom; insbesondere dürfen die verschiedenen nichtkommutierenden TFPT-Clocks nicht stillschweigend zu einer gemeinsamen kommutierenden Zeit gemacht werden.

Für eine irreduzible Rang-3-Familienholonomie ist ihr Kommutant skalar. Nach Einbettung `3+1` in den SU(4)-Vierer folgt daher
\[
\beta=\operatorname{diag}(b,b,b,-3b).
\]
Der Vorzeichen kompensierende globale Lift verlangt halbzahlige Gewichte. Deshalb
\[
b=r+\tfrac12,\qquad
\boxed{m=(r,r,r,-2-3r),\quad r\in\mathbb Z.}
\tag{3}
Die Familiennorm ist `12(r+1/2)²`. Ihr Minimum beträgt drei, erreicht genau bei `r=0,-1`. Mit dem D5-Anteil ergibt sich die gesamte E8-Kocharakternorm vier. Die beiden kleinsten markierten Möglichkeiten sind
\[
m=(0,0,0,-2),\qquad m=(-1,-1,-1,1).
\]
Sie sind bei festgehaltener Triplet-/Singulettmarkierung nicht bloß durch Familienpermutation identisch. Ihre Auswahl verlangt weitere ursprüngliche Daten.

Der bisherige unbeschränkte Norm-2-Wurzellift besitzt dagegen eine `2+2`-Eigenwertaufteilung. Er kann unter dieser Parallelitätsvoraussetzung keine irreduzible dreidimensionale Familienwirkung erhalten. Das folgt bereits aus der Dimension seiner Eigenräume; es ist kein numerischer Befund.

Für das konsistente abelsche Paket A ist ein solcher Wurzellift hingegen zulässig:
\[
\beta_A=\operatorname{diag}(\tfrac12,-\tfrac12,-\tfrac12,\tfrac12)
\]
kommutiert mit allen eingebetteten Monodromien sowie `R_A,S_A`. Seine Familiennorm ist eins. Die exakte Rechnung bestätigt damit den Zusammenhang: **Welche Familienwirkung die Quelle tatsächlich trägt, verändert die zulässige minimale gemeinsame Kopplung.** Ein Normminimum ohne diese gemeinsame Strukturprüfung kann den falschen Kandidaten auswählen.

Für den irreduziblen Zweig muss zur Anwendung von (3) nicht zunächst der gesamte kontinuierliche Familienpunkt berechnet werden: Irreduzibilität plus nachgewiesene Parallelität reicht. Das ist die konstruktive Verkürzung des nächsten Herkunftstests.

## 7. Abgleich mit dem aktuellen TFPT-Stand

Die aktuell verwendete `tfpt_2_standard_model.tex:2177–2202,3969–3985` sagt bereits, dass D4-Symmetrie, lokale Klasse und Produkt allein die Monodromie nicht fixieren. Der aktuelle Ledger enthält entsprechend `FLAV.UFSTAR.01` sowie die aktiven Einträge `FLAV.RIGID.01` und `FLAV.RIGID.02`.

Die letzteren beiden halten gerade fest: Die algebraischen Flavorverhältnisse sind auf den diskreten Selektordaten konstant und benötigen keine Eindeutigkeit des kontinuierlichen Monodromiepunktes. Der vollständige `U_point` bleibt ein separater Anker. Diese Trennung wird hier beibehalten. Weder die Flavorverhältnisse noch die vorhandenen Integer-/Plücker-Ausgaben werden durch die archivierte Fehlformel widerlegt.

Neu in dieser Fortsetzung sind die ausgeschriebene Verbindungsfortsetzung, der direkte Audit der verwendeten v4.5-Formeln, die exakten Symmetriezeugen und ihr Zusammenhang mit der gekoppelten Lift-Auswahl. Die allgemeine Monodromiemehrdeutigkeit wird nicht als neu ausgegeben.

## 8. Was noch zur tatsächlichen Quelle fehlt

Die ursprünglichen Operatoren müssen die markierte Zuordnung zum geometrischen Cliffordmodul, zur Trägerverbindung und zur Familienwirkung liefern. Erst danach kann geprüft werden, ob die Determinantenrichtung diese Familienwirkung parallel erhält oder sie durch einen begründeten gemeinsamen Transport verändert. Danach folgen der tatsächliche Randoperator, seine reduzierte Nullität, der Zustand und dieselbe physische Zeit.

Die beiden Matrixpakete werden nicht anstelle dieses Herkunftsschritts als neue Weltmodelle eingesetzt. Der Test ist mit dem Eindeutigkeitsgegenbeispiel und dem Kommutantensatz abgeschlossen. Die noch offene Angabe ist nun besonders konkret: **die aus dem originalen Collaroperator induzierte Wirkung der Determinantenrichtung auf dem originalen Familienlokalsystem.** Sie muss die zusätzliche Parallelitätsannahme bestätigen oder durch eine explizite gemeinsame Kovarianz ersetzen.

Die Kontrollen verwenden exakte SymPy-Arithmetik; Normal- und `-OO`-Lauf werden verglichen. Der allgemeine Kommutantensatz, der Störungsgegenbeweis für alle Frequenzen und der gültige Existenzsatz stehen ausdrücklich im Text. Endliche Kontrollen ersetzen diese Beweise nicht. Ein unabhängiger Quellenlese-Audit wurde abgeschlossen; für die neuen mathematischen Ergänzungen liegt in dieser Fortsetzung kein abgeschlossenes unabhängiges Agentenreview vor.

Firewall: `experiments/`, keine Paper-/Ledger-/Scorecard-Promotion, kein geschlossenes physisches T1–T8-Gate und keine vollständige TFPT-Lösung.
