# RH-/TFPT-Abgleich und bereinigter E8-Spektralbeobachter

8. September 2026. Abgeschlossene begrenzte Untersuchung. Neue Quellen schreibgeschützt gelesen; keine fremden Läufe, Dateien oder Parameter verändert.

**Es gibt zwei neue lokale Theorieergebnisse und einen präziseren arithmetischen Prüfbeobachter. Ein schneller allgemeiner Faktorisierungszugang wurde nicht gefunden.** Die bekannte E8-/Teilersummenverbindung wird nicht als neuer Durchbruch ausgegeben.

## Neuer RH-Stand

Der [neue Ergebnisbericht](</Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Drei_gezielte_Reserven_lokaler_Nachweis_2026-09-08.md>) ist nach dem bisherigen Snapshot entstanden. Drei gezielt konstruierte Antwortfunktionen erweitern den bisherigen 84-Funktionen-Raum auf 87 Funktionen. Dadurch besteht die vollständige geschützte untere Nachweisform beider Paritäten für den festen Vergleich L=9/4, N=160, J=192, K=320.

Die ursprünglichen Operatorfehler und der vollständige unendliche Rest bleiben erhalten. Die dritte Antwort benötigte eine Wiederholung mit 8192 und 9216 Bit; dieselben exakt eingefrorenen Kandidaten wurden verwendet. Der Bericht und das gespeicherte Ergebnis stimmen in `REFINED_EVEN_REPLAY_VERIFIED`, `PASS_REUSED_ORIGINAL_WINDOW`, `RH_proved=false` und `new_larger_window=false` überein. Diese Statuswerte wurden hier aus den Quellen gelesen, nicht durch erneute Ausführung des Beweissystems erzeugt.

Das ist eine substanzielle lokale Reparatur. Die vorher bewiesene notwendige Rangbedingung r≥2 bleibt damit konsistent; drei konkrete Funktionen sind nun hinreichend, aber drei wurde nicht als minimales mögliches Ergebnis bewiesen. Die globale kofinale Fensterfamilie und ihr Grenzübergang bleiben offen.

Übertragbarer Mechanismus: Ein nachgewiesener Gegenzeuge führt zu einer vollständigen Rückantwort; deren schon vorhandener Anteil wird global entfernt, bevor neue Information ergänzt und die ganze Form erneut geprüft wird. Für Faktorisierung ist zusätzlich eine günstige, N-abhängige Gegenzeuge-/Antwortabbildung erforderlich.

## Neuer TFPT-Stand

Der neue [Plaquette-/Würfel-Bericht](</Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/plaquette-gap-certificate/README.md>) behandelt erstmals in dieser Fortsetzung positive Lücken der vollständigen neutralen lokalen Systeme mit allen ganzzahligen elektrischen Flüssen:

| Räumliche Einschränkung | Eingeschlossene erste Lücke, gerundet |
|---|---:|
| Einzelne Plaquette | 0,0195776909527 bis 0,0204013098746 |
| Gekoppelter dreidimensionaler Würfel | 0,0177576051837 bis 0,0221667420299 |

Die rationalen Endpunkte und ihre Herleitung aus den berichteten Energieintervallen wurden hier zusätzlich mit exakter Bruchrechnung geprüft. Der vollständige Hamiltonian-Beweis wurde nicht unabhängig nachgerechnet. Externe Kopplungen außerhalb der Zelle sind aus der räumlichen Einschränkung entfernt; die Flussrichtungen innerhalb der Zelle werden nicht abgeschnitten. Es wird weder eine gleichmäßige Volumenlücke noch eine eindeutige Bulk-Vakuumauswahl behauptet.

Der Bericht enthält außerdem ein exaktes großes-Volumen-Gegenbeispiel gegen die verwendete nackte P/Q-Trennung: Ein Q-Zustand liegt bei L=28 unter der nackten extensiven P-Referenz. Er liegt weiterhin oberhalb des entsprechend gekleideten Vergleichszustands. Daraus folgen weder negative physische GNS-Energie noch Gaplessness. Dies begrenzt eine konkrete Beweismethode, nicht die gesamte Theorie.

## Unser neuer Prüfbeobachter

Die vollständige [Herleitung](THEORIE.md) definiert

\[
D_B(q)=\sum_{d>B,k>B}d^3q^{dk}.
\]

Diese Funktion lässt sich aus E4 durch explizite rationale Abzüge der kleinen Teiler- und Kofaktorreihen bilden. Für N=pq mit verschiedenen Primzahlen p,q>B ist ihr N-ter Koeffizient p³+q³. Das bekannte triviale N³ wird dabei ebenfalls entfernt. Faktoren werden weder beim Definieren des Beobachters noch beim Bilden der Abzüge vorausgesetzt.

Ein absoluter Fehler von höchstens **4N** im einzelnen Koeffizienten genügt zur exakten Wiederherstellung von p+q und dann der Faktoren. Das folgt aus einem benachbarten Abstand >9N für die monotone Funktion s³−3Ns auf den zulässigen ganzen s≥ceil(2√N). Die offene kostentragende Aufgabe ist, diesen einzelnen Koeffizienten schnell und mit einem vollständigen Fehlernachweis zu erhalten.

**Die einfache gleichmäßige Fouriermessung ist dafür ausgeschieden, wenn Anzahl der Messpunkte und Größe der expliziten Abzüge nur polynomial in der Bitlänge wachsen.** Ein konstruktiver Beweis liefert aus N,B,M einen unteren Alias mit mindestens c³ Beitrag, ohne N zu faktorisieren. Für hinreichend große N übersteigt dieser Beitrag das 4N-Fehlerbudget. Die genaue Aussage betrifft ausschließlich diese positive Trapezregel ohne weitere Aliasabzüge. Sie schließt weder andere Ausleseverfahren noch Faktorisierung allgemein aus.

## Ausgeführte Kontrollen

[PROBE.json](PROBE.json) enthält:

- 11.413 E8-Koeffizienten aus drei eindimensionalen Theta-Polynomen, verglichen mit einer separaten Teilerzählung;
- 57.065 bereinigte Koeffizienten bei fünf Schranken B, exakt gegengeprüft;
- 22 Wiederherstellungen für (N,B)-Kombinationen über **sechs verschiedene kleine Semiprime**, zusätzlich 44 Wiederherstellungen bei Störungen von ±4N;
- explizite faktorunabhängige Alias-Gegenzeugen für Zahlen mit 48, 64, 96, 128, 280, 512 und 1024 Bit. **Diese großen Zahlen wurden hier nicht faktorisiert** und wurden nicht als Semiprime erzeugt oder zertifiziert.

Das größte kleine Beispiel ist N=11.413=101·113. Bei B=64 ist der Zielkoeffizient 2.473.198. Selbst bei 512 gleichmäßig verteilten Messpunkten tragen die unteren Aliase mindestens 2.915.620 bei; das hier vorgesehene Genauigkeitsbudget beträgt nur 45.652. Das ist ein exakter algebraischer Kontaminationsnachweis, keine schlecht eingestellte Gleitkommasimulation. Fehlende untere Aliase in einigen kleineren Beispielen bedeuten noch keinen erfolgreichen Koeffizientenalgorithmus, da obere Aliase und Auswertefehler zusätzlich zu kontrollieren sind.

Die direkte Theta-Polynomrechnung verwendet Grad 91.304, also eine mit N wachsende Liste. Die gespeicherte isolierte Zeit von ungefähr 0,034 Sekunden für diesen kleinen Präfix ist keine vollständige Faktorisierungszeit, kein Rekord und keine Skalierungsaussage. Die unabhängige Teilerzählung gehört ausschließlich zum Prüfer, nicht zur faktorfreien Theta-Konstruktion.

## Verbleibender Kandidat und Abbruchgrenze

Die sinnvoll präzisierte Suche ist eine **adaptive, vollständig zertifizierte Aliasprojektion**: Aus günstig konstruierten störenden Koeffizientenlagen neue Messfunktionen wählen, schon bekannte Anteile global entfernen und alle verbleibenden Beiträge gemeinsam begrenzen. Das entspricht methodisch der neuen RH-Reparatur. In dieser Runde liegt dafür noch kein günstiger Algorithmus vor. Nur einzelne Aliase positiv zu reparieren oder beliebig viele spektrale Abtastungen anzunehmen würde die gesuchte Abkürzung nicht liefern.

Die lokalen TFPT-Spektrallücken verbessern die Kontrolle der festen physikalischen Zellen. Eine Implementierung dieses E8-Beobachters in genau diesen Hamiltonians, eine effiziente Zustandspräparation sowie eine N-abhängige Messkomplexitätsgarantie sind nicht vorhanden. Diese Brücke bleibt ausdrücklich offen.

## Nachweise und Wiederholung

Quellen und Snapshot-Hashes: [SOURCES.json](SOURCES.json). Vollständige algebraische Erläuterung: [THEORIE.md](THEORIE.md). Rohresultate: [PROBE.json](PROBE.json). Begrenzte Quellenkonsistenz: [SOURCE_CHECK.json](SOURCE_CHECK.json). Das [Manifest](MANIFEST.json) bindet diese Dateien.

Zum Wiederholen im Ordner:

```text
/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/tfpt-discovery/.venv/bin/python -B probe.py
```

Die Wiederholung schreibt PROBE.json neu und ändert wegen der Zeitmessung dessen Hash. Das abgeschlossene Manifest muss dann bewusst neu erstellt werden; alte Resultate nicht ungeprüft überschreiben.
