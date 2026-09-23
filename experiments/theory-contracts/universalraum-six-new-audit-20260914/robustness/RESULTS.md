# Robustheit v1.6: Filterkomposition, Leakage und unbedingte Fehlerbilanz

14. September 2026. Eigene unabhängige Prüfung und Fortsetzung im deklarierten
endlichen Modell. Keine Herkunfts-, Kontinuums- oder TOE-Promotion.

**Anschließender stärkerer Fortschritt:** `RESULTS_COUPLED.md` beweist für die neue
Quelle ξ die Identität P−03ξ=−√(3/8)Ω. Ihre Präparation gelingt damit durch einen
einzigen v1.5-Record exakt. Die folgenden F4/F9/F10-Ergebnisse bleiben als
Kompositionsprüfung der gelieferten Filterbehauptungen gültig; sie sind nicht
mehr der einfachste hier gefundene Präparationsweg. Der Folgebericht enthält auch
den stärkeren T1-Ressourcenabstand 15/64 und den konkreten quadratischen
Zwischenzellfehlerbound.

## 1. Ein neuer wichtiger Kompositionsfehler und seine konkrete Reparatur

Die optimale Stabilizerquelle σ aus `BEWEISE.md` ist mit dem 9-Faktorfilter aus
`neu_1.md` **nicht unmittelbar kombinierbar**. Die vollständige ganzzahlige Rechnung
auf 256 Materiedimensionen gibt für die M-Sektoren 0 bis 6 exakt

\[
(\langle P_0\rangle,\ldots,\langle P_6\rangle)_\sigma
=(3/8,0,0,1/2,0,0,1/8).
\]

Der neue Eingang besetzt also den ausgelassenen M=6-Sektor. Bei t/Δ=1/20 lässt
F9 samt Leerbelegungsherald diesen Sektor mit Wahrscheinlichkeit
0.04943867685840455 passieren. Für den normierten σ-Eingang ergibt das:

Die nachgelieferte Datei `TFPT_Universalraum_Forschungsfortsetzung_2026-09-14.md`
führt in Abschnitt 3 einen anderen, mit sechs CNOT erzeugbaren Maximierer ξ ein.
Seine dort ausgeschriebene 16-Wort-Formel ergibt unabhängig geprüft **dieselben
sieben M-Gewichte**. Alle nachfolgenden Filterfehler und Reparaturen gelten daher
auch für ξ. Die vollständige neue Datei wird hier nicht als gesamthaft geprüft
ausgegeben; betrachtet wurden ihre Ziel-/Quellenformel und Schaltung in Abschnitt 3.

| Vollständiges Rohereignis | Gewicht |
|---|---:|
| Akzeptiert und im Ziel Ω | 0.36430949541840213 |
| Akzeptiert, aber orthogonal zu Ω | 0.006179834607300569 |
| Insgesamt akzeptiert | 0.3704893300257027 |
| Bedingte Infidelität | **0.016680195909749524** |

Das ist keine Rundungsresidue. Die naive Kombination hätte etwa 1,67 %
Präparationsinfidelität statt einer exakten Präparation.

Eine konkrete Reparatur ist ein zusätzlicher Faktor für die Energie E=0 des
nackten M=6-Sektors:

\[
F_{10}=F_9\,\frac{I+\exp[-i\pi(H-E_0)/(-E_0)]}{2}.
\]

Dieser gemeinsame Start-/Endfilter funktioniert auf dem erweiterten
**387-dimensionalen** H-invarianten Raum: 352 alte Dimensionen plus 35 nackte
M=6-Dimensionen. Der M=6-Sektor hat keinen angekoppelten hohen Partner.
Die idealen Rohgewichte sind wieder 3w²/8 für die Präparation sowie 3w⁴/8 bzw.
51w⁴/256 für behaltenen/frischen Record; bedingt nach erfolgreicher Präparation
ist der Zustand Ω. Beliebige Störungen oder zusätzliche Record-Wörter sind damit
weiterhin nicht automatisch eingeschlossen.

Für **ausschließlich den idealen σ-Präparationseingang** reichen sogar vier
Löschfaktoren: E−(3/2), E+(0), E+(3/2) und 0. Das ist ein separater Startfilter;
er ersetzt nicht den gemeinsamen Start-/Endfilter. Eine bewusst unterschiedliche
F4-Start-/F9-Endkombination ist beim festgelegten idealen Echo ebenfalls möglich.

| Vertrag | Zeit eines Filters in ℏ/Δ | Start + Ende in ℏ/Δ |
|---|---:|---:|
| F9 für alte ideale Quelle χ/Echo | 2310.3049402665933 | 4620.609880533187 |
| F10 gemeinsam für σ/Echo | 2522.840282102928 | 5045.680564205856 |
| Unterschiedliche F4-σ-Präparation / F9-Endprüfung | 646.8490732327522 / 2310.3049402665933 | **2957.1540134993456** |
| F11 nach zusätzlichem Einschluss beider M=2-Partner | 2957.1984605666485 | 5914.396921133297 |
| F13 auf dem ganzen 544D-Sternraum | 3172.829633999998 | 6345.659267999996 |

Die F11-Zeile erweitert den ursprünglichen F9-Vertrag um M=2, nicht zugleich
um den für σ nötigen M=6-Sektor. Alle Zeiten zählen nur die kontrollierten
Hamiltonentwicklungen; Puls-, Mess-, Reset- und Wiederholungskosten kommen hinzu.
Auch die stärkere Filteroptimierung leitet kontrolliertes H nicht aus TFPT her.
Der v1.5-Recordweg über K^n benötigt diese Spektralfilter überhaupt nicht.

## 2. Der 352D-Raum ist H-invariant, aber nicht record-invariant

Die Quellenaussage für die fünf festgelegten Vektoren χ, Ω, z=C†S01CΩ und
B±Ω ist korrekt: Alle haben exakt Gewicht null in M=2 und M=6. `probe.py`
konstruiert die rationalen Spektralprojektoren durch

\[
P_j=\prod_{k\ne j}\frac{M-kI}{j-k},\qquad
M=3I+S_{01}+S_{02}+S_{03},
\]

und prüft Idempotenz, Identitätsauflösung und sämtliche Quellgewichte mit ganzen
Zahlen. Die Ränge sind (1,30,45,40,15,90,35). Für diese idealen Start- und
Endvektoren bleibt F9 exakt; reine Zeitfehler in Funktionen desselben H verändern
ihre Spektralstütze ebenfalls nicht. Damit wird die eingegrenzte Behauptung aus
`neu_1.md` bestätigt, nicht widerlegt.

Die stärkere generelle Schließung scheitert bereits ohne Rauschen. Setze
v=P5|0001>/||P5|0001>||, einen erlaubten nackten Eingang. Dann gilt exakt:

| Operation auf v | M=2-Gewicht nach Swap | Rohgewicht im M=2-Sektor je Recordausgang ± |
|---|---:|---:|
| Kante 01 | 2/9 | 1/18 |
| Kante 02 | 2/9 | 1/18 |
| Kante 03 | 8/9 | 2/9 |

Die letzte Spalte zählt unnormierte Zweige P±v. Ein ungelesener 03-Record erzeugt
somit insgesamt **4/9** M=2-Gewicht. Das Gegenbeispiel liegt im behaupteten
Eingangsraum, auch wenn es nicht einer der fünf eingefrorenen Idealvektoren ist.

Ebenso gibt es einen konkreten normierten nichtkommutierenden Fehlergenerator:

\[
V=Z_{\mathrm{Bit0},0}Z_{\mathrm{Bit1},1}Z_{\mathrm{Bit0},2},
\quad V^2=I,\quad [V,M]\ne0,\quad
\langle\Omega|V|\Omega\rangle=0,\quad \|P_2V\Omega\|^2=4/9.
\]

Es handelt sich um ein Produkt gewöhnlicher Pauli-Z auf drei Trägern in der
Achtqubitkodierung. Unter exp(−iαV) wird exakt 4sin²α/9 Gewicht in M=2 erzeugt.
F9 plus Leerherald lässt M=2 mit Rohwahrscheinlichkeit 0.08205253533722086 durch.
Daher beträgt die falsche akzeptierte Rohmasse

\[
b=0.08205253533722086\;\frac49\sin^2\alpha.
\]

Bei α=0.01: p_acc=0.971398488479682, b=3.6466577906300703·10⁻⁶ und
1−F_cond=3.7540286853208795·10⁻⁶. Die rationale Stützbehauptung ist exakt;
die hier angegebenen Auswertungen der transzendenten Filterzeiten sind numerisch.
Die Probe stellt dazu F13 als Negativkontrolle gegenüber.

Eine programmierte Clock mit diesen Recordkanten erhält folglich nicht allgemein
I_clock⊗P_support. Für eine vorgegebene Gatterfolge U_k kann zwar der bewegte
Historyraum mit Projektor Σ|k><k|⊗V_k P_support V_k† invariant konstruiert werden.
Das ist ein anderer Raum und keine Garantie, dass der Materieeingang einer späteren
F9-Prüfung wieder im ursprünglichen Träger liegt. Completion-/Clockfehlereignisse
müssen im gemeinsamen Instrument erfasst werden.

## 3. Ein geschlossener Fehlervertrag für Rohgewichte und Konditionierung

Das neue Ergebnis geht über reine Zeittoleranzen hinaus. Man deklariert ein
vollständiges Instrument samt Recordausgängen, Helper, Reset und Erfolgsflag.
Für einen festen Eingang sei v0 dessen idealer akzeptierter Stinespringvektor,
p0=||v0||² und b0=||(I−P_target)v0||². Der ideale Fehler b0 darf positiv sein,
etwa für eine endliche K^n-Präparation. Bei gemischtem Eingang wird eine feste
Purifikation mitgeführt; P_target wirkt nur auf das Zielsystem.

Die kohärent gestörte Realisierung habe akzeptierten Vektor v mit
||v−v0||≤η. Zusätzlich weiche die vollständige Realisierung durch stochastische
Gatter-, Readout-, Reset- oder Clockfehler in halber Diamantnorm höchstens q ab.
Dabei ist diese Distanz auf dem **vollständigen spurerhaltenden Instrument mit
allen Flags**, nicht auf einem nachträglich normalisierten Erfolgszweig definiert.
Dann gelten für alle solchen Fehler gleichzeitig:

\[
|p_{acc}-p_0|\le2\sqrt{p_0}\eta+\eta^2+q,
\]
\[
p_{acc}\ge(\sqrt{p_0}-\eta)_+^2-q=:p_{\min},
\qquad b_{acc}\le(\sqrt{b_0}+\eta)^2+q,
\]
\[
\boxed{1-F_{cond}\le
\min\left(1,\frac{(\sqrt{b_0}+\eta)^2+q}{p_{\min}}\right)}
\quad\text{falls }p_{\min}>0.
\]

Bei p_min≤0 gibt der Vertrag keine informative konditionierte Garantie.
Die Formeln folgen direkt aus Dreiecksungleichung für Erfolgs-/Fehlerprojektionen;
die Distanz q ändert jede gemeinsame Effektwahrscheinlichkeit höchstens um q.
Dies ist ein analytischer Vollraumsatz, kein aus kleinen Residuen abgeleiteter Bound.

Für beliebige, auch nichtkommutierende und zeitabhängige beschränkte
Hamiltonabweichungen δH_j(t) gilt durch Duhamel plus Teleskopsumme

\[
\eta\le\eta_{in}+\sum_j\int\|\delta H_j(t)\|dt/\hbar
+\sum_j e_{gate,j}.
\]

Phasenrauschen kann als solcher zeitabhängiger Generator oder als stochastische
Kanaldistanz in q geführt werden. Timingfehler benötigen zusätzlich die tatsächlichen
Generatornormen ihrer Intervalle. Die Normvoraussetzung ersetzt keine Abschätzung
unbeschränkter Störungen; eine solche Erweiterung wird hier nicht behauptet.

Für L v1.5-Records mit vollständigen endlichen Q-Fenstern und einheitlichem
Hamiltonfehler δ ergibt sich konkret η≤L·70π·δ/Δ plus die separat bezifferten
Eingangs-/Schalt-/Controllerfehler. Symmetrische Messbitfehler f tragen höchstens
q≤Lf bei, selbst wenn die Fehlerereignisse korreliert sind, sofern jeder Schritt
auch bedingt auf die Vergangenheit denselben Fehlervertrag erfüllt.

Für den alten Basiseingang |0123>, n=20, L=60 liefern unabhängige rationale
Zustandsrechnung p0≈1/24 und b0=5.097486212119082·10⁻¹⁹. Eine gemeinsame
ausreichende Wahl ist η≤10⁻⁴ und q≤10⁻⁸. Das entspricht bei ansonsten idealem
Aufbau δ≤7.578806813899778·10⁻⁹Δ und f≤1.6666666666666666·10⁻¹⁰ pro Record.
Dann folgt **1−F_cond≤4.804741936966266·10⁻⁷**. Das ist ein konservativer
gemischter Fehlervertrag, keine gemessene Hardwaretoleranz. Bei ausschließlich
Hamiltonfehlern genügt δ≤1.5454665851634607·10⁻⁸Δ für 10⁻⁶ Infidelität.
Andere Eingänge, insbesondere σ mit deutlich weniger K-Runden, werden durch
dieselben Formeln mit ihren tatsächlichen p0,b0,L eingesetzt.

Die Notwendigkeit der Konditionierung lässt sich exakt sehen: Bei wahrem
Erfolgsgewicht 1/24 und falsch positivem Herald mit Wahrscheinlichkeit 1/1000
auf jedem Fehlzustand ist der falsche Anteil im akzeptierten Ensemble **23/1023**,
nicht 1/1000. Ein entsprechender Mutant wird im Replay verworfen.

## 4. Direkte Verbindung mit dem endlichen v1.5-Makro

Die Probe baut die gesamte 88D-Folge mit physischem Recordpointer und wiederkehrendem
|−>-Helper unabhängig neu auf. Q wird durch den erklärten endlichen Generator
π(I−Q)/2 mit Dauer ℏ/Δ und anschließendem Parken implementiert. Insgesamt entstehen
72 Zeitsegmente und die tatsächliche Dauer 70πℏ/Δ. Es werden keine Forschungsprüfer
importiert.

Als Störung in **jedem** Segment wird
δ(|00_matter><mediator01|+Adjungierte) eingesetzt, identisch auf den beiden Pointern.
Der Generator hat Norm eins, kommutiert nicht mit H und koppelt einen symmetrischen
dunklen Materiezustand an einen Vermittler. Somit wird echte Leakage getestet.

| δ/Δ | Gemessener Isometriefehler | Analytische Schranke 70πδ/Δ |
|---:|---:|---:|
| 0 | 8.86·10⁻¹⁵ | exakt 0 im analytischen Modell |
| 10⁻⁵ | 0.00019153547862394774 | 0.0021991148575128553 |
| 10⁻⁴ | 0.0019157280593497385 | 0.02199114857512855 |

Die reine Matrixresidue bestätigt nur die numerische Rekonstruktion. Der für alle
erlaubten Störungen gültige Bound folgt aus Duhamel. Die Störung ist ein deklarierter
Testgenerator, kein bereits aus TFPT hergeleitetes Rauschmodell.

Zusätzlich wird die gesamte postselektierte K^n-Präparation mit nichtkommutierendem
Pauli-Fehler vor jedem Record und falsch gelesenen Recordbits gerechnet. Der
akzeptierte Kanal eines Schritts ist ausdrücklich

\[
(1-f)P_-U_\alpha\rho U_\alpha^\dagger P_-
+fP_+U_\alpha\rho U_\alpha^\dagger P_+.
\]

Alle abgebrochenen Versuche bleiben in der Bilanz. Bei n=20, α=0.001 und f=10⁻⁵
ergeben sich p_acc=0.041633647613110975 und 1−F_cond=3.1646376019920637·10⁻⁶.
Mehr ideale Filterrunden beseitigen den laufend eingespeisten Fehler also nicht
kostenlos. Normalisierte ideale Fehler kleiner als die Gleitkommapräzision werden
aus exakter rationaler Zustandsrechnung übernommen, nicht als numerische Nullen
ausgewiesen.

## 5. Anschluss an die verschränkte Referenzfamilie

Der Satz für H_N=V_NH_0,NV_N† und Ψ_N=V_NΩ^⊗N aus `neu_1.md` bleibt ein
korrekter, explizit konstruierter Referenzvertrag. Seine globale Lücke folgt aus
Unitäräquivalenz und die Verschränkung aus den erklärten Brückengattern; eine
propagierende TFPT-Familie wird dadurch nicht ausgewählt.

Die bisher freie lokale Zykluszahl ε erhält nun einen konkreten hinreichenden
Implementierungsbound. Hat jedes der drei Records Isometriefehler ≤d_R, jede
Recordmessung halbe Diamantdistanz ≤f und die auf Fehler bedingte Resetoperation
Distanz ≤e_reset, dann genügt

\[
\varepsilon_{cyc}\le\min(1,3d_R+3f+e_{reset}),
\qquad d_R\le70\pi\delta/\Delta+e_{controller}.
\]

Das folgt durch vollständige, nötigenfalls adaptiv kontrollierte Kanäle und
Kontraktivität der Diamantnorm. Der Bound zählt keine normierten Erfolgszweige als
CPTP-Kanäle. Er setzt voraus, dass der Reset auch eventuell entstandene
Vermittler-/Helperleckage im deklarierten gemeinsamen Träger behandelt.
Beim idealen Makro R⊕I haben reine Vermittlereingänge mit frischem |0>-Record
sofort Ergebnis 0 und werden zurückgesetzt. Damit kann die ideale Zykluskontraktion
auf diesen Leckagesektor erweitert werden. Wiederverwendete Helper und Reservoirs
müssen pro Zyklus zurückgesetzt werden oder einen gleichwertigen, auch bedingt auf
die vollständige Vorgeschichte gültigen Kanalfehlervertrag erfüllen. Ein bloßer
Isometriefehler nur auf frisch initialisierten Helpern genügt nicht für unbegrenzte
Zyklen mit unkontrolliertem Speicher. Die Duhamel-Summe für eine feste komplette
kohärente Pulsfolge bleibt hiervon unabhängig gültig.

Für eine Entangling-Schaltung am Ende mit N−1 Brückengattern der jeweiligen
halben Diamantdistanz d_B folgt damit die zuvor fehlende geschlossene Bilanz

\[
\boxed{1-F_{\Psi_N}\le
\min\left(1,Nr^m+
N(3d_R+3f+e_{reset})\frac{1-r^m}{1-r}+(N-1)d_B\right).}
\]

Dabei ist r=1−a(1−β), β=(9+√17)/32 und a der tatsächliche Resetüberlapp.
Die Basis-, χ- und σ-Werte a=1/24,1/6,3/8 können eingesetzt werden. Beim
zusammengeschobenen Ablauf V_N(E^m)^⊗N V_N† werden die V-Gatter innen nicht
kostenlos vielfach gezählt; der anfängliche Decoder kann für den Worst-Case-
Konvergenzterm als beliebiger Eingang behandelt werden. Für genau vorgegebene
Eingangsvergleiche kommt seine Fehlerdistanz separat hinzu.

Das ist eine beweisbare Verknüpfung des makroskopischen Fehlerparameters mit
Hamilton-, Readout-, Reset- und Brückengatterfehlern. Sie ist konservativ, häufig
streng und bei zu großen rechten Seiten informationslos. Ein durch Leakage
unvollständig definierter Reset oder ein nicht beschränktes Bad wird dadurch
nicht automatisch geschlossen. Für den propagierenden Vielzellen-Hamiltonoperator
aus v1.5 bleibt die entsprechende native Implementierung und Rauschdomäne offen.

## Reproduktion und Negativkontrollen

`probe.py` nutzt ausschließlich Standardbibliotheken, NumPy und SciPy.
`replay.py` führt normale und `-OO`-Ausführung aus und verlangt bytegleiche JSONs.
Vier Mutanten müssen fehlschlagen: allgemeine Record-Invarianz annehmen,
Phasenreparaturen bei gleicher Gesamtdauer falsch platzieren, die Konditionierung
ignorieren und σ blind mit F9 kombinieren. Ergebnisse: `verification.json`,
`verification_optimized.json`, `replay.json`; Quellhashes und Evidenzklassen sind
gespeichert. Kein Test führt eine native Herkunfts- oder Gesamtphysikpromotion aus.
