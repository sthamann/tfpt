# TFPT: neue Lösungswege aus dem Abgleich der Lanes

Stand: 20. September 2026. Ergebnis: konstruktive Cross-Lane-Synthese mit unabhängig geprüften endlichen Identitäten; keine vollständige physikalische Gesamtherleitung.

## Der neue gemeinsame Ansatz

Die stärkste Verbindung entsteht aus vier bereits vorhandenen positiven Ergebnissen:

1. Die QWZ-Quelle besitzt ein **komplexes neutrales Determinantenfunktional**, dessen endliche Phase festgelegt ist. Die Current-Referenz erhält sogar geordnete Vierpunktphasen.
2. Die Probe-/Carry-Lane besitzt eine **operatorwertige geladene Antwort**. Sie erhält Übergänge, die eine skalare Vakuumantwort verliert.
3. Die neue Randrekonstruktion liefert einen konkreten gemeinsamen Kandidaten für **lokale E8-Operatoren, Vakuum und Zeit**, zusammen mit einem massiven komplementären Dirac-Sektor.
4. Die Compiler-Lane hat den **vollständigen endlichen Vierquellen-Grundzustandsvergleich** geschlossen und einen aus den Paketmatrixelementen berechneten kritischen Kettenkandidaten gewonnen.

Zusammen legen diese Resultate einen präziseren Lösungsweg nahe: **Die gemeinsame physikalische Theorie durch eine phasen- und antworttreue Reduktion der vollständigen Quelle gewinnen.** Dabei müssen die ausgeblendeten Zustände samt ihrer Rückwirkung und ihrem Beitrag zur Wirkung erhalten bleiben. Das ist eine Forschungsrichtung mit konkreten vorhandenen Eingaben, noch kein Beweis, dass die verschiedenen Quellen bereits identisch sind.

Das Bild dazu: Mehrere Lanes sehen unterschiedliche Anzeigen desselben gesuchten Instruments. Einige sehen Ladungstransport, andere Spektrum, Phase oder Bindungsordnung. Der Abgleich zeigt jetzt genauer, welche inneren Freiheitsgrade eine einzelne Anzeige ausblendet. Die gemeinsame Lösung muss diese Anzeigen aus **einer** Quelle mit **einer** Zeit und konsistenten Operatoren ableiten.

## Was sich durch die anderen Lanes tatsächlich verbessert

| Ergebnis / Herkunft | Belastbarer Fortschritt | Neuer Anschluss und verbleibende Voraussetzung |
|---|---|---|
| `neutral-pair-composition`, `current-fourpoint-limit`, `current-truncation-bridge` | Vollständige endliche neutrale Source-Determinante; phasentreue Current-Referenz und geordneter Vierpunkt-Limes; Current-Galerkin-Konvergenz für feste Wörter | Ein komplexes Antwortfunktional ist bereits vorhanden. Es fehlt der uniforme mikroskopische QWZ-Vergleich und die physische Phasen-/Yukawaabbildung. |
| `UR.SOURCE.PROBE_CARRY.01` | Das volle operatorwertige Übergangsmaß bestimmt die reduzierte Antwort einschließlich Kreuztermen mit Ladungsübertrag | Liefert die geladene Ergänzung zur neutralen Determinante. Proben müssen noch aus der Quelle ausgewählte mikroskopische Felder werden. |
| Task „Gemeinsame Quelle untersuchen“ | Konkrete lokale E8-Randrekonstruktion plus massives gegenläufiges Paar; die sichtbaren Gitter- und Energiematrixformeln sind hier unabhängig bestätigt | Der massive Sektor ist ein konkreter Ort für bisher ausgeblendete Beiträge zur Wirkung. Zusatzpaar, Wechselwirkung und Energiematrix sind noch gewählt. |
| `UR.SOURCE.LOCAL_LIMIT.01`, `UR.SOURCE.RG_CLOCK_BRIDGE.01` | Vollständiger QWZ-Hamiltonoperator, gefüllter Zustand, lokales geladenes CAR-Feld und gemeinsame Zeit; im lokalen Grenzfall ein komplexer chiraler Kanal je Rand | Kein erneuter Aufbau eines beliebigen Vakuummodells nötig. Der unveränderte Streifen liefert jedoch nicht acht interne Spezies. |
| `UR.COMPILER.FOUR_FOLLOWUPS.28` | Alle zuvor offenen zehn K3-Masken ausgeschlossen; vollständiger Vierquellen-Grundraum und eindeutiger Grundzustand auf dem kleinen positiven Strahl | Ein echter endlicher Vakuumschritt ist geschlossen. Große Ketten brauchen noch kontrollierte Rückwirkung des Komplements. |
| Dieselbe Compiler-Lane: Paketkette | Native Matrixelemente ergeben die bedingte Ising-Suchbedingung \(2\mu=\kappa+9J\) | Konkretes Ziel für einen Niederenergiegrenzwert; die Paketfamilie ist unter dem vollen Hamiltonoperator nicht invariant. |
| Charged-Time-/Clock-Lanes | Geladene Felder unterscheiden \(L_0\) von \(L_0-\delta\cdot Q\); affine Stromklammern und echte Clock wählen bedingt \(H=aL_0+c\) | Ein gemeinsamer Zeittest ist formuliert. Neutrale Ströme und diskrete Clocks allein reichen nicht. |
| `UR.RAW_CARRIER_ORIGIN.01`, operationelle Geometrie | Verschiedene Energien können dieselbe Polarisation besitzen; verschiedene lokale Projektoren können nach Kompression identisch werden | Die Reduktion muss die benötigten inneren Ladungen, Zeitdaten und lokalen Algebren unterscheiden können. |

Wichtige Aktualisierung gegenüber älteren Zusammenfassungen: Der offene Vierquellenvergleich aus Contract `.26` ist in `.28` **geschlossen**. Offen bleibt die große Kette, nicht dieser endliche Vergleich. Die zitierte Proof-Datei nennt \(E_0=\lambda\kappa\), \(\lambda=1.221493930352475\ldots\), Grundraumdimension zwei bei \(J=\mu=0\), und einen eindeutigen Grundzustand mit Lücke mindestens \(\mu/8\) für \(J=\mu=\epsilon\kappa\), \(0<\epsilon\le10^{-8}\). Diese bestehenden Beweise wurden gelesen; ihre sämtlichen Checker wurden hier nicht erneut ausgeführt.

## Weg 1 — die vollständige komplexe Wirkung beim Reduzieren erhalten

Dies ist der am besten begründete gemeinsame Weg zur bisherigen Phasenfrage.

Für einen invertierbaren endlichen gaußschen Kern mit invertierbarem Komplementblock gilt exakt

\[
D=\begin{pmatrix}A&B\\C&E\end{pmatrix},\qquad
S=A-BE^{-1}C,
\]
\[
(D^{-1})_{PP}=S^{-1},\qquad
\det D=\det E\,\det S.
\]

Die reduzierte Antwort liefert den Schur-Kern. Der volle Determinant besitzt zusätzlich den Komplementfaktor. Auf einer gemeinsamen glatten, nichtsingulären Parameterfamilie folgt lokal

\[
\partial_\theta\log\det D
=\operatorname{Tr}(E^{-1}\partial_\theta E)
+\operatorname{Tr}(S^{-1}\partial_\theta S).
\]

**Die nützliche neue Korrelation ist nicht die bekannte Blockidentität selbst.** Sie verbindet drei konkrete TFPT-Befunde: die geladene Schur-Antwort, die bereits beobachtete Kompensation in der neutralen Source-Determinante und den zusätzlichen massiven Faktor der E8-Randrekonstruktion.

Der hier ausgeführte exakte Test zeigt: Für \(D'=D\oplus q\) bleibt die gesamte betrachtete P-Antwort gleich, während \(\det D'=q\det D\). Das ist ein Identifizierbarkeitsbeispiel, keine neu postulierte TFPT-Welt. Ein von allen Quellen und Hintergründen unabhängiges \(q\) kann nur eine herauskürzbare Normierung sein. Physikalisch relevant wird der fehlende Faktor erst, wenn seine Parameter-, Eichfeld- oder Geometrieabhängigkeit aus der Quelle stammt und im vollständigen regulierten Ausdruck überlebt.

Die Aussage ist auch kein universelles Unmöglichkeitstheorem: Erzeugen die Proben das gesamte Komplement zyklisch, können vollständige Übergangsdaten dessen endliche minimale Realisierung bestimmen. Genau diese Vollständigkeit muss dann nachgewiesen werden. Ein Hamilton-Resolvent ist zudem nicht automatisch das chirale Fermionmaß einer vierdimensionalen Feldtheorie.

### Positive Eingabe statt frei gewähltem komplexem Seed

Vorhanden ist bereits

\[
\mathcal Z_N[\epsilon,a]
=e^{-i\sum_l\epsilon_l\operatorname{Tr}(PF_{a_l}P)}
\det_{\operatorname{ran}P}
\left(P\prod_l e^{i\epsilon_lF_{a_l}}P\right).
\]

Hier werden die komplexe Phase und die Normalordnung der einzelnen Einfügungen gemeinsam geführt. Für physische alternierende Wörter kürzen die äußeren Rampen exakt. Das Current-Modell liefert die geordnete Vierpunktphase; der mikroskopische Source-Limes ist noch nicht vollständig bewiesen.

Das ist eine bessere Ausgangsbasis als die bloße Ersetzung eines reellen Parameters durch \(z=\phi_0e^{i\theta}\). Es benötigt aber eine echte Abbildung

\[
\theta\longmapsto(F_d(\theta),F_e(\theta))
\longmapsto(Y_d(\theta),Y_e(\theta)).
\]

Die Randendpunkte \(a_l\) sind räumliche Parameter, keine bereits hergeleitete axionartige Phase oder physikalische Zeit. Die beiden Deformationen müssen tatsächlich die Down- und Leptonoperatoren treffen. Ihre relative Antwort darf keine bloße Basisrephasierung, Endpunkt-Koboundary oder gemeinsame neutrale Spektatorphase sein.

**Entscheidender Test:** Beide Deformationen in dieselbe vollständige regulierte Source-Determinante einsetzen und ihre Ward-Antwort einschließlich Komplement vergleichen. Die frühere Identität

\[
E-\frac83N=\delta_e-\delta_d
\]

liefert die Zielstruktur. Die Exponenten \((6,9,10)\) würden unter der zusätzlichen holomorphen Einbettung eine relative Determinantenwindung \(10-9=1\) ergeben; diese Einbettung ist weiterhin zu beweisen. Eine reine Fermionbasisrotation ohne zusätzlichen physikalischen WZ-Term muss in der vollständigen Antwort verschwinden. Ein isolierter Jacobian darf nicht noch einmal als reale Kopplung gezählt werden.

Das aktuelle Material definiert die benötigten gemeinsamen Phasentangenten am QWZ-Quelloperator noch nicht. Daher ist der nächste substanzielle Arbeitsschritt die Herleitung dieser Deformationen aus P1/P2 und dem Flavor-Compiler. Ein frei erfundener Winkel am Zusatzsektor würde genau diese Lücke überspringen.

## Weg 2 — die konkrete E8-Randrekonstruktion zur Herkunftsprüfung verwenden

Die andere Task hat einen deutlich konkreteren Kandidaten als die reine Identifikation gleicher Dimensionen geliefert:

\[
K=\operatorname{diag}(1^9,-1),\quad
n=(1,1,1,-1,-1,-1,-1,-1,-1,3).
\]

Aus den sichtbaren Formeln wurde hier unabhängig ein ganzzahliger Basiswechsel rekonstruiert mit

\[
\det W=-1,\qquad
W^TKW=G_{E_8}\oplus\operatorname{diag}(1,-1).
\]

Alle 240 E8-Wurzeln werden auf ganzzahlige lokale Vektoren abgebildet. Die angegebene Energiematrix ist positiv, mit Eigenwerten \(1\) achtfach und \(17\pm12\sqrt2\). Die E8-Wurzeln sind bezüglich der K-Paarung orthogonal zu beiden zusätzlichen Richtungen. Die algebraischen Voraussetzungen der behaupteten Trennung sind damit konkret geprüft.

Die zugrunde liegende Randrekonstruktionsidee ist bekannte Physik; mehrere Randphasen desselben Bulks und E8-Ränder durch Wechselwirkung mit zusätzlichen trivialen Moden sind in der Primärliteratur beschrieben: [Cano et al., Bulk-Edge Correspondence in 2+1-Dimensional Abelian Topological Phases](https://arxiv.org/html/1310.5708).

**Neu für unsere Suche:** Dieser Kandidat verbindet lokale E8-Operatoren und einen komplementären massiven Sektor in einem expliziten gemeinsamen Rahmen. Damit lässt sich konkret fragen, ob TFPT gerade diese Wechselwirkung und diese Einbettung auswählt, und welchen Beitrag der massive Sektor zur vollständigen Wirkung behält.

Der nächste Herkunftstest ist eng begrenzt: Die native C/J-Wirkung und die tatsächlichen Ladungen auf dem vollständigen zehnkomponentigen Gitter bestimmen; prüfen, ob sie die Nullwechselwirkung und den E8-Teil erhalten; anschließend herleiten, warum Zusatzpaar, Nullrichtung \(n\) und Energiematrix aus der Quelle folgen. Eine Z4-Klebegraduierung allein ist kein Nachweis der TFPT-Clocks.

Der massive Dirac-Sektor ist **kein bereits gefundenes ultraleichtes Axion**. Seine Masse ist im Kandidaten reell; eine dynamische Phase fehlt. Auch die Zuordnung eines 1+1D-Randsektors zu 3+1D-Farb-/EM-Anomalien fehlt. Der originale ausführbare Anhang der anderen Task war nicht zugänglich; die unabhängige Prüfung hier umfasst die sichtbaren Gitter- und Matrixformeln, nicht die dort behauptete vollständige Kokzyklustabelle oder einen Kontinuumsbeweis.

## Weg 3 — dieselbe Reduktion an Vakuum, Zeit und Orten prüfen

Die Compiler-Kette bietet einen zweiten, näher an der Bindungsgrammatik liegenden Testfall. Ihre Paketkompression ergibt

\[
H_{\rm Paket}=\text{const}
+\frac{\kappa+9J}{16}\sum Z_eZ_{e+1}
-\frac\mu8\sum X_e.
\]

Die daraus folgende kritische Suchbedingung ist \(2\mu=\kappa+9J\). Zugleich ist aus dem vollen Hamiltonoperator bekannt

\[
\|(1-P)H|\mathrm{alternierend}\rangle\|^2
\ge\frac{3N(\kappa+J)^2}{160}.
\]

Das Komplement ist also nicht einfach entkoppelt. Die bereits gewonnenen Ritzwerte der Paketkette beweisen keine Kritikalität des vollständigen Systems. Hier lässt sich derselbe Ansatz wie bei Weg 1 anwenden: die energieabhängige Rückwirkung des Komplements bestimmen, statt nur die komprimierte Matrix zu optimieren. Diese Rückwirkung ist allgemein ein Operator; die Gauß-Determinantenformel allein löst das wechselwirkende Vielteilchenproblem nicht.

**Erfolgskriterium:** Eine aus dem wirklichen großen Grundzustand gewonnene Niederenergiebeschreibung mit kontrollierter Komplementrückwirkung, die geladene Antworten und verschiedene lokale Observablen erhält. Erst dann ist ein robuster kritischer Grenzwert belegt. Eine angenommene Komplementlücke wäre als zusätzliche Voraussetzung auszuweisen; wenn resonante Zustände vorliegen, müssen sie im behaltenen Raum bleiben.

Die Clock-Lane liefert dafür einen unabhängigen Test: Auf demselben affinen Stromraum mit additiven skalaren Modenfrequenzen erzwingen Klammern und echte Clock bedingt \(H=aL_0+c\). Aber neutrale Ströme unterscheiden \(L_0\) und \(L_0-\delta\cdot Q\) nicht zuverlässig. Geladene Paar-/Spinorfelder tun es. Daher gehören ihre Frequenzen und die ihrer Adjungierten zum gemeinsamen Prüfkriterium.

Die Geometrielane ergänzt: Wenn zwei verschiedene lokale Projektoren durch \(PQ_1P=PQ_3P\) gleichgesetzt werden, kann die komprimierte Antwort sie nicht als verschiedene Orte rekonstruieren. Die Ortsfrage wird damit zu einer expliziten Prüfung der erhaltenen lokalen Algebren und ihrer Hamiltonträger. Das ist keine automatische Raumzeitdimension aus einer Gitterzahl.

## Beitrag zur Gesamtlösung und Arbeitspriorität

Die drei Wege sind verbundene Prüfungen einer Hauptidee: **eine vollständige gemeinsame Quelle so reduzieren, dass die für die Physik benötigten Antworten erhalten bleiben.** Sie sollen nicht zu drei frei wählbaren Ersatzwelten werden.

Die Priorität liegt auf Weg 1 mit den vorhandenen neutralen und geladenen Quellantworten. Weg 2 liefert einen konkreten Zielkandidaten für die lokale E8-Realisierung; Weg 3 liefert den Test, ob dieselbe Art von Reduktion mit nativem Vakuum, Dynamik und Lokalität vereinbar ist. QWZ-Streifen, erweiterte E8-Randtheorie und Compiler-Hamiltonfamilie sind derzeit verschiedene Konstruktionen. Ihre Operator-, Zustands-, Ladungs- und Zeitabbildungen müssen explizit sein, bevor ihre Resultate als Resultate eines einzigen Systems kombiniert werden.

Eine spätere gemeinsame Wirkung \(\Gamma\) könnte Flavorphasen, elektromagnetische Polarisation, Zustandsregel und Geometrieantwort aus demselben Ursprung liefern. Für Alpha müsste die elektromagnetische Antwort derselben Quelle vorliegen; für Gravitation eine hergeleitete geometrische Hintergrundabhängigkeit. Die Rand-Energiematrix ist dafür noch keine vierdimensionale Metrik. Ein Fermiondeterminant ist zudem nur ein Teil einer vollständigen Wirkung, zu der auch bosonische Terme, Maß, Randbedingungen und Wechselwirkungen gehören können.

Der entscheidende nächste Herkunftsnachweis ist deshalb nicht „noch mehr passende Zahlen“, sondern eine aus der Originalquelle gewonnene Deformationsfamilie, die zugleich die benötigten Ladungen, Flavorphasen und gemeinsame Zeit besitzt. Der Abgleich hat dafür vorhandene positive Bausteine, eine konkrete mögliche Trägerstruktur und scharfe Verlusttests identifiziert. Eine physikalische Gesamtlösung oder die Schließung eines T1–T8-Gates folgt daraus noch nicht.

## Nachvollziehbarkeit

- `lane_inventory.md/json`: neun Lanes, sieben mit direkt abgeglichenem Contract-Index; ergänzend die Phase-/Current- und geladenen Zeitprüfungen.
- `neutral_determinant_bridge.md`, `charged_phase_bridge.md`, `time_source_bridge.md`: genaue Originalstellen und Quellenhashes.
- `check_bridges.py`, `bridge_checks.json`: unabhängige exakte endliche Algebra-Prüfung.
- `REVIEW.md`: separate Gegenprüfung und Geltungsgrenzen.
- `source_manifest.json`: Pins der hier verwendeten Originale und Tasks-Auszüge; `manifest.json`: Hashes der ausgelieferten Dateien.

Der Theoriegraph wurde als Suchkarte genutzt; sein vorhandener Snapshot meldete Hash-Drift. Maßgeblich waren deshalb die aktuellen Originaldateien. Zwei noch laufende Tasks („Extrahiere TFPT-Minimalkern“, „Untersuche TFPT-Feldsignale“) lieferten beim Abruf keine auswertbare aktuelle Abschlussantwort; ihnen wird hier kein neues Ergebnis zugeschrieben. Es wurde kein Ledger- oder Paperstatus hochgestuft.
