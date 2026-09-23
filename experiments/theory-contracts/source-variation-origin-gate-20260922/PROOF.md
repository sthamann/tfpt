# TFPT: Welche Fluktuationen liefert die ursprüngliche Quelle?

22. September 2026 · **UR.SOURCE.VARIATION_ORIGIN.01** · **PARTIAL**

## 1. Ergebnis und Reichweite

Der neue Gross–Neveu-/Berry-Vorschlag ist ein bedingter Mechanismus. Diese Fortsetzung untersucht die davorliegende Frage: Werden seine massenartigen und familienbewegenden Vertizes von den tatsächlich angegebenen Quellenoperatoren erzeugt?

Für die skalare Randzeit und die natürliche Determinantenfortsetzung lautet die Antwort innerhalb ihrer angegebenen Klasse **nein**. Ein allgemeiner Kommutantensatz schließt auch die Reparatur durch beliebig viele innere Fluktuationen derselben blockbewahrenden Algebra aus. Eine echte zusätzliche Operatorrichtung oder eine aus der Quelle abgeleitete nichtabelsche Verbindung bleibt möglich. Welche davon vorliegt, bestimmt die vorhandene Fluktuationsrechnung nicht.

Die Untersuchung findet außerdem eine konkrete logische Lücke in der behaupteten Ursprungsauswahl: Der Originalbeweis für das eindeutige minimale Randdatum liefert ein Minimum eines diskreten Defektvektors, aber keine Klassifikation sämtlicher Operatoren mit diesem Defektvektor. Die spätere Master-Barriere setzt das ausgewählte Randdatum schon ein. Sie schließt diese Lücke nicht nachträglich.

Das ist **kein allgemeiner Unmöglichkeitssatz für TFPT**. Insbesondere bleiben die E8-Verzweigung, Ladungen, nativen Produkte, der gemeinsame Clock-Compiler-Vergleich und die vorhandene Flavor-/Massenleiter erhalten. Die hier geschlossene Teilfrage betrifft die Herkunft der fehlenden Vertizes aus den derzeit expliziten Quellenoperationen. Die vollständige geladene Quelle und T1–T8 sind nicht gelöst.

## 2. Originaldaten statt neuer Hilfsquelle

Die Quellfassung `01_boundary_kernel_source.tex` enthält drei unterschiedliche Ebenen:

1. Zeilen 65–81: Das einseitige Datum enthält **D+ und BΣ als Operatoren** und verlangt die Kragenform
   \[
   D_+=\gamma_n(\partial_n+B_\Sigma).
   \]
2. Zeilen 480–521: Der operationale Start enthält lokale Algebra, Zeit, Reflexion, Zustand, Nahtklasse und **Dcoll**. Die Vervollständigung rekonstruiert den Rand aus diesem bereits gelieferten Kragenoperator. Sie ist keine Gleichung, die Dcoll aus einer zahlenmäßig kleineren Startmenge berechnet.
3. Zeilen 302–316: Die primitive Wirkung ist für ein deklariertes Testprofil
   \[
   S_{\rm prim}=\operatorname{Tr}f(D_{\rm rel}/\chi_{\rm seed})
   -\operatorname{Tr}f(D_{\rm ref}/\chi_{\rm seed})
   +\frac{i\pi}{2}\Delta\eta_\Sigma.
   \]
   Die Wirkung bewertet Operatoren. Um ihre Ableitungen nach Feldern auszurechnen, braucht man zusätzlich die tatsächlich zugelassene Abhängigkeit dieser Operatoren von den Feldern.

Der primitive Hodge-Projektor aus Zeilen 192–263 wählt den nahtgeraden und zulässig gegappten Sektor. Er ist nicht ohne weitere Abbildung ein Rang-drei-Familienprojektor. Der frühere Contract `raw-carrier-origin-gate-20260920` hat bereits den Ausschluss bewiesen, aus der Pluskompression derselben Involution anschließend einen negativen Carrier zu erhalten; dieser Ausschluss wird hier nicht als neuer Befund ausgegeben.

Die konkreten bisher geprüften Variationen sind:

| Daten | Nachgewiesene Wirkung | Nicht dadurch geliefert |
|---|---|---|
| Positive Randdichte q(θ), h=qD auf dem gewichteten Randraum | Skalarer lokaler Zeit-/Geometriefaktor | Interne Familienmischung oder ein Rechts-links-Massenvertex |
| Natürlicher Lift von A_E auf Λeven E und Determinantenpotenzen | Geladene Bündelverbindung mit festem 3+1-Split | Nichtabelsche Verbindung innerhalb der Dreierfamilie oder Bewegung dieses Splits |
| Vorhandenes Flavor-Lokalsystem und Transportkernel | Bedingte Holonomien und Yukawa-Transportformeln | Identifikation als geladene Fluktuation des ursprünglichen Dcoll |
| Endliches NCG-Modell, v252/v254 | Algebraische Konsistenz und erlaubte Fluktuationen für geliefertes D_F | Berechnung des gelieferten D_F aus Dcoll |

In `v254_inner_fluctuations.py:83–88` werden die vier Yukawa-Matrizen als zufällige komplexe 3×3-Matrizen erzeugt und an `full_D` übergeben. Diese Verwendung ist für einen allgemeinen Konsistenztest sinnvoll. Sie ist keine Herkunftsherleitung dieser Matrizen. Die tatsächliche TFPT-Flavorrechnung steht getrennt davon im Transportteil; sie wird durch diesen Befund nicht verworfen.

## 3. Die vorgeschlagene gemeinsame Ableitung, kovariant formuliert

Es seien h(q) ein tatsächlich gegebener selbstadjungierter Quellhamiltonoperator, ∇ die festgelegte Verbindung zum Vergleich seiner Hilberträume und P(q) ein isolierter Spektralprojektor. Auf einer lokal festen Kontur gilt
\[
P=\frac1{2\pi i}\oint(z-h)^{-1}dz,
\qquad
\nabla_A P=\frac1{2\pi i}\oint
(z-h)^{-1}(\nabla_A h)(z-h)^{-1}dz.
\]
Damit ist die gesuchte Projektorableitung berechenbar, sobald der tatsächliche Quellvertex und die Vergleichsverbindung vorliegen. Die Identifikation von h mit einer Funktion von Dcoll ist ihrerseits mitzuführen; sie wird hier nicht vorausgesetzt.

Für ein exakt entartetes Dreierband hP=EP, p=1−P und einen nichtverschwindenden Abstand zum Komplement folgt durch Differentiation:
\[
B_A:=p(\nabla_A P)P
=-(h_p-E)^{-1}p(\nabla_A h)P.
\]
Für ein gespaltenes Band tritt die entsprechende Sylvestergleichung an die Stelle dieses einzelnen Energienenners.

Die induzierte Verbindung P∇ auf dem Dreierraum hat die Krümmung
\[
\boxed{F^P=P F^\nabla P+P(\nabla P)\wedge(\nabla P)P.}
\]
Bei flacher Umgebung ist der zweite Term in Komponenten
\[
F^P_{AB}=B_A^\dagger B_B-B_B^\dagger B_A.
\]
Das ist die präzise Verbindung zwischen einer tatsächlichen Quellenantwort und der vorgeschlagenen Geometrie. Die Formel erzeugt den fehlenden Quellvertex nicht selbst.

## 4. Echte Bandbewegung und bewegte Beschreibung

Sei P0 konstant und U(q) unitär. Werden **alle** Daten gleichzeitig als
\[
P'=UP_0U^\dagger,\qquad \nabla'=U d U^\dagger
\]
transformiert, so gilt
\[
\nabla'P'=0,\qquad F^{P'}=0.
\]
Hier bedeutet UdU† den Operator s↦U d(U†s). In einer festen Darstellung lautet seine Verbindungsform A=−dU U†.

Wird dagegen nur h bzw. P relativ zu einem **physisch festgehaltenen** d verändert, ist eine nichtverschwindende Berry-Krümmung möglich. Das ist keine bloße Wahl einer Basis im Dreierband. Welche Interpretation gilt, muss die ursprüngliche Quelle festlegen.

Der Checker vergleicht dieselben sechs infinitesimalen Mischrichtungen zwischen einer Linie und einem Dreierraum. Bei festem d spannen ihre projizierten Krümmungen u(3), Dimension neun, und ihre spurfreien Teile su(3), Dimension acht. Mit der mittransformierten Umgebung verschwinden sie. Dabei sind auch die Ableitungen von A berücksichtigt: Am Ausgangspunkt heben sich −[G_A,G_B] und [A_A,A_B] exakt auf. A_A=−G_A darf nicht irrtümlich als konstante Verbindung ohne diese Ableitungen interpretiert werden.

Die CP3-Rechnung aus dem Anhang bleibt deshalb ein gültiger bedingter Zeuge. Sie beweist nicht, dass die ursprüngliche Quelle den physisch bewegten Projektor und den festgehaltenen Vergleich auswählt.

## 5. Ein Abschluss-Satz für alle blockbewahrenden inneren Fluktuationen

**Satz.** Sei P ein fester orthogonaler Projektor in einem reellen Spektraltripel mit JDJ⁻¹=±D. Er reduziere den selbstadjungierten Operator D einschließlich seiner Domäne. Für jedes dargestellte Algebraelement a gelte
\[
[P,D]=0,\qquad [P,a]=0,\qquad [P,JaJ^{-1}]=0.
\]
Dann erhalten die inneren Fluktuationen derselben Daten den Unterraum P. Dies gilt auch für die quadratischen Korrekturen ohne erste-Ordnungs-Bedingung und für beliebig viele Wiederholungen.

**Beweis.** Die Jacobi-Identität ergibt [P,[D,b]]=0. Der Kommutant von P ist unter Summen, Produkten, Adjungieren und Kommutatoren abgeschlossen. Daher kommutieren a[D,b], die aus der gegenüberliegenden Algebra gebildeten Terme und ihre quadratischen Kombinationen mit P. Nach jeder solchen Fluktuation gelten dieselben Voraussetzungen erneut. Bei unbeschränktem D sind Domäneninvarianz und wohldefinierte Kommutatoren Teil der Voraussetzungen; der Satz ersetzt keine analytische Domänenprüfung.

Die verwendeten linearen und quadratischen Fluktuationsformeln sind in [Connes–Chamseddine](https://arxiv.org/abs/hep-th/0605011) und [Chamseddine–Connes–van Suijlekom](https://arxiv.org/abs/1304.7583) beschrieben. Der obige Kommutantenschluss ist hier ausgeschrieben und nicht aus einer Behauptung über deren physische Anwendung abgeleitet.

**Anwendung auf die tatsächlich untersuchte Fortsetzung.** Für
\[
A_W=\rho_{\Lambda^{\rm even}}(A_E)\otimes I_4
+I_{16}\otimes\operatorname{diag}(r,r,r,-2-3r)\,\operatorname{tr}A_E
\]
ist P3=diag(1,1,1,0) parallel. Der Familienteil auf seinem Bild lautet lediglich
\[
r\,\operatorname{tr}(A_E)I_3.
\]
Die natürliche Fortsetzung liefert somit keine 3↔1-Vertizes und für sich allein auch keine nichtabelsche Verbindung innerhalb der drei Familien. Ein zusätzliches Φ im Diracoperator kann diese Aussage ändern, **wenn Φ solche Blöcke besitzt**; genau deren Herkunft darf dann nicht vorausgesetzt werden.

Für Herm(4) hat der Kommutant von P3 reelle Dimension 10. Die fehlenden 3↔1-Richtungen bilden sechs reelle Dimensionen. Bei β=b(4P3−3I), b≠0, sind die Kommutanten identisch, denn
\[
[\beta,H]=4b[P_3,H].
\]
Der Checker prüft diese Identität und die vollständigen linearen Ränge, nicht nur einzelne Beispiele.

**Wichtige Grenze.** Ein Operator kann P3 erhalten und dennoch nichtabelsch innerhalb seines Bildes wirken. Der Satz verbietet eine separat hergeleitete U(3)-Verbindung nicht. Ebenso wenig gilt er für eine größere ursprüngliche Algebra mit Offblock-Operatoren. Die vollständige native W-Algebra wird hier ausdrücklich nicht mit der kleineren Determinantenfortsetzung identifiziert.

## 6. Was eine skalare Randzeit an den Gross–Neveu-Vertizes ändert

Die lokale Zeitrechnung liefert einen skalaren q(θ)D-Operator auf einem gewichteten Randhilbertraum. Für eine Erweiterung als Identität im internen Familienfaktor gilt unabhängig vom Profil
\[
(1-P_3)\,\delta(qD\otimes I_F)\,P_3=0.
\]
Für nichtkonstantes q(θ) können sich räumliche Eigenfunktionen durchaus ändern. Der Schluss betrifft den **internen** Familienprojektor und nicht sämtliche räumlichen Spektralprojektoren. Auch die durch q veränderte Hilbertraummetrik wird durch einen skalaren, intern kommutierenden Transport berücksichtigt.

Der GN-Anhang nimmt zusätzlich eine freie nichtchirale 1+1D-Vervollständigung mit rechten und linken 10+6-Vektorfermionen an. Koppelt an diese lediglich eine skalare Metrik-/Zeitfluktuation, bleiben die unabhängigen internen Drehungen
\[
SO(10)_R\times SO(10)_L\times SO(6)_R\times SO(6)_L
\]
erhalten. Das gilt für jeden Wert der skalaren Fluktuation und daher auch nach deren Ausintegration, sofern Maß und Regularisierung diese Symmetrie erhalten.

Die benötigten Bilineare BD=iΣχRχL und BF=iΣχRχL identifizieren hingegen rechte und linke interne Indizes. Ihre GN-Kopplungen bewahren im Allgemeinen nur die jeweils diagonalen Drehgruppen. Sie können in der genannten symmetrischen Klasse nicht als solche aus der reinen Metrikkopplung entstehen. Die unmittelbar vermittelte Wechselwirkung koppelt kinetische Dichten bzw. Energie-Impuls-Tensoren und enthält Ableitungen.

Dieser Ausschluss gilt für die angegebene masselose kinetische Vervollständigung. Ein bereits vorhandener interner Massenterm, eine chiralitätsändernde skalare Quelle, gemeinsam gekoppelte dynamische Eichfelder, eine andere Zustands-/Symmetriestruktur oder zusätzliche dimensionale Reduktion kann die Voraussetzungen ändern. Das sind zu prüfende ursprüngliche Daten, keine Folgen des Symbols q allein. Interne Graduierung und Raumzeit-Chiralität werden nicht gleichgesetzt.

### Eine elementare Massenquelle ist nicht zwingend erforderlich

Der skalare Vermittlungsweg im Anhang ist hinreichend, aber nicht notwendig. Für normalgeordnete lokale Grassmann-Quartiken setze
\[
B_a=i\chi_R^a\chi_L^a,\quad J_R^{ab}=i\chi_R^a\chi_R^b,
\quad J_L^{ab}=i\chi_L^a\chi_L^b,\quad a<b.
\]
Einmaliges Vertauschen der mittleren Grassmannfelder ergibt exakt
\[
B_aB_b=-J_R^{ab}J_L^{ab}.
\]
Damit ist derselbe GN-Term gleich
\[
g_D\sum_{a<b\le10}J_R^{ab}J_L^{ab}
+g_F\sum_{11\le a<b\le16}J_R^{ab}J_L^{ab}
+g_X\sum_{a\le10<b}J_R^{ab}J_L^{ab}.
\]
Die drei Summen besitzen 45, 15 und 60 Kanäle: die schon bekannte Bivektorzerlegung von so(16). Eine tatsächlich hergeleitete gemeinsame Stromvermittlung wäre deshalb ein zweiter Zugang ohne neue elementare skalare Massenquelle. Ein symmetriebrechender gemeinsamer Stromkopplungsterm fällt nicht unter den obigen Metrik-allein-Ausschluss.

Die Identität bestimmt weder einen ursprünglichen Strompropagator noch sein Vorzeichen, seine Reichweite oder seinen Zustand. Sie identifiziert außerdem nicht interne so(16)-Generatoren automatisch mit dynamischen Eichfeldern. Sie gilt für die angegebenen normalgeordneten Quartiken; Kontaktterme und eine renormierte Quantentheorie brauchen ihre eigenen Festlegungen. `current_channel.py` prüft die 120 Paaridentitäten und die drei vollständigen Koeffizienten getrennt.

## 7. Was die Spektralwirkung tatsächlich zur Hessian beiträgt

Am endlichen Schnitt sei L(q)=D(q)/χ(q) eine glatte selbstadjungierte Matrixfamilie. Alle Ableitungen der Skala χ sind in L enthalten. Setze
\[
V_A=\partial_A L,\qquad W_{AB}=\partial_A\partial_B L.
\]
In einer Eigenbasis von L mit Eigenwerten λi gilt für ein hinreichend glattes f:
\[
\partial_A\partial_B\operatorname{Tr}f(L)
=\operatorname{Tr}\bigl(f'(L)W_{AB}\bigr)
+\sum_{ij}(f')^{[1]}(\lambda_i,\lambda_j)
(V_A)_{ij}(V_B)_{ji},
\]
mit (f')^[1](x,y)=(f'(x)−f'(y))/(x−y) und diagonal f''(x).

Für die relative Wirkung müssen die entsprechenden Referenzterme subtrahiert und die η-Antwort separat berücksichtigt werden. In unendlicher Dimension braucht die Formel zusätzliche Regularitäts-/Spurannahmen. Aus der relativen Differenz folgt insbesondere nicht automatisch eine positive Gauß-Kovarianz auf allen Feldern. Stabilität und die Entfernung von Eichnullrichtungen sind eigene Voraussetzungen einer Gauß-Näherung.

**Der zweite Operatorjet ist wesentlich.** Sei
\[
L(t)=e^{tX}\operatorname{diag}(e_0,e_1,e_1,e_1)e^{-tX}
\]
mit einer Rotation zwischen der ersten und zweiten Richtung. Dann ist jedes Tr f(L(t)) konstant. Für f(x)=x² ergibt die vollständige Ableitung
\[
2\operatorname{Tr}(L'^2+LL'')=0,
\]
während das Weglassen von L'' den falschen positiven Wert 4(e0−e1)² erzeugt. Der Checker verifiziert dies exakt und prüft die Hessianformel für f(x)=x⁴ mit allgemeinen symbolischen hermiteschen V und W an einem festen vierdimensionalen Diagonaloperator.

Damit kann man K_AB nicht aus einer gewünschten ersten Vertexmatrix bestimmen und die zweite Ableitung stillschweigend fortlassen. Die vollständige Abhängigkeit der Quelle wird gebraucht.

Bei rein internen isospektralen Matrizen kann eine Spektralspur keine Eigenvektorbewegung auswählen. Beim **vollständigen Differentialoperator** ist die Grenze wichtig: Wird nur der interne Term gedreht und die räumliche Ableitung festgehalten, können Spektralwirkung und Wärmeentwicklung Gradienten dieser Drehung erfassen. Wird dagegen der vollständige Operator einschließlich Verbindung unitär konjugiert, bleibt auch seine Spektralspur unverändert. Ein allgemeines Verbot geometrischer Dynamik wird daraus nicht abgeleitet.

## 8. Die Ursprungsauswahl ist im Original behauptet, aber hier nicht bewiesen

Die Quelle enthält tatsächlich mehr als eine offene Liste von Parametern. `01_boundary_kernel_source.tex:543–559` definiert eine lexikographische Defektfolge aus Spektralfluss, wesentlichem endlichen Rang, Determinantengrad und verbleibender Randnullität. In Zeilen 646–682 wird ein eindeutiges minimales Randdatum bis auf unitäre Äquivalenz behauptet.

Der dortige Beweis liefert jedoch nur das folgende:

- Wohlordnung gibt bei nichtleerer zulässiger Defektmenge einen kleinsten **Defektvektor**.
- Entfernen trivialer Summanden verhindert eine bestimmte künstliche Rangvergrößerung.
- Die Kragen-Normalform beschreibt die Form des Diracoperators.

Keiner dieser Schritte zeigt, dass zwei Operatoren mit demselben minimalen Defektvektor unitär äquivalent sind. Dafür wäre eine Injektivitäts-/Klassifikationsaussage über die gesamte minimale Faser nötig. Schon die Invarianzaussage in Zeilen 588–593 nennt diese Klassifikation als zusätzlichen Schritt. Sie wird im anschließenden Beweis nicht durchgeführt.

`02_carrier_source.tex:3021–3062` definiert anschließend die Master-Barriere als null genau für B≅Bmin und sonst unendlich. Die kontinuierlichen Variablen sind α, χgeo, δph und ρvac. Die Barriere **setzt die Klasse von Bmin bereits voraus**. Sie ist keine unabhängige Operator-Auswahlgleichung. Die dortige Ableitung der vier kontinuierlichen Sektorgleichungen liefert deshalb nicht automatisch die fehlenden geladenen Ableitungen von Dcoll.

Diese Feststellung ist eine konkrete Beweislücke im Auswahlargument. Es wird hier kein vollständiges Gegenmodell zu allen TFPT-Bedingungen behauptet. Insbesondere wird eine mögliche globale Skalierung nicht als vollständiger Gegenbeweis ausgegeben: Dafür müssten Normalisierung, sämtliche Zulässigkeitsbedingungen und spätere Rückkopplungen gemeinsam erhalten werden.

## 9. Welcher Weg den vorhandenen Flavor-Erfolg erhält

Die ursprüngliche Flavorverbindung ist ein **flaches** Lokalsystem. Eine flache Verbindung kann nichtabelsche globale Monodromie besitzen. Deshalb ist nichtverschwindende Berry-Krümmung kein notwendiges Ziel für diesen bereits vorhandenen Kandidaten.

Der Quotient
\[
L_F=(\widetilde X_f^\circ\times\mathbb C^3)/\rho_F,
\qquad X_f^\circ=\mathbb P^1\setminus\mu_4,
\]
liefert bei vorgegebener vollständiger unitärer Darstellung ρF tatsächlich die entsprechende flache Verbindung. Das ist die gültige Konstruktion in `03_em_flavor_source.tex:1217–1237`. Ihre dort behauptete vorherige Auswahl allein aus lokalen Spektren und D4-Symmetrie darf nicht ungeprüft übernommen werden: `source-boundary-lift-selection-20260922` hat zwei nichtkonjugierte Pakete mit diesen groben Bedingungen gezeigt und die archivierte explizite Paketformel beanstandet.

Der aktuelle v117-Kandidat und sein gemeinsames Wörterbuch mit den ursprünglichen Compilerclocks bleiben als präzise Vergleichsdaten verfügbar. Dabei ist M eine Punkturmonodromie und U eine Deck-Äquivarianz; U wird nicht zu einer zweiten gewöhnlichen Schleifenholonomie umgedeutet.

Die kürzeste noch sinnvolle Herkunftsaufgabe ist daher:

**Aus dem tatsächlichen geladenen Kragenproblem die Verbindung auf seinem Familienraum ableiten und erst danach mit dem vorhandenen flachen Kandidaten vergleichen.**

Ein solcher direkter Anschluss braucht keine künstlich gekrümmte CP3-Zwischenwelt. Ergibt die Quelle stattdessen wirklich einen bewegten isolierten Unterraum, liefern die Formeln in Abschnitt 3 seinen korrekten Test. Die Art des Anschlusses darf nicht vorher anhand des gewünschten Ergebnisses ausgewählt werden.

Für den GN-Zweig ist getrennt die tatsächliche Kopplung zwischen den rechten und linken Sektoren samt Zustand und Korrelationsfunktion erforderlich, entweder durch Massenquellen oder durch die dargestellte gemeinsame Stromvermittlung. Eine elementare rechts-links-koppelnde Zweifermionmatrix ist dafür nicht generell notwendig. Die erfolgreiche Ein-Schleifen-Verhältnisgleichung aus dem Anhang kann die Herkunft der Wechselwirkung nicht ersetzen; auch ein positiver gekoppelter Gram allein liefert keine vierdimensionale chirale Materie.

## 10. Prüfung und belastbarer Abschluss

`checker.py` prüft die endlichen algebraischen Identitäten, Ränge, kovariante Auslöschung und Hessian-Gegenprobe. `INDEPENDENT_REVIEW.md` ist eine getrennte mathematische Agentenprüfung, kein externes Peer Review. Die Quelleninventur beruht auf den hier benannten Originalstellen, nicht auf dem bloßen Fehlen von Suchtreffern. Die allgemeinen Kommutanten- und Symmetrieschlüsse sind im Text bewiesen; ein endlicher Checker wird nicht als Beweis aller analytischen Voraussetzungen verkauft.

Kein genetischer Algorithmus wurde eingesetzt. Er könnte innerhalb des bewiesenen Kommutanten keine fehlende Operatorrichtung erzeugen. Eine Suche in einer größeren Klasse würde zuerst eine Begründung dieser Klasse aus den ursprünglichen Daten benötigen.

**Offen bleibt genau die gemeinsame geladene Quellenrealisierung: Auswahl des Operators und der erlaubten Variationen, Zustand, Produkte und Zeitantwort auf demselben Raum. Die vollständige TFPT-Lösung ist damit weiterhin nicht erbracht.**
