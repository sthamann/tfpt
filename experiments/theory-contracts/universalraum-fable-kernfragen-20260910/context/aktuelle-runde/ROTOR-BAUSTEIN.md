# Ein konkreter gemeinsamer Baustein: Rotor, Überträge, Überlagerungen

10. September 2026. Konstruktion und begrenzter Herkunftsnachweis für den vorhandenen kompakten U(1)-Rotor/CAR-Gitterparent. Kein Anspruch, damit den gesamten TFPT-Compiler, seine physische Zustandsauswahl, die Gravitation oder RH hergeleitet zu haben.

**Ergebnis:** Die vollständige originale Rotor-Dynamik lässt sich exakt in Viererzustände und mitgeführte ganzzahlige Überträge übersetzen. Die Kreisüberlagerungen liefern zugleich einen konkreten multiplikativen Bausteinkasten. Nimmt man dessen additive Operation und eine ausdrücklich bezeichnete thermische Gleichgewichtsbedingung hinzu, werden die logarithmischen Primzahlgewichte erzwungen. Diese arithmetische Gleichgewichtsdynamik ist jedoch nicht die bereits vorhandene elektrische TFPT-Zeit. Die Unterscheidung lässt sich an expliziten Operationen beweisen.

## 1. Genau bezeichnete Quelle und frühere Ergebnisse

Die nativen Dateien `ground-state-loop-response/README.md` §1 und `observable-dynamics/README.md` §§1–2 verwenden den vollen elektrischen Raum, keinen endlichen Flux-Cutoff:

\[
\mathcal H_{\mathrm{rot}}=\ell^2(\mathbb Z),\quad E|n\rangle=n|n\rangle,
\quad U|n\rangle=|n+1\rangle.
\]

Auf einem endlichen kubischen Torus lautet die elektrische Energie \(H_E=(\kappa/2)\sum_e E_e^2\), \(\kappa=1/100\). Der vollständige Materieparent ist

\[
H_m=l^*(aA_U+\beta a^2A_U^2)l+M d^*d
 +b(d^*A_Ul+l^*A_Ud),
\quad(a,\beta,b,M)=(1/12,1/4,1/24,4).
\]

Die örtliche Rotoralgebra enthält ausdrücklich alle beschränkten Operatoren auf den örtlichen Rotoren. Die folgenden beschränkten Karten gehören deshalb zur angegebenen großen Algebra; Zugehörigkeit zu einer kleineren Weyl-C*-Algebra wird nicht behauptet. Beschränkte Operatorzugehörigkeit beweist noch keine billige Präparation oder physische Steuerbarkeit.

Der Bericht `round17_delta_audit.md` vom 6. September hatte bereits vollständige skalare Rotorüberlagerungen für U(1)^8, ihren Gauss-Transport, den Energie-Skalierungsfaktor n² und den Unterschied zur logarithmischen Zeit bewiesen. Das ist wiederverwendete Vorarbeit. Seine kinematischen Grade n^(8M) und physischen Gitterindizes n^8 dürfen nicht zu n umbenannt werden. Neu ausgearbeitet werden hier der vollständige Radixtransport, die konkrete verlorene Uhrantwort und der Anschluss an die additive Überlagerungsalgebra mit ihrer Zustandsbedingung.

## 2. Verlustfreier Radixtransport auf dem ungeschnittenen Raum

Für jede feste Basis \(b\ge2\) besitzt jedes \(n\in\mathbb Z\) genau eine Darstellung \(n=bq+r\), \(q\in\mathbb Z\), \(0\le r<b\). Daher ist

\[
V_b|bq+r\rangle=|q\rangle\otimes|r\rangle
\]

unitär und surjektiv. Es wird kein Freiheitsgrad angehängt: Beide Seiten enthalten exakt dieselben Originalzustände.

Seien \(Q|q\rangle=q|q\rangle\), \(R|r\rangle=r|r\rangle\), \(B|q\rangle=|q+1\rangle\). Dann gelten

\[
V_bEV_b^*=bQ\otimes I+I\otimes R,
\]
\[
V_bUV_b^*=I\otimes\sum_{r=0}^{b-2}|r+1\rangle\langle r|
 +B\otimes|0\rangle\langle b-1|. \tag{1}
\]

Der letzte Summand ist der genaue Übertrag. Insbesondere ist die b-te Potenz von (1) \(B\otimes I\), nicht die Identität. Für jedes positive m ist die skalare Überlagerungsisometrie \(S_m|n\rangle=|mn\rangle\) in denselben Koordinaten

\[
V_bS_mV_b^*|q,r\rangle
=|mq+\lfloor mr/b\rfloor,\;mr\bmod b\rangle. \tag{2}
\]

Beide Identitäten folgen auf jedem Basisvektor; beschränkte Operatoren sind damit auf dem ganzen Raum gleich. Für E und E² gilt die Gleichheit einschließlich der Definitionsbereiche, weil die quadratisch summierbaren gewichteten Fourierkoeffizienten durch die bijektive Umindizierung unverändert sind.

Für b=4 ist \(Z=e^{i\pi E/2}\). Mit \(P_3\) als seiner Projektion auf den Rest 3 definiert

\[
L=U(I-P_3)+U^{-3}P_3
\]

den internen endlichen Verschieber: \(V_4LV_4^*=I\otimes L_4\), \(L_4|r\rangle=|r+1\bmod4\rangle\). Somit \(L^4=I\) und \(ZL=iLZ\). L ist eine andere tatsächliche Operation als U; die zusätzliche Rückwicklung um drei darf nicht verschwiegen werden.

## 3. Der gesamte gegebene Gitterparent wird exakt übertragen

Wende \(V_4\) auf jeden der endlich vielen Links an und die Identität auf die bereits vorhandene CAR-Fockkomponente. Das Produkt \(\mathcal V\) ist unitär. Ersetze in jeder ursprünglichen Hamiltonoperation U durch (1) und E durch \(4Q+R\). Insbesondere

\[
\mathcal V H_E\mathcal V^*
=\frac\kappa2\sum_e(16Q_e^2+8Q_eR_e+R_e^2). \tag{3}
\]

Alle ursprünglichen ein- und zweischrittigen Materiehops behalten ihre Reihenfolge, ihre CAR-Zeichen und ihre genauen Koeffizienten. Die Gaussoperatoren werden mit derselben Substitution übertragen: Der Flussanteil wird \(4\operatorname{div}Q+\operatorname{div}R\), die ursprüngliche Materieladung bleibt erhalten. Deshalb sind die beiden Register im physischen Gaussraum nicht frei voneinander wählbar.

Für \(H'=\mathcal V H\mathcal V^*\), \(\operatorname{Dom}H'=\mathcal V\operatorname{Dom}H\), gilt durch den Spektralsatz

\[
e^{-itH'}\mathcal V=\mathcal V e^{-itH}.
\]

Mit \(\rho'=\mathcal V\rho\mathcal V^*\) und \(O'=\mathcal V O\mathcal V^*\) stimmen alle Erwartungswerte beschränkter Observablen und alle endlichen zeitgeordneten Folgen beschränkter Operationen genau überein. Unbeschränkte Ausdrücke erfordern die transportierten Definitionsbereiche und die Existenz der betreffenden Erwartungswerte. Für algebraische Zustände benutzt man entsprechend den Zustandsrückzug. Dies ist der **vollständige Darstellungswechsel des bereits gegebenen Gitterparents**, einschließlich seiner Eingriffe und seines Zustands. Er ist kein Beweis, dass der Parent aus P1/P2 folgt.

Örtliche Produkte dieser Umindizierungen sind mit Volumeneinbettungen kompatibel und erhalten die Grade der CAR-Algebra. Die konjugierte endliche Dynamik hat damit denselben bereits bewiesenen örtlichen Volumengrenzwert. Die ursprüngliche fehlende Punkt-Norm-Stetigkeit auf der großen Rotoralgebra wird durch eine isometrische Algebraabbildung nicht beseitigt. Eine unendliche Tensorprodukt-Vakuumdarstellung wird dafür nicht zusätzlich postuliert.

## 4. Warum das Weglassen der Überträge wirklich falsche Antworten erzeugt

Schon die elektrische Ein-Link-Energie \(cE^2\), \(c>0\), genügt. Wähle die zwei Originalzustände

\[
|\psi_q\rangle=\frac{|4q\rangle+|4q+1\rangle}{\sqrt2},\quad q=0,1.
\]

Nach Wegspuren des q-Registers sehen beide zunächst wie \((|0\rangle+|1\rangle)/\sqrt2\) aus. Unter der elektrischen Zeit erhält die relative Phase jedoch die Frequenz \(c(8q+1)\). Bei \(t=\pi/(8c)\) unterscheiden sich die beiden relativen Phasen exakt um π. Die reduzierten Viererzustände sind dann orthogonal. Eine Rechnung, die nur den anfangs identischen Viererzustand behält, kann beide Ausgänge nicht richtig vorhersagen.

Das ist ein exakter Gegenbeweis gegen die geschlossene Viererreduktion, kein Gegenbeweis gegen (1)–(3), die gerade alle Überträge bewahren. Der ergänzende Wilson/CAR-Bericht konstruiert den gaugeinvarianten Cap in den tatsächlichen Feldern und zeigt zusätzlich die wirklichen Materieübergänge aus seinem endlichen Unterraum.

## 5. Kreisüberlagerungen, Primzahlen und die endliche Faser

Jeder stetige Gruppenhomomorphismus \(f:U(1)\to U(1)\) besitzt die Form \(f(z)=z^m\), \(m\in\mathbb Z\). Ein direkter Beweis: Hebe \(f(e^{it})\) zu \(e^{ig(t)}\) mit stetigem g und g(0)=0. Der Homomorphismus erzwingt, dass \(g(t+s)-g(t)-g(s)\) stetig und in \(2\pi\mathbb Z\) liegt, also null ist. Stetige Additivität liefert g(t)=ct, und 2π-Periodizität erzwingt \(c=m\in\mathbb Z\). Die positiv orientierten endlichen Selbstüberlagerungen haben genau m≥1.

Ihre Komposition ist \(f_mf_n=f_{mn}\). Eine nichttriviale solche Überlagerung ist genau dann nicht in zwei nichttriviale solche Überlagerungen zerlegbar, wenn ihr Grad eine Primzahl ist. Dies verwendet die gewöhnliche Primzahldefinition in dem nun geometrisch realisierten Gradmonoid. Es ist keine neue Aussage über die Verteilung der Primzahlen.

Die vierfache Überlagerung hat Deckgruppe Z4. Auf dem Fourierraum wird sie durch S4 dargestellt. Ihre vier Zweige

\[
T_r=U^rS_4,\quad 0\le r<4
\]

erfüllen \(T_r^*T_s=\delta_{rs}I\) und \(\sum_rT_rT_r^*=I\), weil ihre Bilder genau die vier Restklassen sind. Außerdem \(V_4^*(|q\rangle\otimes|r\rangle)=T_r|q\rangle\). Die Matrixeinheiten \(T_rT_s^*\) bilden genau die interne M4-Algebra. Damit sind Rotor-Radix, endliche Matrixoperationen und Überlagerung explizit verbunden.

Diese Algebra ist ein bekannter Baustein der von Cuntz untersuchten ax+b-Algebra. Der vorliegende Bericht beansprucht keine Neuheit dieser Algebra. Der neue taskbezogene Anteil ist ihre genaue Umsetzung samt elektrischen Überträgen im festgehaltenen TFPT-Modell und der Abgleich mit dessen offenen Quellenverträgen. [Cuntz, Definition 3.1 und die kanonische Darstellung nach Theorem 3.4](https://arxiv.org/pdf/math/0611541)

## 6. Eine konstruktive Auswahl der Logarithmusgewichte — mit expliziter neuer Voraussetzung

Bezeichne \(P_m=S_mS_m^*\). Der vollständige additive Überlagerungsbaukasten erfüllt

\[
S_mS_n=S_{mn},\quad S_mU=U^mS_m,\quad
\sum_{r=0}^{m-1}U^rP_mU^{-r}=I. \tag{4}
\]

Nehme eine Punkt-Norm-stetige Automorphismengruppe an mit
\(\lambda_t(U)=U\), \(\lambda_t(S_m)=e^{it\varepsilon_m}S_m\), und einen β-KMS-Zustand ω, β>0. Diese Annahmen sind zusätzliche mathematische Auswahlbedingungen, keine bereits hergeleiteten physischen TFPT-Eigenschaften.

Die S_m sind analytische Elemente. KMS ergibt

\[
\omega(P_m)=\omega(S_m^*\lambda_{i\beta}(S_m))
=e^{-\beta\varepsilon_m}.
\]

Da U von der Zeit fixiert wird, liegt es im Zentralisator des KMS-Zustands. Alle m Summanden von (4) haben dasselbe Gewicht. Also

\[
1=m e^{-\beta\varepsilon_m},\qquad
\boxed{\varepsilon_m=\frac{\log m}{\beta}.} \tag{5}
\]

Hier erzwingen die vollständige additive Restklassenstruktur und KMS die logarithmischen Gewichte. Eine gesonderte gewöhnliche Ordnungsmonotonie wird in diesem Satz nicht gebraucht. Für die normierte Zeit \(\varepsilon_m=\log m\) ist β=1 erzwungen. Ein entsprechender 1-KMS-Zustand existiert in der bekannten Cuntz-Algebra (Proposition 4.2); dessen Existenz wird als Literaturresultat verwendet, die notwendige Gleichung (5) wurde oben vollständig bewiesen.

Der Zustand ist auf der von den 16 Matrixeinheiten T_rT_s* erzeugten M4-Algebra die normierte Spur: Die Zeit fixiert diese Algebra, KMS ist dort eine Spur, und die normierte Matrixspur ist eindeutig. Deren Einschränkung auf den diagonalen oder zyklischen vierdimensionalen C4-Sektor ist gleichgewichtet. Die volle 16-dimensionale Matrixalgebra wird damit nicht mit dem ursprünglichen vierdimensionalen Frobeniusobjekt verwechselt. Dadurch ist eine **gleichgewichtete endliche Faser** mit den logarithmischen Gewichten algebraisch kompatibel. Das behebt die im einfacheren ζ-Gibbs-Modell ungleichen Restklassengewichte durch einen ausdrücklich anderen Zustand und eine andere Algebra. Es beweist nicht, dass dieser Zustand der native TFPT-Zustand ist.

Die Behauptungen aus Cuntz werden nur im gelesenen Umfang §§2–4 benutzt. Insbesondere wird die dort typographisch zu weit gefasste Formulierung von Lemma 3.2(c) nicht für gleiche oder nicht teilerfremde Indizes eingesetzt; etwa S_m* S_m=I ist für m>1 nicht S_m S_m*. Unsere Relationen (1)–(5) sind direkt begründet.

## 7. Zwei genaue Gründe, weshalb diese Normzeit noch keine physische TFPT-Zeit ist

**Operatorantwort.** Für den bereits gegebenen elektrischen Ein-Link-Generator \(cE^2\) gilt

\[
e^{itcE^2}S_m e^{-itcE^2}|n\rangle
=e^{itc(m^2-1)n^2}|mn\rangle.
\]

Die Frequenz hängt vom Originalzustand n ab. (5) verlangt dagegen eine von n unabhängige Frequenz. Bereits m=2 und n=1,2 unterscheiden beide Zeitentwicklungen. Ferner wird das echte U unter elektrischer Zeit nicht fixiert. Genau die in §6 verlangte Auswahl passt also nicht zum unveränderten elektrischen Parent.

**Zustand und Darstellung.** Der KMS-Zustand aus §6 kann in der konkreten Rotor-Darstellung auf ℓ²(Z) kein normaler Dichteoperatorzustand sein. Fixiere n∈Z. Die Projektionen \(U^nP_{j!}U^{-n}\) auf die Restklasse n modulo j! fallen stark gegen \(|n\rangle\langle n|\). Ihre Zustandsgewichte sind jedoch \(1/j!\to0\). Ein normaler Dichteoperatorzustand müsste folglich \(\rho_{nn}=0\) für jedes n erfüllen. Das widerspricht \(\operatorname{Tr}\rho=1\). Dieser direkte Beweis benutzt nur die bezeichneten Restklassenprojektionen und normale Monotoniekonvergenz.

Folglich braucht dieser Normzustand eine andere GNS-Realisierung beziehungsweise einen nichtnormalen Grenzzustand. Das ist mathematisch zulässig, ersetzt aber nicht die Herleitung aus dem tatsächlichen TFPT-Vakuum. Auch die Festlegung β=1 ist eine Temperaturnormierung dieser Algebra, keine Riemannsche kritische Linie Re(s)=1/2.

## 8. Was dieser Baustein vollständig leistet

1. Jeder Originalzustand und jede Originaloperation des bezeichneten Rotor/CAR-Gittermodells kann einschließlich Zeit und Gaussbedingungen exakt in Radixform hin- und zurückübersetzt werden.
2. Die Kreisüberlagerungen und ihre endlichen Fasern geben einen ausdrücklich konstruierten gemeinsamen arithmetisch-geometrischen Operationsbaukasten. Die Primzahlen sind dessen unzerlegbare positive Grade.
3. Unter einer genauen KMS-Auswahl werden aus den Restklassenpartitionen die Gewichte log m erzwungen; eine passende gleichgewichtete endliche Faser existiert in der bekannten algebraischen Gleichgewichtsrealisierung.

Was weiterhin nicht daraus folgt: Auswahl des ursprünglichen TFPT-Parents aus dem Compiler, Identität des Normzustands mit dem tatsächlichen physischen Zustand, gravitative Raumzeit, ein vollständiger Weil-/Riemann-Operator oder eine billige Herstellung jedes Faktorreaders. Der nächste dynamische Anschluss muss die nachgewiesenen Materieübergänge aufnehmen und den Zustands- und Zeitwechsel begründen.
