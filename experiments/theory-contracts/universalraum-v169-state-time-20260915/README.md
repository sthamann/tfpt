# TFPT / Universalraum v1.6.9 — Zustand und Zeit ohne Zirkularität

Endlicher, nichtarithmetischer Forschungsvertrag (NON-RH), 15. September
2026. Untersucht wird, ob ein unabhängig begründeter Zustand über modularen
Fluss die native Dynamik auswählt.

## Ergebnis

Die geprüfte Kandidatenklasse ist sauber negativ entschieden. Sektortrace,
gleich gewichteter Quellenzustand, Quellen-/Randstrahlen, positive
Besetzungsgewichte und aus dem W-Quelloperator gebildete Exponentialzustände
liefern keinen modularen Fluss, der auf den geprüften nativen Blöcken mehrere
vorgegebene dimensionslose Antworten trifft. Im erweiterten
Zweigeneratoransatz `rho ∝ exp(-a Nb-b X)` trifft nur `b/a=1/20`; dann ist
`rho ∝ exp(-beta H)` und die Auswahl zirkulär.

Der Nachtrag prüft zusätzlich die mathematisch echte Unteralgebra-Route:
globale Reinheit kann nach Einschränkung einen treuen Zustand ergeben.
Zwei-Chart-Verschränkung, W-Paar-Kondensat und gefüllter Zustand liefern
auf den getesteten nativen Unteralgebren dennoch keinen zugleich treuen,
H-invarianten und mehrfach passenden modularen Fluss.

## Dateien

- `check_candidate_states.py` — Positivität, Normierung, Treue und
  H-Stationarität auf dem N=2-Stern (9), N=4-Singulettblock (2) und hellen
  Träger (120).
- `check_modular_dimensionless.py` — Modularoperatoren/-flüsse, exakte
  Negativkontrollen und die drei dimensionslosen Vergleiche.
- `check_mu_separation.py` — feste Sektoren gegenüber globaler
  `H+mu N`-Zustandswahl.
- `check_subalgebra_route.py` — Unteralgebra-Theorem, Zwei-Chart-Zustand,
  W-Paar-Kondensat und gefüllter Zustand.
- `RESULTS.md` — deutscher Bericht mit den Labels exakt, numerisch, bedingt,
  offen.
- `replay.py`, `replay_manifest.json` — normal/`-OO`-Replay und Hashes.

## Reproduktion

```sh
cd experiments/theory-contracts/universalraum-v169-state-time-20260915
/opt/homebrew/bin/python3 replay.py
```

Erwartet: `PASS`, 141 exakte Guards, sechs numerische Kontrollen,
byteidentische Checker-JSONs normal und mit `-OO`.

## Firewall

Nur Theory Contract in `experiments/`: keine Promotion nach
`verification/`, kein Ledger-, Paper-, Website- oder Scorecard-Eintrag.
Der ausgeschlossene Umfang ist die ausdrücklich geprüfte endliche
Kandidatenklasse, kein No-go für alle denkbaren Zustandsprinzipien. Der
H-Gibbs-Zustand dient ausschließlich als zirkuläre Positivkontrolle.
