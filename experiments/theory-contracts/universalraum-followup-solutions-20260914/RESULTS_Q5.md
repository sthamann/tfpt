# Q5: Entsteht daraus eine einzige gemeinsame Welt?

## Eine einzige native skalierende Familie durch alle vier Welt-Tests

14. September 2026. Forschungsresultat, keine T1-T8-, RH- oder Komplexitaetspromotion.

Die v1.4-Pruefung verwendete pro Phaenomen ein **separates** Kontrollmodell. Hier
laeuft die **selbe Familienobjekt** — `C16 x (Z/LZ)^d` mit internem Operator
`H_int = A_C16` (Clebsch-Adjazenz, Spektrum `{5, 1, -3}`) — durch **alle vier**
Tests zugleich. Kein pro-Test-Modellaustausch.

### Familienobjekt (einmal deklariert, fuer alle Tests)

- Graph: `C16 x (Z/LZ)^d`. `C16` = Clebschgraph: 16 Stellen = gerade Paritaet
  `{+-1}^5`, 40 Kanten (Paare, die in genau 4 Koordinaten differieren).
- Adjazenzspektrum: `{5^[1], 1^[10], (-3)^[5]}` (numerisch verifiziert).
- Laplace-Spektrum: `lambda = lambda_int + 4 sum_mu sin^2(pi k_mu / L)`,
  `lambda_int in {0 (x1), 4 (x10), 8 (x5)}` (`L = 5 - A`).
- Pruefer: `one_family.py`, **214 Bedingungen**, normal/`-OO` bytegleich,
  `checker_sha256 = 06e543cb9ccd08846b1b847b6f9035c8e41a09b20f027c27f4a2d4afa89d4dd2`.

---

## T3 — Spektrale Dimension

Waermekernspur faktorisiert exakt: `Z(t) = Z_int(t) * Z_torus(t)^d`. Spektrale
Dimension `d_s = -2 d log Z / d log t` (exakt aus den Summen, `t = 8`).

| d | L | d_s | d_s / d |
|---|---|---|---|
| 1 | 16 | 1.00244 | 1.00244 |
| 1 | 64 | 1.00367 | 1.00367 |
| 2 | 16 | 2.00549 | 1.00275 |
| 2 | 64 | 2.05014 | 1.02507 |
| 3 | 16 | 3.01101 | 1.00367 |
| **3** | **64** | **3.05014** | **1.01671** |
| 4 | 16 | 4.01649 | 1.00412 |
| 4 | 64 | 4.10027 | 1.02507 |

**v1.4-Bestaetigung:** bei `(d=3, L=64, t=8)` ist `d_s = 3.05014`, `d_s/d = 1.01671`
(v1.4: ~1.0167 d). **OK.**

**VERDICT T3:** Die Familie **reproduziert** die eingesetzte Dimension — sie
**waehlt** nicht `d = 3`. Fuer jedes `d in {1,2,3,4}` liefert derselbe Waermekern
`d_s ~ d`. **Fehlende Zutat:** ein Prinzip aus der Quelle, das `d` (und `L` bzw.
einen Kontinuumslimes) auswaehlt; ein Waermekern ist kein kausaler Propagator und kein
Auswahlmechanismus.

---

## CONE — Gemeinsamer Lichtkegel

Dispersion: `omega(k) = sqrt(lambda_int + 4 sin^2(pi k / L))`.
`v = d omega/dk = (2 pi / (L omega)) sin(2 pi k / L)`. `L = 64`, `k = 1`.

| lambda_int | v(k=1) | v(k->0) | omega(k=0) |
|---|---|---|---|
| 0 (masselos) | 0.098057 | 0.098175 (= 2 pi/L) | 0.0000 |
| 4 (massiv) | 0.004806 | 4.82e-06 (-> 0) | 2.0000 |
| 8 (massiv) | 0.003400 | 2.40e-06 (-> 0) | 2.8284 |

- **Mismatch-Verhaeltnis** `v(lam=4) / v(lam=0) = 0.04901` (massiver Kanal ~20x langsamer).
- `k -> 0`: massloser Kanal `v -> 2 pi/L`; massiver Kanal `v -> 0`.

**VERDICT CONE:** Derselbe Graph traegt **verschiedene Kegel** pro internem Kanal.
Ein gemeinsamer Kegel fuer mehrere Spezies ist **nicht automatisch** — nur wenn alle
propagierenden Spezies `lambda_int = 0` teilen (genau ein Kanal). **Fehlende Zutat:**
eine einzige quadratische Form (eine Metrik), die alle Spezies regiert; entartete
niederenergetische Propagation nur in einem gemeinsamen masselosen Sektor.

---

## T4 — Chiralitaet

Wilson-Dirac auf **derselben Familie** bei `d = 2`:
`D = D_torus(m0=1, U(1)-Fluss) ⊗ I_16 + I_{2LL} ⊗ (c * A_C16)`.
Overlap `D_ov = I + gamma5 sgn(gamma5 D)`, `gamma5 = gamma5_torus ⊗ I_16`.
Gesamtdimension `2 * 8 * 8 * 16 = 2048`. Blockstruktur: in der internen Eigenbasis
ist `A_C16` diagonal, also Bloecke `H_lam = H_tor + c*lam*g5_tor` (dim 128), jeweils
`mult(lam)`-fach. Effektive Masse pro Kanal: `m_eff = 1 + c*lam`.

### Effektive Massen bei `c = 1/8`

| lam | mult | m_eff = 1 + c*lam |
|---|---|---|
| -3 | 5 | 5/8 = 0.625 |
| 1 | 10 | 9/8 = 1.125 |
| 5 | 1 | 13/8 = 1.625 |

### Primaerlauf: `flux = 3`, `c = 1/8`, `L = 8`

| Groesse | Wert |
|---|---|
| Gesamt-Nullmoden | **48** |
| Index | **-48** |
| GW-Defekt | 8.26e-13 |
| pro Kanal lam=-3 | 15 (5 x 3) |
| pro Kanal lam=1 | 30 (10 x 3) |
| pro Kanal lam=5 | **3** (1 x 3) |

Alle drei internen Kanaele sind im physikalischen Fenster `|c*lam| < 1`. Der
`lam=5`-Kanal (Mult 1) allein liefert 3 gleichchirale Moden — aber vermischt mit
45 weiteren aus den Kanaelen `lam=-3, 1`.

### Kontrollen bei `c = 1/8`

| flux | Gesamt | Index | pro Kanal (-3 / 1 / 5) |
|---|---|---|---|
| 1 | 16 | -16 | 5 / 10 / 1 |
| 3 | 48 | -48 | 15 / 30 / 3 |
| 4 | 64 | -64 | 20 / 40 / 4 |

Index = `16 * flux` (alle Kanaele aktiv). **OK.**

### c-Scan: `flux = 3`, `c in linspace(-2, 2, 81)` + 95 verfeinerte Punkte

Gemessene Zaehlfunktion `f(c, flux=3)` — Uebergaenge:

| c-Bereich | total | index | (-3 / 1 / 5) | Erklaerung |
|---|---|---|---|---|
| [-2.0, -1.05] | 34 | +30 | 0 / 30 / 4 | lam=1 Doubler, lam=5 Uebergang |
| [-0.95, -0.6] | 34 | -30 | 0 / 30 / 4 | lam=1 physikalisch, lam=5 Uebergang |
| [-0.55, -0.3] | 33 | -27 | 0 / 30 / 3 | lam=1 physik., lam=5 Doubler |
| [-0.15, +0.15] | 48 | -48 | 15 / 30 / 3 | alle physikalisch, gleich |
| [+0.2, +0.3] | 45 | -45 | 15 / 30 / 0 | lam=5 ausserhalb |
| [+0.35, +0.85] | 45 | -15 | 15 / 30 / 0 | lam=-3 Doubler, lam=1 physik. |
| [+0.9, +0.95] | 15 | +15 | 15 / 0 / 0 | nur lam=-3 Doubler |
| [+1.0, +2.0] | 20 | 0 | 20 / 0 / 0 | lam=-3 Uebergang, Index 0 |

**Kein einziges `c` liefert `total_zero = 3`.** Das Minimum ist 15 (nur `lam=-3`
im Doublerfenster bei `c ~ 0.9`). Drei gleichchirale Moden erfordern die Isolierung
des `lam=5`-Kanals (Mult 1), aber dessen aktives Fenster `|c| < 0.2` ist **enthalten**
im aktiven Fenster von `lam=1` (`|c| < ~0.9`), also ist `lam=1` (Mult 10) stets
mitaktiv. Kein Quellenprinzip waehlt das noetige `c`/Fluss-Paar aus.

**VERDICT T4:** Die Familie **waehlt nicht drei Familien nativ**. Der Nullmoduszaehler
ist eine Funktion `f(c, flux)`: bei `c = 1/8`, `flux = 3` sind es 48 (davon 3 im
`lam=5`-Kanal); ueber den ganzen Scan kein `c` mit genau 3 Gesamt-Nullmoden.
**Fehlende Zutat:** ein quellenabgeleiteter Grund fuer das spezifische `c`/Fluss-Paar;
drei gleichchirale Moden erfordern explizites Tuning.

---

## T7 — Tensorsektor

TT-Projektor: `TT = (P⊗P symmetrisiert) - (1/2) P⊗P Spuranteil`, `P = I - k k^T`,
`k = (0,0,1)`.

| Groesse | Wert |
|---|---|
| TT-Rang | 2 |
| `||TT^2 - TT||` | < 1e-14 (Projektion) |
| TT2 (k=(1,0,0)) Rang | 2 (frequenzunabhaengig) |
| Masseloser Spin-2-Pol | **nein** |

Freie gapped Bilineare, `m = 0.5`, Schwelle `2m`:

| L | min omega | Schwelle 2m |
|---|---|---|
| 8 | 0.500000 | 1.000000 |
| 16 | 0.500000 | 1.000000 |
| 32 | 0.500000 | 1.000000 |
| 64 | 0.500000 | 1.000000 |

Der TT-Projektor hat Rang 2 und keinen Frequenznenner — er erzeugt **keinen Pol**.
Die gapped Bilineare hat Schwelle `2m = 1 > 0` bei allen Gittergroessen.

**VERDICT T7:** Aus der deklarierten Familiendynamik entsteht **kein masseloser
Spin-2-Modus**. **Fehlende Zutat:** ein tatsaechlicher masseloser Spin-2-Sektor mit
Constraints (Eichstruktur) aus derselben Quelle.

---

## JOINT — Gemeinsame Fehlerkarte

Eine Familie, vier Tests, exakte Fehlerkarte:

| Test | Resultat |
|---|---|
| T3 | Dimension reproduziert, nicht ausgewaehlt (`d_s = 1.0167 d` bei `d=3, L=64`) |
| CONE | Gemeinsamer Kegel nicht automatisch (`v4/v0 = 0.049` Mismatch) |
| T4 | Nullmoduszaehler = `f(c, flux)`; 3 chirale Moden erfordern Tuning (kein `c` liefert `total = 3`) |
| T7 | Kein masseloser Pol (TT Rang 2, Schwelle `2m = 1`) |

**Aussage:** Ein positiver Test fuer nur einen Punkt bleibt ein Teilresultat. Hier
wird **kein Punkt nativ** von der einzelnen Familie bestanden. Die vier fehlenden
Zutaten sind:

1. **T3:** Ein Prinzip aus der Quelle, das `d` (und `L` bzw. einen Kontinuumslimes)
   auswaehlt.
2. **CONE:** Eine einzige quadratische Form (eine Metrik), die alle Spezies regiert;
   gemeinsamer Kegel nur bei gemeinsamem masselosen Sektor.
3. **T4:** Ein quellenabgeleiteter Grund fuer das spezifische `c`/Fluss-Paar; drei
   gleichchirale Moden erfordern explizites Tuning.
4. **T7:** Ein tatsaechlicher masseloser Spin-2-Sektor mit Constraints (Eichstruktur)
   aus derselben Quelle.

**Antwort auf Q5:** Nein — aus der einzelnen skalierenden Familie `C16 x (Z/LZ)^d`
entsteht **keine** einzige gemeinsame Welt. Jeder Test fuer sich zeigt, dass die
Familie das jeweilige Phaenomen **reproduzieren** kann, wenn man den Parameter
einspeist, aber **kein** Test wird nativ bestanden: die Dimension wird nicht
ausgewaehlt, der Kegel ist nicht gemeinsam, die drei Familien sind nicht
ausgewaehlt, und der masselose Spin-2 fehlt. Die einzelne Familie ist ein
reproduktiver Rahmen, kein konstruktiver Ursprung.
