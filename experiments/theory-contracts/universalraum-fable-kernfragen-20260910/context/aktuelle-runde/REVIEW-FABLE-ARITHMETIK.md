# Unabhängiger Review: Gibbs, Restklassen, KMS und Transformatoren

10. September 2026. **Die grundlegenden Restklassen-, Überlagerungs- und Fourierformeln sind tragfähig. Mehrere anschließende Identifikationen und Kostenfolgerungen sind jedoch falsch oder stärker als ihre Beweise.** Insbesondere ist die endliche-β-Gleichsetzung mit μ_s zu korrigieren; der native Cap ist durch den Haar-Grenzwert seiner Diagonalmarginale nicht identifiziert.

Gebundener Stand: Fable `PROOF.md`, SHA-256 `3f131a30611f5fd5f482b422d334e0722e5a0d6d083763d7f39c8a4139b5aa90`; `ERGEBNISSE.md`, SHA-256 `3d205c8d81c1a2efc37b6c1d4de21ede2099b024d73295aadd87df7b45598da5`. Beide liegen unverändert als eigene Snapshots im Unterordner `fable-arithmetik-review/`. Der Review betrifft Theoreme 3–6 und ihre Ergebniszusammenfassung; den LL2-Fehler behandelt der separate Review.

## 1. P1: Theorem 5 verwechselt Divisibilitätsmomente und vollständige Restklassenverteilungen

Die angegebenen vier Restklassenformeln für den positiven Zeta-Integer `Pr(X=n)=n⁻ᵝ/ζ(β)` sind korrekt. Nenne seinen profiniten Pushforward ν_β. Die Quellenfamilie μ_β besitzt zusätzlich unabhängige Haar-Einheiten und ist unter Multiplikation mit profiniten Einheiten invariant. Das steht ausdrücklich in **§7.1 des hochgeladenen Universalraum-Berichts** und in `Teilerprozess-F9.md`, §§3–4. Beide Quellen warnen ausdrücklich davor, nur aus gleichen Teilbarkeitsmomenten gleiche Restklassenverteilungen zu folgern.

Ein unmittelbarer Gegenzeuge steht bereits in Fables eigener Formel:

\[
\nu_\beta(1\bmod4)-\nu_\beta(3\bmod4)
=L(\beta,\chi_4)/\zeta(\beta)>0,
\]

während

\[
\mu_{\beta,4}(1)=\mu_{\beta,4}(3)=\tfrac12(1-2^{-\beta}).
\]

Positivität des L-Werts folgt für β>1 schon durch Paarung der Reihe: Jeder Term `(4k+1)⁻ᵝ−(4k+3)⁻ᵝ` ist positiv. Bei β=2 gilt sogar `L(2,χ₄)>8/9` und `ζ(2)<2`; somit ist der Unterschied der beiden ungeraden ν-Massen größer als **4/9**. Es handelt sich nicht um einen Rundungsfehler.

**Exakte Reparatur:** Beide Familien haben dieselben Teilbarkeits- und ggT-Klassenmassen. Ihre vollständigen Verteilungen werden durch Einheitenmittelung verbunden:

\[
\boxed{\mu_\beta=\int_{\widehat{\mathbb Z}^{\times}}u_*\nu_\beta\,du.}
\]

Das Haarmittel ist einheiteninvariant, erhält alle Teilbarkeitsmomente und ist daher nach dem vorhandenen Eindeutigkeitssatz genau μ_β. Die notwendige zusätzliche Symmetrisierung darf nicht weggelassen werden. Dies ist zugleich ein präziser Anschluss an die Symmetriemittelung der Bost–Connes-Zustände, wenn deren volle Algebra und Darstellung zusätzlich festgelegt sind.

## 2. P1/P2: Der kritische Grenzwert braucht Algebra, Topologie und Energiedomäne

**Akzeptiert:** Für jedes feste m konvergieren alle m Restklassenmassen von ν_β gegen 1/m. Ein elementarer Beweis vergleicht die m arithmetischen Progressionssummen: Ihre paarweisen Differenzen bleiben für β nahe eins beschränkt, da Differenzen benachbarter Potenzen durch eine konvergente Reihe der Ordnung `k⁻ᵝ⁻¹` begrenzt werden. Division durch `ζ(β)→∞` lässt die Unterschiede verschwinden; die normierte Summe ist eins. Damit folgt `ν_β⇒Haar` schwach auf dem kompakten profiniten Raum. Auch μ_β hat diesen festen-Modulus-Grenzwert.

**Zu korrigieren:** „uniformly for all moduli“ ist ohne Norm unpräzise und in Totalvariation falsch. Für jedes β>1 gilt

\[
d_{TV}(\nu_\beta,\mathrm{Haar})=1,
\qquad\sup_m d_{TV}(\nu_\beta\bmod m,\mathrm{Unif}_m)=1.
\]

Beweis: ν_β sitzt auf der abzählbaren Menge positiver Integer; Haar gibt dieser Menge Maß null. Für die endlichen Quotienten wähle K mit `Pr(X≤K)>1−ε` und danach `m>K/ε`. Die K betreffenden Restklassen besitzen Haar-Masse `K/m<ε`, aber ν-Masse größer als `1−ε`. Die Distanz ist mindestens `1−2ε`.

**Zusätzliche physische Kostenbedingung:** Für denselben Zustand und die von Fable verwendete elektrische Energie `H_E|n>=(κ/2)n²|n>` ist

\[
\langle H_E\rangle_\beta=
\frac{\kappa}{2\zeta(\beta)}\sum_{n\ge1}n^{2-\beta}.
\]

Dieser Mittelwert ist nur für **β>3** endlich; für jedes `1<β≤3` divergiert er. Der kritische Zeta-Gibbs-Grenzweg ist daher kein Grenzweg mit kontrollierter endlicher elektrischer Energie. Eine beanspruchte physische Realisierung benötigt zusätzlich eine genaue Einschränkung, Skalierung oder andere Zustandskonstruktion. Die Gleichheit der Eigenbasis bezahlt diese Aufgabe nicht.

**Kein gewöhnlicher normierter Gibbsoperator bei β=1:** `Tr(e⁻ᴴˡᵒᵍ)=Σ1/n` divergiert. Der Haar-Grenzzustand auf `C(Ẑ)` bleibt sinnvoll; er ist keine Dichtematrix `n⁻¹/ζ(1)` auf `ℓ²(N)`. Die Bost–Connes-Originalarbeit definiert eine vollständige C*-Algebra, ihre Zeitentwicklung und ihre Darstellungen; auf dieser Grundlage werden Gibbs-/KMS-Zustände und ihre kritische Phase klassifiziert. [Bost–Connes, Proposition 8, Theorem 25 und §7](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf)

**Die Cap-Identität ist damit nicht bewiesen.** Bereits `I₄/4` und `|+₄><+₄|` haben dieselben vier Diagonalmassen, aber für den zyklischen Shift X die verschiedenen Erwartungswerte 0 und 1. Der reine verschränkte Cap hat zudem mehr Korrelationsdaten als eine einzelne Marginale. Ein vollständiger Identifikationssatz benötigt dieselbe Algebra, Zustandskorrelatoren, Dynamik und die konkrete Einbettung. Auf der bloßen Diagonalalgebra wirkt H_log trivial; dort allein unterscheidet die KMS-Bedingung weder Haar von anderen Maßen noch eine besondere Temperatur. Korrekte Überschrift: **„Die festen Restklassenmarginalen haben einen Haar-Grenzwert; der vollständige native Cap/KMS-Anschluss bleibt offen.“**

## 3. Akzeptierte und begrenzte Überlagerungs-/Zeitresultate

Die Basisidentitäten `S_m U=UᵐS_m`, `ES_m=mS_mE`, `S_mS_k=S_mk` und die vier Radix-Cuntz-Relationen folgen direkt aus den Bildlabels und gelten ohne numerischen Cutoff. Das Energieskalieren um m² gilt auf dem deklarierten reinen, ladungsfreien Schleifenflusssektor. Es ist eine Aussage über Ausgangsenergie; keine vollständige Implementierungs- oder thermodynamische Arbeitskostenrechnung. Bei zusätzlichem Flusshintergrund müssen dessen Kreuzterme erhalten bleiben.

Auch `H_E=(κ/2)e^{2H_log}` gilt auf dem ausdrücklich eingeschränkten Nichtnull-Ladungsraum. Sie liefert keine skalare Zeitumparametrisierung: Die Übergänge `1↔2` und `2↔4` haben dieselbe logarithmische Energiedifferenz, aber elektrische Differenzen im Verhältnis 1:4. Der Nullmodus und beim vollen Rotor die beiden Ladungsvorzeichen müssen beim Zustandsvergleich eigens behandelt werden.

Bei `Alg(L,E)=⊕_q M₄(q)` ist die verwendete Vervollständigung zu benennen: Der Hilbertraum zerfällt in Viererfasern; alle beschränkten blockdiagonalen Operatoren bilden das Produkt `∏_q M₄`, nicht die `c₀`-Direktsumme. Eine formale Algebra mit unbeschränktem E benötigt zusätzlich einen gemeinsamen Definitionsbereich. Die konkrete Konjugationsformel und der Kopplungsterm 8QR bleiben hiervon unberührt.

## 4. P1: Theorem 6 überdehnt die Operationsklasse und ihre Kosten

**Akzeptiert:** Für `gcd(a,N)=1` sind U_a unitär, multiplikativ komponierbar und erfüllen exakt `F_NU_aF_N†=U_(a⁻¹)`. Ihre Orbits liefern die genannten Einheitswurzelspektren. Die direkte Shift/Diagonal-Normalform besitzt genau `N/gcd(a−1,N)` verschiedene Verschiebungslabels.

**Expliziter Gegenzeuge zur pauschalen Nichtzugehörigkeit:** Der Übertrag C aus Theorem 3 ist selbst

\[
C=U^4P_0+(I-P_0).
\]

Er hat nur die Verschiebungen 0 und 4 und liegt somit in der von Fable ausdrücklich angegebenen Algebra endlicher Summen `ΣU^k g_k(E)`. Auch das interne L besitzt eine solche Zweitermdarstellung. Unbeschränkte Überlagerungen `n→mn` haben für m>1 dagegen unbeschränkte Verschiebung und liegen nicht in dieser **algebraischen endlichen Normalform**. Für jedes feste endliche N liegt U_a durchaus in der Shift/Diagonal-Algebra. Diese drei Fälle dürfen nicht als eine pauschal ausgeschlossene Operationsklasse zusammengefasst werden.

**Kostenkorrektur:** Die Zahl der Shift-Summanden ist eine Komplexität dieses Darstellungsformats, keine allgemeine Schaltkreis-Untergrenze. Eine einzelne modulare Multiplikation U_a ist von der kontrollierten Exponentiation `|j>|1>→|j>|a^j modN>` zu unterscheiden. Erst letztere verwendet O(log N) kontrollierte Potenz-Multiplikationen bei der üblichen Registergröße. Ihre einzelnen Bit-/Gatekosten, Vorberechnungen und Fourierpräzision sind zusätzlich zu zählen. „Order finding ist daher Shor“ gilt nur nach Bereitstellung des gesamten kohärenten Zugriffsvertrags; klassisches Orbitaufzählen bleibt ebenfalls Order finding.

**Reduktion bedeutet hier zunächst Indexreduktion:** Die formale Abbildung `|n>→|n modN>` ist kein beschränkter Hilbertraumoperator `ℓ²(Z)→C^N`: K verschiedene Basiszustände derselben Restklasse werden auf denselben Zustand addiert; der Normverstärkungsfaktor wächst wie √K. Sie ist daher ohne weiteren Kanal-/Kodierungsvertrag keine physische Isometrie. Die endliche U_a-Identität bleibt als separat konstruierte Permutation korrekt.

Ob ein festes natives H oder ein zulässiges Steuerprotokoll bestimmte Transformationen mit günstigen Kosten erreicht, folgt weder aus einer einzelnen Hamiltonian-Termliste noch aus algebraischer Nichtzugehörigkeit zu einer endlichen Normalform. Algebraische, Norm- und starke Abschlüsse sowie erlaubte Kontrollen müssen dafür festgelegt werden. Ebenso ist „ohne diesen Mechanismus existiert kein anderer Reader“ durch die vorliegenden Beweise nicht gedeckt.

## Beleg- und Kontrollumfang

Die beiden Fable-Snapshots wurden vollständig gelesen. Zusätzlich wurden gezielt §7.1 des vorhandenen PDF-Textextrakts, §§3–4 von `Teilerprozess-F9.md` und die angegebenen Stellen der Bost–Connes-Originalarbeit geprüft. Die Gegenbeispiele und Grenzargumente oben sind analytisch beziehungsweise exakt algebraisch; es wurde kein zusätzlicher numerischer Sweep ausgeführt. NumPy-/mpmath-Stichproben werden nicht als Beweis der allgemeinen Aussagen behandelt. Originaldateien und Forschungsregister wurden nicht verändert.
