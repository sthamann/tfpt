# Ausgeführte Prüfungen

9. September 2026. Repo-Basis:
`66b91e40e245569f06ab440ead80f446c9be0ee5`.

## Ergebnis

| Testsuite | Normal (`-B`) | Optimiert (`-B -OO`) |
| --- | ---: | ---: |
| `half-loop-source-transport/test_checker.py` | 23 bestanden | 23 bestanden |
| `common-engine-threeway/test_engine.py` | 25 bestanden | 25 bestanden |
| `half-charge-energy-bridge/test_checker.py` | 12 bestanden | 12 bestanden |
| Gesamt je Ausführungsmodus | **60 bestanden** | **60 bestanden** |

Das sind 60 unterschiedliche Tests, zweimal ausgeführt; keine vollständige
Repo-Testsuite und kein externer mathematischer Begutachtungsprozess.
Die Prüfungen unter `-OO` bestätigen insbesondere, dass die benutzten
Quellprüfungen nicht von abschaltbaren Python-Assertions abhängen.

Beide vollständigen Läufe von `run.py` waren erfolgreich.
`validation.json` und `validation_optimized.json` sind bytegleich.
Die darin aufgezeichneten SHA-256-Werte wurden nach dem letzten Lauf mit
den aktuellen vier lokalen Python-Dateien verglichen und stimmen überein.

## Was geprüft wurde

- Gepinnte Vorgängerquellen einschließlich ihrer Quellvalidierung;
  absichtliche Abweichungen von Pins werden abgewiesen.
- Alle 70 physikalischen Materiebelegungen mit symbolischem ganzzahligem
  Fluss: inverser Operator, Quadrat, Gauss-Erhaltung und Energieabschätzung.
- Eine getrennte Auswertung der Fermion-Erzeugungs- und
  Vernichtungsoperatoren auf allen 70 × 70 Belegungspaaren.
- Große positive und negative Flusswerte als zusätzliche Gegenkontrollen.
- Der nichtverschwindende Ladungskommutator unter der originalen Dynamik
  sowie ein expliziter ursprünglicher Transportpfad mit Windungszahl −1.
- Der skalare Vergleichsoperator mit unabhängigen Fourier-Integralen und
  seiner analytischen Energiedivergenz.
- Die vollständige sechsdimensionale symmetrieverträgliche quadratische
  Energieklasse, fünf unabhängige Bedingungen und fünf positive Mutanten,
  die jeweils eine weggelassene Bedingung verletzen.
- Die exakte Gegenladungs-Paaridentität bei beliebigem gemeinsamem
  Referenzpunkt und linearem Hintergrund; 240 Wurzelpaare in jeder der
  beiden gepinnten Hintergrundvarianten.
- Die Folge entwickeln → Halb-Schritt → weiterentwickeln unter dem
  unveränderten Quell-Hamiltonoperator.

## Numerische Folge und analytische Grenze

Die Folge wurde bei elektrischem Cutoff 10 auf 1.412 Zuständen ausgeführt,
mit jeweils Zeit 2 vor und nach Anwendung von S. Die Energie beträgt davor
ungefähr `8.02083333333334`, danach `8.023051772616705` und bleibt bei der
anschließenden Zeitentwicklung erhalten. S ist kein Energieerhaltungssatz
und darf beim Anwenden Energie übertragen.

Der aufgezeichnete Projektionsverlust nach S ist ungefähr
`7.04e-89`. Dies ist eine endliche numerische Diagnose, keine zertifizierte
Fehlergrenze eines unendlichen räumlichen Systems. Die Kontrolle auf allen
ganzzahligen Flussstufen folgt getrennt aus der analytischen Abschätzung
in [PROOF.md](PROOF.md), nicht aus dieser kleinen Zahl.

## Laufzeitumgebung und Reproduktion

Verwendet wurde die vorhandene TFPT-Umgebung:
Python 3.14.3, NumPy 2.4.6, SciPy 1.17.1 und SymPy 1.14.0.
Aus dem Repo-Root:

```sh
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/half-loop-source-transport -p test_checker.py -v
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/common-engine-threeway -p test_engine.py -v
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/half-charge-energy-bridge -p test_checker.py -v
```

Die gleichen drei Aufrufe wurden zusätzlich mit `-B -OO` ausgeführt.
Vollständige Replay-Aufrufe stehen in [README.md](README.md).

## Nicht behauptet

Keine der Prüfungen identifiziert S als das gesuchte mikroskopische
E₈-Halb-Ladungsfeld. Der erhaltene Ladungsoperator und die physikalische
Auswahl des Kandidaten fehlen weiterhin. T1–T8 bleiben offen.

Diese Runde ergänzt ausschließlich den neuen Forschungsordner. Keine
Änderung an alten Quellen, Paper, Webseite, globalen Statusmarkern oder
fremden Arbeiten; kein Commit und kein Push.
