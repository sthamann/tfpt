# Kontrollierter Zwei-Banken-Transfer · v1.6.5

Eigener Forschungsordner. Der neue Satz gilt für einen ausdrücklich
zusätzlichen Rotor-Link zwischen zwei nativen Banken, nicht für einen
aus dem ursprünglichen Compiler hergeleiteten Link.

## Reproduktion

Mit Python, NumPy und SymPy vom entpackten Ordner aus:

```sh
python3 -B replay.py --frozen-only
```

Die Quellen sind schon eingefroren; `--freeze` ist ausschließlich die
einmalige Erstellung aus den ursprünglichen lokalen Quellen und verweigert
das Überschreiben eines bestehenden Quellenmanifests. Standardmäßig prüft
der Replay zusätzlich alle noch vorhandenen Originalorte strikt. Da ein
anderer Bearbeiter den alten Bericht inzwischen geändert hat, benutzt die
versionierte Reproduktion ausdrücklich `--frozen-only`. Unterschiede werden
trotzdem im Manifest sichtbar; kein Quellpin wird erneuert.

Die Python-Prüfer sind vollständig lokal. Sie rufen weder Netzwerke noch
bezahlte Dienste auf. Optimierter Pythonlauf bedeutet `-OO`; geprüfte
Bedingungen sind explizite Fehlerprüfungen und verschwinden dabei nicht.

## Dateien

- `RESULTS.md`: neuer technischer Bericht mit vollständiger analytischer
  Beweiskette und Quellenintegration.
- `LATE_AUDIT.md`: vollständige Prüfung und Integration der zwei zuletzt
  eingegangenen Anlagen, einschließlich bestätigtem Z4-Lift und Korrekturen.
- `UPDATE.md`: nur Änderungen gegenüber v1.6.4.
- `EINFACH.md`: bildlicher Gesamtstatus und nächste drei Ziele.
- `verify_two_bank_transfer.py`: alle hohen Ladungssektoren, zentrale
  Komplementlücken, Gaussgesetz, normierte Transfer- und Fehlergrenzen.
- `verify_symmetry_scope.py`: bedingte Einordnung des geänderten
  Symmetrieentwurfs, kein neuer vollständiger Darstellungsbeweis.
- `audit_addenda.py`: 62 unabhängige Nachprüfungen der letzten beiden Anlagen;
  exakte Tensor-/Phasen-/Darstellungstests und getrennte numerische Zeitsuche.
- `replay_manifest.json`: Laufstatus, identische Ergebnisse beider Varianten,
  externe Originalgleichheit und gesonderter Live-Quellenstatus.
- `source_drift_failure_receipt.json`: aufbewahrter Fehlerbeleg der echten
  Quellenänderung; er wird nicht als erfolgreiche Prüfung umgedeutet.
- `sources/`, `external/`: eingefrorene Eingaben, native v1.6.4-Abhängigkeit
  und unverändert ausgeführte externe Programme.
- `late_sources/`, `late_sources_manifest.json`: zuletzt gelieferte Programme
  und separate unveränderliche Pins; kein Überschreiben des ersten Snapshots.

Der Satz wird analytisch bewiesen und mit exakten Zahlen zertifiziert,
nicht durch Testzählen und nicht in einem formalen Beweisassistenten.
Keine Änderungen an fremden Forschungsordnern oder an Akzeptanzmarkern.
