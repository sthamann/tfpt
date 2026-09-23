# F6 gemeinsamer Transfer: Amplitude, Neigung, Tensor, Flavour

14. September 2026. NON-RH. Nur `experiments/theory-contracts/`.
Keine Promotion zu verification, Ledger, Paper oder Website.

Dieselbe **fixierte** einfache Inflationsbranche und dasselbe Overlap-Modell
werden gleichzeitig gegen ACT und gegen Flavour gehalten. Es gibt kein
Nachjustieren pro Observable. Status: **Spannung**, kein neuer Fit als Lösung.

## Firewall

| Erlaubt | Verboten |
|---|---|
| Eine Parametrisierung, gemeinsame Korrekturen | `c3` als Kosmologie-Dial (+/−9,61 %) |
| Zitierte ACT-Zahlen aus Tabelle 5 v2 | Neuer Likelihoodfit ohne Deklaration |
| Joint-χ² als Diagnose entlang der Branche | Per-Observable-Retuning von N oder Texturen |
| Drei Nullmoden ≠ Massenhierarchie | Kosinus-Profil als abgeleitete SM-Hierarchie |

## Kosmologie (gemeinsam)

Unveränderte einfache Inflationsbranche, `c3 = 1/(8π)` fixiert, ohne frei
nachjustiertes N in den Invarianten:

\[
A_s(1-n_s)^2 = \frac{c_3^7}{6\pi^2},\qquad r = 3(1-n_s)^2.
\]

Äquivalent mit N: `As = N² c3^7/(24 π²)`, `ns = 1−2/N`, `r = 12/N²`.

ACT DR6 v2, Tabelle 5, Spalte **P-ACT-LB2**
([arXiv:2503.14452v2](https://arxiv.org/abs/2503.14452v2)), visuell/tabellarisch
zitiert, nicht neu gefittet:

- `ns = 0.9752 ± 0.0030`
- `log(10^10 As) = 3.062^{+0.010}_{-0.012}`

Reproduziert mit derselben Parametrisierung:

| Kalibrierung | N | Vorhersage | Abweichung |
|---|---|---|---|
| auf zentrale `As` | 56.62391 | `ns = 0.96467923`, `r = 0.003743` | **3.5069σ** in `ns` |
| auf zentrales `ns` | 80.64516 | Amplitude **2.02842×** zu groß | `r = 0.001845` |

Gemeinsames Treffen beider Zentralwerte würde `c3` um **9,61 % kleiner**
machen (`c3_req/c3 = 0.90390`). Das ist keine Reparatur: `c3` ist anderweitig
fixiert. (Die Größenordnung 9,61 % ist dieselbe Zahl wie im v1.4-Bericht;
das Vorzeichen ist eine Verkleinerung, kein Zuschlag.)

### Joint-χ² (deklarierte Diagnose, kein neuer Fit)

Kovarianz in `(ln 10^10 As, ns)`: symmetrisierter Tabellenfehler
`σ_lnAs = 0.011` aus `+0.010/−0.012`. Die **Korrelation steht nicht in
Tabelle 5** und wird nicht gefittet. Scan `ρ ∈ {−0.5, 0, 0.3, 0.8}`:

- Minimum entlang der Branche: **√χ² ≈ 3.39–3.70** (bei `ρ = 0`: **3.50**)
- Der Bestpunkt sitzt bei `N ≈ 56.4–57.2`, also an der As-Kalibrierung
- Der ns-kalibrierte Punkt `N = 80.65` hat χ² > 3000 und ist keine Lösung

Reheating verschiebt nur N **entlang** der Invariante
`As(1−ns)² = c3^7/(6π²)`. Im eingefrorenen Band `N ∈ [50, 60]` (plus
Higgs-Kanal 51.44) bleibt χ²(ρ=0) ≥ 12.3, meist weit darüber. Leading
Slow-Roll `O(1/N) ≈ 3.5 %` schließt die benötigte **~30 %-Änderung** der
Tilt-Relation nicht. Tensor `r` hängt an demselben N; kein separates
Tensor-Nachjustieren.

Invariant `C_inf = 6π² As(1−ns)²/c3^7 = 0.493` statt 1
(≈ **−2.92σ** in `ln C_inf`, ns-fehlerdominiert).

**Status: Spannung.**

## Flavour (gemeinsam)

Deklariertes Overlap-Modell (Zweitorus, `m0 = 1`, U(1)-Fluss). Fluss 3 liefert
auf `L = 8` und `L = 10` **drei** Nullmoden, keine Extra-Paare. Fluss 0 hat
zwei Nullmoden bei Index 0: ein Index allein schließt vektorartige Paare
nicht aus.

Konstantes skalares Profil:

\[
Y_{ab} = y\,\delta_{ab}
\]

Einheitsmatrix, **keine Hierarchie**. Drei Nullmoden und Massenhierarchie
sind getrennt. Ein beispielhaftes Kosinus-Profil spaltet Eigenwerte
(zwei fast entartet, eine verschoben), ist aber **neuer Input**, keine
abgeleitete Textur.

Fehlende gemeinsame Transferstücke: normierte gemeinsame Wirkung,
abgeleitetes Higgsprofil, RG vom Overlap zur IR-Masse, Gitter-/Theoriefehler
des Overlaps. Keine nachträglichen Texturen.

**Status: kein gemeinsamer Flavour-Transfer.**

## Reproduktion

```bash
python3 -B checker.py validation.json
python3 -B -m unittest test_checker
```

Auch mit `-OO`. Kein Scorecard-Eintrag (theory-contract). Kein T1–T8-Abschluss.
