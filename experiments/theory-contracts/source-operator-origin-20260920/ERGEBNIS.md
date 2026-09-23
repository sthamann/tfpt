# Herkunft der Wechselwirkung: der nächste tragende Anschluss ist entschieden

20. September 2026 · `UR.SOURCE.OPERATOR_ORIGIN.01` · **PARTIAL**

**Eine vollständige TFPT-Lösung ist weiterhin nicht bewiesen. Neu ist ein exakter Herkunftstest, der die Arbeit wesentlich enger führt:** Das unveränderte native Fockmodell kann die zuletzt konstruierten ungeraden lokalen Randfelder unter dem festgehaltenen gemeinsamen Gruppenwörterbuch nicht liefern — auch nicht durch beliebig komplizierte Zusammensetzungen. Der erste fehlende Baustein liegt vor der Dynamikoptimierung: im Übergang von der ursprünglichen Clifford-Struktur zur tatsächlich ausgeführten Feldalgebra.

## 1. Warum dieser Test die Suche verändert

Die native Quelle enthält eine echte Wechselwirkung zwischen 64 Fermionmoden und 60 Bosonkanälen. Sie war deshalb der begründet erste Kandidat für die bislang nur diagnostisch gewählten Randwechselwirkungen. Die Prüfung betrachtet zwei interne Vierteldrehungen zusammen. Bei jedem vorhandenen nativen Quellfeld heben sich ihre Phasen auf. Die benötigten ungeraden lokalen Randfelder erhalten dagegen ein Minuszeichen.

| Dasselbe zentrale Gruppenelement | Wirkung |
|---|---:|
| alle 64 nativen Fermionmoden | +1 |
| alle 60 nativen Bosonmoden | +1 |
| jeder Operator auf diesem nativen Fockraum | +1 |
| jedes ungerade lokale Feld im gemeinsamen T-Randwörterbuch | −1 |

Aus Feldern, auf denen diese Transformation identisch wirkt, entsteht kein Feld mit dem entgegengesetzten Zeichen. Der Beweis gilt für die ganze Operatoralgebra; er hängt nicht an einer beschränkten Anzahl getesteter Produkte. Mehr Kopplungswerte, andere Zustände oder höhere Polynomgrade würden dieses Problem unverändert lassen.

Formal ist das Element das diagonale Zentrum von Spin(10)×SU(4). Die Quelle trägt `(bar16,bar4)` und `(10,6)` mit zentralem Zeichen+1. Die lokalen c-Felder tragen `(16,bar4)+(bar16,4)` mit Zeichen−1. Für jeden integralen Randvektor x ist dieses Zeichen exakt `(-1)^(x^T K x)`, also die geerbte Fermionparität. **Die native Quelle besitzt Fermionen; ihre Verknüpfung von Gruppenwirkung und Parität passt aber nicht zu diesem Randwörterbuch.**

Das widerlegt die konkrete unveränderte Quellenidentifikation. Es widerlegt weder die übrigen TFPT-Befunde noch jede mögliche Feldzuordnung. Insbesondere ist das alternative native F_aux-Wörterbuch von der gemeinsamen T-Einbettung verschieden und darf nicht unbemerkt an deren Stelle treten.

## 2. Der Folgeschritt wurde bereits an der Originalquelle geprüft

Vor der Auswahl des geraden Familien-Unterraums enthält der ursprüngliche Clifford-Aufbau tatsächlich sechs Übergangsmatrizen mit der richtigen algebraischen Struktur:

\[
6\otimes\bar4\longrightarrow4.
\]

Sie tragen das fehlende zusätzliche zentrale Zeichen. Ihre 90 Kovarianzgleichungen sind exakt geprüft. Das ist der konkrete Ansatzpunkt, den die zusammengeführten Ergebnisse freilegen.

Der nächste entscheidende Test zeigt jedoch: In der **tatsächlich exportierten geraden Familienkompression** verschwinden alle sechs einzelnen Übergänge:

\[
P_{\rm even}\gamma_aP_{\rm even}=0.
\]

Die Quelle nutzt ihre geraden Produkte als Symmetriegeneratoren. Sie führt die sechs chiralen Übergänge nicht als zusätzliche physikalische Felder oder Hamiltonoperatoren des 64-CAR/60-CCR-Modells aus. Ein im Rechenaufbau benutzter Hilfsraum ist damit noch keine ausgeführte Teilchensorte. Auch die korrekte physische Fermionparität muss beim Übergang von Zuständen zu Feldoperatoren separat erhalten werden.

**Der jetzt präzise Herkunftsgate:** Aus der ursprünglichen Quelle muss hervorgehen, ob und wie diese vor der Kompression vorhandene geladene Struktur als lokaler graduierter Feldoperator mit derselben Zeitentwicklung erhalten bleibt. Sie frei wieder einzusetzen wäre eine neue Modellannahme. Erst nach diesem Nachweis wäre eine weitere n/z-Kopplungsrechnung begründet.

## 3. Was die beiden anderen Anschlüsse beitragen

**Rotor:** Die vorhandene elektrische Dynamik erzeugt exakt eine Quartik-Komponente `-q0*q1/7200` im Doppelkommutator. Sie ist kein bereits hergeleiteter statischer Hamiltonterm. Der direkte Test eines originalen Gauß-neutralen Zustands zeigt eine Lecknorm zum Nichtnullfluss von `1/288`; das Hopping ist mit `a/Delta_E=50/3` größer als die elektrische Lücke. Diese Quotienten betreffen nur die elektrische Lücke. Der vollständige Folgetest behält die ebenfalls ursprüngliche High-Masse 4 und ergibt **positiv** eine kontrollierte Rang-eins-Spektralreduktion: `0.01996381<E*<0.01996382`, mit Fastanteil-Verhältnis kleiner als 1/4000. Das widerlegt eine pauschale Aussage, die Quelle besitze gar keine Eliminationshierarchie. Der verbleibende Gauß-neutrale Low-Raum ist auf dieser Kante jedoch eindimensional. Das Ergebnis ist eine skalare Energiekorrektur, noch kein Mehrfeld-Quartikterm oder zehnkanaliger Randoperator.

**Austausch der Randwechselwirkungen:** Der rationale Austausch n↔z wirkt exakt auf einem gemeinsamen Untergitter vom Index 2. Dieses enthält die Klassen 0 und c und damit gerade die zuvor gefundenen ungeraden Spinoren. Die übrigen lokalen Klassen v und s liegen außerhalb. Ein formaler Labeloperator erfüllt `D^2=1+eta`; eine vollständige lokale Defekt-/Sektorenregel und ihre Herkunft aus der Quelle sind damit nicht konstruiert.

Diese beiden Zeichen sind verschieden:

| lokale Klasse | 0 | v | s | c |
|---|---:|---:|---:|---:|
| Austausch-Untergitter: eta | + | − | − | + |
| diagonales Gruppenzentrum | + | − | + | − |

Der naive Zusammenschluss „nur die nativen zentral neutralen Felder behalten und danach den Austausch-Unterraum auswählen“ lässt daher nur Klasse 0 übrig. Er erzeugt das gewünschte c-Feld nicht. Eine Quelle muss das fehlende zentrale Zeichen wirklich tragen.

Auch der bereits vorhandene metaplektische Half-Deck aus `SEAM.CLIFFORD.MODULAR_S.01` ist nicht automatisch dieser Austausch: Seine beiden rationalen E8-Gitter haben nur den Nullvektor gemeinsam. Mit einem unverändert angehängten Zweierpaar besitzt der Schnitt Rang 2; beim benötigten gemeinsamen Randgitter ist der Schnitt von Rang 10 und Index 2. Eine bloße gemeinsame Koordinatenänderung kann diesen Unterschied nicht beseitigen. Der Zweierindex der Clifford-Gruppe ist kein Beweis für den benötigten Zweierindex des lokalen Gitters.

## 3b. Neu eingetroffener Lane-Befund: dieselbe Lücke als Ladungssektor

Während des Abgleichs wurde `UR.SOURCE.ROTOR_GAUSS.01` neu registriert. Die andere Lane reduziert den Gauß-physischen Rotorraum exakt und findet innerhalb der bereits deklarierten E8-Randverklebung die notwendige Kandidaten-Eichladung `g=±K n`. Ihre Erweiterung zeigt: Die beiden lokalen Spinorfeldfamilien tragen genau+1 und−1; die E8-Ströme bleiben neutral. Das ist noch kein tatsächlich realisiertes Gauging.

Die gemeinsame Rechnung führt nun zu einer einzigen universellen Beziehung:

\[
\boxed{\text{zentrales Vorzeichen}
=\exp(i\pi\,\text{Kandidaten-Eichladung})
=\text{Fermionparität}.}
\]

Damit ist der fehlende Anschluss genauer benannt: **ein ursprünglicher, lokal korrekt behandelter Sektor mit ungerader Kandidaten-Eichladung.** Der bereits geprüfte Clifford-Übergang zeigt die algebraische Stelle für dieses Vorzeichen, seine physische Feld- und Zeitrealisierung fehlt weiterhin.

Die Kombination ändert außerdem die kritische Modellannahme: `n` ist unter g neutral, `z` hat Ladung2. Der nackte z-Term darf nach einer tatsächlichen Eichung nicht unverändert im Hamiltonian bleiben. Die gleiche Quelle kann deshalb nicht ohne weitere Herleitung gleichzeitig als neutrale E8-Eichkonstruktion und als bisheriger nackter n/z-Ising-Punkt behandelt werden.

## 4. Korrektur, Prüfung und vollständiger Scope

Die zunächst erwogene „nur im Familienanteil antilineare Abbildung“ wurde verworfen. Auf einem komplexen Tensorprodukt ist sie nicht wohldefiniert. Linear verhindert das Familienzentrum die Abbildung; global antilinear verhindert sie das Spin(10)-Zentrum. Dieser einfache Gruppenbefund wurde unabhängig geprüft. Die anschließende Verstärkung auf die gesamte Operatoralgebra, die universelle Randparitätsidentität und der Clifford-Projektionstest sind hier explizit bewiesen und exakt nachgerechnet. Der unabhängige Review wird nicht nachträglich als Prüfung dieser späteren Verstärkungen ausgegeben.

Die drei Rechenpakete wurden normal und mit deaktivierten Python-Assertions ausgeführt; die Zertifikate stimmen byteweise überein. Quellenhashes sind gepinnt. Das sind mathematische Prüfungen der angegebenen Modelle, keine empirische Bestätigung oder neue physikalische Gate-Schließung. Keine Änderung an Papers, Originalquellen oder Verifikationsledger.

Die letzte vollständige Rahmenprüfung bleibt erhalten: P1/P2, Compiler/E8, alpha-Fixpunkt, Flavor, Clocks und die ursprünglichen Quellmodelle bilden weiterhin das Gesamtproblem. Hier wurde der erste tragende Anschluss des zuletzt verfolgten lokalen Randwegs entschieden. Quellenselektierte Feldalgebra, Zustand, gemeinsame physische Zeit, 3+1D-Kontinuum und vollständige TFPT-Schließung bleiben offen.

## Nachweise

- [Gruppenwirkung, universeller Operatorausschluss und ursprünglicher Clifford-Folgetest](family_intertwiner/PROOF.md)
- [Unabhängige Prüfung des linearen und antilinearen Gruppenbefunds](family_intertwiner/INDEPENDENT_GROUP_REVIEW.md)
- [Exakte Rotorwirkung und Eliminationsgrenze](rotor_audit/PROOF.md)
- [Gemeinsames Untergitter, Austauschvertrag und Half-Deck-Vergleich](glue_correspondence/PROOF.md)
- [Quellenvergleich mit nachgetragenem tatsächlichem Gate-Ergebnis](source_selection/REVIEW.md)
- [Reproduktionszertifikat](validation.json)

Zum methodischen Unterschied von exakter Dualität, diskretem Gauging und Projektion wurde [Pace, Chatterjee und Shao](https://arxiv.org/html/2412.18606v2) herangezogen. Diese Literatur begründet keine TFPT-Quellidentifikation; die obigen Ausschlüsse beruhen auf den angegebenen Originaloperatoren und exakten Identitäten.
