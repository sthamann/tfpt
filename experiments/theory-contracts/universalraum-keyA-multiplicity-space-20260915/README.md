# Key-A: Multiplizitätsraum des nativen Blocks — 15. September 2026

Endliche, nichtarithmetische Forschungsrechnung (NON-RH). **Firewall:** dies
ist ein Theory-Contract-Experiment — **keine** Claims in `verification/`,
`status_ledger.csv`, Papers oder Website, keine Commits, keine Promotion.
Geprüft wird die Hypothese „Raum = die Multiplizitätenräume des einen nativen
Bausteins" durch exakte Wachstums- und Lokalitätsanalyse der Singulett- (und
Pol-)Multiplizitäten pro Bosonlevel.

## Fragestellung

Modell (N=64, Lochsprache: Level k = 2k Löcher + k Bosonen auf |F⟩):
wächst der Multiplizitätsgraph der Singulette wie ein d-dimensionales Gitter
(polynomiell ~ k^(d−1)) oder baumartig/exponentiell? — Die entscheidende
Rechnung dazu, ob „Raum" bereits im einen Baustein steckt.

## Dateien

- `multiplicity_growth.py` — Checker 1: exakte Weyl–Steinberg-Multiplizitäten
  auf DP-Gewichtsverteilungen (c_j = j-Teilmengen der 64 Moden, b_k =
  k-Multimengen der 60 Bosonen). Singuletts `mult_k` für k=0..8 (N=64) und
  Pol-Typ `(16,4̄)` `mult64_k` für k=0..7 (N=63). Validierung: mult_0,1,2 =
  1,1,4 (zertifizierte Schwesterwerte), Kammerunabhängigkeit, exakte
  gewichtsnull-Dimensionen (480, 442800, 257326240). Wachstumsfits am Ende
  numerisch (markiert).
- `locality_embryo.py` — Checker 2: exaktes Lokalitätsembryo. Helle
  3-Kette (β₁²=480, β₂²=916, Jacobi-Block), exakte 1↔2-Singulettkopplungen
  (Quadrate 36,16,504,360), exakte helle Träger/Kantenzahlen bis Level 3,
  unabhängige mult_3=13-Rechnung, rigorose Valenzschranke 2→3 (≤13 pro Kopie).
- `RESULTS.md` — vollständiger Bericht inkl. Grenzen (deutsch; Label
  exakt/numerisch/bedingt/offen).
- `replay_manifest.json` — Status beider Checker; normale und optimierte
  (`-OO`) Ausführung müssen bis auf Laufzeitfelder byteidentisch sein.

## Reproduktion

```sh
cd experiments/theory-contracts/universalraum-keyA-multiplicity-space-20260915
/opt/homebrew/bin/python3 replay.py
```

NumPy, SciPy, SymPy werden benötigt. Die Laufzeit wird von den hohen
Steinberg-Auswertungen dominiert (parallele exakte Integerreduktion,
16 Worker); Checker 1 deutlich länger als Checker 2. Kein Zugriff auf Dateien
außerhalb des Repositorys; die Gewichts-/W-Tensoren werden in-repo
rekonstruiert und per SHA-256 gegen die gepinnten `native_source.py`-Werte
abgesichert.
