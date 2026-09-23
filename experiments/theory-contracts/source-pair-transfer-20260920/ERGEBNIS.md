# Der gemeinsame Paaroperator — und die fehlende Bindungsdynamik

20. September 2026 · **UR.SOURCE.PAIR_TRANSFER.01 · PARTIAL**

**Der Zusammenhang zwischen E8-Randfeldern und dem nativen Kopplungstensor
ist stärker als bisher gezeigt: Im bereits angenommenen Randmodell
bestimmt derselbe Tensor W die vollständige zeitabhängige Paarantwort.**
Die Antwort lässt sich mit nur zwei ausdrücklich berechneten Funktionen
schreiben. Der bereits vorhandene Ladungsterm bleibt als zusätzlicher
bekannter Zeitfaktor erhalten. Es wurden keine Kopplungen angepasst.

Aus den wirklichen Feldprodukten lässt sich außerdem ein normerhaltender
Paarzustandsraum gewinnen. Wenn die beiden Feldeinfügungen zusammenrücken
und mit ihren berechneten Normen skaliert werden, bleiben alle 2016
Paarrichtungen erhalten. Dieser Grenzübergang bewahrt die vorgegebene
Zeitentwicklung. Sein Fehler ist für alle reellen Zeiten beschränkt:
Bei quadriertem Abstand rho höchstens 5 rho. Das ist eine Aussage über
diese konkrete Paarantwort im gewählten Randmodell, keine Herleitung
der gesamten physikalischen Zeit aus P1/P2.

## Was der resultierende Energieoperator tatsächlich sagt

Die Rechnung liefert im rekonstruierten Paarraum

**Paarenergie = Summe der beiden Einzelfeldenergien + 2 × Projektor auf
die dunklen Paarrichtungen.**

Die zwei Einheiten beziehen sich auf die bereits gewählte konforme
Energienormierung. Sie sind keine Massenprognose in GeV.

| Kanal | Energie gegenüber denselben beiden Einzelfeldern |
|---|---:|
| 60 helle Kopplungsrichtungen | 0 |
| 1956 dunkle Paarrichtungen | +2 |

Die hellen Richtungen sind also günstiger als die dunklen. Sie liegen
aber **nicht unter der Summe ihrer Einzelfeldenergien**. Das ist der
entscheidende Unterschied zur nativen Vermittlerrechnung: Dort entsteht
bei jeder von null verschiedenen Kopplung eine negative Bindungsenergie
im hellen Kanal.
Verglichen wird hier der native Zweiteilchensektor über seiner leeren
Fock-Referenz. Das ist keine neue Berechnung der Feldantwort um den
wechselwirkenden nativen Grundzustand im Sektor N=64.

Bildlich: Zwei Wege führen unterschiedlich hoch über einen gemeinsamen
Ausgangspunkt. Der niedrigere Weg ist deshalb noch kein Tal unter diesem
Ausgangspunkt. Genau dieser Bezugspunkt entscheidet später über
Bindung und Vakuum.

In einer umgeschriebenen Formel taucht tatsächlich der erwartete negative
Term mit W auf. Daneben steht jedoch ein positiver Paarterm. Lässt man
diesen weg, sieht die Rechnung wie native Attraktion aus — man hat dann
aber die Dynamik geändert. Eine globale Verschiebung der Energien kann
das nicht rechtfertigen, wenn Vakuum und Einteilchenenergien erhalten
bleiben sollen.

## Was die vollständige Zeitantwort zusätzlich klärt

Bei endlichem Abstand enthält die Antwort unendlich viele positive
Spektralbeiträge. Ein einzelner gemessener mittlerer Energieoperator
reproduziert diesen Zeitverlauf nicht. Die zusätzliche Quellinformation
ist im kontrollierten Grenzübergang berücksichtigt; sie wurde nicht
durch einen frei gewählten kleinen Oszillator ersetzt.

Das liefert einen konkreten Fortschritt gegenüber einem bloßen
Tensorvergleich: Zustandsnormen, Zeitverlauf und Grenzfehler sind jetzt
gemeinsam bestimmt. Eine Identifikation mit den vollständigen nativen
Fermion- und Bosonoperatoren folgt daraus weiterhin nicht. Insbesondere
wird aus einer Antwort zusammengesetzter Felder kein neu hergeleiteter
mikroskopischer Vierfermionterm.

## Abgleich mit der anderen Lane

Die neue Rechnung **UR.SOURCE.SECTOR_RECONSTRUCTION.01** wurde gelesen
und reproduziert. Sie gewinnt die ursprünglichen geladenen Felder aus
den vier nötigen Sektoren der geraden Randbeschreibung zurück, samt
ihren vorgegebenen Übergängen und ihrer Zeitentwicklung.

Beide Ergebnisse ergänzen sich: Die Sektorrekonstruktion erhält die
Felder; die jetzige Rechnung bestimmt ihre vollständige Paarantwort.
Weil der Hamiltonoperator dabei derselbe bleibt, erzeugt die
Sektorrekonstruktion keine zusätzliche negative Bindungsenergie.

**Für die Gesamtlösung fehlt damit eine präzise benennbare Herleitung:**
Ein Operator beziehungsweise Mechanismus der ursprünglichen Quelle muss
die benötigte gebundene Paarenergie liefern, ohne Vakuum,
Einteilchenenergien, Ladungen oder Feldprodukte nachträglich umzudefinieren.
Die bisher gewählte Zehnkanal-Randtheorie und ihre E8-Energie sind selbst
weiterhin nicht aus P1/P2 hergeleitet; auch das verwendete Randvakuum ist
eine festgehaltene Voraussetzung.

Die vollständige TFPT-Lösung ist damit noch nicht bewiesen. Der neue
Befund verhindert aber, dass ein übereinstimmender Tensor oder ein
relativer Energieabstand fälschlich als bereits hergeleitete
Bindungs- und Vakuumdynamik weiterverwendet wird.

[Mathematische Herleitung](PROOF.md) · [Zertifikat](certificate.json) ·
[Quellenbindungen](source_manifest.json)
