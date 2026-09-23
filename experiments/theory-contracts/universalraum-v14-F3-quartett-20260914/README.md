# F3: Vierfachstruktur — exakte Projektoren, bedingter Sektorvergleich

14. September 2026. NON-RH. Nur `experiments/theory-contracts`.
Keine Promotion nach `verification/`, Ledger, Papers oder Website.

## Firewall

Gleitkomma-`eigh` zählt keine Multiplizität. Residuenkugeln um acht
Lanczos-Paare sind kein Intervallzertifikat des 24.024D-Operators.
Die berichtete nackte Nichtsingulettuntergrenze `12.133537149348086`
ist **nicht** zertifiziert. Der kanonische `H6`-Rest bleibt separat offen
und wird nicht behauptet.

## Status, ehrlich getrennt

| Klasse | Inhalt |
|---|---|
| **exakt** | Operatoridentitäten, `S6`-Annihilator, `f` streng steigend, Rang-4-Idempotent in `ℚ[S5]`, `0 ≤ H0 ≤ 40 I`, Schur–Weyl |
| **zertifiziert** | Gershgorin `[0,10]` für `Av`; rationale LDL-Inertia und Temple auf der ganzzahligen Standard-4 von `S5`; `\|Aut(Clebsch)\|=1920` |
| **bedingt** | *Wenn* das nackte Nichtsingulettminimum `≥ 12.133537149348086`, dann `f(H0) ≥ 12.96487952485328` über der variationalen Viererraum-Obergrenze `12.447023775951228` |
| **offen** | Intervall der 180.180D-Adjungierten; Intervall des 24.024D-trunkierten Spektrums; `H6` |

Die Vierfachheit ist **nicht** mit Spektralzertifikat bewiesen. Exakt ist
ein Rang-4-Projektor und dass jeder `Aut`-invariante Operator Isotypen
erhält. Die Identifikation des numerischen ersten Clusters mit diesem
Isotyp bleibt an die gepinnte dichte Singulettanalyse gebunden.

## 1. Exakte Bausteine

`Ee = I − Se`, `Ee² = 2 Ee`, `Av = Σ_{e∋v} Ee`, `A = Σ_e Ee`, `Σ_v Av = 2A`.
Auf der ganzzahligen regulären Darstellung von `S4` (24D):

`F4,edge = 2A + Σ_{Überlapp} {Ee,Ef} = Σ_v Av² − 2A = Σ_v Av(Av−I)`.

`720D`-reguläres `S6`: `Π_{k=0}^{10}(Av − kI) = 0` exakt, Gershgorin
`[0,10]`, also `Av ≥ 0` ganzzahlig und `Av(Av−I) ≥ 0`.

Clebsch (16 Orte, 40 Kanten, Grad 5): `A = 80I − 2H0` und
`Σ_v (Av − A/8)² ≥ 0` liefert die Operatorschranke

`F4,edge ≥ A²/4 − 2A = H0² − 76H0 + 1440 I`,

ohne gemeinsame Diagonalisierbarkeit der `Av`. Bei `ε = 1/20` ist
`f(h) = h + ε²(h² − 76h + 1440)/2` auf `[0,40]` streng steigend
(`f'(0) = 181/200`).

## 2. Singulettlauf (gepinnt, nicht neu diagonalisiert)

`H0 + 0.00125 F4,edge` im 24.024D-Singulett, aus
`spectrum_followup.json` (Hash gepinnt):

- `E0 = 11.960507412663516`
- `E1 = 12.446984939669278`
- Gap `0.4864775270057624`
- max. Residuum `4.75e-14`
- variationelle Viererraum-Obergrenze `12.447023775951228`

Das sind reproduzierte Gleitkommazahlen des *trunkierten* Operators,
kein Intervall des vollen Spektrums.

Exakter Symmetrieprojektor: zentrales Idempotent von `[4,1]` in `ℚ[S5]`,
`e² = e`, `tr(e) = 4`, orthogonal zum trivialen Idempotent. `S5` hat
keine Irreps der Dimension 2 oder 3.

## 3. Nacktes Nichtsingulett — Methode da, Zahl nicht

Die 64-Sektor-Tabelle nennt das nackte Minimum im Adjungierten
`(5,4,4,3)` (`dim S_n = 180180`, `dim SU(4) = 15`) als
`12.133537149348086`. Gershgorin/Projektorensumme zertifiziert nur
`H0 ∈ [0,40]`. Die Schwelle, ab der `f` die variationelle Obergrenze
schlägt, liegt bei etwa `11.58`. `0` liegt darunter, die berichtete
Zahl darüber — aber nur die berichtete Zahl ist nicht zertifiziert.

Auf der ganzzahligen Standard-4 von `S5` laufen Intervall-, Inertia-
und Temple-Schranken durch (Methodenzeugnis, nicht die 180.180D-Zahl).

Sobald eine zertifizierte nackte Untergrenze `≥ 12.133…` vorliegt,
wird der Sektorvergleich `bedingt → zertifiziert`. Bis dahin: bedingt.

## Negativkontrollen

`Se` selbst verletzt `Ee² = 2Ee`; das `S6`-Produkt nur bis `k=9`
verschwindet nicht; `A = 80I − H0` zerstört das Schrankenpolynom;
`ε = 1` macht `f'(0) < 0`; `f(11) = 11.90625` liegt unter `12.447`;
der triviale Projektor hat Rang 1, nicht 4; Gershgorin beweist
`H ≥ 8` auf der kleinen Form nicht.

## Reproduktion

```sh
python3 -B checker.py validation.json
python3 -B -m unittest test_checker
python3 -B -OO -m unittest test_checker
```

239 Bedingungen (213 exakt, 10 zertifiziert, 7 Negativkontrollen, 9 numerisch),
10 Tests, normal und `-OO`. Die schweren 24.024D- und 180.180D-Läufe werden
nicht wiederholt. Quellenhashes stehen in `checker.py`.
