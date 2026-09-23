# Randoperator und gemeinsame Familienauswahl

`UR.SOURCE.BOUNDARY_LIFT_SELECTION.01` · 22. September 2026 · **PARTIAL**

Die induzierte Verbindung auf dem gemeinsamen Spinor-/Familienträger ist explizit hergeleitet. Bei festem Hauptsymbol ist ihr glatter Wechsel eine beschränkte Störung nullter Ordnung und trägt den benötigten Selbstadjungiertheitsschritt. Eine irreduzible Familienwirkung erzwingt unter ausdrücklich zusätzlicher Parallelitätsannahme den Lift `m=(r,r,r,-2-3r)`. Der bisherige uneingeschränkte Wurzellift mit `2+2`-Aufteilung ist dann nicht kompatibel.

[Vollständige Herleitung](PROOF.md) · [Originalquellen-Audit](aps_origin_audit.md) · [exakte Ergebnisse](results.json)

Der archivierte v4.5-Quelltext enthält einen falschen allgemeinen Erstordnungs-Störungsschluss und eine inkonsistente Monodromieformel. Zwei explizite, nicht konjugierte D4-Pakete prüfen den behaupteten Auswahlmechanismus. Sie sind Gegenbeispiele zur Eindeutigkeit aus den ausgeschriebenen Symmetriebedingungen, keine neuen TFPT-Quellen. Die allgemeine Monodromiemehrdeutigkeit ist im aktuellen TFPT-Paper und Ledger schon bekannt. Die bestehenden algebraischen Flavorverhältnisse benötigen die Eindeutigkeit dieses kontinuierlichen Punktes nicht.

## Reproduktion

Python 3 und `sympy==1.14.0`:

```sh
python3 checker.py
python3 -OO checker.py
```

Die acht in `source_pins.json` bezeichneten Originaldateien müssen unverändert vorliegen. Beide Ausgaben sind bytegleich mit den gespeicherten Ergebnissen. Allgemeine Aussagen werden im Beweis begründet; endliche Kontrollen und Quellenhashes ersetzen diese Argumente nicht. Für die neuen mathematischen Ergänzungen ist kein unabhängiger Agentenreview abgeschlossen. Ein unabhängiger Quellenlese-Audit liegt vor.

## Offener Herkunftsschritt

Die Originalquelle muss bestimmen, wie ihre Determinantenrichtung auf das tatsächliche markierte Familienlokalsystem wirkt. Erst daraus folgt, ob Parallelität oder eine andere gemeinsame Kovarianz gilt. Weder diese Auswahl noch die ursprünglichen geladenen Felder, deren Zustand und gemeinsame physische Zeit sind hier geschlossen.

Firewall: Forschungscontract unter `experiments/`, keine Paper-/Ledger-/Scorecard-Promotion und keine vollständige TFPT- oder T1–T8-Lösung.
