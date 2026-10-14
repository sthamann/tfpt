# Pakettest der Quellenladung gegen die ursprüngliche Träger-/Familienformel

**Originalformel.** `source-boundary-lift-selection-20260922/PROOF.md`, Gl. (1):
`A_W = ρ(A_E)⊗I₄ + I₁₆⊗M_m·tr A_E` mit `β_j = m_j + ½` und `Σ m_j = −2`
(`source-joint-spin-family-lift-20260922`, §4). Die Familie wirkt also **nur über
die Spur** der Trägerverbindung. Ein Trägerkocharakter x ∈ Z⁵ mit Spur t induziert
den Familienanteil `T(β_m)·t` (A3 → D3 über die Isometrie T).

## K1 [E]
`λ_A = (e₃; T β_A) = (0,0,1,0,0; 1,0,0)` mit `m_A = (0,0,−1,−1)` ist eine E8-Wurzel,
und `2λ_A = Q' = 2(e₃+e₆)`. Codex' Ward-Wörterbuch ist damit genau das
Minimalpaket.

## K2 [E] – Ward-Normierung wählt das Paket
Sei der Trägeranteil die **ursprüngliche primitive Clutching-Richtung** e_weak
(Norm 1, Spur 1; Klasse `(c₁(E₃), c₁(E₂)) = (0,1)`). Dann gilt
`|λ_m|² = 1 + Σβ_j² = 2d` mit `d = ½Σm_j²`. Aus `q = k·λ_m` und `|q|² = 8`
folgt `k²·2d = 8`, also `(k,d) ∈ {(2,1), (1,4)}`. `d = 4` hat keine Lösung mit
`Σm = −2`: Vier Quadrate mit Summe 8 sind nur vom Typ (±2,±2,0,0), deren
Summen ±4 oder 0 sind. **Also k = 2 und m = m_A bis auf S4.** Der Checker bestätigt
das durch Aufzählung.

Folge: Das bisher als „Zusatzvertrag" geführte Normminimum `d = 1`
(`source-joint-spin-family-lift`, §4) folgt aus der Ward-Normierung der
tatsächlichen Quellenladung, sofern `q = k·λ_m` mit der ursprünglichen
Clutching-Richtung gilt. Dann ist `q/2 = λ_A` eine Gitterwurzel; das erzwingt die
s-Chiralität und führt zum Ausschluss in `ward-chirality-vacuum-no-go-20261014`.

**Scope.** Lässt man beliebige ganzzahlige Trägerkocharaktere zu, gibt es weitere
Lösungen, z. B. mit Spur 2 und k = 1. K2 hängt also an der ursprünglichen
Clutching-Richtung, nicht nur an der Paketformel.

## K3 [E] – Codex' c-Rahmen-Test bestätigt
`R0 = diag(−1, 1⁷)` bildet `D8+c` auf `D8+s` ab. Das von Codex mit der alten exakten
Matrix M transportierte Bild `(−1,−1,2,0,0; 1,−1,0)` hat Norm 8 und liegt in D8.
Seine Hälfte liegt in keinem E8. Der Trägeranteil ist spurfrei (t = 0); nach der
Paketformel muss der Familienanteil dann für **jedes** m verschwinden. Er ist aber
`(1,−1,0) ≠ 0`. Damit passt das Bild für kein m.

## K4 [E] – welche Familienwirkung zusätzlich nötig wäre
`Tᵀ(1,−1,0) = (0,1,−1,0)`: ein spurfreier A3-Wurzelkocharakter mit ganzzahligen
Einträgen. Er ist zu keinem `β_m` proportional, denn alle β-Einträge sind
halbzahlig. Er liegt in einem SU(3) ⊂ SU(4) (4 → 3+1).

## Originalsuche nach einer unabhängigen Familienwirkung
* `source-boundary-lift-selection-20260922/PROOF.md` nach (1): „Zusätzliche
  unabhängige Familienverbindungen oder Endomorphismusterme werden durch (1)
  nicht automatisch beseitigt" – zugelassen, aber nicht geliefert.
* `origin_theory.tex:1210–1218`: Die Flavor-Monodromie ist SU(3)-wertig auf H₁ mit
  Zentrum Z₃ und parabolischen Gewichten {0, ⅓, ⅔}; SU(3) ⊂ SU(4) über 4 → 3+1.
  Das ist der einzige im Original benannte Kandidat für eine von tr A_E
  unabhängige Familienwirkung. Seine lokalen Exponenten sind Z₃-Brüche, nicht der
  ganzzahlige Kocharakter (0,1,−1,0); eine Ableitung des benötigten Generators
  daraus wurde **nicht** gefunden.
* `tfpt_1_architecture_e8.tex:3510–3517`: Residuennormalform mit Spektrum
  {0, ⅓, ⅔}, unitarisierte Holonomie W(A3) = S4 (diskret). Diskrete Holonomie
  liefert keinen kontinuierlichen Kocharakter.

**Verdict.** Im c-Rahmen müsste eine Familienwirkung mit Kocharakter (0,1,−1,0)
zusätzlich aus der Quelle kommen. Die Originale benennen mit der
SU(3)-Flavormonodromie nur einen Kandidaten, dessen Daten ihn nicht liefern.
