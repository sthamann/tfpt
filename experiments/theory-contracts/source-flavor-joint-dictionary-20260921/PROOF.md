# TFPT: gemeinsamer Flavoranschluss und physische Auswahl

21. September 2026 · `UR.SOURCE.FLAVOR_JOINT_DICTIONARY.01` · **PARTIAL**

## Ergebnis

Der tatsächliche Flavorcompiler Q, sein Sigma-Split Q± und die bereits im Original hergeleiteten D4-Generatoren lassen sich zusammen auf den Residuenraum der vier Nahtmarken übertragen. Dies ist ein abstraktes endliches D4-Modulwörterbuch nach Wahl der markierten Residuenbasis. Eine einzige explizite Abbildung erhält dabei alle Operatorprodukte; ihre induzierte Gramform wird mitgeführt. Dafür ist weder ein neuer Hamiltonoperator noch eine neue Bedeutung der Compilerinvolution erforderlich. Dies beweist nicht, dass der physische Generationenraum mit H¹ beziehungsweise dem Residuenraum identisch ist.

Dies korrigiert eine konkrete ältere Identifikation: Das vereinfachte Operatorpaar aus v69 ist dem tatsächlichen Paar aus v50 nicht gemeinsam ähnlich, obwohl sogar die Spektren aller Linearkombinationen übereinstimmen. Im tatsächlichen Paar existiert ein zusätzlicher gerichteter Operatorblock. Die späteren ursprünglichen D4-Konstruktionen liefern eine passende Darstellung; in ihr muss der vollständige Q-Operator erhalten bleiben.

Die physische Auswahl dieses Wörterbuchs aus dem ursprünglichen Nahtkern ist dadurch nicht bewiesen. Die Konstruktion beginnt beim bereits hergeleiteten Compiler und transportiert ihn zur Geometrie. Sie leitet ihn nicht umgekehrt aus dem rohen geladenen Quellenprozess ab. Die bestehenden Flavorformeln und ihre Zahlenwerte werden nicht verändert. Es erfolgt keine Paper- oder Ledger-Promotion.

## 1. Originaloperatoren und ursprüngliche D4-Wirkung

Aus v50 und den späteren v97/v98/v141/v146 verwenden wir unverändert

\[
Q=\begin{pmatrix}3&1&0\\3&2&0\\3&2&1\end{pmatrix},\quad
\Sigma=\operatorname{diag}(1,-1,-1),\quad
T_A=\begin{pmatrix}0&1&0\\1&0&0\\2&-2&1\end{pmatrix},\quad G=T_A\Sigma.
\]

Es gelten T_A²=Σ²=I, G⁴=I und T_A G T_A=G⁻¹. Insbesondere ist Σ=T_A G eine Spiegelung dieser D4-Darstellung. Wir ersetzen sie nicht durch die zentrale Halbdrehung G².

Mit A=Q+=(Q+ΣQΣ)/2, B=Q−=(Q−ΣQΣ)/2 und

\[
V=\begin{pmatrix}1&0&0\\0&1&0\\0&2&1\end{pmatrix}
\]

folgt genau

\[
A_0=V^{-1}AV=\operatorname{diag}(3,2,1),\qquad
B_0=V^{-1}BV=\begin{pmatrix}0&1&0\\3&0&0\\-3&0&0\end{pmatrix}.
\]

Die Q+=1-Linie trägt unter G den Eigenwert −1; auf den Q+=2,3-Linien wirkt G als Vierteldrehung. Q+ ist somit eine kovariante Gradierung, kein mit der gesamten D4-Gruppe kommutierender Operator. Dies ist bereits in der späteren Deckauswahl angelegt. Insbesondere wird hier keine Identität mit einem zugleich in den G-Charakterräumen diagonalen Euleroperator behauptet: Gemeinsame Intertwiner müssen auch den Kommutator erhalten. Eine vollständig D4-invariante hermitesche Antwort wäre auf dem irreduziblen Zweierraum skalar; dies widerlegt nicht die hier verwendete Gradierung.

## 2. Das vollständige gemeinsame Wörterbuch

Auf den vier Marken seien die Permutationswirkungen

\[
r(x_0,x_1,x_2,x_3)=(x_3,x_0,x_1,x_2),\qquad
s(x_0,x_1,x_2,x_3)=(x_0,x_3,x_2,x_1).
\]

Der Residuenraum U=ker(Σx_i) hat die Basis

\[
H=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\\-1&-1&-1\end{pmatrix}.
\]

Die induzierten Generatoren sind

\[
r_H=\begin{pmatrix}-1&-1&-1\\1&0&0\\0&1&0\end{pmatrix},\qquad
s_H=\begin{pmatrix}1&0&0\\-1&-1&-1\\0&0&1\end{pmatrix}.
\]

Ein gemeinsamer Intertwiner lautet

\[
\boxed{X=\begin{pmatrix}-1&-3&1\\1&1&-1\\1&-1&1\end{pmatrix}},\qquad \det X=4.
\]

Direkte Multiplikation ergibt XG=r_H X und XT_A=s_H X. Zugleich werden

\[
\Sigma_H=X\Sigma X^{-1}=s_Hr_H
=\begin{pmatrix}-1&-1&-1\\0&0&1\\0&1&0\end{pmatrix}
\]

und der vollständige Compiler übertragen:

\[
\boxed{Q_H=XQX^{-1}=\begin{pmatrix}2&-3&-4\\0&2&1\\-1&0&2\end{pmatrix}}.
\]

Sein tatsächlicher Split ist

\[
A_H=\begin{pmatrix}3/2&-1/2&-1\\1/2&5/2&1\\-1/2&1/2&2\end{pmatrix},\qquad
B_H=\begin{pmatrix}1/2&-5/2&-3\\-1/2&-1/2&0\\-1/2&-1/2&0\end{pmatrix}.
\]

Es gelten Q_H=A_H+B_H und A_H=(Q_H+Σ_H Q_H Σ_H)/2, analog für B_H. Für jedes nichtkommutative Operatorwort p gilt

\[
p(A_H,B_H,r_H,s_H)=X\,p(A,B,G,T_A)\,X^{-1}.
\]

Damit erhält dieselbe Abbildung alle Produkte. Die passende D4-Modulstruktur wurde schon zuvor gezeigt; der neue Audit ergänzt den gemeinsamen Transport des tatsächlichen Q±-Paares samt Normen und grenzt ihn von der unzutreffenden vereinfachten Normalform ab.

**Gittergrenze:** X identifiziert die reellen bzw. komplexen Darstellungen. det X=4 ist keine unimodulare Identifikation der hier gewählten ganzzahligen Gitter. Der frühere Index-2-Befund betrifft eine anders gestellte Homologie-/Deckfrage; Gitter, Dualisierung und Generatorbedingungen müssen vor einem Vergleich getrennt werden.

## 3. Gramform und verbleibende Freiheit

Die kanonische Residuenpaarung induziert F=H†H=I+11ᵀ. Ihr Pullback bei obigem X ist

\[
\boxed{G_X=X^\dagger F X=\begin{pmatrix}4&0&0\\0&20&-8\\0&-8&4\end{pmatrix}>0}.
\]

Die führenden Hauptminoren sind 4,80,64. G und T_A sind bezüglich G_X unitär. Die isometrische Karte aus einem orthonormalen Compilerraum lautet

\[
J=HXG_X^{-1/2},\qquad J^\dagger J=I.
\]

Mit Q_can=G_X^(1/2) Q G_X^(−1/2) gilt auf U

\[
JQ_{\rm can}J^\dagger=H Q_H F^{-1}H^\dagger.
\]

Dies führt Norm und Operator gemeinsam mit. G_X ist die aus einer gewählten endlichen Abbildung zurückgezogene Residuenmetrik, nicht bereits die aus P1 rekonstruierte physische Zweipunktform.

Die gesamte Lösungsmenge der beiden linearen Intertwinerbedingungen ist

\[
X(a,b)=\begin{pmatrix}-a-2b&-a-4b&b\\a+2b&-a&-b\\a+2b&a&b\end{pmatrix},\quad
\det X(a,b)=4b(a+2b)^2.
\]

Sie ist invertierbar für b≠0 und c=a+2b≠0. Für komplexe Parameter gilt

\[
V^\dagger G_{X(a,b)}V=4\operatorname{diag}(|c|^2,|c|^2,|b|^2).
\]

Die D4-Darstellung allein lässt also die relative Norm des Einser- und des Zweierraums frei. Die einfache Wahl a=−1,b=1 setzt beide gleich. Es gibt jedoch eine stärkere, schon im bisherigen Gitterprogramm motivierte Auswahl: minimaler ganzzahliger Index.

Für ganzzahlige Intertwiner ist der kleinste nichtverschwindende Betrag der Determinante 4. Er erzwingt b=±1 und c=±1. Die vier Lösungen (a,b)=(−1,1),(−3,1),(1,−1),(3,−1) unterscheiden sich nur durch Gesamtvorzeichen und die vorhandene Rotation G². Sie induzieren dieselbe Gramform. Unter dieser Zusatzbedingung existiert somit eine einzige solche Äquivalenzklasse; der oben gewählte Repräsentant ist kein kontinuierlicher Fit.

Dasselbe wird an den Normen besonders deutlich. Alle reellen symmetrischen D4-invarianten Formen lauten

\[
M(u,v)=\begin{pmatrix}u&0&0\\0&u+4v&-2v\\0&-2v&v\end{pmatrix},\qquad \det M=u^2v.
\]

Positivität verlangt u,v>0. Ganzzahligkeit verlangt u,v ganzzahlig. Die zusätzliche Unimodularität det M=1 erzwingt u=v=1. Also ist

\[
\boxed{M_0=G_X/4=\begin{pmatrix}1&0&0\\0&5&-2\\0&-2&1\end{pmatrix}}
\]

die eindeutige positive ganzzahlige unimodulare D4-invariante Form. Die Division durch 4 entfernt den gemeinsamen ganzzahligen Faktor der induzierten Form; sie ist weder die c3-Normierung noch eine Festlegung der Quellenkovarianz. Minimalindex und diese Formeigenschaft geben hier dieselbe relative Normierung. Die früheren Quellen untersuchen minimale Gitterindizes; sie beweisen aber nicht, dass P1 diese Bedingung für die volle physische Zweipunktform auswählt. Algebraische Auswahl und physische Herkunft bleiben getrennte Aussagen.

Für positive reelle b,c ergibt die kanonische Normierung bereits beim B-Vertex

\[
B_{\rm can}=\begin{pmatrix}0&1&0\\3&0&0\\-3b/c&0&0\end{pmatrix}
\]

mit singulären Werten 1, 3√(1+(b/c)²), 0. Die Eigenwerte bleiben gleich, die normierte Übergangsstärke hängt aber von der relativen Quellennorm ab. Unter der Minimalindex-Auswahl gilt |b/c|=1, also erhält man 1,3√2,0. Der Test identifiziert eine benötigte Eingangsgröße und führt kein neues dynamisches Modell ein. D4-Kovarianz allein enthält die zusätzliche Gitterauswahl nicht.

## 4. Der gemeinsame Fehler in der vereinfachten v69-Normalform

v69 verwendet nach derselben Reihenfolge der A-Eigenwerte

\[
A_1=\operatorname{diag}(3,2,1),\qquad
B_1=\begin{pmatrix}0&\sqrt3&0\\\sqrt3&0&0\\0&0&0\end{pmatrix}.
\]

Die einzelnen charakteristischen Polynome stimmen mit denen von A_0,B_0 überein. Sogar für jedes t gilt

\[
\det(xI-A_0-tB_0)=\det(xI-A_1-tB_1)
=(x-1)((x-3)(x-2)-3t^2).
\]

Mit den polynomialen Spektralprojektoren P_j(A) gilt jedoch

\[
\boxed{P_1(A_0)B_0P_3(A_0)=-3E_{31}\ne0},\qquad
P_1(A_1)B_1P_3(A_1)=0.
\]

Ein invertierbarer gemeinsamer Basiswechsel kann einen nichtverschwindenden Operator nicht in null verwandeln. Es existiert somit keine gemeinsame Ähnlichkeit. Die erzeugten unitalen assoziativen Algebren haben entsprechend Dimensionen 7 bzw. 5. Dieser Befund ist metrischunabhängig und exakt.

Die Originalprogramme bestehen ihre bisherigen Prüfungen: v50 7/7, v69 8/8. Die letzten beiden geometrischen Schlussbehauptungen in v69 werden allerdings durch konstante True-Prüfungen eingetragen, nicht durch einen gemeinsamen Intertwinerbeweis. Der hier fehlende Test war in den bisherigen Erfolgszahlen nicht enthalten.

Eine positive Form kann die fehlende gemeinsame Ähnlichkeit nicht heilen. Sollten beide ursprünglichen Operatoren darüber hinaus selbstadjungierte Observablen derselben positiven Form sein, erzwingt A_0 eine diagonale Form diag(g1,g2,g3); B_0 verlangt g1=3g2 und g3=0. Das ist nicht positiv definit. Ihre korrekte Verwendung als Compilerabbildungen oder nichtselbstadjungierte Vertizes wird dadurch nicht ausgeschlossen.

## 5. Eine zusätzliche Diagnose für den neuen Zeit-/Kovarianztext

Die v69-Normalform ist mit unterschiedlichen linken und rechten Karten erreichbar. Für E=E32, S=diag(√3,1,1), L=S(I+E), R=(I−2E)S⁻¹ gilt

\[
LA_0R=A_1,\quad LB_0R=B_1,\quad LR=I-E\ne I.
\]

Gleichzeitig wird

\[
L(zI-A_0-tB_0)R=z(I-E)-A_1-tB_1.
\]

Das ist eine strikte Äquivalenz eines Matrixbüschels, kein produkt- und zeiterhaltender gemeinsamer Basiswechsel. Die linke und rechte Gramform müssen mitgeführt werden. Den Koeffizienten von z wieder auf I zu setzen ändert die Antwort. Dieser algebraische Vergleich erklärt die Rolle von Norm und Zeit, macht den Compiler aber nicht zu einem Hamiltonoperator. Der bevorzugte Anschluss aus Abschnitt 2 benötigt diese zweiseitige Umdeutung nicht.

## 6. Rückbindung an die vollständige Lösung

Die vorhandenen Ergebnisse bleiben verbunden: P1/P2, Compiler und E8, Flavorformeln, Clocks, native Fock-/RR-Dynamik und die bedingten Rekonstruktionssätze. Offen ist ihre gemeinsame Herkunft in demselben geladenen Quellenprozess.

Der Quellenaudit trennt die tatsächlich spezifizierten Objekte:

1. P1 deklariert orientierte Naht, Reflexionspositivität, Einheitswindung und c3-Normierung. Dies liefert noch keine explizite geladene Zustandsfunktion mit allen Einfügungen und ihrer Zeitwirkung.
2. Die Geometrie liefert U, die Residuenpaarung und D4. Die vorhandene Greenmatrix hat einen Einser- und einen Zweierblock mit bekannter Eigenwertdifferenz −log 2. Ihre Gleichsetzung mit dem rohen P1-Calderónoperator ist der eigene offene Nachweis `QGEO.KERNEL.01`.
3. Die konkreten CAR-/QWZ- und nativen W-Realisierungen liefern innerhalb ihrer zusätzlichen Annahmen Felder, Zustand und Zeitantwort. Ihre internen Rechnungen leiten die Auswahl dieser Realisierungen aus P1 nicht nachträglich her.

Die Papers enthalten explizite Kernel-Templates und Familien; der Befund lautet nicht, dass dort keine Kernformeln existieren. Die ausgewerteten Beispiele hängen von einer zusätzlichen Polarisation A, einem Zustand, einer Metrik oder Projektionen ab. Was nicht geliefert wird, ist die eindeutige Auswahl des rohen geladenen P1-Kerns mitsamt seiner physikalischen Zeit.

Auch Residuenpaarung und Greenkern dürfen nicht verschmolzen werden. Für die bekannte viermarkige Greenmatrix mit gemeinsamer Diagonale d, Nachbareintrag −(log 2)/2 und gegenüberliegendem Eintrag −log 2 ergibt der obige gemeinsame Transport exakt

\[
X^\dagger H^\dagger K_{\rm Green}HX=4M(d+\log2,d).
\]

Diese Form ist auf U für d>0 positiv, aber für kein endliches d proportional M0. Die bekannte Green-Anisotropie verschwindet nicht durch die kanonische Gitterwahl. M0 beschreibt die transportierte Residuennorm; K_Green ist ein anderer, bereits vorhandener Kernelkandidat. Welcher davon welche physische Rolle hat, muss die Quelle bestimmen. Insbesondere darf die gewünschte Quellenkovarianz nicht nachträglich auf M0 festgesetzt werden.

Die vollständige Antwort der symmetrischen nativen W-Bank ist im Familienindex skalar. Weitere symmetrieerhaltende Komplementelimination erzeugt allein keine Hierarchie. Ein konstanter linearer Feldwechsel führt eine Gramform ein; nach kanonischer Normierung bleibt dieselbe skalare Antwort. Dies schließt weder anders begründete Quellen noch nichtlineare Felder oder einen hergeleiteten Higgs-Hintergrund aus.

Der zuerst benötigte Herkunftsschritt ist damit präzise: **Der rohe Quellenprozess muss eine Karte nach U und deren physische Zweipunktform liefern, die mit dem tatsächlichen Q±-Paar und den Original-D4-Generatoren zusammenpasst.** Danach müssen derselbe Prozess und derselbe Zustand den geladenen Vertex und die Zeitantwort bestimmen. Sie dürfen nicht aus Q_H, Gamma, Vaux oder einem gewünschten RR-Block eingesetzt werden. Die früher getesteten Energien 3,4,5 bleiben kandidatenbezogene Tests.

Aus der endlichen D4-Darstellung allein sind diese Daten nicht bestimmbar; Abschnitt 3 zeigt sowohl die freie Normierung als auch ihre bedingte algebraische Auswahl. Derselbe Zustandsprojektor bestimmt außerdem nicht den Betrag des Zeitgenerators, wie der vorhandene Zustands-/Dynamik-Audit bereits zeigt. Mehr Spektren schließen diese beiden unterschiedlichen Lücken nicht.

**Die vollständige physische TFPT-Lösung ist nicht erreicht.** Erreicht ist ein korrekter gemeinsamer endlicher Anschluss, eine eindeutige minimale Gitterklasse und ein überprüfbarer Ausschluss der vereinfachten gemeinsamen Normalform. Die Quellenidentifikation wird dadurch präzisiert, nicht vorausgesetzt. Raumzeit-, Kontinuums-, chirale, Kopplungs-, Gravitations- und Zustandsnachweise werden nicht geschlossen. Kein T1–T8-Gate wird als erledigt markiert.

## 7. Quellen und Prüfstatus

- `verification/v50_q_geometry.py` und `v69_d4_q_geometry.py`: Originaloperatoren und bisherige Prüfungen.
- `tfpt_2_standard_model.tex`, v97/v98/v141/v146: tatsächliche D4-Wirkung, Deckauswahl, Spiegelungsklassen und physische Realisierungsvoraussetzung.
- `tfpt_1_architecture_e8.tex`, P1/P2, Family=A3 und The metric, computed: Originalpostulate, Residuenpaarung und Greenmetrik.
- `rr-continuous-clock-20260921`, `rr-three-family-state-20260921`: volle native Antwort, geometrische Familienauswahl und Zustandssektor.
- `primitive-charged-source-response-20260921`: Quellenprovenienz und konkrete bedingte geladene Realisierungen.
- `symmetric-source-car-interface-20260921`: vorhandene symmetrische Wechselwirkungsalternative und ihre Quellenvoraussetzungen.

Der Begleitprüfer verwendet exakte Matrizen; Normal- und optimierter Lauf stimmen bytegenau überein. Eingabe-Hashes und ein unabhängiger Quellenreview dokumentieren die Herkunft. Die endlichen PASS-Prüfungen sind vom gesamten physischen Verdict PARTIAL zu unterscheiden.
