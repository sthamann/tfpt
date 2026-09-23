# Ein Wedge-Operator, zwei Darstellungen — mikroskopischer Doppelstern

Stand 2026-09-14. Die Einbettung ist ein Herkunftssatz **innerhalb des vorgegebenen Fockvertrags**, keine frei gewählte Matching-Hamiltonmatrix. Der bereits vorbereitete Vergleich aller 15 SU(4)-Typen ist beendet; keine weitere Modellvergrößerung läuft.

## Was tatsächlich zusammenfällt, was gewählt bleibt

Vermittlerfarbe und antisymmetrische Zweimateriefarbe sind dieselbe SU(4)-Darstellung. Derselbe ursprüngliche Wedge-Vertex erzeugt sowohl die Übergänge zwischen Vermittlerbelegungen als auch den effektiven P⁻-Austausch; ein unabhängiger Transferparameter ist unnötig.

**Nicht identifiziert werden verschiedene physische Matchingzustände.** Ihre Bilder im nackten Materieraum können überlappen, bleiben aber verschiedene direkte Summanden: das Matchinglabel ist ein messbarer Belegungszustand und darf nicht wegquotientiert werden. Gewählt bleiben CAR-Materie, bosonische kantenlokale Sechsermoden, additive lokale Qv, der Graph, t und Δ. Ihre Herkunft aus E8 allein ist hier nicht bewiesen.

## Herkunftssatz mit allen Vorzeichen

Annahme ist exakt das bisherige Wedge-Fockmodell: Materiemoden f_{v,a} erfüllen CAR; Vermittler b_{e,ab}, a<b, sind bosonisch und kantenlokal; Q_v=n_f(v)+Σ_{e∋v}n_b(e)=1. Drift ist ΔΣ_e n_b(e), und der einzige Vertex ist tΣ_e(W_e+W_e†), mit

\[
W_e=\sum_{a<b}b_{e,ab}^{\dagger}
(f_{j,b}f_{i,a}-f_{j,a}f_{i,b}),\qquad e=(i,j).
\]

Nichtnegative Besetzungszahlen und Qv=1 erzwingen genau Matchings M belegter Kanten; dazu ist kein weiterer Hard-core-Satz aus Lie-Wurzeladdition erforderlich. Für einen solchen Summanden gilt

\[
\mathcal H_M\simeq (\wedge^2\mathbb C^4)^{\otimes|M|}
\otimes(\mathbb C^4)^{\otimes(8-2|M|)}.
\]

Definiere W_M=∏_{e∈M}W_e als Abbildung vom Nullvermittlerraum nach H_M. Weil jeder Materieteil fermionisch gerade ist, kommutieren disjunkte Wedges einschließlich ihrer CAR-Vorzeichen. Mit P_M=∏_{e∈M}P_e⁻ gilt

\[
W_M^\dagger W_M=2^{|M|}P_M,\qquad
W_MW_M^\dagger=2^{|M|}I_{\mathcal H_M}.
\]

Somit ist C_M=2^{-|M|/2}W_M† eine Isometrie von H_M auf imP_M. Für zulässiges Hinzufügen einer disjunkten Kante e folgt

\[
C_{M+e}W_e C_M^\dagger
=\sqrt2\,P_{M+e}\big|_{\operatorname{im}P_M}.
\]

Dies ist genau der verwendete Block, multipliziert mit dem ursprünglichen t; die Diagonale ist Δ|M|. Die Konstruktion erhält die Besetzungs- und Fermionvorzeichen, weil C_M aus W_M selbst definiert ist. Eine naive feste Tensorbasis ohne diese Phasen wäre nicht gerechtfertigt. Zwei exakte lokale CAR-Identitäten und 432 Vergleiche der Reihenfolge disjunkter Wedges prüfen dies zusätzlich; ein negativer Zeuge zeigt den Vorzeichenwechsel durch einen besetzten Ort zwischen den Endpunkten.

## Gesicherter numerischer Abgleich, ohne Intervallbehauptung

Der ursprüngliche Siebenkanten-Doppelstern besitzt 25 Matchings: 1,7,13,4 für Vermittlerzahlen 0,1,2,3. Der gesamte Qv=1-Fockraum hat Dimension371200. Sein Singulettblock hat Dimension171; die größten vollständigen Matching-Spechtblöcke haben Dimension714. Es wurden die kleinsten zwei Eigenwerte in allen 15 SU(4)-Typen numerisch ausgewertet; exakte Projektorränge summieren sich mit SU(4)-Multiplizitäten zu371200.

Für Δ=1, t=.05, J=2t²/Δ=.005 ist die notwendige Konvention

\[
H_{\rm eff}/J=H_{\rm nackt}/J-7I,\qquad
e_{\rm vergleich}=E_{\rm mikro}/J+7.
\]

| Größe | Nackte führende Ordnung | Matching-vollständiges Mikromodell, numerisch |
|---|---:|---:|
| Grund, nach +7J und /J | 0.407294979577 | 0.505646405864 |
| Erstes Niveau, gleiche Konvention | 0.729740834932 | 0.816804076901 |
| Globale erste Lücke/J | 0.322445855355 | 0.311157671037 |

Die numerische globale Ordnung bleibt ein einfacher Singulettgrund und ein 15-faches Adjointniveau. Die absoluten Mikroenergien sind E₀/Δ≈−0.032471767970679 und E₁/Δ≈−0.030915979615494. **Die Mikroordnung und Mikroenergien sind keine exakten oder Intervallzertifikate; kleine numerische Residuen ersetzen diese nicht.**

Das Nullvermittlergewicht im Mikrogrund beträgt0.968746984172. Nach Konditionierung darauf beträgt der Quadratüberlapp mit dem nackten Grund0.999987642514: der Materiezustand ist sehr ähnlich, obwohl die skalierte Energie eine sichtbare endliche-Δ-Korrektur besitzt. Der Quadratüberlapp mit ΩΩ beträgt konditioniert0.813149374919 und ohne Konditionierung0.787736004634.

Die Mediatorzahlverteilung lautet ungefähr (0.968746984172,0.030987859042,0.000264809030,0.000000347756). Weglassen der zulässigen Zwei-/Dreivermittlerzweige verändert die Grundenergie von−0.032471767971Δ auf−0.031943159653Δ; sie wurden also nicht stillschweigend abgeschnitten.

`verification.json` enthält69 Guards samt Singulett-Skalierungsscan; `all_sectors.json` enthält16 weitere Sektor-/Dimensionskontrollen. `singlet_matching_matrices.npz` enthält Drift und denselben unveränderten Kopplungsoperator. Ein reproduzierter Importnamenskonflikt der Prüfer wurde nach systematischer Ursachenprüfung durch explizites Laden des ursprünglichen Prüfers unter einem eindeutigen Modulnamen behoben; danach bestanden beide vollständigen Läufe.

Dieser Abschluss identifiziert eine zuvor getrennt behandelte mikroskopische und effektive Kopplung. Er wählt weder den Fockvertrag noch die räumliche Architektur, die Zustandpräparation oder den physikalischen Anfangszustand aus und ist kein zusätzlicher fundamentaler Beweis durch größere Matrizen.
