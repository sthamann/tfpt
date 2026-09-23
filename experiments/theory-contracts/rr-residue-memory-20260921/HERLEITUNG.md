# TFPT: Die Residuenbrücke braucht ihren konstanten Quellenmodus

21. September 2026 · Forschungs-ID `UR.RR.RESIDUE.01` · Gesamtverdict **PARTIAL**

## Ergebnis und Bedeutung für das Gesamtziel

Die bereits markierte Vierpunktgeometrie liefert eine explizite Abbildung vom fünfteiligen Riemann–Roch-Träger auf die vier Marken. Damit ist eine gemeinsame geometrische Herkunft dieser beiden endlichen Räume ausgeschrieben. Dieselbe Abbildung zeigt aber auch, welche Information eine Identifikation mit einem selbstständig laufenden Viererraum verlieren würde: **Der gemeinsame Markenmittelwert tauscht sich mit der konstanten Quellenfunktion aus.** Die drei übrigen Markenkombinationen sind unter dem vorhandenen Generator invariant.

Beim diskreten Vierteltakt bleibt dieser Austausch unsichtbar: Der ausgelassene Modus kehrt genau zurück. Zur Hälfte dieses Taktes liegt der anfänglich reine Markenmittelwert dagegen vollständig in der konstanten Quellenlinie. Dieser vollständige Austausch folgt sogar für jeden selbstadjungierten Logarithmus derselben Vierteldrehung, der die unten angegebene affine Zeitspiegelung erfüllt.

Die Konsequenz ist konstruktiv und eng: Eine zeiterhaltende Abbildung muss entweder den schon vorhandenen fünften Modus mitführen oder seine exakt berechenbare Rückwirkung enthalten. Ein autonomer Viererquotient reicht unter diesen Voraussetzungen nicht aus. Es wurde kein zusätzlicher Oszillator, kein Bad und kein neuer Kopplungsparameter eingeführt.

**Die vollständige TFPT-Lösung folgt daraus nicht.** Die Rechnung betrifft einen endlichen geometrischen Quellenraum mit der bereits erklärten Hardy-Metrik und Zeit. Sie liefert noch keine lokale, zustandserhaltende Abbildung auf die nativen CAR/CCR-Felder und ihren Wechselwirkungs-Hamiltonoperator. Insbesondere ist die unten berechnete geometrische Rückwirkung nicht die bereits bekannte nichtlineare native Antwort `Σ₂`.

## 1. Voraussetzungen aus dem bestehenden Anschluss

Es gelten unverändert

\[
D=\mu_4=\{1,i,-1,-i\},\quad P(z)=z^4-1,\quad
E=H^0(\mathbb P^1,\mathcal O(D)),\quad e_n=z^n/P\ (0\le n\le4).
\]

Der Raum hat Dimension fünf. Seine markierten Pullbacks lauten

\[
(Rf)(z)=f(iz),\quad (Sf)(z)=f(1/z),\quad
Re_n=i^n e_n,\quad Se_n=-e_{4-n}.
\]

Die konstante Funktion ist \(1=e_4-e_0\). Aus dem vorherigen Hardy-Anschluss werden ausdrücklich übernommen:

\[
\langle f,g\rangle_D=\int_{S^1}|P|^2\bar f g\,\frac{d\theta}{2\pi},
\qquad h=J^{-1}(z\partial_z)J,quad Jf=Pf.
\]

Damit sind die \(e_n\) orthonormal und \(he_n=ne_n\). Die Metrik und die kontinuierliche Zeit sind hier erklärte Voraussetzungen; ihre physische Auswahl aus P1/P2 wird nicht nachträglich behauptet. Es gelten \(e^{i\pi h/2}=R\) und \(ShS=4I-h\).

## 2. Die exakte Abbildung auf die Marken

Definiere die normalisierten Residuen

\[
q_a(f)=\operatorname{Res}_{z=a}\bigl(f(z)\,dz/z\bigr),\qquad a\in D.
\]

Direkt folgt

\[
q_a(e_n)=a^n/4,\qquad \ker q=\mathbb C1.
\]

Eine explizite Rechtsinverse ist durch

\[
l_a(z)=\frac{a}{z-a}+\frac12,\quad q_b(l_a)=\delta_{ab},\qquad
\ell(f)=\frac{f(0)+f(\infty)}2
\]

gegeben. Es gilt \(\ell(l_a)=0\), \(\ell(1)=1\) und für jedes \(f\in E\)

\[
f=\ell(f)\,1+\sum_{a\in D}q_a(f)l_a.
\]

Dies ist keine bloße Dimensionszählung. Abbildung, Kern und Rückweg sind angegeben. Außerdem ist ℓ(f)·1 der D4-Mittelungsprojektor (1/8)∑ₖ₌₀³(Rᵏ+SRᵏ)f. Die Spaltung benötigt bei festem R,S daher keine zusätzliche metrische Auswahl.

Die tatsächliche Gruppenwirkung muss mitgeführt werden:

\[
q_a(Rf)=q_{ia}(f),\qquad q_a(Sf)=-q_{a^{-1}}(f).
\]

Für die Reihenfolge \((1,i,-1,-i)\) ist die Drehung auf Komponenten also \(q'_j=q_{j+1}\). Das ist die inverse Matrix zur aktiven Verschiebung der Basisvektoren \(\mathbf e_j\mapsto\mathbf e_{j+1}\). Die Spiegelung trägt zusätzlich den Charakter \(\chi(R)=1,\chi(S)=-1\). Präzise lautet die exakte Sequenz

\[
0\longrightarrow\mathbb C1\longrightarrow E
\overset q\longrightarrow\chi\otimes F_4\longrightarrow0.
\]

Der rohe Residuenvektor ist daher nicht ohne diesen Charakter das zuvor verwendete unverdrehte Familienfeld. Für logarithmische Differentiale kompensiert die Spiegelung von \(dz/z\) genau dieses Vorzeichen.

## 3. Drei geschlossene Kombinationen und ein gekoppelter Mittelwert

In den Koordinaten \((c,q)\), mit \(c=\ell(f)\), lautet der vorhandene Generator exakt

\[
h=\begin{pmatrix}2&\mathbf1^T\\\mathbf1&M\end{pmatrix},\qquad
M_{aa}=2,\quad M_{ab}=\frac{a+b}{2(a-b)}\quad(a\ne b).
\]

Die Gram-Matrix lautet

\[
G=\operatorname{diag}\left(2,\,4I_4-\tfrac12\mathbf1\mathbf1^T\right).
\]

Diese Norm ist wesentlich: Die Darstellung in Residuenkoordinaten ist keine willkürlich deklarierte euklidische Vierermetrik.

Setze \(u=\mathbf1/2\). Die konstante Linie und die Linie des uniformen Residuenvektors \(u\) sind orthogonal und haben hier dieselbe Norm. In der normalisierten Zweierbasis gilt

\[
h_{\rm Mittelwert}=\begin{pmatrix}2&2\\2&2\end{pmatrix}.
\]

Die übrigen drei Richtungen erfüllen \(\sum_a q_a=0\). Sie sind invariant und tragen die Frequenzen \(1,2,3\). Geometrisch entsprechen sie

\[
H^0(\mathbb P^1,\Omega^1(\log D))
=\operatorname{span}\{z^{k-1}dz/P:k=1,2,3\}.
\]

Die Residuen dieser Differentiale summieren sich zu null. Dabei bleibt der Spiegelungscharakter entscheidend: Der RR-Unterraum trägt F₄⁰⊗χ mit Spiegelspur −1, der Raum logarithmischer Differentiale dagegen F₄⁰ mit Spiegelspur +1. Die Abbildung durch Multiplikation mit dz/z ist also nur mit diesem Twist äquivariant. Das ist eine präzise Dreierstruktur mit den Drehungseigenwerten \(i,-1,-i\). Sie ist kein Nachweis dreier physischer Teilchengenerationen und darf nicht mit dem Farbendreierraum verwechselt werden, dessen Drehungseigenwerte \(1,-1,1\) sind.

## 4. Warum der volle Viererquotient keine autonome Zeit trägt

Bereits der kleinste Test entscheidet:

\[
q(1)=0,\qquad q(h1)=\mathbf1\ne0.
\]

Damit gibt es keinen festen Viereroperator \(A\) mit \(qh=Aq\). Gleiche Residuen zur Startzeit bestimmen ihre spätere Entwicklung nicht: Zwei Quellenfunktionen können sich um eine Konstante unterscheiden, die später wieder in die Residuen eingeht.

Für \(U(t)=e^{-ith}\) ist der exakte Zweierpropagator

\[
U_{\rm Mittelwert}(t)=e^{-2it}
\begin{pmatrix}\cos(2t)&-i\sin(2t)\\-i\sin(2t)&\cos(2t)\end{pmatrix}.
\]

Beginnt der Zustand auf der normierten Mittelwertlinie, beträgt sein Normanteil auf der konstanten Linie

\[
L(t)=\sin^2(2t).
\]

| Zeitpunkt im vorhandenen dimensionslosen Zeitmaß | Mittelwert auf den Marken | Konstante Quellenlinie |
|---|---:|---:|
| \(0\) | 100 % | 0 % |
| \(\pi/4\) | 0 % | 100 % |
| \(\pi/2\) | 100 % | 0 % |

Das sind Normanteile in dem endlichen deklarierten Hilbertraum, keine behaupteten Messwahrscheinlichkeiten eines schon hergeleiteten physischen Quellenfeldes. Die drei orthogonalen Markenkombinationen verlieren keinen Normanteil.

## 5. Der Austausch ist gegen kompatible Logarithmusänderungen stabil

Der folgende Satz ist weiter als die spezielle Hardy-Rechnung, aber seine Voraussetzung wird ausdrücklich genannt.

Sei \(H\) selbstadjungiert bezüglich einer positiven D4-invarianten Metrik und gelte

\[
e^{i\pi H/2}=R,\qquad SHS=2cI-H
\]

für eine reelle Konstante \(c\). Die zweite Gleichung ist eine affine Zeitspiegelung; sie wird nicht allein aus der diskreten D4-Wirkung abgeleitet.

Weil \(H\) mit seiner Exponentialfunktion kommutiert, erhält es die R-Eigenräume. Der R-Eigenraum zum Eigenwert −1 ist eindimensional: \(\mathbb Ce_2\). Dort erzwingt die Spiegelung \(He_2=ce_2\). Die Vierteldrehung verlangt deshalb \(c\in2+4\mathbb Z\).

Auf dem R-Eigenraum +1 liegen genau die konstante Linie mit S-Eigenwert +1 und die Mittelwertlinie mit S-Eigenwert −1. In einer orthonormalen Basis hat H dort die Form

\[
H_+=\begin{pmatrix}c&v\\\bar v&c\end{pmatrix}.
\]

Seine beiden Eigenwerte müssen in \(4\mathbb Z\) liegen. Somit gilt \(|v|\in2+4\mathbb Z\) mit \(|v|>0\). Insbesondere kann die konstante Linie nicht invariant sein. Bei \(t=\pi/4\) gilt sogar \(\cos(|v|t)=0\): Die beiden Linien werden vollständig ausgetauscht, bis auf eine Phase.

**Folge:** Innerhalb dieser Voraussetzungen beseitigen weder eine andere D4-invariante positive Norm noch ein anderer kompatibler kontinuierlicher Logarithmus den Halbzeitaustausch. Wer den konstanten Modus dauerhaft entfernen will, muss mindestens eine dieser ausdrücklich genannten Zeit-/Markierungsvoraussetzungen ändern. Eine zeitabhängige Projektion wäre ebenfalls ein anderer Abbildungsvertrag.

## 6. Exakte Rückwirkung statt eines zusätzlichen Modells

Eliminiert man die konstante Linie rechnerisch, erhält man für den komprimierten Resolventen

\[
P_q(z-h)^{-1}P_q
=\left[z-M-\Sigma_{\rm geom}(z)\right]^{-1},
\qquad
\Sigma_{\rm geom}(z)=\frac{\mathbf1\mathbf1^T}{z-2}
=\frac{4P_u}{z-2}.
\]

Hier ist \(P_u=uu^\dagger\) der Projektor auf den uniformen Markenmodus. Die Gleichung gilt auf dem Viererunterraum in der induzierten Metrik, zunächst außerhalb der relevanten Pole, und danach als rationale Identität. Der Zwischenpol z=2 des Schur-Ausdrucks darf nicht ungeprüft als zusätzlicher Eigenwert der gekoppelten Zweiermatrix gelesen werden: Diese hat die Eigenwerte 0 und 4.

Äquivalent enthält die exakte Vierergleichung für anfänglich verschwindenden konstanten Anteil eine Erinnerung an frühere Werte:

\[
i\dot q(t)=Mq(t)-i\mathbf1\int_0^t e^{-2i(t-s)}\mathbf1^Tq(s)\,ds.
\]

Für \(c(0)\ne0\) kommt der genau bestimmte Term \(\mathbf1e^{-2it}c(0)\) hinzu. Das ist die exakte Eliminierung einer vorhandenen Linie. Sie führt weder ein neues Quantenbad noch eine freie Dämpfung ein; das endliche geschlossene System kehrt periodisch zurück.

## 7. Rückprüfung der Hodge-Abkürzung

Der parallel geprüfte Hodge-Gedanke schließt den lokalen geladenen Quellenanschluss nicht. Die fest markierte \(D_5+A_3\)-Verklebung besitzt die beiden Klassenuntergruppen \(H_+=\langle(1,1)\rangle\) und \(H_-=\langle(1,-1)\rangle\) in \(\mathbb Z_4^2\). Alleinige Familienkonjugation vertauscht diese beiden Klebungen. Der entsprechende Ausschluss für die ursprünglichen 64 Gewichte steht bereits im bestehenden `family_intertwiner`-Beweis; er wird hier nicht als neue Entdeckung gezählt.

Der RR-Hodge-Operator kann auf einer vollständigen Clifford-Algebra algebraisch gehoben werden. Im vorhandenen W-Anschluss ist er aber zunächst ein Bosonenbasiswechsel. Dass dieser allein W nicht fixiert, beweist keine Unmöglichkeit sämtlicher kombinierten Transformationen. Für die konkret benötigte physische Brücke fehlen weiterhin die passende markierte Feldabbildung und eine nachgewiesene gemeinsame Hamiltonsymmetrie. Der ausführliche Prüfbericht liegt bei.

## 8. Was damit geschlossen ist – und was für die vollständige Lösung fehlt

**Geschlossen, unter den angegebenen geometrischen Voraussetzungen:** die konkrete Residuenabbildung samt D4-Charakter, die eindeutige Quellenzerlegung über die gewählte 0/∞-Mittelung, die Dreierinvarianz für die bestehende Clock, der unvermeidbare Halbzeitaustausch unter affiner Zeitspiegelung und die exakte Rückwirkung der vorhandenen konstanten Linie.

**Nicht geschlossen:** Die geometrische Konstante ist noch kein identifiziertes natives physisches Feld. Sie ist insbesondere nicht ohne weitere Abbildung der native Spinor-Vakuumplatz \(\Lambda^0E\), der Familienmittelwert in \(\Lambda^{\rm even}E\otimes F_4\), ein Higgsfeld oder ein Bad. Verschiedene Konstruktionen mit einer eindimensionalen Komponente sind nicht deshalb dasselbe Objekt.

Der entscheidende fehlende Satz bleibt eine lokale, ladungs-, graduierungs-, zustands- und zeiterhaltende Abbildung von der ursprünglichen Quelle auf die nativen Felder, die deren W-Paarprodukt tatsächlich erzeugt. Eine solche Abbildung muss die hier bestimmte Linienkopplung entweder mittransportieren oder ihre Eliminierung begründen. Die Übereinstimmung einzelner Pole, Dimensionen oder diskreter Marken reicht nicht. Insbesondere kann `Σ_geom` nicht ohne diesen Satz mit der nativen nichtlinearen Antwort `Σ₂` identifiziert werden.

Die Rechnung verengt damit den zulässigen Quellenanschluss. Sie schließt kein physisches T1–T8-Gate und behauptet keine vollständige Theorie. Vorhandene Compiler-, E8-, Ladungs-, Clock-, Grundzustands- und Antwortresultate behalten jeweils ihren dokumentierten Geltungsbereich.
