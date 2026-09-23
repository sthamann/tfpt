# Quellenprüfung: Quellsymmetrie, Verfügbarkeit und Lorentztypen

Stand: 15. September 2026. Eigenständiger Teil-Audit der ersten neuen Anlage und dreier Programme. Keine Änderung der gelieferten Programme, Ergebnisdateien oder Dokumente. Keine Aussage, dass T1–T8 geschlossen seien.

## 1. Reproduktion

Alle drei Programme wurden vollständig gelesen und anschließend in isolierten Kopien ausgeführt. Die relevanten Tensoren wurden an ihre von den unveränderten Programmen erwarteten relativen Orte kopiert. Normaler und optimierter Lauf reproduzieren jeweils die gelieferten Ergebnisdateien byteidentisch, ohne Standardfehlerausgabe:

| Programm | Gelieferte Prüfbedingungen | Reproduktion |
|---|---:|---|
| `operation_symmetry.py` | 944 | PASS, identisch |
| `symmetry_availability.py` | 31 | PASS, identisch |
| `lorentz_types.py` | 152 | PASS, identisch |
| Summe | 1127 | normal und `-OO` |

Die Zusatzprüfung `check_scope.py` rechnet kleine exakte Gegenprüfungen zur Reichweite der Aussagen. Das ausführbare Reproduktionsprogramm ist `replay.py`; Quellenpins, Kopien, Originalberichte und Ausgaben liegen in diesem Auditordner. `replay_receipt.json` dokumentiert alle Pins und die Unverändertheit der Eingaben.

Programm-Pins:

| Quelle | SHA-256 |
|---|---|
| `operation_symmetry.py` | `ec93f759d6582f42542a597bf916ee2a62a51c510240aa777ae439e90fe28382` |
| `symmetry_availability.py` | `88cc3e3361a198fe7b1b32a7174f3dd45f341106978d8abd8d5722e0cb631967` |
| `lorentz_types.py` | `43777c81ea8ba2d2ae12b711321a54abd7f7152a326611a296598d5c5dd463da` |
| Nativer Tensor | `3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763` |

Die Erzählung über zwei unabhängig entstandene, vollständig übereinstimmende Programme ist durch diese Reproduktion **nicht** geprüft: Vorgelegen hat die erhaltene Fassung mit 944 Guards, nicht die vorherige Fassung mit 528 Guards.

## 2. Bestätigte Mathematik

Der N=3-Raum zerfällt als Darstellung von Spin(10) × SU(4) in sieben Isotypien. Drei haben Multiplizität zwei, die anderen vier Multiplizität eins. Die zwei Fockteile Λ³(C⁶⁴) und C⁶⁰⊗C⁶⁴ sind jeweils multiplizitätsfrei; der gesamte N=3-Raum ist es ausdrücklich **nicht**.

Die irreduziblen Dimensionen sind 24000, 11200, 2688, 2880, 576, 320, 64; die mit Multiplizitäten gewichtete Summe ist 45504. Die Spin(10)-Darstellung mit Dimension 16 in BF und Λ³ ist in den angegebenen Gewichten die konjugierte Spinordarstellung; die Dimensionskurzschreibweise `16` darf diese Information nicht ersetzen.

Bestätigt sind:

- die exakte Zerlegung über Gewichtsmultiplizitäten und Racah-Alternation;
- `C(560)=117/4` in der erklärten Casimir-Normierung;
- die Quellenintertwiner für alle 60 Lie-Erzeuger;
- `rank C3=3776`, `dim ker C3=37888`;
- Spektrum von `C3 C3†`: 0,7,10,12 mit Multiplizitäten 64,2880,576,320;
- die drei dunklen Typen mit Gesamtcasimir 45, aber getrennten Spin-Casimiren 141/4,117/4,165/4;
- für den **gewährten** Satz X,Nb eine assoziative Algebra der komplexen Dimension 14;
- für alle punktweise symmetrieinvarianten Operatoren die Dimension 16;
- nach zusätzlicher Gewährung aller 60 Gruppenerzeuger die assoziative Dimension 743583744 und Kommutantdimension 7.

Die Eigenwertzuordnung im Code prüft pro S-Eigenwert einen Vektor, nicht eine vollständige Basis dieses Eigenraums. Zusammen mit der unabhängig geprüften Multiplizitätsfreiheit, der Kommutation mit allen Erzeugern und der eindeutigen Dimensionszuordnung der BF-Teilsummen ist die Zuordnung trotzdem abgesichert. Die Guard-Beschriftung »entire eigenspace« ist als direkte Beschreibung dieser einen Rechnung zu weit.

## 3. Invarianz und Kovarianz auseinanderhalten

Mit `A0=Alg*(X,Nb)` und Gruppenwirkung ρ bezeichne

`C = End_G(H3) = ⊕_i End(C^{m_i}) ⊗ I_{d_i}`.

Dann gilt `A0 ⊂ C`, `dim A0=14` und `dim C=Σ m_i²=16`. Jedes Wort aus X und Nb kommutiert mit ρ(G). Nichtzentrale Lie-Erzeuger können deshalb aus diesem Alphabet nicht entstehen. Dieser Ausschluss ist korrekt und bleibt richtig, wenn nur ein fixes H statt zweier unabhängiger Kontrollen gewährt ist.

Nach Gewährung der Gruppenerzeuger entsteht dagegen

`Afull = ⊕_i End(C^{m_i} ⊗ V_i)`.

Diese Algebra ist **unter Gruppenkonjugation stabil**, aber ihre Operatoren sind nicht sämtlich invariant. In `symmetry_availability.py` ist die Kennzeichnung `symmetry_invariant: true` für diese Zeile daher falsch. Der Kommutant von Afull ist die sieben-dimensionale skalare Blockmitte.

Sieben ist ein Boden, solange alle zusätzlichen Operationen diese sieben Isotypie-Projektoren erhalten; insbesondere senken zusätzliche punktweise G-invariante Operationen den bereits erreichten Kommutanten nicht weiter. Sieben ist aber **kein** universeller Boden für unter G stabile Algebren oder alle denkbaren nativen Verträge. `End(H3)` ist unter jeder Gruppenkonjugation stabil und hat nur den skalaren Kommutanten. Ein exaktes 2×2-Gegenmodell in der Zusatzprüfung macht die Unterscheidung direkt sichtbar.

Die Zahlen sind zudem Dimensionen **komplexer assoziativer Sternalgebren**, keine nachgewiesenen Dimensionen einer dynamischen Lie-Algebra oder erreichbaren Unitärgruppe. Burnside liefert nicht automatisch beliebige ausführbare Gatter auf jedem irreduziblen Block.

## 4. Verfügbarkeit ist keine universelle Ja/Nein-Frage

Ein vorgegebener Hamiltonoperator allein gewährt nicht bereits das unabhängige Schalten von X und Nb. Am erklärten Punkt g/Δ=1/20 besitzt ein fixes H im N=3-Raum acht verschiedene Energien, also nur eine acht-dimensionale kommutative Spektralalgebra. Die großzügigere Annahme unabhängiger Kontrollen X,Nb ergibt 14.

Eine treue, auf die Multiplizitätsräume reduzierte rationale Matrixrechnung ergibt:

| Zusätzlich gewährter Satz | Assoziative Dimension |
|---|---:|
| Nur fixes H=Nb+X/20 | 8 |
| X,Nb | 14 |
| X,Nb plus Projektor auf genau einen dunklen Typ | 15 |
| X,Nb plus Spin(10)-Casimir | 16 |
| X,Nb plus SU(4)-Casimir | 16 |
| X,Nb plus Gesamtcasimir | 14 |

Bereits **einer** der getrennten Casimire reicht zur vollständigen Trennung der drei dunklen Typen. Die zwei fehlenden Algebradimensionen sind kein Beweis, dass genau zwei physische Griffe fehlen. Die Dimension 15 zeigt eine mögliche invariante Zwischenstufe. Die behauptete universelle Dichotomie »getrennte Griffe ja oder unverändert 14« und das `IF AND ONLY IF` zur Verfügbarkeit der vollen Symmetrie sind daher zu stark.

Die zusätzlichen Projektoren und Casimirkontrollen werden hier nur als algebraische Gegenbeispiele verwendet. Ihre Implementierung aus dem Compiler wird nicht behauptet.

## 5. Der Clock-Satz ist im gelieferten Checker nicht geprüft

`operation_symmetry.py:478` schreibt den Normalisator- und Nichts-hinzufügen-Satz als `need(True, ...)`. Insgesamt enthält diese Datei neun solche als Prüfbedingungen gezählten theoretischen Folgerungen. Einige sind durch die vorausgehende Mathematik gut begründet; der bloße grüne Guard zertifiziert sie jedoch nicht unabhängig.

Die direkte Clock-Definition liegt in `universalraum-native-operations-ground-response-20260915/common.py`, Funktion `clock_lift`, ab Zeile 187: eine Permutation der fünf Oszillatorachsen wird mit Exterior-Vorzeichen auf den geraden Spinorraum gehoben; `GF=G16⊗I4`. Der Bosonlift wird entsprechend gebaut und die Tensorintertwining-Gleichung geprüft. Eine neue direkte Prüfung der Clock-/Casimir-Beziehungen erfolgt im parallelen Hauptstrang, nicht in diesem Audit.

## 6. Feldtyp: was tatsächlich erzwungen ist

Für ein **lokales, ableitungsfreies Bilinear zweier gleichhändiger Weylfelder**, das alle 64 inneren Quellenmarken unverändert als unabhängige innere Komponenten und genau den gegebenen antisymmetrischen Tensor W verwendet, gilt

`(1/2,0) ⊗ (1/2,0) = (1,0) ⊕ (0,0)`.

Die skalare Epsilon-Kontraktion zusammen mit antisymmetrischem W ist im gemeinsamen Index symmetrisch und verschwindet wegen Grassmann-Antikommutation. Der symmetrische Spinortensor, also der (1,0)-Kanal, bleibt nichtverschwindend. Im genannten Vertrag ist dies korrekt. Ein zusätzliches unabhängiges gleichgeladenes Hilfsdublett erlaubt stattdessen wieder die skalare Kontraktion.

Die Zahlen 180/128 beziehungsweise 60/256 zählen **komplexe lokale Feldkomponenten im jeweiligen direkten Tensorprodukt-Ansatz**. Sie zählen nicht automatisch zusätzliche unabhängige physische Oszillatoren oder propagierende Freiheitsgrade. Diese hängen von Kinetik, Nebenbedingungen, positiver Energie, Teilchen-/Antiteilchenstruktur und dem tatsächlichen Feldadapter ab. Deshalb folgt aus der Multiplikation mit zwei oder drei kein allgemeiner Ausschluss jeder relativistischen Lesart mit den nativen Modenzahlen.

Vor allem folgt daraus keine vorgeschriebene Reihenfolge »erst räumliche Skalierung, dann Feldwörterbuch«. Lokale Darstellungstypen und mögliche Kinetik können vor einer Skalierungsrechnung geprüft werden. Welche Feldkomponenten tatsächlich aus dem räumlichen Quellprozess entstehen, muss anschließend gemeinsam mit dem Adapter untersucht werden.

### Konkreter Gegencheck jenseits der ableitungsfreien Klasse

Der allgemeine Satz »ein Vektor verlangt ψ†ψ und scheitert deshalb an der Ladung« ist falsch, sobald Ableitungen zugelassen werden. Beispielsweise ist

`J^A_mu = Σ_IJab M^A_IJ ε_ab ψ_Ia ↔∂_mu ψ_Jb`

ein Lorentzvektor mit Ladung −2. Die Ableitungsantisymmetrisierung macht ihn bei antisymmetrischem M nichtverschwindend. Für M=ε und zwei inneren Marken liefert die exakte Grassmann-Jetrechnung vier nichtverschwindende Monome mit Koeffizienten +2,−2,−2,+2. Ein entsprechend geladener Vektorvermittler könnte algebraisch durch `b†_mu J^mu + h.c.` koppeln, ohne Ladungsverletzung.

Das ist **nur ein Gegenbeispiel gegen den überbreiten Ausschluss**, keine native Lösung: Es fügt eine Ableitung und einen Feldtyp hinzu; bei kanonischen 4D-Felddimensionen ist es ein höherdimensionaler Kopplungsterm. Gesunde Kinetik, Quellenherkunft, Skalierung und T1–T8 werden dadurch nicht bewiesen.

## 7. Konsequenz

Die neuen Quellen verkleinern und präzisieren den endlichen N=3-Operationsraum. Sie schließen weder die physische Verfügbarkeit der Operationen noch den Lorentzadapter. Die sachlich tragfähige Integration übernimmt die Zerlegung, Casimire, 14/16/7 im jeweils erklärten Vertrag sowie den eingeschränkten Feldtypsatz; sie ersetzt die überbreiten Ausschlüsse und die behauptete Programmumkehr durch explizite Bedingungen.
