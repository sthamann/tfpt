# v1.6.9: Bosonzahlkontrolle ersetzt den zusätzlichen Einzelmodenimpuls

## Ergebnis und genaue Verbesserung

Der kausale Dreizustandsversuch benötigt keinen separat gewährten Impuls
auf Fermionmode 4. Die globale Bosonzahlphase

\[
Z_b=e^{i\pi N_b}
\]

aus dem bereits dokumentierten Kontrolltyp Nb genügt für einen exakten,
nichtnachselektierten Eingriffseffekt auf die spätere Besetzung n5.
Der Tensor, das freie H, der N=2-Startzustand und der Dreizustandsraum
bleiben dieselben wie in v1.6.8.

Die Verbesserung ist algebraisch streng: Der alte Impuls Z4 liegt außerhalb
der auf diesem Raum von X und Nb erzeugten Algebra. Der neue Impuls liegt
innerhalb. Ein zusätzlicher Modenselektor wird damit eingespart.
**Das beweist noch keine vom Compiler bereitgestellte Schaltbarkeit.**
Der Unterschied zwischen fixem H und unabhängig steuerbarem X/Nb bleibt
ausdrücklich bestehen.

Ein ergänzendes Instrument zeichnet nur Paar- gegenüber Bosonzweig auf.
Es erhält die Kohärenz zwischen allen Fermionenpaaren und den vollständigen
gemeinsamen Zustand einschließlich Zeiger. Beim Weglassen des Zeigers
ändert sich die Systemkohärenz zwischen Paar und Boson; die daraus folgende
Empfängerwirkung ist exakt die Hälfte des Phasenimpulseffekts. Die Konstruktion
enthält einen wirklichen Zeigerkoppler und ist keine Umbenennung von
Messergebnissen.

## 1. Was ursprünglich dokumentiert ist

Acht Eingaben sind unverändert unter `inputs/` eingefroren.
`inputs_manifest.json` enthält Pfade, Größen und SHA-256. W bleibt
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

Die eingefrorene `operations_commutant.py`, Zeilen 6–18, definiert
das feste Modell H=ΔNb+gX und getrennt den Kontrolltier A={X,Nb}.
Die Datei prüft in Zeilen 389–414 außerdem die Kommutation sämtlicher
60 innerer Generatoren und der Clock mit X und Nb. Die entsprechenden
Focklifts in `native_common.py`, Zeilen 104–219, erhalten die Besetzungszahlen.
Der frühere Quellenbericht `v168_mechanism.md` trennt diese gewährten
Kontrollstufen bereits von einer Herleitung aktiver Geräte aus dem Compiler.
Die großen Kommutantenprogramme wurden hier nicht erneut ausgeführt.

Auf dem exakt selben Raum

\[
\mathcal K_3=\operatorname{span}\{p_0,R_7,b_0\},\qquad p_0=|4,57\rangle,
\quad R_7=\frac1{\sqrt7}\sum_{q=1}^7s_q|p_q\rangle
\]

lauten die Operatoren

\[
X_3=\begin{pmatrix}0&0&-1\\0&0&\sqrt7\\-1&\sqrt7&0\end{pmatrix},
\quad B=N_b|_{\mathcal K_3}=\operatorname{diag}(0,0,1),
\quad H_3=\Delta B+gX_3,
\]
\[
Z_b|_{\mathcal K_3}=I-2B=\operatorname{diag}(1,1,-1),\qquad
E=J^\dagger n_5J=\operatorname{diag}(0,1/7,0).
\]

Die Formeln I−2Nb und die zwei Besetzungsprojektoren unten gelten auf N=2.
Auf dem ganzen Boson-Fockraum ist Zb die Parität exp(iπNb); außerhalb N=2
ist I−2Nb nicht dieselbe Operation.

Der dunkle Projektor ist \(P_D=I-X_3^2/8\). Die Algebra von X3 und B ist
exakt \(\mathbb C P_D\oplus M_2\), komplexe Dimension fünf. Eine Basis ist
I, B, X3, i[B,X3], X3²; ihre Multiplikationsschließung wurde geprüft.
Alle ihre Elemente kommutieren mit PD. Für den alten
\(Z_4=\operatorname{diag}(-1,1,1)\) gilt dagegen [Z4,PD]≠0.
Es wird folglich tatsächlich ein bisher unabhängiger Operatortyp entfernt.
Die neue Kontrollklasse erzeugt aber nicht die volle M3-Algebra.

## 2. Exakter unbedingter Eingriff

Setze

\[
\Omega=\sqrt{\Delta^2/4+8g^2},\qquad
\tau=\frac\pi{2\Omega},\qquad d=\frac\Delta{2\Omega},\qquad
U=e^{-i\tau H_3}.
\]

Beide Arme starten im gleichen Produktzustand p0, alle Bosonen leer:

\[
\text{frei: }U\,I\,U|p_0\rangle,
\qquad\text{Eingriff: }U\,Z_b\,U|p_0\rangle.
\]

Anschließend wird n5 unbedingt ausgelesen. Zb wirkt auf die bosonische
Algebra; n5 auf eine Fermionmode. Sie kommutieren auf der ganzen ursprünglichen
Fock-Algebra. Unmittelbar beim Impuls bleibt die Empfängerstatistik für
jeden Zustand unverändert. Die Entwicklung nach dem Impuls erzeugt

\[
p_{\rm frei}(n_5=1)=\frac{1+\cos(\pi d)}{32},
\]
\[
p_{Z_b}(n_5=1)=
\frac{1+(1-2d^2)^2-2(1-2d^2)\cos(\pi d)}{64},
\]
\[
\boxed{\delta_{b\to5}=
-\frac{(1-d^2)\left[d^2+\cos(\pi d)\right]}{16}}.
\]

Dies ist ein kausaler Vergleich von Eingriff und Nicht-Eingriff auf derselben
Quelle. Keine Ergebnisbedingung und keine Zweipunktkorrelation ersetzt den
Vergleich. Ein Zb direkt auf dem anfänglichen Zustand p0 hätte keinen Effekt;
die native Vorentwicklung ist deshalb ein wesentlicher Teil des Versuchs.

### Strikter endlicher Nachweis

Für Δ>0 und 0<g²≤5Δ²/128 gilt 2/3≤d<1. Aus
\(\cos x\ge1-x^2/2\) und \(\pi<22/7\) folgt

\[
d^2+\cos\pi d
\le -(1-d)\left[1+d-\frac{\pi^2}{2}(1-d)\right]<0.
\]

Denn die eckige Klammer ist größer als (291d−193)/49 und damit
mindestens 1/49. Also ist δb→5 in diesem ganzen Parameterintervall strikt
positiv. Außerhalb gilt die exakte Formel weiterhin, aber nicht dieselbe
Vorzeichenaussage.

Am Prüfpunkt Δ=1, g=1/20 sind τ≈3.02299894039036 und d=5/(3√3):

| Größe | Wert |
|---|---:|
| n5 ohne Impuls | 0.0002194998817122665 |
| n5 mit Bosonphase | 0.0005299169088385700 |
| Unbedingte Differenz | +0.0003104170271263035 |
| Endwert Nb ohne Impuls | 0 exakt |
| Endwert Nb mit Impuls | 25/729 exakt |

Im Gegensatz zum alten Z4-Protokoll haben die beiden Endzustände also
verschiedene Zusammensetzungen. Der neue Test beweist eine kausal beeinflusste
Fermionbesetzung; er beansprucht keine in beiden Armen bosonfreie
Paarumverteilung am Endpunkt. Nb ist ein globaler bosonischer Kontrolltyp,
kein aus dem Compiler abgeleiteter räumlich lokaler Sender.

## 3. Schaltbarkeit und Arbeit werden mitgerechnet

Es gilt

\[
Z_bH_3Z_b=\Delta B-gX_3,\qquad[Z_b,H_3]\ne0\quad(g\ne0).
\]

Jedes Wort ausschließlich aus dem fixen H bzw. seinen freien Entwicklungen
kommutiert dagegen mit H. Deshalb kann Zb nicht als zustandsunabhängiges
Wartewort des unverändert laufenden H ausgegeben werden.

Eine konkrete **bedingte** finite Umsetzung im unabhängig schaltbaren Tier
{X,Nb} ist: Beide Arme entwickeln zunächst τ mit H; für dieselbe Dauer
T_p=π/Δ wird die Paarwechselwirkung pausiert. Im Referenzarm ist zusätzlich
der Nb-Term pausiert, also H_ref=0. Im Impulsarm läuft H_ctrl=ΔNb.
Danach folgt in beiden Armen erneut τ mit H. Die Gesamtdauer ist identisch,
und die mittleren Entwicklungen sind exakt I bzw. Zb. Das verlangt
entsprechende Nullstellungen oder Kompensationen beider Kontrollkoeffizienten.
Eine Quelle, die lediglich das feste H liefert, hat diese Möglichkeit noch
nicht geliefert. Eine idealisierte Instantanphase ohne diese Erläuterung
würde die Kontrollressource verstecken.

Auch die Energieänderung ist nicht null. Der Ausgangszustand und seine
freie Vorentwicklung haben Erwartungsenergie null. Der Impuls deponiert

\[
\Delta E_{\rm Phase}=\frac\Delta4(1-d^2)
=\frac\Delta{54}\quad\text{bei }g/\Delta=1/20.
\]

Die Kontrolle muss diese Arbeit bereitstellen. Ladungserhaltung ersetzt
keine Energiebilanz des Steuerapparats.

## 4. Ein echtes, die Paarkohärenz erhaltendes Aufzeichnungsinstrument

Man gewähre einen zweistufigen, ladungs- und G-trivialen Zeiger im Zustand
|0⟩R sowie einen schaltbaren gemeinsamen Koppler. Die Isometrie

\[
\boxed{V_{\rm rec}\psi=(I-B)\psi\otimes|0\rangle_R
+B\psi\otimes|1\rangle_R}
\]

bleibt in \(\mathcal K_3\otimes\mathbb C^2\), Dimension sechs. Sie ist die
Einschränkung des vollständigen unitären Kopplers

\[
C_R=(I-B)\otimes I+B\otimes X_R
=\exp\!\left[-\frac{i\pi}{2}B\otimes(I-X_R)\right].
\]

Bei fortgesetzter Definition mit dem ganzzahligen Nb auf dem gesamten
Fockraum zeichnet dieser Koppler Bosonparität auf; im vorliegenden N=2-Raum
ist diese identisch mit Nb=0 oder 1. Die gemeinsame Kopplung erhält N und
die innere Gruppe, ist aber als Zeigerkopplung eine **zusätzliche Ressource**.
Aus der Verfügbarkeit eines CP-Phasenkanals folgt nicht automatisch dessen
kohärent kontrollierte Umsetzung. Bei einer endlichen Messzeit müssen die
freie Entwicklung und der Vergleichsarm ebenso kontrolliert werden wie
beim Phasenpuls; hier wird die angegebene Isometrie als Instrument gewährt.

Alle Fermionenpaare erhalten dasselbe Zeigerlabel 0. Ihre Amplituden und
Interferenzen werden nicht einzeln aufgezeichnet. Es gilt
Vrec†Vrec=I3: Die Abbildung erhält sämtliche gemeinsamen Skalarprodukte.
Das bedeutet keine Gleichheit der zukünftigen reduzierten Systemstatistik
mit dem Prozess ohne Recorder. Der Recorder und sein Zeiger sind ein
anderer, vollständig mitgerechneter Prozess.

Wenn der Zeiger ignoriert wird, lautet der **wirkliche Zustandsupdate**

\[
\mathcal D_B(\rho)=(I-B)\rho(I-B)+B\rho B
=\frac12(\rho+Z_b\rho Z_b).
\]

Der Gesamtprozess ist CPTP. Er hat auf den Empfänger unmittelbar keinen
Effekt, da beide Krausoperatoren mit n5 kommutieren. Die Paar-Boson-Kohärenz
des isolierten Systems geht dabei verloren; die Kohärenz im Paarblock
bleibt erhalten. Dies ist eine gezielt gebaute grobe Lüders-Messung, kein
feines Paarlabelinstrument mit anschließend umbenannten Ausgängen.

Wird der Recorder am selben mittleren Zeitpunkt eingesetzt und der Zeiger
bei der abschließenden n5-Statistik nicht ausgewählt, ergibt sich exakt

\[
p_{\rm rec}=\frac12(p_{\rm frei}+p_{Z_b}),\qquad
\boxed{\delta_{\rm rec}=\frac12\delta_{b\to5}}.
\]

Am Prüfpunkt beträgt die Differenz +0.0001552085135631517. Jeder Zeigerzweig
und sein Gewicht wird mitgeführt; es gibt keine Postselektion. Die
Aufzeichnung deponiert im System die Energie Δ(1−d²)/8=Δ/108. Ein anfänglich
bereiter, ladungsneutraler Zeiger ist daher keine kostenlose Energiequelle.

Allgemeiner multiplizieren Zeigerzustände mit reellem Überlapp η zwischen
0 und 1 die reduzierte Paar-Boson-Kohärenz mit η. Die Empfängerwirkung wird
\((1-\eta)\delta_{b\to5}/2\). Vollständig gleiche Zeigerzustände (η=1)
bewahren diese Kohärenz, enthalten aber keine Information über die
Zusammensetzung. Perfekt unterscheidbare Zustände (η=0) liefern den gerade
berechneten Recorder. Die Informations-/Rückwirkungsgrenze bleibt sichtbar.

Die terminale n5-Messung besitzt weiterhin die v1.6.8-Instrumentengrenze:
Ihr Effekt ist exakt auf K3 komprimierbar, ihre Zustandsrückwirkung erhält
K3 nicht. Eine Wiederverwendung nach dieser Endmessung wird nicht behauptet.
Der hier neue Nb-Recorder selbst bleibt dagegen einschließlich Zeiger im
angegebenen sechs-dimensionalen Raum.

## 5. Warum reine innere Symmetrieimpulse diese Rolle nicht übernehmen

Sei V ein tatsächlicher innerer Gruppenimpuls. Dann [V,H]=0. Wenn sein
Senderbereich anfangs mit einem Empfängeroperator O kommutiert, gilt

\[
[V,O]=0\quad\Longrightarrow\quad
[V,O(t)]=[V,e^{itH}Oe^{-itH}]=0
\]

für alle Zeiten. Folglich ist die unbedingte Empfängeränderung exakt null,
für jeden Anfangszustand. Derselbe Schluss gilt für einen spurtreuen
Krausprozess, dessen sämtliche Krausoperatoren diese beiden
Kommutationsbedingungen erfüllen. Das ist kein Schluss nur aus einer
verschwindenden linearen Antwort auf einem einzelnen Zustand.

Die Voraussetzung ist Operator-Kommutation. Wenn V den Empfänger bereits
direkt umzeichnet, oder nur zufällig sein Anfangserwartungswert gleich bleibt,
folgt dieser Satz nicht. Ein solcher direkter Zugriff wäre aber kein
verzögertes Signal zwischen zuerst kommutierenden Operationsbereichen.

Zb ist **G-invariant**, aber kein solcher **G-Impuls**: Es kommutiert mit
der Gruppenwirkung, jedoch nicht mit H. Es greift in die zwei Vorkommen
desselben inneren Typs ein, nämlich Paar und Boson. Genau dieser Unterschied
zwischen einer inneren Gruppenaktion und einer invarianten Operation auf
den Multiplizitäten trägt den neuen Versuch.

## 6. Verifikation und verbleibender Herkunftsschritt

Für den parallelen Quellvergleich ist zusätzlich ein dimensionsunabhängiger
kleiner Blocksatz geprüft: Bei
\(H_C=\left(\begin{smallmatrix}0&gC^\dagger\\gC&\Delta I\end{smallmatrix}\right)\)
und einem normierten Eingang v auf der Bosonseite ist die erste und dritte
Ableitung der Boson-Überlebenswahrscheinlichkeit null, während
\(p''_{N_b}(0)=-2g^2\langle v,CC^\dagger v\rangle\).
Somit gilt \(p_{N_b}(t)=1-g^2\langle CC^\dagger\rangle t^2+O(t^4)\).
Dieser reine Blocksatz verbindet dieselbe Nb-Auslese mit einem
Kopplungs-Gramoperator; er leitet die Eingangspräparation oder die präzise
Schätzung der Anfangskrümmung nicht her.

`verify_protocol.py` prüft Eingabepins, W und den identischen nativen Adapter,
die fünfdimensionale Kontrollalgebra, beide Phasenwahrscheinlichkeiten,
die Vorzeichenregion, Energieänderungen, das echte Zeigerinstrument und
die allgemeine Kommutatorinduktion. Ein unabhängiger Matrixexponential-Replay
bestätigt den dreidimensionalen Phasenversuch und den sechs-dimensionalen
Aufzeichnungsprozess. Normal und `-OO` werden mit expliziten Guards und
Warnungen als Fehler ausgeführt. Zahlen und vollständige Prüfbedingungen
stehen in `protocol_normal.json` und `protocol_optimized.json`.
Die abschließenden Läufe enthalten **92 exakte und vier numerische
Prüfbedingungen**. Sie sind byte-identisch; der optimierte Lauf wurde
zusätzlich aus einem fremden Arbeitsverzeichnis gestartet. Beide
Ergebnisdateien besitzen SHA-256
`5f6dbae2f5a62204cf5a03971389e301268678f3b52268e40c609d32b93141ae`.

**Erreicht:** Ein zuvor separat nötiger Fermionmodenimpuls wird durch den
bereits dokumentierten Kontrolltyp Nb ersetzt. Ein kleiner gemeinsamer
Recorder bewahrt die relevante Paarkohärenz und liefert einen eigenen
unbedingten kausalen Effekt mit vollständiger Ladungs- und Arbeitsangabe.

**Weiter offen:** Compilerseitige Schaltbarkeit von X/Nb, ursprüngliche
Präparation von p0, kalibrierter n5-Detektor, bereitgestellter Zeiger,
sein kohärenter Koppler und die Quelle der Steuerarbeit. Das konkrete
Ergebnis reduziert die Zahl unabhängiger Operatortypen; es macht daraus
noch keinen autonomen Universumsprozess und keine räumliche Welt.
