# TFPT und Universalraum: Fünf-Quellen-Prüfung und eigene Fortsetzung v1.4

14. September 2026. Forschungsresultate, keine T1–T8-, RH- oder Komplexitätspromotion.
Diese Runde wurde **vor** dem PDF-Update gerechnet. Grundlage bleibt das vollständige
Hauptbuch v1.3. Die fünf gelieferten Texte sind als N9–N13 unverändert archiviert.

## 1. Was an den neuen Berichten trägt

| Quelle | Bestätigt / integriert | Korrektur oder Grenze |
|---|---|---|
| N9 Fable-Abschlussrunde | Standard-E8-Cocycle: F2-Ränge 45 und 285; Obstruktion für geteilte Vermittlervorzeichen; lokale F4-Zahlen; vorhandene 64-Sektor-Tabelle | Dichte Gleitkommadiagonalisierung ist kein exakter Multiplizitätsbeweis. Niedrige nackte Eigenmoden plus Rayleighkorrekturen sind keine vollständige Diagonalisierung von H2+H4. Zelllokale und kantenlokale Vermittler sind nicht identisch. |
| N10 Sol-Runde 2 | Vierfachheit bleibt numerisch; grobe Norm 1920; nichtinjizierende unitäre Vervollständigungen; begrenzte Faktor-Schnittstelle | Frühere Bandgrenze 1/640 ist für die endliche Belegungsbandtrennung durch N11 überholt. Ein Sektorausschluss aus nicht zertifizierten nackten Minima ist nur bedingt, nicht automatisch rigoros. |
| N11 Astra | Gewichteter Schurtest, Bandabstand 2Δ/5 bei 1/20; endliche Feshbachrekursion; Feedbackattraktor; dyadische Filtergrenze; ACT-Diagnose | Bandabstand ist kein innerer Gap. Kernelrest ist nicht kanonischer H4-Rest. Kontrollierte Operationen bleiben Zusatzressourcen. |
| N12 Astra hoch | Gemeinsame endliche Ausführung, statischer Pulsfehler, vollständige Rohstatistik, systematische T1–T8-Gates | Methodische Kandidaten sind keine schon konstruierten nativen Operatoren. |
| N13 Spark | Übersichts- und Quellenarbeit; unabhängige historische Wiederholungen | Zeitgebundene Statusfelder teilweise überholt. Alte Rohwerte gehören nicht zum neuesten Protokoll. Lokalität allein erzwingt keinen Kantenmodusvertrag. |

Die vorhandene 64-Sektor-Datei umfasst alle SU(4)-Sektoren mit
Σ dim(Specht) dim(SU4)=4^16. In 63 Sektoren stehen aber nur ausgewählte niedrige
nackte Moden. Die große dichte Singulettrechnung und der gesamte 64-Sektor-Lauf
wurden hier nicht neu ausgeführt. Ihr Code und die Ergebnisdateien wurden geprüft.
Die eigene neue 24.024-dimensionale Rechnung ist separat ausgeführt und unten erklärt.

## 2. Der entscheidende Architekturfehler: drei statt zwei Verträge

Bei L Clebsch-Zellen gibt es drei unterschiedliche Vermittlerarchitekturen:

1. **Eine globale Bank:** gleiche Moden über alle Zellen, 10 C(4L,2) gleichlabelige Paarterme.
2. **Eine Bank pro Zelle:** gleiche Moden innerhalb der Zelle, 60L innere Paarterme.
3. **Eine Bank pro Kante:** getrennte Moden auf jeder Kante, keine solchen disjunkten Paarterme.

Die zweite und dritte Variante sind bei fester Zellgröße und endlichreichweitiger
Zwischenzellkopplung beide lokal. Schon ohne Zwischenzellkopplung ist die zweite
Variante ein exaktes extensives Gegenmodell zur behaupteten Auswahl der dritten.
Sie behält den positiven Lückenkoeffizienten +13.901769…, während der kantenlokale
Vertrag −11.955494… besitzt. Der Unterschied ist nicht durch Umbenennung zu beseitigen.

Das quadratische Wachstum eines Störungskoeffizienten beweist außerdem nicht,
dass die volle exakte Energie in jedem Grenzprozess quadratisch wächst: Die
Entwicklung kann selbst ihre Größenuniformität verlieren. Es ist eine konkrete
Warnung vor der unnormierten globalen Bank, kein universeller Ausschluss kollektiver Modelle.

## 3. Bandtrennung und neuer kantenlokaler Satz

Für das harte C16-Modell mit Ladung Nf+2Nb=16 und |t|/Δ≤1/20 liefert der unabhängige
vollständige Ortsmengenzensus dieselben Maximalzahlen besetzter Kanten:

L(m)=(0,0,1,2,4,5,7,9,12,14,17,20,24,27,31,35,40).

Für An=Q(n+1) B† Qn und Ln=L(16−2n) gilt durch gewichteten Schurtest

||An||² ≤ 2(n+1) min(4,n+1) Ln

bei einer geteilten Bank innerhalb der Zelle. Der rationale LDL-Test bestätigt
QHQ≥2ΔQ/5. Mit PHP=0 und dim P=4^16 liefert Minmax ein niedriges Band von genau
4^16 nichtpositiven Eigenwerten und alle weiteren ≥2Δ/5.

**Eigene Verbesserung für Vermittler pro Kante:** Im Rückweg gibt es pro besetzter
Mode nur eine adressierte Kante. Daher gilt stattdessen ||An||²≤2(n+1)Ln, also
a²=(80,124,144,136,120,84,56,16). Die exakten LDL-Pivots für T−7I/10 sind

3/10, 4/15, 19/20, 559/190, 23467/5590, 616006/117335,
38644109/6160060, 2818555933/386441090.

Alle sind positiv. Damit ist das Belegungsband im benannten kantenlokalen C16-Modell
um mindestens **0.7Δ** getrennt. Ein zuerst versuchter Wert 0.8Δ scheiterte am zweiten
Pivot; der negative Test bleibt im Prüfer. Das ist weiterhin kein thermodynamischer
Bandabstand und kein Beweis des viel kleineren inneren Singulettgaps.

Die Feshbachrekursion aus N11 und ihre energieabhängige Restschranke sind korrekt.
Bei e≤0 und t/Δ=1/20 sinkt dieselbe Schranke mit den kantenlokalen Normen von
13.1528J auf **1.71601J**. Noch immer zu groß für den inneren Gap. Weder diese
Schranke noch die neue Bandtrennung zertifizieren den kanonischen H6-Rest.

## 4. F4 ist im kantenlokalen Modell überraschend einfach

Setze Ee=I−Se, Av=Σ(e enthält v)Ee und A=Σe Ee. Dann gilt exakt

F4,edge = 2A + Σ(überlappende e<f){Ee,Ef}
        = Σv Av² − 2A = Σv Av(Av−I).

Begründung: Ee²=2Ee und Σv Av=2A. Für eine Clebsch-Ecke ist Av die Summe von fünf
I−Swap-Terms. In der treuen regulären S6-Darstellung wurde die ganze ganzzahlige
Identität Π(k=0,…,10)(Av−kI)=0 auf 720 Dimensionen geprüft. Av≥0 und sein Spektrum
ist ganzzahlig; daher Av(Av−I)≥0. Somit **F4,edge≥0 als Vollraum-Operator**.

Zusätzlich liefert Σv(Av−A/8)²≥0 die Schranke

F4,edge ≥ A²/4−2A = H0²−76H0+1440I,

wobei H0=Σe P+e in J-Einheiten und A=80I−2H0. Das gilt ohne gleichzeitige
Diagonalisierbarkeit der Av. Bei ε=1/20 ist
f(h)=h+ε²(h²−76h+1440)/2 auf 0≤h≤40 streng steigend.

Die neue unabhängige Singulettrechnung reproduziert zunächst die beiden Varianten:

| Größe | Zellintern geteilt | Pro Kante lokal |
|---|---:|---:|
| F4-Grundwert | 555.4885003638373 | 732.1203109419222 |
| F4 auf den vier ersten gefundenen Moden | 583.292038666386 | 708.209322518918 |
| Koeffizient der Gapkorrektur ε² | +13.901769151274 | −11.955494211502 |

Danach wurde **H0+0.00125 F4,edge selbst** neu diagonalisiert, nicht nur F4 auf
alten Eigenvektoren ausgewertet. Ergebnis im 24.024-dimensionalen Singulettsektor:
E0=11.960507412663516, E1=12.446984939669278, Gap=0.4864775270057624;
maximale Residue der acht berechneten Vektoren 4.75e−14.
Dies sind die niedrigsten berechneten Eigenwerte des vollständigen *trunkierten Operators*, nicht dessen gesamtes Spektrum und nicht die volle Mikrodynamik.

Setzt man das aus der fremden 64-Sektor-Numerik berichtete nackte Nichtsingulettminimum
12.133537149348086 als tatsächliche Untergrenze voraus, folgt durch f(H0) die
korrigierte Nichtsingulettuntergrenze 12.96487952485328. Sie liegt über der
variationalen Viererraum-Obergrenze 12.447023775951228. Der Operatorvergleich ist
exakt; die eingesetzte nackte Untergrenze ist noch nicht zertifiziert. Das Ergebnis
wird deshalb **bedingt** geführt. Eine Intervall-/Inertia-Zertifizierung bleibt nötig.

## 5. E8-Vorzeichen und ein neuer CAR-Adapter

Der Standard-Gittercocycle ε(m,n)=(−1)^(mᵀBn) wurde unabhängig konstruiert.
Die F2-Probleme bestätigen Rang 45 für die lokale Antisymmetrie und Rang 285 für
den kantenlokalen Vorzeichenadapter. Die geteilte Bank hat in dieser Klasse
diagonaler ±1-Gauges eine Obstruktion. Kein Nachweis schließt daraus alle
komplexen oder nichtdiagonalen Adapter aus. Ein Standard-Gittercocycle ist auch
noch nicht sein Transport zur tatsächlichen TFPT-Clock-/Quellbasis.

**Eigener allordentlicher CAR/Tensor-Satz, eingeschränkter Vertrag:** Bei
kantenlokalen Vermittlern ohne Hopping sind
Qv=nf(v)+Σ(e enthält v)ne erhalten. Aus der vollständig belegten Nullbosonquelle
gilt Qv=1. Besetzte Bosonen bilden daher ein Matching. Für eine feste Ortsordnung
sei G(M)=(−1)^(Zahl sich kreuzender besetzter Kanten). Kalibriere die feste
Kantenphase mit (−1)^(j−i−1). Bei Entfernung eines Paars i<j unterscheidet sich
der CAR-Vertex dann vom harten Tensorvertex um (−1)^(Zahl der Löcher zwischen i,j).
Diese Parität zählt genau die Kreuzungen der neuen Kante mit dem alten Matching.
Also ist das relative Vorzeichen G(M')G(M). Adjungierte folgen durch Rücknahme.

Damit sind die vollständigen Hamiltonoperatoren in diesem erreichbaren Sektor
unitär gauge-äquivalent, nicht nur bis vierter Ordnung. Auf dem vollständigen
940-dimensionalen K4-Matchingsektor wurden alle 1584 Erzeugungsübergänge geprüft,
darunter 144 mit nichttrivialem relativem Vorzeichen. Geteilte Moden, Vermittlerhopping,
andere Ladungssektoren und der native Clock-Adapter sind ausdrücklich nicht eingeschlossen.

## 6. Ein physikalischer Filter statt eines kostenlos angenommenen Zielprojektors

Der tatsächliche 544-dimensionale Sternhamiltonoperator wurde aus seiner
288×256-Kopplungsmatrix neu aufgebaut. Sein Spektrum hat 14 verschiedene Werte:
sieben niedrige E−(g), g=0,1/2,…,3; sechs obere E+(g), g<3; und Δ mit Multiplizität 67.
E±(g)=(Δ±sqrt(Δ²+4t²(6−2g)))/2. Ziel ist der eindeutige niedrigste Wert E0.

Für jeden der 13 anderen Werte Ej setze τj=πℏ/(Ej−E0). Ein Hadamardtest mit
kontrolliertem exp[−iτj(H−E0)/ℏ] hat im akzeptierten Ausgang den Krausoperator

Aj(H)=(I+exp[−iτj(H−E0)/ℏ])/2.

Dann gilt auf dem **ganzen** Sternraum exakt Πj Aj(H)=P0,dressed: Jeder unerwünschte
Eigenwert wird von mindestens einem Faktor gelöscht, der Zielwert von allen erhalten.
Es ist keine kommensurable gemeinsame Uhr erforderlich. Ein Filter nur über die
sechs anderen niedrigen Werte reicht auf dem vollen Raum nicht; diese Negativkontrolle
wurde ausgeführt. Der volle 544D-Matrixvergleich bestätigt den Projektor.

Bei Δ=1,t=1/20 ist Στj=3172.829634 ℏ/Δ. Das ist eine echte Ressourcenzahl,
keine Behauptung kostenloser Spektralauswahl. Benötigt werden die bekannte kleine
Spektralstruktur, kontrollierte Entwicklung, genaue Phasen und Zeiten sowie 13
frische gemessene Bits oder 13 kohärente Hilfsbits.

Kohärentes Berechnen, Phasieren des All-null-Records und Rückrechnen realisieren
auch eine selektive Zielphase. Pro Zielphase sind 26 kontrollierte H-Aufrufe nötig;
zwei Verstärkungsschritte brauchen 52, zusätzlich die Eingangsphasenoperationen.
Bei idealen übrigen Gattern genügt konservativ δH+δE0≤7.88e−8 Δ für Infidelität
≤1e−6, denn der Zustandsfehler ist höchstens 4Στj(δH+δE0)/ℏ. Zeitfehler und andere
Gatterfehler müssen zusätzlich berechnet werden. Endliche exakte Clifford+T-Synthese
dieser reellen Zeiten wird nicht behauptet.

## 7. Neue gemeinsame mikroskopische Vorbereitung, Record und Schlussprüfung

Es geht noch einfacher als eine kohärente Entkleidung: Nach dem Filter die
Vermittlerbelegung messen und den leeren Zweig behalten. Mit
w=(1+Δ/sqrt(Δ²+24t²))/2 gilt auf nackter Materie

Pbare P0,dressed Pbare = w PΩ.

Das ist ein einzelner vollständiger akzeptierter Krausoperator, keine nur
bedingte Fidelitätsaussage. Aus dem elementaren Zweisingulettzustand χ entstehen
Ω mit Rohwahrscheinlichkeit w²/6. χ benötigt nicht bereits Ω als Ressource.
Danach benutzen lokale Ticks und der resonante Record die nackte Materie. Die
Schlussprüfung verwendet **denselben** mikroskopischen Filter samt Leerbelegung.

Für C als lokalen Dreierzyklus ergibt die neue volle 256D-Echorechnung:

| Größe | Record behalten | Record frisch |
|---|---:|---:|
| Präparation erfolgreich | 0.16191533129706945 | gleich |
| Schluss erfolgreich, nach Präparation | 0.9714919877824064 | 0.5161051185094034 |
| Gesamterfolg je gestartetem Versuch | 0.15729944705423687 | 0.08356533124756335 |

Formeln: Schluss w² bzw. 17w²/32; insgesamt w⁴/6 bzw. 17w⁴/192. Der Quotient
frisch/behalten bleibt 17/32. Es sind nicht die alten nackten Rohwerte 1/24 und
17/768; Eingangs- und Filtervertrag sind neu und benannt. Reset liefert im Mittel
6.1761 Präparationsversuche. Start plus Schluss brauchen 26 schwache kontrollierte
Entwicklungen mit Gesamtzeit 6345.659268 ℏ/Δ, zusätzlich Recordpulse und Reset.

Der Record selbst vereinfacht sich: Für den realen resonanten Volltransfer Ures
gilt Ures† Q Ures=R auf Materie und Identität auf dem übrigen lokalen 44D-Sektor.
Die zusätzlichen Viertelphasen sind für die spezielle Involution U0 nötig, nicht
für diese Record-Makrooperation. Beide Recordausgänge bleiben erhalten.

Dies schließt eine endliche gemeinsame **kontrollierte Modellrechnung**. Es
ist kein Nachweis unveränderter statischer Dynamik oder der nativen Verfügbarkeit
von Resonanz, isoliertem Stern, kontrolliertem H, Record, Clock und Reset.

## 8. Feedback, Fehler und viele unabhängige Zellen

Der N11-Kanal E(ρ)=KρK†+Tr[(I−K†K)ρ]ρ0 ist CPTP und hat Ω als einzigen
stationären Zustand. K fixiert Ω, und K†K≤PΩ+β(I−PΩ), β=(9+sqrt(17))/32.
Mit <Ω|ρ0|Ω>=1/24 folgt 1−F(E^mρ)≤r^m(1−Fρ), r=0.97542071045.
556 Zyklen genügen für 1e−6. Der eigene komplette 256D-Lauf prüft zusätzlich
Spur-/Gewichtsidentität und Kontraktion bei jedem Schritt.

**Eigene Robustheit:** Bei höchstens ε Kanalfehler in halber Diamantnorm pro
Zyklus gilt 1−F_m≤r^m(1−F_0)+ε(1−r^m)/(1−r). Der konservative Fehlerboden
ist 40.6847ε. 1e−6 Dauerfehler verlangt somit ε≲2.46e−8. Die Zutaten bleiben
eine Mess-/Resetumgebung; der Kanal ist nicht derselbe wie die unitalen ungelesenen Records.

Für N unabhängig lokal kontrollierte Zellen gilt auch bei anfänglich verschränkten
Eingängen durch den Vereinigungsbound global 1−F≤N r^m; lokale Marginalfehler bleiben
größenuniform. Für N=4096 genügen konservativ 890 Zyklen für global 1e−6. Dies ist
kein wechselwirkender Zustandssatz. Ein Messreset benötigt bis zu acht klassische
Farbbits pro zurückgesetzter Zelle, zusätzlich drei Austauschrecords pro Zyklus.
Löschung, Energie und Entropie sind reale Budgets; daraus folgt keine kostenlose Kühlung.

## 9. T1–T8: eigene Arbeit auch jenseits der kleinen Maschine

| Tor | Neue Rechnung / Ableitung dieser Runde | Nächste fehlende Beweiskante |
|---|---|---|
| T1 | Vollständige Rang-Ausnahmestellen der Lazy-Walk-Familie erneut exakt: 1/7 löscht 30, 1/3 löscht 5 Richtungen; Kontext- und Strahlentropie wählen verschiedene Werte. Drei lokale Architekturlesarten getrennt. | Die native Operations- und Zustandsauswahl; eine Symmetrie oder maximale Entropie ohne Auslesevertrag genügt nicht. |
| T2 | Exakte Vakuum-Oszillatornormkoeffizienten für q=1/2,1,2; Half-Charge-Paritätsobstruktion gegenüber ausschließlich ganzzahligen Ladungsverschiebungen. | Feld auf gemeinsamer dichter Domäne mit Energie-/Adjungiertenkontrolle aus der tatsächlichen Quelle, nicht einer hinzugefügten Ladungsgitter-CFT. |
| T3 | Wärmekern der ausdrücklich gewählten Familien C16 × (Z/LZ)^d für d=1,2,3,4 und L=16,32,64; alle zeigen ihre eingesetzte Dimension. Zwei verschiedene Geschwindigkeiten auf demselben Graphen bleiben möglich. | Auswahl der Familie und gemeinsamer kohärenter Lorentzkegel; ein Wärmekern ist kein kausaler Propagator. |
| T4 | Eigener Overlap-Diracoperator mit Fluss 3 auf 8×8 und 10×10: genau drei Nullmoden, Index −3 in der erklärten Orientierung, GW-Defekt <1.2e−13. Fluss 1 und 4 liefert entsprechend andere Zahlen. | Herkunft von Fluss/Geometrie, 3+1D-Propagation, Spiegelgap, global konsistentes chirales Maß und richtige Ladungen. |
| T5 | Neue Band-, CAR- und F4-Sätze; echte lokale H2+H4-Neudiagonalisierung; bedingte sektorübergreifende Untergrenze. | Zertifizierte nackte Sektorgrenzen, kontrollierter kanonischer Rest, wechselwirkender Vielzellenlimes. |
| T6 | ACT-Invariantenrechnung; zusätzlich Yukawaüberlappungen der drei eigenen Nullmoden: konstantes skalares Profil liefert die Einheitsmatrix, also keine Flavorhierarchie. | Normierte gemeinsame Wirkung, Higgsprofil, RG und Theorieunsicherheiten; keine nachträglich eingesetzten Texturen. |
| T7 | Acht Weyl-Knoten im einfachsten Sinussymbol; gapped freie Tensor-Zweipunktfunktion hat Schwelle 2m; TT-Projektor mit Rang zwei erzeugt keinen Pol; Zweimaterie-Ward-Test erzwingt gleiche weiche Spin-2-Kopplung. | Tatsächlicher masseloser Spin-2-Sektor mit Constraints und universeller Kopplung aus derselben Quelle. |
| T8 | Feedbackattraktor verifiziert; Fehlerboden und unabhängiger Mehrzellbound neu; gemeinsamer mikroskopischer Filter und Rohstatistik. | Physische Reset-/Controllerkopplung, kosmologische Randbedingung und gemeinsames Zustandsfunktional. |

### Analytische Naht genauer

Im ausdrücklich normierten freien Bosonreferenzmodell ist
Σ c_n z^n=(1−z)^(−q²), c_n=(q²)_n/n!. Die Rekursion n c_n=(q²+n−1)c_(n−1)
ist exakt nachgerechnet. Auf dem Vakuum hat ein geeignet verschmiertes Feld
die Normsumme Σ|f_n|² c_n; exponentiell fallende Koeffizienten machen sie endlich.
Das ist noch keine Abschätzung auf allen energiegewichteten Zuständen.
Auf dem deklarierten halbganzzahligen Ladungsgitter kommutieren Integer-Shifts
mit (−1)^(2Q), Half-Shifts antikommutieren. Algebraische Produkte ausschließlich
ersterer und passende starke Grenzwerte bleiben im Paritätskommutanten. Die
fehlende intersektorielle Operation muss tatsächlich hinzugefügt oder aus einem
größeren Quellsektor gewonnen werden; mehr ganzzahlige Tests ersetzen sie nicht.

### Geometrie, Familien und Flavor genauer

Für den Produktgraphen sind die Laplaceeigenwerte λint+4Σ sin²(πkμ/L).
Die Wärmespur faktorisiert exakt, ohne bis zu 268 Millionen Knoten auszuschreiben.
Bei t=8 und L=64 erhält man ds≈1.0167d. Der dreidimensionale Fall ist also
nicht ausgezeichnet. Ein kohärentes Sinus-Weylsymbol Σσμ sin kμ besitzt zudem
acht Knoten mit insgesamt null chiraler Ladung; ein lokaler Weyl-Limes um einen
Punkt entfernt die übrigen sieben nicht.

Der innere Overlap-Test verwendet einen separat gesetzten Zweitorus, m0=1 und
U(1)-Fluss. D=I+γ5 sign(γ5DW) erfüllt γ5D+Dγ5=Dγ5D. Bei Fluss 3 werden auf
beiden Gittergrößen drei und keine zusätzlichen Nullmoden gefunden. Fluss 0 hat
hier zwei Nullmoden bei Nettoindex null: ein konkreter Hinweis, weshalb ein Index
allein keine vektorartigen Paare ausschließt. Für orthonormale gleiche linke/rechte
innere Moden und konstantes Profil ist Yab=y δab. Ein beispielhaft gewähltes
kosinusförmiges Profil spaltet die Eigenwerte, ist aber ein neuer Input, keine
abgeleitete Massenhierarchie. Dieses Modell ist ein regulatorischer Mechanismustest,
nicht die Behauptung dreier nativer Standardmodellfamilien.

### Parameter und Gravitation genauer

Für den unveränderten einfachen Inflationszweig gilt ohne N:
A_s(1−n_s)²=c3^7/(6π²), r=3(1−n_s)². ACT DR6 v2, Tabelle 5, P-ACT-LB2,
nennt n_s=0.9752±0.0030 und log(10^10 A_s)=3.062. Die Tabelle wurde direkt
visuell geprüft. Kalibrierung auf die zentrale Amplitude gibt N=56.62391,
n_s=0.96467923, marginale Abweichung 3.5069 Standardunsicherheiten. Umgekehrt
erzwingt der zentrale Tilt N=80.64516 und eine um Faktor 2.02842 zu große Amplitude.
Gemeinsames Treffen beider Zentralwerte würde c3 um rund 9.61 Prozent ändern.
Das ist keine vorgeschlagene Reparatur: c3 ist bereits anderweitig fixiert.
Ein neuer Likelihood-/Reheating-/Theoriefehlerfit wurde nicht ausgeführt.

Im ausdrücklich freien gapped Referenzmodell hat ein normalgeordnetes bilineares
Tensorobservable erst ab 2m Spektralgewicht; eine TT-Projektion verändert diese
Energien nicht. Für einen angenommenen weichen gravitativen Pol liefert die
Wardvariation in einer nichttrivialen Zweimateriestreuung (g1−g2)(p3−p1)=0.
Universelle Kopplung ist damit eine zusätzliche zwingende Prüfung, nicht eine
automatische Folge des Rang-zwei-TT-Projektors. Diese konkreten Tests erzeugen
noch keinen neuen gravitativen Pol.

## 10. RH, Faktorisierung und weitere Physik

RH-Aktualitätsprüfung erneut blockiert: der gepinnte Quellenordner fehlt. Der
separate Faktorgraph fehlt ebenfalls. Es wurden keine Pins geändert oder
Beweismarker angehoben. Die Originalrouten r404 (RESTATEMENT) und r647
(STRUCTURAL_MISMATCH) wurden gelesen. Neuere Metadaten beschreiben einen
ausführbaren Referenz-Periodenleser; dessen extern gepinnter Quellpfad fehlt hier
ebenfalls. Das ist ein Quellenhinweis, keine unabhängig geprüfte neue Fähigkeit.

Die vollständige signierte Weil-Normidentität bleibt offen; endliche Schurpositivität
und der physikalische Bandbeweis liefern sie nicht. Für den bekannten Faktorweg
fehlen weiterhin der native skalierende Compiler und ein neuer Auslesemechanismus
jenseits der bereits begrenzten ggT-Momentroute. P versus NP bleibt eine separate Frage.

Dunkle Materie: kein berechneter stabiler Sektor samt Produktion. Dunkle Energie:
keine radiativ stabile gravitative Vakuumwirkung. Baryogenese: keine dynamische
Asymmetrieausbeute. Starkes CP: kein Schutz im fertigen fermionischen Maß.
Schwarze Löcher: benötigen den noch fehlenden T7-Sektor. Diese Punkte werden
nicht durch den endlichen Feedback- oder Filtererfolg geschlossen.

## 11. Ausgeführte Prüfung, Grenzen und nächste Entscheidung

Eigene leichte Prüfer: frontier.py, phase_car.py, spectral_algebra.py; zusammen
**8232 Bedingungen**. Normal/-OO bytegleich; sieben gezielte Mutanten erkannt.
Die meisten Bedingungen sind einzelne Zustands-/Übergangsprüfungen, keine
unabhängigen Entdeckungen. Hinzu kommt der neue 24.024D-Singulettlauf mit echter
H2+H4-Neudiagonalisierung. Die Analysesätze sind ausgeschrieben, nicht Lean-formalisiert.

Die nächste entscheidende Forschungsarbeit ist die Quelle des nun vollständig
spezifizierten **kontrollierten** Mikrolabors: kontrolliertes H, Resonanz, isolierte
Kanten/Sterne, Q, elementarer Reset und physischer Entropieabfluss. Gleichzeitig
lohnt sich die Zertifizierung der nackten C16-Untergrenzen: Die neue positive
F4-Darstellung macht daraus eine deutlich kleinere, präzise spektrale Aufgabe.
Für T3/T4/T7 fehlt weiterhin eine einzige native skalierende Familie.

Primärreferenzen: [Schrieffer–Wolff](https://arxiv.org/abs/1105.0675),
[unitäre Gitter-VOA](https://arxiv.org/abs/1308.2361),
[Ginsparg–Wilson](https://arxiv.org/abs/hep-lat/9802011),
[magnetisierte innere Räume](https://arxiv.org/abs/hep-th/0404229),
[Weyl-Walks](https://arxiv.org/abs/1708.00826),
[ACT DR6 v2](https://arxiv.org/abs/2503.14452v2),
[NIST/CODATA 2022](https://physics.nist.gov/cuu/Constants/Table/allascii.txt).
Sie stützen Methoden und Daten, nicht automatisch die hier untersuchte TFPT-Auswahl.
