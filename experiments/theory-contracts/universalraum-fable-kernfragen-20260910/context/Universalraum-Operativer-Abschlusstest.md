# Ein ausführbarer Abschluss-Test für eine gemeinsame Prozessquelle

10. September 2026. Neue Anwendung und Gegenprüfung innerhalb dieses Forschungsdurchgangs; kein Anspruch auf erstmalige Erfindung des allgemeinen Momenten- oder Rekonstruktionsverfahrens.

## 1. Was eindeutig rekonstruiert werden kann

Eine Hilbertquelle mit normiertem Anfangsvektor Ω und endlich vielen **beschränkten** Operatoren A_s sei gegeben. Die Liste enthält mit jedem Operator sein Adjungiertes. Wähle Wörter w_1=1,w_2,…,w_r dieser ursprünglichen Operatoren, deren Vektoren v_i=w_iΩ linear unabhängig sind. V bezeichnet die Spaltenabbildung mit diesen Vektoren, G=V†V>0 ihre Gram-Matrix. Aus den ursprünglichen **gemischten, geordneten** Antworten bilde

\[
B_s=V^\dagger A_sV,\qquad K_s=V^\dagger A_s^\dagger A_sV,
\qquad R_s=K_s-B_s^\dagger G^{-1}B_s.
\]

Dann ist P=VG⁻¹V† die orthogonale Projektion auf S=ran V und

\[
R_s=(A_sV)^\dagger(1-P)(A_sV)\ge0.
\]

Insbesondere ist R_s=0 genau dann, wenn A_s S⊂S. Gilt das für alle ursprünglichen Generatoren samt Adjunkten, ist S reduzierend, enthält Ω und enthält sämtliche erzeugten Wortvektoren. Weil die v_i ihrerseits Wortvektoren sind, ist S genau der zyklische Quellenraum.

Die rekonstruierten Operatoren in der Wortbasis sind

\[
J_s=G^{-1}B_s,\qquad A_sV=VJ_s.
\]

Damit folgen **alle zukünftigen geordneten Wortantworten** aus endlich vielen Daten, etwa Ω†A_sA_tΩ=e_1†GJ_sJ_te_1. Zwei solche Quellen mit denselben benannten Antwortmatrizen sind auf ihren zyklischen Räumen durch v_i↦v'_i unitär äquivalent. Unsichtbare, nichtzyklische Zusatzräume werden nicht bestimmt. Zusätzliche integrale Markierungen müssen als Daten mitgeführt werden; eine beliebige komplexe Basisänderung rekonstruiert kein ausgezeichnetes Ganzzahlgitter.

Ein nichtverschwindendes R_s ist konstruktiv: rank R_s ist genau die Zahl unabhängiger Richtungen von A_sS außerhalb S. Die basisunabhängige maximale Leckage erfüllt

\[
\|(1-P)A_sP\|^2
=\|G^{-1/2}R_sG^{-1/2}\|.
\]

Dies ist eine elementare Form des Gram-/Momentenabschlusses. Allgemeine positive Erweiterungssätze auf *-Algebren gehören bereits zur Literatur, etwa [Mourrain und Schmüdgen, *Flat extensions in *-algebras*](https://arxiv.org/abs/1406.4975). Hier wird nicht aus beliebigen numerischen Tabellen die Existenz einer ursprünglichen Quelle behauptet: Voraussetzung sind konsistente Antworten einer vorhandenen positiven Quelle. Für unbeschränkte Generatoren wären zusätzliche gemeinsame Definitionsbereichs- und Fortsetzungsbedingungen nötig; sie werden hier nicht behauptet.

## 2. Konkrete Anwendung auf die originalen TFPT-Familienpfeile

Verwendet werden die bereits quellengeprüften ganzzahligen R- und Q-Matrizen:

\[
R=\begin{pmatrix}1&3&0\\1&5&2\\2&5&3\end{pmatrix},\quad
Q=\begin{pmatrix}3&1&0\\3&2&0\\3&2&1\end{pmatrix},\quad
L=R+Q\operatorname{diag}(1,-1,-1)+Q.
\]

Für diese endliche Demonstration werden ausdrücklich die euklidische positive Metrik und Ω=e_3 gewählt. Das ist keine neue Herleitung der physikalischen TFPT-Zustandswahl. Der Wortträger V=(Ω,RΩ,R²Ω) hat det V=−12 und det G=144. Für R,L,R†,L† verschwinden die vier Restmatrizen exakt. Der Test rekonstruiert beide ursprünglichen Pfeile und ihre Adjunkte in derselben positiven Wortbasis.

Mit nur V_2=(Ω,RΩ) ist dagegen

\[
R_R=\begin{pmatrix}0&0\\0&36\end{pmatrix}.
\]

Die dritte Richtung ist damit direkt aus der Quellenantwort nachweisbar. Diese Rechnung führt einen gemeinsamen endlichdimensionalen Familienabschluss vor; sie leitet weder die vollständige Seam, noch E₈-Feldoperatoren, Gravitation oder eine ursprüngliche 3+1D-Wirkung daraus ab. Weil det V=−12 keine Einheit ist, darf die Wortbasis auch nicht als unveränderte originale integrale Markierung ausgegeben werden.

## 3. Warum endlich viele Treffer ohne Abschlusszertifikat nicht genügen

Für jede Entfernung d≥1 betrachte auf C^(d+1) die verbundenen Jacobi-Matrizen

\[
H_\lambda=3I+\sum_{j=0}^{d-1}(|j\rangle\langle j+1|+|j+1\rangle\langle j|)
+\lambda|d\rangle\langle d|,\qquad \lambda=0,1,
\]

mit Ω=|0⟩. Beide sind strikt positiv. Ihr Graph ist verbunden und Ω ist zyklisch: Die Krylov-Matrix (Ω,HΩ,…,H^dΩ) ist dreieckig mit Diagonale 1.

Ein geschlossener Weg vom Ursprung, der den veränderten Diagonaleintrag am Ende verwendet, benötigt mindestens d Schritte hin, einen Aufenthalt und d Schritte zurück. Daher

\[
\langle\Omega,H_0^k\Omega\rangle=\langle\Omega,H_1^k\Omega\rangle
\quad(0\le k\le2d),
\]

aber die Differenz beim Moment 2d+1 ist exakt 1. Dies ist kein Beispiel eines unsichtbar angehängten Zuschauers: Beide Quellen sind vollständig zyklisch und minimal. Bei d=14 stimmen sogar 28 nichttriviale Momente überein; das 29. unterscheidet sie. Die Zahl dient nur der Veranschaulichung und identifiziert TFPTs 27 unterschiedlichen Vorhersagekarten ausdrücklich nicht mit diesen Momenten.

Die Alternative ist ein tatsächliches Abschlusszertifikat: Ist G_r=(m_(i+j))_(0≤i,j<r)>0 und b=(m_r,…,m_(2r−1)) mit m_(2r)−b†G_r⁻¹b=0, so hat der Vektor H^rΩ−Σ_i(G_r⁻¹b)_i H^iΩ die Norm null. Daraus folgen die vollständige Rekursion und die r-dimensionale zyklische Rekonstruktion. Das ist mehr Information als eine Liste übereinstimmender Momente.

## 4. Konsequenz für den P-versus-NP-Vorschlag

Für den schon diskutierten SAT-Projektor Π unter Gleichverteilung gilt p=#SAT/2^n, Π²=Π. Seine skalare Antwort ist von Rang höchstens zwei, denn m_0=1 und m_k=p für k≥1. Beim Wortträger (Ω,ΠΩ) ist

\[
G_p=\begin{pmatrix}1&p\\p&p\end{pmatrix},\qquad
\det G_p=p(1-p).
\]

Für 0<p<1 gilt λ_max(G_p)≥1 und λ_min(G_p)≤p, also κ(G_p)≥1/p. Schon eine einzige erfüllende Belegung ergibt eine Konditionierung von mindestens 2^n. Ein universeller endlicher Rekonstruktionssatz liefert deshalb noch keinen uniform schnellen Weg zu seinen Eingangsdaten.

Konkrete Zugriffsgrenze: Im Modell unabhängiger klassischer Proben des binären Π-Ergebnisses beträgt der totale Variationsabstand zwischen p=0 und p=2⁻ⁿ nach M Proben genau 1−(1−2⁻ⁿ)^M≤M2⁻ⁿ. Konstante Unterscheidungsgüte erfordert dort Ω(2^n) Proben. Dies ist eine Grenze dieses Probenzugsriffs, kein unterer Komplexitätssatz für allgemeine SAT-Algorithmen und keine Aussage gegen P=NP. Exakte symbolische Momente oder andere Zugriffe sind eine andere, gesondert nachzuweisende Ressource.

## 5. Praktischer nächster Einsatz

Das Prüfverfahren fragt nun konkret: Welche original erzeugten Mischantworten zwischen Familienpfeilen, geladenen Seam-Operatoren und Zeitentwicklung schließen einen gemeinsamen Raum? Fehlende Richtungen können gezielt ergänzt werden. Ein durch gewünschte Massen rückwärts definierter Zustand erfüllt diese Herkunftspflicht nicht. Im RH-Zweig müsste die Positivität der ursprünglichen arithmetischen Form zuerst bewiesen werden; sie darf nicht als Eingang dieses Verfahrens vorausgesetzt werden. Im Faktor- und SAT-Zweig gehören die Kosten der Eingangsdaten und des Ausgangslesers ausdrücklich zum Ergebnis.

`check.py` führt 117 exakte, endliche Kontrollen zu diesen Formeln aus. Sie ersetzen die obigen allgemeinen Argumente nicht und enthalten keine empirische TFPT-Bewertung.
