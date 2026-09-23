# KeyC: Kondensat- oder Zustandshypothese — Ergebnisse

**Theory Contract, 15. September 2026.** Hypothese „die Zustandsregel erzeugt
den Raum": geprüft wird, ob der native N=64-Grundzustand auf eine
Multiplizitäts-Kopie lokalisiert (Copy-Symmetrie gebrochen) oder über die
vier Level-2-Singulettkopien delokalisiert ist, plus selbstkonsistente
Regel min E(N)/N. Keine Claims in Papers/Ledger/Website, keine Commits.

Labels: **exakt** = Ganzzahl/rational mit Guard; **numerisch** = float64 mit
Toleranz-Guard (Ritz-Eigenwerte, Überlapp-Kombination);
**bedingt** = μ*-Intervall (exakte + numerische Kante); **offen** = mit den
rigorosen Schranken nicht entschieden (Floors notwendig-nicht-hinreichend).

## 1. Level-2-Lokalisierungsprofil (Aufgabe 1)

Singulettbasis `s_R = P_R v2/‖P_R v2‖`, `R ∈ {(54,1),(1,20′),(54,20′),(45,15)}`
(**exakt**: Projektoren aus Spin/Color-Spuren; `(1,1)`-Anteil exakt 0;
jede Kopie Multiplizität 1, daher `P_R w2 ∝ P_R v2`).

v2-Normen (**exakt**): 17280, 7680, 241920, 172800 (Summe 439680);
Kopplungen `‖P_R v2‖²/480` (**exakt**): 36, 16, 504, 360 (Summe 916).
Normiertes v2-Profil `p_R = ‖P_R v2‖²/‖v2‖²` (**exakt**):
9/229 = 0,03930; 4/229 = 0,01747; 126/229 = 0,55022; 90/229 = 0,39301.
Partizipation PR = 2,178, max = 0,550 (**exakt**): keine Konzentration.

w2 (skaliert `q=229`, `‖w2‖²=5001523200/229`, **exakt**): skalierte
R-Normen 131632128000, 232996331520, 448772244480, 331948108800
(Summe 1145348812800, **exakt**); Eigenprofil `q_R` (**exakt**):
0,11493; 0,20343; 0,39182; 0,28982 (PR = 3,423, max = 0,392).
Mischkoeffizienten `λ_R = ⟨P_R v2|P_R w2⟩/(q‖P_R v2‖²)` (**exakt**):
2760/229; 5508/229; −1362/229; 1386/229. Kreuzsumme 0 (`w2⊥v2`, **exakt**).

K=3-Ritz bei `g/Δ=1/20` (**numerisch**): E = −1,09423187;
evec = (0,63044; −0,62975; 0,41514; −0,18335; 0,000577);
Level-2-Gewicht `c2²+cw²` = 0,17234 (w2-Anteil 3,3·10⁻⁷, vernachlässigbar).

`|⟨s_R|Ω_K3⟩|²` (**numerisch** = exakte R-Normen × numerische Ritz-Koeffizienten):
(54,1): 0,006805; (1,20′): 0,003039; (54,20′): 0,094602; (45,15): 0,067894
(Summe 0,17234 = Level-2-Gewicht, Guard 10⁻⁹).
Bedingt auf Level 2 (**numerisch**): 0,03949; 0,01763; 0,54893; 0,39395
(PR = 2,182, max = 0,549) — praktisch das v2-Profil.

**Verdikt (exakt/numerisch): delokalisiert.** Weder v2 noch w2 noch Ω_K3
sind auf eine Kopie konzentriert (Schwelle 0,9 nie erreicht); die
Copy-Permutationssymmetrie wird vom Zustand **nicht** gebrochen.

## 2. Copy-Symmetrie-Wirkung (Aufgabe 2, exakt)

Gruppe G: Ordnung 768 (**exakt**, BFS + Orbit-Stabilisator 64·12).
Orbits (**exakt**): Moden 1×64; Paare 31; Bosonen 5×12; Vertizes 5.
W-Kovarianz `W·Λ²G_F = G_B·W` für alle 7 Generatoren (**exakt**, dünn).
`det(G_F) = +1` für alle 7 Generatoren (**exakt**) — |F⟩, v2, w2 invariant
(kein Vorzeichen); `T_+` G-invariant ⇒ jede R-Kopie erhalten, keine
Permutation, kein Mischen. 4 Kopien ≠ 5 Boson-Orbits: Kopien sind
Irrep-Labels, keine G-Orbits. Ritz-Profil invariant (**exakt**, `det²=1`).

**Verdikt (exakt): Copy-Symmetrie erhalten.** Die Quellgruppe rotiert die
vier Kopien nicht; das delokalisierte Profil ist G-invariant.

## 3. Selbstkonsistente Zustandsregel (Aufgabe 3)

Floors `E_floor(N)` (**exakt**, notwendig-nicht-hinreichend): alle `N≤64`
`−15/800·N` (Nb=0 optimal), pro N degeneriert `−3/160 = −0,01875`;
N=59: −177/160; N=60: −9/8; N=61: −183/160; N=62: −93/80; N=63: −189/160;
N=64: −6/5 (Kandidat); N=65: −29/160; N=66: −1/5; N=68: +4/5.

| N | E_floor (exakt) | E/N (exakt) | Singulett (Z4) |
|---:|---|---|---|
| 56 | −21/20 | −3/160 | ja |
| 60 | −9/8 | −3/160 | ja |
| 64 | −6/5 (+ Ritz5 −1,138476 numerisch) | −3/160 (Floor) / −0,01779 (Ritz) | ja |
| 68 | +4/5 | +1/85 | ja |

Ritz-Obergrenzen N=64 (**numerisch**): K=3: −1,094232; K=4: −1,129638;
K=5: −1,138476 (monoton, reproduziert). Bestes Ritz-pro-N (−0,01779) liegt
strikt **über** der Floor-Linie (−0,01875): keine Separation.
μ* (`E+μN`-Konvention; **bedingt**): Floor-Kante 0,01875 (**exakt**),
Ritz3-Kante 0,01710, Ritz5-Kante 0,01779 (**numerisch**);
`μ=Δ/50=0,02` wählt den leeren Zustand (konsistent).

**Verdikt (offen): min E/N selektiert N=64 nicht.** Die Floor-Gewinner sind
über alle `N≤64` degeneriert (inkl. Nicht-Singuletts `N≠0 mod 4`); wahre
`E(N)` unbekannt; hinreichende Schranken fehlen.

## 4. Kondensatkriterium (Aufgabe 4)

μN-Freiheit (**exakt**): Level 2 bei N=64 hat uniform `Nf=60,Nb=2` ⇒ μN ist
c-Zahl, Splitting 0 — kann nicht lokalisieren.
G-invariante level-diagonale Operatoren sind per Schur diagonal in R
(kein Mischen, nur Splitting); alle hellen Kopplungen >0
(**exakt**: 36, 16, 504, 360) ⇒ bei endlichem Shift bleiben alle vier
R-Gewichte >0. Scan `|ε|≤Δ` im 6-dim-Modell (81 Ecken, **numerisch**):
schlimmstes max-Gewicht 0,828, schlimmste PR 1,412 — nie >0,9.

**Verdikt (exakt/numerisch): Lokalisierung braucht G-Brechung.**
Innerhalb der dokumentierten Algebra (μN + level-diagonale Singulett-
Operatoren) ist kein Kondensat auf eine Kopie erreichbar; eine Kopie
selektieren hieße 3 von 4 Kopplungen nullen oder R mischen —
außerhalb der inneren Symmetrie.

## 5. Verifikation

`replay.py`: 3 Checker je normal + `-OO`, byteidentisch, PASS.
Guards: localize 48, copysym 56, staterule 53 (Summe 157).
Budget eingehalten: keine Level-3-Basis (257 Mio.); v3 (15.252.960 Einträge)
kanalweise gestreamt. Kein Commit, keine Ledger/Paper/Website-Änderung.
