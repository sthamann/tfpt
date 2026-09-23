# Operationssatz, Feldwörterbuch und Grundzustandssonde — 15. September 2026

Endliche, nichtarithmetische Forschungsfortsetzung (NON-RH). Kein neuer
Hamiltonterm, keine Zustandsauswahl, keine Promotion nach `verification/`,
kein Ledger-/Paper-/Website-Eingriff, kein vollständiges T1–T8-Tor.
Schwesterordner mit der Grundzustands-Antwort-Konsolidierung:
`universalraum-native-ground-response-20260915` (v1.6.4).

## Dateien

- `native_source.py` — gemeinsame Quelle: W, J, C3, Cartan-Gewichte,
  Clock-Gruppe, 60 Lie-Erzeuger, CAR-Helfer, alles exakt und komplett
  in-repo rekonstruiert (kein externer Tensor-Zugriff nötig).
- `operations_commutant.py` — WP-A: erzeugte Algebra und Kommutant für
  die geschachtelten Operationssätze S0..S4 in den Sektoren N=2 und N=3.
- `field_dictionary.py` — WP-C: exaktes Lorentz-Feldwörterbuch des
  nativen Vertex (Skalarkanal exakt null; Vertex rein (1,0)+h.c.).
- `groundstate_probe.py` — WP-B-Sonde: Z4-Regel, exakte Singulett-
  Multiplizitäten (1, 1, 4), exakte Lanczos-Koeffizienten 480, 916,
  299520/229, Krylov-Schranke, Sektorfloors, Gruppenzensus.
- `RESULTS.md` — vollständiger Bericht einschließlich Grenzen.
- `replay_manifest.json` — aktueller Status aller vier Prüfer; normale
  und optimierte (`-OO`) Ausführung müssen bis auf Laufzeitfelder
  byteidentisch sein.

## Reproduktion

```sh
cd experiments/theory-contracts/universalraum-operations-groundstate-20260915
/opt/homebrew/bin/python3 replay.py
```

NumPy, SciPy, SymPy werden benötigt. Laufzeit ca. fünf Minuten
(die Grundzustandssonde dominiert). Kein Zugriff auf Dateien außerhalb
des Repositorys erforderlich.
