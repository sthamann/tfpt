# Zwei vollständige nackte TFPT-Zellsterne mit festem Quellenaustausch

Stand: 2026-09-14. **Der gesamte nackte Acht-Ququart-Raum ist spektral geordnet**, ohne 31-Zustände-Bandkompression. Es gibt bei gleich starker ursprünglicher Blatt-Blatt-Brücke einen eindeutigen SU(4)-Singulettgrund und eine positive erste Lücke. Die frühere 31×31-Projektion ist für diesen Grundzustand quantitativ gut, aber weder exakt noch gleichmäßig störungstheoretisch klein.

## 1. Unveränderter Modellvertrag

Vier Ququarts pro ursprünglicher Sternzelle, Zentren 0 und 4, Blätter 1,2,3 bzw. 5,6,7. Eine physische Brücke verbindet **Blatt 1 mit Blatt 5**. Für J>0:

\[
H/J=P^+_{01}+P^+_{02}+P^+_{03}+P^+_{45}+P^+_{46}+P^+_{47}+P^+_{15},
\qquad P^+_{ij}=(I+S_{ij})/2.
\]

Die Brücke hat **λ=J**, nicht einen nachgepassten freien Transferparameter. Dies ist die nackte führende Superaustauschordnung bei denselben t,Δ an allen sieben Kanten, mit J=2t²/Δ. Die mikroskopische Form −JΣP⁻ unterscheidet sich von der hier ausdrücklich verlangten positiven P⁺-Konvention um −7JI; Zustände und Lücke bleiben unverändert.

Zusatzannahmen/Grenzen: ursprüngliche vierörtige Sterngeometrie; identische führende Kopplung; nackte Materiezustände. **Kein 544D-Vermittlerdressing, keine endliche-Δ-Restkontrolle, kein C16-Geometrieersatz, keine thermodynamische oder TOE-Schlussfolgerung.**

## 2. Exakte vollständige Spektralordnung

Schur–Weyl zerlegt (C⁴)^⊗8 in die 15 Youngformen λ⊢8 mit höchstens vier Zeilen. Ihre Spechtblöcke sind höchstens 90-dimensional; die SU(4)-Darstellungen liefern die physikalische Multiplizität. Exakt geprüft:

\[
\sum_\lambda f^\lambda\dim V^{SU(4)}_\lambda=65536.
\]

`checker.py` konstruiert rationale Young-Seminormalmatrizen, prüft sämtliche Coxeterrelationen, bildet alle sieben originalen Transpositionen und berechnet/faktorisiert sämtliche ganzzahligen Charakteristiken von X=2H/J−7I. Exakte Sturmzählungen an vier rationalen Grenzen ergeben auf dem **gesamten** Raum die kumulativen Multiplizitäten **0,1,1,16**.

| Größe | Zertifiziertes Intervall | Physikalische Entartung |
|---|---:|---:|
| E₀/J | (0.407294979576, 0.407294979578) | 1 |
| E₁/J | (0.729740834930, 0.729740834934) | 15 |
| (E₁−E₀)/J | (0.322445855352, 0.322445855358) | — |

Der Grund liegt in λ=(2,2,2,2), dem 14-dimensionalen Spechtblock und SU(4)-Singulett. Die erste Anregung liegt in λ=(3,2,2,1), Spechtmaß 70, SU(4)-Adjointmaß 15. Innerhalb des Spechtblocks ist die erste Wurzel einfach.

Die Grundenergie e=E₀/J ist die kleinste reelle Nullstelle von

\[
8e^5-100e^4+456e^3-924e^2+786e-195=0.
\]

Die vollständige Singulettcharakteristik in x=2e−7 lautet

\[
(x+2)(x^2+4x+1)(x^3+6x^2+5x-2)^2
(x^5+10x^4+18x^3-56x^2-143x-66).
\]

Die Grad-12-Minimalpolynomkoeffizienten des ersten Adjointniveaus sowie alle 15 Sektorfaktorisierungen stehen maschinenlesbar in `verification.json`. Zusätzlich werden die vollen Spuren Tr H und Tr H² gegen direkt aus den ursprünglichen Permutationen berechnete Werte geprüft.

## 3. Exakter Vergleich mit Ω⊗Ω und der bisherigen 31×31-Projektion

Sei Ω das vollständig antisymmetrische Vier-Ququart-Singulett. Sein Produkt bleibt bei zugeschalteter Brücke kein Eigenzustand; sein Erwartungswert beträgt exakt 5J/8. Für den normierten tatsächlichen Grund g gilt:

\[
0.815782914923\leq |\langle\Omega\Omega|g\rangle|^2
\leq0.815782914924.
\]

Diese Schranke ist **algebraisch zertifiziert**, nicht nur ein Eigenvektor-Float. Aus dem rationalen Rang-eins-Projektor wird Tr[PΩΩ(xI−X)⁻¹]=N(x)/D(x) gebildet; das Residuum N(x₀)/D′(x₀) ist das gesuchte Gewicht. Reduktion modulo dem Grundpolynom und rationale Intervall-Hornerauswertung an einer exakt isolierten Wurzel geben die angegebenen Grenzen.

Die lokale 31D-Projektion behält Ω plus alle 30 ersten Sternanregungen bei J/2. Diese Projektoren werden als exakte Polynome der **jeweiligen ursprünglichen Sternoperatoren** gebaut. Der Produktprojektor P hat Rang 961 im ganzen Raum, Rang 5 im Singulett-Spechtblock und Rang 12 im Adjoint-Spechtblock. Für den echten Grund:

\[
0.004116589233\leq \|(I-P)g\|^2
\leq0.004116589234.
\]

Damit sind rund **0.412% Grundleckage** bei λ=J nun tatsächlich kontrolliert. Für die erste Adjointanregung beträgt die Leckage numerisch 0.009252238971066, also rund 0.925%; diese zweite Zustandsgewichtszahl wird nicht als Intervallzertifikat bezeichnet.

| Größe | 31×31-Projektion | Vollständige nackte Rechnung |
|---|---:|---:|
| E₀/J | 5/12 = 0.416666666667 | 0.407294979577 |
| E₁/J | 0.752072946454 | 0.729740834932 |
| Lücke/J | 0.335406279788 | 0.322445855355 |

Die projizierte Grundenergie liegt um 0.009371687090J zu hoch, die erste Energie um 0.022332111523J. Die projizierte Lücke ist um **4.0194%** zu hoch. Der Quadratüberlapp des projizierten mit dem tatsächlichen Grund beträgt numerisch 0.995749000088; für das erste Niveau 0.990738410995.

Die exakte Singulettcharakteristik der Projektion hat die fünf Wurzeln
5/12,13/12,13/12,109/72,7/4. Sie reproduziert damit den früheren 961D-Wert unabhängig von dessen numerischer Basis.

### Keine uniforme Kleinheitsgarantie aus dem kleinen Grundgewicht

`leakage_norm.py` bestimmt über alle 15 Sektoren exakt:

\[
\|(I-P)HP\|/J=\sqrt{1023}/64
\simeq0.499755799741.
\]

Die Schranke wird im Sektor (3,3,1,1) erreicht. Relativ zur lokalen Sternlücke J/2 ist dies √1023/32≈0.99951, also **nicht klein**. Die konkrete niedrige Grundleckage rechtfertigt weder uniforme Dynamikkontrolle auf allen 961 Zuständen noch eine thermodynamische Fortsetzung der Kompression.

## 4. Unabhängige und negative Kontrollen

`controls.py` baut unmittelbar die Permutationsmatrizen in der 2520D-Komputationsbasis mit jeder Farbe genau zweimal. Diese von den Youngkoordinaten unabhängige Rechnung reproduziert E₀, E₁, den Produktvakuumüberlapp und die lokale Projektionsleckage; Eigenvektorresiduen sind kleiner als 10⁻¹⁰.

- Brücke entfernen: Grund 0, erste Lücke J/2.
- Falsches Vorzeichen P⁺→P⁻: Grund 0; der Hauptbefund würde nicht unverändert bestehen bleiben.
- Exakt [H,P]≠0 und [H,PΩΩ]≠0: weder die Kompression noch das Produktvakuum sind ein invarianter Einzustandsersatz.
- Diagnostischer vollständiger Youngscan λ/J=0,0.1,0.25,0.5,1: Lücken ungefähr 0.5,0.486938,0.461029,0.409759,0.322446. **Kein nativer Fit und kein Beweis zwischen Scanpunkten.**

Verifikationsumfang: **483** Hauptguards, **17** exakte uniforme-Leckageguards, **9** unabhängige Kontrollen. Der Hauptprüfer wurde vollständig mit normalem Python und mit `-OO` ausgeführt; die exakten JSON-Zertifikate stimmen bis auf die ausdrücklich ausgeschlossene Laufzeit überein. Siehe `optimized_comparison.json`.

## 5. Reproduktion und erreichte Grenze

Vom Repository aus, jeweils mit `/opt/homebrew/bin/python3`:

```text
experiments/theory-contracts/universalraum-six-new-audit-20260914/full_two_cells/checker.py --exact
experiments/theory-contracts/universalraum-six-new-audit-20260914/full_two_cells/controls.py
experiments/theory-contracts/universalraum-six-new-audit-20260914/full_two_cells/leakage_norm.py
experiments/theory-contracts/universalraum-six-new-audit-20260914/full_two_cells/reproduce.py
```

Erreicht ist der **volle endliche Acht-Ququart-Spektral- und Grundzustandsvergleich** für zwei tatsächliche nackte Sternzellen plus die feste physische Brücke. Dadurch ist die frühere fehlende Aussage über diese konkrete 31D-Projektion ersetzt worden: ihre niedrigen Zustände sind brauchbare Näherungen mit explizit gemessenen bzw. zertifizierten Fehlern; sie ist trotzdem keine uniforme kleine-Störungsreduktion.

Nicht erreicht sind eine aus dieser Zelle hergeleitete unendliche kritische Kette, die mikroskopische 544D-Dressierung, eine C16-Bankarchitektur oder die Schließung von T1–T8.
