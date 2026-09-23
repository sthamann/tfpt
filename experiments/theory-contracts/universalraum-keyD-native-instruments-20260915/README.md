# Schlüssel D: native Instrumente des N=2-Kausalzeugen — 15. September 2026

Theorievertrag (Experiment-Firewall): **keine** Aussagen in Papers, Ledger
oder Website; keine neuen nativen Hamiltonterme; keine Änderung fremder
Ordner; kein T1–T8-Abschluss. Schließt den algebraischen Kern der offenen
Priorität „das kleine Kausalexperiment an den Compiler anschließen":
Alphabet-Mitgliedschaft von Z_r = (−1)^{n_r}, die 3-Punkt-No-Go-Frage auf
dem exakten Sternblock, die Lückentabelle der Zeugenschritte und das
minimale schließende Primitiv.

## Dateien

- `native_source.py` — byte-gepinnte Kopie der gemeinsamen nativen Quelle
  aus `universalraum-operations-groundstate-20260915` (SHA-256
  `380577f8…`; W, J, C3, Cartan-Gewichte, Gruppe, Lie-Erzeuger, CAR-Helfer;
  kein externer Tensor-Zugriff).
- `check_alphabet_membership.py` — Aufgabe 1: Z_r als passiver Focklift
  Γ(u_r), {N}′-Kompatibilität, kron-Obstruktion + Schreier-Kern der
  deklarierten Gruppe (mit/ohne Clock), Kommutantzeuge [n₄, WᵀW] ≠ 0,
  S3-Identität Z_r = 1 − 2n_r.
- `check_threepoint_star.py` — Aufgabe 2: v1.6.8-Reproduktion mit nur
  nativen Schritten (9×9-Stern exakt, 3×3-Reduktion gegengeprüft),
  CAR-Nulllemma Z_r f_r = f_r (576 exakte Sektoridentitäten bis N=3),
  2-Punkt-Analogon δ_rs/8, Mittelpunktszeuge auf dem hellen Zustand
  (−3x/128 off-diagonal, +21x/128 diagonal), numerische Gegenprobe auf dem
  vollen N=2-Block (2076).
- `check_gap_closure.py` — Aufgabe 3/4: Ladungsgraduierung (Worte in
  {Alphabet + S3 + Q} erreichen nur N + 4ℤ), Weyl-Identitäten
  (−[N_b,[Q,X]] = R₊+R₋ u. a.), geladener Schluss
  (f₄†f₅₇†|0⟩ = +|Paar(4,57)⟩, n_r = f_r†f_r, Modentransport),
  S3-Trägergraph N=2 zusammenhängend, Q-natives N=4-Singulettblock-Analogon.
- `replay.py` — führt alle drei Prüfer normal und unter `-OO` aus und
  verlangt byteidentische JSON-Ausgaben (bis auf Laufzeitfelder);
  `replay_manifest.json` enthält Status und Hashes.

## Reproduktion

```sh
cd experiments/theory-contracts/universalraum-keyD-native-instruments-20260915
/opt/homebrew/bin/python3 replay.py
```

Benötigt werden NumPy, SciPy und SymPy. Laufzeit unter einer Minute.
Gelesen werden nur Repository-Dateien (die gepinnte Clock-Quelle
`compiler-involution-types/checker.py`, SHA-256 `9bf99de7…`); geschrieben
wird ausschließlich in diesen Ordner. Der abschließende Lauf muss PASS mit
2487 Wachen (2478 exakt, 9 numerisch) melden.
