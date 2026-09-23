# Relationaler Lochraum und externe Anschlussprüfung — v1.6.2

Datum: 15. September 2026. Endliche nichtarithmetische Forschungsfortsetzung.

- RESULTS.md: vollständiger neuer Forschungsnachtrag einschließlich der
  drei externen Eingaben, eigener Fortsetzung, Gegenprüfungen und T1–T8.
- EINFACH_ERKLAERT.md: dieselben Ergebnisse in verständlicher Sprache.
- replay_manifest.json: aktueller Status aller vier eigenen Prüfer;
  normale und optimierte Ausführung müssen jeweils byteidentisch sein.
- sources/: unveränderte Kopien der drei Eingaben und des zweiten
  externen Forschungsberichts samt dessen ursprünglichem Prüfpaket.
- external_replay/: Ergebnisse des separat wiederholten fremden Pakets.
- delivery_manifest.json: Hashes und direkte Documents-Ziele der neuen Texte.

Lokale Reproduktion mit dem vorhandenen Python:

    /opt/homebrew/bin/python3 replay.py

NumPy, SciPy und SymPy werden benötigt. Die eigenen Prüfer greifen
schreibgeschützt auf gepinnte frühere TFPT-Prüfer sowie den nativen Tensor
unter dem angegebenen lokalen Pfad zu. Dieser Ordner allein ist deshalb
kein vollständig portables Quellpaket. Die externen Prüfungen des zweiten
Texts besitzen dagegen ihr eigenes mitgeliefertes Tensorarchiv.

Der Replay-Einstieg setzt seinen Status vor Beginn auf RUNNING und
verzeichnet Prüfungsfehler als FAIL; ein alter PASS darf nach einem
fehlgeschlagenen neuen Lauf nicht weiter als aktueller Status stehen.
Nur ein vollständig erfolgreicher Durchlauf setzt PASS.

Die vorhandenen Haupt- und Update-PDFs v1.6 wurden nicht verändert.
Keine bestehenden Quellen wurden überschrieben. Kein Commit oder Push.
Kein vollständiges T1–T8-Tor und keine globale mathematische Vermutung
wird durch diese endliche Rechnung als gelöst markiert.
