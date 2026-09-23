# Native Grundzustandsantwort · v1.6.4

Abgetrennter Forschungsordner. Keine neuen nativen Hamiltonterme, keine
Änderung fremder Quellen, kein vollständiger T1–T8-Abschluss.

- `RESULTS.md`: konsolidierter technischer Bericht einschließlich eigener Beweise.
- `EINFACH_ERKLAERT.md`: bildliche Kurzfassung und die wichtigsten nächsten Ziele.
- `ground_replay_manifest.json`: frische vollständige Normenumeration bis k=4 und vier native Zertifikate.
- `external_pole_replay_manifest.json`: neu gelieferte v1.6.3, normal/optimiert und identisch zum Originalbericht.
- `response_replay_manifest.json`: neue eigene Antwort-, Feldtyp-, Operations- und Konsolidierungsprüfungen.
- `operation_symmetry.py`: dritter Operationsvertrag. Zerlegt den N=3-Sektor unter der
  Quellsymmetrie Spin(10)×SU(4), belegt Multiplizitätsfreiheit und damit den Kommutanten
  der Dimension exakt 7 als absoluten Boden der geschachtelten Reihe
  1444233216 > 240742144 > 7.

## Reproduktion

Vom Repository mit dem Python aus der verifizierten Umgebung:

```sh
python3 experiments/theory-contracts/universalraum-native-ground-response-20260915/replay_ground.py
python3 experiments/theory-contracts/universalraum-native-ground-response-20260915/replay_external_pole.py
python3 experiments/theory-contracts/universalraum-native-ground-response-20260915/replay_response.py
```

Benötigt werden Python, NumPy, SciPy, SymPy sowie Apple clang/libdispatch
für die unverändert übernommene vollständige Konfigurationsenumeration.
Die beiden Quellenreplays verwenden die in ihren Manifesten genannten
originalen Dateipfade und verweigern abweichende Hashes. Das Prüfpaket ist
ein vollständiger Arbeitssnapshot, aber kein pfadunabhängig installierbares
Softwareprodukt. Diese Arbeitskopie und die gepinnten Repository-Abhängigkeiten
müssen für die identische Reproduktion vorhanden sein.

Statusdateien starten vor jedem Lauf mit RUNNING und werden bei Fehlern
auf FAIL gesetzt. PASS setzt erfolgreiche Unterprozesse und byteidentische
normale/optimierte JSON-Berichte voraus. Vorherige Ergebnisse sind kein
Ersatz für den abschließenden Status des jeweils laufenden Manifests.

Die gelieferten v1.6.3-Dateien sind unter `sources/` eingefroren. Ihre
Forschungsanweisungen wurden als Quelleninhalt behandelt. Die vorangehende
v1.6.2 bleibt unverändert; ihr fehlendes Pluszeichen ist im neuen Bericht
als Erratum dokumentiert.
