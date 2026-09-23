# Prüfanmerkungen zur Universalraum-Konsolidierung

10. September 2026. Die verständliche Übersicht steht in Universalraum-Konsolidierter-Stand.md. Hier folgen die getrennten mathematischen Gegenprüfungen.

---

## Mathematische Schließung und nativer Rand

# Gegenprüfung der neuen Pro-Analyse, Abschnitte 1 und 2

Die beiden neuen algebraischen Sätze sind im genau angegebenen Modell richtig. Für die konsolidierte Übersicht lautet die entscheidende Aussage:

**Die neue Auswahlbedingung funktioniert im exakt erklärten Modell. Dass dieses Modell und gerade diese Auswahlbedingungen aus der vollständigen nativen Quelle folgen, bleibt zu zeigen.**

Die Prüfung bezieht sich auf den eingefügten Text `/Users/stefanhamann/.codex/attachments/32aeadc6-1536-4caa-8b43-67cb47b2fa6c/pasted-text.txt`. Die dortigen Inhaltsreferenzen 9 und 10 enthalten hier keine auslesbaren zusätzlichen Manuskripte oder Prüfpakete. Die folgende Bewertung benötigt diese Referenzen nicht für die endliche Algebra; die unbeschränkte Erweiterung wird mit eigenen ausdrücklichen Voraussetzungen formuliert. Es wurde kein TFPT-Code ausgeführt oder verändert.

## 1. Positiver Sättigungssatz: korrekt, mit zusätzlichen Quellprämissen

Für endlichdimensionales, invertierbares selbstadjungiertes A, selbstadjungiertes D und
\[
B=\begin{pmatrix}A^2/4&A/2\\A/2&D-3I\end{pmatrix}\ge0
\]
ist die angegebene Kongruenz exakt; insbesondere ist keine Vertauschbarkeit von A und D erforderlich. Es folgt D≥4I. Deshalb erzwingt tr D=4d genau D=4I. Ebenso gilt bei 0≤tr(D−4I)≤ε die Operatornormschranke ||D−4I||≤ε.

Zusätzliche Voraussetzungen sind der vollständig festgehaltene niedrige und gemischte Block, die relative Kopplungspositivität gegenüber dem bezeichneten freien Parent und das exakte Spurbudget. Gesamtpositivität oder die Positivität von e^(−tH) liefert die relative Kopplungspositivität nicht. Das im Text genannte Erwartungswertgegenbeispiel −1/34 stimmt: Auf einem Eigenvektor mit A-Eigenwert a=−ξ/2 hat der Vektor (−2a^(−1),1) normiert durch √17 den relativen Erwartungswert (ξa)/17=−1/34.

Bei singulärem A lautet die allgemeine endliche Schurbedingung stattdessen
\[
D\ge3I+P_{\operatorname{ran}A}.
\]
Das Minimalbudget beträgt dann 3d+rank A. Das Budget 4d ist nicht mehr minimal. Beispielsweise sind A=diag(1,0), D=diag(5,3) zulässig und haben tr D=8, obwohl D≠4I. Die im Pro-Text ausdrücklich verlangte stetige Erweiterung von invertierbaren Hintergründen ist eine mögliche zusätzliche Lösung; die invertierbaren Hintergründe müssen dafür im tatsächlich erlaubten Familienraum hinreichend dicht sein.

### Der native ambiente Randterm verhindert die automatische Übertragung

Unser bereits gesicherter Randabschluss lautet
\[
L_{\rm amb}=A_S+\frac14(A_S^2+C^\dagger C),\qquad
C^\dagger C=4a^2I,\quad a=\frac1{12}.
\]
Der Pro-Satz behandelt dagegen exakt L=A+A²/4. Diese Differenz ist für sein Sättigungsargument entscheidend. Gegenüber dem unveränderten freien Parent diag(A_S,3I) hat die echte ambiente relative Form den niedrigen Block (A_S²+4a²I)/4. Ihre Schurbedingung ist
\[
D\ge3I+A_S(A_S^2+4a^2I)^{-1}A_S.
\]
Da ||A_S||≤2a, liegt der letzte Summand zwischen 0 und I/2. Das Budget tr D=4d ist hier folglich nicht ausgeschöpft. Insbesondere bleiben D=4I±A_S zulässig, weil D−3I≥5I/6.

Ein vollkommen exakter Gegenfall verwendet den Viererring mit unitären Linkphasen und Gesamtfluss π:
\[
A_S=a\begin{pmatrix}
0&1&0&-1\\
1&0&1&0\\
0&1&0&1\\
-1&0&1&0
\end{pmatrix}.
\]
Dies ist ein zulässiger fester unitärer Linkhintergrund der ambienten Einteilchen-Wand. Er erfüllt A_S²=2a²I, ist also invertierbar, und hat Spur null. Der relative niedrige Block ist genau I/96, entsprechend dem ursprünglichen ambienten Onsite-Wert 6c. Für D=4I±A_S hat die relative Form den strikt positiven Schurrest
\[
\frac23I\pm A_S>0,
\]
und gleichzeitig gilt tr D=16, D≠4I. Das ist kein Gegenbeispiel gegen den korrekt formulierten Pro-Satz: Es zeigt, warum der richtige niedrige Block und der gewählte freie Parent bei der Übertragung auf die tatsächliche Quelle nicht übersprungen werden dürfen. Insbesondere ist dies keine Behauptung einer vollständigen quantisierten Rotor- oder Vielteilchenrekonstruktion.

Man könnte den festen Randbeitrag in den freien Parent aufnehmen und relative Positivität bezüglich dieses strengeren Parents verlangen. Dann müsste gerade diese geänderte relative Positivität aus der Quelle gerechtfertigt werden; sie folgt nicht schon aus der bisherigen ambienten Gramdarstellung.

## 2. Vier Operatorzeitmomente: korrektes Schließungskriterium

Für selbstadjungierte endliche oder beschränkte Blöcke und reelles m stimmen alle angegebenen Formeln. Die geordnete Rechnung für M4 enthält insbesondere sowohl LC1 als auch C1L und den Term C0². Es folgt
\[
\Delta_4(m)=((D-mI)V)^\dagger((D-mI)V)\ge0.
\]
Bei Δ4=0 gilt DV=mV. Damit ist der Raum aus dem gesamten niedrigen Eingaberaum und dem Abschluss von ran V invariant. Auf dem davon nicht erreichbaren hohen Raum darf D weiterhin beliebig sein; der Satz rekonstruiert nicht sämtliche denkbaren Eingaben oder Interventionen. Diese Grenze ist im Pro-Text richtig angegeben.

Die Rechtsrekursion
\[
M_{k+2}=M_{k+1}(L+mI)-M_k(mL-C_0)
\]
ist auch dann korrekt, wenn L und C0 nicht kommutieren. Direkt gilt
\[
H^2J-HJ(L+mI)+J(mL-C_0)=0.
\]
Links mit J†H^k multipliziert ergibt dies die behauptete Rekursion. Die adjungierte Linksrekursion ergibt die angegebene Differentialgleichung für den niedrigen Ausgang. Es liegt kein unzulässiger Austausch der Multiplikationsreihenfolge vor.

Das Beispiel D=4I+ξA^r, V=A/2 liefert bei selbstadjungiertem A und reellem ξ genau Δ4(4)=ξ²A^(2r+2)/4. Erfasst werden vollständige Operatorzeitmomente, keine endlich vielen räumlichen Taylorzahlen. Das beseitigt weder Auslesekosten noch die mögliche geringe Größe des Residuumsignals.

### Die vollständige Duhamel-Schranke und ihre Bereiche

Eine ausreichende, ausdrücklich nachprüfbare unbeschränkte Version lautet: L und V sind beschränkt, L ist selbstadjungiert, D ist selbstadjungiert, ran V⊂Dom D und DV ist beschränkt. Letzteres folgt hier bereits aus der Abgeschlossenheit von D und dem Satz vom abgeschlossenen Graphen. H ist dann auf H_low⊕Dom D selbstadjungiert. Setze R=(D−mI)V und η=||R||.

Schreibe U_flat(s)J=(X(s),Y(s))^T. Dann
\[
Y(s)=-i\int_0^s e^{-im(s-r)}VX(r)\,dr,
\qquad
\|(D-mI)Y(s)\|\le |s|\eta,
\]
weil ||X(r)||≤1. Das Integral liegt im Graphbereich von D. Die Duhamelidentität liefert somit für alle reellen t
\[
\|(e^{-itH}-e^{-itH_{\rm flat}})J\|
\le\eta t^2/2.
\]
Die Aussage benötigt keinen uniformen kleinen Operator D−mI auf dem gesamten hohen Raum. Sie kontrolliert den vollen Ausgang, aber nur für das erklärte J.

**Bei unbeschränktem H müssen die Momentdefinitionen präzisiert werden.** Unter den eben ausreichenden Voraussetzungen sind die beschränkten Formmomente
\[
M_2=(HJ)^\dagger(HJ),\quad
M_3=(HJ)^\dagger H^2J,\quad
M_4=(H^2J)^\dagger(H^2J)
\]
definiert und liefern genau die Restidentität mit C2=(DV)†DV. Der Ausdruck J†H⁴J als buchstäbliche Komposition kann stärkere Bereiche verlangen; bei beschränkten L,V reicht beispielsweise ran V⊂Dom D³. Ohne Einsicht in das referenzierte Manuskript ist dessen konkrete Bereichsformulierung nicht geprüft. Die endliche Aussage und die hier ausgeschriebene unbeschränkte Formmoment-Version sind direkt begründet.

## 3. Verhältnis zu den bisherigen Ergebnissen

- Unser Determinanten-Schließungssatz fixiert den vollständigen niedrigen und gemischten Kernel und eine gemeinsame Polynomklasse. Der neue Sättigungssatz ist ein anderer ausreichender Quellvertrag: Er erlaubt allgemeines D, braucht dafür relative Positivität und minimale Spur. Beide Aussagen sind konditional; keiner der Verträge wurde bislang aus der ursprünglichen Seam hergeleitet.
- Unser Randabschluss bestimmt den tatsächlichen zusätzlichen niedrigen Beitrag. Er muss vor der Anwendung des neuen Auswahlprinzips berücksichtigt werden; der invertible Phasenring oben demonstriert die Konsequenz.
- Unser Thermalresultat konstruiert für jedes feste s>0 ganze, energiegeglättete Feldoperatoren und konvergente endliche Produkte. Es beweist weder Δ4=0 noch ein minimales Spurbudget und entfernt die Puffer nicht. Der Momenttest kann eine zusätzliche Prüfung auf einem präzise identifizierten Eingaberaum sein; er ersetzt diesen Operator-/Bereichsabschluss nicht.
- Die skalaren Zahlen aus §3 sind intern konsistent: M4−M2²−M3²/M2=12673/23887872; der angegebene Selektor F(ξ) hat bei ξ=0 genau diesen Wert. Die unabhängige Herkunft der angegebenen nativen Momente ist damit noch nicht verifiziert.

Der eigene kleine Prüfer `check_algebra.py` besteht 37 exakte rationale/symbolische Kontrollen, darunter nichtkommutierende Momentbeispiele, die Rekursion und der invertible ambiente Randgegenfall. Diese Kontrollen stützen die Rechnung; die allgemeinen Aussagen werden durch die obigen Beweise getragen. Die Rückkehr-, Galois- und Komplexitätsaussagen der späteren Abschnitte waren nicht Gegenstand dieses begrenzten Reviews.

---

## Synchronisation und Quantenkompilierung

# Kurzaudit: Synchronisation und Quantenkompilierung, §§4–6

Geprüft wurde der Nutzertext `/Users/stefanhamann/.codex/attachments/32aeadc6-1536-4caa-8b43-67cb47b2fa6c/pasted-text.txt`, Zeilen 342–507. Die beiden Prüfpakete werden dort lediglich über nicht auflösbare `chatgpt-content-reference`-Marken bezeichnet. Ihre Originalbeweise und Ergebnisdateien lagen diesem Audit nicht vor. Keine Repositoryänderung, keine Rückkehrkampagne und keine Ausführung fremder Prüfer.

**Gesamturteil:** Die zentrale Phasenidentität ist exakt richtig. Sie schließt die angegebene Driftinkompatibilität, sofern die gemeinsamen Spektralrelationen und Quellzuordnungen tatsächlich so gelten wie behauptet. Die quantitativen Exponenten sind als konservative bedingte Abschätzungen mathematisch nachvollziehbar. Das trägt einen bedingten asymptotischen Anschluss an Shor unter einem idealen skalierbaren Gerätevertrag, aber bestätigt noch keine praktische Maschine oder vollständige TFPT-Herleitung. Es wurde in den dargestellten Formeln kein konkreter algebraischer Widerspruch gefunden.

## Evidenzklassifikation

| Behauptung | Prüfung | Einordnung |
|---|---|---|
| Angegebene Spuren und Phasen erfüllen die gemeinsame Identität | Sieben rationale Identitätsprüfungen, Ergebnis `exact-trace-check.json` | Direkt unabhängig geprüft; die Spuren selbst wurden nicht aus den Quellmatrizen rekonstruiert |
| Quellpolynome haben Gruppen S38, S32 und S4 | Die Polynome und modularen Zertifikate stehen nicht im Paste | Berichtete Voraussetzung, hier nicht unabhängig bestätigt |
| Alle gemeinsamen rationalen Relationen sind innerhalb der drei Blöcke konstant | Gruppenargument unter den genannten vollen symmetrischen Gruppen schlüssig | Bedingter Schluss, keine unabhängige Prüfung des konkreten Quellzertifikats |
| Aktiver Austausch und inaktive Identität sind gemeinsam näherbar | Kontinuierlicher Torusabschluss plus exakte Phasenkompatibilität | Mathematisch korrekt unter dieser Relationen- und Quellprämisse |
| Zeitexponent `38!32!4!+73` und verbesserter Exponent 146 | Allgemeines Norm-/Fourierargument rekonstruiert; keine konkrete Konstante oder Originalabschätzung reproduziert | Nachvollziehbar konditional, nicht als vollständig unabhängig verifiziert ausgeben |
| Q016 liefert lokale Vierercodeoperationen aus 13 Altersquellen mit polynomialen Ressourcen | Im Paste lediglich referiert | Zusätzliche nicht unabhängig geprüfte Quell-/Compilerprämisse |
| Daraus folgt polynomialer Shor-Aufwand | Fehler- und Ressourcenkomposition ist unter diesen Voraussetzungen konsistent | Bedingtes Quantenkorollar; keine neue klassische Faktorisierung und keine Praxisvalidierung |

## 1. Was die Phasenrechnung genau leistet

Mit den angegebenen rationalen Spuren und Phasen ergibt sich komponentenweise

\[
(38(\gamma/q-1),32(\gamma/q+1),4\chi/q)
=\left(\frac{13910356}{15},\frac{11714944}{15},\frac{731728}{15}\right)
=3040(T_+,T_-,T_4).
\]

Die Formel gilt auch für q=0, wenn man sie ohne Division als lineare Identität in q schreibt. Sind alle Energierelationen blockkonstant, so liefert jede ganzzahlige Relation `a T_+ + b T_- + c T_4=0` exakt die Zielphasenrelation null. Damit liegt die Zielphase im Abschluss von `t -> (exp(-it E_j))`. Positive Zeiten genügen ebenfalls, da der Vorwärtshalbfluss in einer kompakten Gruppe denselben Abschluss besitzt.

Wichtig ist **kontinuierliche** Zeit: Es geht um Relationen `sum n_j E_j=0`, nicht um eine zusätzlich angenommene Unabhängigkeit der Energien modulo 2π. Die spätere rationale Zeitgitter-Suche approximiert einen kontinuierlichen Treffer; sie muss keinen neuen diskreten Kronecker-Satz behaupten.

Die Gruppenprämisse ist wesentlich. Spuren allein schließen zusätzliche einzelne Energiegleichheiten zwischen den Blöcken nicht aus. Solche Gleichheiten könnten den verlangten unterschiedlichen Blockphasen widersprechen, obwohl die dargestellte Trace-Identität weiter stimmt.

Die behauptete Goursat-Strategie braucht keine vollständige lineare Disjunktheit: Bei einem gemeinsamen Untergruppe-über-allen-Faktoren-Argument erzwingen die nicht passenden großen einfachen alternierenden Faktoren unabhängige A38- und A32-Wirkungen. Ihre Standarddarstellungen erzwingen konstante Relationskoeffizienten in den großen Blöcken; danach genügt die volle S4-Wirkung für den quartischen Block. Bei drei nichtverschwindenden rationalen Spuren bleiben zwei rationale Relationen und somit Rang 72. Das ist ein bedingter Gruppenbeweis, kein Ersatz für die fehlenden konkreten Polynomzertifikate.

Für r wirklich isolierte inaktive Kopien folgt `(r+1)η` durch Teleskopieren des Tensorprodukts unitärer Operatoren. Diese Normabschätzung gilt auch auf verschränkten Eingaben. Paarwahl, Schaltung der Kopplungen, präparierte Referenzen und das Ausbleiben weiterer unmodellierter Wechselwirkungen bleiben Teil des Gerätevertrags.

## 2. Warum die Zeitexponenten plausibel sind

Seien `m=74` und α die feste Energieliste. Gilt für nichtresonante ganzzahlige k

\[
 |k\cdot\alpha|\ge c(1+\|k\|)^{-\tau},
\]

so liefert ein glatter, kompakt getragener Testbuckel um die kompatible Zielphase die konservative Treffzeitschranke `T <= C η^{-(m+τ)}`. Man kann den Buckel als Autokorrelation wählen: Seine Fourierkoeffizienten sind nichtnegativ; die resonanten Zielphasenbeiträge sind daher nichtnegativ und enthalten einen Nullterm von Größenordnung η^m. Der zeitlich gemittelte nichtresonante Rest ist höchstens `C T^{-1} η^{-τ}`. Für ausreichend großes T bleibt eine positive mittlere Treffermasse.

- Im gemeinsamen Zahlenkörper mit Grad höchstens `D=38!32!4!` liefert das algebraische Normargument effektiv `τ=D-1`. Daraus entsteht genau `D+73`.
- Bei tatsächlich bewiesenem rationalem Rang 72 reduziert man auf 72 unabhängige algebraische Frequenzen. Die klassische lineare-Formen-Folgerung aus Schmidts Unterraumsatz liefert mit einem Zusatzexponenten eins `τ=72`, im Allgemeinen mit ineffektiver Konstante. Das ergibt konservativ `74+72=146`.
- Ein rationales Zeitgitter mit Abstand proportional zu η braucht bis zu einem solchen Treffer `O(η^-147)` Kandidaten. Feste algebraische Eigenwerte und computable Zielwinkel lassen sich mit zertifizierter Genauigkeit auswerten. Ein sauberer Suchalgorithmus verwendet einen Sicherheitsabstand, überspringt bei fester Präzision unentschiedene Randkandidaten und garantiert so, nicht an einer Gleichheitsentscheidung hängen zu bleiben.

Diese Rekonstruktion erklärt die Zahlen und bestätigt die Logik unter den Voraussetzungen. Sie ersetzt nicht die Prüfung der unzugänglichen Originalmanuskripte oder die Bestimmung ihrer Konstanten. Der unbekannte Wert von C_* verhindert einen nutzbaren garantierten Zeitplan, widerspricht aber nicht der asymptotischen Polynomialzeit eines terminierenden Suchalgorithmus für diese eine feste Quelle. Polynomial in `1/η` ist weiterhin nicht polynomial in der Bitlänge `log(1/η)` einer beliebig geforderten Genauigkeit.

Als Primärbezug wurde Schmidts Originalarbeit [Linear forms with algebraic coefficients I](https://doi.org/10.1016/0022-314X(71)90001-1) bibliographisch/über das Originalabstract geprüft. Die konkret verwendete lineare-Formen-Fassung und ihre Ineffektivität wurden zusätzlich in Evertses vom Autor bereitgestelltem Beweistext, Theorem 1.6 und Bemerkung nach Theorem 1.3, gelesen: [The Subspace Theorem](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-subspace.pdf). Das ursprüngliche Schmidt-Paper wurde nicht vollständig neu begutachtet.

## 3. Was der Shor-Anschluss voraussetzt

Die bekannte zustandsbasierte Hamiltonsimulation benötigt viele unabhängige Kopien der Softwarezustände; partielle Austausche realisieren die entsprechende lokale Entwicklung mit kontrolliertem Fehler. Das ist keine kostenlose Wiederverwendung verbrauchter Referenzen. Der hier vorgeschlagene gemeinsame Takt würde die **noch nicht verbrauchten** isolierten Kopien an Stufenenden wieder auf ihre Alterszustände bringen. Die bekannte Sample-Komplexität und die Gültigkeit auf verschränkten Eingaben sind in [Kimmel et al., Theorem 1](https://arxiv.org/pdf/1608.00281) explizit; Abschnitt 7 behandelt Universalisierung durch partielle Austausche und präparierte Zustände.

Ein partieller Swap mit einem Winkel, für den Sinus und Kosinus beide ungleich null sind, verschränkt orthogonale Produkteingaben. Zusammen mit verfügbaren lokalen Operationen greift die bekannte Universalitätsaussage [Brylinski–Brylinski, Theorem 1.3](https://arxiv.org/html/quant-ph/0108062v1). Der spezielle Nachweis, dass gerade die 13 genannten Altersquellen diese lokalen Operationen mit polynomialem Aufwand liefern, bleibt hier die nicht eingesehene Q016-Prämisse.

Wenn alle lokalen Synthesen, Referenzmengen, Paaradressierungen und Messungen polynomial skalieren, kann man bei polynomial vielen Gesamtaufrufen inverse polynomiale Einzelfehler wählen. Die Wartezeiten und ihre rationale Suche bleiben dann nach den bedingten Schranken ebenfalls polynomial. Damit ist der Anschluss an [Shors bekannten Quantenalgorithmus](https://arxiv.org/abs/quant-ph/9508027) logisch korrekt. Shors Exponentialpräzision einer vollständig ausgeschriebenen Fouriermatrix ist dafür nicht erforderlich; entscheidend ist ein ausreichend kleiner Gesamtfehler einer polynomial großen approximierenden Schaltung.

Nicht daraus abgeleitet sind reale stabile Hamiltonparameter über diese langen Zeiten, effizienter autonomer Schalterbau oder Fehlertoleranz. Schon ein Hamiltonfehler δH akkumuliert im Allgemeinen als `t ||δH||`; der ideale Zeitvertrag muss daher entsprechend präzise realisiert werden. Der Paste benennt idealen Gerätevertrag, fehlende praktische Pulse, fehlende Fehlertoleranz und fehlende Herkunft aus TFPT ausdrücklich. In dieser begrenzten Form ist seine Schlussfolgerung vertretbar.

**Für die verständliche Konsolidierung:** Ein sinnvoller mathematischer Synchronisationsmechanismus ist beschrieben und seine zentrale Zahlenidentität stimmt. Der vollständige Quellnachweis ist wegen der fehlenden Prüfpakete noch nicht unabhängig bestätigt. Selbst wenn er bestätigt wird, erhält man eine bedingte Konstruktion eines idealen Quantencomputers, der den bekannten Shor-Algorithmus ausführen könnte; noch keine praktisch verfügbare universelle Maschine und keinen gemeinsamen Beweis für TFPT, RH oder P=NP.

---

## RH und P versus NP

# Pro §7: RH und P versus NP im aktuellen gemeinsamen Stand

10. September 2026. Reiner Quellen- und Statusabgleich; keine neue
Kampagne, Registrierung oder Repositoryänderung.

Geprüfter Pro-Text:
 /Users/stefanhamann/.codex/attachments/32aeadc6-1536-4caa-8b43-67cb47b2fa6c/pasted-text.txt,
 Zeilen 509–550 (§7).

## Einfache Übersicht

| Aussage im neuen Pro-Text | Einordnung gegenüber unserem Stand |
|---|---|
| Positive Prozess-/Momentform ist noch keine signierte Weilform. | **Richtig und weiterhin offen.** Weder neue Dynamikschließung noch positive Norm liefern den arithmetischen Identitäts- und Positivitätsbeweis. |
| Der vollständige invers gewichtete Schalenvergleich ist nicht ausgerechnet. | **Richtig.** Unsere relative Gram-Fassung mit vollständigem Rest ist bewiesen, die tatsächliche neue Randgramrechnung bleibt offen. |
| Originaldaten und Beweisdateien zu W,M wurden dort nicht gefunden. | **Sessionspezifisches Hindernis, hier teilweise behoben.** Originalbeweise, eingefrorene Graph-/Antwortdaten und 80×80-Zertifikatmatrizen sind hier vorhanden. Die eindeutige Zuordnung und Verwendung im neuen Randvergleich ist damit noch nicht abgeschlossen. |
| Zum RH-Fortschritt ist nur die offene Randgramrechnung genannt. | **Als hiesiger Stand unvollständig.** Hinzugekommen ist der strenge Gegenzeuge gegen genau die konstante 7/10-Gate, einschließlich der Korrektur „Zertifikatsload ist nicht notwendig die echte Schurantwort“. |
| Alle kompakten glatten ungeraden Tests genügen für die gewählte RH-Route. | **Richtig mit genau diesen Quantoren und derselben ursprünglichen Weilform.** Ein einzelnes Fenster oder endlich viele Testvektoren genügen nicht. Keine pauschale Aussage über beliebige andere native Testklassen oder Quotienten. |
| SAT-Projektor hat Momentraumrang höchstens zwei; seine Antwort kann dennoch schwer zugänglich sein. | **Ergänzend und korrekt.** Die unbekannte Zahl p steckt bereits im ersten Moment. Eine kleine formale Darstellung beweist keine billige Auswertung. |
| Direkte Stichproben bei einer Lösung sind teuer, aber kein allgemeiner SAT-Laufzeitbeweis. | **Richtig.** Die Kosten gehören zu diesem Zugriffsmodell; strukturausnutzende Algorithmen sind dadurch nicht ausgeschlossen. |
| P versus NP wird nicht entschieden. | **Richtig.** Unser bestehender Gibbs-Mittelenergie-Satz formuliert den noch fehlenden deterministischen Auslesevertrag bereits genauer. |

## Was bei RH tatsächlich strenger geworden ist

Für das eingefrorene K und v=1_S F beweist unser rationaler Grad-19-Zeuge
\[
\frac{\langle v,Kv\rangle}{\|v\|^2}
\ge0.711512473774446293\ldots>0.7.
\]
Damit ist genau die konstante 7/10-Gate ausgeschlossen, einschließlich
jeder richtigen endlichen-plus-Rest-Oberprüfung desselben Operators.
Das ist stärker als der allein offene RH-Status in Pro §7. Der Zeuge
hat positive Weilenergie; er beweist weder RH noch eine negative
Weilrichtung und verwirft nicht alle konstanten Grenzen.

Weiterhin gilt: Ist A die tatsächliche alte verschobene Form und G ihr
unteres Zertifikat, dann A>=G und
\[
X^*G^{-1}X\ge X^*A^{-1}X.
\]
Der Vergleich mit der Zertifikatsload ist **hinreichend**. Seine
Notwendigkeit folgt nicht aus den gegebenen Prämissen. Die Pro-Formel
sollte deshalb als „gewählter hinreichender noch offener Anschluss“
gelesen werden, nicht als Äquivalenz zur ganzen Fensterpositivität.

Quellen:
- /Users/stefanhamann/Documents/Codex/2026-09-10/scha/outputs/RH-Strenger-Gegenzeuge-zur-07-Grenze.md, §§1 und 6–8.
- /Users/stefanhamann/Documents/Codex/2026-09-10/scha/work/fable-rh-continuation/independent-review.md.
- /Users/stefanhamann/Documents/Codex/2026-09-10/scha/work/rh-universal-audit/weighted_shell_lemma.md.
- /Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_shell_coupling_certificate_20260910/PROOF.md, §§1–3.

## Ungerade Tests: genau die richtige Reichweite

Die primär gegengeprüfte Aussage lautet: Nichtnegativität der
ursprünglichen Weilform auf **allen nichtnullen ungeraden**
\(v\in C_c^\infty(\mathbb R)\) impliziert RH.
Suzuki nennt hierfür Yoshida, Proposition 1:
[Weil’s quadratic form via the screw function, Version 2, Seite 2](https://arxiv.org/pdf/2606.09096v2).

Eine ausreichend weite Folge von Fenstern reicht daher, wenn in jedem
Fenster die Nichtnegativität auf der **ganzen dortigen ungeraden
glatten Testklasse** bewiesen wird: Jede kompakte Unterstützung liegt
irgendwann in einem solchen Fenster. Die Form und ihre Normalisierung
müssen dabei identisch bleiben. Werden stattdessen nur diskrete oder
endlichdimensionale Unterräume geprüft, sind Dichte und ein gültiger
Form-/Grenzübergang zusätzliche Pflichten. Eine von der Fenstergröße
unabhängige strikt positive Marge wird von diesem Kriterium nicht
verlangt. Für diese Route braucht es keine separate gerade Kampagne;
andere Darstellungen erhalten diese Testabdeckung nicht automatisch.

## W/M: hier vorhandene Daten, weiterhin offene neue Rechnung

Hier wurden direkt gelesen beziehungsweise als strukturierte
Originaldaten geprüft:

- /Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_odd_saturation_20260908/ASSEMBLY_PROOF.md:
  ursprünglicher Graph, tatsächliche dyadische Antwort Z0, ganze Wirkung,
  ursprüngliche Fehlerlast und 80×80-Matrixvergleiche.
- /Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_saturation_response_20260908/SATURATION_PROOF.md:
  vollständige inverse Antwort und ihre Residualidentitäten.
- /Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_odd_saturation_20260908/fast_state/initial.stdout
  und replay.stdout:
  JSON-Felder selection.graph, selection.response,
  products sowie result; eingefrorene dyadische Graph-/Antwortdaten.
- /Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_odd_saturation_20260908/fast_state/AUDIT.json:
  rekonstruierte lower/upper/inherited_lower-Matrizen von je 80×80.
- /Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research/rh_odd_saturation_20260908/WEIGHTED_FAST_RESULT.json
  und WEIGHTED_OUTPUT_COROLLARY.md:
  gespeicherte positive gewichtete Anfangs-/Replay-Entscheidungen für
  das alte Fenster und deren mathematische Reichweite.

Diese Dateien wurden nicht neu ausgeführt. Die Existenz und der
gespeicherte Status sind keine neue unabhängige Reproduktion.
ASSEMBLY_PROOF.md bezeichnet auch eine **gemischte Zwischenmatrix**
\(M=U^*\widetilde E\). Diese darf keinesfalls bloß wegen desselben
Buchstabens als positives M des späteren Schalenvergleichs eingesetzt
werden. Die Quelldaten sind wesentlich reichhaltiger als die Verweise
im PDF; die neue schalenbezogene Auswertung ist dennoch nicht erledigt.

## P versus NP: Ergänzung zum kleinen Momentraum

Für den SAT-Projektor Π und die uniforme Eingabe gilt Π²=Π,
M0=1 und Mk=p für k>=1. Der 2×2-Hankelblock ist
\[
\begin{pmatrix}1&p\\p&p\end{pmatrix},
\]
mit Determinante p(1-p). Der Rang ist höchstens zwei. Das bestätigt den
Pro-Kontrollfall, berechnet aber p nicht. Eine exakte Rang-/Momentantwort
darf nicht als kostenloses Orakel vorausgesetzt werden.

Unser bestehender, vollständig ausgeschriebener Satz benutzt stattdessen
den lokal beschriebenen Klauselverletzungs-Hamiltonian H_phi und
\[
k=n+\lceil\log_2\max(1,m)\rceil+3,\qquad
u_\varphi=\frac{\operatorname{Tr}(H_\varphi2^{-kH_\varphi})}
{\operatorname{Tr}(2^{-kH_\varphi})}.
\]
Es gilt \(0\le u_\varphi-E_0\le1/8\). Damit ist P=NP exakt äquivalent
zur uniformen deterministischen klassischen Polynomialzeit-Berechnung
von u_phi mit additivem Fehler höchstens 1/4.

In einer Richtung trennt der Schwellwert 1/2 erfüllbare und unerfüllbare
Formeln. In der anderen berechnet P=NP die minimale Zahl verletzter
Klauseln E0 durch NP-Entscheidungen und binäre Suche; E0 approximiert
u_phi schon auf 1/8. Weder eine exakte Partitionsfunktion noch der
gesamte Gibbszustand wird dafür verlangt. Dies ist ein bedingter
Auslesevertrag, kein Beweis seiner effizienten Realisierbarkeit.

Quellen:
- /Users/stefanhamann/Documents/Codex/2026-09-10/scha/work/complexity-universal-audit/reconstruction-and-computation.md, §§2–4.
- /Users/stefanhamann/Documents/Codex/2026-09-10/scha/outputs/Universalraum-RH-Faktorisierung-Komplexitaet.md, Abschnitt zur Mittelenergie.
- /Users/stefanhamann/Documents/Codex/2026-09-10/scha/outputs/Fable-Abgleich-und-TFPT-Dynamik-Fortsetzung.md, Schlussabschnitt.

Die Pro-Fortsetzung ergänzt diesen Satz um ein anschauliches
Kleinrang-Beispiel. Sie erfüllt den erforderlichen deterministischen
Auslese- und Gesamtkostenvertrag noch nicht. Eine bedingte
Quantenkompilierung von Shor wäre damit ebenfalls kein P=NP-Nachweis.

