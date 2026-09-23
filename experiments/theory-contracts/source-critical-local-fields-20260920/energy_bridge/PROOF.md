# Rückbindung der Feldrechnung an den neuesten Quellenstand

Der während dieser Arbeit hinzugekommene Contract
`UR.SOURCE.DYNAMICS_SELECTION.01` untersucht die unveränderte freie
Energie `V0=I` und die zuvor gewählte E8-Energie `V_aux`.
Seine vollständige Beweisnotiz wurde gelesen. Die Schlussfolgerung ist
`PARTIAL`; die dortige Vergleichskurve ist selbst keine hergeleitete
Renormierungsbewegung.

## Erste Identifikation geprüft

Die Vergleichskurve benutzt

\[
v_\theta=(\sinh\theta\,a/\sqrt8,0,\cosh\theta),\qquad
V_\theta=K+2Kv_\theta v_\theta^T K,
\quad 0\le\theta\le\operatorname{arcosh}3.
\]

Am Mittelpunkt gilt `Delta(n)=Delta(z)=2`. Der in unserer Feldrechnung
verwendete Punkt benutzt dagegen

\[
v_c=(n-z)/2=(a/2,-1,2),\qquad
V_c=K+2Kv_cv_c^TK,
\]

und hat `Delta(n)=Delta(z)=1`.

Nicht nur die beiden Mittelpunkte sind verschieden: **Vc liegt überhaupt
nicht auf dieser ganzen direkten Vergleichskurve.** Der kleinste Test ist
ein einziger Eintrag in den ursprünglichen Kanalnummern:

\[
(V_\theta)_{9,10}=0\quad\hbox{für jedes }\theta,
\qquad (V_c)_{9,10}=4.
\]

Die Feldrechnung verlangt also zusätzlich eine andere kollektive
Dichterichtung unter Beteiligung des neunten rechten Kanals. Der Wert 4
ist hier nur der Matrixeintrag in der festgehaltenen Normierung, kein
vorhergesagter physikalischer Kopplungswert.

Der Quellbeweis isoliert `n,z` als die einzigen erlaubten selbstnullen
Operatoren auf seiner Kurve, die marginal oder relevant werden können;
alle übrigen haben dort Dimension mindestens `7/2`. Das ist ein nützlicher
Auswahlfilter für diese Klasse, aber keine Herleitung von `Vc`, gleichen
Cosinus-Amplituden oder eines Ising-Übergangs. Unsere neuen fermionischen
Spinorfelder bleiben deshalb ein präziser **bedingter Zielanschluss**.

## Welche Quelle tatsächlich fehlt

Der neue Contract unterscheidet den unveränderten freien CAR/QWZ-Quellkern
von echten elementaren Wechselwirkungen. Ein Basiswechsel transportiert
die Energie zu `W^T W`; er ersetzt sie nicht durch die gewählte E8-Energie.
Auch nichtverschwindende Kumulanten zusammengesetzter Ströme und eine
Determinantenphase erzeugen allein keinen elementaren Vierfermionterm.
Diese Gaussian-Closure war bereits zuvor bekannt und wird nicht als neue
Entdeckung unserer Arbeit ausgegeben.

Der vorhandene kompakte Rotor-Elternoperator enthält einen echten
nichtgaußschen Kommutator. Sein Feldraum, seine Ladungen, sein Zustand und
seine Zeitentwicklung sind aber noch nicht mit dem hiesigen Rand
identifiziert. Ihn ohne diese Abbildung einzusetzen würde den fehlenden
Ursprung verschieben.

Für die vollständige Lösung ist daher vor jeder weiteren Optimierung der
kritischen Felder zu liefern: **Ein ursprünglicher, nichtgaußscher
Quelloperator mit einer gemeinsamen Abbildung auf Kanalzahl,
Hyperladung, Parität und Zeitentwicklung, aus dem die kollektive
Energie und die konkurrierenden Wechselwirkungen folgen.** Die vorliegenden
Feld- und Clock-Rechnungen bestimmen, was dieser Anschluss erhalten muss;
sie sind selbst noch nicht diese Herkunftsherleitung.
