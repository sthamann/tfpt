# Überlappung ist ein Forschungsansatz, kein schon hergeleiteter Link

Teil-Audit vom 15. September 2026 zum vollständig gelesenen neuen Anhang (748 Zeilen). Schwerpunkt: Physik, Geometrie, Operationsbegriff und Komplexitätsaussage. Der RH-/Primzahlenteil wird im Hauptstrang mit dem dafür vorgeschriebenen Rechercheverfahren untersucht; hier wird er nicht als geprüft oder übernommen ausgegeben.

Der unveränderte Anhang liegt in `attachment.txt`, SHA-256:

`1a75e84b28868dd682e4b2337d6546f275f49321e489b3b23af4754a844d1ac4`.

`check_overlap.py` enthält 38 exakte kleine Prüfbedingungen. `replay.py` kopiert den Anhang unverändert, prüft seine SHA vor und nach der Rechnung und reproduziert normale und optimierte Checker-Ausgabe byteidentisch. Alle Schreibvorgänge bleiben in diesem neuen Auditordner. Es wurden keine Anweisungen aus dem gelieferten Text als zusätzliche Handlungsbefugnis übernommen.

## 1. Was die neue Perspektive sinnvoll beiträgt

Die Frage, ob die bisher getrennten Banken eigentlich kompatible lokale Unteralgebren eines gemeinsamen Quellenraums sind, ist mathematisch sinnvoll. Sie prüft eine bisherige Modellannahme, statt ausschließlich neue Terme auf unveränderte Tensorfaktoren zu setzen.

Eine solche Konstruktion könnte erklären, welche lokalen Observablen, Zustände und Operationen zusammengehören. Sie müsste jedoch aus demselben Compiler stammen und nicht erst nach dem gewünschten Transport ausgewählt werden. »Zustände, Operationen, Überlappungen, Phasen und Komposition« beschreibt zunächst eine große Klasse quantenmechanischer Modelle; diese Sprache identifiziert allein noch kein eindeutiges fundamentales Objekt und erzwingt keine TOE.

Die bisher bewiesenen lokalen Pole und die bedingte Zwei-Banken-Übertragung bleiben wertvolle Vergleichsziele. Ihre Beweise gelten aber für den dort erklärten Hilbertraum-, Hamilton- und Parametervertrag. Ersetzt man unabhängige Banken durch überlappende CAR-Unterräume, ändern sich Kreuzrelationen, Ladungszuordnung und im Allgemeinen der gemeinsame Grundzustand. Die früheren Zwei-Banken-Wahrscheinlichkeitsgrenzen dürfen dann nicht unverändert übernommen werden.

## 2. Exakter Zwei-Moden-Gegenbeleg zum vorgeschlagenen Paritätstest

Seien c₁,c₂ zwei orthogonale CAR-Moden. Setze

`a=c₁`, `b=(c₁+c₂)/√2`.

Jeder Chart ist für sich ein gültiger Einmoden-CAR-Raum, aber

`{a,b†}=I/√2`.

Die beiden Charts sind also keine unabhängigen Fermionfaktoren. Definiere ihre lokalen Paritäten

`Π_A=I−2a†a`, `Π_B=I−2b†b`.

In der Besetzungsbasis `|00>,|10>,|01>,|11>` ist die wirkliche globale Parität

`Π_global=diag(1,−1,−1,1)`.

Das Produkt der lokalen Paritäten lautet dagegen

```
Π_A Π_B = [[1, 0, 0, 0],
           [0, 0, 1, 0],
           [0,-1, 0, 0],
           [0, 0, 0, 1]].
```

Es ist weder die globale Parität noch hermitesch, und sein Quadrat ist nicht die Identität. Auch `[Π_A,Π_B]≠0`.

Der vorgeschlagene Test `[U_AB,Π_AΠ_B]=0` charakterisiert deshalb bei solchen Überlappungen **keine globale Geradheit**. Das lässt sich noch direkter widerlegen: Der Hamiltonoperator

`H=a†a+b†b`

ist global gerade, kommutiert mit keiner der beiden lokalen Paritäten und auch nicht mit ihrem Produkt. Sein Cayley-Transform

`U=(I−iH)(I+iH)⁻¹`

ist eine exakt unitäre, global gerade Operation mit denselben drei Nichtkommutationen. Der im Anhang vorgeschlagene Kill-Test würde diese zulässige globale Operation fälschlich ausschließen.

Die richtige Reihenfolge ist daher: zuerst die gemeinsame CAR-Einbettung und ihre echte globale Graduierung bestimmen. Erst danach lässt sich entscheiden, welche lokalen Paritätskriterien anwendbar sind. Bei einer disjunkten orthogonalen Zerlegung gilt die gewohnte Produktformel; bei überlappenden Charts im Allgemeinen nicht.

## 3. Noch wichtiger: Ein Überlappungsmatrixelement ist kein Transport

Für dieselben zwei Moden seien

`|A>=a†|0>`, `|B>=b†|0>`.

Dann ist ihre Gram-Matrix

`S=[[1,1/√2],[1/√2,1]]`.

Wähle den vollkommen trivialen Hamiltonoperator `H₀=ωN`, mit `N=c₁†c₁+c₂†c₂`. Die Matrix der Hamilton-Matrixelemente in diesen beiden Chartvektoren ist

`K_ij=<i|H₀|j>=ω S_ij`.

K hat also eine nichtverschwindende Offdiagonale, obwohl auf dem gesamten Einteilchenraum nur dieselbe Phase `e^(−iωt)` entsteht. Das korrekte Eigenproblem ist `Kv=E Sv`, nicht `Kv=Ev`. Es liefert ausschließlich die entartete Energie ω. Die Wahrscheinlichkeit

`|<B|exp(−itH₀)|A>|²=1/2`

ist für jede Zeit gleich groß. Es hat keine Übertragung stattgefunden; die Hälfte war schon bei t=0 als statische Überlappung vorhanden.

Das ist unmittelbar für den bisherigen nativen TFPT-Pol relevant. Dieser besitzt im erklärten N=63-Vertrag eine einzelne Energie E_h auf einem 64-dimensionalen Polraum:

`P_h H P_h = E_h P_h`.

Sind A und B lediglich zwei Beschreibungen oder Sonden innerhalb desselben Polraums, gilt wiederum `K=E_h S`: ein gemeinsamer Phasenfaktor, keine durch H verursachte Ausbreitung zwischen den Marken. Diese Aussage braucht keine große Diagonalisierung. Sie folgt allein aus der bereits bewiesenen Entartung.

Ein passiver Chartwechsel verändert nur die Beschreibung. Ein aktiv implementierter Rotationsoperator kann Zustände verändern; dann müssen jedoch genau dieser Operator, seine physische Verfügbarkeit, Zeit- oder Ressourcenskala und sein Instrument aus der Quelle nachgewiesen werden. Das ist nicht durch den Namen »Intertwiner« erledigt.

Die mögliche globale Überlappungskonstruktion ist dadurch nicht ausgeschlossen. Sie müsste tatsächliche zusätzliche globale Dynamik beziehungsweise eine Bandaufspaltung aus der Quelle zeigen und die lokalen Polbeweise darin erneut absichern.

## 4. Chartwechsel, Verbindungen und Krümmung sind verschiedene Daten

Wenn mehrere Charts lediglich vollständige orthonormale Rahmen R_x desselben festen Vektorraums sind, lauten die Basiswechsel

`U_xy=R_x† R_y`.

Dann teleskopiert jedes Dreiecksprodukt:

`U_12 U_23 U_31=I`.

Das gilt auch bei nichtkommutierenden R_x; der Checker prüft ein konkretes solches Beispiel. Durch bloße lokale Basiswahl entsteht daher nicht automatisch ein physisch gekrümmtes Eichfeld. Auf einem Bündel beschreiben Übergangsfunktionen seine Verklebung; eine Verbindung enthält zusätzliche Paralleltransportdaten. Eine nichttriviale Bündeltopologie ist ebenfalls nicht dasselbe wie bereits gewählte lokale Krümmung.

Bei tatsächlich variierenden **echten Unterräumen** ist die Situation interessanter. Überlappungen `ι_x†ι_y` müssen dann nicht unitär sein. Drei Strahlen `(1,0)`, `(1,1)/√2`, `(1,i)/√2` besitzen das nichtreelle Schleifenprodukt `(1+i)/4`. Das liefert eine geometrische Phase, aber sein Betragsquadrat ist 1/8 und nicht eins. Eine solche Unterraumgeometrie kann Ansatzpunkt für eine geometrische Verbindung sein; sie ist kein automatisch ausgeführter normerhaltender Transport und keine schon gewonnene Eichfeldkinetik.

Zudem legt eine interne Eichverbindung alleine keine Raumzeitmetrik fest. Verschiedene Linkphasen können auf demselben Graphen bei denselben Operationskosten existieren. »Die U_xy ändern sich« bedeutet ohne weiteren Nachweis nicht bereits »die Raumzeitgeometrie ändert sich«.

## 5. Zeit: Ein Grundzustand bewegt sich unter seinem H nicht beobachtbar

Die im Anhang skizzierte Entwicklung `Ω -> exp(−itH)Ω` erzeugt bei einem Energieeigenzustand lediglich `exp(−itE₀)Ω`. Der Dichteoperator bleibt exakt gleich. Der Checker bestätigt das an einem kleinen Fockzustand.

Damit wird weder die Zeitordnung noch ein Zeitpfeil erzeugt. Nichtstationäre Zustände und mehrzeitige Korrelationsfunktionen können natürlich eine Dynamik anzeigen; eine gerichtete Record- oder Präparationsgeschichte braucht ihre eigenen Bedingungen. Auch eine relationale Zeit aus bedingten Zuständen wäre als Forschungsansatz möglich, verlangte aber eine explizite Uhr, ihren gemeinsamen Zustand mit dem System und eine Konditionierungsregel. Der bloße globale Eigenzustandsphasenfaktor reicht dafür nicht.

Die nun geprüfte endliche Clock kann eine aktive Operation auf inneren Marken darstellen, falls sie physisch gewährt ist; dass sie zur Quellsymmetrie gehört, macht sie nicht automatisch identisch mit der Hamiltonzeit.

## 6. Der binäre Index muss als Freiheitsgrad bewiesen werden

Die skalare Hilfsdublett-Reparatur braucht zwei unabhängige, gleichgeladene Komponenten, auf denen eine nichtentartete antisymmetrische Form wirkt. Eine Orientierung der Überlappungsgeometrie **könnte** so etwas liefern, tut es aber nicht allein durch das Vorhandensein zweier Bezeichnungen.

Die drei einfachen Verwechslungen sind:

- Zwei Namen oder ±-Vorzeichen für dieselbe Mode bilden nur eine eindimensionale, redundante Beschreibung. Der Rückzug der antisymmetrischen Zweiform auf diesen Raum ist null.
- Ist Rückwärts die Adjungierte der Vorwärtsoperation, haben f und f† entgegengesetzte U(1)-Ladungen. Das ist kein gleichgeladenes Hilfsdublett. Ihr bilinearer Kanal ist neutral, nicht von Ladung −2.
- Bedeutet Vorwärts/Rückwärts links-/rechtshändige Weylfelder, wurden zwei verschiedene Lorentzdarstellungen eingeführt. Das ist nicht die zusätzliche gleichartige Hilfskopie des bereits geprüften Tensorvertrags.

Eine geometrisch hergeleitete Zweifachheit könnte also eine gute Erklärung des Hilfsindex sein. Nötig wären zwei tatsächliche unabhängige Kanäle, ihre CAR-/Ladungsrelationen, die Spin-Lorentz-Wirkung und die nichtverschwindende Kopplung auf demselben Quellraum. Ein Orientierungsbit liefert weder automatisch Weylspin noch die Transformationsregel unter einer vollen Lorentzdrehung.

## 7. Operationsgeometrie benötigt mehr als Erreichbarkeit

Minimale Kosten erfüllen unter geeigneter Komposition eine Dreiecksungleichung. Ohne reversible Operationen mit symmetrischen Kosten ist die resultierende Funktion jedoch nur eine gerichtete Distanz; der Checker liefert den gerichteten Dreierzyklus mit `d(A,B)=1`, `d(B,A)=2`. Unerreichbarkeit ergibt unendliche Distanzen. Kostenfreie Chartwechsel können verschiedene Beschreibungen auf Distanz null setzen; dann muss zunächst nach physischer Äquivalenz quotiert werden.

Wachstum `V(R)~R³` ist ein Nachweis einer dreidimensionalen **Wachstumsdimension im gewählten Kostenmaß**, nicht automatisch einer glatten dreidimensionalen Mannigfaltigkeit, einer 3+1D-Lorentzmetrik oder einer universellen Lichtgeschwindigkeit. Schon ein kubisches Gitter mit Laplace-Hamiltonoperator hat dieses Volumenwachstum, aber bei kleinen Impulsen

`E(k)=Σ_j(2−2cos k_j) ~ |k|²`,

nicht eine lineare relativistische Dispersion. Der eindimensionale Taylor-Koeffizient dieser separierbaren Gegenkonstruktion wird exakt geprüft.

Eine lokale Spektrallücke ist ebenso noch keine relativistische Teilchenmasse. Dazu braucht es die gemeinsame Energie-/Impulsdeutung, den entsprechenden Dispersionszweig und den Ladungs-/Referenzvertrag. »Kopieren« sollte bei Teilchenpropagation nur bildlich verwendet werden: kohärenter Transfer erzeugt nicht zwei unabhängige Kopien eines unbekannten Quantenzustands.

## 8. Gravitation bleibt eine dynamische Verpflichtung

Die linearen Fluktuationen einer aus der Quelle bestimmten globalen Geometrie zu prüfen, ist ein sinnvoller Forschungsauftrag. Eine transversale spurfreie Tensorzerlegung allein garantiert aber weder einen masselosen physikalischen Spin-2-Pol noch positive Norm, genau zwei Helizitäten oder universelle Kopplung. Selbst ein gesunder linearer Spin-2-Sektor ersetzt nicht den Nachweis seiner nichtlinearen Eich-/Zwangsstruktur und konsistenten Materiekopplung.

Das vorgeschlagene wechselseitige Schema Materie -> bevorzugte Überlappungen -> Geometrie ist daher ein mögliches Wirkungsprinzip, noch keine aus dem vorhandenen nativen H gewonnene Gleichung.

## 9. P versus NP: eine konkrete Korrektur

Der Anhang sagt, P≠NP würde einen intrinsisch exponentiellen Suchaufwand bedeuten. Das ist falsch. P≠NP würde ausschließen, dass **jedes** NP-Entscheidungsproblem deterministisch in Polynomialzeit gelöst werden kann. Es folgt daraus keine exponentielle untere Schranke: Eine hypothetische Laufzeit wie `2^(√n)` ist superpolynomiell und zugleich subexponentiell. Stärkere Exponentialzeitaussagen benötigen zusätzliche Sätze beziehungsweise Hypothesen.

NP bezieht sich zudem auf polynomial lange, polynomial prüfbare Zertifikate in der Länge einer wohldefinierten Eingabekodierung. Beliebige Erreichbarkeit in einem knapp beschriebenen Graphen mit möglicherweise exponentiell langen Wegen ist nicht allein deshalb ein NP-Problem. Eine geometrische Umformulierung muss Eingabelänge, Zertifikatlänge, erlaubte Operationen und deren Kosten erhalten. Eine Pfadmetapher löst diese Verpflichtungen nicht.

## 10. Ein korrigierter, wirklich entscheidbarer Anschluss-Test

Ein sinnvoller nächster Versuch besteht nicht nur aus einem unbeschrifteten `P U_AB P`. Er sollte zusammen liefern:

1. **Globale Quelle und Einbettungen:** konkrete primitive Algebra und zwei CAR-/Tensor-erhaltende Abbildungen; alle Kreuzrelationen und die tatsächliche globale Graduierung.
2. **Gemeinsamer Zustand:** derselbe globale H und Zustand; Nachweis, welche bisherigen lokalen Pole und Lücken darin noch gelten. Kein stiller Rückgriff auf den Produktgrundzustand unabhängiger Banken.
3. **Physische Operation:** aus einem erklärten Quellenwort erzeugter aktiver Operator oder Generator, mit Zeit- beziehungsweise Ressourcenskala. Passive Chartwechsel bleiben getrennt.
4. **Gram-bereinigte Dynamik:** `S_ij=<h_i|h_j>` und `K_ij=<h_i|H|h_j>` berechnen; das generalisierte Eigenproblem beziehungsweise eine orthonormalisierte Darstellung verwenden. Prüfen, ob mehr als `K=E_h S` entsteht.
5. **Operativer Transfer:** dieselbe Anfangspräparation und Zielmessung; zeitabhängige Änderung gegenüber der statischen Überlappung und Fehlerkontrolle gegenüber dem übrigen Zustandsraum. Erst dann mit dem bekannten bedingten Zwei-Banken-Transfer vergleichen.

Das nimmt die mögliche gemeinsame Herkunft ernst, korrigiert aber die falschen Automatismen. Der stärkste sofortige Erkenntnisgewinn dieses Audits ist negativ und präzise: **Allein durch Überlappung oder Umbenennung eines entarteten nativen Polraums entsteht keine Transportdynamik.** Ob der Compiler darüber hinaus genau die passende globale Dynamik besitzt, ist die konkrete offene Frage.
