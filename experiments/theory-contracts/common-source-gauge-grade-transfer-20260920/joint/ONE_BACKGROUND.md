# Ein Familienhintergrund reicht in der kovarianten Klasse nicht

20. September 2026. Exakter Darstellungssatz unter expliziten Voraussetzungen;
kein Ausschluss der vollständigen TFPT-Quelle.

## Präzise Frage

Kann man die Nullrichtung des vorhandenen Familientensors
\(A(h)_{ij}=\epsilon_{ijk}h_k\) allein durch weitere Korrekturen aus demselben
Higgs-Familienvektor \(h\) und seiner komplexen Konjugierten aufheben?

Betrachtet wird eine beliebige eindeutig definierte Koeffizientenfunktion
\(F:\mathbb C^3\setminus\{0\}\to\operatorname{Mat}_3(\mathbb C)\).
Die beiden Fermion-Familienindizes transformieren fundamental, deshalb
transformiert ihr Koeffizient mit zwei konjugierten Fundamentalindizes.
Wir verlangen

\[
 F(gh)=\bar g F(h)\bar g^T \quad(g\in SU(3)),\qquad
 F(e^{it}h)=e^{it}F(h).
\tag{1}
\]

Die zweite Gleichung ist der Ladungsgrad des zugehörigen Higgs, normiert
auf +1. Sie ist keine zusätzlich aus dem Compiler hergeleitete kontinuierliche
Phasensymmetrie. Sie muss gelten, wenn diese Funktion als der betreffende
eichkovariante Higgs-Koeffizient verwendet werden soll. Die Eichdarstellung
des äußeren Fermionpaares wird dabei festgehalten.

Weitere Familienvektoren, spurionartige Matrixmarkierungen, tensorwertige
Propagatoren mit unabhängiger Orientierung oder ausgewählte Vakuumdaten sind
aus dieser Klasse ausdrücklich ausgeschlossen. Normabhängige skalare
Kopplungen dürfen beliebig sein. Auch komplexe Koeffizienten sind zugelassen.

## Satz und Beweis

Jede Funktion mit (1) hat die Form

\[
 F(h)=f(h^\dagger h)A(h),\qquad F(h)h=0,\qquad\det F(h)=0.
\tag{2}
\]

Analytizität oder eine Störungsentwicklung werden dafür nicht benötigt.

Sei zunächst \(h=r e_3\), \(r>0\). Sein SU(2)-Stabilisator wirkt auf den
ersten beiden Komponenten. Die einzige invariante Zweiform auf dieser
Dublette ist die antisymmetrische Form \(\epsilon_2\); zwischen Dublette
und Singulett existiert kein invarianter Vektor. Somit erzwingt die erste
Gleichung von (1)

\[
 F(r e_3)=\begin{pmatrix}a(r)\epsilon_2&0\\0&b(r)\end{pmatrix}.
\]

Jetzt verwende
\(g_t=\operatorname{diag}(e^{-it/2},e^{-it/2},e^{it})\in SU(3)\).
Es gilt \(g_t r e_3=e^{it}r e_3\). Die SU(3)-Kovarianz multipliziert den
Dublettblock mit \(e^{it}\), den Singulettblock jedoch mit \(e^{-2it}\).
Der Ladungsgrad in (1) verlangt für beide Blöcke den Faktor \(e^{it}\).
Deshalb ist \(b(r)=0\). SU(3) wirkt transitiv auf jeder Sphäre in
\(\mathbb C^3\); mit \(f(r^2)=a(r)/r\) folgt (2) für jedes \(h\neq0\).

Die Konstruktion ist konsistent, weil
\(A(gh)=\bar g A(h)\bar g^T\). Falls F auch bei h=0 kovariant definiert
ist, folgt dort \(F(0)=0\), da \(\bar3\otimes\bar3\) keinen SU(3)-Singulett
enthält.

## Warum der scheinbar passende Rang-eins-Term nicht genügt

\(\bar h\bar h^T\) besitzt die richtige SU(3)-Transformation und kann
algebraisch die Nullrichtung ergänzen. Unter \(h\mapsto e^{it}h\) hat es
jedoch Ladungsgrad -2 statt +1. Eine Multiplikation mit einer skalaren
SU(3)-Invarianten aus nur h und seiner Konjugierten ändert diesen Grad
nicht. Ein zusätzlich gewählter Phasenfaktor mit Grad +3 wäre bereits ein
weiteres Hintergrunddatum und liegt außerhalb der Klasse (1).

Das ist stärker als die rein algebraische Beobachtung \(AFA^T h=0\):
Selbst eine nichtperturbative Koeffizientenfunktion kann innerhalb (1)
die fehlende Masse nicht erzeugen. Umgekehrt behauptet der Satz nicht,
dass jede im anderen Proof untersuchte formale Zweivertexkontraktion
automatisch (1) erfüllt. Beispielsweise muss ein eingesetztes \(\delta_{ij}\)
mit zwei unteren Familienindizes selbst auf seine tatsächliche
Transformation geprüft werden.

## Konsequenz für den gemeinsamen Lösungsweg

Die bereits nachgewiesene interne Markierung S behebt den Austauschtyp
des vollständigen Koeffizienten. Sie wirkt nicht auf die Familienindizes
und hebt den Satz (2) daher nicht auf.

Ein neuer physischer Rang muss aus einem tatsächlich vorhandenen zusätzlichen
Familienkanal oder einem die Klasse (1) verlassenden Quelltensor kommen.
Die vollständige Compilerquelle enthält weitere diskrete Markierungen;
ob und wie sie einen solchen Tensor auswählen, ist offen und hier nicht
negativ entschieden. Ebenso offen bleiben eine zweite unabhängige
Higgs-Familienrichtung und eine reale Komplementkopplung mit beiden
nichtverschwindenden Überlappungen \(h^T b\) und \(c^T h\).

Der Satz verhindert nur, dass eine weitere Korrekturrechnung mit unverändertem
Ein-Hintergrund-Ansatz als Lösung der dritten Familienmasse ausgegeben wird.
Er ist kein Ausschluss von spontaner Symmetriebrechung mit zusätzlichen
Zustandsdaten, nichtlokalen tensorwertigen Quellen, der nativen endlichen
Symmetriegruppe oder der TFPT-Gesamtlösung.
