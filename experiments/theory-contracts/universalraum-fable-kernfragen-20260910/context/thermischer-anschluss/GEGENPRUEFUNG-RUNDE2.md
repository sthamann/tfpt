# Unabhängige Gegenprüfung: Fable Runde 2

10. September 2026. **Teilweise bestätigt; die globale Parent-Wärmesummenentwicklung und ihre Ausschlussfolgen werden nicht übernommen. Kein Blocker für unseren separat bewiesenen Theta-Transfer oder thermischen Anschluss.** Dieser Review betrifft die unten gehashten ersten Fassungen von `BERICHT.md` und `ABSCHLUSS.md`, nicht einen eventuell späteren Fable-Review der inzwischen zugänglich gemachten thermischen Originaltexte.

## Tragfähiger Kern

Die elektrische Energie 2κn², β=πt/(2κ), der Nullmodusterm, die ganze klassische ξ-Integralidentität und ihre Symmetrie sind richtig. Bei der ausdrücklich verwendeten Definition

    Φ(u)=Σ_n≥1 [2π²n⁴e^(9u/2)−3πn²e^(5u/2)]e^(−πn²e^(2u))

ist der korrigierte Faktor **Ξ(z)=4∫₀∞Φ(u)cos(zu)du** richtig. Analytisch: Mit f(u)=e^(u/2)ψ(e^(2u)) gilt f''−f/4=2Φ und f'(0)=−1/4. Zweifache partielle Integration der ξ-Formel liefert den Faktor vier; er ist nicht nur numerisch motiviert. Die elektrische Spektralzeta ist 2(2κ)^−s ζ(2s), zunächst für Re s>1/2; Re s=1/4 bezeichnet die vermutete Linie der **nichttrivialen** Nullstellen nach Umskalierung.

Die kleinen exakten Ringkontrollen bestätigen μ₂=1/72 und μ₃=57497/1036800 für die geprüften Ladungen. Für jeden fest gewählten endlich unterstützten Schleifenvektor ist die skalare Wärmeentwicklung mit diesen Momenten gerechtfertigt. Dies entspricht genau der engeren Vektoraussage unseres `rh/THETA-TRANSFER.md`.

## 1. Die behauptete Exponentialschranke ist falsch

Aus H≥H_diag−||V|| folgt nicht die angegebene obere Schranke für jeden Diagonaleintrag der Exponentialfunktion. Konkretes Gegenbeispiel bei β=1:

    H_diag=diag(0,4),   V=[[0,1],[1,0]],   ||V||=1.
    <1|e^−H|1>=e^−2[cosh(√5)−(2/√5)sinh(√5)]
                =0.080542165938203916…
    e^−(4−1)    =0.049787068367863943… .

Der strikt positive Unterschied 0.030755097570339973… wurde mit 60-stelliger Arb-Einschließung bestätigt. Dieser Einwand ist ein echtes Gegenbeispiel zum verwendeten Lemma.

**Die Konvergenz von D(β) lässt sich dennoch reparieren:** Der vollständige endliche Parent hat durch die positive Gitterquadratik und die beschränkte Störung eine endliche Wärmespur. Für die orthonormale Schleifenfamilie ist Σ_n<v_n,e^−βH v_n>≤Tr(e^−βH)<∞. Zusammen mit der endlichen elektrischen Spur folgt absolute Summierbarkeit der Differenzen. Es wird dafür keine Exponential-Operatorordnung benötigt.

## 2. Der Austausch der Taylorentwicklung mit der unendlichen Summe ist unbegründet

Fable schreibt einen absoluten O(β⁴)-Rest nach einer unendlichen Schleifensumme und einen gemeinsamen Korrekturfaktor durch relative Ordnung β³. Die pro-Vektor-Momentrechnung liefert keine dafür nötige uniforme Restkontrolle.

Eine zusätzliche gezielte Fraction-Rechnung im selben unveränderten Ringcode ergibt bei n=−2,−1,0,1,2,3 exakt

    μ₄(n)=1658352817/7464960000+n²/720000.

Die quadratische n-Abhängigkeit erklärt sich bereits aus den nach dem ersten Hop linearen elektrischen Energiedifferenzen ±κn. Der Taylorrest ist daher keineswegs ladungsunabhängig. Unter dem elektrischen Gaußgewicht gilt <n²>_β∼1/(4κβ). Der **isolierte** n²-Anteil des vierten Taylorterms hätte somit relative Größe β³/691200, also bereits die Ordnung des im Bericht festgehaltenen dritten Terms. Das ist keine hier neu behauptete vollständige korrigierte Summenasymptotik; es zeigt konkret, weshalb der ausgelassene Rest kontrolliert werden muss. Auch ein konstanter β⁴-Term wird durch die unnormalisierte Spur mit Θ∼β^−1/2 gewichtet.

Status: Die globale Formel in `BERICHT.md`, `ABSCHLUSS.md` und den zurückgegebenen Code-Behauptungstexten ist **nicht bewiesen** und wird nicht als exakte Parentformel übernommen. Die festen Vektormomente bleiben gültig.

## 3. „Nicht modular / keine ξ-Darstellung“ folgt daraus nicht

Ein nichtkonstanter Faktor C(t) allein zerstört die Jacobi-Inversion nicht: Beispielsweise ist C(t)=1+exp(−t−1/t) nichtkonstant und erfüllt C(t)=C(1/t), sodass Θ(t)C(t) dieselbe Gewichtsrelation besitzt. Eine lokale Klein-β-Entwicklung entscheidet ohne zusätzliche globale Kontrolle keine Inversionsrelation. Noch weiter reicht die nicht bewiesene Behauptung, es existiere überhaupt keine ξ-Darstellung der Parent-Rückkehrfunktion.

Tragfähig bleibt: Der feste Vektordefekt schließt die **unveränderte elektrische Antwort auf derselben Einbettung** als exakte volle Parentantwort aus. Genau diesen engeren Schluss verwendet unser Theta-Bericht.

Auch „Θ herausdividieren ist nicht definiert“ ist mathematisch zu stark: Für β>0 ist Θ>0, und nach dem reparierten Konvergenzbeweis existiert Z_loop/Θ. Daraus entsteht jedoch nicht automatisch eine positive physische Antwort oder eine dynamisch hergeleitete ξ-Quelle. D(β) ist ein sauberer relativer Gegenstand, aber nicht der einzig definierbare.

## 4. Numerik und Quellenumfang

Die Teile A/B benutzen gewöhnliches mpmath, endliche Summen und adaptive Quadratur. Sie sind **numerische Kontrollen, keine einschließenden Zertifikate**. Einzelterm-Abschneideangaben ersetzen weder den gesamten unendlichen Tail noch eine Kontrolle des Quadratur- und Rundungsfehlers. Der Spektralzeta-Check setzt sogar denselben `mp.zeta(6)`-Wert in den ergänzten Tail ein; er ist damit keine unabhängige Rekonstruktion dieser Zetaantwort. Die bekannten ersten Nullstellen sind Eingaben der Tests.

Fables `QUELLEN.json` pinnt interne Berichte und Code; es dokumentiert keine Originalstellen für die pauschale Aussage über „Pólyas endliche Approximationen“. Diese Formulierung wird ohne Definition der betreffenden Approximationen und Quellensatz nicht übernommen. Die benötigte Grenze – positiver gerader Kern allein beweist keine reellen Transformationsnullstellen – ist bereits durch unser ausdrückliches Gegenbeispiel abgesichert.

## 5. Zusätzliche Aussagen im ersten ABSCHLUSS.md

Fable erklärt dort ausdrücklich, unseren thermischen Originalbericht noch nicht lesen zu können. Sein Konsistenzkommentar ist somit kein unabhängiger Proofreview dieses Textes.

Die zusätzliche Zwei-Plaquetten-Aussage τ⊗τ mit O(√(βκ)) wird ebenfalls nicht als bereits bewiesenes Ergebnis übernommen. Dafür wären eine gemeinsam definierte ganzzahlige Koordinatenzerlegung, die zugehörigen kommutierenden affinen Operationen und ein uniformer gemeinsamer Fehlerbeweis nötig. Korrelierte hochtemperierte Gaußgewichte faktorisieren nach Skalierung im Allgemeinen nicht; eine mögliche asymptotische Unabhängigkeit fester Restklassen braucht einen eigenen Gitterbeweis. Der behauptete Cap-Zahlenvergleich erfordert außerdem dieselben genau identifizierten Operatoren auf beiden Seiten. Dies ist eine mögliche zusätzliche Konstruktion, keine Widerlegung und kein Bestandteil unseres Einschleifen-Satzes auf A_p.

Beim gesamten physischen Gitter beträgt die elektrische Energieasymptotik d/(2β) mit d=2N+1 unabhängigen Zyklenkoordinaten. „1/(2β) pro Rotor“ darf hier nicht mit 3N unabhängig zählbaren Linkrotoren verwechselt werden.

## Snapshot und Quellenpins

Die gelesenen Fassungen liegen unverändert als Arbeitskopien in `fable-runde2-review-snapshot/`; die Originale wurden nicht geändert.

- `BERICHT.md`: `bc5b5b93a845660c0694a9b995f516251f6e4101921522ba8137fef44ee7b9a1`
- `theta_transfer.py`: `c1cfb68fddb3c36c4069ac07f543cabcd0cf32261a36c22fda702be634fe57d4`
- `QUELLEN.json`: `b47eb4a7459addc927cda6ded80ca3d784774fcc8a035d4a4a62da79170ff4c7`
- `ABSCHLUSS.md`: `f702ef83d7c90c130c5e0b52f9375eecc2fcc639c6d7e61a43d6616afdf88782`
- Gelesener/importierter `fable/cap_dynamics.py`: `f60783fcaedfe34b7de1a54d2f8a720e5229a837f162daf5cc6c72f71802032e`

Umfang der eigenen Rechnung: sechs exakte Ringmomente bis μ₄ und ein eingeschlossenes 2×2-Gegenbeispiel. Kein erneuter Gesamtaudit und kein Überschreiben von Fables Ergebnisdateien.
