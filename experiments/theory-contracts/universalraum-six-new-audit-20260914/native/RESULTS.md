# Lokale Ladungen erlauben quelleneigenen Transport mit expliziter Gegenbilanz

14. September 2026. Eigenständige Fortsetzung der nativen Quellenfront.
Experiments only; kein T1–T8-Abschluss, kein Commit und keine Promotion.

## Die neue konkrete Brücke

**Die bereits postulierte Wedge-Quelle transportiert Vermittler über benachbarte
Kanten, während sämtliche lokalen Qv exakt erhalten bleiben. Der vorhandene
Monomer übernimmt die Gegenbilanz.** Dafür braucht die Quelle keinen zusätzlich
eingesetzten nackten Vermittlerhoppingterm. Auf drei Sites und vier Farben ist
der vollständige entsprechende Raum 112-dimensional; der kohärente
Rekopplungsblock hat exakt Rang 24, mit quadrierten Singulärwerten 1 (20-mal)
und 4 (4-mal).

Daneben bewegt der aus derselben Quelle abgeleitete führende niederenergetische
Austausch Farbzustände, ohne die Ortsladungen überhaupt zu verändern. Lokale
Qv-Erhaltung erzwingt daher **keinen Stillstand zwischen Zellen**. Sie untersagt
nur Transporte, deren lokale Ladungsänderung nicht kompensiert wird.

Dies beweist Transport aus dem vorhandenen, **postulierten** Wedge-Hamiltonoperator.
Es leitet dessen Herkunft aus P1/P2 und eine bestimmte skalierende
Zwischenzellgeometrie nicht ab. Auch der selektive kritische Zelltransfer aus
v1.5 ist damit noch nicht als native effektive Dynamik hergeleitet.

## 1. Quelleneigener Monomer-Dimer-Schritt, ohne neuen Generator

Nehme die zwei vorhandenen Quellenkanten e=01 und f=12. Die vierfarbigen
Paarabbauoperatoren sind, in der im Prüfer erklärten CAR-Reihenfolge,

\[
K_{ij}^{ab}=f_{j,b}f_{i,a}-f_{j,a}f_{i,b},\quad a<b,
\qquad
H=\Delta\sum_{e,a<b}n_{e}^{ab}
+t\sum_{e,a<b}(b_e^{ab\dagger}K_e^{ab}+\mathrm{h.c.}).
\]

Die getrennten lokalen Ladungen lauten

\[
Q_v=n_f(v)+\sum_{e\ni v,a<b}n_e^{ab}.
\]

Im Sektor Q0=Q1=Q2=1 liegen 64 reine Materiezustände und 2×6×4=48
Vermittler-plus-Monomerzustände. Mehr als ein Vermittler ist auf diesem Pfad
wegen des gemeinsamen Mittelpunkts unmöglich. In dieser vollständigen Basis ist

\[
H=\begin{pmatrix}0&tB^\dagger\\tB&\Delta I_{48}\end{pmatrix},
\qquad B=\begin{pmatrix}B_{01}\\ B_{12}\end{pmatrix}.
\]

Jeder der zwei einzelnen B-Blöcke erfüllt exakt B_e B_e†=2I24. Der Kreuzblock

\[
C=B_{12}B_{01}^\dagger
\]

ist **nicht null**, sondern hat Rang 24. Ein konkreter Eingang ergibt

\[
C\,|b_{01}^{01}; f_2^2\rangle
=-|f_0^1;b_{12}^{02}\rangle+|f_0^0;b_{12}^{12}\rangle.
\]

Die beiden Ausgänge sind kohärent, einschließlich ihrer CAR-Vorzeichen.
Der Vermittler zieht von Kante 01 nach 12. Seine lokale Ladungsänderung ist
(-1,0,+1); der Monomer zieht von Site 2 nach Site 0 und trägt (+1,0,-1).
Der Zwischenzustand besitzt drei Monomere und keinen Vermittler. **Die
Bilanzressource ist bereits Bestandteil der Quellenbasis.**

Das ist kein nur nachträglich entworfener effektiver Term: Der volle
zeitunabhängige Hamiltonoperator erfüllt exakt

\[
P_{12}H^2P_{01}=t^2 C,
\qquad
P_{12}e^{-iH\tau/\hbar}P_{01}
=-\frac{t^2\tau^2}{2\hbar^2}C+O(\tau^3).
\]

Also existiert für hinreichend kleine nichtverschwindende Zeit eine
Transportamplitude. Bei t/Δ=1/20 und τ=ℏ/Δ beträgt für den obigen Eingang die
numerisch neu gerechnete Wahrscheinlichkeit eines Vermittlers auf 12
**2.9507179393021938×10⁻⁶**. Entfernen der Quellenkante 12 liefert exakt null.
Die Zahl ist eine endliche Demonstration; der Beweis der Nichtnullamplitude
liegt im ganzzahligen H²-Block.

Eliminiert man für E≠0 die Materiekomponente, erhält man ohne asymptotische
Ersetzung den energieabhängigen Vermittleroperator

\[
H_{\mathrm{med}}(E)=\Delta I+(t^2/E)BB^\dagger.
\]

Nahe der Einvermittlerenergie E≈Δ besitzt der Transfer daher den führenden
Koeffizienten t²/Δ. Er hängt aber von Monomerbelegung und Farbrekopplung ab.
**Er ist kein frei wählbares, rein quadratisches η b_f†b_e.**

Die 24 aktiven Kanäle zerfallen in die SU(4)-Dimensionen 20 und 4. Der Prüfer
benötigt dafür keine angenommene Darstellungstabelle: Er berechnet aus der
ganzzahligen CAR-Matrix exakt spec(C†C)={1²⁰,4⁴}. Diese volle Rangkontrolle
verhindert, dass die Brücke nur einem handverlesenen Farbzustand gilt.

## 2. Was daraus für Zwischenzellkopplung folgt

Sind 01 und 12 tatsächliche Quellenkanten über eine Zellgrenze, funktioniert
derselbe Schritt dort. Ein neues Transportfeld ist nicht erforderlich. Sind
alle Quellenkanten ausschließlich innerhalb getrennter Zellen vorhanden,
faktorisiert der Hamiltonoperator entsprechend; der obige Transport erzeugt
keine fehlende Zwischenzellkante. Die **Existenz und Anordnung dieser Kanten**
bleibt die zusätzliche geometrische Voraussetzung.

Schon im Nullvermittlerraum ergibt dieselbe Rechnung exakt

\[
B^\dagger B=2I-S_{01}-S_{12},
\quad
H^{(2)}_\mathrm{low}=-(t^2/\Delta)B^\dagger B
=(t^2/\Delta)(S_{01}+S_{12}-2I).
\]

Dies ist der vorhandene SU(4)-Superaustausch; mit J=2t²/Δ ist die
Farbhoppingamplitude J/2. Beispielsweise ist das Matrixelement von
|1,0,0⟩ nach |0,1,0⟩ genau t²/Δ. Alle drei Ortsladungen bleiben eins.
Der Ausdruck ist die führende Reduktion, kein behaupteter exakter
allordentlicher niederenergetischer Hamiltonoperator.

Für die in v1.5 eingesetzte statische Vermittlermatrix h=ΔI−ηA ist deshalb
zu unterscheiden: Als eigenständiges angenommenes Modell kann ihre
Positivität/Reichweitenschranke korrekt sein. Auf Vermittlern verschiedener
Endpunktladungen widerspricht ein nacktes b_f†b_e jedoch den konservierten Qv.
Der native Ersatz enthält die Materiebilanz und Farbmatrix C. Die frühere
skalare Hoppingform darf nicht ohne diese zusätzliche Herleitung als dieselbe
Quelle bezeichnet werden.

Die Recordkonstruktion verwendet weiterhin genau die einzelne Wedge-Kante.
Die Belegungsabfrage Q_occ verändert keine Qv, ebenso wenig die vorhandenen
Detuningphasen. **Record und Bewegung sind somit algebraisch verträglich.**
Um den bedingten exakten v1.5-Record während einer Mehrzellrechnung tatsächlich
auszuführen, braucht man aber weiterhin das dort erklärte Adressieren und
Abschalten störender Kanten, die Pointer und deren Zeitsteuerung. Die aktuelle
Rechnung entfernt diese Controllerressource nicht.

## 3. Nichtdiagonale Moden und Termaufhebungen: der präzise Architektursatz

Voraussetzungen: selbstadjungierte additive Ladungen
Q_v=n_f(v)+b†q_v b auf dem vollständigen Quellenraum und ein linearer
Erzeugungsvertex V=Σ_e b†C_e K_e+h.c.; dabei sind die K_e unabhängige
Paarabbauoperatoren mit Endpunktgewicht a_e(v)=δvi+δvj. C_e darf beliebige
komplexe Modenmischung enthalten; q_v muss in der gewählten Basis nicht
diagonal sein.

Aus [Q_v,V]=0 folgt

\[
(q_v-a_e(v)I)C_e=0\quad\text{für jedes e,v}.
\]

Warum keine versteckte Termaufhebung? Die bosonischen Erzeugungs- und
Vernichtungsgrade sind getrennt. Die K_e sind als Operatoren unabhängig,
etwa durch Test auf Eingängen, die nur an den betreffenden Endpunkten
Materie tragen. Innerhalb eines Kanten-/Farbkanals zusammengehörige Beiträge
müssen zuerst zu C_e zusammengefasst werden. Aufhebungen können so einen
effektiven Kanal entfernen; sie können keinen verbleibenden Kanal mit
falschem Ladungsgewicht erzeugen. Ein lediglich auf Qv=1 komprimierter
Raum genügt für dieses Argument ausdrücklich nicht.

Jeder aktive Vermittlervektor liegt folglich im gemeinsamen Eigenraum zum
Gewicht a_e. Für e≠f gibt es ein v mit a_e(v)≠a_f(v). Selbstadjungiertheit
von q_v ergibt dann

\[
\langle C_e x,C_f y\rangle=0.
\]

Eine nichtdiagonale oder komplexe Basisrotation hebt diese Orthogonalität
nicht auf. Der aktive Einvermittlerraum hat mindestens Dimension
Σ_e rank(C_e), insbesondere 6|E| bei vollständig aktiven vierfarbigen
Wedgekanälen. Dafür wird keine gleichzeitige Diagonalisierbarkeit des
gesamten unbenutzten Modenraums benötigt.

**Genau daraus folgt die Trennung aktiver Kantenladungsräume, nicht schon
die Anzahl primitiver Tensorfaktoren.** Freie unabhängige bosonische
Fockmoden liefern eine entsprechende Fockfaktorisierung als zusätzliche
Darstellungsannahme; ein begrenzter gemeinsamer Speicher mit orthogonalen
Kanten-/Lochzuständen kann denselben aktiven Raum anders realisieren.
Erlaubt man Qv zudem nur als skalare I auf einem bereits ausgewählten
Qv=1-Sektor, kommutiert dort auch eine Drei-Zustandsmatrix mit einem
gemeinsamen Vermittler und zwei Materieeingängen mit allen Qv. Der Prüfer
enthält dieses Gegenbeispiel. **Konservierte Zahlen auf dem Projektionsraum
allein beweisen keine mikroskopische Architektur.**

Der rationale Prüfer rotiert zwei Kantenkanäle mit der nichtdiagonalen Matrix
[[3/5,4/5],[-4/5,3/5]], baut die tatsächlich nichtdiagonalen q_v neu und
prüft alle vollständigen Kommutatoren exakt. Die absichtliche Ersetzung
durch eine einzelne gemeinsam geladene Mode verletzt dagegen Q0.

## 4. Exakte Minimalressource für einen isolierten Vermittlertransport

Der folgende Satz braucht keine diagonale Modenbasis: Für kommutierende
selbstadjungierte Gesamtladungen und [U,Q_v^S+Q_v^R]=0 kann ein
Systemübergang q→q+a nur mit einem Referenzübergang r→r−a auftreten.
Dies folgt direkt durch Projektion auf die gemeinsamen Ladungseigenräume.
Mögliche Termaufhebungen ändern diese Auswahlregel nicht.

Für a≠0 benötigt ein solcher deterministischer Schritt mindestens zwei
verschiedene Referenzladungssektoren. Diese Untergrenze ist erreichbar:

\[
H_\mathrm{bal}=\kappa\bigl(|f\rangle\langle e|
\otimes|0\rangle\langle a|+\mathrm{h.c.}\bigr),
\quad Q_v^R=\operatorname{diag}(0,a_v).
\]

Bei τ=πℏ/(2κ) ist |e,a⟩→−i|f,0⟩ exakt; alle Gesamtladungen bleiben
erhalten. Die Referenz wurde dabei **verändert**. Eine unverändert
zurückgegebene endliche Referenz kann keinen deterministischen nichtnulligen
Systemladungsübertrag kompensieren: Schon die erhaltenen
Ladungserwartungswerte widersprechen dem. Für K aufeinanderfolgende Schritte
mit demselben nichtnulligen a werden mindestens K+1 unterschiedliche
Referenzladungssektoren benötigt, sofern die Systemzustände diese Schritte
überhaupt zulassen. Dies ist kein Verbot von Rücktransport oder neutralen
geschlossenen Zyklen.

Im nativen Drei-Site-Schritt liefert gerade der Monomer diese zwei
Ladungspositionen. Die Zweistufenreferenz beschreibt hier eine bewiesene
Minimalbilanz, **kein zusätzlich notwendiges neues Feld**.

## 5. Reine Vermittler können ebenfalls kollektiv bewegen

Soll Materie völlig unverändert bleiben, verbietet die Qv-Auswahlregel
quadratische Übergänge zwischen verschiedenen Kanten eines einfachen
Graphen. Sie erlaubt aber ladungsneutrale Viererterme, beispielsweise auf
dem tatsächlichen Clebsch-Vierzyklus 0–1–3–2–0:

\[
H_\square=\kappa\bigl(b_{01}^\dagger b_{23}^\dagger
b_{13}b_{02}+\mathrm{h.c.}\bigr).
\]

Jeder Eckpunkt verliert und gewinnt gleichzeitig eine Kantenladung. Zwei
gegenüberliegende Dimere resonieren bei πℏ/(2κ) vollständig auf die
andere Paarung. In dieser Zahl erhaltenden rein bosonischen Polynomklasse
ist Grad vier die kleinste mögliche nichttriviale Bewegung zwischen
verschiedenen Kanten: Grad zwei wäre gerade das verbotene nackte Hopping.
Interne Farbrotationen derselben Kante sind davon nicht ausgeschlossen.

**Hier ist κ ein neuer nicht abgeleiteter Koeffizient.** Der Ringterm
dient als exaktes Gegenbeispiel gegen ein allgemeines Bewegungsverbot.
Der oben bewiesene Monomer-Dimer-Schritt kommt dagegen bereits aus den
vorhandenen zwei Wedgevertices und benötigt diesen zusätzlichen Term nicht.

## Verifikation und verbleibender Anschluss

`checker.py` läuft unabhängig von anderen Forschungsprüfern. **142 explizite
Bedingungen**, normale und `-OO`-Ausführung, bytegleiche
`verification.json` und `verification_optimized.json`. Ganzzahlige/SymPy-
Identitäten und numerische Zeitentwicklung sind im Ergebnis getrennt.
Negativkontrollen: gemeinsame falsch geladene Mode; nacktes Hopping ohne
Bilanz; entfernte empfangende Quellenkante; fehlender Architekturinhalt
skalaren Qv=1-Wissens. Die Quellenhashes der vier neuen Eingabetexte sind
in der JSON gespeichert.

Reproduktion mit `/opt/homebrew/bin/python3 -B checker.py` und zusätzlich
`/opt/homebrew/bin/python3 -B -OO checker.py --output verification_optimized.json`.

Der nächste inhaltliche Anschluss ist jetzt konkret: Für die tatsächlich
gewählten Zwischenzellkanten den gemeinsamen Wedge-Hamiltonoperator auf
die ersten **Zellanregungen** reduzieren und seine festen Transfer-, Dichte-
und Farbkoeffizienten gegen die v1.5-Kritikalitätsbedingungen prüfen. Die
Existenz lokaler Ladungserhaltung steht diesem Versuch nicht entgegen.
Geometriewahl, kritische Koeffizienten, Clock/Reset und P1/P2-Herkunft bleiben
zusätzliche, hier nicht bewiesene Anforderungen.
