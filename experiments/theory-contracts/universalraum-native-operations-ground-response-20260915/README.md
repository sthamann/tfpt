# Operationssatz, nativer Grundzustand und Feldwörterbuch — v1.6.3

Datum: 15. September 2026. Endliche nichtarithmetische Forschungsfortsetzung
(NON-RH). Kein T1–T8-Tor wird geschlossen; keine Promotion nach `verification/`,
Ledger, Papers oder Website. Kein Commit oder Push in dieser Runde.

Die Runde bearbeitet die vier Prioritäten aus v1.6.2 §14 in der dort festgelegten
Reihenfolge: (1) den tatsächlich verfügbaren Operationssatz exakt abgrenzen und
seinen Kommutanten bestimmen, (2) den berichteten nativen N=64-Grundzustand mit
dem ursprünglichen Hamilton- und Sektorvertrag reproduzieren und darauf die
geladene Antwort berechnen, (3) das Lorentz-Feldwörterbuch am tatsächlichen
Tensor festhalten, (4) räumliche Skalierung erst danach — sie ist hier
ausdrücklich **nicht** Gegenstand.

## Dateien

| Datei | Inhalt |
|---|---|
| `common.py` | Gepinnte Konventionen: Tensor W (repo-lokal, SHA `3f00a089…`), Gewichte, so(10)/su(4)-Generatoren, induzierte Bosongeneratoren, Casimir-Identität, Clock-Lift. Selbsttest per `python3 common.py`. |
| `operations_commutant.py` | Kommutant der von jeder Operationsstufe erzeugten Algebra auf N=2 und N=3: {X, N_b} → +Clock → +su(4) → +so(10) → alle Generatoren → B(H_N). Exakte Irreduzibel-Zerlegung über Höchstgewichtsvektoren. |
| `native_ground_state.py` | Lochbild des N=64-Sektors, exakte Krylov-Kette v₀…v₃ (bis 15 252 960 Einträge), Schließungstest mit w₂, Ritz-Obergrenzen, Observablen, geladene Ein-Teilchen-Antwort, Sektorauswahlschranken. |
| `norms_by_traces.py` | Unabhängige Krylov-Normen ν₁…ν₅ über Onishi-Determinante, bosonische Kohärenzzustands-Integration und Wick-Paarung (Spurnetzwerke auf dem Φ-Tensor), exakte `Fraction`-Vorfaktoren, zertifizierte float64-Kontraktion. |
| `field_dictionary.py` | Lorentz-Feldtyp-Census am tatsächlichen Tensor: Zweikomponenten-Weyl, Vierkomponenten-Dirac/Majorana, Chiralitätsgradierungen, Stabilisatoren und Kommutanten. |
| `replay.py` | Führt alle fünf Prüfer normal und unter `-OO` aus, verlangt byteidentische Ausgaben, schreibt `replay_manifest.json`. |
| `RESULTS.md`, `EINFACH_ERKLAERT.md` | Forschungsnachtrag und einfache Erklärung. |

Reihenfolge im Replay: `norms_by_traces.json` muss vor `native_ground_state.py`
vorliegen, weil dessen Ritz-Kette damit verlängert und die Übereinstimmung
ν₁…ν₃ geguardet wird.

## Reproduktion

    /opt/homebrew/bin/python3 replay.py

NumPy ≥ 2.0 (für `np.bitwise_count`), SciPy und SymPy werden benötigt. Der
Grundzustandsprüfer baut zweimal einen Zustand mit ~1,5·10⁷ Einträgen
(je ≈ 5 Minuten, ≈ 5 GB); alle anderen Prüfer laufen in Sekunden bis wenigen
Minuten. Der Replay-Einstieg setzt den Status zu Beginn auf RUNNING; ein alter
PASS überlebt keinen fehlgeschlagenen Lauf.

Die Prüfer lesen ausschließlich die repo-lokale Kopie des nativen Tensors
(`../universalraum-v16-integrated-20260915/sources/native_tensor.npz`) und den
gepinnten Clock-Konstruktor (`../compiler-involution-types/checker.py`). Der
Ordner ist damit ohne den externen `Documents`-Pfad lauffähig.

## Nicht behauptet

Keine physische Herleitung des Zustandsfunktionals, kein 3+1D-Träger, kein
dynamischer Spin 2, keine Reproduktion des Worker-Beweises „eindeutiger
N=64-Grundzustand bis g/Δ = 1/20“ (siehe RESULTS.md, Abschnitt Sektorauswahl).
Guardzahlen zählen Prüfbedingungen, keine unabhängigen Theoreme.
