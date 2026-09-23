# Der GNS-Teil des Diagramms: exakter Satz und drei fehlende Identifikationen

10. September 2026. Prüfung des neuen „Master Solution Program“. Der bedingte Diagrammsatz unten ist vollständig ausgeschrieben. Seine Anwendung auf die konkrete TFPT-Seam verlangt weiterhin die benannte Quellenabbildung. Die endlichen Gegenmodelle treffen behauptete automatische Übergänge, keine allgemeine Unmöglichkeit einer tieferen TFPT-Theorie.

## 1. Was eine positive Algebra tatsächlich liefert

Für eine unitale C*-Algebra A und einen normierten positiven Zustand ω bildet GNS den Quotienten aus den Nullrichtungen der Paarung `ω(a*b)`, vervollständigt ihn zum Hilbertraum und stellt A durch Linksmultiplikation dar. Die zyklische Darstellung ist bis auf eine passende unitäre Äquivalenz eindeutig **für dieses bereits gegebene Paar (A,ω)**. Sie wählt weder A noch ω selbst aus. Eine bloße algebraische *-Algebra ohne passende Norm-/Beschränktheitsannahmen garantiert noch keine Darstellung durch lauter beschränkte Operatoren. [Landsman, Konstruktion 2.9.4 und Proposition 2.9.5](https://arxiv.org/pdf/math-ph/9807030)

Zwei Präzisierungen des Anhangs sind notwendig:

- Ein Adjunkt ist kein allgemeiner inverser Prozess. Eine nichttriviale Projektion p erfüllt p*=p, besitzt aber kein Inverses.
- Positivität liefert nicht automatisch nichtkommutative Quantenphysik. Für A=C² mit ω(a,b)=(a+b)/2 ist der GNS-Raum C², aber alle zulässigen Observablen wirken diagonal und kommutieren. Diese Beschreibung ist eine klassische Zweipunkt-Wahrscheinlichkeitswelt trotz Hilbertraumdarstellung.

## 2. Der exakte Diagrammsatz

Seien `(A₀,ω₀)` und `(A₁,ω₁)` solche Paare und `Φ:A₀→A₁` ein unitaler *-Isomorphismus mit

\[
\omega_1\circ\Phi=\omega_0.
\]

Ihre zyklischen GNS-Darstellungen seien `(H_j,π_j,Ω_j)`. Dann existiert genau ein Unitär V mit

\[
V\Omega_0=\Omega_1,\qquad
V\pi_0(a)=\pi_1(\Phi(a))V.
\]

**Beweis.** Definiere auf den dichten zyklischen Vektoren

\[
V\pi_0(a)\Omega_0=\pi_1(\Phi(a))\Omega_1.
\]

Die Normquadrate stimmen überein, weil `ω₁(Φ(a)*Φ(a))=ω₀(a*a)`. Das gilt ebenso für alle inneren Produkte und macht die Definition unabhängig von Nullvertretern. Sie setzt sich isometrisch auf H₀ fort. Surjektivität von Φ und Zyklizität von Ω₁ machen das Bild dicht; ein isometrisches Bild ist geschlossen, also ist V surjektiv. Produkte liefern die Intertwining-Identität. Die vorgegebene Wirkung auf einer dichten Menge erzwingt Eindeutigkeit. □

Ist Φ nur ein unitaler *-Homomorphismus mit derselben Zustandserhaltung, ergibt dieselbe Rechnung eine Isometrie in den von `π₁(Φ(A₀))Ω₁` erzeugten Teilraum. Das ist keine automatische Abdeckung sämtlicher physischer Felder. Eine Cap-Vektorabbildung ist zudem noch kein solcher Algebra-Homomorphismus: Dafür müssen die Produkte und Relationen der tatsächlichen Prozessalgebra erhalten werden.

## 3. Wann das Diagramm auch die Zeitentwicklung schließt

Seien zusätzlich `α_t^(j)` punktnormstetige Automorphismengruppen mit invarianten Zuständen und

\[
\Phi\alpha_t^{(0)}=\alpha_t^{(1)}\Phi.
\]

Auf zyklischen Vektoren sind die kanonischen Gruppen definiert durch

\[
U_j(t)\pi_j(a)\Omega_j=\pi_j(\alpha_t^{(j)}(a))\Omega_j.
\]

Zustandsinvarianz erhält die Paarung, die inverse Zeit liefert das inverse Unitär. Stetigkeit auf dieser dichten Menge folgt aus Punktnormstetigkeit von α und erweitert sich auf H_j. Direktes Einsetzen ergibt

\[
VU_0(t)=U_1(t)V.
\]

Für die selbstadjungierten Generatoren `U_j(t)=exp(itK_j)` folgt durch die Ableitungsdefinition des Generators einschließlich seiner Domäne

\[
V\operatorname{Dom}K_0=\operatorname{Dom}K_1,\qquad
VK_0=K_1V.
\]

**Der GNS-/Dynamikteil des gewünschten Diagramms ist damit bewiesen, sobald die echte quellen- und zustandserhaltende Prozessabbildung vorliegt.** Er erzeugt die fehlende Abbildung und Zustandsauswahl nicht rückwirkend.

## 4. Positive Paarung ist nicht positive physische Energie

Betrachte A=M₂(C), `H=diag(0,ε)` mit ε>0 und einen treuen Gibbszustand `ρ∝exp(−βH)`. In der GNS-Darstellung auf Hilbert–Schmidt-Matrizen gilt

\[
\pi(a)X=aX,\quad\Omega=\sqrt\rho,\quad
U(t)X=e^{itH}Xe^{-itH}.
\]

Der kanonische Generator ist

\[
KX=HX-XH,\qquad\operatorname{spec}K=\{0,0,\varepsilon,-\varepsilon\}.
\]

Das folgt durch Anwendung auf die vier Matrixeinheiten E_ij: `K(E_ij)=(h_i−h_j)E_ij`. Die Paarung und der Zustand sind positiv; trotzdem besitzt K eine negative Eigenrichtung. Dies ist eine reguläre thermische GNS-Darstellung. Die physische Vakuum-Spektralbedingung ist deshalb eine zusätzliche Anforderung und darf nicht aus dem Wort „positiv“ abgeleitet werden.

Auch eine endliche Clockmarkierung wählt die kontinuierliche Dynamik nicht eindeutig. Setze in Zeiteinheiten mit einem Clockschritt bei t=1

\[
H_0=\operatorname{diag}(0,\pi/2,\pi,3\pi/2),\qquad
H_1=H_0+2\pi\operatorname{diag}(0,1,0,0).
\]

Beide sind positiv und liefern `exp(iH₀)=exp(iH₁)=diag(1,i,−1,−i)`. Beide erhalten den Spurzutand und die Clockmarke. Bei t=1/2 entwickeln sie E₀₁ jedoch mit entgegengesetztem Vorzeichen. Eine zusätzliche kontinuierliche Auswahlregel könnte eine Variante bevorzugen; sie ist keine Folge derselben diskreten Clock allein. Dies behauptet keine Erhaltung zusätzlicher, hier nicht vorgegebener vollständiger TFPT-Relationsdaten.

## 5. Der kritische Fehler bei „D ist automatisch auch die Dynamik“

Der Anhang schlägt zugleich spektrale Geometrie und

\[
\alpha_t(a)=e^{itD}ae^{-itD}
\]

als Prozessentwicklung vor. Diese Formel definiert zunächst eine Konjugation auf den Operatoren des Hilbertraums. Sie muss die gewählte Beobachtungsalgebra A überhaupt nicht erhalten.

**Exaktes Gegenbeispiel.** Auf H=C² sei A die diagonale Algebra, D=σ_x und a=σ_z. Bei t=π/4 gilt

\[
e^{i\pi\sigma_x/4}\sigma_z e^{-i\pi\sigma_x/4}=\sigma_y.
\]

Die rechte Seite ist nicht diagonal. Daher ist diese α keine Automorphismengruppe der ursprünglichen A. Derselbe D liefert über die Kommutatorformel durchaus den endlichen Zweipunktabstand eins. **Geometrischer Operator und innerer Prozessgenerator sind somit nicht automatisch dieselbe Struktur.**

Man kann A vergrößern. Dann muss die Theorie aber die neue Algebra, deren physische Observablen und die Geometrie dieser vergrößerten Darstellung prüfen. Eine Umbenennung löst das Problem nicht. Auch ein allgemeiner Diracoperator ist nicht allein aufgrund seines Namens ein nach unten beschränkter physischer Hamiltonoperator.

## 6. Wann auch die Geometrie korrekt mittransportiert wird

Seien zusätzlich selbstadjungierte geometrische Operatoren D₀ und D₁ mit

\[
VD_0V^*=D_1
\]

einschließlich der Domänen gegeben. Für die dichten glatten Algebren mit beschränkten Kommutatoren wird ausdrücklich `Φ(A₀^∞)=A₁^∞` verlangt; alternativ verwendet man auf beiden Seiten die gesamten beschränkten Kommutatordomänen. Dann folgt

\[
[D_1,\pi_1(\Phi(a))]=V[D_0,\pi_0(a)]V^*,
\qquad
\|[D_1,\pi_1(\Phi(a))]\|=\|[D_0,\pi_0(a)]\|.
\]

Transportiere Zustände durch `φ₁=φ₀∘Φ⁻¹` und `ψ₁=ψ₀∘Φ⁻¹`. Damit stimmen die über den bezeichneten vollen Testalgebren definierten Kommutator-Abstände exakt überein: In der Supremumsdefinition ist Φ eine Bijektion zwischen den beiden Lipschitz-Einheitsbällen. Dies ist auch bei unendlichen Abständen eine Gleichheit. Eine nur kleinere gemeinsame Testalgebra würde ohne weiteren Dichtheits-/Approximationbeweis keine Gleichheit mit dem Abstand einer größeren Ziel-Testalgebra liefern.

**Das schließt den geometrischen Transport bedingt.** Ein beliebiges spektrales Tripel erfüllt deshalb noch keine Mannigfaltigkeitsrekonstruktion; eine Riemannsche Rekonstruktion liefert noch keine Lorentz-Raumzeit. Die in der vorigen Untersuchung gelesenen Connes-Hypothesen bleiben erforderlich. Vor allem sind D_j zusätzlich zu den K_j angegeben: Ihre physische Beziehung muss bewiesen werden.

## 7. Konsequenz für das vorgeschlagene Masterprogramm

Das korrekte Diagramm besitzt drei unterschiedliche Aufgaben:

1. **Quelle auswählen:** Algebra, vollständige Relations-/Markierungsdaten, Zustand, lokale Teilalgebren und reale Generatoren aus der TFPT-Seam gewinnen.
2. **Algebren identifizieren:** Eine tatsächliche Φ zu den CAR-/Rotorprozessen angeben, die Produkte, Adjunkte, Zustand und Originaloperationen erhält. Gleiche Dimension oder dieselbe Parent-Grammatrix ist schwächer.
3. **Darstellungen übertragen:** Der obige GNS-Satz liefert dann V und den Dynamiktransport. Ein separater D-Intertwiner plus geometrische Hypothesen trägt die Geometrie mit.

Die GNS-Eindeutigkeit ist also eine Eindeutigkeit der Darstellung gegebener Daten. Der vom Nutzertext gewünschte Satz „Seam bestimmt eine eindeutige physische Prozessquelle“ bleibt eine andere, stärkere Aussage. Ebenso schließt ein Fixpunktsatz erst dann eine Theorie, wenn der Transformationsoperator, sein Bereich, die physische Äquivalenzrelation und Auswahl-/Stabilitätsbedingungen bereits konstruiert sind.

`check_gns.py` kontrolliert eine explizite nichttriviale GNS-Abbildung, Generatortransport, positive/negative Energie, Clockmehrdeutigkeit und den Algebra-Verlust beim geometrischen D. Die allgemeinen Aussagen sind oben bewiesen; ein konkreter TFPT-Cap↔CAR-Intertwiner oder eine TOE wird nicht als konstruiert ausgegeben.
