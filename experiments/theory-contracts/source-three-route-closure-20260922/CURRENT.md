# Stromkanäle: exakte Antwortbedingung und Herkunftsgrenze

22. September 2026 · `UR.SOURCE.THREE_ROUTE_CLOSURE.01` · **CONDITIONAL**

## 1. Direkter Test der ursprünglichen Quelle

Die vorherige Rechnung beweist für normalgeordnete Grassmannprodukte

\[
B_a=iR_aL_a,\quad J_R^{ab}=iR_aR_b,\quad J_L^{ab}=iL_aL_b,
\qquad B_aB_b=-J_R^{ab}J_L^{ab}\quad(a<b).
\]

Damit ist der Gross–Neveu-Vierfermionterm als Stromkopplung in den Kanälen 45, 15 und 60 formulierbar. Diese Identität verlangt keine zusätzliche elementare skalare Massenquelle. Sie bestimmt keinen Propagator und keinen Zustand.

Ein direkter Anschluss ist möglich, sofern die ursprüngliche Quelle tatsächlich Operatoren \(O_R^a,O_L^a\) und ihre linearen Kopplungen an physische Ströme liefert. Kopplungsfaktoren seien in \(O\) enthalten. Für dieselbe Quelle und denselben Zustand sei

\[
W[j]=\log\left\langle\mathcal T\exp\!\left(-\int j_iO_i\right)\right\rangle,
\qquad C_{ij}(x,y)=\langle\mathcal T O_i(x)O_j(y)\rangle_c.
\]

Für ein reguliertes, zweimal stetig funktional differenzierbares \(W\) gilt am Ursprung

\[
-W[j]=\int j_i\langle O_i\rangle
-\frac12\int j_i(x)C_{ij}(x,y)j_j(y)+o(\|j\|^2).
\]

Setzt die **hergeleitete** Kopplung \(j=(J_R,J_L)\), ist der gemischte Vierfermion-Koeffizient daher \(-C_{RL}\). Dies ist eine Ableitungsidentität, kein Gauß-Postulat. Bei einer Gaußquelle endet die Entwicklung bei zweiter Ordnung; sonst bleiben höhere verbundene Antworten und weitere Wechselwirkungen. Direkte Vierfermion- oder Kontaktterme müssen zusätzlich berücksichtigt werden. Ohne Kleinfrequenznäherung ist der Ausdruck im Allgemeinen nichtlokal.

Die Trennung zwischen ausintegriertem Quellensektor und verbleibenden Strömen muss aus TFPT stammen. Dieselben Freiheitsgrade dürfen nicht als unabhängige Quelle und als verbleibende Fermionen doppelt gezählt werden. Diese Rechnung setzt eine zulässige Trennung voraus; sie begründet sie nicht.

## 2. Vorzeichenkriterium

Unter Zeittranslationsinvarianz, einem tatsächlichen räumlich/chiralen Austausch \(J_R\leftrightarrow J_L\), reeller symmetrischer Antwort und einer begründeten Reduktion auf einen invarianten Kanal sei

\[
\Sigma(\omega)=\begin{pmatrix}a(\omega)&c(\omega)\\c(\omega)&a(\omega)\end{pmatrix},
\qquad C_\pm(\omega)=a(\omega)\pm c(\omega).
\]

In der erklärten Fierz-Konvention folgt

\[
\boxed{g(\omega)=-c(\omega)=\frac{C_-(\omega)-C_+(\omega)}2.}
\]

Für die folgende punktweise Frequenzaussage wird außerdem ein positiver hermitescher Spektralkern vorausgesetzt; OS-Positivität allein ist kein Ersatz für diese Voraussetzung. Positive Kovarianz fordert \(C_\pm\ge0\), aber nicht deren Reihenfolge. Die Beispiele \((C_+,C_-)=(2,1)\) und \((1,2)\) haben dieselbe Spur und dasselbe ungeordnete Spektrum, ergeben aber \(g=-1/2\) und \(g=+1/2\). Ihre Orientierung relativ zu den tatsächlichen rechten und linken Vertices entscheidet das Vorzeichen.

Die drei Zahlen \(g_D,g_F,g_X\) reichen nur bei begründeter Invariantenreduktion und ohne weitere Mischungen. Unter voller \(SO(10)\times SO(6)\)-Invarianz trennen die nichtäquivalenten irreduziblen Kanäle \((45,1),(1,15),(10,6)\) die Antwort nach Schurs Lemma. Dass Zustand und Vertices diese Voraussetzung erfüllen, ist offen. Die Kanalwerte im Zertifikat sind illustrative Beispiele.

Räumlicher/chiraler Austausch ist nicht OS-Zeitreflexion. Deck-Ungeradheit von \(D_{\mathrm{rel}}\) beweist keine physische \(J_R-J_L\)-Kopplung. Das OS-Doppel liefert nicht von selbst zwei unabhängige chirale Teilchenzweige. Auch ein imaginärer euklidischer Vertex darf nicht bloß zur Vorzeichenkorrektur eingeführt werden; seine Herkunft aus der hermiteschen Theorie wäre zu beweisen.

## 3. Zeitantwort und kontrollierte lokale Näherung

Für den ausschließlich als Antwortdiagnose benutzten skalaren Kernel

\[
C_m(t)=\frac{e^{-m|t|}}{2m},\qquad
\widehat C_m(\omega)=\frac1{\omega^2+m^2}
\]

ist die OS-Matrix \(C_m(t_i+t_j)=v_iv_j/(2m)\), \(v_i=e^{-mt_i}\), auf positiven Zeiten positiv. Auf \(|\omega|\le\Omega\) gilt

\[
\frac{|\widehat C_m(\omega)-\widehat C_m(0)|}{\widehat C_m(0)}
=\frac{\omega^2}{m^2+\omega^2}\le\frac{\Omega^2}{m^2}.
\]

Mit unterschiedlichen Paritätsmassen,

\[
C_\pm(\omega)=\frac{y_\pm^2}{\omega^2+m_\pm^2},
\]

ergibt der exakt symbolisch geprüfte Zeuge \(y_-^2=1,m_-^2=1,y_+^2=2,m_+^2=4\)

\[
g(\omega)=\frac{2-\omega^2}{2(\omega^2+1)(\omega^2+4)}.
\]

Beide Kanal-Kovarianzen bleiben positiv, während \(g(0)=1/4\), \(g(\sqrt2)=0\) und oberhalb \(g(\omega)<0\) gilt. Positive statische Kopplung allein garantiert also keine Attraktion auf jedem Frequenzband.

Aus

\[
\left|\frac{y^2}{\omega^2+m^2}-\frac{y^2}{m^2}\right|
=\frac{y^2\omega^2}{m^2(\omega^2+m^2)}\le\frac{y^2\omega^2}{m^4}
\]

folgt durch Dreiecksungleichung

\[
|g(\omega)-g(0)|\le\frac{\omega^2}{2}
\left(\frac{y_-^2}{m_-^4}+\frac{y_+^2}{m_+^4}\right).
\]

Ein positives \(g(0)\), das diese Fehlergrenze bei \(\Omega\) übertrifft, sichert Attraktion auf dem Band in diesem Antwortmodell. Für eine quantitative lokale Näherung muss der Fehler gegenüber \(g(0)\) klein sein. Weder Band noch Massen werden dadurch aus TFPT ausgewählt.

## 4. Native Quellenlage und Typprüfung

Der operationale Seed nimmt den Kragengenerator als Eingabe: [01_boundary_kernel_source.tex](/Users/stefanhamann/Projekte/tfpt-theoryv4/_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex:480). Die OS-Konstruktion setzt geeignete bosonische und CAR-Kerne voraus: [04_qft_source.tex](/Users/stefanhamann/Projekte/tfpt-theoryv4/_archive/tfpt-45/source_extracts/04_qft_source.tex:474). Invariante Yukawa-Trilineare sind bereits vorhanden: [02_carrier_source.tex](/Users/stefanhamann/Projekte/tfpt-theoryv4/_archive/tfpt-45/source_extracts/02_carrier_source.tex:2088). Ihre Existenz liefert den Stromantwortkern nicht automatisch.

Das vorhandene Funktional \(W_k[J]\) ist der passende formale Ort für Quellenableitungen: [04_qft_source.tex](/Users/stefanhamann/Projekte/tfpt-theoryv4/_archive/tfpt-45/source_extracts/04_qft_source.tex:2164). Seine Definition setzt \(S_{\rm adm}\), Felder und Maß voraus. Die folgende exakte Flussgleichung wählt diese Eingaben nicht selbst.

Die bekannte Multiplikation \(\Lambda^2(16,4)\to(10,6)\) und der GN-Mischstrom aus Vektoren \((10,1)\otimes(1,6)\to(10,6)\) haben verschiedene Eingangsobjekte. Der gemeinsame Ausgangskanal identifiziert weder Felder noch Zustand noch Propagator. Die Gram-Norm des ersten Produkts ersetzt \(C_{RL}\) daher nicht.

**Offen:** die tatsächlichen geladenen Operatoren, ihre Stromvertices und die verbundene Antwort \(C_{RL}(\omega)\) im selben hergeleiteten Zustand. Die Antwortbedingung ist ausgerechnet; ihr TFPT-Wert ist nicht berechnet. Ein zusätzliches elementares Mediatorfeld ist dafür keine zwingende Voraussetzung.
