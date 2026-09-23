# TFPT: stabile Rekonstruktion aus niedrigen Ladungssektoren

21. September 2026 · Fortsetzung des Einzustandssatzes und der eingereichten Ereignis-/Kinetikrechnung

## Forschungsfrage

Der verlangte Endpunkt ist die vollständige gemeinsame physische Herleitung von TFPT. Die aktuelle Rechnung bearbeitet die erste offene Verbindung: Wählt die primitive Quelle auf denselben kanonischen Feldern deren Kinetik und genau die native Paarumwandlung aus? Eine stärkere Rekonstruktion des Zielgenerators ersetzt diese Herkunft nicht.

## Ergebnis der unabhängigen Fortsetzung

Die eingereichte Stabilitätsidee trägt unter ihrer globalen Voraussetzung. Daraus folgt neu ein vollständiger Rekonstruktionssatz innerhalb der genannten Klasse aus den Sektoren Q≤4, einschließlich einer positiven Formel D₄=D_F. Außerdem muss der Wert 349/120 bei allgemeiner Kinetik durch eine exakt bestimmte positive Varianz ergänzt werden. Die direkten nativen W-Rechnungen einschließlich der mindestens 33 Krylovrichtungen sind unabhängig bestätigt.

Der ursprüngliche Quellenbestand wurde auf das nun erforderliche infinitesimale Ereignisgesetz geprüft. Der stärkste geladene Tensor und der stärkste rohe Zeittransfer liegen noch auf verschiedenen, nicht gemeinsam identifizierten Feldräumen. Der Quellenwert D₄=0 und die nichtverschwindende Kopplung sind daher weiterhin nicht hergeleitet. Gesamtverdict: **PARTIAL**, Forschungs-ID **UR.SOURCE.LOWQ.01**.

## 1. Die Stabilitätsforderung hat eine konkrete neue Konsequenz

Angenommen werden endlich viele kanonische Fermion- und Bosonmoden auf dem vollen irreduziblen Fockraum, ein selbstadjungierter, stark Q=N_f+2N_b-erhaltender H und die globalen unteren Antworten

\[
\{[f_i,H],f_j^\dagger\}=h_{ij}I,
\qquad [[b_A,H],b_B^\dagger]=\Omega_{AB}I,
\]

mit hermiteschen Zahlenmatrizen h und Ω. Sämtliche Identitäten gelten auf dem gemeinsamen invarianten algebraischen Teilchenkern. Nach Abzug der quadratischen Operatoren erzwingt der bisherige Rekonstruktionssatz

\[
H=cI+d\Gamma_f(h)+d\Gamma_b(\Omega)
+\sum_{m=1}^{32}(T_m+T_m^\dagger),
\quad
T_m=\sum_{|\alpha|=m,\,|I|=2m}C_{\alpha I}(b^\dagger)^\alpha f_I.
\]

Wenn zusätzlich eine gemeinsame untere Energieschranke auf dem gesamten Fockraum gilt, verschwinden alle T_m mit m≥3. Der höchste solche Term würde entlang einer bosonischen kohärenten Amplitude r z wie r^m wachsen. Sein nichtverschwindender hermitescher Fermionkoeffizient hat Spur null und damit eine negative Richtung. Diese dominiert die freie Energie O(r²). Der Algebraaudit behandelt den Schritt vom kohärenten Vektor zu endlich besetzten Kernvektoren ausdrücklich.

Es bleibt deshalb

\[
\boxed{H=cI+d\Gamma_f(h)+d\Gamma_b(\Omega)+T_1+T_1^\dagger+T_2+T_2^\dagger.}
\]

Das ist ein Satz in dieser Antwortklasse, kein allgemeines Verbot höherer QFT-Wechselwirkungen. Stabilität in nur einem festen Q-Sektor reicht nicht: Solche Sektoren sind endlichdimensional. Die Schranke muss über alle Sektoren gemeinsam gelten. Auch eine lediglich eichinvariante eingeschränkte physische Zustandsmenge darf nicht mit dem vorausgesetzten vollen Fockraum vertauscht werden.

## 2. Der gesamte Umwandlungstest lässt sich auf Q=2 und Q=4 verlagern

Sei P_{b,f} der Projektor auf b Bosonen und f Fermionen. In normierten Besetzungsbasen definieren wir

\[
C_1=P_{1,0}HP_{0,2},\qquad C_2=P_{2,0}HP_{0,4}.
\]

C₁ ist der vollständige einfache Umwandlungstensor; C₂ ist der vollständige direkte Doppelumwandlungstensor. Die quadratische Kinetik trägt zu diesen rechteckigen Blöcken nichts bei. Mit dem vorhandenen W und ||W||²_HS=480 folgt

\[
g_4=\frac{\langle W,C_1\rangle_{\rm HS}}{480},
\qquad
\boxed{D_4=\|C_1\|_{\rm HS}^2-
\frac{|\langle W,C_1\rangle_{\rm HS}|^2}{480}
+\|C_2\|_{\rm HS}^2\ge0.}
\]

Unter den genannten globalen Voraussetzungen gilt

\[
D_4=0\quad\Longleftrightarrow\quad
H=cI+d\Gamma_f(h)+d\Gamma_b(\Omega)+g_4X+\bar g_4X^\dagger.
\]

Außerdem ist D₄ exakt gleich dem bisherigen D_F am vollbesetzten Fermionzustand. Die verschiedenen Umwandlungsmonome erzeugen aus F orthogonale Loch-/Bosonzustände. Ihre Normen entsprechen genau den Matrixelementnormen in C₁ und C₂, einschließlich der Bosonfaktoren α!. Man benötigt den Zustand Q=64 daher nicht als physischen Prüfzustand, sofern die beiden globalen Antworten und die globale Stabilität anderweitig bewiesen sind.

Auch die quadratischen Anteile sind aus niedrigen Sektoren lesbar: c aus Q=0, h aus dem Einfermionblock, Ω aus dem Einbosonblock nach Abzug von c. Der vollständige Generator ist in dieser eingeschränkten Klasse somit durch seine Einschränkung auf Q≤4 bestimmt.

Die Einschränkung auf die Klasse ist tragend. Ein zusätzlicher positiver Operator κ1_{N_f≥5} mit κ>0 ist auf Q≤4 unsichtbar und erhält Semibeschränktheit, verletzt jedoch im Allgemeinen die globalen unteren Antwortidentitäten. Diese Identitäten dürfen nicht durch Kontrollen nur in niedrigen Sektoren ersetzt werden.

Q=N_f+2N_b ist hier die erhaltene Fockzahl; eine Identifikation mit elektrischer Ladung wird nicht vorgenommen. Kleine Q-Sektoren sind außerdem nicht automatisch die energetisch tiefsten Zustände.

Die geringe maximale Ladung bedeutet nicht geringe Matrixgröße: C₂ hat im nativen Modenraum 1830 Zeilen und 635376 Spalten. Eine explizite Vollmatrix wird hier nicht aufgebaut. Der Satz komprimiert den Beweisauftrag, nicht automatisch seine Rechenkosten.

## 3. Die Quelle muss eine erste Ableitung liefern

Für einen unabhängig hergestellten Quellentransfer T(τ)=exp(−τ(H−aI)) sind die entsprechenden Blöcke K₁(τ) und K₂(τ) direkt aus denselben Projektoren definiert. Auf den endlichen Sektoren gilt

\[
C_1=-K_1'(0),\qquad C_2=-K_2'(0).
\]

Das Herkunftsziel lautet daher konkret: Die erste Ableitung des Q=2-Blocks muss −gW liefern, die erste Ableitung des direkten Q=4-Doppelblocks muss verschwinden. Wenn diese Bedingungen und die globalen Voraussetzungen gelten, bestimmt derselbe Generator auch die vollständige wiederholte Zeitentwicklung.

Ein verschwindender direkter Q=4-Block verbietet seine spätere Besetzung nicht. Für den nativen Generator lautet dessen Beginn

\[
K_2(\tau)=\frac{\tau^2g^2}{2}P_{2,0}X^2P_{0,4}+O(\tau^3).
\]

Die Gegenfamilie H_η besitzt hingegen bereits einen linearen Anteil in τ. Die Zahl 439680 bezeichnet die Norm derselben erreichbaren Richtung, nicht dieselbe elementare zeitliche Ausführung.

Komposition und zeitliche Reflexionspositivität ergänzen dieses Herkunftsgesetz nicht automatisch: Jeder stabile H_η erzeugt nach Energieverschiebung eine positive Kontraktionshalbgruppe. Ihre reflektierte Zeitkernelmatrix ist eine Gram-Matrix und daher positiv. Das ist ausdrücklich kein vollständiges räumliches OS-Modell und kein Gegenbeweis gegen alle P1/P2-Bedingungen. Der vollständige Beweis und die genaue Grenze stehen im Transferbericht.

## 4. Kinetik verändert den skalenfreien Momententest

Für den skalaren nativen Vertrag bestätigt die Rechnung die angegebenen ersten Momente und I_F=349/120. Diese Zahl darf jedoch nicht unverändert auf beliebige h und Ω übertragen werden.

Setze K=dΓ_f(h)−tr(h)I+dΓ_b(Ω), v=XF und v̂=v/√480. Bei bereits nativer Umwandlung, g≠0 und sonst denselben Voraussetzungen gilt

\[
\boxed{\mathcal I_F=\frac{349}{120}
+\frac{\operatorname{Var}_{\widehat v}(K)}{480|g|^2}.}
\]

Die Zahl 349/120 ist damit eine Untergrenze in dieser erweiterten Klasse. Gleichheit gilt genau dann, wenn Kv in derselben Richtung wie v bleibt. Die zusätzliche Varianz misst die kinetische Mischung des nativen Paarkanals. Sie ist keine zusätzliche Doppelumwandlung; D_F kann gleichzeitig null sein.

Der Unterschied ist wichtig für die Gesamtarchitektur: Ein Quellenkandidat mit echter räumlicher Kinetik darf nicht allein deshalb verworfen werden, weil seine Momente vom skalaren Einbankwert abweichen. Umgekehrt kann die Gleichheit als zusätzliche Verträglichkeitsbedingung zwischen Kinetik und W geprüft werden, wenn sie unabhängig aus der Quelle vorliegt.

## 5. Herkunft und verbleibender Gesamtabschluss

Der Quellenbericht prüft den ursprünglichen Transferbestand und die stärksten positiven geladenen Anschlüsse. Im geprüften Bestand liefert der finite OS-/Nahtansatz H_seam=dΓ(−log T) eine freie Kinetik auf seinem eigenen Raum. Der affine E8-Kubikzweig liefert getrennt den markierten Kopplungskandidaten. Die vorhandene primitive Viergenerator-Ereignisregel nimmt explizit zusätzlich an, dass Produkte nur sequenziell auftreten; diese Annahme ist dort nicht aus P1/P2 hergeleitet. Sie kann deshalb nicht als schon bewiesene Auswahl von C₂=0 übernommen werden.

Die bloße Existenz von W als normierter affiner Kubikkoeffizient liefert noch keine kanonischen C₁/C₂-Blöcke derselben Quellenzeit. Ein passend definiertes exp(−τH_W) würde das verlangte Resultat einsetzen.

Weder h, Ω, g noch C₂=0 sind hier aus der primitiven TFPT-Quelle ausgewertet. Die Weiterführung liefert eine strengere und kleinere hinreichende Rekonstruktionsaufgabe, aber keine zusätzliche physische Ausgangsannahme, die diese Werte ohne Beweis festsetzt.

Die physischen T1–T8-Gates bleiben offen. Die gemeinsame lokale chirale Theorie, ihr kontrolliertes wechselwirkendes Kontinuum, alle Kopplungen, Quantengravitation und kosmologische Zustandsauswahl bleiben Bestandteile desselben verlangten Gesamtabschlusses. Keine Ledger- oder Paper-Promotion.

## 6. Nachweise und Reproduktionsumfang

Der Algebraaudit enthält den allgemeinen Stabilitäts-/Kernsatz und seine Voraussetzungen. Ein exakter kleiner Focktest prüft die Rückgewinnung sämtlicher Koeffizienten, D₄=D_F und den Unterschied von H und H²; er beweist nicht durch Enumeration den unendlichen Stabilitätssatz.

Der separate native Audit verwendet den tatsächlichen W-Tensor: X†XF=480F, X†X²F=916XF und ||X²F||²=439680 werden als vollständige sparse Vektoridentitäten bestätigt. Für die Summe der 60 antisymmetrischen Paarmatrizen ergibt sich exakt det(Σ_A Q_A)=5³². Damit ist X^mF≠0 bis m=32 und der native Krylovraum hat bei g≠0 mindestens 33 Dimensionen.

Im nichtskalaren Beispiel h=diag(1,0,…,0), Ω=I₆₀ ergibt das tatsächliche W eine kinetische Varianz 31/1024. Bei g=1 ist I_F=285907/98304 statt 349/120; die native Umwandlung selbst ist unverändert.

Die Berichte und gezielten Replays werden mit gepinnten Eingaben geliefert. Der Quellenaudit ist eine Originaltextprüfung, keine neue Quellenmessung. Eine Vollsuite, ein Kontinuumsnachweis und ein vollständiges physisches TFPT-Schwingerfunktional wurden nicht erzeugt.
