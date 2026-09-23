# Ein konkreter E₈-Anschluss und seine genaue dynamische Reichweite

10. September 2026. Quellengebundene mathematische Fortsetzung zur TFPT-, RH- und Faktorisierungsuntersuchung. Die algebraischen Aussagen werden unten bewiesen; die beigefügten Programme prüfen ausgewählte exakte Identitäten. Kein Beweis von RH, P=NP oder allgemeiner effizienter Faktorisierung.

**Ergebnis.** Das aktuelle Faktorisierungspolynom der AO-Reihe führt über seine geometrische Monodromie und die klassische McKay-Korrespondenz zum selben affinen E₈-Tensorgraphen wie TFPTs endlicher Dynamikprüfer. Die dimensionsgewichtete Markovkonstruktion reproduziert nach einer ausdrücklich gewählten Halb-Lazifizierung die dortige goldene Relaxationsrate. Eine exakte, schrittgleiche Zustandsauslese von einer endlichen deterministischen Iteration in diesen festen Kern kann jedoch keine dauerhafte nichtstationäre Information erhalten. Beide Aussagen sind miteinander vereinbar: Der gemeinsame Tensorgraph ist vorhanden; eine gemeinsame arithmetische Prozessdarstellung verlangt mehr Daten.

**Der arithmetische Ausgangspunkt.** Die bereits vor dieser Untersuchung verfasste AO-Quelle verwendet

\[
F(s)=\frac{s(3s^2-10s+15)^2}{64}.
\]

Direkte Rechnung ergibt

\[
F'(s)=\frac{15(s-1)^2(3s^2-10s+15)}{64},\qquad
F(s)-1=\frac{(s-1)^3(9s^2-33s+64)}{64}.
\]

Die einzigen Verzweigungswerte sind 0, 1 und unendlich. Die Zykeltypen sind entsprechend (2,2,1), (3,1,1) und (5). Die geometrische Monodromie ist transitiv, von geraden Permutationen erzeugt und enthält Elemente der Ordnungen 3 und 5. In der Grad-fünf-Situation ist sie A₅; das AO-Original prüft dies zusätzlich durch vollständige Aufzählung der kompatiblen Verzweigungspaare. Diese Belyi-/A₅-Identifikation ist **ein bereits vorhandenes AO-Ergebnis**, keine hier erstmals entdeckte Beziehung.

Die arithmetische Gruppe über ℚ(t) ist dagegen S₅. Tatsächlich gilt

\[
\operatorname{disc}_s(64(F(s)-t))
=5\,[8294400\,t(t-1)]^2.
\]

Die geometrische Gruppe A₅ liegt normal in der arithmetischen Gruppe. Die nichtquadratische Diskriminante macht deren Vorzeichendarstellung nichttrivial; somit ist die arithmetische Gruppe S₅ und ihr konstantes quadratisches Feld ℚ(√5). Das Feld der beiden zusätzlichen direkten Zielvorgänger ist ein anderes:

\[
F(s)=1,\quad s\ne1
\quad\Longrightarrow\quad s=\frac{11\pm3\sqrt{-15}}6.
\]

Die Wahl D=−15 koppelt die operative Quelle an dieses **spezielle Vorgängerfeld**, nicht an das konstante Diskriminantenfeld ℚ(√5).

**Die konkrete McKay-Verbindung.** Identifiziere A₅ mit der Rotationsgruppe des Ikosaeders in SO(3). Sei Γ ihr volles Urbild unter SU(2)→SO(3). Γ ist die binäre Ikosaedergruppe der Ordnung 120. Hier wird kein homomorpher Lift A₅→SU(2) vorausgesetzt.

Die klassische McKay-Korrespondenz identifiziert den Graphen des Tensorierens der irreduziblen Γ-Darstellungen mit ihrer fundamentalen zweidimensionalen Darstellung mit dem affinen E₈-Diagramm. Die Dimensionen sind die affinen höchsten-Wurzel-Markierungen; siehe die explizite Erinnerung an diesen Zusammenhang bei [Kostant, 2010](https://arxiv.org/abs/1003.0046) und den Primärquellenkontext [Aizenbud und Entova-Aizenbud, McKay trees](https://arxiv.org/abs/2109.01842).

In der tatsächlich verwendeten TFPT-Beschriftung bestehen die Kanten aus

\[
01,12,23,34,45,56,67,58,
\]

und der Dimensionsvektor lautet

\[
d=(1,2,3,4,5,6,4,2,3),\qquad Ad=2d,\qquad \sum_i d_i^2=120.
\]

A bezeichnet die symmetrische Adjazenzmatrix. Weil das Tensorprodukt mit der fundamentalen Darstellung selbstdual ist, stimmen die Multiplizitäten in beiden Richtungen überein. Für D=diag(d) setze

\[
P=\frac12D^{-1}AD,\qquad \pi_i=\frac{d_i^2}{120}.
\]

P ist nichtnegativ und zeilenstochastisch, denn P1=1. Ferner

\[
\pi_iP_{ij}=\frac{A_{ij}d_i d_j}{240}=\pi_jP_{ji},
\]

also ist π die stationäre Verteilung. Diese Übergangswahrscheinlichkeit gewichtet einen irreduziblen Summanden seines Tensorprodukts nach dessen Dimension. Es handelt sich um eine konkrete Darstellungstheorie-Dynamik.

P hat wegen der Bipartition Periode zwei. Wähle daher ausdrücklich

\[
T=\frac{I+P}{2}.
\]

Diese Halb-Lazifizierung ist ein zusätzlicher Zeitschrittvertrag. Sie folgt weder aus der A₅-Monodromie allein noch aus der modularen Iteration F. Der verbundene Graph und die Selbstschleifen machen T primitiv.

**Das vollständige Spektrum.** Direkte Determinantenrechnung liefert

\[
\det(xI-A)=x(x^2-4)(x^2-1)(x^4-3x^2+1).
\]

Für φ=(1+√5)/2 gilt damit

\[
\operatorname{spec}(A)=\{2,\varphi,1,\varphi^{-1},0,-\varphi^{-1},-1,-\varphi,-2\}.
\]

T ist ähnlich zu I/2+A/4. Alle seine Eigenwerte liegen in [0,1], der größte ist einfach und gleich eins, der zweitgrößte ist

\[
\boxed{\lambda_2(T)=\frac{2+\varphi}{4}=\frac{5+\sqrt5}{8}},
\qquad
\boxed{1-\lambda_2(T)=\frac{3-\sqrt5}{8}}.
\]

Das ist exakt die in TFPTs `v383_dynamics_universal.py` verwendete goldene Rate. Es wurde somit ein identischer endlicher Tensorgraph samt explizitem Markovoperator identifiziert. Ein bloßes Zusammentreffen zweier Dezimalwerte wäre eine schwächere Aussage.

**Satz über sämtliche exakten Zustandsauslesen in diesen Kern.** Sei X eine beliebige endliche Menge und F:X→X eine beliebige deterministische Abbildung. Sei K:X→Δ₈ eine Wahrscheinlichkeitsauslese mit

\[
K(Fx)=T^\top K(x)\quad\text{für alle }x\in X.
\tag{1}
\]

Setze ε=(1,−1,1,−1,1,−1,1,−1,1). Dann sind sämtliche Lösungen von (1) genau

\[
\boxed{K_i(x)=\pi_i[1+c(x)\varepsilon_i],\quad
|c(x)|\le1,\quad c|_{F(X)}=0.}
\tag{2}
\]

Insbesondere gilt für jede solche Auslese

\[
\boxed{K(Fx)=\pi\quad\text{für alle }x.}
\tag{3}
\]

**Beweis.** Schreibe M=Tᵀ. Jeder endliche F-Orbit erreicht einen Zyklus: Für jedes x existieren a≥0 und ℓ≥1 mit F^(a+ℓ)x=Fᵃx. Aus (1) folgt

\[
M^a(M^\ell-I)K(x)=0.
\]

M ist diagonalisierbar. Für jeden seiner Eigenwerte 0<λ<1 ist λᵃ(λ^ℓ−1) ungleich null. Diese Eigenkomponenten von K(x) verschwinden daher schon am ursprünglichen Zustand x. Übrig bleiben der stationäre Eigenraum und höchstens der Nullraum.

Alle Eigenvektoren zu Eigenwerten ungleich eins haben Komponentensumme null, weil 1ᵀM=1ᵀ. Die Normalisierung von K legt deshalb den stationären Anteil auf π fest. Der Nullraum ist eindimensional und wird von z=ε⊙π erzeugt. Das folgt auch direkt aus der −2-Eigenrichtung der bipartiten Adjazenzmatrix. Beide Bipartitionsklassen besitzen π-Masse 1/2. Daher ist K=π+cz genau für −1≤c≤1 nichtnegativ.

Mπ=π und Mz=0 ergeben (3). Damit muss c auf F(X) verschwinden. Umgekehrt erfüllt jede Funktion c mit den Bedingungen aus (2) unmittelbar Normalisierung, Positivität und (1). Das beweist die vollständige Klassifikation.

Bei einer bijektiven endlichen Iteration ist bereits K≡π. Allgemeiner erlaubt jeder primitive **invertierbare** stochastische Zielkern unter (1) nur die stationäre Auslese: Auf einem Zyklus folgt Stationarität aus Primitivität, davor aus Invertierbarkeit. Diagonalisierbarkeit wird für diese Verallgemeinerung nicht benötigt. Bei einem singulären primitiven Kern kann sein verallgemeinerter Nullraum eine endlich lange Transiente tragen; die maximale Jordanblocklänge am Eigenwert null begrenzt diese Dauer.

**Was damit für den Universalraum feststeht.** Der konkrete goldene E₈-Kern kann unter (1) keine dauerhaft informative Zustandsdarstellung der endlichen modularen F-Iteration sein. Er vergisst nach einem Schritt alles außer π. Ein sinnvoller Anschluss muss daher die Beziehung genauer wählen, beispielsweise durch erhaltene Eingabe- oder Historieregister, einen größeren kohärenten Prozess, kontrollierte zeitabhängige Operatoren oder eine ausdrücklich nur gemittelte beziehungsweise approximative Beziehung. Der Satz entscheidet nicht, welche dieser Erweiterungen tatsächlich funktioniert.

Insbesondere liefert er keine allgemeine Laufzeituntergrenze für Faktorisierung. Er widerlegt weder die McKay-Korrespondenz noch eine gemeinsame komplexe Geometrie. Er identifiziert genau die Information, die ein zu kleiner, fest gehaltener Markovschatten bei einer direkten Dynamikgleichsetzung nicht bewahren kann. Auch die volle arithmetische S₅-Struktur, das Feld ℚ(√−15), N-abhängige Einzugsgebiete und die Faktorauslese werden durch den Tensorgraphen allein nicht rekonstruiert.

**Prüfungen und Provenienz.** `mckay_markov_bridge.py` besteht 20 exakte Kontrollen einschließlich Diskriminanten, Spektrum, Stationarität, detailliertem Gleichgewicht und Primitivität. `exact_intertwiner_control.py` löst für F modulo 7, 11 und 17 die vollständigen linearen Intertwining- und Normalisierungsbedingungen über ℚ. Alle 19 Kontrollen bestehen. Die nichtstationären Lösungsdimensionen sind 2, 4 und 6, genau die jeweilige Zahl von Zuständen ohne Vorgänger. Für den ebenfalls geprüften invertierbaren Kern (2I+P)/3 sind sie null. Diese Beispiele sind Kontrollen der allgemeinen Beweise, keine Ersetzung ihrer Quantoren.

Die AO-Originale heißen `MATHEMATIK.md`, `GEOMETRIE.md` und `ERGEBNISSE.md` im Quellenordner `quadratic_capture_20260910ao`. Die native TFPT-Matrix stammt aus `verification/v383_dynamics_universal.py`. Absolute Quellenpfade und SHA-256-Bindungen stehen in den Manifesten des Prüfpakets. Die allgemeine Ausleseklassifikation wurde zusätzlich unabhängig schriftlich gegengeprüft. Die McKay-Konstruktion ist klassische Mathematik; der hier geleistete Beitrag ist ihre konkrete Verbindung zu diesen beiden vorhandenen Forschungssträngen samt präziser Prüfung der dynamischen Reichweite.
