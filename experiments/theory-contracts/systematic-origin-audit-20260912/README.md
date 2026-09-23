# Systematische gemeinsame Prüfung: Ursprung, Kopplung und Ladung

12. September 2026. Drei parallele Subagenten plus Hauptstrang; NON-RH.
**Kein vollständiger TOE-Nachweis. Alle acht physikalischen Tore bleiben offen.**

Dieser Bericht führt die Ergebnisse zusammen, statt unabhängig erfolgreiche
Teilmodelle zu einer scheinbar fertigen Theorie zu addieren. Originalquellen,
neue endliche Beweise, bedingte Konstruktionen und fehlende physikalische
Identifikationen werden getrennt. Historische Paper-/Ledger-Marker werden
nicht verändert. Die untersuchten Originalquellen sind in den jeweiligen
Prüfern beziehungsweise dem unabhängigen Prüfbericht mit Hashes dokumentiert.

## 1. Arbeitsaufteilung und abgeschlossene Ergebnisse

| Strang | Auftrag | Ergebnis und Beleg |
| --- | --- | --- |
| Ursprung | Ist der Familienzyklus bereits eine physikalische Aktualisierung? | Nein, die geprüfte Quelle definiert eine Symmetrie. Auf einem einzelnen Viererraum schließt das untersuchte Generatorenset zu 96 Matrizen/48 Kanälen; ein fest wiederholtes Wort hat Kanalperiode höchstens sechs. [Quellenprüfung](clock-origin/AUDIT.md). |
| Wechselwirkung | Welche Kopplung erzwingen die ursprünglichen Regeln? | Exakt getrennte lokale Aktualisierung erzwingt ein Produkt. Gemeinsame ursprüngliche Symmetrie erlaubt sieben nichtskalare Hamiltonparameter. Eine bedingte Verstärkung wählt den Bell-Kopplungstyp. [Vollständige endliche Klassifikation](interaction/RESULTS.md). |
| Unabhängige Gegenprüfung | Stimmen die Kernidentitäten und ihre Aussagegrenzen? | Unabhängige Matrixrekonstruktion bestätigt sie und verwirft zwei absichtlich defekte Varianten. Eindeutigkeit des irreduziblen Schritts bestimmt keine zusätzlichen physikalischen Freiheitsgrade. [Red-Team](redteam/REPORT.md). |
| Gemeinsame Ladungs-/Zeitprüfung | Kann derselbe endliche Schritt zugleich das fehlende Half-Charge-Feld sein? | Nein unter der exakten additiven Ward-Identität. Ein unbeschränkter Übertrag ist konsistent, aber eine zusätzlich angesetzte Produktdarstellung erzeugt keine Wechselwirkung und ist nicht die autonome Zeitentwicklung. [Brückenbeweis](CHARGE_CLOCK_BRIDGE.md). |

Die neue Arbeitsweise umfasst Quellenherkunft, vollständige endliche
Klassifikationen, Gegenbeispiele, unabhängige Rekonstruktion und die gemeinsame
Prüfung der Beweispflichten. Ein erfolgreicher endlicher Prüflauf ersetzt
keines dieser physikalischen Herkunftsprobleme.

## 2. Die stärkste positive Auswahl: bedingte Bell-Kopplung

Für ein vierdimensionales System und sein **zusätzlich physisch angenommenes**
komplex-konjugiertes Gegenstück reduziert volle aktive U(4)-Invarianz den
Hamiltonraum auf

    H = alpha I + beta |Phi><Phi|,
    |Phi> = (1/2) sum_(a=0)^3 |a,a>.

Ein eindeutiger Grundzustand erzwingt beta<0. Nach Wahl des Energie-Nullpunkts:

    H_glue = J (I-|Phi><Phi|),  J>0.

Damit ist der Kopplungstyp tatsächlich ausgewählt, nicht nur als mögliches
Beispiel konstruiert. Er kann Verschränkung erzeugen. Dies ist ein allgemeines
bedingtes Resultat auf dem gewählten Paar; kein Nachweis eines neuartigen
universellen Naturgesetzes oder seiner Eindeutigkeit aus TFPT.

Die vier zusätzlichen Fragen dürfen nicht verschwinden:

1. Warum realisiert die Quelle zwei unabhängige, konjugiert gepaarte Systeme?
2. Warum gilt die stärkere **aktive** volle U(4)-Symmetrie für diese Kopplung,
   statt bloßer Kovarianz unter einem Wechsel der Beschreibung?
3. Welche Kopplungen zwischen welchen physikalischen Teilen existieren?
4. Welche Skala, Entwicklung und physikalische Präparation wählt die Quelle?

Im vorherigen Registercode fixiert diese Kopplung nur das Bell-Paar zwischen
einem Registerteil und dem ergänzten System. Der logische Viererraum bleibt
frei. Ein eindeutiger Paarzustand ist daher kein eindeutiger Weltzustand.

### Sofortiger Zusammensetzungstest: Drei werden wieder ein Viererbaustein

Die Wechselwirkungs- und Gegenprüfungsstränge wurden nach dem Zweierresultat
fortgesetzt, statt dieses als Endpunkt zu behandeln. Drei überlappend
Bell-gekoppelte Viererfaktoren haben keinen Zustand, der beide Paarbedingungen
perfekt erfüllt. Ihr vollständiges Spektrum ist 3/4 (vierfach), 5/4 (vierfach)
und 2 (56-fach), in den gewählten Einheitskopplungen.

Positiv: Der vierdimensionale Grundraum trägt wieder dieselbe fundamentale
Darstellung. Seine Randabbildung multipliziert spurlose Operatoren mit 3/5.
Für zwei konjugierte Dreierblöcke erhält die komprimierte Verbindung exakt
wieder die Bell-Form:

    H_eff = (9/25)(I-P_Bell) + (3/5)I.

Diese Selbstähnlichkeit ist eine exakte statische Kompression; bei zusätzlich
angenommener schwacher Zwischenblockkopplung liefert sie die erste
Störungsordnung. Sie ist keine nachgewiesene geschlossene Dynamik. Die
Kopplung verlässt den unveränderten Produkt-Grundraum bei jedem von null
verschiedenen logischen Eingang: Die berechnete Übergangs-Grammatrix ist

    (24I+126P_Bell)/625 > 0.

Die unabhängige Gegenprüfung hat diese Aussage zusätzlich direkt im
4096-dimensionalen Sechsfaktorenraum bestätigt. Das schließt nicht jede
angepasste effektive Zweiblockbeschreibung aus; volle Symmetrie kann deren
Form bei isoliertem Band weiterhin stark einschränken. Eine geschlossene
lokale Viele-Block-Iteration samt Fehlerkontrolle ist nicht bewiesen.

Die Informationsabbildung ist außerdem nicht neu als allgemeiner
Quantenalgorithmus: Nach Ausblenden des mittleren Faktors entspricht sie
exakt Werners bekanntem symmetrischem 1-zu-2-Klonkanal (approximatives,
nicht perfektes Kopieren). Alle 16 Matrixeinheiten wurden verglichen.
Siehe [Werner, Abschnitt 3, Gleichung 3.3](https://arxiv.org/html/quant-ph/9804001).
Der Befund ordnet unseren Kandidaten in bekannte Quanteninformation ein,
statt ihn vorschnell als TFPT-exklusives Naturgesetz zu bezeichnen.

[Herleitung und Zusammensetzung](interaction/COMPOSITION.md),
[unabhängige Sechsfaktorenprüfung](redteam/COMPOSITION_REVIEW.md).

## 3. Warum nicht einfach alle bisherigen Modelle zusammensetzen?

| Bereits bearbeiteter Träger | Tatsächliche Leistung | Noch nicht bewiesene Gleichsetzung |
| --- | --- | --- |
| Endlicher Compiler und seine Darstellungen | Vorzeichen, Multiplikation, Familienwirkung, endliche Codierung und Rekonstruktion. | Physische Freiheitsgrade, Zustandspräparation, Raum- und Zeitzuordnung. |
| Tatsächlicher QWZ-Streifen und seine gefüllten Meere | Sektorweise ganzzahlige CAR-Felder; tatsächliche Ladungs-/Energievergleiche. In einem deklarierten Grenzsektorenraum weitere bedingte Half-Charge-Konstruktionen. | Lokales renormiertes mikroskopisches Intersektorfeld mit acht ausgewählten, korrekt markierten E8-Kanälen. |
| Gewählter kompakter Rotor-/CAR-Parent | Bereits vorhandene echte Rückwirkung aus elektrischem Generator und ladungstragendem Transport; separate Dynamik- und Zustandsergebnisse. | Auswahl dieses Parents aus TFPT und markierungs-, ladungs-, adjungierten- und energieerhaltende Verbindung zum Compiler und zur Seam. |

Die alten QWZ-/Rotor-Beweise wurden hierfür gezielt gelesen, nicht als neue
vollständige Replays ausgegeben. Grundlage sind der
[Forschungsstand vom 9. September](../RESEARCH_2026-09-09.md),
[gemeinsame ältere Vergleich](../common-engine-threeway/README.md),
[sektorielle Quellenbrücke](../source-half-sector-bridge/README.md) und
[bedingte Raumzeit-Feldkonstruktion](../two-edge-spacetime-field/README.md).

Ein Tensorprodukt könnte diese Modelle formal nebeneinanderstellen. Es würde
damit weder die benötigten Identifikationen noch ihre Wechselwirkung herleiten.
Gerade die Nichtvertauschbarkeit von E und Ladungstransport im Rotor-Modell
ist zusätzliche dynamische Struktur, nicht die endliche Clock-Symmetrie.

## 4. Alle acht Tore am selben Nachweis messen

Die folgenden Tore sind die tatsächlichen obersten T1–T8 aus
`TFPT.TOE.COMPLETE.01`, nicht gleichnamige Untertests aus älteren Suiten.

| Tor | Für den Abschluss erforderlich | Beitrag und Grenze dieser Runde |
| --- | --- | --- |
| T1 | Strukturpostulat selektiert P1/P2, Compiler und physische Dimensionsannahmen. | Generische Codekonstruktion und zusätzliche Auswahlannahmen wurden offengelegt; keine physische Auswahl bewiesen. |
| T2 | Tatsächliche markierte E8-Seam inklusive Half-Charge-Feld, Energie, beider Adjungierter und Skalierungsgrenze. | Endlicher Clock-Reset als persistentes Ladungsfeld ausgeschlossen; korrekter unbeschränkter Übertrag erhalten. Fehlender mikroskopischer Feldnachweis nicht ersetzt. |
| T3 | Ein ausgewählter lokaler/quasilokaler unitärer 3+1D-Parent für alle Sektoren. | Exakte Bedingung für echte gemeinsame Operatorwirkung und bedingte einfache Kopplung bestimmt; weder Raum noch Parent ausgewählt. |
| T4 | Chirales Standardmodell, Maß, Anomalien/Index und gleichmäßige Spiegelentkopplung. | Keine neue Realisierung. Eingesetzte Yukawa-/Massendaten eines endlichen Dirac-Modells sind keine Herleitung. |
| T5 | Wechselwirkendes Kontinuum, Lorentz-Verhalten, Confinement, Clustering und erforderliche Streuung. | Endliche Positivität und periodische Kanäle liefern diesen Grenzübergang nicht. |
| T6 | Drei Eichkopplungen sowie vollständige Neutrinotextur und -skala intern bestimmt. | Keine Kopplungs-/Neutrinoherleitung; freie Skalen bleiben explizit. |
| T7 | Masseloser Quantenspin zwei mit universeller Kopplung aus demselben Parent. | Keine kollektive mikroskopische Realisierung; endliche Bell-Kopplung ist kein Gravitationsfeld. |
| T8 | Physischer Anfangszustand und eine gemeinsame erzeugende Funktion für alle Readouts. | Paarzustandsauswahl von logischer/globaler Zustandsauswahl getrennt; keine gemeinsame physische Auswahl. |

## 5. Gemeinsamer Abnahmepunkt für weitere Lösungsvorschläge

Der nächste beanspruchte gemeinsame Ursprung muss **ein einziges markiertes
System** liefern: Zustandsraum, Observable-Algebra, Dynamik, physische
Präparation und zugängliche Messoperationen; für Kontinuumsbehauptungen eine
kompatible Familie solcher Systeme mit Verfeinerungsabbildungen.

Seine Compiler- und Seam-Abbildungen müssen auf demselben Definitionsbereich
Produkte, Adjungierte, Ladungen, Zeitentwicklung und Zustandsantworten erhalten.
Ein erster endlicher Erfolg muss einen quellenbegründeten gemeinsamen
Transport-/Readout-Versuch ausdrücken, bei dem ein tatsächlich zugänglicher
Operator gemeinsame Wirkung entwickelt. Die zweite-Teil-Abhängigkeit darf
nicht vom Auswerter hineingeschrieben sein.

Nicht ausreichend sind gleiche Eigenwerte, gleiche Gruppengrößen, ein
gewünschter Grundzustand nach freier Parameterwahl, ein hinzugefügtes
Hilfsregister oder das Umbenennen einer Symmetrie in Zeit. Die neue Prüfung
enthält ausdrückliche Gegenbeispiele gegen genau diese Abkürzungen.

Das ist kein allgemeines Unmöglichkeitstheorem für TFPT. Es trennt die
bereits bewiesenen einfachen Beziehungen von noch hinzuzufügender Physik.

## Reproduktion und Integration

`run_verification.py` führt die vorherige Codierung und Auswahlprüfung sowie
die drei Worker-Prüfer, die Ladungs-/Clock-Brücke und beide Zusammensetzungs-
Prüfer getrennt aus, jeweils normal und unter `-OO`: acht Prüfer, sechzehn
isolierte Ausführungen. Der gemeinsame maschinenlesbare Bericht liegt in
`verification.json`. Die Ergebnisgleichheit wird pro Strang verglichen;
Prüfungszahlen werden nicht zu physikalischen Abschlussquoten addiert.

Die Artefakte sind lokal integriert. Kein Commit, Push, Website-/Paper-Build,
Cloud-Export oder physikalischer Statuswechsel gehört zu dieser Runde.
