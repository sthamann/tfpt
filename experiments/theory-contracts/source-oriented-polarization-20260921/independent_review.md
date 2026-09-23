# Unabhängige Gegenprüfung: skalarer CR-Kern, CAR und Cliffordisierung

## Urteil

Der konstruktive skalare Kern ist korrekt:

\[
\mathcal A_{\rm hol}
=\ker(\Lambda+i\partial_s)
\]

ist für eine glatte orientierte kompakte Fläche mit glattem zusammenhängendem Rand genau die Algebra der Randspuren glatter holomorpher Funktionen. Auf der Scheibe ist ihr \(L^2\)-Abschluss der Hardy-Raum der nichtnegativen Fouriermoden. Diese Auswahl gewinnt aus dem positiven Operator \(|D|\) durch die Randorientierung tatsächlich das fehlende Vorzeichen zurück.

Sie liefert aber zunächst eine **skalare Cauchy–Riemann-Polarisierung**. Eine Clifford-/CAR-Konstruktion daraus ist kanonisch möglich, sobald man einen reellen Einteilchenraum, seine Konjugation und gegebenenfalls ein Spin- oder Ladungsbündel festlegt. Sie erzwingt nicht von selbst, dass das physische geladene P1-Feld ein Spinor dieses Bündels ist. Genau diese Feld-/Spinlift-Identifikation bleibt der erste zusätzliche Ursprungssatz.

## 1. Prüfung des DtN–Cauchy–Riemann-Satzes

Belishev–Korikov, arXiv:2103.03944, definieren auf dem Rand den positiv orientierten Einheitstangentialvektor \(\gamma=\Phi\nu\). Für \(w=u+iv\) holomorph liefern die Rand-Cauchy–Riemann-Gleichungen

\[
\Lambda u=\partial_s v,
\qquad
\Lambda v=-\partial_s u.
\]

Zusammen sind sie äquivalent zu

\[
(\Lambda+i\partial_s)(u+iv)=0.
\]

Umgekehrt zeigt die dortige Eindeutigkeitsfortsetzung, dass jedes glatte komplexe Randdatum im Kern die Spur einer holomorphen Funktion ist. Damit ist

\[
\ker(\Lambda+i\partial_s)
=\operatorname{Tr}_{\partial M}\mathcal O(M)
\]

unter den genannten Glattheits-, Orientierungs- und Zusammenhangsvoraussetzungen exakt. Maßgeblich sind die Definition des Randoperators in Gleichung (3) und die Randrelationen in Gleichung (7); die Notwendigkeitsrichtung und ihre Umkehrung stehen im Beweis direkt danach. Quelle: https://arxiv.org/abs/2103.03944

Das Vorzeichen hängt von der Konvention \(\gamma=\Phi\nu\) ab. Eine Umkehr der Randorientierung vertauscht holomorph und antiholomorph. Das ist eine erwartete physische Wahl, kein Defekt.

### Scheibe

Für \(e_n(s)=e^{ins}\), \(\Lambda=|D|\) und \(i\partial_s e_n=-n e_n\) gilt

\[
(\Lambda+i\partial_s)e_n=(|n|-n)e_n.
\]

Der Kern besteht daher aus \(n\ge0\). Die entgegengesetzte Orientierung liefert \(n\le0\). Der konstante Modus liegt in beiden skalaren holomorphen Richtungen; deshalb ist dieser Kern noch nicht ohne Weiteres eine self-duale CAR-Hälfte.

## 2. Weyl-Verhalten

Für \(g'=e^{2\sigma}g\) gilt am Rand mit \(\sigma_b=\sigma|_{\partial M}\)

\[
\Lambda_{g'}=e^{-\sigma_b}\Lambda_g,
\qquad
\partial_{s'}=e^{-\sigma_b}\partial_s.
\]

Also

\[
\Lambda_{g'}+i\partial_{s'}
=e^{-\sigma_b}(\Lambda_g+i\partial_s)
\]

und der holomorphe Randkern ist Weyl-invariant. Das ist stärker als eine Gleichheit nur des Hauptsymbols.

Eine kleine Typgrenze bleibt: Als **Unterraum glatter Randfunktionen** ist der Kern unverändert. Der orthogonale Hardy-Projektor hängt zusätzlich vom gewählten Rand-\(L^2\)-Produkt ab. Unter Änderung der Randdichte muss er mit der entsprechenden unitären Dichteabbildung transportiert werden. Diese Hilbertraumfrage ändert nicht die Kernidentität.

## 3. Self-duale CAR und der Nullmodus

Sei

\[
\Gamma(e_n\otimes v)=e_{-n}\otimes\bar v
\]

die CAR-Konjugation. Auf periodischen Moden liefert \(P_{\ge0}\) die Identität

\[
P_{\ge0}+\Gamma P_{\ge0}\Gamma=I+P_0.
\]

Die reine self-duale Bedingung \(C+\Gamma C\Gamma=I\) wird daher genau durch

\[
C=P_{n>0}\otimes I+P_0\otimes C_0,
\qquad
C_0+\bar C_0=I
\]

repariert. Reinheit verlangt zusätzlich \(C_0^2=C_0=C_0^*\). Auf einem 16-dimensionalen realen internen Raum hat ein solcher \(C_0\) komplexen Rang 8 und entspricht einer orthogonalen komplexen Struktur.

Die Symmetrieaussage ist ebenfalls korrekt. Ein Endomorphismus, der mit der vollen irreduziblen \(Spin(16)\)-Vektorwirkung kommutiert, ist skalar. Self-duale Komplementarität erzwingt dann \(C_0=I/2\). Dieser Operator ist eine gemischte Kovarianz und kein Projektor. Jede reine Rang-8-Wahl reduziert den Stabilisator auf \(U(8)\). Ein reiner, voller \(Spin(16)\)-invarianter periodischer Nullmodenzustand existiert somit in dieser Einteilchenbeschreibung nicht.

Im NS-Sektor liegen die Moden in \(\mathbb Z+\tfrac12\). Es gibt keinen Nullmodus, und

\[
C=P_{n>0}

\]

ist bereits ein reiner self-dualer Projektor. Er ist eindeutig, sobald Spinstruktur, CAR-Konjugation und der tatsächlich geladene tangentiale Dirac-Operator einschließlich seiner Verbindung gegeben sind. Eine zusätzliche Eichholonomie kann das Spektrum verschieben; sie gehört deshalb zu diesem „Dirac-Operator gegeben“ und darf nicht aus der skalaren Formel weggelassen werden.

## 4. Erzwingt natürliche Cliffordisierung den geladenen Spinor?

Nein. Sie ermöglicht ihn funktoriell, schließt aber die physische Identifikation nicht.

### Was funktoriell möglich ist

Aus einem reellen Hilbertraum mit Skalarprodukt kann man die Clifford-/CAR-Algebra bilden. Aus einer zulässigen Polarisierung kann man anschließend die quasifreie Fockdarstellung konstruieren. Der skalare CR-Kern liefert dafür die positive Modenteilung außerhalb des konstanten Modus. Diese Konstruktion ist mathematisch natürlich und benötigt kein frei erfundenes endliches Hamiltonmodell.

### Was dabei nicht folgt

Der skalare holomorphe Randwert ist eine Funktion, also ein Objekt vom konformen Gewicht null. Ein chirales Fermion ist eine Halbform beziehungsweise eine Sektion eines Spinbündels, lokal von der Form

\[
f(z)(dz)^{1/2}.
\]

Der Übergang verlangt eine Quadratwurzel des kanonischen Bündels und eine Identifikation des physikalischen Feldes mit deren Sektionen. Die komplexe Struktur bestimmt das kanonische Bündel, aber im Allgemeinen keine eindeutige Quadratwurzel. Auf einer Fläche positiver Gattung existieren mehrere Spinstrukturen; der skalare DtN-Operator beziehungsweise seine holomorphe Funktionsalgebra wählt keine davon aus.

Es gibt zwar eine kanonische Spin-c-/Dolbeault-Cliffordisierung auf Differentialformen. Sie liefert ein natürliches Clifford-Modul, aber nicht automatisch das gewünschte ehrliche Majorana-Spinbündel, seine Ladungsdarstellung oder die interne 16-fache Multiplizität. Eine Kähler–Dirac-Konstruktion auf Formen beantwortet daher eine andere Typfrage.

### Sonderfall Scheibe

Die Scheibe besitzt eine eindeutige Spinstruktur. Ihre auf den Rand induzierte Struktur ist bounding/NS; in der mitrotierenden Tangentialtrivialisierung erscheinen die Spinormoden halbzahlig. Deshalb gilt:

\[
\text{physisches P1-Feld ist ein über die Scheibe fortsetzbarer Spinor}
\Longrightarrow
\text{NS-Moden und eindeutige reine Hardy-CAR-Polarisierung}.
\]

Der Folgerungspfeil ist stark und konstruktiv. Seine Voraussetzung folgt jedoch nicht aus der skalaren CR-Algebra allein. Man muss beweisen, dass der geladene P1-Feldgenerator gerade eine Sektion dieses Spinbündels ist und dass seine CAR-Konjugation sowie Ladungsverbindung mit dem skalaren Randwörterbuch verträglich sind.

Auch „sheet-odd“ ersetzt diesen Beweis nicht: Ein endliches Vertauschen \(S^+\leftrightarrow S^-\), eine räumliche Doppelüberdeckung und der Spinlift eines einmal umlaufenden Fermions sind drei verschiedene Abbildungen, bis ein gemeinsamer Intertwiner angegeben ist.

## 5. Konsequenz für den v113-Rang-8-Kern

Der endliche v113-Projektor könnte im periodischen Fall **als** \(C_0\) des Nullsektors verwendet werden. Das ist die kleinste mathematisch konsistente Rolle für ihn neben der neuen skalaren Hardy-Auswahl. Aus den bisherigen Formeln folgt diese Rolle aber nicht:

- v113 besitzt keine Fourierzerlegung in \(n>0\), \(n=0\), \(n<0\);
- sein Rang-8-Projektor wird als gesamte endliche Seam-Polarisierung eingesetzt;
- seine reine Wahl hat nur \(U(8)\)-Stabilisator und braucht daher eine begründete Symmetriereduktion;
- im NS-Fall wird er zur Modenpolarisierung überhaupt nicht benötigt und kann höchstens eine andere interne Struktur beschreiben.

Somit darf der vorhandene Rang-8-Test nicht rückwirkend als bereits bewiesene Nullmodenbehandlung gelesen werden.

## Kleinster tragender Folgetest

Der nächste Test ist eine einzige typisierte Quellenabbildung:

\[
\iota_{\rm spin}:
\text{geladene P1-Randgeneratoren}
\longrightarrow
\Gamma\bigl(\partial M,S_{\partial M}\otimes L_q\bigr).
\]

Zu beweisen sind:

1. \(S_{\partial M}\) ist der von der P1-Normalfläche induzierte Spinlift;
2. \(L_q\) und seine Verbindung stammen aus der P1-Einheitswindung statt aus einer nachträglichen Holonomiewahl;
3. die physische CAR-Konjugation entspricht der Bündelkonjugation;
4. der tangentiale Dirac-Spektralprojektor stimmt mit der aus \(\ker(\Lambda+i\partial_s)\) gewonnenen Richtung überein.

Bei NS schließt dies die Polarisationsauswahl ohne internen Nullmodus. Bei Ramond bleibt als genau lokalisierte Restfrage die quellenabhängige Wahl von \(C_0\). Die bloße Existenz eines Clifford-Funktors oder einer endlichen Rang-8-Matrix erfüllt keinen dieser vier Identitätstests.
