# Seam-Reflexionsoperator — 15. September 2026

Endliche, nichtarithmetische Forschungsrechnung (NON-RH). **Firewall:** dies
ist ein Theory-Contract-Experiment — **keine** Claims in `verification/`,
`status_ledger.csv`, Papers oder Website, keine Commits, keine Promotion.

## Fragestellung

Liefert die ursprüngliche markierte TFPT-Seam genau das gemeinsame Paar von
Spiegelungswirkungen, das Fermionorte, Paarübergänge und Zustand konsistent
verbindet? — Abschnitt 15.3 des Spinlift-Hauptdokuments (v1.6.10) präzisiert
den Angriffspunkt: die geometrische σ muss auf den Fermionorten als das
passende J wirken und zugleich die W-Paarbänke mit der verschobenen
Kantenwirkung von L abbilden, inklusive Zustandsverträglichkeit. Dieser
Contract macht daraus fünf endliche, exakte Prüfteile (S1–S5) und benennt
den verbleibenden nichtendlichen Rest ehrlich (QGEO.MARKS.01 /
QGEO.KERNEL.01, spinoriales Vorzeichen aus roher Seam-Geometrie).

## Dateien

- `seam_reflection_operator.py` — der Checker. S1: Seam-Skelett (D4 auf
  (P¹, μ4), induzierte Kantenwirkung, H¹-Aktion, Ordnungswache gegen die
  innere Uhr der Periode 6). S2: erschöpfende Enumeration der reellen
  Zwei-Nachbar-Rahmenklasse (1024 Kandidaten; Filter: Involution, signierte
  Diederrelation, Paarkovarianz bei Balance, kein dunkler Mode). S3: native
  Operatorzuordnung auf dem 256-Fermion-Vierbankmodell mit gepinntem
  In-Repo-W (Term-Level-CAR-Kovarianz, B/T/D−kT-Kommutation). S4: Toy-
  Voll-Fock-Zustandsverträglichkeit (8 Moden, exakt). S5: Wachstumsprobe
  (Dunkelmoden-Rangregel n = 3..16, N2-Kettenband vs. relativistische
  Dispersion bis O(k⁶)).
- `RESULTS.md` — vollständiger Bericht inkl. Grenzen (deutsch; Label
  exakt/numerisch/bedingt/offen).
- `EINFACH_ERKLAERT.md` — die Bildversion.
- `replay_manifest.json` — Status; normale und optimierte (`-OO`) Ausführung
  sind bis auf Laufzeitfelder byteidentisch.

## Reproduktion

```sh
cd experiments/theory-contracts/universalraum-seam-reflection-operator-20260915
/opt/homebrew/bin/python3 replay.py
```

NumPy, SciPy, SymPy werden benötigt. Laufzeit wenige Sekunden. Kein Zugriff
auf Dateien außerhalb des Repositorys: der W-Tensor wird aus
`universalraum-singlet-observable-20260915/sources/native_source.py`
rekonstruiert und per SHA-256 gepinnt
(`7a4a0b1c4401a20a84aee47b75f9b9d8882299bdff938ba11fd5b2bfe5656112`).
