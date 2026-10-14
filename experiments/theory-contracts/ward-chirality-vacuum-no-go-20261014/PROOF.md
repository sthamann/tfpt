# Keine E8-Erweiterung der gefalteten Quellenströme erfüllt Ward-Markierung und eindeutiges Vakuum

Gemeinsame Bedingung nach Codex (Punkt 3): Die ursprüngliche U(1)-Ladung ist
`q = (1,…,1)`; `q/2` ist eine Norm-2-Wurzel in `D8+s`, aber kein Vektor in `D8+c`;
`Q'/2 = e3+e6` ist eine E8-Wurzel.

**Klasse.** E8-Erweiterungen der Quellenströme: gerade unimodulare Gitter, die die
Bilinear-Wurzeln D8 der acht gefalteten Kanäle enthalten. Das sind genau
`E8_s = D8 ∪ (D8+s)` und `E8_c = D8 ∪ (D8+c)`. Zeitgesetz unverändert:
`K(p) = |p|²/2 + δ·p`, `δ_k = (k+α)/8 − ½`.

## Satz N [E]

1. **W1:** `q/2 ∈ E8_s`, `q/2 ∉ E8_c`. Eine orthogonale Gitterabbildung g mit
   `g(E8_c) = E8` und `g(q) = Q'` hätte `g(q/2) = Q'/2 ∈ E8`, also `q/2 ∈ E8_c`.
   Widerspruch. Die Ward-Markierung verlangt daher **E8_s**.
2. **W2:** E8_s hat für jedes geprüfte α zwei Grundzustände; E8_c hat für
   0 < α < 1 genau einen. Damit **erfüllt keine E8-Erweiterung der Quellenströme
   gleichzeitig Ward-Markierung und eindeutiges Vakuum.**
3. **W3 – geschützt:** `K(p*) = 0` bleibt unter jeder Verdrillung mit der
   Quellenladung, `δ → δ + ηq`, erhalten, weil `p*·q = 0`. Ursache ist
   `δ_{k+4} − δ_k = ½` für alle k, also die Beziehung zwischen den
   Deck-Partnerkanälen: `K(p*) = 1 − ½·Σ_{k<4}(δ_{k+4} − δ_k) = 1 − ½·4·½ = 0`.
4. **W5 – nicht eichbar:** p* ist neutral und invariant unter Fold-Clock g, g²
   und Deck g⁴, für jedes α. Eine Eichung von U(1), Clock oder Deck entfernt ihn
   nicht.
5. **W4 – Rückzug (Codex Punkt 4 bestätigt):** Eine geladene Randphase h wird auf
   dem zusammenhängenden Doppel zu h². Die Deck-Eigenräume tragen auf der Basis die
   Holonomien h und −h. Für h = ±i sind das die beiden Viertelphasen, nicht NS + R.

## Was ausgeschlossen ist, was nicht

Ausgeschlossen ist der Weg „E8 als Erweiterung der Bilinearströme des gefalteten
Quellfermions mit unverändertem Fold-Zeitgesetz". Das gilt für jede Randphase und
jede U(1)-Verdrillung, und die Chiralitätswahl rettet ihn nicht.

Nicht ausgeschlossen:
* E8-Gitter, die die gefaltete D8 **nicht** enthalten. Das ist z. B. der
  trialitätsverwandte V16-Rahmen aus `moebius-clock-fold-20261014`, F3. Dann ist
  E8 aber keine Erweiterung der Quellenströme, und die Abbildung muss aus dem
  Original kommen.
* Ein anderes Zeitgesetz mit nicht gleichmäßiger Änderung von δ, die den Abstand
  ½ zwischen Deck-Partnern aufhebt. Die Fold-Geometrie liefert das nicht.

Deutung: Die Quelle sitzt im zyklisch getwisteten Sektor der acht Kanäle, denn das
ist die Herkunft der Spreizung k/8 von δ. Genau dort trägt E8_s einen geschützten,
symmetrieinvarianten Nullzustand.
