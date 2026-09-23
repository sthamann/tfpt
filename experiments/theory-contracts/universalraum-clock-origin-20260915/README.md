# TFPT Universalraum: Clock und gemeinsame Quelle, v1.6.6

Diese isolierte Forschungsrevision verifiziert drei neue Nutzertexte und
integriert vier parallele Teiluntersuchungen plus die eigene exakte
Clock-in-Spin(10)-Konstruktion. Keine vollständige TOE-/RH-Abschlussbehauptung.

Lesereihenfolge: `EINFACH.md`, `UPDATE.md`, `RESULTS.md`. Ausführliche
Beweise und Gegenchecks liegen in `agents/`; `RH_LOOP_AUDIT.md` prüft den
arithmetischen Teil der nachgereichten Hypothese mit offengelegter
Katalog-Versionsgrenze. Die alten vollständigen Herleitungen stehen in
`sources/historical_v1.6.5.md`, ihr unverändertes Prüfarchiv daneben.

## Reproduktion

Benötigt: Python 3 mit NumPy, SciPy, SymPy und mpmath sowie ein C++17-Compiler.
Im ausgepackten Verzeichnis:

```sh
python3 -B replay.py
```

Dies übersetzt den kleinen unabhängigen Kontraktionskern und führt acht
Programme normal sowie mit `-OO` aus. Es werden ausschließlich eingefrorene
Eingaben verwendet, keine Live-Quellen nachgezogen. Das Gesamtprotokoll
steht in `replay_manifest.json`; die Einzelberichte unter `replay_outputs/`.

**2205 Prüfbedingungen pro Variante:** 1127 gelieferte Guards und 1078
eigene Checks. Fünf eigene Checks betreffen numerische Ritzwerte; unter den
gelieferten Guards sind neun wörtliche `need(True, ...)`-Folgerungen. Diese
Zählung ist keine Zahl unabhängiger Beweise oder gelöster Physikprobleme.
Mehrfach intern ausgeführte Quellprüfungen werden nicht doppelt addiert.

`freeze.py` und `freeze_addendum.py` dokumentieren die ursprüngliche
Quellübernahme am Arbeitsrechner; sie sind für einen Paket-Replay **nicht**
auszuführen. Die Teilagenten-Replays können ebenfalls ursprüngliche
Dateipfade enthalten; für die portable Gesamtreproduktion ausschließlich
den hier angegebenen Root-Replay verwenden.

`deliver.py` baut ein vollständiges Markdown-Dokument samt früheren
Herleitungen, ein kurzes Update, eine einfache Erklärung und ein Prüfarchiv.
Es kontrolliert alle Archivbytes und reproduziert nach dem Auspacken erneut
alle acht aktuellen Programme. Alte v1.6.4-/v1.6.5-Großprüfungen sind erhalten,
werden dadurch aber nicht als erneut ausgeführt ausgegeben. Neue Artefakte
werden direkt unter `Documents` versioniert abgelegt; frühere Dateien bleiben
unverändert. Kein Commit, Push, Webdeploy oder PDF-Neubau in dieser Revision.
