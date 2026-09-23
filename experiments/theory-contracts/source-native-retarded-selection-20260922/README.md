# Native Zeitwirkung und Familienanschluss

22. September 2026 · `UR.SOURCE.NATIVE_RETARDED_SELECTION.01`

**Verdict: PARTIAL.** [Beweis und Quellen](PROOF.md).

Die bereits vorhandene W-Paarwechselwirkung lässt sich exakt über die
bestehenden Bosonen eliminieren. Ihr euklidischer Zeitkern ist
`(Delta-i omega)^(-1)`; die entsprechende Stromwirkung ist bilokal.
Die Casimiridentität dafür stammt aus dem vorhandenen Stand vom
15. September und wird nicht als neue Entdeckung ausgegeben.

Ein exakter Anschluss-Test schließt konstante lineare Familienfilter
im invarianten nativen Zustand als alleinige Ursache unterschiedlicher
Familienenergien aus. Der direkte Abgleich benutzt die vorhandenen
TFPT-Leptonverhältnisse und die tatsächliche irreduzible A4-Holonomie.
Ein paralleler Yukawa-Homomorphismus zwischen den unitären irreduziblen
Familienlokalsystemen hat gleiche Singularwerte. Die fehlende Quellwirkung
muss also mehr leisten als Basiswahl, Feldamplituden oder eine parallele
3+1-Determinantenrichtung. Flache Verbindung und nichtparalleler
Yukawa-Operator bleiben miteinander vereinbar.

Die Prüfung ist eine notwendige Strukturentscheidung, kein neuer
Massenfit und keine Herleitung des nativen Hamiltonoperators aus P1/P2.
Die physische Quellenauswahl, der tatsächliche Yukawa-Operator aus ihr
und der vierdimensionale Anschluss bleiben offen.

## Wiederholung

```sh
python3 -B checker.py --out certificate.json
python3 -OO -B checker.py --out certificate_optimized.json
```

Die Zertifikate sollen byteidentisch sein. Der Prüfer kontrolliert
Quellenpins, alle 60 nativen Generator-Intertwiner, die vollständige
Zweikörper-Casimiridentität, symbolische Kernidentitäten, Gram-Normierung
und das bestehende A4-Familienpaket samt Lepton-Ziel. Das allgemeine
Funktionsintegral-/Schur-Argument steht separat im Beweis.

Interner mathematischer Review: [REVIEW.md](REVIEW.md).
Quellstand: [source_pins.json](source_pins.json).

Firewall `experiments/`; Verdict-Enum `PASS/PARTIAL/FAIL`; keine
Paper-/Ledger-/Scorecard-Promotion, keine vollständige TFPT-Lösung,
kein geschlossenes physisches T1–T8-Gate.
