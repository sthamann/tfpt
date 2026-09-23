# Markierter Nahttransfer und Produktgrenze

**UR.SOURCE.MARKED_CP_LIFT.01 — PARTIAL — 2026-09-21.**

Unter einer offen ausgewiesenen Zusatzannahme existiert ein exakter diskreter vollständig positiver Anschluss zwischen dem q*-markierten Compileroperatorraum und dem ursprünglichen Drei-Zustands-Nahttransfer. Die Annahme lautet: Ein primitiver Schritt ist ein unitaler, spurtreuer, vollständig positiver und unter den markierten Pauli-Konjugationen sowie der bezeichneten S5-Wirkung kovarianter orbit-skalarer Prozess auf der vorhandenen Algebra `M4(C)`; die Nahtfaktoren `1/3` und `2/3` werden seinen beiden markierten Operatorsektoren zugeordnet. Diese gemeinsame physische Wirkung ist nicht aus P1/P2 hergeleitet.

Vollständige Positivität verwirft die Zuordnung `(2/3,1/3)` und wählt in dieser Klasse eindeutig

\[
\Phi=\Pi_0+\frac13\Pi_5+\frac23\Pi_{10}
=\frac7{12}\operatorname{id}+\frac1{12}\sum_{j=1}^5\operatorname{Ad}_{g_j}.
\]

Die ursprünglichen fixierten Wörter `A_BIT` und `FSIG` liefern eine positive Trine-Auslesung, auf der `Phi` die vollständige ursprüngliche Matrix

\[
B=\frac1{18}\begin{pmatrix}13&1&4\\1&13&4\\4&4&10\end{pmatrix}
\]

eintragsweise realisiert; sechs Schritte ergeben das ursprüngliche `v221`-Transferobjekt. Das ist mehr als eine Spektralübereinstimmung, aber noch keine Auswahl eines physischen Messinstruments.

Die Produktgrenze ist vollständig: Für den random-unitären Kanal ist der Schwarz-Defekt eine Summe positiver Quadrate. Sein Verschwinden zwingt einen Operator in den gemeinsamen Kommutanten der fünf tatsächlichen `g_j`. Das exakte lineare Kommutantensystem hat Rang 15, daher ist der multiplikative Bereich genau `C I4`. Kein nichttrivialer Basiswechsel macht diesen endlichen Kanal zu einer produkt- und ladungserhaltenden geschlossenen Feldzeit.

Der stetige Ausschluss gilt ausschließlich für die gleiche markierte orbit-skalare CPTP-Halbgruppenklasse. Größere Dilatationen, andere Zwischenzeit-Kovarianz oder andere TFPT-Vervollständigungen werden nicht ausgeschlossen.

`ERGEBNIS.md` enthält Herleitung und Grenzen. `SOURCE_PROVENANCE.md` dokumentiert den begrenzten Quellen- und Neuheitsaudit. Reproduktion mit Python 3 und SymPy:

```sh
python3 -B checker.py --out certificate.json
python3 -B -OO checker.py --out certificate_optimized.json
cmp certificate.json certificate_optimized.json
```

Vier Mutanten müssen scheitern:

```sh
python3 -B checker.py --mutant reverse_is_cp
python3 -B checker.py --mutant continuous_is_cp
python3 -B checker.py --mutant readout_is_projection
python3 -B checker.py --mutant charge_preserved
```

Der Checker führt 65 exakte Bedingungen aus; normaler und optimierter Lauf sind bytegleich. Keine Claims oder physischen Gates werden geschlossen. Keine Paper-, Ledger-, Scorecard- oder T1–T8-Promotion.
