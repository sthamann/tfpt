# Ursprünglicher Mechanismus, Erhaltung und die kleinste zusätzliche Ressource

## Ergebnis

**Exakt neu:** Am unveränderten Tensor schließt ein zweidimensionaler
G-Singulett-Unterraum mit physischer Ladung N=4 unter dem gesamten nativen H.
Seine Matrix ist

\[
H_{4,\mathrm{klein}}=
\begin{pmatrix}2\Delta&4g\\4g&\Delta\end{pmatrix}.
\]

Der Koeffizient 4 und die Invarianz wurden aus sämtlichen ursprünglichen
Paartermen berechnet. Es handelt sich um einen invarianten Unterraum, keine
abgeschnittene Näherung. Damit liegt ein kleiner ursprünglicher Mechanismus
zwischen zwei verschiedenen Zusammensetzungen desselben Singuletttyps vor.
Seine Vorbereitung aus dem Vakuum ist durch diese Rechnung nicht geliefert.

**Exakt ausgeschlossen:** Kein Wort aus X, Nb und den dokumentierten passiven
Focklifts von Clock und innerer Gruppe kann den Systemsektor N verändern.
Das gilt für beliebige Wortlängen. Die zusätzlichen Terme B+ und R+ aus
v1.6.7 können daher in diesem festen Alphabet nicht durch weitere
Kommutatorsuche gefunden werden.

**Bedingt konstruiert:** Ein zusätzliches Bosonpaarinstrument ist die
einfachste invariant mögliche Erweiterung nach Polynomialgrad. Zusammen
mit einer zweistufigen G-trivialen Referenz entsteht ein exakt geschlossener
Dreizustandsprozess mit voller Spin(10)×SU(4)-Invarianz und Ngesamt=4.
Die Referenz und die gekoppelte Operation sind ausdrücklich neue Ressourcen.
Dieser gemeinsame Prozess implementiert keinen kostenlosen kohärenten
Bosonpaarantrieb auf dem isolierten System.

## 1. Was die tatsächlichen Quellen konstruieren

Alle zwölf verwendeten Eingaben sind unter `inputs/` unverändert eingefroren;
`inputs_manifest.json` enthält ihre ursprünglichen Pfade, Größen und SHA-256.
Das maßgebliche Tensorarchiv besitzt weiter den SHA-256
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

| Quellstelle | Tatsächlich konstruierter Gegenstand | Grenze dieses Anschlusses |
|---|---|---|
| `universalraum-singlet-observable-20260915/sources/native_source.py`, Zeilen 36–67 | Fünf Jordan-Wigner-Hilfsoperatoren, deren 16-dimensionaler gerader Spinorraum, zehn BETA-Matrizen und der Farbkeil ergeben W | Die Hilfs-CAR auf fünf Bits sind keine Ausführung der 64 physischen Fermionoperatoren |
| Dieselbe Datei, Zeilen 87–99 | BAR und ETA aus entgegengesetztem Vektorgewicht und komplementärem Farbpaar | Eine invariante Koeffizientenmatrix ist noch kein Bosonpaarinstrument |
| Dieselbe Datei, Zeilen 101–129 | J und C3 mit JC3=0 sowie JJ†=15I | Ein weiterer E8-Koeffiziententensor ist keine vollständige E8-Operatordarstellung auf dem Fockraum |
| `seam_state_derivation_probe.py`, Helfer ab Zeile 380 und Hauptkonstruktion 486–627 | Markierte endliche Clockpermutation aus der ursprünglichen Duad-/Aut-Konstruktion | Keine Auswahl einer physikalischen Zeiteinheit oder des Hamiltonoperators |
| `native-operations-ground-response-20260915/common.py`, Zeilen 104–170 und 187–219 | 60 innere Lie-Matrizen, ihr Bosonlift und der Clocklift | Die konkreten Lifts erhalten Fermion- und Bosonzahl jeweils; aktive unabhängige Kontrolle bleibt eine weitere Voraussetzung |
| `operations_commutant.py`, Zeilen 6–18 | Ausdrücklich unterschiedene Kontrollstufen: fixes Modell, X/Nb, Clock, Gruppenmatrizen | Die Stufen klassifizieren gewährte Operatoren, nicht deren Compilerverfügbarkeit |
| `compiler-origin-audit-20260913/context_instrument.py`, Zeilen 1–6 und 109 ff. | Instrumente auf dem ursprünglichen vierdimensionalen Kontextträger unter Born-/Wiederholbarkeitsannahmen | Kein gegebener Adapter zu B+, R+ oder der 64f/60b-Bank |
| `compiler-kernel-foundation-20260914/relational_kernel.py`, Zeilen 99–121 | Konkrete geordnete Reflexionswörter und ihr interner Phasenzeuge | Ihre vorhandene C4-Wirkung liefert nicht automatisch einen ladungsändernden Fockgriff |

Die letzten beiden Quellen werden hier zur Typ- und Verfügbarkeitsprüfung
gelesen, nicht erneut als Gesamtprogramme ausgeführt. Die Quellenprüfung ist
auf diese konkret bezeichnete Kette begrenzt; sie ist keine Behauptung, dass
jedes denkbare andere Compilerabbild oder jede Datei des Repositories
ausgeschlossen wurde. Die verfügbaren MCP-Codegraphtools enthielten keine
aufrufbaren Graphsuchfunktionen; deshalb wurde gezielt lokal gelesen.

Der eigene Replay führt die tatsächliche `native_source.py` bis einschließlich
Zeile 220 mit allen 17 dortigen Guards aus. Nur die nachfolgende optionale
Hashbildung des dichten C3-Arrays und der Druckblock entfallen. Der erhaltene
W-Tensor stimmt in jedem Eintrag mit dem gepinnten Archiv überein. Der
ursprüngliche Clockkern wird einschließlich seiner vier mathematischen
S0.1–S0.4-Guards wiederholt; die übrigen numerischen Seam-Proben laufen nicht.
Das ergibt erneut p=(2,0,1,4,3) und den dokumentierten passiven Focklift.

## 2. Geschlossener Erhaltungssatz für das dokumentierte Alphabet

Es gilt auf dem endlichen Besetzungszustandskern

\[
N=N_f+2N_b,\quad
[N,f_i]=-f_i,\quad [N,b_A]=-2b_A.
\]

Mit den unveränderten Definitionen

\[
P_A=\sum_{i<j}W_{A,ij}f_jf_i,\qquad
T_+=\sum_A b_A^\dagger P_A,\quad T_-=T_+^\dagger,
\quad X=T_++T_-
\]

hat jedes der 480 signierten Wechselwirkungsmonome Ladung +2−1−1=0.
Nb, alle Modenbesetzungen und alle passiven Bilineare f†Af beziehungsweise
b†Cb sind ebenfalls neutral. Die dokumentierten inneren Liegeneratoren
werden genau auf diese Weise zweitquantisiert. Die Clock schickt
f† nach GF f† und b† nach GB b†, mischt also keine Erzeuger mit Vernichtern.

Sei A0 die von diesen gewährten Operationen erzeugte *-Algebra. Aus

\[
[N,AB]=[N,A]B+A[N,B]
\]

folgt induktiv

\[
\boxed{\mathcal A_0\subseteq\{N\}'.}
\]

Der Beweis umfasst Produkte, Summen, Adjungierte und Kommutatoren jeder
endlichen Länge. Auf jedem festen N-Sektor sind die betreffenden nativen
Hamiltonoperatoren endlichdimensional; ihre exponentiellen Entwicklungen
und endliche Pulsfolgen erhalten daher ebenfalls diesen Sektor. Es ist
keine numerische Suche nur bis zu einer endlichen Wortlänge.

Für die in v1.6.7 geprüften Kandidaten gilt hingegen

\[
[N,B_+]=4B_+,\qquad [N,R_+]=4R_+.
\]

Ihre Nichtnullwirkung ist direkt sichtbar:

\[
\|B_+|0\rangle\|^2=30,\qquad
\|R_+|0\rangle\|^2=480.
\]

Also gehören B+, R+ und ihre nichttrivialen hermiteschen Quadraturen nicht
zu A0. Ein fixes H bietet nicht mehr Erreichbarkeit als das großzügigere
Alphabet mit X und Nb als unabhängigen Kontrollen. Selbst alle gewährten
inneren Gruppenoperationen beseitigen dieses N-Hindernis nicht.

### Instrumente und die genaue Ancilla-Grenze

Ein Instrument mit Krausoperatoren Kx aus A0 kann aus einem scharfen
N-Sektor keinen anderen erzeugen. Eine spurtreue Summe solcher Zweige erhält
die gesamte Sektorverteilung. Selektive Konditionierung kann die Gewichte
einer bereits vorhandenen Mischung verändern, aber keine neue Sektorstütze
erzeugen.

Dasselbe gilt für einen zusätzlichen Zeiger, dessen Ladungsoperator auf
seinem ganzen Hilbertraum null ist, sofern auch die gemeinsame Kopplung
N erhält. Es gilt ausdrücklich **nicht** für eine beliebige mitgeführte
Ladungsreferenz. Bei deren Ladungswechsel kann die Systemladung wechseln,
während die Gesamtladung unverändert bleibt. Abschnitt 5 gibt dafür einen
expliziten positiven Zeugen. Ein Zeiger, der anfangs Ladung null hat, aber
andere Ladungszustände besitzt, ist nicht mit einem auf dem ganzen Raum
ladungstrivialen Zeiger gleichzusetzen.

## 3. Die kleinste zusätzliche Operation ist schon algebraisch ausreichend

In der ursprünglichen Basis ist

\[
B_+=\frac12 b^\dagger\eta b^\dagger
=\sum_{A<\bar A}\eta_A b_A^\dagger b_{\bar A}^\dagger,
\qquad Q=B_++B_-.
\]

Dabei ist der zweite Bosonindex BAR(A). Es gibt dreißig solche ungeordneten Paare.
Die vollständige Invarianz von η wird an allen 45+15 ursprünglichen
Liegeneratoren geprüft. Die 60 verschiedenen Bosongewichte und der
zusammenhängende Lie-Wirkungsgraph beweisen zusätzlich, dass diese
Paarung bis auf einen Skalar eindeutig ist.

Unter den G-invarianten, fermionparitätsgeraden, normalgeordneten
Polynomen ist Grad zwei der kleinste mögliche Grad einer N-ändernden
Operation: Es gibt kein lineares Bosonsingulett; fermionische Paarterme
haben nichttriviale SU(4)-Zentrumsladung; die verbleibenden Bilineare f†f
und b†b erhalten N. Die minimale Klasse ist daher
κB+ + κ̄B−. Eine Phase, Stärke oder Ausführungszeit wird dadurch nicht gewählt.

Die exakten CCR liefern am gesamten 60-Kanal-Tensor

\[
[T_-,B_+]=R_+,\qquad
[Q,X]=R_--R_+,\qquad
\boxed{R_++R_-=-[N_b,[Q,X]].}
\]

Der ursprünglich zusätzlich vorgeschlagene kubische Quartettkanal braucht
somit keinen zweiten unabhängigen Koeffiziententensor. Ein einziger
zusätzlich gewährter Bosonpaargriff Q reicht algebraisch, sobald X und Nb
separat zugänglich sind. Der Nachweis benutzt exakte Normalordnung auf dem
unendlichen Boson-Fockraum, keine abgeschnittenen Oszillator-CCR.

Das ist eine konkrete minimale **Erweiterung** des Operationsvertrags.
Die Quelle liefert η und W; sie liefert in der geprüften Kette keine
Ausführung von Q. Aus der Kommutatoridentität allein folgt außerdem kein
endliches exaktes Pulswort für exp(−itR). Eine Interpretation als
Kontrollsynthese benötigt schaltbare Vorzeichen/Zeiten und eine bewiesene
Konvergenz samt Fehlerkontrolle. Bereits der statische Zusatz κQ bricht N;
die separate X/Nb-Verfügbarkeit ist nur für die genannte Synthese nötig.

## 4. Ein neuer kleiner ursprünglicher Singulettmechanismus

Definiere am wirklichen Vakuum der 64f/60b-Bank

\[
|\beta\rangle=\frac{B_+|0\rangle}{\sqrt{30}},\qquad
|\rho\rangle=\frac{R_+|0\rangle}{\sqrt{480}}.
\]

Beide Zustände sind volle G-Singuletts und haben N=4. β enthält zwei
Bosonen; ρ enthält einen Boson und zwei Fermionen. Ihre Orthogonalität
folgt schon aus den unterschiedlichen Besetzungszahlen.

Der Schließungsschritt beruht auf der tatsächlichen Fierz-Identität

\[
\sum_{AB}\eta_{AB}P_A^\dagger P_B^\dagger=0.
\]

Der Prüfer enumeriert hierfür **3840 signierte Quellterme auf 960
Fermionquartetts**. Nach vollständiger CAR-Normalordnung bleibt kein
einziger Koeffizient übrig. Zusätzlich wird die gesamte ursprüngliche
Wechselwirkung direkt auf alle 30 Komponenten von B+|0⟩ und alle 480
Komponenten von R+|0⟩ angewendet. Das ergibt genau

\[
\begin{aligned}
T_+B_+|0\rangle&=0,&T_-B_+|0\rangle&=R_+|0\rangle,\\
T_+R_+|0\rangle&=16B_+|0\rangle,&T_-R_+|0\rangle&=0.
\end{aligned}
\]

Es gibt keine ausgelassenen Übergänge. Nach Normierung beträgt die
Kopplung in beiden Richtungen 4g. Deshalb ist span{β,ρ} unter dem ganzen
Hnat invariant und besitzt die eingangs angegebene Zweizustandsmatrix.
Eine Behauptung über die Dimension des gesamten N=4-Singulettsektors ist
für diesen Schluss nicht erforderlich und wird hier nicht erhoben.

Für einen anfangs verfügbaren β-Zustand lautet die Umwandlung

\[
P_{\beta\to\rho}(t)=
\frac{64g^2}{\Delta^2+64g^2}
\sin^2\!\left(\frac{t}{2}\sqrt{\Delta^2+64g^2}\right).
\]

Am ursprünglichen Prüfpunkt g/Δ=1/20 ist ihr Maximum exakt **4/29**.
Das ist Veränderung der Zusammensetzung in einer Bank; die Rechnung
führt keine Orte ein. Dieser N=4-Startzustand ist auch nicht der frühere
N=64-Grundzustand Ω.

Zum Vergleich bleibt der elementare N=2-Kanal
W†|A⟩/√8 ↔ |bA⟩ mit Matrix [[0,√8g],[√8g,Δ]] erhalten. Sein Maximum
beträgt am selben Prüfpunkt 2/27; ein einzelnes ursprüngliches Paar besitzt
nur 1/8 des hellen Gewichts und erreicht 1/108. Auch hier sind Vorbereitung,
Auslesung und Zeitkalibrierung zusätzliche Teile eines ausgeführten
Prozessvertrags.

## 5. Exakter gemeinsamer Dreizustandsprozess mit voller innerer Symmetrie

Man gewähre eine Referenz R mit zwei **G-trivialen** Zuständen |0⟩R und
|4⟩R, deren N_R-Ladungen null beziehungsweise vier sind. Setze

\[
L_-=|0\rangle_R\langle4|,\qquad
V=\kappa(B_+\otimes L_-+B_-\otimes L_-^\dagger),
\]

\[
H_{\rm joint}=H_{\rm nat}\otimes I+
E_R I\otimes|4\rangle_R\langle4|+V.
\]

Für reelle g, κ und ER ist Hjoint auf jedem festen Gesamt-N-Sektor eine
endliche hermitesche Matrix. V erhält Ngesamt und die **ganze** innere
Gruppe: B± sind bereits G-Skalare, die Referenz ist G-trivial. Anders als
ein ausschließlich auf Cartanladungen beruhender Ansatz ist hier kein
ungeprüfter Rest der nichtabelschen Gruppe übrig.

Der gemeinsame Raum

\[
\mathcal K=\operatorname{span}\{
|0\rangle_S|4\rangle_R,
|\beta\rangle_S|0\rangle_R,
|\rho\rangle_S|0\rangle_R\}
\]

hat durchgehend Ngesamt=4 und ist unter Hjoint invariant. Denn B−β=√30|0⟩,
B−ρ=0, L−|0⟩R=0 und die nativen Übergänge sind vollständig in Abschnitt 4
bewiesen. In dieser orthonormalen Basis lautet der **exakte ganze Block**

\[
\boxed{
H_{\rm joint}|_{\mathcal K}=
\begin{pmatrix}
E_R&\sqrt{30}\kappa&0\\
\sqrt{30}\kappa&2\Delta&4g\\
0&4g&\Delta
\end{pmatrix}.}
\]

Die zweite Kopplung ist unverändert aus Hnat abgeleitet. Die erste stammt
aus dem ausdrücklich neuen gemeinsamen Instrument V. Für den Start
|0⟩S|4⟩R ist die Quartettwahrscheinlichkeit bei kleinen Zeiten

\[
P_{\rho,0_R}(t)=120\kappa^2g^2t^4+O(t^6).
\]

Das positive führende Glied ist exakt aus (Hjoint²)31 berechnet; die
Geradheit folgt bei reellen Parametern aus der reellen symmetrischen Matrix.
Es wird weder eine besondere Auswahl der Energie ER noch ein universeller
hoher Übertragungsgrad behauptet.

### Die Referenz verschwindet nicht aus der Rechnung

Ein allgemeiner gemeinsamer Zustand in K hat die Form

\[
a|0,4_R\rangle+b|\beta,0_R\rangle+c|\rho,0_R\rangle.
\]

Nach Ausspuren der Referenz bleibt

\[
\rho_S=|a|^2|0\rangle\langle0|+
(b|\beta\rangle+c|\rho\rangle)
(\bar b\langle\beta|+\bar c\langle\rho|).
\]

Die N=0/N=4-Kohärenzen sind null; die β/ρ-Kohärenz innerhalb N=4 bleibt.
Ein erfolgreicher Ladungseintrag hinterlässt die Referenz bei null statt
vier. Der Prozess implementiert deshalb keinen unveränderten katalytischen
Q-Antrieb des isolierten Systems. Eine zusätzliche kohärente Referenz kann
einen effektiven Antrieb in erster Ordnung liefern; eine beliebige endliche
Referenz ist aber nicht automatisch ein exakter wiederverwendbarer Antrieb.
Ein ergänzender exakter Vierzustandszeuge zeigt beides: Eine scharfe
Ladungsreferenz erzeugt eine inkohärente Populationsänderung; für die
gleichgewichtete kohärente Referenz hat die reduzierte Systemdichte nach
dem gewählten Puls Determinante 1/16 und ist somit gemischt.

### Anschluss an das nachgereichte Forschungspaper

Abschnitt 9 des nachgereichten Papers benutzt dasselbe Prinzip einer
mitgerechneten Ladungsreferenz. Sein dortiger N=9-Vierzustandstransfer
erhält mit der neuen Referenz **eine einzelne innere Cartanladung**.
Unsere Konstruktion betrifft stattdessen N und erhält die vollständige
innere Gruppe, erzeugt aber keine räumliche Übertragung. Sie ersetzt den
dortigen Transferzeugen nicht und beweist dessen native Herkunft nicht.
Das Paper benennt seine Ein-Cartan-Grenze und den Referenzverbrauch selbst
ausdrücklich. Hier wurde nur dieser begrenzte Anschluss gelesen; sein
Gesamtaudit liegt außerhalb dieses Strangs.

## 6. Ressourcenbilanz und der jetzt konkrete nächste Nachweis

| Ressource | Herkunft im geprüften Vertrag | Was noch zu liefern wäre |
|---|---|---|
| W, η, innere Darstellung, endliche Clock | Tatsächliche Quellkonstruktion und erneuter exakter Replay | Physische Identifikation des Trägers |
| Hnat mit Δ,g | Bestehender ausdrücklich festgelegter Modellvertrag | Physische Auswahl und Kalibrierung |
| Zweizustandsblock β↔ρ | Neue vollständige Anwendung aller nativen Terme | Ursprüngliche Vorbereitung von β oder ρ |
| Unabhängige X/Nb-Kontrollen | Gewährte Kontrollstufe, nicht aus fixes H abgeleitet | Instrumente und Schaltvertrag |
| Q oder der gemeinsame Übergang V | Hier genau ausgeschriebene zusätzliche Operation | Compilerwort oder Instrument, das diesen Übergang wirklich erzeugt |
| G-triviale Referenz mit N_R=0,4 | Minimaler zusätzlicher Ladungsspeicher für diese Konstruktion | Träger, Präparation, Energie ER und alle Ressourcenkosten |
| Anfang | Vakuum × scharfe Referenzladung vier | Herkunft dieses Gesamtzustands |
| Ausgang | Gemeinsame Besetzungen und Referenzwechsel | Ausführbare gemeinsame Auslesung, ohne stilles Ausspuren relevanter Information |

Die Minimalität ist präzise begrenzt: Grad zwei ist der kleinste zugelassene
G-invariante paritätsgerade N-ändernde Systemgrad; zwei verschiedene
Referenzladungen sind die kleinste Dimension für den einmaligen scharfen
Ausgleich; die Dreizustandsmatrix ist der kleinste von diesem konkreten
Anfang durch die beiden nichtverschwindenden Kopplungen erzeugte Raum.
Das ist keine globale Minimierung aller möglichen Universen oder Compiler.

**Nächster Herkunftsnachweis:** Ein vorhandener ursprünglicher Quellbaustein
muss einen getypten Adapter zu V einschließlich Referenzzustand und
gemeinsamer Auslesung liefern. Ein Vorschlag allein aus den bereits
N-neutralen Fockwörtern scheitert jetzt am bewiesenen Erhaltungssatz und
braucht keine weitere Wortsuche. Ein anderer getypter Quellbaustein bleibt
eine offene Möglichkeit; bloße E8-Grade oder gleiche Matrizenabmessungen
reichen als Adapter nicht aus.

## 7. Reproduktion und Beweisumfang

Aus diesem Ordner:

```sh
python3 -B -W error verify.py --output results_normal.json
python3 -OO -B -W error verify.py --output results_optimized.json
cmp results_normal.json results_optimized.json
```

Benötigt werden Python, NumPy, SciPy und SymPy. Der Replay liest nur die
eingefrorenen Eingaben und braucht weder das ursprüngliche Repository noch
Netzwerkzugriff. `freeze.py` ist nur das Herkunftswerkzeug für die erste
Archivierung und gehört nicht zum wissenschaftlichen Replay.

Es gibt **261 explizite exakte Prüfbedingungen pro Modus**, zusätzlich zu
den separat ausgewiesenen 17 erhaltenen nativen Konstruktorguards. Die vier
Clockguards sind in den 261 enthalten. Normaler und `-OO`-Lauf erzeugen
byteidentische JSON-Dateien. Die Bosonidentitäten nutzen die exakte Weyl-
Normalordnung; die nativen Zustandsaktionen nutzen alle CAR-Vorzeichen
und Bosonmultiplikitäten. Keine Prüfung benutzt ein wegoptimierbares
`assert`, und Warnungen werden als Fehler behandelt.

Die Bedingungen prüfen konkrete algebraische Tatsachen und Quellenpins;
die allgemeinen Induktions- und Verfügbarkeitsargumente stehen oben.
Die Zahl 261 ist keine Zahl unabhängiger Theoreme oder physischer
Realisierungen. Kein neuer Grundzustandssatz für die Erweiterung, keine
native Raumzeit, keine vollständige E8-Operatordarstellung und kein T1–T8-
Abschluss wird behauptet. Fremde Quellen, v1.6.7, zentrale Ledger und
Webseiten wurden nicht verändert.
