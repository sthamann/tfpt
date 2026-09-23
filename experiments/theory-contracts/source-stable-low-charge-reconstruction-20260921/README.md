# Stabile Quellenrekonstruktion aus niedrigen Ladungssektoren

Forschungs-ID: `UR.SOURCE.LOWQ.01` · Gesamtverdict: **PARTIAL**.

Die physischen T1–T8-Gates bleiben offen.

Der mathematische Satz rekonstruiert den stabilen Generator aus `Q<=4` nur
unter vollständiger irreduzibler Fockdarstellung, globalen unteren
Operatorantworten und einer uniformen globalen Energieschranke. Die Quelle
liefert bislang weder `C1`, `C2`, `h`, `Omega`, `g`, physische Zeit und Zustand
noch das räumliche Kontinuum.

- `HERLEITUNG.md`: zusammengeführtes Ergebnis und Herkunftsgrenze.
- `algebra/`: bedingter Stabilitäts-/Niedrigsektorsatz und exakter kleiner Test.
- `native/`: exakte W-Vektoridentitäten, Krylov-Zertifikat und Momentenkorrektur.
- `source/`: Audit des fehlenden gemeinsamen Quellenjets.
- `transfer/`: Semigroup-/Reflexionspositivitätsgrenze.
- `certificate.json`: Ausgabe des portablen gezielten Replays.
- `validation_receipt.json`: Lauf- und Hashnachweis.
- `source_pins.json`: Hashes der gelesenen Originalbelege.

Reproduktion mit Python, NumPy und SymPy:

```text
python3 -B replay.py
python3 -B -OO replay.py
```

Beide Aufrufe erzeugen bytegleiche JSON-Ausgabe. Es wurde keine Vollsuite und
keine Ledger-, Paper- oder Website-Promotion ausgeführt.
