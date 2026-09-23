# Reproduktion und Reichweite

Forschungsbezeichner: `TFPT.SOURCE.THREE_ROUTES.20260920` · Gesamturteil: `PARTIAL`.

`checker.py` führt die vier eng begrenzten Rechnungen aus. Benötigt werden Python 3, NumPy und SymPy sowie die 22 Originaldateien unter den absoluten Pfaden in `source_manifest.json`. Die Originale werden vor und nach dem Lauf gehasht. Das Paket ist deshalb am vorhandenen Arbeitsplatz reproduzierbar, aber kein eigenständiges Quellenarchiv.

```sh
python3 -B checker.py
python3 -B -OO checker.py
```

Das Skript meldet getrennt den bestandenen Rechenlauf und das weiterhin nur teilweise geschlossene Forschungsziel. Die 27 Phasen-Prüfbedingungen enthalten die Kontrolle der übernommenen Determinantengrade; die 44 E8-Prüfbedingungen enthalten auch Quellenpins. Sie sind keine Zahl unabhängiger physikalischer Bestätigungen. Beim lokalen Quelloperator sind sechs Gruppen exakter Identitäten und der separate Überlapptest ausgeführt. Phi- und Omega-Kanäle sind zusätzlich analytisch hergeleitete und separat gegengeprüfte Konsequenzen.

Die Textbeweise begründen die allgemeinen Aussagen. Endliche symbolische Kontrollen und Literatur liefern nur die ausdrücklich genannten Teile. Es findet keine Promotion in Paper, Statusledger oder T1–T8 statt.

`source_manifest.json` pinnt Eingaben; `MANIFEST.json` pinnt diese Auslieferung. Die Gegenprüfung und ihre eingearbeiteten Präzisierungen stehen in `GEGENPRUEFUNG.md`.
