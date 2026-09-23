# μ₄-Pointing auf der Seam: trägt die Seam mehr als die Kardinalität? — 17. September 2026

Endliche, nichtarithmetische Forschungsrechnung (NON-RH). **Firewall:** dies
ist ein Theory-Contract-Experiment — **keine** Claims in `verification/`,
`status_ledger.csv`, Papers, Website oder Scorecard (Theory-Contracts kommen
nie in die Scorecard), keine Beförderung. **MARKS.01 und T4 bleiben offen**,
egal wie dieser Lauf ausgeht; eine Promotion wäre ein separater Schritt nach
`promote-to-verification`.

## Hypothese (Prüfstand, kein Claim)

> μ₄ wurde bisher nur als Kardinalität |μ₄| = 4 genutzt; seine
> Pointing-Struktur (Basispunkt 1, Orientierung i, Vorzeichen −1) ist die
> fehlende Semantikschicht für MARKS.01 (rohe Seam → markierter Rand) und
> T4 (chirales Maß).

Angriffsform: Die Seam trägt **bereits** eine kanonische
μ₄-Pointing-Struktur, und das abstrakte ℤ₄ (nur Kardinalität) reicht für
die betreffenden Tests **nicht**. Der Diskriminator der Hypothese ist genau
dieser Kontrast — deshalb ist die Negativkontrolle (B4) Teil der Prüfung,
nicht Beiwerk.

## Vorrunden-Befund (VERIFIED)

Quelle: `universalraum-seam-closure-20260915` (PASS, 44 exakte Bedingungen):
T = R ⊗ G_F auf den 4·64 = 256 Fermionmoden hat Ordnung 24 mit T¹² = −I;
sechs gemeinsame Spiegel S = J ⊗ S_F erfüllen S² = I und S T S⁻¹ = T⁻¹;
⟨T,S⟩ hat 48 Elemente. Boson-Uhr T_B = P_link ⊗ G_B hat Ordnung 12 ohne
−I. Offen danach: u. a. MARKS.01 (rohe Seam → markierter Rand,
„konstruktive Geometrie, keine endliche Rechnung") und T4 (chirales Maß).
Kontext: `universalraum-carrier-hand-20260915` ordnet die μ₄-Stationsuhr
als Galois-Getriebe des Trägerfünfecks ein (kein Zeiger) — dieser Contract
prüft eine davon unabhängige, schwächere Frage: ob auf der Seam-Gruppe
selbst mehr als die Kardinalität 4 ausgezeichnet ist.

## Präregistrierte Bedingungen (festgelegt vor dem Lauf)

**B1 — Auszeichnung der C4.** ⟨T,S⟩ enthält genau EINE Untergruppe ≈ C4:
die Ordnung-4-Elemente sind exakt T⁶ und T¹⁸. Sie ist normal (jede der
sechs Spiegelungen konjugiert T⁶ zu T¹⁸). Ihr einziges Involutionselement
ist T¹² = −I — das Vorzeichen −1 der Pointing wäre damit kanonisch und
mit dem Fermionvorzeichen identisch.

**B2 — Orientierung (T4-Angriff).** Die zwei Erzeuger T⁶, T¹⁸ werden als
Operatoren verglichen; jede Seam-Spiegelung vertauscht sie. (T¹⁸)² = −I
und tr(T¹⁸) = 0, also Eigenwerte ±i: jede Pointing-Wahl liefert eine
bestimmte chirale Graduierung der 256 Moden; die zwei Pointings liefern
entgegengesetzte. Bosonseite: T_B⁶ vs. T_B¹⁸ (Orientierungsblindheit?).

**B3 — Basispunkt.** Ist eine der vier Stationen geometrisch
ausgezeichnet? Modellseite: Stationsbild von R und J. Rohe Seam
(v480-Ring, ganzzahlige Kombinatorik): Fixstationen der vier
stationenerhaltenden Spiegelungen.

**B4 — Negativkontrolle (muss scheitern, sonst WIDERLEGT).** Abstraktes
ℤ₄ ohne Pointing: die bosonische ℤ₄ = ⟨T_B³⟩ existiert (Kardinalität ist
da), aber ihr Involutionselement T_B⁶ ≠ −I, und −I liegt in keinem
Element von ⟨T_B, S_B⟩ — die Vorzeichenschicht fehlt dem unpointierten
ℤ₄. Ohne Erzeugerwahl ist die chirale Graduierung nur bis auf
Vertauschung bestimmt (B2 prüft, dass die Pointings disagree), ohne
Stationswahl gibt es keinen Basispunkt (B3).

**B5 — Konsistenz und Markierungsraum.** Die Markierungswahl ändert
keinen Operator: Replay der pointing-relevanten Seam-Closure-Schnittstelle
(R⁴ = −I, R⁸ = I, G_F⁶ = I, J R J = R⁻¹, T¹² = −I, Ordnung 24, sechs
Spiegel als Involutionen mit S T S = T⁻¹, |⟨T,S⟩| = 48,
Casimir-Identität, W Λ²(S_F) = S_B W, S_B² = I, S_B T_B S_B = T_B⁻¹).
Der Markierungsraum M = {Basispunkt ∈ ℤ4} × {Orientierung ∈ ±1} trägt die
durch die Operatoren induzierte Aktion t:(b,ε)↦(b+1,ε),
s:(b,ε)↦(−b,−ε); Bildgröße, Gruppenstruktur und Transitivität werden
exakt bestimmt.

## Verdict-Enum (präregistriert)

- **PASS** — alle Checks grün, und die Faktenlage zeigt die VOLLE Pointing
  auf der Seam: C4 eindeutig und normal, Vorzeichen kanonisch, UND
  Orientierung UND Basispunkt geometrisch ausgezeichnet; Negativkontrolle
  diskriminiert.
- **PARTIAL** — alle Checks grün; die Seam trägt die C4 und das Vorzeichen
  kanonisch, aber mindestens eine Pointing-Schicht (Orientierung oder
  Basispunkt) ist nachweislich NICHT ausgezeichnet; die Negativkontrolle
  diskriminiert weiterhin (abstraktes ℤ₄ scheitert wie gefordert).
- **FAIL** — mindestens ein exakter Check schlägt fehl (z. B. C4 nicht
  eindeutig, Markierungsaktion widerspricht den Operatorrelationen,
  Replay bricht).
- **WIDERLEGT** — die Negativkontrolle diskriminiert nicht: abstraktes ℤ₄
  ohne Pointing besteht dieselben Tests (Vorzeichen/Graduierung/Basispunkt
  ohne Wahl bestimmt) — die Pointing wäre irrelevant, die Hypothese
  widerlegt.

Hinweis: `status: PASS` im Skript-JSON bezeichnet nur die Rechenintegrität
(alle Bedingungen bestanden); das inhaltliche Contract-Verdict steht in
`RESULTS.md`.

## Dateien

- `mu4_pointing.py` — der Checker, ganzzahlig exakt (int64, keine Floats).
- `RESULTS.md` — Bericht nach dem Lauf, exakte Zahlen, Verdict.

## Reproduktion

```sh
cd experiments/theory-contracts
python3 universalraum-mu4-pointing-20260917/mu4_pointing.py
```

Benötigt NumPy und SciPy sowie repo-lokal `native_common.py`
(v1.6.9-Quellpaket), den gepinnten Tensor
`universalraum-v16-integrated-20260915/sources/native_tensor.npz` und den
gepinnten Clock-Konstruktor `compiler-involution-types/checker.py`
(SHA-256-Pins via `native_common`). Kein Zugriff außerhalb des
Repositorys. Der Lauf endet mit `status: PASS` und der Zeile
`N/N Bedingungen`.
