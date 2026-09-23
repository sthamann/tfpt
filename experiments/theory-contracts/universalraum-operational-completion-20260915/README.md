# Operationale Completion und stabile Prozessfixpunkte

Neue Prüfung des Nutzerentwurfs vom 15. September 2026.

- [Ausführliche Analyse mit Beweisen und Grenzen](RESULTS.md)
- [Einfach und bildlich](EINFACH.md)
- [Normale exakte Kontrollen](normal.json)
- [Optimierte exakte Kontrollen](optimized.json)

Die normale und optimierte Ausführung ergeben dieselben 65 bestandenen
endlichen Kontrollen. Allgemeine Sätze stehen getrennt im Bericht.

Reproduktion im Verzeichnis:

```sh
python3 -B checker.py --output normal.json
python3 -OO -B checker.py --output optimized.json
cmp normal.json optimized.json
```

Benötigt SymPy. Der Checker schreibt ausschließlich die ausdrücklich benannte
Ergebnisdatei und liest die im Quellmanifest benannten Eingaben. Keine
E₈-/TOE-/RH-Beförderung, keine Änderung bestehender Papers oder des Kompasses.
