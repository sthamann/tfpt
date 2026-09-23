# Lokaler Quellen-Grenzwert und Prüfung der ursprünglichen Trägerauswahl

**Forschungs-ID:** `UR.SOURCE.LOCAL_LIMIT.01` · **Verdict: PARTIAL** · 20.09.2026

Der Konflikt zwischen Viertelholonomie und geladenen Clocks auf einem Kreis
fester Größe ist kein allgemeines Hindernis für eine lokale Feldtheorie.
Bei wachsendem Radius verschwindet der zusätzliche lokale Frequenzversatz,
während eine nichtverschwindende geladene Antwort bestehen bleibt. Dies wird
hier auf der unveränderten bisherigen Ein-Kopien-Quelle und, getrennt davon,
im bereits vorausgesetzten E8-Zielraum nachgewiesen.

Die neue Voraussetzung ist der Grenzwert selbst: `R -> unendlich`, zugleich
`a = 2*pi*R/N -> 0`, bei festen örtlichen Abständen und Zeiten. Seine physische
Auswahl aus P1/P2 wird nicht behauptet. Der endliche Kreis behält seine früher
bewiesene Holonomie, Vakuumstruktur und Clock-Nichtkommutation.

## Ergebnisse und ihre Reichweite

1. **Unveränderte Quelle:** Der exakte Zeilenresidual am ursprünglichen
   Fourieroperator kontrolliert sowohl die gefüllte Quellkovarianz als auch
   ihre Zeitentwicklung. Daraus folgen die Grenzwerte geschmierter geladener
   CAR-Operatoren und aller festen endlichen quasifreien Wörter. Kein neues
   Hamiltonglied, keine zusätzlichen Kopien und keine erneute Projektion
   während der Zeitentwicklung werden eingeführt.
2. **Kanalzahl:** Am selben Operator gibt es beim kleinen Impuls genau einen
   chiralen Kanal pro Rand. Acht Querplätze sind keine acht Teilchensorten.
   Der hier bewiesene Grenzwert erzeugt daher noch keine native E8-Quelle.
3. **Bedingter E8-Zielraum:** Die lokalen geladenen Spektralmaße tendieren zu
   `omega d omega`, die Zweipunktfunktion zu `1/tau^2`. Die tatsächlichen
   C/J-Clockdefekte verschwinden auf festen physischen Energiefenstern.
   Getrennte endliche Vertexwörter besitzen ihren ebenen Grenzwert.
4. **Kontrollen:** Bei festem Radius bleibt der Holonomieunterschied trotz
   Gitterverfeinerung bestehen. Bei Beobachtungszeiten proportional zum Radius
   bleibt er auch im E8-Ziel sichtbar. Der Satz ist ausdrücklich lokal.
5. **Ursprüngliche Trägerauswahl:** Der Quellen-Audit lokalisiert die nicht
   ausgeschriebene Auswahl des endlichen Trägers. Ein zusätzlicher exakter
   Paritätstest entscheidet die wörtliche gleichräumige Lesart: Wer zuerst
   nur den positiven Sektor einer Involution behält, kann durch Einschränken
   derselben Involution keinen negativen Trägersektor zurückgewinnen. Ein
   anderer tatsächlich gemeinter Übergang benötigt seine konkrete Abbildung.

## Beweise und Reproduktion

- [Beweis am ursprünglichen Quellenoperator](SOURCE_LINE_PROOF.txt)
- [Unabhängige Kontrolle dieses Beweises](SOURCE_LINE_REVIEW.txt)
- [Geladene E8-Wörter, Vakuumwörter und Clockschranken](LOCAL_LIMIT_REVIEW.txt)
- [Erste Kompression und Trägerparität](POLARIZATION_GATE.txt)
- [Audit der Originalranddaten und Lean-Schnittstellen](SOURCE_AUDIT.txt)
- [Gemeinsames Zertifikat](certificate.json)
- [Quelldateien mit Prüfsummen](source_manifest.json)

```sh
python3 -B experiments/theory-contracts/source-local-line-20260920/checker.py
python3 -B -OO experiments/theory-contracts/source-local-line-20260920/checker.py
```

Die exakten Matrixprüfungen kontrollieren die endlichen Voraussetzungen.
Die numerischen Grenzwertfolgen sind Diagnosen; die unendlichen Aussagen
folgen aus den ausgeschriebenen Residual-, Spektral- und Riemannsummenbeweisen.
Die Überprüfung ist keine externe Begutachtung oder Beweisassistenten-Formalisierung.

## Bedeutung für die Gesamtlösung

Wir müssen die Holonomie nicht durch einen passenden neuen Energieterm
entfernen, um lokale geladene Dynamik zu ermöglichen. Dieser mögliche
Umweg ist beseitigt. Der entscheidende offene Schritt liegt davor: die
lokale Quelle mit ihrer richtigen inneren Multiplizität und ihren geladenen
Feldern aus den ursprünglichen Randdaten gewinnen.

Dabei sind ein endlicher interner Faktor, ein unendlicher lokaler
Einteilchenraum und die E8-Vertexerweiterung drei unterschiedliche Objekte.
Ebenso liefert eine Determinantenform auf einem unbekannten Rang `n` eine
`n`-Form; sie wird nicht ohne Rangherleitung zu einer trilinearen Yukawa-Form.
Die genauen Abbildungen müssen diese Typen erhalten.

`QGEO.KERNEL.01` und die vollständige physische Realisierung bleiben offen.
Weder 3+1-dimensionale Raumzeit, chirale Materie, Kopplungen noch Gravitation
werden durch den lokalen Grenzwert allein hergeleitet. Keine T1–T8- oder
Ledger-Promotion; keine Änderung an den veröffentlichten Theorieaussagen.

Der während dieser Untersuchung hinzugekommene Contract
[UR.RAW_CARRIER_ORIGIN.01](../raw-carrier-origin-gate-20260920/PROOF.txt)
bestätigt den Paritätstest unabhängig und behandelt zusätzlich die
Transformationseigenschaften der reinen CAR-Polarisation. Dieser gemeinsame
Befund wird hier als Anschluss dokumentiert, nicht als mehrfacher neuer
Fortschritt gezählt. Seine weitergehenden Prüfungen sind nicht Teil unseres
Checkers. Eine Zustandsprojektion, eine geometrische Spiegelung und eine
interne Trägeroperation müssen mit ihren jeweiligen Abbildungen getrennt
bleiben. Der lokale Grenzwert dieses Contracts setzt keine Gleichsetzung
dieser drei Operatoren voraus.
