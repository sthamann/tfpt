# Der übersehene Träger-Zeiger: die Fünf im Vier-Bank-Modell (2026-09-15)

**NON-RH, firewalled.** Theory-Contract-Experiment; keine Claims in
`verification/`, Ledger, Papers oder Website. Enum: exploratorisch.

## Frage

Was haben die Universalraum-Modellrunden (v1.6.x, Seam-Lift, Seam-Closure)
gegenüber dem TFPT-Kern übersehen?

## Antwort (Kernlektüre `origin_theory.tex`, v223/v228/v315/v316/v319/v419)

**Die Fünf.** Das zweite Axiom `g_car = 5` kommt im Vier-Bank-Modell nirgends
vor. Die Uhrdoktrin der Theorie sagt exakt verifiziert:

1. `h(E8) = 30` ist quadratfrei ⇒ `Z/30` hat kein Ordnung-4-Element ⇒ die
   μ4-Stationsuhr ist **kein Zeiger, sondern das Getriebe**: der
   Galois-Frobenius `G` des Trägerfünfecks, `G C5 G⁻¹ = C5²` (v419).
2. Die wahre Uhr ist der Ordnung-30-Coxeter-Zyklus `30 = 5·6`
   (Träger-Zeiger `Z/5` × Familien-Zeiger `Z/6 = 2N_fam`, v319). Die native
   6er-Uhr des Modells ist der Familien-Zeiger; der Träger-Zeiger `C5`
   fehlte — obwohl der Stationsraum genau `4 = deg Φ₅` Dimensionen hat.
3. Die C12-Vereinigung der Vorrunde (`lcm(4,6)`) war die falsche Lesart:
   Getriebe ⊗ Zeiger. Richtig: `lcm(5,6) = 30`.
4. Der Seam-Spiegel ist galois-seitig die komplexe Konjugation
   (`29 = −1` in `(Z/30)^×`) — dieselbe Operation, die v316 als
   CP-Konjugation identifiziert.

## Ergebnis: PASS, 26 exakte Bedingungen, alles ganzzahlig

- **A (F20):** `C5` (Φ₅-Companion, Ordnung 5) und Frobenius `G` (Ordnung 4)
  erfüllen `G C5 G⁻¹ = C5²`; `⟨C5,G⟩` hat exakt 20 Elemente (F20 = Z5⋊Z4);
  `G²` invertiert `C5` (Konjugation/CP); in der Normalbasis ist `G` der
  reine Viererzyklus — die vorzeichenlose μ4-Stationsdrehung.
- **B (30er-Uhr):** `T30 = C5 ⊗ G_F` hat auf den 4·64 = 256 Modellmoden
  exakt Ordnung 30; das μ4-Getriebe schaltet sie auf die 7. Potenz
  (`7` = Ordnung-4-Generator von `(Z/30)^×`, v223); alle sechs Spiegel
  `S = G² ⊗ S_F` sind Involutionen und invertieren sie (`S T30 S = T30²⁹`).
- **C (Holonomie):** Getriebegruppe = 8 Elemente = `(Z/30)^× = μ4×Z2 =
  rank E8 = φ(30)`; Gesamtgruppe `⟨T30, Getriebe⟩` hat exakt **240 = 30·8**
  Elemente (Holomorph von Z/30). Dass 240 die E8-Wurzelzahl ist, bleibt
  arithmetische Beobachtung, keine behauptete Identifikation.

## Ehrlich offen

- Basisidentifikation Marken (4. Einheitswurzeln) vs. Normalbasis
  (primitive 5. Einheitswurzeln) auf den Bank-Stationen.
- `g/Δ`: theorieseitiger Kandidat ist jetzt benannt — die einzige dynamische
  Rate der Theorie, `(2/3)⁶ = (|Z2|/N_fam)^{2N_fam}` auf dem
  Familien-Zeiger (v124/v312/v314/v319). Hier **nicht** behauptet.
- MARKS.01/KERNEL.01, T3/T4/T7/T8.

## Reproduktion

```bash
python3 carrier_hand.py        # → run_normal.json
python3 -OO carrier_hand.py    # → run_optimized.json (byteidentisch)
```
