# Clock als Verklebungsanweisung — exakter Test (keyB, 2026-09-15)

Datum: 15. September 2026. Endliche nichtarithmetische Forschungsfortsetzung
(NON-RH). Kein T1–T8-Tor wird geschlossen; keine Promotion nach `verification/`,
Ledger, Papers oder Website. Kein Commit oder Push in dieser Runde.

Die Runde testet die Hypothese „die native Clock ist die Verklebungsanweisung,
die den einen Baustein zu einem Turm komponiert" exakt: zerlegt der Ordnungs-6-
Clock \(\Lambda^2(C_{3,F})\) den 2016-dim Fermion-Paarraum in eine
\(\mathbb{Z}_6\)-gradierte Slot-Struktur über seine sechs rotierten hellen
Unterräume, oder nicht?

## Dateien

| Datei | Inhalt |
|---|---|
| `common.py` | Gepinnte Konventionen: Tensor W (repo-lokal, SHA `3f00a089…`), Gewichte, Clock-Lift (Permutation (2,0,1,4,3), Vorzeichen −1), Kovarianz \(W\Lambda^2(G_F)=G_B W\). Selbsttest per `python3 common.py`. |
| `clock_gluing.py` | Hauptprüfer: sechs rotierte helle Räume \(V_k\), 6×6-Überlappungstabelle, Union-Rang, dunkler Kern, Clock-Zykelstruktur auf 60 Bosons und 480 Trägern, Slot-Übergangsmatrix, Verdict. Exakte modulare Rangberechnung (GF\((p)\) + CRT über fünf Primzahlen). |
| `replay.py` | Führt beide Prüfer normal und unter `-OO` aus, verlangt byteidentische Ausgaben, schreibt `replay_manifest.json`. |
| `RESULTS.md` | Forschungsnachtrag (Deutsch) mit allen exakten Zahlen und dem Verdict. |

## Reproduktion

    /opt/homebrew/bin/python3 replay.py

NumPy ≥ 2.0 (für `np.bitwise_count`), SciPy und SymPy werden benötigt. Der
Hauptprüfer läuft ≈ 3–4 Minuten (die modulare Rangberechnung der 2016×360-Matrix
dominiert). Der Replay-Einstieg setzt den Status zu Beginn auf RUNNING; ein
alter PASS überlebt keinen fehlgeschlagenen Lauf.

Die Prüfer lesen ausschließlich die repo-lokale Kopie des nativen Tensors
(`../universalraum-v16-integrated-20260915/sources/native_tensor.npz`) und den
gepinnten Clock-Konstruktor (`../compiler-involution-types/checker.py`).
`common.py` ist eine eigenständige Kopie der benötigten Konventionen; die
Quellordner werden nicht mutiert.

## Firewall

Dies ist ein **theorievertraglicher Forschungsversuch** in `experiments/`.
Keine Behauptungen aus dieser Runde werden in Papers, Ledger (`status_ledger.csv`)
oder Website übernommen. Keine `vN_*.py` wird angelegt oder geändert. Kein Commit
oder Push. Guardzahlen zählen Prüfbedingungen, keine unabhängigen Theoreme.
