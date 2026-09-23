# F1: Wer bedient das Labor? — eingefrorene Primitive

14. September 2026. NON-RH. Nur `experiments/theory-contracts`.
Keine Promotion nach `verification/`, Ledger, Papers oder Website.

## Firewall

Kein zusätzlich eingeführter Zielzustandsprojektor darf die Aufgabe
verstecken. Filter sind Polynome eines konstruierten Hamiltonoperators.
`U` ist nicht aus P1+P2 hergeleitet; die Bornregel bleibt ein Zugriffaxiom.

## Eingefrorene Primitive

| Id | Typ | Inhalt |
|---|---|---|
| `U_e` | unitäres Ereignis | Vertex aus normierten E8-Strukturkonstanten auf Materie × Vermittler × History |
| `access` | Zukunftsalgebra | Ob ein Historyfaktor später noch gelesen wird |
| `born_on_declared_access` | Messaxiom | Born auf Vermittlerbelegung oder Historybit |

Die E8-Klammer `Q` liefert nur Amplituden und relative Phasen. Sie ist nicht
die Dynamik: gemeinsames `g2`-Gewicht kann Kanten kohärent auslöschen.

## Jeder Laborhandgriff

| Handgriff | Umsetzung | Kosten | Versteckter Projektor? |
|---|---|---|---|
| Isolierte Kante | Träger von `U_e`; Löcher `\|∅_s ∅_t⟩` sind das Kantenlabel | 1 Vertex | nein |
| Belegungsabfrage | Born auf dem adressierten Vermittler | 1 Bit | nein |
| Record | History ist der Wertebereich von `U_e`; Makro `(U0⊗I)Q(U0⊗I)` | 1 `U0` + Kopie | nein |
| Kontrolliertes `H` | Virtuelle 2. Ordnung von `U_e`; `H_eff = (2t²/Δ) Σ P₊` | Zeit `τ`, `t/Δ` | nein |
| Resonanz / Filter | Fourier/Lagrange von `spec(H)` | 13 Zeiten, `Στ = 3172.829634 ℏ/Δ`; Start+Ende 26 Aufrufe | nein |
| Messung | Born auf der deklarierten Zugriffsalgebra | 1 Schuss | nein |
| Reset | Quellmessung plus Quell-Pauli | 8 Farbbits/Zelle plus Umgebung | nein |
| Präparation | Sternfilter von `H`, leeren Vermittler behalten | `w²/6 ≈ 16,19 %`, im Mittel 6,176 Versuche | nein |
| Record frisch/behalten | Zugriffsklasse auf `H_history` | Quotient `17/32` | nein |

Gleichlabelige Clebsch-Kanten sind ein 1-Faktor: vier paarweise disjunkte
Kanten. `Q` auf gemeinsamem Kanal kann sie auslöschen; die Löcher von `U`
bleiben orthogonal.

Der Tetramerfilter

`(1/8) Σ_{r=0}^{7} exp(−iπ r H / 4J)`

ist 1 auf Energie 0 und 0 auf `{2,3,4,6}`. Der eindeutige Kern ist `Ω`,
aber `Ω` ist kein Eingabeprojektor.

## Was offen bleibt

Existenz und Eindeutigkeit von `U` aus P1+P2; Bornregel; Resetumgebung /
Entropiesenke; absolute Skala von `t` und `Δ`. T1 bleibt deshalb offen.

## Reproduktion

```sh
python3 -B checker.py --output validation.json
python3 -B -m unittest test_checker
python3 -B -OO -m unittest test_checker
```

84 Bedingungen. Normal und `-OO` müssen dieselben Tests bestehen.
