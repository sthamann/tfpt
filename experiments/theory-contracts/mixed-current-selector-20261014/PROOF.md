# Beweis: Gemischter Gewicht-1-Strom wählt d = 4 ohne Abschlussannahme

Vergleichsklasse wie in `TFPT_Gesamtsynthese_2026-09-28.tex`, Abschnitt
`sec:globaloriginselection`: Zyklenseite `A_{d-1}`, Funktions-/Cliffordseite
`D_{d+1}`, `R_d = A_{d-1} ⊕ D_{d+1}`, `d ≥ 2`. Ein Gitter-Gewicht-1-Strom mit
Ladung `x` ist ein Vektor `x ∈ R_d^*` mit `|x|² = 2` (konformes Gewicht `|x|²/2 = 1`).
Er heißt **gemischt**, wenn seine Klasse in `A_{d-1}^*/A_{d-1}` und in
`D_{d+1}^*/D_{d+1}` beide nichttrivial sind: Er wirkt auf beide Lesarten
derselben Naht.

**Nicht vorausgesetzt:** gerader unimodularer (holomorpher) Abschluss, diagonaler
Glue, Stromvollständigkeit, Rang acht, E8.

## Satz M

1. Ein gemischter Gewicht-1-Strom existiert genau für `d = 4`. Die möglichen
   Klassen sind `(s,1), (s,3), (c,1), (c,3)` (Spinortyp) und `(v,2)` (Vektortyp).
2. Ein gemischter Spinorstrom erzeugt allein `R_4 + Zx ≅ E8`. Gerader
   unimodularer Abschluss ist damit **Folge**, nicht Voraussetzung.
   Ein gemischter Vektorstrom erzeugt `D8`; sein Doppeltes ist die Klasse des
   Spinorstroms: `2(s,1) = (v,2)`.
3. Ohne die Mischbedingung gibt es genau drei weitere `d` mit einem
   nichttrivial geladenen Gewicht-1-Strom, alle **zerfallend**:
   `d = 7` (reiner `D8`-Spinor, `A6 ⊕ E8`, det 7), `d = 8` (reiner `A7`-Strom,
   `E7 ⊕ D9`), `d = 9` (reiner `A8`-Strom, `E8 ⊕ D10`).

## Beweis

Für `y ∈ R_d^*` und `r ∈ R_d` gilt `|y+r|² − |y|² = 2 y·r + |r|² ∈ 2Z`, weil
`R_d` gerade ist und `y·r ∈ Z`. Alle Normen einer Nebenklasse sind also
kongruent modulo 2 zu ihrem Minimum. Eine Nebenklasse `(c,k) ≠ (0,0)` enthält
daher einen Norm-2-Vektor genau dann, wenn `μ_D(c) + μ_A(k) = 2` (das Minimum
ist positiv und höchstens 2). Die Minima sind
`μ_A(k) = k(d−k)/d`, `μ_D(0)=0`, `μ_D(v)=1`, `μ_D(s)=μ_D(c)=(d+1)/4`.

* Vektortyp, `k ≠ 0`: `k(d−k) = d`, also `d = k+1+1/(k−1)`; ganzzahlig nur
  `k = 2, d = 4`.
* Spinortyp, `k ≠ 0`: `(d+1)/4 < 2` erzwingt `d ≤ 6`. Für `d = 2,…,6` hat
  `d² + (4k−7)d − 4k² = 0` nur `(d,k) = (4,1),(4,3)`.
* Nicht gemischt: `(s/c,0)` verlangt `(d+1)/4 = 2`, also `d = 7`; `(0,k)`
  verlangt `k(d−k) = 2d`, also `(d,k) ∈ {(8,4),(9,3),(9,6)}`; `(v,0)` hat Norm
  ungerade.

Für 2.: Ist `|x|² = 2` und `x ∈ R_d^*`, so ist `R_d + Zx` gerade, da die
Diskriminantenform `q(jx) = j² q(x) ≡ 0 (mod 2)`. Der Index ist die Ordnung
von `[x]`, also 4 für `(s,1)` und 2 für `(v,2)`; `det = 16/16 = 1` bzw.
`16/4 = 4`. Das einzige gerade unimodulare Gitter vom Rang 8 ist E8; das
Index-2-Gitter ist `D3 ⊕ D5 + (v,v) = D8` (mit `A3 ≅ D3`). ∎

## Zusatz: Lage der Auswahlinformation unter der internen Z4-Graduierung

Im E8-Modell `E8 = D8 ∪ (D8+s)`, Koordinaten `(p1..p5 | p6..p8)`, mit
`L0 = D5 ⊕ D3 = R_4` und interner Gluegraduierung `k(p) = 2 Σ_{i≤5} p_i mod 4`
(siehe Synthese, `CU_sC^{-1} = iU_s`) verteilen sich die 240 Wurzelströme auf
die Grade 0/1/2/3 als **52 / 64 / 60 / 64**:

* Grad 0 = Wurzeln von `R_4` selbst. Solche Ströme existieren für **jedes** d
  und wählen nichts aus.
* Grad 2 = gemischte Vektorströme: wählen d = 4, erzeugen aber nur D8.
* Grad 1, 3 = gemischte Spinorströme: wählen d = 4 und erzeugen E8.

Die neutrale Erwartung `E0 = ¼ Σ_k C^k (·) C^{-k}` behält genau Grad 0.
**Die gesamte Auswahlinformation liegt damit in den Graden, die `E0` entfernt.**
Ein Strom `J` vom Grad 1 hat `E0(J) = 0`, sein Paar `J*J` ist neutral und
sichtbar. Das ist dieselbe Struktur wie der Zeuge `E0(X)=0`, `E0(X*X)=P0` aus
`v993`; die bereits bewiesene mikroskopische Paarantwort
`(1−e^{2πi(b−a)})^{-2}` ist genau dieser sichtbare neutrale Schatten.

Die Identifikation der internen Gluegraduierung `C` mit der Clock `u` aus
`v993` ist **nicht** Teil dieses Beweises (Registerladung, Fermionenmonodromie
und Gluegrad sind laut Synthese verschiedene Wirkungen).

## Was dadurch nicht bewiesen ist

* Dass die ursprüngliche mikroskopische Nahtoperation einen solchen gemischten
  lokalen Gewicht-1-Strom erzeugt (`SEAM.SIMPLECURRENT.GENERATOR.01`,
  `SEAM.MMST.TYPEIII.CHARGED.01` bleiben offen).
* Spinortyp statt Vektortyp (das eine verbleibende Bit E8 vs. D8).
* Die Vergleichsklasse selbst (Clifford-Lesart, Gittermetrik), P1, Zustand,
  Zeit, 3+1D.
