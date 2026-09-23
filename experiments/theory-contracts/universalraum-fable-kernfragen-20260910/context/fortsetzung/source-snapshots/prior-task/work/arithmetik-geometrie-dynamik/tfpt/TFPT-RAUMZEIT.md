# TFPT: Compiler, Raumzeit und die noch fehlende Transformation

Stand: 10. September 2026. Begrenzter Quellenabgleich am lokalen Commit `66b91e40e245569f06ab440ead80f446c9be0ee5`. Die ausgewählten Originaltexte, 15 aktuelle Ledgerzeilen, zwei relevante Verifikationsfunktionen und die Vorhersagenregister wurden live gelesen. Die gesamte Suite und die ganze historische Theorie wurden nicht erneut geprüft. Keine Originaldatei und kein Status wurden geändert.

**Die gemeinsame mathematische Sprache ist schon erkennbar: Operationen, Zustände und ihre Antworten müssen gemeinsam transportiert werden. TFPT besitzt sowohl einen weit ausgebauten algebraischen Compiler als auch echte, quellenbezogene Dynamiksätze. Die entscheidende offene Verbindung ist, dass diese bislang verschiedenen Quellen dieselbe physische Theorie realisieren. Eine gleiche Zahl, ein E8-Gitter oder ein passendes Spektrum beweist diese Verbindung nicht.**

## 1. Was der Compiler tatsächlich als Ausgangsdaten verwendet

Das originale Architekturpapier unterscheidet ausdrücklich zwei Dinge:

- P1 setzt einen orientierten, reflexionspositiven Seam-Kern mit Einheitwindung und der Normierung `c3=1/(8π)` voraus. Die Identität `4·2π·c3=1` erklärt diese Normierung; ihre konkrete modulare Antwortherkunft ist weiter offen.
- P2 unterscheidet die physische Fünf-Slot-Schnittstelle von ihren algebraischen Konsequenzen. Bei dieser Schnittstelle folgen die Hyperladungen `−1/3, 1/2`, die Trägerstruktur und Familienzählung aus den bezeichneten Regeln. Verschiedene spätere Auswahlregeln erzwingen fünf innerhalb ihrer jeweiligen Architektur.

Beide Zahlen lassen sich als elementarsymmetrische Daten des Ankers `a=(1,1,2)` schreiben: `e1=4`, `e2=5`, `e3=2`. Das ist eine kompakte Erzeugungsvorschrift. Dass gerade dieser Anker, die zugrunde liegende Algebra, ihr Zustand und ihre räumliche Realisierung physisch ausgewählt werden, ist eine zusätzliche Aussage. Die aktuelle Ledgerzeile AX.P2 dokumentiert erhebliche Verfeinerungen bis zu endlichen demokratischen Antwortwerten, lässt aber die physische Grenzidentifikation und die Axiomtypisierung bestehen.

Die Formulierung „nur π bleibt“ betrifft in dieser Darstellung die ausdrücklich verwendeten dimensionslosen transzendenten Zahlen. Sie bestimmt weder ein Raumzeitmaß noch Newtons dimensionsbehaftete Konstante noch einen kosmologischen Anfangszustand. Die Quellen führen eine induzierte Gravitationsskala und eine absolute Amplitudennorm gesondert.

Quellen: `tfpt_1_architecture_e8.tex`, Abschnitt „Foundational postulates“ und anschließende Anchor-first-Verfeinerung; `verification/status_ledger.csv`, AX.P1.01/AX.P2.01; `docs/CLAIMS.md`, vier Schichten. Die oft stärkeren historischen Kurzformulierungen in Übersichten werden hier anhand der aktuelleren expliziten Verträge gelesen.

## 2. Was „Standardmodell aus dem Compiler“ präzise abdeckt

| Ebene | Tatsächliches Objekt / Beispiel | Noch zusätzlich nötige Aussage |
|---|---|---|
| Gitter und Darstellung | `(D5⊕A3)+μ4 ≅ E8`, Klebeindex vier; im gewählten Träger drei Familien | Die konkrete Quelle der physischen, chiralen 3+1D-Felder realisiert diese Darstellung mit der richtigen lokalen Dynamik. |
| Zahlengrammatik | `φ0=1/(6π)+3/(256π⁴)`; Flavoroperatoren mit Determinanten `(3,4,8,20)`; rationale Massenverhältnisse | Physische Operatoridentifikation, Schementransport, absolute Skalen und vollständige Neutrinodaten. |
| Elektromagnetischer Fixpunkt | Eindeutige numerisch eingeschlossene Nullstelle der bezeichneten Gleichung, `α⁻¹=137.0359992168…` | Die tatsächliche Quillen-Variation ist exakt diese Gleichung; nicht nur eine identische Auswertung nach Einsetzen der Gleichung. |
| Kosmologie | Eingefrorene Formeln und Bänder, etwa `r=12/N★²`, `n_s=1−2/N★` | Auswahl von Zustand, Reheating/Transfer und relevanter physischer Skala; `N★∈[50,60]` wird im Register als externer Reheatingeingang bezeichnet. |
| Gravitation | Konsistente Koeffizienten und quadratische Spin-2-Zielmodelle | Ein gemeinsamer ausgewählter Parent, der den masselosen Modus, die universelle Kopplung und die Raumzeitgrenze hervorbringt. |

Die Zahlenseite ist deshalb ein wertvoller Satz von Constraints an eine gemeinsame Theorie. Sie ist noch keine Konstruktion des gesamten nichtperturbativen Standardmodells mit lokaler chiraler Maßstruktur, allen drei Eichkopplungen, Streuprozessen und Gravitation.

Quellen: `tfpt_1_architecture_e8.tex`, Architektur/Träger; `tfpt_2_standard_model.tex`, Massen-Masterformel; `predictions_frozen.json`; ALPHA.QUILLEN.EXACT.01 und die aktuelle T1–T8-Tabelle in `experiments/theory-contracts/RESEARCH_2026-09-09.md`.

## 3. Was die „27 Vorhersagen“ zählen

Die lokale Websitequelle enthält tatsächlich **27 Karten**. Ihre eigenen Statusfelder lauten:

| Status der Karte | Anzahl |
|---|---:|
| Exact identity | 5 |
| Numerical fixed point | 4 |
| Conditional | 16 |
| Open / not forced | 2 |

Daneben enthält das maschinenlesbare eingefrorene Register **16 Werte**, **2 zugewiesene Texturwerte**, **2 bedingte Bänder** und **2 ausdrücklich nicht als zusätzliche Vorhersagen gezählte Varianten**. Die ältere Falsifikationsliste `freeze_file.csv` enthält 18 Prüfflächen. Diese Listen zählen verschiedene Dinge; sie dürfen nicht addiert werden. `vorhersagen-inventar.json` enthält sämtliche Karten mit ihrem Originalstatus sowie die Zähler.

Ein „Exact identity“-Status bezeichnet die interne Formel oder Struktur. Er bedeutet nicht automatisch, dass eine unabhängige Messung die physische Deutung bestätigt hat. Die Websitekarten umfassen zudem abhängige Kombinationen und offene Prüfflächen. In `docs/FALSIFICATION.md` steht ausdrücklich, dass viele Ausgangsbeobachtungen bei der Formelfindung bereits bekannt waren und mehrere Treffer von denselben wenigen Atomen abhängen. Der Freeze schützt künftige Tests, macht frühere bekannte Daten aber nicht nachträglich blind.

Damit ist „27 statusgekennzeichnete Prüfflächen“ belegt. „27 unabhängige, bereits bestätigte Blindvorhersagen“ ist hieraus nicht belegt. Dies ist eine Zähl- und Herkunftskontrolle, keine neue Außenweltbewertung der einzelnen Messungen; ältere Sigmaangaben wurden nicht als aktuell übernommen.

## 4. Der stärkste bereits vorhandene dynamische Herkunftssatz

Die am 9. September integrierte Forschung hat eine wichtige, tatsächlich passende Transformation: **Ein lokales geladenes Feld wird aus derselben mikroskopischen Quelle samt gefülltem Vakuum und Dynamik gewonnen.**

Die Quelle ist ein bestimmter komplexer QWZ-Streifen mit Breite acht, Masse eins und Holonomiesektor `r=1`. Seine Einteilchendimension ist `16N` über den komplexen Zahlen. Sie ist nicht identisch mit den sechzehn reellen Majoranas des endlichen Compilers.

Mit der originalen Matrix `h_N` und ihrem negativen Spektralprojektor `P_N` lautet die Energie

\[
D_N=\frac{N}{2\pi}h_N,\qquad
\mathcal H_N=d\Gamma(D_N)-\operatorname{Tr}(P_ND_N).
\]

Die Subtraktion stammt vom tatsächlich gefüllten See. Die lokalen Operatoren sind originale, an der oberen Randzeile geglättete CAR-Vernichter und ihre wirklichen Adjunkten. Es werden keine zusätzlichen Ladungsregister eingesetzt.

Der ausgeschriebene Beweis konstruiert Vergleichsabbildungen `V_N`, für die auf dem gemeinsamen endlichen Energiekern gleichzeitig gilt:

\[
\Psi_N(g)V_N-V_N\Psi(g)\longrightarrow0,
\quad
\Psi_N(g)^*V_N-V_N\Psi(g)^*\longrightarrow0,
\quad
(\mathcal H_NV_N-V_N\mathcal H)1_{\mathcal H\le E}\longrightarrow0.
\]

Ladung und Polarisierung werden exakt erhalten. Daraus folgen alle fest gewählten endlichen Feldwörter und ihre komplexen Vakuumantworten, auch zu endlich vielen Zeiten. Das ist deutlich mehr als ein ähnliches Spektrum. Der Beweis behält die Holonomieverschiebung `j−1/4` und liefert etwa die wirklichen Randladungsenergien `q²/2−q/4`.

**Dieser Satz ist in den Originalen bereits vorhanden; er wird hier als gelungenes Vorbild identifiziert, nicht als neue Entdeckung ausgegeben.** Der direkte schriftliche Beweis wurde gelesen; seine gesamte numerische Verifikationskette wurde in dieser Bestandsaufnahme nicht erneut ausgeführt. Freie chirale Randfermionen selbst sind klassisch. Auch der extern zitierte Osborne–Stottmeister-Satz behandelt Gitterannäherungen von 1+1D-CFTs unter bestimmten Voraussetzungen, keine automatische 3+1D-Welt. [Osborne–Stottmeister, Originalarbeit](https://arxiv.org/abs/2107.13834)

Lokale Hauptquelle: `experiments/theory-contracts/microscopic-charged-car-limit/README.md`, Abschnitte 2–7; integrierte Darstellung `tex-artefacts/toe_research_20260909.tex`, Abschnitt 1.

## 5. Zwei konkrete nächste Herkunftssätze

Diese beiden Aussagen sind **offene Ziele mit benanntem Input**, keine als bewiesen ausgegebenen Resultate.

### A. Vom vorhandenen geladenen Feld zur markierten E8-Erweiterung

Aus derselben mikroskopischen CAR-Quelle und ihren zulässigen Ladungssektoren sind renormierte, geglättete Zwischen-Sektor-Felder zu konstruieren. Sie müssen mit beiden Adjunkten auf einem gemeinsamen Energiekern konvergieren. Die acht Kanäle, ihre Familien- und Clockmarkierung sowie ihr Ladungskokzyklus müssen dabei aus der Quelle folgen.

Das E8-Ziel ist konkret: die Spinorladung `s=(1/2,…,1/2)` hat `|s|²/2=1`; die Produkte müssen den tatsächlichen Ladungsübertrag erhalten. Eine vierwertige Gradmarke bedeutet nicht `U_s⁴=I`, sondern im vorhandenen Ziel `U_s⁴=U_(4s)`. Die mikroskopische Identifikation muss genau diese Operatorprodukte und nicht nur die Grade treffen.

**Entscheidungstest:** Ein nichtverschwindender geglätteter Zwischen-Sektor-Grenzoperator mit aus der Quelle bestimmter Normierung, beiden Adjunkten, Energiebeschränkungen und korrektem Produkt-/Ladungstransport. Ein scharfer unrenormierter Halbtwist ist bereits durch eine divergierende Hilbert–Schmidt-Summe ausgeschlossen; dieselbe scharfe Konstruktion größer auszurechnen schließt die Lücke nicht. Acht unabhängige Kopien bloß anzuhängen würde die Kanalauswahl voraussetzen.

Das ist der direkte Fortschrittspfad zu T2 und zu den daran hängenden P1/KMS/Quillen-Identifikationen. Selbst sein Erfolg wäre noch kein T3–T8-Abschluss.

### B. Vom tatsächlichen nichtgaußschen Transport zur Compiler-Wechselwirkung

Die sechzehn-Majorana-Quelle besitzt Hamiltonoperatoren der Form

\[
H(D)=\frac{i}{4}\gamma^TD\gamma.
\]

Für skalare Koeffizienten schließen diese unter Kommutatoren quadratisch. Auch die reguläre rein fermionische Gaussian-Elimination erzeugt im Logarithmus keinen verbundenen quartischen Vertex. Die Originalgeneratoren `A0,A_int` kommutieren sogar miteinander; „int“ bezeichnet hier Kanalvermischung. Der Name ist kein Nachweis einer Viele-Teilchen-Wechselwirkung.

Im separat deklarierten kompakten U(1)-Rotor/CAR-Parent existiert dagegen wirklich nichtkommutierende elektrische Dynamik. Ein echter elektrischer Doppelkommutator liefert einen quartischen Anteil. **Gesucht ist deshalb eine zustands- und operationsverträgliche Abbildung zwischen diesem tatsächlichen Transportträger und der richtigen Clock-CAR-Algebra.** Sie muss Gaussgesetz, Boundary-Support, komplette Clockwirkung, tatsächliche Hamiltonoperatoren und relevante Antworten erhalten. Erst dann darf der erzeugte Vertex als Compiler-Wechselwirkung gelesen werden.

**Entscheidungstest:** Der Kandidat muss auf der Gauss-physischen Algebra nichttrivial wirken und die ursprünglichen Wechselwirkungsterme mitführen. Der schon geprüfte Weg über ortsfeste, rotorunabhängige interne Phasen scheitert: Aus den originalen Hoppings folgen nur `h_x=l_x=q_x` und Linkgrade `q_v−q_u`. Diese Transformation ist auf dem Gauss-Sektor skalar. Außerdem passen die Clockmultiplizitäten `(5,1,1,1)` nicht zu den paarweise geraden L/H-Multiplizitäten. Räumliche, flussabhängige oder Bogoliubov-Abbildungen werden dadurch nicht ausgeschlossen; sie müssen explizit angegeben werden.

Dieser zweite Herkunftssatz entscheidet eine bestimmte vorhandene Wechselwirkungsroute. Er darf keine frei gesetzten neuen Kopplungen als Herkunft ausgeben und ist kein allgemeines Unmöglichkeitstheorem.

Quellen A: `microscopic-charged-car-limit/README.md`, `RESEARCH_2026-09-09.md`, Abschnitte Source-field/Next experiment; B: `clock-interaction-provenance/README.md` und `clock-rotor-joint-charge/README.md`, jeweils vollständig gelesene benannte Beweisabschnitte.

## 6. Wie daraus Raumzeit werden müsste

Der Zustand zusammen mit seiner Algebra definiert einen modularen Fluss. Für physische Raumzeit braucht man zusätzlich eine Familie lokaler Algebren, ihre Inklusionen und Kommutanten, eine spektrale Energiebedingung und die kompatible geometrische Wirkung. Ein einzelner Fluss oder eine KMS-Temperatur enthält diese ganze Organisation nicht.

Der originale Bulkvertrag verlangt deshalb Lokalität, Poincaré-Kovarianz, positive Energie, Spin/Statistik, beide Helizitäten, Clustering, nichttriviale Streuung und eine genaue Operatorübersetzung. Seine ursprüngliche unbedingte Eindeutigkeitsforderung wurde bereits eingeschränkt: Man kann unsichtbare entkoppelte Bulksektoren hinzufügen, ohne Seamantworten zu verändern. Die neue Forderung betrifft seam-erzeugte Vervollständigungen mit trivialem relativen Kommutanten. **„Prime completion“ bedeutet dort irreduzible/seam-erzeugte Vervollständigung; das Wort ist nicht automatisch ein Primzahloperator.**

Ein konkret gebauter kompakter Rotorparent besitzt inzwischen zeitlich unbeschränkte Quasilokal-Dynamik und neutrale Grundzustandsgrenzen mit positiver Energie. Die Originalquelle nennt seine Koeffizienten ausdrücklich: `a=1/12, η=1/2, β=1/4, κ=1/100, M=4`. Sie sind für dieses Modell festgelegt. Der Compiler hat gerade diesen Parent noch nicht ausgewählt. Auch Zustandsauswahl, wechselwirkende Kontinuumsgrenze, chirales Standardmodell und Gravitation werden damit nicht gemeinsam identifiziert. Auf der gesamten beschränkten lokalen Algebra ist sein Fluss zudem nicht in Punktnorm stetig; der Originalsatz benennt die kleinere stetige Algebra.

Die jüngste integrierte T1–T8-Tabelle bleibt daher maßgeblich:

| Gate | Erste verbleibende physische Aufgabe |
|---|---|
| T1 | Prinzip, Anker/Compiler und Dimension auswählen. |
| T2 | Tatsächliche markierte E8-Seam mit halber Ladung und kontrollierter Feldgrenze. |
| T3 | Einen gemeinsamen, TFPT-ausgewählten lokalen unitären 3+1D-Parent herleiten. |
| T4 | Dessen chirale Eich-/Weyltheorie, Anomalien und gleichmäßige Spiegelentkopplung. |
| T5 | Physische wechselwirkende Grenze, Lorentzverhalten und erforderliche Streuung/Clustering. |
| T6 | Alle drei Eichkopplungen und vollständige Neutrinotextur/-skala intern bestimmen. |
| T7 | Masselosen Quantenspin zwei mit universeller Kopplung aus demselben Parent gewinnen. |
| T8 | Physischen Anfangszustand und ein gemeinsames Funktional für sämtliche Antworten auswählen. |

Quellen: `tfpt_research_contracts.tex`, SEAM.BULK4D.RECON.01/BULK.PRIME_COMPLETION.01; DYN.UNITARY.DILATION.01; QFT4D.OS.RECON.01; TFPT.TOE.COMPLETE.01; `RESEARCH_2026-09-09.md`.

## 7. Warum der Gravitationsteil nicht bereits durch die neue Verbindung erledigt ist

Das bestehende `v359_grav_nonlinear_einstein.run` prüft konkrete Koeffizienten- und Spuridentitäten: zum Beispiel `2π/(1/4)=8π=1/c3` und den bezeichneten Vakuumenergievorfaktor. Die Tensorstruktur, Jacobson-/CHM-Anwendbarkeit und der Übergang über alle zeitartigen Richtungen sind in dieser Funktion als zitierte Schritte eingetragen; mehrere entsprechende Prüfungen erhalten direkt `True`. Das ist eine Dokumentation der angenommenen Schritte, kein maschineller Beweis ihrer Anwendbarkeit auf einen neu erzeugten TFPT-Raum.

Der aktuelle Vertrag GRAV.NONCIRCULAR.01 sagt das ausdrücklich: Die Einstein-Entropiegleichgewichtsroute setzt eine geeignete lokale 4D-Theorie, Vakuum- und Modularstruktur voraus. Diese Voraussetzungen dürfen nicht anschließend als von derselben Formel hergeleitete Raumzeit ausgegeben werden. Der Originalartikel von Jacobson ist ebenfalls enger: Er behandelt erste Variationen des lokalen Vakuums; bei nichtkonformen Feldern bleibt eine Entropievariationsannahme. [Jacobson, Originalarbeit](https://arxiv.org/abs/1505.04753) Die benutzte Kugelabbildung von Casini–Huerta–Myers setzt eine geeignete CFT und ihre konforme Abbildung voraus. [CHM, Originalarbeit](https://arxiv.org/abs/1102.0440)

Der aktuelle Spin-2-Vertrag verlangt daher aus **derselben** spektralen Quelle einen masselosen transversalen Pol, zwei Helizitäten, positive physische Normen, universelle Stresskopplung und die richtigen Wardidentitäten. Es gibt inzwischen quadratische, lokal constrained Zielmodelle und freie Weyl/Fock-Zeugen. Sie zeigen, wie ein benötigtes Teilstück mathematisch funktionieren kann; der gemeinsame Parent, seine nichtlineare universelle Kopplung und der physische Grenzübergang bleiben offen.

Auch eine wichtige Einschränkung ist schon bewiesen: Ein gleichmäßig über alle Volumina strikt gapped Parent kann keinen masselosen Modus mit Frequenz gegen null erzeugen. Das verbietet, den endlichen positiven Compiler-Relaxationsgap ungeprüft zum Gap der gesamten Welt zu erklären. Ein möglicher Anschluss braucht eine kritische physische Folge beziehungsweise passende lokale Constraints. Das betrifft den bezeichneten Mechanismus, nicht alle möglichen emergenten Gravitationsmodelle.

## 8. Konsequenz für Arithmetik ↔ Geometrie ↔ Dynamik

Die strukturelle Gemeinsamkeit liegt am belastbarsten in einem **Antwort-erhaltenden Operatorwörterbuch**. Die E8-Gitterübersetzung erhält Paarungen und Monodromie; die U/V-Rekonstruktion erhält alle Wörter ihres bezeichneten Alphabets; die mikroskopische CAR-Grenze erhält Felder, Adjunkte, Ladung, Seezustand und Energie. Diese drei Beispiele bewahren jeweils mehr als gemeinsame Zahlen, aber jeweils klar bezeichnete Daten.

Eine universelle Transformation müsste zusätzlich zeigen, dass dieselben Abbildungen für alle benötigten Quellen, lokalen Gebiete, Generatoren und Grenzübergänge kompatibel sind. Für eine rechnerische Abkürzung müsste die Auswertung auf der geometrischen Seite einschließlich Hin- und Rückübersetzung effizienter sein. Für Gravitation müsste gerade die physische Lokal-/Stress-/Zustandsstruktur erhalten bleiben. Diese Anforderungen werden durch bloße Spektralkorrelationen oder die Häufigkeit der Zahlen 2, 3 und 5 nicht geliefert.

Der gezielte nächste Versuch ist damit A oder B aus Abschnitt 5: **eine bisher fehlende Operation samt Zustand und Dynamik wirklich von einer vorhandenen Quelle in die andere übertragen.** So kann die universelle Hypothese an einem neuen, entscheidbaren Anschluss wachsen. Kein neuer RH-Beweis, keine Faktorisierungsbeschleunigung und kein vollständiger TOE-Abschluss wurden in diesem Quellenabgleich festgestellt.

## Belegumfang

`quellenmanifest.json` hält Dateihashes, gelesene Abschnitte und Grenzen der Einsicht fest. `ledger-auszug.json` bewahrt die vollständigen 15 ausgewählten Originalzeilen; `vorhersagen-inventar.json` die aktuelle Zählung mit allen 27 Karten. Die Webprimärquellen wurden in dieser Bestandsaufnahme auf Abstract-/Metadatenebene geprüft; keine Volllektüre ihrer langen Beweise wird behauptet. Ältere Memoryhinweise dienten nur als Suchhilfe und wurden an den aktuellen Originalen überprüft.
