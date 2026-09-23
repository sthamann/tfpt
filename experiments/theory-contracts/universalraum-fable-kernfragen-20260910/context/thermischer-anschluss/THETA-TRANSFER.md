# Vom elektrischen Rotor zur vollständigen Riemannfunktion

10. September 2026. Klassischer Theta-/Mellin-Satz, ausdrücklich in der bereits konstruierten neutralen TFPT-Schleife realisiert, mit berechenbarem Gesamtfehler. Kein neuer RH-Beweis und kein Anspruch auf Neuheit der Thetaidentität.

## 1. Genau bezeichnete Quelle

Auf einem endlichen kubischen Torus mit Seitenlänge mindestens fünf sind die Zustände

    J|n> = W^n Ω0,  n ∈ Z,

der gewählten orientierten Plaquette orthonormal und erfüllen die Gaußbedingung. Ω0 hat einen Low-Fermionmodus pro Ort und keinen High-Fermionmodus. W addiert die geschlossene Flusskette p mit ||p||²=4. Deshalb ist

    J* H_el J = 2κ E²,   E|n>=n|n>,   κ=1/100.

Die volle Hilbertraumspur des gesamten Gitters wird hier nicht eingesetzt. Wir verwenden die Spur des elektrischen Operators auf dieser gewählten Schleifenfamilie. Aus β=πt/(2κ) folgt exakt

    Θ(t) = Tr_loop exp[−β H_el] = Σ_{n∈Z} exp(−πt n²),  t>0.

Der Materie-Onsitewert εN wird bei einer Kompression des vollen Parents als ausdrücklich bekannte Konstante abgezogen. Dies ist eine Energieverschiebung und noch kein Abschalten der Übergänge nach außerhalb der Schleifenfamilie.

## 2. Vollständiger analytischer Transfer

Setze ψ(t)=(Θ(t)−1)/2=Σ_{n≥1}exp(−πn²t). Die Poissonformel für den Gaußkern liefert

    Θ(t)=t^(−1/2) Θ(1/t).

Für Re s>1 erlaubt absolute Konvergenz den Termtausch:

    ∫_0^∞ ψ(t)t^(s/2−1)dt = π^(−s/2) Γ(s/2) ζ(s).

Zerlege bei t=1, setze im unteren Integral t=1/u und benutze Poisson. Der elementare Nullmodusterm ergibt

    ∫_0^1 [(t^(−1/2)−1)/2] t^(s/2−1)dt
      = 1/(s−1)−1/s = 1/[s(s−1)].

Somit ist

    ξ(s) = 1/2 + s(s−1)/2 · ∫_1^∞
                  [t^(s/2)+t^((1−s)/2)] ψ(t) dt/t.             (1)

Auf jeder kompakten Teilmenge der komplexen s-Ebene wird der Integrand einschließlich jeder s-Ableitung durch eine integrierbare Funktion mit exponentiellem Abfall dominiert. Daher definiert (1) eine ganze Funktion. Im anfänglichen Halbraum stimmt sie mit

    ξ(s)=s(s−1)π^(−s/2)Γ(s/2)ζ(s)/2

überein. Identitätssatz und (1) geben ξ(s)=ξ(1−s) und ξ(0)=ξ(1)=1/2. Gammafaktor und beide meromorphen Polbeiträge sind mitgeführt. Im Halbplan Re s>1 besitzt ζ außerdem das klassische Eulerprodukt; dessen Zerlegung in Primzahlen ist mit derselben Funktion verbunden, kein zusätzlich angenommenes Nullstellenspektrum.

Dies ist die klassische Formel NIST DLMF 25.5.13–14, kombiniert mit 25.4.4 und 20.7.32. Das Neue dieser Untersuchung ist die kontrollierte Zuordnung zur angegebenen elektrischen TFPT-Schleife und die Begrenzung der daraus zulässigen dynamischen Folgerung.

## 3. Endlicher berechenbarer Fehlervertrag auf der ganzen s-Ebene

Für a∈C, x>0 definiere

    I(a,x)=∫_1^∞ t^(a−1)e^(−xt)dt = x^(−a) Γ(a,x).

Das Integral ist ganz in a. Die obere unvollständige Gammafunktion an x>0 kann durch einschließende komplexe Intervallrechnung ausgewertet werden; keine Nullstellen- oder Primzahltabelle ist Eingabe.

Mit den ersten M positiven Flussenergien berechne

    ξ_M(s)=1/2+s(s−1)/2 Σ_{n=1}^M
                    [I(s/2,πn²)+I((1−s)/2,πn²)].             (2)

Wähle eine nichtnegative Zahl q≥max(Re(s)/2−1,(1−Re(s))/2−1) und M mit π(M+1)²>q. Da log t≤t−1 für t≥1, ist jeder der beiden Beträge eines n-Terms im Integral höchstens

    exp(−πn²)/(πn²−q).

Für n=M+1+j gilt n²≥(M+1)²+(2M+3)j. Deshalb folgt der vollständige analytische Rest

    |ξ(s)−ξ_M(s)| ≤ |s(s−1)| exp[−π(M+1)²]
       / {(π(M+1)²−q)[1−exp(−π(2M+3))]}.                  (3)

Die Schranke deckt alle ausgelassenen Flüsse und die gesamte Integrationshalbgerade ab. Für kompakte s-Mengen können q und |s(s−1)| gleichmäßig nach oben beschränkt werden. Einschließende FLINT-Arb-Auswertung von (2) plus ein komplexes Fehlerquadrat mit Radius (3) ergibt eine vollständige numerische Einschließung, einschließlich Rundung. Eine unzureichende Präzision wird als Fehlschlag ausgegeben und nicht als Vorzeichenbeweis behandelt.

Für jedes feste s und jede positive absolute Fehlervorgabe reicht ein endliches M. Aus (3) folgt für die Zahl expliziter Energiekomponenten grob M=O(sqrt(log(1/ε)+log(1+|s|))) auf einem festen Realteilstreifen. Das ist keine vollständige Bitlaufzeitanalyse: die Arbeit und Genauigkeit der unvollständigen Gammaauswertung, große Höhen und Auslöschung werden zusätzlich bezahlt. Bekannte schnelle Zetaverfahren werden damit nicht überboten.

## 4. Warum die vollständige Parent-Dynamik nicht dieselbe Wärmespur hat

Für den gegebenen Parent H, h=J*HJ=εN+2κE² und Γ=(1−JJ*)HJ gilt auf endlich unterstützten Schleifenvektoren

    Γ*Γ=(N/96)I,
    J*H²J−h²=Γ*Γ=(N/96)I.                               (4)

Die erste Gleichheit folgt aus den 6N gerichteten Low–High-Ausgängen mit Betrag b=1/24: 6Nb²=N/96. Die verschiedenen Ausgänge sind orthogonal; elektrische Energie und Low–Low-Hops liefern im All-low-Flussbasiscode keinen weiteren Ausgang. Es ist derselbe bereits unabhängig geprüfte physische Austritt aus dem vorangegangenen Wilson-Beweis, nun für den ganzen einzelnen Schleifensektor.

Für jeden endlich unterstützten normierten ψ gilt daher, mit rechtsseitigem β→0,

    <Jψ,e^(−βH)Jψ> − <ψ,e^(−βh)ψ>
       = β² N/192 + o(β²).                               (5)

Der Parent ist nach unten beschränkt, und diese Vektoren liegen im Bereich jeder Potenz von H, sodass die zweiten Ableitungen der skalaren Wärmeantwort gerechtfertigt sind. (5) ist eine Aussage pro Vektor; wir tauschen sie nicht unkontrolliert mit einer unendlichen Spur oder dem Mellinintegral.

Eine gemeinsame konstante Energieverschiebung lässt (4) unverändert. Insbesondere schließt (4) jeden exakten zeitverflechtenden Ersatzoperator auf dieser selben Einbettung J aus: Ein solcher müsste wegen der ersten Ableitung h sein, widerspräche dann aber der zweiten Ableitung. Größere Räume, echte Selbstenergien und kontrollierte Approximationen werden dadurch nicht ausgeschlossen.

Ein frei subtrahierter Rest kann (1) formal zurückgewinnen, ist aber keine hergeleitete positive physische Antwort. Der neue endliche Dynamikalgorithmus des Teamkollegen rechnet die tatsächlichen Austritte mit; er beweist keine automatische Erhaltung der Thetaidentität unter der vollständigen Materiekopplung.

## 5. Exakte Grenze gegenüber RH

RH fordert die Lage **aller** Nullstellen von ξ. Der positive elektrische Operator hat Eigenwerte 2κn². Die Nullstellen der Mellintransformierten sind nicht diese Eigenwerte. Selbstadjungiertheit dieses Operators entscheidet ihre Lage daher nicht.

Auch Positivität, Symmetrie und schneller Abfall eines Fourierkerns reichen allein nicht. Beispielsweise besitzt der strikt positive gerade Schwartz-Kern

    k(x)=2g_σ(x)+(g_σ(x−1)+g_σ(x+1))/2,
    g_σ(x)=exp(−x²/(2σ²))/(sqrt(2π)σ)

die ganze Fouriertransformierte

    F(z)=exp(−σ²z²/2)(2+cos z).

Diese hat die ausdrücklich nichtreellen Nullstellen z=(2j+1)π±i arcosh(2). Dieses Gegenbeispiel widerlegt nur den allgemeinen Schluss „positiver gerader Gaußkern ⇒ ausschließlich reelle Nullstellen“, nicht RH oder eine spezielle Eigenschaft des Riemannkerns.

Ein RH-Abschluss benötigt eine zusätzliche, unabhängig bewiesene Eigenschaft des **genau richtigen** ξ-Kerns oder eine exakt identifizierte selbstadjungierte Nullstellendarstellung. Die alte globale signierte Weil-Positivität bleibt ebenfalls eine gültige offene Route. Kein positives endlichdimensionales Testergebnis ersetzt diesen Satz.

## 6. Vorarbeiten und Unterschied

- `rh/catalog/analysis/positivity_origin_search.md`, P2–P3, beschreibt bereits Theta-/Mellinobjekte und die Trennung zwischen Wärmespektrum und Nullstellen. Die dort betrachtete E8-Spur ist nicht die hier ausdrücklich gewählte Rang-eins-Schleifenspur. Beide unterliegen derselben Beweisgrenze.
- `rh_theta_stability_compiler_20260908/README.md` dokumentiert konkrete gescheiterte hinreichende Kriterien und zulässige engere Möglichkeiten. Es wird kein ausgeschlossenes universelles Dilation-/Multiplikatorkriterium neu angenommen.
- Die Graphpfade zum Hilbert–Pólya-Operator enthalten heuristische Kanten und offene Identifikationen. Sie werden nicht als Beweise verwendet.
- Gegenüber `r647` wird kein Rang-acht-Schalenzähler als billiger Faktorisierer ausgegeben; gegenüber `r638` wird keine lokale positive Form mit der globalen signierten Weilform gleichgesetzt. Die neue Leistung ist ein ausgeführter, kostenbezeichneter klassischer Transfer und sein präziser Parent-Defekt, keine Wiederbelebung einer getöteten RH-Route.

Primär-/Standardquellen: https://dlmf.nist.gov/25.5#E13, https://dlmf.nist.gov/25.4#E4, https://dlmf.nist.gov/20.7#E32; einschließende Funktionsauswertung: https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.gamma_upper.
