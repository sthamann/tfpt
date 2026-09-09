# TFPT-Fortsetzung: dynamischer Clock-Test und quellenbasierte Feldreferenz

2026-09-08, lokal auf b803b7e5. Drei parallel bearbeitete, abgegrenzte
Arbeiten: Clock-Dynamik, unabhängiger Markierungs-/Zustandscheck und
Referenztransport für den Feldgrenzwert. Kein neuer physikalischer Parent
oder ausgewählter Zustand stillschweigend hinzugefügt.

## Was jetzt tatsächlich geschlossen ist

**Endlicher primitiver Clock-Sektor:** Die vier Bilinearoperatoren sind
explizite Eigenoperatoren der unveränderten Quelldynamik. Zwei erhalten
die Gesamtteilchenzahl, haben Frequenzbeträge (sqrt(3)±1)t und eine exakt
berechnete Gibbs-Zweipunktfunktion. Die Grundfrequenz u fällt heraus.
Alle thermischen Gewichte wurden gegen direkte Spuren auf sämtlichen
256 Fock-Zuständen geprüft. [Beweis und Daten](README.md).

**Präzise Vakuumgrenze:** Am bisher geprüften Punkt u=1,t=1/8 annihilieren
beide langsamen Transfers und ihre Adjungierten den eindeutigen Grundzustand.
Das folgt aus einer exakten Positivitätsurkunde, nicht aus numerischem
Nullsetzen. Für t>0,u>=0 sind die anderen Grundzustandsfenster einschließlich
thermischer Nullmoden-Endpunkte vollständig angegeben. Eine hilfreiche
andere Wahl von u/t wäre noch keine TFPT-Herleitung.

**Zugang und Markierungen:** Separate Carrier-Zahlen sind in der Quelle
selbst nicht erhalten; Marker sind deshalb nicht automatisch Gauge-
Constraints. Trotzdem tragen die primitiven Operatoren Familienladung.
Außerdem kommutieren sie mit dem gesamten vorhandenen dynamisch erzeugten
Boundary-Feldzugang. Auch ihr thermisches Signal schließt diese Zugangs-
lücke nicht. [Unabhängiger Gegencheck](../clock-marking-audit/README.md).

## Feldgrenzwert: neuer konstruktiver Fortschritt

Für die Current-Referenz werden nun konkrete Rand-Quasimoden aus der
unveränderten QWZ-Quelle verwendet und auf deren tatsächliche besetzte
beziehungsweise unbesetzte Spektralräume projiziert. Das ergibt eine
explizite polarisationsverträgliche Isometrie, keine Identifikation allein
über Matrixdimensionen.

Auf dem verbleibenden Raum behält die neue Vergleichsreferenz denselben
aus der Quelle stammenden Empty-Arc-Generator an jedem Endpunkt bei.
Dieser gemeinsame Rest hebt sich in neutralen Feldwörtern exakt auf,
beeinflusst aber die während der Entwicklung auftretenden Übergänge.
So bleibt die Referenzamplitude gleich, während der relevante Vergleich
der gesamten Operatorgeschichte deutlich besser wird.

Beispiel: halber Kreis, Standardfenster ohne Anpassung an Messwerte.
Gemessene Integrale des Hilbert-Schmidt-Abstands der gedrehten Kreuzblöcke:

| N | Rest auf null gesetzt | Gemeinsamer Quellenrest behalten |
| ---: | ---: | ---: |
| 8 | 0.87723 | 0.47514 |
| 16 | 0.83210 | 0.27660 |
| 24, zusätzliche Zwischengröße | 0.85457 | 0.19409 |
| 32 | 0.88022 | 0.15015 |

Die N24-Prüfung verwendet dieselbe zuvor festgelegte Referenzvorschrift.
Das sind endliche Quadraturdiagnosen, weder zertifizierte Integrations-
Fehlerschranken noch ein Beweis der asymptotischen Abnahmerate.

Zusätzlich folgt aus der schon bewiesenen Quellen-Energiezählung eine
explizite Heat-Trace-Schranke für den beibehaltenen Rest. Dadurch ist
die Referenzgröße A0=O(sqrt(t)) kontrolliert. In Verbindung mit der
Feldnormierung genügt nun als vollständig formuliertes hinreichendes Ziel

    integral ||Q(B_N-B_ref,N)P||_HS ds = o(N^(-3/16)).

Dieses strengere Ziel ersetzt für diese Referenz die bisher unbewiesene
Annahme A0=O(sqrt(log t)). Bewiesen sind die Referenzkonstruktion und ihre
Größenkontrolle, nicht die noch erforderliche mikroskopische Fehlerrate.
Separat offen bleiben die Referenz-zu-Current-Konvergenz, gleichmäßige
Nahdiagonalkontrolle und die gemeinsamen geladenen Feldoperatoren.
[Referenztransport, Beweise und Kontrollen](../history-reference-transport/README.md).

## Die nächsten entscheidenden Schritte

1. Für diese konkrete Referenz den mikroskopischen Geschichtsfehler
   analytisch begrenzen, statt weitere kleine Determinantenfehler als
   Grenzwertersatz zu verwenden. Die bewegte P/Q-Rahmenwirkung und der
   gemeinsame Quellenrest müssen im Beweis erhalten bleiben.
2. Für die Clock einen aus TFPT begründeten Carrier-Zugang und die
   Präparation herleiten. Eine Bandbesetzung oder Parameterwahl, die eine
   Antwort erlaubt, ist jetzt genau bekannt, aber noch nicht ausgewählt.
3. Die lokalen geladenen Felder mit Carry, Familienwirkung, Adjungierten
   und Noether-Strom auf demselben Objekt zusammenführen. Die endliche
   Clock-Rechnung allein liefert weder Chiralität noch 3+1D-Kontinuum.

Das exakte Verhältnis der zwei langsamen Frequenzen ist 2+sqrt(3).
Seine reell-quadratische Einheiteneigenschaft ist ein konkreter algebraischer
Anschluss an die logarithmische Kaskadenidee, aber die Quelle implementiert
damit noch keine hyperbolische Iteration und kein vollständiges Primzahl-
spektrum. Keine neue RH- oder Faktorisierungsbehauptung.

## Verifikation und Repo-Stand

**54 Tests je Modus** in dieser Runde erneut ausgeführt: 17 neue Clock-
Tests, elf neue Referenztests und 26 Regressionen. Ein unabhängig
erkannter Transpositions-/Vorzeichenfehler im neuen Einteilchen-Comparator
wurde nach systematischer Reproduktion korrigiert und durch einen direkten
Fock-Sektorvergleich abgesichert; Frequenzen und Vakuumurkunde blieben
unverändert. [Prüfprotokoll](TEST_RESULTS.md).

Alle Änderungen lokal: neue Forschungsordner, Index und Arbeitsnotizen.
Vorhandene fremde Änderungen erhalten; Quellen, Paper, Website und T1-T8-
Abschlussmarker nicht verändert. Kein Commit oder Push dieser Runde.
Die vollständige TOE bleibt offen; abgeschlossene endliche Teilrechnungen
werden nicht mit ihrer fehlenden gemeinsamen physikalischen Herleitung
gleichgesetzt.
