# Drei präzise Grenzen der neuen Opus-Quellenauswahl

14. September 2026. Originaltexte und `architecture.py`/`primitives.py` aus
`universalraum-followups-closure-20260914` wurden direkt gelesen. Diese
Beurteilung verändert deren Dateien und die zuvor postulierten Modelle nicht.

## Wurzelraumdimension ist keine räumliche Modenzählung

Die vierfache Abbildung von Kanten-/Farbpaaren auf dieselbe E8-Wurzel kann
korrekt sein. Ebenso gilt dim(gα)=1. Der entscheidende zusätzliche Schritt
im Opus-Prüfer lautet jedoch ausdrücklich **„One root, one mode“**. Er ist
eine Wahl des Einteilchenträgers, keine Konsequenz allein der Wurzelzählung.

Ein explizites Gegenmodell ist die lokalisierte Algebra
g⊗C⁴ mit punktweiser Multiplikation der vier räumlichen Labels. Für
orthogonale Projektoren Pi gilt

\[
[E_\alpha\otimes P_i,E_{-\alpha}\otimes P_j]
=\delta_{ij}H_\alpha\otimes P_i.
\]

Alle vier Eα⊗Pi besitzen dieselbe **interne** Wurzel α, während die interne
Ausgangsalgebra weiter dim(gα)=1 hat. Der Einteilchenträger gα⊗C⁴ enthält
vier räumliche Moden desselben Wurzelfelds. `source_claims.py` prüft diese
Identitäten vollständig in einem konkreten sl2-Wurzelsektor. In der
**erweiterten** Algebra besitzt das Gewicht gegenüber dem globalen Cartan
natürlich Multiplizität vier; das wird nicht mit der internen g verwechselt.

Der äußere Labelraum ist eine explizite Ressource. Das Gegenmodell behauptet
nicht, dass er schon aus TFPT abgeleitet wäre. Es widerlegt aber die
Folgerung „eindimensionaler interner Wurzelraum ⇒ nur eine räumliche Mode“.
Bereits „eine Kopie pro Zelle“ setzt ebenfalls ein äußeres Zelllabel ein.
Warum gerade Zellen und keine Kanten-/Lochlabels den Träger erweitern,
entscheidet die Wurzelraumdimension allein nicht.

**Bedingt korrekt** bleibt: Wird zusätzlich und abschließend genau der
Fockraum über einer einzigen endlichen Adjungierten pro Zelle vorgeschrieben,
existiert dort ein primitiver Modus je Basisgenerator. Dann ist eine
unabhängige Kantenbank eine Trägererweiterung. Der fehlende Satz ist die
Quellenableitung dieser bereits gewählten Fockvorgabe, nicht die Zahl 60.

Das früher hier bewiesene lokale Qv-Kriterium enthält eine andere
Voraussetzung: unabhängig erhaltene Ortsladungen auf dem vollen Quellenraum.
Es erzwingt verschiedene aktive Endpunktladungsräume. Man darf weder
dieses Ladungsmodell noch „Fock nur über g“ nachträglich allein wegen
eines gewünschten Spektrums als alternativlos erklären.

## Fehlende Wurzelsumme ist kein Hard-Core-Beweis

Der Opus-Prüfer bezeichnet α+β∉Φ als „two carriers never share a place:
hard core is exact“. Tatsächlich folgt zunächst nur [Eα,Eβ]=0.
Das ist keine Aussage EαEβ=0 in einer Operatorrepräsentation.

Ein konkretes E8-Paar gleicher D5-Ortskomponente ist
α=(1/2)⁸ und β=(1/2)⁵⊕(−1/2,−1/2,1/2). Beide sind Wurzeln,
α·β=1, α+β ist keine Wurzel und α−β ist eine Wurzel. In der
Adjungierten liefert Jacobi

\[
\operatorname{ad}(E_\alpha)\operatorname{ad}(E_\beta)(E_{-\alpha})
=[E_\beta,H_\alpha]=-E_\beta\ne0.
\]

Das entsprechende A2-Matrixgegenbeispiel E12,E13,E21 wird exakt geprüft:
[E12,E13]=0, aber [E12,[E13,E21]]=−E13. Damit ist der Hard-Core-Schluss
aus bloßer Wurzeladdition ungültig. Ein separat und explizit gesetzter
Hard-Core-Fockvertrag wird dadurch nicht widerlegt.

## Halbe Cartankomponente ist nicht der halbe Gluegenerator

Der tatsächliche Spinor-Gluevektor s=(1/2)⁸ besitzt Normquadrat 2 und
konformes Gewicht h=1. Er trägt bereits halbzahlige **einzelne
Cartankomponenten**. Dies ist nicht der Vektor s/2=(1/4)⁸ mit
Normquadrat 1/2 und h=1/4.

`half_charge_obstruction()` setzt ohne Herleitung voraus, dass der gesuchte
physische Halbladungsoperator einen Vektor g mit 2g=s erfordert. Seine
Kongruenzrechnung betrifft somit den ausdrücklich **halbierten gesamten
Gluegenerator**. Dieser besitzt sogar schon ein nichtganzzahliges
Skalarprodukt 1/2 mit der D5-Wurzel e1+e2 und ist deshalb keine lokale
integer-spin-Erweiterung desselben gewöhnlichen Gitter-Vertexvertrags.
Die enge Obstruktion ist sinnvoll, ihre Gleichsetzung mit jeder
physikalischen Halbladungsverschiebung ist unbelegt.

Für λ∈D5⊕D3 gilt tatsächlich
||s/2+λ||²=1/2+(Σλi)/2+||λ||²∈1/2+Z; das erklärt die
nichtganzzahligen Gewichte der getesteten Kandidaten ohne endliche
Boxenumeration. Es zeigt weder, dass der tatsächliche T2-Ladungsoperator
gerade diese Normierung besitzt, noch dass alle möglichen Intertwiner
durch diese eine Kandidatenklasse erschöpft sind.

**Folge:** Die globale T2-Halbladungsobstruktion ist damit nicht geschlossen.
Umgekehrt ist T2 auch nicht positiv erledigt: Die Abbildung der wirklichen
TFPT-Ladung auf Cartankomponenten, ein natives renormiertes Feld, gemeinsame
Domänen, Adjungierte und Energieabschätzungen bleiben eigene Anforderungen.
Das Spinor-Gluebeispiel widerlegt die ungeprüfte Identifikation
„Halbladung = halbierter Gluegenerator“; es ersetzt diese Anforderungen nicht.

Alle expliziten endlichen Gegenmodelle stehen in `source_claims.py` und
`source_claims.json`; sie benötigen keine fremden Forschungsprüfer.
