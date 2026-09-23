# UR.SOURCE.REGISTER_RESPONSE.01

**Verdict: PARTIAL.** Exakte bedingte geladene Antwort der korrelierten
v1033-C4-Quelle, mit vollständigem endlichem Grundzustand und ursprünglichem
Disorder-Operator. Keine Promotion.

- [Verständliches Ergebnis](ERGEBNIS.md)
- [Annahmen, Allzeitformel und Beweis](PROOF.md)
- [Vorab festgelegte Frage](SPEC.md)
- [Reproduzierbare Resultate](certificate.json)
- [Quellenpins](source_manifest.json)
- [Interner Review und Validierung](VALIDIERUNG.md)

Ausführen:

```sh
python3 -B checker.py --output /tmp/tfpt-register-response.json
python3 -OO -B checker.py --output /tmp/tfpt-register-response-optimized.json
cmp /tmp/tfpt-register-response.json /tmp/tfpt-register-response-optimized.json
```

Standardrepository: `/Users/stefanhamann/Projekte/tfpt-theoryv4`;
abweichend mit `--repo /pfad/zum/repository`. Benötigt SymPy und NumPy.
Der ausführbare Checker prüft zunächst die Herkunftspins und vergleicht die
Originaldefinitionen mit ihren exakten Matrizen.

Die numerisch kontrollierten Zeitpunkte beweisen keine Allzeitaussage.
Deren Beweis ist die allgemeine äußere-Algebra-Identität in PROOF.md.
Die Grundzustands- und Polynomresultate sind exakte endliche Rechnungen.
Die physischen Ursprungsannahmen bleiben ausdrücklich offen.

