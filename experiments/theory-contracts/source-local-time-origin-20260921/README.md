# Lokale Randzeit, Originaltransfer und Windung

Contract `UR.SOURCE.LOCAL_TIME_ORIGIN.01`, 21. September 2026. **PARTIAL**.

Die neu eingereichte skalare Kreiszeitklassifikation ist korrekt. Eine direkte Identifikation mit beiden ursprünglichen v221/v814-Recoveryraten ist ausgeschlossen. Der andere ursprüngliche Kandidat mit ungerader Determinantenklasse bestimmt ein internes Bündel auf S² bis Isomorphie, aber noch keine physische P1-Quellenabbildung, räumliche Spinstruktur oder CAR-Statistik.

[Beweis und Quellenabgleich](PROOF.md) · [unabhängiger Review](independent_review.md) · [ausführlicher Transfertest](original_transfer_test.md) · [Rechenergebnisse](results.json)

## Reproduktion

Im Contract-Ordner:

```sh
python3 checker.py
python3 -OO checker.py
```

Nur Python-Standardbibliothek. `source_pins.json` enthält die lokalen Originalpfade und ihre SHA-256-Hashes; diese Quellen müssen vorhanden und unverändert sein. Die Ergebnisse beider Aufrufe stimmen byteweise überein. Der Prüfer bestätigt konkrete rationale Rechnungen, während die allgemeinen Aussagen im Beweis stehen. Hashprüfung ersetzt keinen Beweis.

Das im Anhang erwähnte externe Reproduktionspaket war hinter nicht auflösbaren Referenzplatzhaltern verborgen. Es wurde nicht als ausgeführter Test ausgegeben; dieses Paket enthält unabhängige Kontrollen.

## Reichweite und nächster Schritt

Die einzige ausgeschlossene Zeitidentifikation ist eine gemeinsame direkte Isometrie bzw. zwei exakt passende komprimierte Zeitschritte zwischen Recovery und der einzelnen freien Kreisquelle. Die Anlage selbst setzt diese Identifikation nicht. Die mathematische Auswahlregel bleibt gültig. Keine allgemeine Widerlegung von TFPT.

Die angegebenen Determinantenlinienklassen bestimmen auf S² bereits die Bündelklasse; ein fehlender ausgeschriebener Matrixrepräsentant ist keine eigenständige topologische Lücke. Zu beweisen bleiben die markierte Assoziation aus der Originalquelle, die Feldalgebra samt Zustand und die physische Zeit. Danach sind Ladungen, Produkte, Gram-Matrix und Zeitantwort des Randkandidaten gemeinsam zu prüfen.

Firewall: Forschungscontract unter `experiments/`, keine empirische Scorecard, keine Promotion zu Ledger/Paper/Website, keine geschlossenen physischen T1–T8-Gates, keine vollständige TFPT-Lösung.
