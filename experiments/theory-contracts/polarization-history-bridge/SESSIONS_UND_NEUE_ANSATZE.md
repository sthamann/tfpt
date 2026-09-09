# TFPT: Sessions-Abgleich und neue belastbare Möglichkeiten

2026-09-08. Statusaufnahme 19:14:44 MESZ, ergänzende Forschung danach.
Repo-HEAD b803b7e5. Sechs zugehörige Aufgaben untersucht, nicht alle
Cursor-Prozesse oder sonstigen Nutzeraufgaben. Fremde Aufgaben nur gelesen,
nicht neu gestartet, umgelenkt oder als eigene Ergebnisse ausgegeben.
[Originalstatus mit IDs](session_snapshot.json).

## 1. Was die anderen Sessions tatsächlich tragen

| Aufgabe / Artefakt | Beobachteter Stand | Belastbare Aussage und Grenze |
| --- | --- | --- |
| Finde fehlende RH-Bausteine in TFPT | aktiv | Beschränkte positive Modulspektren passen nicht zum benötigten xi-Resolventen. Der Folgeversuch untersucht Nulltemperatur und unbeschränkte physische Skalierung. Kein RH-Beweis. |
| Untersuche TFPT und neue Faktorisier | inaktiv nach abgeschlossener Runde | Rekursive Radikalreduktion verbessert einige Phasensuchvarianten bei kleinen Fällen. Kein Vorteil gegenüber direkter Faktorsuche. |
| Pi-Primzahl-Korrelationen prüfen | inaktiv nach abgeschlossener Runde | Arithmetischer Vorfilter trägt, spezieller pi-Effekt nicht. Der Vergleich berücksichtigt jetzt auch die Vorfilterkosten. |
| Prüfe TFPT auf Millennium-Probleme | nicht geladen; Abschlussbericht vorhanden | Deklarierter reiner SU(2)-Gittersektor hat ein belegtes Starkkopplungsprogramm; kein Kontinuums- oder Millennium-Abschluss. |
| Untersuche TFPT und K aus M | frühere Aufnahme: nicht geladen | Historischer A3-Rahmungsbericht vorhanden; dessen genannte lokale Ausgabedateien aktuell nicht gefunden. Keine frische Repo-Integration daraus behauptet. |

Zusätzlich ist das neue Repo-Artefakt
[Geometrie und Readout](../../double-cover-rh-audit-2026-09-08/GEOMETRIE_UND_READOUT.md)
aus der Aufgabe mit den zehn Foto-Anhängen ausgewertet; diese war inaktiv.
Der lange Originaltitel bleibt unverändert im Status-JSON.

### RH: die skalierte Spektralfrage ist tatsächlich eine neue Pflicht

Der [RH-Sessionsbericht](</Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Sessionsabgleich_und_Spektralbruecke_2026-09-08.md>)
vergleicht G(x)=d log xi(1/2+sqrt(x))/dx mit einem positiven Stieltjesmaß
auf [0,M]. Für x>=x0 gilt F(x)/F(x0)<=(x0+M)/(x+M).
Bei M=64, x0=4, x=10000 ist die obere Schranke 0.0067568, während
das im RH-Zweig intervallgeprüfte G-Verhältnis etwa 0.3051473 beträgt.
Mehr beschränkte positive Gewichte beheben das nicht. Ebenso liefert die
einfache ganzzahlige Fourier-Clock nicht den erforderlichen logarithmischen
Hochenergie-Faktor. Das ist kein Ausschluss einer aus der Quelle bewiesenen
unbeschränkten Skalierungsfolge. Diese Front wird bereits dort bearbeitet.
Alle Primstellen, Gewichte und globale Positivität bleiben eigene Pflichten.

### Faktorisierung und pi: kein Rechenvorteil durch Umbenennung

Die [Radikalrunde](</Users/stefanhamann/Documents/Codex/2026-09-05/unt/work/recursive_radical_search_20260908e/ERGEBNISSE.md>)
erhält affine Bedingungen und alle niedrigeren Phasenterme an jeder
Verzweigung. Bei 14 Zielbits gelingen 6/6 Aufrufe, aber das sind nur drei
verschiedene Zahlen mit je zwei Wiederholungen; bei 16/18 Zielbits 0/6.
Die sechs kleinen Erfolge brauchen insgesamt 3.709 s gegenüber 0.000120 s
direkter Enumeration. Kein allgemeiner neuer Faktorisierungsalgorithmus.

Der [aktuelle arithmetische Vergleich](../../pi-prime-event-log-2026-09-08/arithmetic-gate/README.md)
erreicht auf 64 Validierungszahlen 61/64 mit kleinem exaktem Kofaktorfilter,
gegenüber 56/64 sequentiell bei gleicher Zahl teurer Hauptprüfungen.
Die Gesamtzeiten sind jedoch 1.891 s versus 0.938 s. Pi, e, sqrt(2) und
Zufallssortierungen innerhalb der Kofaktorgruppen erreichen alle 61/64;
pi ist dabei nicht schneller. Die Primzahlen/Perioden werden dem Filter
übergeben, nicht durch die Dynamik erzeugt. Ältere 40/64-Angaben wurden
hier nicht als aktueller Stand weiterverwendet.

### SU(2): nützliche Vergleichstheorie mit scharfer Bereichsgrenze

Der [SU(2)-Beweisbericht](</Users/stefanhamann/Documents/Codex/2026-09-08/che-2/outputs/su2-round2/PROOF.md>)
bildet den deklarierten Gitteroperator auf die Voraussetzungen des
[Yarotsky-Satzes](https://arxiv.org/html/math-ph/0412040) ab.
Ein hinreichend kleines Verhältnis r=c_B/c_E liefert dort eine
volumenuniforme Lücke; die numerische Schwelle ist nicht bekannt.
Unter der verwendeten Kontinuumsnormierung r=4/g^4 läuft der schwach
gekoppelte Kontinuumsweg gerade aus diesem Bereich heraus. Weder dieser
Weg noch die Auswahl des SU(2)-Parents durch TFPT sind damit geschlossen.
Die Tests dieser fremden Session wurden hier nicht erneut ausgeführt.

## 2. Neue gemeinsame Erkenntnis: nicht die Räume verwechseln

Die neue rationale Reflexion aus dem Geometrie-Zweig erhält den Boundary,
kehrt aber die Clock um und mischt die beiden Carrier-Markierungen.
Eine alle drei Markierungen erhaltende lineare Signumkehr ist durch einen
nichtverschwindenden Dreiecks-Spurinvarianten ausgeschlossen. Die QWZ-
Ortsreflexion tauscht außerdem im Allgemeinen Holonomiesektoren alpha und
-alpha; eine gemeinsame direkte Summe ist eine erklärte Erweiterung.

Unser neuer [Involutionstyp-Beweis](../compiler-involution-types/README.md)
zeigt unabhängig: Die vier vorhandenen kohärenten K-Lifts auf den 16
E8-Ladungszeichen-Zuständen haben Typ 12+4. Eine Involution, die den
invertiblen Operator auf 16 Majorana-Koordinaten umkehrt, hat Typ 8+8.
Kein invertierbarer linearer Ganzraum-Intertwiner kann diese Typen angleichen.
Eine größere Operatoralgebra oder anders typisierte Abbildung wird dadurch
nicht ausgeschlossen. Der positive Boundary-Zeuge bleibt gültig.

### Positiver Anschluss: Primitive Clock-Sektoren in vorhandenen Bilinearen

Der fremde Readout-Beweis zeigt O P_B=P_B und [O,H]=0: Neutrale
Boundary-Dynamik bleibt Clock-blind. Wir haben anschließend die tatsächliche
Quelle exakt weiter zerlegt. Auf den Majorana-Koordinaten fehlen die
primitiven C6-Grade 1 und 5. In den **bereits algebraisch vorhandenen
Majorana-Bilinearen** gibt es dagegen vier Komponenten jedes dieser Grade.
Das äußere Quadrat wurde unabhängig über eine vollständige 120x120-Matrix
geprüft. Details und Auswahlregel: [Clock-Readout](../compiler-involution-types/CLOCK_READOUT.md).

Das ist eine konkrete Alternative zu zusätzlichem willkürlichem Bulk:
Nichtneutrale Carrier-Bilineare untersuchen, die die gesuchte Clock-
Information überhaupt tragen können. Ihre Algebra ist jetzt nachgewiesen,
ihre Zulässigkeit unter allen physikalischen Constraints, ihre Antwort im
ausgewählten Zustand und ihr Zusammenhang mit dem E8-Ladungslift noch nicht.

## 3. Neue analytische Vereinfachung: vollständige Polarisationsgeschichte

Unser [vollständiger Beweis](README.md) entfernt alle Rotationen innerhalb
besetzter und unbesetzter Zustände exakt durch einen mitbewegten Rahmen.
Die volle komplexe Vakuumamplitude bleibt erhalten. Eine künstliche
besetzte Rand/Bulk-Trennung, inverse Kompressionen und ein von null
verschiedener Determinant sind nicht erforderlich.

Neu ist die unmittelbar bewiesene dimensionsunabhängige Fehlerschranke
zwischen zwei gedrehten Kreuzblock-Geschichten auf derselben Polarisation.
Für die vorhandene Feldnormierung genügt Z_t^2 epsilon_N -> 0, zusätzlich
zum separat zu beweisenden Vergleich des Referenzmodells mit dem Current-
Grenzwert. Unter der angegebenen Referenzschranke folgt als konkretes Ziel

    integral ||Q(B_N-B_ref,N)P||_HS ds = o(N^(-1/16)/sqrt(log N)).

Diese Rate ist ein hinreichendes Beweisziel, kein bereits gemessener oder
bewiesener Quellenfehler. Die exakte Reduktion wurde auf sechs vollständigen
QWZ-Fällen erneut geprüft, Rest <=1.1e-13. Einfaches Weglassen der inneren
Blöcke scheitert hingegen schon endlich und verschlechtert hier die Fehler.

Eine exakte Purifikation überträgt denselben Ansatz auf thermische und
gemischte Kovarianzen. Das verbindet die Rechenmethoden der beiden Sessions,
nicht automatisch deren physikalische Zustände. Die Hilfskopie ist nur eine
mathematische Darstellung; Nullmodenpräparation und ein gemeinsamer
mikroskopischer Parent müssen weiterhin hergeleitet werden.

## 4. Priorisierte nächste Beweise statt weiterer lose verbundener Modelle

1. **Mikroskopischer Feldvergleich:** Referenzpolarisation quellengetreu
   einbetten, beide gedrehten Geschichten konstruieren und die obige Rate
   samt Nahdiagonal-Kontrolle zeigen. Erfolg: voller normierter komplexer
   Zweipunkt-Limes aus derselben Quelle, danach feste höhere Feldwörter.
2. **Clock sichtbar machen:** die exakt gefundenen Grad-1/5-Bilineare mit
   den Quellen-Constraints und dem ursprünglichen H prüfen. Erfolg:
   zulässiger, nichttrivialer, dynamischer Zweipunkt-Readout in einer
   begründeten Präparation; anschließend Zuordnung zum E8-Carry. Kein
   erneuter Versuch des ausgeschlossenen invertierbaren 16D-Gleichsetzens.
3. **Chiralität über Noether-Antwort testen:** Die Arbeit von Dang, Karur
   und Sen [Gauge field flow for chiral gauge theories on a slab](https://arxiv.org/abs/2606.05306)
   untersucht 2026 auf einem 2+1-dimensionalen Slab mit 1+1-dimensionalem
   Rand, wie aus einem Rand-Eichfeld bestimmter Bulk-Fluss die Kopplung zum
   Spiegelrand beeinflusst. Ihr Gittertest betrifft Stromerhaltung und
   Anomalieeinfluss, nicht den vollständigen 3+1D-TFPT-Parent. Als konkreter
   Vergleich: volle Strombilanz und Spiegelrandantwort im vorhandenen
   geladenen Quellmodell messen. Eine eingeführte Flussvorschrift zuerst
   ausdrücklich als Modellvariation kennzeichnen; ihre TFPT-Herleitung
   ist Teil des Erfolgsmaßstabs. Kein Spiegelrand-Abschneiden per Projektion.

Die aktive RH-Session verfolgt separat die unbeschränkte spektrale Skalierung.
Ein Erfolg dort muss anschließend mit denselben Zuständen und Observablen
kompatibel sein. Die alte endliche E8-Kaskade erzeugt durch ihre logarithmische
Schreibweise noch kein vollständiges arithmetisches Spektrum.

## 5. Integrations- und Evidenzgrenze

Lokal integriert: Beweise, exakte Prüfer, numerische Quellenkontrollen,
Sessionsnapshot und Arbeitsplan. [153 Tests je Modus](TEST_RESULTS.md)
bestanden, inklusive drei zuletzt ergänzter Clock-Tests. Unabhängige
mathematische Gegenprüfung der neuen Geschichtsschranke und Gegenprüfung
des Involutionsbeweises. Das ist keine unabhängige Herleitung der TFPT-Quelle.
Die systematische Fehlersuche isolierte einen bestehenden optimierten
Importfehler im neuen Adapter; fremde Quellen blieben unverändert.

Kein Commit/Push, keine Paper-/Website-Aktualisierung dieser Runde.
Keine T1-T8-Abschlussmarker geändert. Gemeinsamer lokaler Parent,
physikalische Präparation, geladene Felder/Chiralität, relativistischer
Kontinuumsgrenzwert und vollständige Gravitations-/Flavor-/Maß-Verknüpfung
sind durch diese Resultate nicht vollständig gelöst.
