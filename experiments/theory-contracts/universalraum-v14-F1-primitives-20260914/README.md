# F1 — Laborgriffe auf eingefrorene Compiler-Primitive

14. September 2026. NON-RH. Nur `experiments/theory-contracts/`.
Keine Promotion nach `verification/`, Ledger, Paper oder Website.

## Ergebnis

Jeder Bedienschritt des v1.4-Mikrolabors hat jetzt eine **eingefrorene**
primitive Operation, eine explizite Matrixumsetzung und eine Kostenzahl.
Der 544D-Sternfilter, die nackte Präparation aus dem Zweisingulett χ und
der resonante Record werden aus diesen Griffen zusammengesetzt. **P0 und Ω
sind keine Ressourcen** — sie entstehen als akzeptierter Krausausgang.
Kontrollierte Zeitentwicklung, Resonanz, Belegungsabfrage, Messung und
Reset bleiben deklarierte Primitive; sie sind hier nicht aus P1/P2
abgeleitet.

**Verdict:** `consistent` — die Reduktionen und Kosten stimmen im benannten
Modell. F1 ist damit als *Laborvertrag* geschlossen, nicht als native
Compilerherleitung.

## 1. Eingefrorene Primitive

| id | Operation | Definition | Zeit | Gatter | Bits | Versuche |
|---|---|---|---:|---:|---:|---:|
| `K_B7` | Kontextwahl | \(K=B/7\); 60-Strahl-Zeile \(1/7+12\cdot1/14+47\cdot0\) | 0 | 0 | 0 | 1 |
| `Q_C` | Quellkopplung | \(Q_C=I-2\sum_j\|j\rangle\langle j\|\otimes\|b_j\rangle\langle b_j\|\) | 0 | 4 | 0 | 1 |
| `U_C` | Vormessung | \(U_C=(W\otimes I)Q_C(A\otimes I)\), \(A\|0\rangle=\|+\rangle\), \(U_C^2=I\) | 0 | 6 | 0 | 1 |
| `C` | nackter Tick | \(0\to1\to2\to0\), \(3\to3\); \(C^3=I\) | 1 Takt | 1 | 0 | 1 |
| `Ures` | resonanter Record | \(\begin{pmatrix}P_+&-iW^\dagger\\-iW&0\end{pmatrix}\) | 1 Puls | 1 | 0 | 1 |
| `Q` | Belegung | \(I_{16}\otimes I_2\oplus I_6\otimes X\) | 0 | 1 | 1 | 1 |
| `c_exp` | kontrollierte Evolution | \(\|0\rangle\langle0\|\otimes I+\|1\rangle\langle1\|\otimes e^{-i\tau H/\hbar}\) | \(\tau\) | 1 | 1 | 1 |
| `Hadamard` | Hadamard-Test | \(H\); c-\(U\); \(H\); Messen; 0 \(\Rightarrow(I+U)/2\) | \(\tau+2H\) | 3 | 1 | 1 |
| `measure_reset` | Messung+Reset | \(M_x=X_{a\oplus x}\|x\rangle\langle x\|=\|a\rangle\langle x\|\) | 0 | 2 | 2 | 1 |
| `fresh_measured_bits` | frische/gemessene Bits | \(\|0\rangle\) bzw. klassisches Messergebnis | 0 | 1 | 1 | 1 |

Kein Eintrag ist \(P_0\), \(P_\Omega\) oder ein Zielprojektor.

## 2. Zusammensetzungen

**(a) Sternfilter.** \(A_j(H)=(I+e^{-i\tau_j(H-E_0)/\hbar})/2\),
\(\tau_j=\pi\hbar/(E_j-E_0)\). Auf dem ganzen 544D-Stern gilt
\(\prod_{j=1}^{13}A_j(H)=P_{0,\mathrm{dressed}}\).
\(\sum\tau_j=3172.829634\,\hbar/\Delta\).
Negativkontrolle: die sechs niedrigen Faktoren allein sind **kein**
Vollraumprojektor.

**(b) Nackte Präparation.** Erlaubter Eingang ist χ (zwei Singuletts,
Überlapp \(1/6\)). Leerbelegung nach dem Filter ist Q plus Messen, nicht
ein vorausgesetztes \(P_\Omega\):

\[
P_{\mathrm{bare}}P_0 P_{\mathrm{bare}}=w\,P_\Omega,\qquad
w=\bigl(1+\Delta/\sqrt{\Delta^2+24t^2}\bigr)/2\approx0.9856429312.
\]

Rohstatistik bei \(\Delta=1\), \(t=1/20\): Präparation \(w^2/6\approx0.16191533\);
gesamt behalten \(w^4/6\approx0.15729945\); frisch \(17w^4/192\approx0.08356533\);
Quotient \(17/32\); Reset \(\approx6.1761\) Versuche. Start+Schluss: 26
kontrollierte \(H\)-Aufrufe, \(6345.659268\,\hbar/\Delta\).

**(c) Record.** \(U_{\mathrm{res}}^\dagger Q\,U_{\mathrm{res}}=R\oplus I\)
auf dem lokalen 44D-Sektor, \(R=P_+\otimes I+P_-\otimes X\). Viertelphasen
braucht nur die Involution \(U_0\), nicht diese Makrooperation.

**(d) Fehlerbudget.** Zustandsfehler \(\le4\sum\tau_j(\delta H+\delta E_0)/\hbar\).
Für Infidelität \(\le10^{-6}\) bei idealen übrigen Gattern:
\(\delta H+\delta E_0\le7.88\cdot10^{-8}\Delta\) (Amplitudenbudget \(10^{-3}\)).
Zeitfehler und andere Gatterfehler sind **getrennt** auszuweisen.

## 3. Was primitiv bleibt, was abgeleitet ist

| Abgeleitet (kein extra Projektor) | Bleibt Ressource |
|---|---|
| \(P_{0,\mathrm{dressed}}=\prod A_j(H)\) | `c_exp`, `Hadamard`, Zeiten \(\tau_j\) |
| \(P_{\mathrm{bare}}\) = Q + Messen + Leerzweig | `Q`, `measure_reset` |
| \(P_\Omega\) = Leerbelegung nach dem Filter \(/w\) | Eingang χ, nicht Ω |
| Record \(R\) = \(U_{\mathrm{res}}^\dagger Q\,U_{\mathrm{res}}\) | `Ures`, `Q` |
| Kontextprozess, Vormessung, Tick | `K_B7`, `Q_C`, `U_C`, `C` |

**Entscheidender Test für F1:** Jeder Laborgriff hat eine Zeile in der
Tabelle samt Kosten, und kein Schritt darf \(P_0\) oder Ω als Input
verwenden. Das ist hier erfüllt. Dass die Primitive selbst aus der
ursprünglichen TFPT-Regel kommen, ist eine andere Frage.

## Ausführen

```sh
cd experiments/theory-contracts/universalraum-v14-F1-primitives-20260914
python3 -B checker.py validation.json
python3 -B -m unittest test_checker
python3 -B -OO -m unittest test_checker
```

`checker.py` ist deterministisch. Normal- und `-OO`-JSON sind bytegleich.
Mutanten: Sechsfaktor als Projektor, Ω als Input, falsches \(w\), 13 statt
26 kontrollierte Aufrufe, Zeit-/Gatterfehler im 7.88e-8-Budget, gebrochener
Quellpin.

## Firewall

Search-surface / theory contract, kein load-bearing Claim. Verdict-Enum
`consistent` heißt: die genannten Identitäten gelten im deklarierten
kontrollierten Modell. Keine T1–T8-Schließung, keine RH-/Faktor-/P-vs-NP-
Aussage, keine stillschweigende native Herleitung von Resonanz, isoliertem
Stern, kontrolliertem \(H\), Record, Clock oder Reset. Endliche
Clifford+T-Synthese der reellen Zeiten wird nicht behauptet.
Quellenpin: `compiler-origin-audit-20260913/context_instrument.py`
SHA-256 `ba1da931…9e3995`.
