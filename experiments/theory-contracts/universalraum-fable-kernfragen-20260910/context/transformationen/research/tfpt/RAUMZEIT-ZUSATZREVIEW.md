# Zusatzreview: relative Geometrie und Halbseiteninklusion

10. September 2026. Eng begrenzte Primärquellenprüfung und eine vollständig ausgeschriebene Zweipunktrechnung. Keine Änderung vorhandener Dateien, kein neuer TFPT-/TOE-Beweis.

## 1. Connes: die relative Lage trägt geometrische Information

[Connes, *On the spectral characterization of manifolds*, §12.1, Theorem 12.1 und Lemma 12.2](https://arxiv.org/pdf/0810.2088) bestätigt die vorgeschlagene Lesart: Das Spektrum von D allein bestimmt die Geometrie nicht. Hinzu kommt die relative unitäre Lage von D und der dargestellten beobachtbaren Algebra M. Der Text vergleicht ausdrücklich Spektrum plus Verknüpfungsmatrix mit Teilchenmassen plus CKM-/PMNS-Matrix. Das ist eine strukturelle Analogie, keine Herleitung bestimmter Mischungswinkel.

Theorem 12.1 rekonstruiert eine kompakte orientierte spinᶜ-Riemannsche Mannigfaltigkeit unter den starken Kompatibilitätsbedingungen (202)–(204), kommutativem M und vorgeschriebener Multiplizität. Dazu gehören Regularität/Ordnungsbedingung, geeigneter endlicher projektiver Modul samt Integrationsstruktur und antisymmetrische Orientierung. Der Text weist außerdem darauf hin, dass das bestimmte Hauptsymbol nicht den ganzen Diracoperator eindeutig auswählt.

Lemma 12.2 erhält im dortigen Kontext für den Kern von `exp(itD)` die Schranke

\[
\operatorname{supp}k_t\subset\{(x,y):d_D(x,y)\le|t|\},\quad
d_D(x,y)=\sup_{\|[D,h]\|\le1}|h(x)-h(y)|.
\]

Sein Beweis verwendet insbesondere die Ordnungs-eins-Bedingung. Die Aussage ist keine automatische Lorentz-, Gravitations- oder Kausalitätsrekonstruktion für beliebige endliche Matrizen.

## 2. Eigene vollständige Diagnose: gleiches Spektrum, verschiedene Abstände

Die dargestellte Algebra bleibt fest: `A=C²` wirkt diagonal auf `H=C²`. Für m>0 setze

\[
D_1=\begin{pmatrix}m&0\\0&-m\end{pmatrix},\qquad
D_2=\begin{pmatrix}0&m\\m&0\end{pmatrix}.
\]

Beide charakteristischen Polynome sind `λ²−m²`. Für `h=diag(a,b)`, a,b reell, gilt aber

\[
[D_1,h]=0,\qquad
[D_2,h]=m\begin{pmatrix}0&b-a\\a-b&0\end{pmatrix},
\quad \|[D_2,h]\|=m|a-b|.
\]

Deshalb ist der Abstand der beiden Auswertungszustände bei D1 unendlich: Jede Differenz ist zulässig. Bei D2 ist er exakt `1/m`: Die Normbedingung erzwingt diese obere Grenze, und etwa `a=1/m,b=0` erreicht sie.

Eine Hadamardrotation verwandelt D1 in D2, rotiert dabei aber auch die Algebra. In dieser Gegenprobe wurde die Algebra gerade festgehalten. Bewiesen ist damit die Bedeutung der relativen Lage, nicht die Inequivalenz einer gleichzeitig mitrotierten vollständigen Darstellung.

Die fehlende Mannigfaltigkeitsvoraussetzung lässt sich direkt sehen:

\[
[[D_2,h],h]=m(a-b)^2\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]

ist im Allgemeinen nicht null. Tatsächlich besitzt `exp(itD2)` den Nebendiagonaleintrag `i sin(mt)`, bereits für beliebig kleine positive Zeiten. Diese eigene Rechnung zeigt, warum man die endliche Abstandsformel nicht mit einer bewiesenen endlichen Signalausbreitung gleichsetzen darf. Sie ist keine Behauptung physischer Kausalität im Zweipunktmodell.

## 3. Araki–Zsidó: Vorzeichen, Domäne und Voraussetzungen stimmen

[Araki–Zsidó, *Extension of the structure theorem of Borchers and its application to half-sided modular inclusions*, Theorem 2.1](https://arxiv.org/pdf/math/0412061) setzt eine Inklusion N⊂M in kompatiblen Standarddarstellungen voraus. Das normale semifinite treue Gewicht φ auf M muss sich zu einem semifiniten Gewicht ψ auf N einschränken; beide modularen Operatoren gehören zu dieser gemeinsamen Situation.

Unter

\[
\Delta_M^{it}N\Delta_M^{-it}\subset N\quad(t\le0)
\]

ist der auf `Dom(log ΔN)∩Dom(log ΔM)` definierte Differenzoperator wesentlich selbstadjungiert. Seine selbstadjungierte Abschließung

\[
P=\overline{\frac{\log\Delta_N-\log\Delta_M}{2\pi}}\ge0
\]

liefert `U(s)=exp(isP)` und exakt

\[
\Delta_M^{-it}U(s)\Delta_M^{it}
=\Delta_N^{-it}U(s)\Delta_N^{it}
=U(e^{2\pi t}s).
\]

Das angefragte Vorzeichen ist richtig. Der Satz gibt außerdem `N=U(1)MU(1)*` und Halbseitenendomorphismen. Es handelt sich nicht um eine Positivitätsregel für beliebige Differenzen selbstadjungierter Operatoren oder Logarithmen positiver Matrizen. Gewicht, Standarddarstellung, Inklusion, Domänen und Halbseiteneigenschaft tragen die Aussage.

## 4. Präzises Forschungsziel für TFPT

Die zu prüfende gemeinsame Struktur wäre eine tatsächlich quellenbestimmte Familie beobachtbarer Algebren samt relativem Operatorstand und Zustand. Der geometrische Ansatz müsste die erforderlichen Rekonstruktionshypothesen aus dieser Quelle zeigen. Der modulare Ansatz müsste ein konkretes Paar N⊂M mit kompatiblem Zustand/Gewicht und der echten Halbseiteneigenschaft liefern. Für einen nichttrivialen Transport wäre zusätzlich P≠0 zu zeigen; die triviale Inklusion genügt dafür nicht.

Eine ganze 3+1D-Geometrie würde darüber hinaus kompatible weitere Richtungen, deren Beziehungen und eine physische Lokal-/Dynamikidentifikation benötigen. Zwei aus TFPT stammende gleichartige Spektren oder eine passende formale Differenz reichen als Nachweis nicht. Diese Präzisierung macht den nächsten Herkunftssatz prüfbar; sie schließt keine aktuelle TOE-Lücke selbst.

## Leseumfang

Connes: PDF-Seiten 54–56, §12.1 samt (202)–(204), Theorem 12.1, CKM/PMNS-Passage und §12.2/Lemma 12.2 vollständig; zusätzlich Einführung, fünf Hypothesen und Theorem 11.5 im gezielten Kontext. Araki–Zsidó: PDF-Seiten 7–8, vollständiger Satz 2.1, seine Standard-/Gewichtsvoraussetzungen sowie der anschließende Beweisüberblick. Die langen vorausgehenden Rekonstruktionsbeweise beziehungsweise der gesamte neunphasige Beweis von Satz 2.1 wurden nicht vollständig erneut überprüft. Die Zweipunktdiagnose oben ist eine eigene elementare Rechnung.
