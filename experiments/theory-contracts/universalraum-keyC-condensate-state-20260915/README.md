# KeyC: Kondensat- vs. Zustandsfrage (Theory Contract)

**Firewall:** reines Theorie-Experiment in `experiments/`. Keine Claims in
`papers/`, `status_ledger.csv`, `website/`. Keine Commits. Quelle: kopierte
Konstruktionen aus den beiden Universalraum-Runden (W-Aufbau, Loch-Krylov,
Weyl–Steinberg-Logik); Quellordner werden nie modifiziert oder importiert.

## Fragestellung

Bildet die Zustandsregel „der Zustand erzeugt den Raum" ein auf eine
Multiplizitäts-Kopie lokalisiertes Kondensat, oder bleibt der native
N=64-Grundzustand über die vier Level-2-Singulettkopien delokalisiert?
Dazu: Level-2-Lokalisierungsprofil, Copy-Symmetrie-Wirkung (Ordnung 768),
selbstkonsistente Regel min E(N)/N, Kondensatkriterium.

## Checker

- `keyc_localize.py` — Aufgabe 1+4: exakte R-Projektionen von v2/w2,
  K=3-Ritz-Überlapps, Kondensatkriterium (schwer: baut v3 mit 15,25 Mio.
  Einträgen, ~5 min, ~5 GB).
- `keyc_copysym.py` — Aufgabe 2: Gruppenzählung 768, Boson-Orbits (5),
  W-Kovarianz, Copy-Wirkung (schnell).
- `keyc_staterule.py` — Aufgabe 3: exakte Sektorfloors, E/N-Tabelle,
  μ*-Intervall (schnell).

Budget: nie Level-3-Basen bauen (Gewicht-0-Raum 257 Mio.); v3 wird
gestreamt (kanalweise Merges), nicht verdichtet.

## Run

```sh
cd experiments/theory-contracts/universalraum-keyC-condensate-state-20260915
/opt/homebrew/bin/python3 replay.py
```

`replay.py` führt jeden Checker normal und unter `-OO` aus und verlangt
byteidentische JSON-Ausgaben; Ergebnis in `replay_manifest.json` (muss PASS).
Einzelchecker: `/opt/homebrew/bin/python3 keyc_staterule.py` (schnell),
`keyc_copysym.py` (schnell), `keyc_localize.py` (schwer).

## Labels

- **exakt**: Ganzzahl/rational, Guard-geprüft.
- **numerisch**: float64-Eigenwerte/Toleranz-Guards (Ritz, Überlapp-Kombination).
- **bedingt**: μ*-Intervall (exakte Floor-Kante + numerische Ritz-Kante).
- **offen**: min-E/N-Selektion (Floors notwendig-nicht-hinreichend).
