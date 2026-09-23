# Unabhängiger Review: LL-Zweilinkterm und Exaktheitsstatus

10. September 2026. **Der gemeldete Implementierungsfehler ist unabhängig exakt bestätigt.** Der aktuelle Zweilinkterm implementiert einen besetzungsabhängigen Vielteilchenoperator anstelle des direkten Bilinears aus dem ursprünglichen Einteilchenkern. Die nackte All-low-Leak-Aussage bleibt unter dieser Korrektur unverändert; die bereits ausgegebenen Dressing-Residualwerte ändern sich tatsächlich.

Geprüfter Stand von `experiments/theory-contracts/universalraum-fable-kernfragen-20260910/fable/checks.py`:

`a92ba954452f1397c364da1da6e7243d5ec5dff5fead0e5548f14f96becc8e6a`

Die Quelle blieb während dieses Reviews bytegleich. Es wurde keine Fable-Datei verändert.

## 1. P1: `apply_H`, Zeilen 111–117, verwechselt zwei verschiedene Operatoren

Die Originalquelle `experiments/theory-contracts/det-wall-hh-rule/PROOF.md`, Abschnitte 0–1, definiert den LL-Einteilchenblock als `A+λg²A²`. Die Zweilinkkomponente eines Pfades `x→y→z` wird daher nach zweiter Quantisierung zum direkten Endpunktbilinear

\[
c\,l_z^\dagger U_{yz}U_{xy}l_x.
\]

Fables zwei aufeinanderfolgende Aufrufe von `hop` führen dagegen erst `l_y†l_x`, dann `l_z†l_y` aus. Für verschiedene x,y,z ist ihr Produkt

\[
l_z^\dagger l_y l_y^\dagger l_x
=l_z^\dagger(1-n_y)l_x.
\]

Es enthält einen zusätzlichen Pauli-Blocker am Zwischenort. Der korrekte Einteilchenkern transportiert den Endpunktmodus direkt und benötigt keine freie Zwischenbesetzung. Die Rotoroperatoren verändern auf beiden Wegen die zwei Linkflüsse; sie beseitigen diesen CAR-Unterschied nicht.

**Vollständiger rationaler Gegenzeuge:** Viererring, Lowmaske `0b1011`, Highteil `1<<6`, Gesamtmaske **75**, Flux `(0,0,0,0)`, Pfad `0→1→2`.

- Anfang und korrekter Endzustand erfüllen beide die implementierte Gaußbedingung.
- Der erste aktuelle Hop wird durch das belegte Low-Orbital 1 blockiert.
- Das direkte Bilinear annihiliert Low 0 und erzeugt Low 2; es liefert Gesamtmaske **78** und Flux **(1,1,0,0)**.
- Mit der implementierten Jordan-Wigner-Konvention ist die Amplitude exakt **−1/576**. Im aktuellen vollständigen `apply_H` ist die Amplitude dieses Zielzustands **0**.

Die notwendige Korrektur ist daher: eine Low-Annihilation nur an x, eine Low-Erzeugung nur an z und beide Linkverschiebungen entlang des Pfades. Kein temporäres Erzeugen oder Vernichten eines Fermions an y. Die beiden Ringpfade zu demselben gegenüberliegenden Endpunkt besitzen verschiedene Fluxänderungen und müssen separat erhalten bleiben.

Die Onsitekonstante wurde für diesen Review nicht verändert. Die Originalquelle erklärt ausdrücklich die beibehaltene Umgebungskoordinationszahl sechs gegenüber zwei Rückläufen des Viererrings; das ist ein separater, deklarierter Modellentscheid.

## 2. Tatsächlich betroffene Resultate

Eine unabhängige Korrektur **nur im Speicher** ersetzt ausschließlich die nicht zurücklaufenden LL-Zweilinkterme. Alle übrigen Koeffizienten, Zustände und Dressingformeln bleiben gleich.

Auf jedem der vier ursprünglichen All-low-Fluxcodezustände stimmen altes und korrigiertes `H|J_a>` exakt überein: Jeder Low-Endpunkt ist dort schon belegt. Daher bleiben das nackte Leck **1/72**, der komprimierte Generator und die daraus gebaute erste Dressingstufe unverändert. Auch das Beimischungsgewicht bleibt gleich.

`H` wirkt danach jedoch auf die gemischten Low/High-Zustände des Dressings. Deshalb muss dessen Residualleck neu berechnet werden. Schon der erste Diagonalwert ändert sich exakt von

\[
\frac{2530540647500}{76160383064493849}
\quad\text{auf}\quad
\frac{1026808008239051162932690061875}
{30908197644274121699004267184252848}.
\]

Das entspricht `3.322646953281599·10⁻⁵ → 3.322121917481888·10⁻⁵`. Die Reduktion um mehr als den Faktor 100 besteht in dieser überprüften Korrektur weiter; ihr erster Faktor wird ungefähr **418.0728** statt **418.0068**. Alle vier Residualdiagonalen ändern sich. Berichte und etwaige Residualzerlegungen müssen daher aus dem korrigierten Operator regeneriert werden; eine unveränderte Zahl ist hier keine zulässige Übernahme.

## 3. P2: Das gesamte Skript ist nicht „all finite/exact“

Der Eingangstext und `record()` bezeichnen den Gesamtlauf als exakt. Das trifft nicht auf alle Kontrollen zu:

- `coverings()` verwendet NumPy-Gleitkommamatrizen, `sqrt` und `np.allclose` auf ausgewählten Innenbereichen.
- `gibbs_residues()` verwendet 30-stellige mpmath-Arithmetik, `nsum` und Fehlertoleranzen. Sechs endliche β-Werte sind kein numerischer Beweis des Grenzwerts β→1⁺.
- `modular_covering()` prüft eine numerische komplexe DFT und numerisch berechnete Eigenwerte mit `np.allclose`.

Diese Kontrollen können die getrennt ausgeschriebenen algebraischen oder analytischen Beweise unterstützen. Sie sind weder rationale Exaktkontrollen noch automatisch rigorose Intervallzertifikate. Der Ergebnisstatus sollte die exakten diskreten/CAR-Kontrollen, numerischen Stichproben und schriftlichen allgemeinen Beweise getrennt kennzeichnen.

## Reproduktion und Scope

`check_fable_ll2_review.py` extrahiert ausschließlich die benötigten Funktionsdefinitionen und rationalen Konstanten aus dem SHA-256-geprüften Snapshot `fable-ll2-reviewed-source.py`. Dieser hält den geprüften Stand auch nach einer späteren Korrektur in Cursor reproduzierbar fest. Der Prüfer führt weder Fables vollständiges `record()` noch dessen NumPy-/mpmath-Teile aus. Die ursprünglichen Dateien werden nur gelesen; der korrigierte Operator existiert ausschließlich im eigenen Prozessspeicher.

**14 exakte Kontrollen bestanden.** `fable-ll2-review-checks.json` enthält den Quellhash, den expliziten Gegenzeugen sowie sämtliche alten und korrigierten Leckwerte. Dies ist ein enger Implementierungsreview, keine unabhängige Prüfung sämtlicher Behauptungen in Fables Bericht.
