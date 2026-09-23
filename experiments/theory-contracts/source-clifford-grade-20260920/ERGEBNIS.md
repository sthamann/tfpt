# TFPT: konkreter Spinor-Keim und der verbleibende Ursprungstest

20. September 2026 · **UR.SOURCE.CLIFFORD_GRADE.01 · PARTIAL**

**Im bereits untersuchten vollständigen Randmodell ist ein konkreter
Ausgangspunkt für den gesuchten fermionischen Spinor identifiziert:
das ursprüngliche Zusatzfermion `e9`.** Die gemeinsame D8-Symmetrie
verwandelt dieses Feld in einen ganzen Spinororbit. Dabei entstehen
zusammengesetzte Felder aus denselben vorhandenen Randkanälen.

Das geht über ein bloßes Nachzählen von 16, 64 oder 128 Zuständen hinaus:
Die Operatoren, ihre Ladungen, ihre Fermionparität und die verbindenden
Stromoperationen sind explizit angegeben und geprüft.
**Der physikalische Ursprung dieser kritischen Randdynamik ist damit
noch nicht bewiesen; eine vollständige TFPT-Lösung liegt nicht vor.**

## Der konstruktive Anschluss

Im bisherigen gemeinsamen Wörterbuch lautet die Identität

\[
e_9=T(-a/2)+v.
\]

`T` beschreibt die internen D8-Gewichte, `v` den schon vorhandenen
neutralen Ergänzungsanteil. Beide Teile zusammen ergeben das lokale
ursprüngliche Feld; der Ergänzungsanteil allein wäre kein lokales Feld.

Die D8-Stromoperationen verbinden es mit **128 lokalen ungeraden
Feldern**. Unter Spin(10)×SU(4) zerfällt dieser Orbit in zwei Zweige
zu je 64 Feldern, `(16,bar4)` und `(bar16,4)`. Die kleinere Gruppe allein
verbindet nur einen dieser Zweige. Diese Unterscheidung ist geprüft.

Ein anschauliches Bild: Wir müssen in dieser bedingten Beschreibung nicht
128 unabhängige neue Instrumente hinzufügen. Die vorhandenen Instrumente
können unter einer bestimmten gemeinsamen Dynamik 128 zusammengehörige
Spielweisen tragen. Welche Dynamik sie tatsächlich zusammenbindet, ist
jedoch die entscheidende Herkunftsfrage.

## Was dafür wirklich entstehen muss

Die verbindende Symmetrie wirkt auf die ursprünglichen Felder nichtlinear:

| Stromoperatoren | Zwei Fermionfaktoren | Vier Fermionfaktoren |
|---|---:|---:|
| gemeinsame D8-Wurzelströme | 56 | 56 |
| davon Spin(10)×SU(4)-Wurzelströme | 26 | 26 |

Am freien Ausgangspunkt haben die vierfachen Ströme die falsche
Skalendimension für diese chirale Stromsymmetrie. Erst beim schon früher
eingeführten kritischen Operator `Vc` erhalten alle das passende Gewicht
eins. Gleichzeitig erhalten die 128 Spinorfelder die gemeinsamen
Randgewichte `(h,h̄)=(1,1/2)`.

**Die konkrete nächste Herleitung ist damit:** Aus der ursprünglichen
Quelle müssen diese zusammengesetzten Ströme und ihre gemeinsame
kritische Zeitentwicklung hervorgehen. `Vc` lediglich einzusetzen wäre
weiterhin eine zusätzliche Annahme. Die Zahlen sind Gewichte einer
1+1-dimensionalen Randbeschreibung, keine bereits hergeleiteten
vierdimensionalen Weyl-Teilchen.

## Was die einfache Clifford-Reparatur ausschließt

Die vorige Runde hatte vor der Familienprojektion passende
Clifford-Übergangsmatrizen gefunden. Ich habe jetzt die vollständige
unprojizierte Operatoralgebra geprüft. Spinorzustände darin sind noch
keine Spinor-Feldoperatoren: Operatorgewichte sind Differenzen von
Zustandsgewichten und haben die andere Symmetriewirkung.

Auch das gewöhnliche graduierte Zusammensetzen der nativen Fermionen
mit zusätzlichen Vektor-Majoranas hilft nicht. Zwei zentrale
Symmetriezeichen erzwingen auf der **gesamten** zusammengesetzten
Operatoralgebra die falsche Parität für den gesuchten Spinorzweig.
Dieser Ausschluss betrifft beliebig hohe Produkte, nicht nur den
einfachsten Ansatz. Ein frei angesetzter neutraler Zusatzfermionfaktor
ist im vorhandenen lokalen neutralen Gitter nicht enthalten.

Die nichtlineare Randwirkung oben ist ein ausdrücklich anderer
Gruppenanschluss und fällt deshalb nicht unter diesen Ausschluss.
Sie ist der weiterzuverfolgende positive Ansatz, sofern ihre Dynamik
aus der ursprünglichen Quelle begründet werden kann.

## Abgleich mit den anderen Lanes

Der aktuelle Graph und die Originaldateien wurden erneut geprüft.
Die Tasks „Untersuche TFPT-Feldsignale“ und „Extrahiere TFPT-Minimalkern“
waren bei den kompakten Statusabfragen aktiv. Die zusätzliche Prüfung der
gespeicherten Dateien fand während dieser Runde den neuen Vertrag
**`UR.SOURCE.FLUX_INDEX.01`**. Sein algebraischer Prüflauf wurde hier
reproduziert und mit dem gespeicherten Zertifikat verglichen.

Der Ladungskandidat `g=K n` aus dieser Quellenarbeit passt zum neuen Feldorbit: **Alle 128 Felder
tragen dieselbe Kandidatenladung −1; die verbindenden Ströme sind neutral.**
Das bezeichnet einen geladenen Feldsektor. Nach einer tatsächlichen Eichung
wären die Felder keine lokalen Gauss-invarianten Observablen.

Die andere ursprüngliche Ladung `q` unterscheidet die Felder dagegen.
Deshalb bleibt der bekannte Quellzeitterm `−Qq/4` sichtbar und spaltet
ihre Frequenzen. Eine Verschiebung durch `Qg` kann das nicht korrigieren,
weil sie alle 128 Felder gleich verschiebt. Der gleiche Ursprung muss
also auch diesen Zeitanschluss erklären.

Der neue Flussindex-Vertrag begründet außerdem den vollständigen
**neutralen E8-Gitterquotienten** innerhalb seines festgehaltenen
Randwörterbuchs. Hier zeigt sich nun eine entscheidende zusätzliche
Prüfung: Zwei Stromvertreter können im neutralen E8-Quotienten gleich
sein und auf das geladene Ausgangsfermion trotzdem verschieden wirken.
Der explizite Vergleich liefert einmal einen einfachen Pol in der
Feldkorrelation und einmal keinen; ihre kritischen Dimensionen sind
eins beziehungsweise zwei. Der Quotient verliert also genau Information,
die für den geladenen Materieanschluss benötigt wird.

Die beiden Lane-Ergebnisse passen deshalb als unterschiedliche Teile
einer möglichen vollständigen Feldtheorie zusammen. Ihre Gleichsetzung
als bereits gemeinsame physikalische Lösung wäre falsch. Der neutrale
E8-Sektor und der geladene Spinorsektor brauchen dieselbe nachgewiesene
Quellwirkung, einschließlich dieser unterschiedlichen Stromvertreter.

## Nachprüfbarkeit und Grenze

Die ausführliche Herleitung steht in [PROOF.md](PROOF.md), die
Originalquellenbindungen in [source_manifest.json](source_manifest.json)
und die konkreten Rechnungen in [certificate.json](certificate.json).
Normaler und optimierter Prüflauf müssen identische Zertifikate erzeugen.
Die allgemeinen Ausschlüsse sind schriftlich bewiesen; die endlichen
Rechnungen sind keine formale Beweisassistentenprüfung. Für diese Runde
wird kein unabhängiger Agentenreview beansprucht.

Der verwendete Gitter-/Stromanschluss folgt dem etablierten
[D8/E8-Vertexalgebra-Rahmen](https://arxiv.org/html/0808.1458v2).
Die [Primärliteratur zur sektorübergreifenden Feldkonstruktion, §7.3](https://arxiv.org/html/2608.26456v1#S7.SS3)
zeigt zudem, weshalb eine echte unendliche Felderweiterung mehr verlangt
als ein zusätzliches endliches Clifford-Zustandslabel. Beide Quellen
liefern keine TFPT-spezifische Herkunftsherleitung.

Offen bleiben der Quelltransfer zur kritischen Dynamik, die Kanalherkunft
und der gemeinsame physikalische Zeit-/Feldanschluss. Kein T1–T8-Gate,
keine vollständige Raumzeitphysik und keine Gesamtlösung werden geschlossen.
