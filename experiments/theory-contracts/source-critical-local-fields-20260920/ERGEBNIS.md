# Quellen-Lane, lokale Fermionen und Rückbindung an die gemeinsame Dynamik

20. September 2026 · `UR.SOURCE.CRITICAL_FIELDS.01` · **PARTIAL**

**Die andere Quellenarbeit ist weitergekommen. Ihr neuer Dynamikvergleich
entscheidet zugleich, wie unser nächster Anschluss zu bewerten ist:**
Der direkte Vergleich der ursprünglichen freien Energie mit der gewählten
E8-Energie erreicht den hier untersuchten Ising-Punkt nicht. In diesem
separat gewählten Punkt können wir inzwischen explizite lokale ungerade
Spinorfelder angeben. Ihre Herkunft, ihre vollständige Kopplung und der
Übergang zu drei leichten physikalischen Familien sind damit noch nicht
hergeleitet. Eine vollständige TFPT-Lösung liegt weiterhin nicht vor.

Die neue positive Konstruktion ist präziser als ein Vergleich von Zahlen
oder Dimensionen: Feldvektoren, Hyperladung, mikroskopische Parität,
Familienorientierung und der notwendige neutrale Anteil sind ausgeschrieben.
Der Abgleich mit Energie, Clocks und realem Higgs zeigt, welche zusätzliche
Struktur eine gemeinsame Quelle tatsächlich liefern müsste.

## 1. Was sich in der anderen Lane verändert hat

Die App-Tasks und ihre Originalartefakte wurden gelesen; Einzelheiten stehen
in [LANES.md](LANES.md). Die jüngsten übernommenen Contracts sind:

| Original | Belastbarer Inhalt | Konsequenz für die Gesamtlösung |
|---|---|---|
| `UR.SOURCE.GRADED_LOCALITY.01` | Vollständiges Quellgitter mit vier korrelierten lokalen Klassen; im ausgelückten E8-Sektor fehlen leichte ungerade Felder | Die schweren Zusatzmoden tragen notwendige Statistik; ihr Weglassen ersetzt kein Materiefeld |
| `UR.SOURCE.DYNAMICS_SELECTION.01` | Tatsächlicher Energietransport, Verteilung der E8-Wurzeldimensionen, direkter Vergleichspfad und vollständige Grenze für andere neutrale Nulloperatoren | Der gewählte wechselwirkende E8-Rand entsteht nicht durch bloßes Umschreiben der freien Quelle |
| `UR.SOURCE.FLAVOR_ORIGIN.01` | Gegenüber dem vorherigen Abgleich unveränderte Kernartefakte | Dort ist kein neuer Massenoperator hinzugekommen |

Die neue Dynamikarbeit unterscheidet den passiven Basiswechsel
`V0 → W^T V0 W` von einer tatsächlichen Änderung zu `V_aux`.
Bei der ursprünglichen freien Energie besitzen die 240 E8-Wurzelvertices
die Dimensionen `1` (56 Stück), `2` (112), `5` (56), `10` (16).
Erst bei der zusätzlich gewählten E8-Energie haben alle Dimension 1.
Das ist ein physikalischer Unterschied der Korrelationen.

Auf dem dort festgehaltenen Vergleichspfad sind nur die beiden neutralen
selbstnullen Terme `n,z` Kandidaten für Relevanz oder Marginalität. Alle
anderen zulässigen selbstnullen Vertices haben auf dem gesamten Pfad
Dimension mindestens `7/2`. Der gemeinsame Mittelpunkt hat

\[
\Delta(n)=\Delta(z)=2.
\]

Dies ist eine genaue Aussage über den angegebenen Vergleichspfad, keine
bereits berechnete wechselwirkende Phasenentwicklung.

## 2. Der neue konstruktive Feldanschluss

Wir behalten das vollständige ursprüngliche Gitter
`Gamma=Z^(9,1)` mit `K=diag(1^9,-1)` und seine fermionischen Vorzeichen.
Die gemeinsame D8-Einbettung lautet

\[
a=(1,1,1,-1,-1,-1,-1,-1),\qquad
T(p)=(p,-a\cdot p/2,a\cdot p/2).
\]

Mit den schon vorhandenen neutralen Richtungen

\[
n=(1,1,1,-1,-1,-1,-1,-1,-1,3),\quad z=e_9-e_{10},
\quad u=(n+z)/2,\quad v=(n-z)/2
\]

trägt die Klasse `c` die Spinordarstellung

\[
\boxed{(16,\overline4)+(\overline{16},4)}.
\]

Sie ist im gemeinsamen `T(D8)`-Wörterbuch **ungerade**. Die bisherige
E8-Spinorklasse `s` trägt dagegen
`(16,4)+(bar16,bar4)` und ist dort gerade. Das vertauschte Familienverhalten
ist wesentlich; `4` und `bar4` werden nicht gleichgesetzt.

Für

\[
p=(-1/2,1/2,1/2,1/2,1/2,1/2,1/2,1/2)
\]

erhalten wir zwei tatsächliche ganzzahlige lokale Feldvektoren:

\[
x_R=T(p)+u=(0,1,1,0,0,0,0,0,1,0),
\]

\[
x_L=T(p)+v=(0,1,1,0,0,0,0,0,0,1).
\]

Beide sind mikroskopisch fermionisch, besitzen `q=3`, `Y=1/3` und liegen
im Zweig `(16,bar4)`. Ihr neutraler Anteil ist erforderlich: `u` und `v`
allein sind nicht ganzzahlig und damit keine unabhängigen lokalen Vertices
dieser Quelle. In einem Bild: Der Spinor und sein neutraler Anteil bilden
zusammen das lokale Feld; die beiden Hälften dürfen nicht getrennt als
vollständige Teilchen behandelt werden.

Am bereits gewählten Diagnosepunkt

\[
V_c=K+2Kvv^TK
\]

haben beide Felder die Skalendimension `3/2`. Ihre konformen Gewichte sind
`(3/2,0)` beziehungsweise `(1,1/2)`. Beim zweiten Feld ist nur der neutrale
Faktor linksbewegend; das ganze Feld ist nicht rein linksbewegend.
Diese Gewichte gelten in **1+1 Dimensionen**. Sie liefern keine
Identifikation mit einem vierdimensionalen Weyl-Fermion.

Die vollständige Klassifizierung gilt für alle Gitterfelder, nicht nur
für eine Auswahl kurzer Vektoren:

| gemeinsame D8-Klasse | Parität | kleinstes UV-Delta bei Vc | bedingter führender kritischer IR-Anteil |
|---|---|---:|---|
| `0` | gerade | 0 | Vakuum und gerade Nachkommen |
| `v` | ungerade | 3/4 | Vektor mal Twistfeld, Delta 5/8 |
| `s` | gerade | 5/4 | Spinor mal komplementäres Twistfeld, Delta 9/8 |
| `c` | ungerade | 3/2 | gekreuzter Spinor mal Majorana, Delta 3/2 |

Die IR-Spalte setzt gleiche passend normierte Cosinus-Kopplungen,
ein gewähltes Massenvorzeichen und den passenden Langdistanzanteil des
massiven Ising-Sektors voraus. Die Refermionisierung selbst ist bekannt;
neu ist hier ihre Verbindung mit den expliziten lokalen Quellvektoren und
der tatsächlichen Familienorientierung.
[Lecheminant–Gogolin–Nersesyan, Abschnitt II.2](https://arxiv.org/abs/cond-mat/0203294),
[Tsvelik, Appendix B](https://link.aps.org/accepted/10.1103/PhysRevB.94.205141).

Die globalen Sektoren bleiben korreliert. Der zusätzliche Test in
[IR_GLUE.md](local_modules/IR_GLUE.md) gibt einen sechssektorigen algebraischen
Kandidaten an, dessen Monodromie und Fusion passen. Er liefert noch keinen
vollständigen, aus der Quelle ausgewählten IR-Vakuumprojektor. Ein beliebiges
Tensorprodukt aus D8- und Ising-Feldern wäre hier unzulässig.

Eine während der Gegenprüfung gefundene Verwechslung wurde behoben:
Der rohe Vertreter `f+b` hat Delta `5/2`, nicht `3/2`. Die kleine Dimension
gehört einem um einen echten D8-Gittervektor verschobenen minimalen
Vertreter derselben Klasse. Die Prüfroutinen vergleichen jetzt direkt die
vollständigen zehnkomponentigen Felder mit ihren angegebenen Gewichten.

## 3. Was der neue Spinor für Massen erlaubt

Die tatsächliche Familienwirkung erzwingt für die neuen `(16,bar4)`-Felder
den zugehörigen Tensor

\[
\Lambda^2\overline4\longrightarrow6.
\]

Aktiviert man in einem festen neutralen Higgs-Kanal nur ein Familientriplet
`h`, bleibt die Dreifamilienmatrix

\[
A(h)_{ij}=\epsilon_{ijk}h_k,\qquad A(h)h=0,
\quad\operatorname{rank} A(h)=2\quad(h\ne0).
\]

Ein genauer bedingter Rangweg ergibt sich mit beiden Tripletkomponenten
`h,k` und einem vierten SU(3)-Singletkanal:

\[
Y(h,k)=\begin{pmatrix}A(h)&k\\-k^T&0\end{pmatrix},
\qquad\det Y=(h^T k)^2.
\]

Das zeigt konkret, welche zusätzliche Kopplung die fehlende Richtung
erreichen könnte. Wir haben geprüft, ob die native Realität des Higgs
sie schon automatisch liefert. Das Ergebnis lautet: **nicht innerhalb
eines festgehaltenen neutralen Yukawa-Kanals**.
Die vorhandene Konjugation vertauscht gleichzeitig `H_d` und `H_u`
sowie die komplementären Familienkomponenten. Sie bestimmt somit nicht
`k=conjugate(h)` bei festem `H_d`.

Unter der zusätzlichen Wahl eines separierbaren Hintergrunds mit einzeln
reellem Spin(10)- und Familienfaktor ist dagegen `k=conjugate(h)` möglich;
dann ist `det Y=||h||^4`. Diese Wahl ist ein algebraischer Vollrangweg für
**vier** Komponenten. Die Quelle bestimmt bisher weder diese Auswahl noch
einen schweren vierten Kanal, drei verbleibende leichte Familien oder deren
Massenhierarchie. Auch der neue Tensor ist noch nicht als Kopplung der
lokalen `c`-Felder im ursprünglichen Hamiltonoperator ausgeführt.
Die Einzelheiten stehen in [REVIEW_FLAVOR.md](flavor_delta/REVIEW_FLAVOR.md).

Der direkte Vergleich der 64 implementierten Gewichte klärt dabei eine
wichtige Konvention: Im hier fixierten Wurzelwörterbuch gehört der native
Block zu `(bar16,bar4)`. Erst seine ausdrücklich erklärte globale
Wurzelkonjugation liefert den alten Zweig `(16,4)`. Der neue Zweig
`(16,bar4)` ist mit keinem davon durch bloßes Umbenennen identifiziert.
Die beschriebenen algebraischen Konjugationen sind noch kein gemeinsamer
physikalischer Transport von Operator, Hyperladung und Energie.

## 4. Rückprüfung mit Energie und Clocks

Der neue Energievergleich erlaubt einen besonders kurzen Gegencheck:

\[
(V_\theta)_{9,10}=0\ \text{auf dem gesamten direkten Vergleichspfad},
\qquad (V_c)_{9,10}=4.
\]

Unser Ising-Punkt ist also nicht nur ein anders benannter Mittelpunkt.
Er benötigt eine andere kollektive Dichterichtung mit Beteiligung des
zusätzlichen rechten Kanals. Diese Quelle ist noch nicht hergeleitet.
[Genauer Abgleich](energy_bridge/PROOF.md).

Auch die früher gespeicherten 10D-Lifts der nativen Clocks wurden direkt
geprüft. Keine nichttriviale Potenz von `C` oder `J` erhält zugleich den
hier gewählten Energiepunkt; nur die Identität erhält den `z`-Cosinus bis
auf Vorzeichen. Jedes weitere Element seiner jeweiligen Clock-Bahn hat
eine von null verschiedene ursprüngliche Hyperladung.
Eine bloße Addition der gesamten Bahn würde daher bei festem
Hyperladungs-U(1) geladene Wechselwirkungen hinzufügen.

Das ist ein Ausschluss dieses **stationären Anschlusses mit diesen festen
Lifts**. Es ist kein allgemeiner Satz, dass eine Clock mit jedem
Hamiltonoperator kommutieren müsse. Ein gemeinsamer Transport von
Hamiltonoperator, Markierung und Zustand wäre eine andere physikalische
Identifikation und muss als solche aus der Quelle folgen.
[Exakter Clock-Test und unabhängiger Review](clock_gate/PROOF.md).

## 5. Was jetzt zur vollständigen Lösung geliefert werden muss

Das gesamte TFPT-Gefüge bleibt der Maßstab: ursprünglicher Rand,
Compiler und E8-Abschluss, Standardmodell und Flavor, Alpha, Clocks,
Quantenstruktur, Zustand, Dynamik und schließlich gemeinsames Kontinuum
und Gravitation. Die heutigen Rechnungen ersetzen keine dieser Ebenen.

Der neue Anschluss macht die Herkunftsfrage konkreter. Benötigt wird
ein **ursprünglicher nichtgaußscher Quelloperator**, dessen gemeinsame
Abbildung Kanalinhalt, Ladungen, Parität, lokalen Zustand und Zeitentwicklung
erhält und aus dem die kollektive Energie sowie die relevanten Kopplungen
folgen. Für den hiesigen Kandidaten müsste dieser Operator außerdem die
kritische Auswahl und den neuen Materie-Kopplungstensor tragen.

Ein schon konstruierter Ziel-Hamiltonoperator, der anschließend mit einem
gewählten Basiswechsel auf einen anderen Raum zurückgezogen wird, liefert
diesen Ursprung nicht. Ebenso wenig reichen ein passendes Spektrum,
eine Determinantenphase oder ein vierdimensionaler invertierbarer
Familienblock für den vollständigen physikalischen Anschluss.

**Ergebnis des Weiterarbeitens:** Der fehlende lokale ungerade
Spinoranschluss ist für einen klar benannten kritischen Kandidaten
konstruktiv eingegrenzt; Ladungen und Familienwirkung sind geprüft.
Der tatsächliche Massenweg und die erste zusätzliche Dynamik sind genauer
bestimmt. Ihre gemeinsame Auswahl aus der ursprünglichen Quelle ist
weiter offen. Der Contract schließt deshalb kein physikalisches T1–T8-Gate
und behauptet keine vollständige Lösung.

## Nachprüfung und Herkunft

Die einzelnen Beweise und unabhängigen Reviews liegen in `local_modules`,
`critical_review`, `flavor_delta`, `clock_gate` und `energy_bridge`.
Der gemeinsame Prüflauf und die Quellen-Hashes stehen in `validation.json`
und `source_manifest.json`. Exakte algebraische Prüfungen bestätigen die
angegebenen bedingten Aussagen; ihre Anzahl ist kein Maß für physikalische
Evidenz. Die tragende Verifikationssuite, Papers und empirische Scorecard
werden durch diesen Forschungs-Contract nicht geändert.
