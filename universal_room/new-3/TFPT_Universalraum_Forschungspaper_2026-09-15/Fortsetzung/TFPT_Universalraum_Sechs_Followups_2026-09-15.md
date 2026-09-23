---
title: "TFPT und Universalraum: sechs Forschungsfortsetzungen"
subtitle: "Optimale native Kodierung, gemischte Antwort und die Grenze der physikalischen Auswahl"
author: "Forschungssynthese und eigene Herleitungen · erstellt mit Codex"
date: "15. September 2026 · Fortsetzung 1.1"
lang: de-DE
---

# Zusammenfassung

Diese Arbeit bearbeitet alle sechs Folgeaufgaben des vorausgehenden Forschungspapers: Auswahl der Dynamik, native Referenz, physische Teilbereiche, gemischte Matrixmomente, geschützte Kodierung und konsistente Vergrößerung. Vier während der Rechnung nachgereichte Texte werden zusätzlich mit den aktuellen Quellen und Resultaten abgeglichen. Die Arbeit ist eine endliche, nichtarithmetische Fortsetzung. Sie enthält neue Konstruktionen und exakte Gegenbeispiele; eine vollständige physikalische Theorie wird nicht behauptet.

Der stärkste neue positive Befund ist ein **optimaler 15-dimensionaler Untercode** im vorhandenen Rang-60-Kodierer. Seine Basis besteht aus 15 vorzeichenbehafteten perfekten Paarungen der 64 Fermionmoden. Jede Paarung enthält 32 disjunkte Paare. Der Verlust einer beliebigen einzelnen Mode ist exakt korrigierbar, sofern deren Position bekannt ist. Eine Rangschranke beweist die Optimalität innerhalb des ursprünglichen hellen Codes. Zusammen mit den entsprechenden Bosonzuständen entsteht ein **30-dimensionaler, unter dem nativen Hamiltonoperator invarianter Unterraum**: Die 15 logischen Dimensionen bleiben bei der Paar-Boson-Umwandlung unverändert; die zweidimensionale Zusammensetzung ist ein eigener Freiheitsgrad. Auch bei dieser Umwandlung bleibt der logische Teil gegen einen einzelnen bekannten Modenverlust korrigierbar.

Der zweite neue Befund ist die vollständige gemischte Rückwirkung der dritten Bosonstufe auf die vier Singulett-Richtungen der zweiten Stufe. Sie wird als exakte 4×4-Matrix mit rationalen Einträgen berechnet. Ihr charakteristisches Polynom und ihre positiven Eigenwerte liefern eine konkrete Restkopplungsschranke. Ein zusätzlicher Spurnetzwerk-Rechner bestimmt gemischte Paarwort-Überlappungen und stimmt in nativen Vieroperator- sowie kleineren Sechsoperator-Beispielen exakt mit einer unabhängigen Besetzungsrechnung überein.

Drittens wird die stabile komplexe Hamiltonfamilie unter den ausdrücklich festgelegten, gleichförmigen kanonischen Transformationen klassifiziert. Nach Entfernung des Bosonpaarterms bleiben eine positive Bosonfrequenz und zwei nichtnegative kubische Kopplungen, außerdem die Fermionenergie. Stabilität und konsistente Zusammensetzung wählen ihre dimensionslosen Verhältnisse nicht aus.

Die Referenz- und Raumaufgaben liefern präzise Grenzen. Ein vorhandener nativer 35-Zustands-Übergang wird unabhängig einschließlich sämtlicher 60 Lie-Erzeuger geprüft; er ist ein bereits bekannter Ladungsausgleich, kein neu entdeckter Raumtransport. Die beiden ursprünglichen Kontrollen erzeugen weder Teilchen aus dem leeren Zustand noch frei adressierbare logische Operationen auf dem neuen Code. Eine exakte Folge unabhängig zusammengesetzter Codes ist konstruierbar; sie leitet keinen räumlichen Graphen und keine Raumdimension her. Alle sechs Richtungen sind damit konkret bearbeitet, während ihre globalen physikalischen Abschlussfragen offen bleiben.

# 1. Umfang, Quellen und Status der sechs Aufgaben

## 1.1 Gemeinsamer Modellvertrag

Der native Ausgangspunkt bleibt

$$H=\Delta N_b+g(T_++T_-),\qquad
T_+=\sum_A b_A^\dagger P_A,\qquad T_-=T_+^\dagger,$$

$$P_A=\sum_{i<j}W_{A,ij}f_jf_i,\qquad
N=N_f+2N_b,\qquad WW^\dagger=8I_{60}.$$

Es gibt 64 Fermionmoden, 60 Bosonmoden und 480 von null verschiedene Tensorstellen. Die innere Gruppe ist $\mathsf G=\mathrm{Spin}(10)\times SU(4)$. Die Tensorquelle ist unverändert und durch denselben SHA-256 wie im Hauptpaper gesichert. Mit $\hbar=1$ sind Zeiten in inversen Energieeinheiten angegeben.

Die Rechnungen verwenden verschiedene ausdrücklich benannte Zustandsverträge. Die Kodierung liegt im Sektor $N=2$, der nachgerechnete Referenzübergang in $N=3$, die Singulett-Matrixmomente auf der gefüllten Referenz $F$ in $N=64$. Diese Sektoren gehören zu demselben nativen Hamiltonoperator. Sie sind damit noch nicht aus einer einzigen physisch hergeleiteten Präparation zugänglich.

## 1.2 Ergebnisübersicht

| Folgeaufgabe | Tatsächlich erreicht | Verbleibende physikalische Frage |
|---|---|---|
| 1. Dynamik auswählen | Stabile komplexe Normalform; expliziter Gegenbeleg gegen eindeutige Auswahl durch Stabilität und Zusammensetzbarkeit | Herkunft der verbleibenden Parameter und der Zustandsregel |
| 2. Native Referenz | Unabhängiger 35D-Replay mit vollständiger Lie-Kovarianz; Präparations- und Auslesegrenze konkretisiert | Erzeugung und Messung der Referenz aus ursprünglichen Instrumenten |
| 3. Physische Teile | Kontrollalgebra und Zwischenstufen geprüft; zugelassene Wirkung von bloßen Labels getrennt | Native unabhängig adressierbare Teile und deren räumliche Bedeutung |
| 4. Matrixmomente | Vollständige 4×4-Kontraktion; gemischter Wick-Rechner; exakte Restnorm und 10D-Kompression | Höhere Blöcke und ausreichend scharfe spektrale Restkontrolle |
| 5. Geschützte Kodierung | Optimaler 15D-Untercode; explizite Decoder; nativer invarianter 30D-Unterraum | Physische Kodierung, Korrektur und zugängliche logische Operationen |
| 6. Größenfolge | Exakte bedingte Produktfolge; Gegenbeispiel zur geschlossenen reduzierten Dynamik | Ursprüngliche Kopplungsregel, wechselwirkender Grenzwert und Raumzeit |

Die Worte „bearbeitet“ und „exakt“ beziehen sich jeweils auf diese konkreten Gegenstände. Eine noch fehlende globale Ableitung wird nicht durch einen endlichen Prüflauf ersetzt. Standardmethoden werden auf den nativen Tensor angewandt; „neu“ bezeichnet neue Rechnungen dieser Fortsetzung gegenüber den ausgewerteten Quellen, keinen weltweit geprüften Prioritätsanspruch.

# 2. Folgeaufgabe 1: stabile komplexe Dynamik in Normalform

## 2.1 Die vollständige betrachtete Polynomialklasse

Die jüngste Quelle R1 klassifiziert bereits die $\mathsf G$-invarianten, fermionparitätsgeraden, normalgeordneten Polynome bis Grad drei am unveränderten Träger. Mit einer reellen symmetrischen invarianten Bosonpaarung $\eta$, $\eta^2=I$, lautet die Familie

$$\begin{aligned}
H_{\rm ext}={}&c_0+\varepsilon N_f+\Delta N_b
+\frac12\big(\kappa b^\dagger\eta b^\dagger+
\bar\kappa b\eta b\big)\\
&+g\,b^\dagger P+\bar g\,P^\dagger b
+\lambda b^\dagger\eta P^\dagger+\bar\lambda P\eta b.
\end{aligned}$$

Die Koeffizienten $g,\lambda,\kappa$ dürfen jetzt komplex sein. Der nachfolgende Satz gilt im strikt stabilen Bosonbereich $\Delta>|\kappa|$. Er klassifiziert die Familie unter gleichförmigen, $\mathsf G$-verträglichen linearen Boson-Bogoliubov-Transformationen und globalen Fermion-/Bosonphasen. Nichtlineare Transformationen, ein Austausch des festgehaltenen inneren Darstellungsvertrags oder größere Polynomialklassen werden nicht mitklassifiziert.

## 2.2 Satz: drei dimensionslose Parameter bleiben

Setze

$$\omega_b=\sqrt{\Delta^2-|\kappa|^2}>0,\qquad
U=|g|^2-|\lambda|^2,$$

$$K=\Delta(|g|^2+|\lambda|^2)
-2\operatorname{Re}(\bar\kappa g\lambda).$$

Dann besitzt jede betrachtete stabile Hamiltonfunktion eine Normalform

$$H_{\rm can}=c'_0+\varepsilon N_f+\omega_b N_c
+g_c(c^\dagger P+P^\dagger c)
+\lambda_c(c^\dagger\eta P^\dagger+P\eta c),$$

wobei

$$\boxed{g_c^2=\frac{K/\omega_b+U}{2},\qquad
\lambda_c^2=\frac{K/\omega_b-U}{2},\qquad
 g_c,\lambda_c\ge0.}$$

Der konstante Energieversatz ist

$$c'_0=c_0+30(\omega_b-\Delta).$$

Nach Wahl der Energieeinheit verbleiben also insbesondere

$$\varepsilon/\omega_b,\qquad g_c/\omega_b,
\qquad\lambda_c/\omega_b.$$

**Herleitung.** Für $\kappa=|\kappa|e^{i\phi}$ setze

$$b=c\cosh r-e^{i\phi}\eta c^\dagger\sinh r,
\qquad\tanh2r=|\kappa|/\Delta.$$

Die kanonischen Kommutatoren bleiben erhalten. Der Bosonpaarterm verschwindet; die positive Frequenz ist $\omega_b$. Mit $u=\cosh r$, $v=-e^{i\phi}\sinh r$ werden die kubischen Koeffizienten

$$g'=ug+v\bar\lambda,\qquad
\lambda'=u\lambda+v\bar g.$$

Direktes Ausmultiplizieren ergibt

$$|g'|^2-|\lambda'|^2=U,\qquad
|g'|^2+|\lambda'|^2=K/\omega_b.$$

Die verbleibenden beiden globalen Phasen wirken auf die Phasen von $g'$ und $\lambda'$ mit einer 2×2-Matrix der Determinante vier. Beide Koeffizienten können deshalb gleichzeitig nichtnegativ gewählt werden. Die positive bosonische Normalform ist innerhalb der genannten Transformationen bis auf diese Phasen festgelegt. Für $\kappa=0$ wird $r=0$ genommen. $\square$

Dies erweitert den reellen Reduktionstest aus R1. Der dortige Ausdruck $\kappa(g^2+\lambda^2)-2\Delta g\lambda$ bleibt für seine reelle Teilklasse nützlich. In der komplexen Klasse sind die normalisierten Beträge die einfacheren Kennzahlen. Eine Entfernung des zusätzlichen kubischen Kanals verlangt $\lambda_c=0$; seine bloße Symmetrieverträglichkeit entscheidet das nicht. Methodischer Hintergrund zur Bosondiagonalisierung ist E3.

## 2.3 Zwei exakte Phasenbeispiele

Für $\Delta=5$, $\kappa=3$, $g=1+i$, $\lambda=2-i$ erhält man

$$\omega_b=4,\qquad g_c^2=5/8,\qquad\lambda_c^2=29/8.$$

Bei gleichem $\Delta,g,\lambda$, aber $\kappa=3i$, ergibt sich dagegen

$$\omega_b=4,\qquad g_c^2=17/8,\qquad\lambda_c^2=41/8.$$

Die relative Phase ist somit in der ursprünglichen Beschreibung physikalisch relevant: Sie verändert die kanonischen Beträge. Beide Beispiele wurden ohne numerische Näherung geprüft.

Eine kanonische Umbenennung definiert nur dann denselben vollständigen Prozess, wenn Zustand und Messoperatoren mittransformiert werden. Das alte Bosonvakuum ist nach einer nichttrivialen Squeezing-Transformation nicht einfach das neue Vakuum. Eine Auswahl bestimmter Anfangs- oder Messzustände kann deshalb zusätzliche Unterscheidungen festlegen.

## 2.4 Warum Stabilität und Zusammensetzung nicht eindeutig auswählen

In der Normalform kann man die linearen Bosonkopplungen quadratisch ergänzen. Da jeder $P_A$ aus acht beschränkten Paaroperatoren besteht, gilt konservativ $\|P_A\|\le8$. Damit folgt beispielsweise

$$H_{\rm can}\ge c'_0+64\min(\varepsilon,0)
-\frac{3840(g_c+\lambda_c)^2}{\omega_b}.$$

Die grobe Schranke beweist untere Beschränktheit im angegebenen Bereich; sie liefert keine ausgewählte Kopplung und keinen Eindeutigkeitssatz für den Grundzustand.

Schon die native Teilfamilie $\lambda_c=0$, $\varepsilon=0$ enthält die beiden stabilen Verhältnisse $g_c/\omega_b=1/20$ und $1/40$. Auf dem ausdrücklich zugelassenen Eingang $F$ unterscheiden sie sich durch

$$\frac{\mu_4\mu_2}{\mu_3^2}
=1+1396(g_c/\omega_b)^2,$$

also durch $4.49$ gegenüber $1.8725$. Für beide kann man unabhängig zusammengesetzte größere Systeme definieren. Stabilität, innere Symmetrie und solche Kompositionskonsistenz reichen deshalb nicht zur eindeutigen Auswahl. Das Gegenbeispiel widerlegt keine zusätzliche, künftig begründete Ursprungsregel.

# 3. Folgeaufgabe 2: Referenz, Ladungsausgleich und die erste fehlende Operation

## 3.1 Ein bereits vorhandener nativer Übergang unabhängig geprüft

Die Quellen R2/R3 enthalten einen Übergang im unveränderten $N=3$-Sektor:

$$|b_{36},f_4\rangle\longrightarrow
|f_0f_4f_{57}\rangle\longrightarrow|b_0,f_0\rangle.$$

Die neue Rechnung konstruiert aus W und den CAR-Vorzeichen sämtliche von diesem Eingang erreichbaren Zustände. Die abgeschlossene Komponente hat genau 35 Dimensionen: fünf Boson-Fermion-Zustände und 30 Dreifermion-Zustände. Für die Konversionsmatrix $C$ gilt

$$\operatorname{spec}(CC^\dagger)=\{7,7,7,7,12\}.$$

Das konkrete Endpunktmatrixelement ist

$$\langle b_0,f_0|X^2|b_{36},f_4\rangle=-1,$$

also beginnt die Übergangsamplitude mit $g^2t^2/2$. Die Rechnung bestätigt alle acht Cartanladungen auf jedem Pfad und zusätzlich die Kovarianz des tatsächlichen W unter allen 45+15 Lie-Erzeugern. Die zugrunde liegende volle Dynamik ist daher innerlich symmetrieverträglich. Die einzelne feste Gewichtskomponente muss selbst kein unter der ganzen Gruppe invarianter Teilraum sein.

Dies ist ein **unabhängiger Replay eines bekannten Ergebnisses**. Er zeigt, dass die native Bosonbelegung einen Fermionlabelwechsel begleiten kann. Er identifiziert die beiden Labels nicht mit Orten. Der Eingang und eine Auslesung der konkreten Ausgangsmoden bleiben Ressourcen.

## 3.2 Ein scharfer Präparationsausschluss

Auf dem leeren Zustand gilt

$$X|0\rangle=0,\qquad N_b|0\rangle=0.$$

Jedes Wort aus diesen beiden Operatoren wirkt auf dem Vakuum skalar oder verschwindet. Auch Zeitfolgen von Hamiltonoperatoren, die ausschließlich daraus gebildet sind, verlassen den Vakuumstrahl nicht. Daher kann dieses enge Alphabet weder den obigen $N=3$-Eingang noch die gefüllte $N=64$-Referenz erzeugen.

Der Schluss gilt für diesen Anfangszustand und diesen Operationssatz. In der Z4-Erweiterung können zusätzliche Terme auf dem Vakuum wirken; deren ursprüngliche Verfügbarkeit ist gerade eine offene Auswahlfrage. Ebenso würde eine externe Teilchenquelle den Vertrag erweitern.

## 3.3 Was eine tatsächlich verfügbare Messung zusätzlich leisten würde

Im nativen hellen $N=2$-Raum ist die Dynamik

$$h_2=\begin{pmatrix}0&\sqrt8g\\\sqrt8g&\Delta\end{pmatrix}$$

für alle 60 inneren Zustände gleich. Bei $g/\Delta=1/20$ erreicht die Paar-Boson-Konversion die maximale Wahrscheinlichkeit $p=2/27$. Eine **zusätzlich gewährte**, kohärenzerhaltende Messung nur der Bosonzahl kann Erfolg und Misserfolg unterscheiden, ohne das innere Label aufzuzeichnen.

Im Erfolgszweig wird die gesamte innere Quantenzustandsinformation konvertiert; im Misserfolgszweig bleibt sie bis auf eine skalare Amplitude erhalten. Bei idealer wiederholter Messung und erneutem optimalem Zeitintervall beträgt die mittlere Versuchszahl $1/p=27/2$. Dieser mathematische Instrumentenvertrag schließt seine Wahrscheinlichkeiten und die Fehlversuche ein. Der dazu erforderliche Detektor, seine Zeitsteuerung und seine Aufzeichnung wurden nicht aus $X,N_b$ konstruiert.

Genau dies ist die erste fehlende physische Verbindung: Ein Operator, dessen Algebra bekannt ist, ist noch kein aus derselben Quelle gebautes Messgerät.

# 4. Folgeaufgabe 3: Was als unabhängiger Teil zugänglich ist

## 4.1 Der neue Code trägt logische Unterschiede, die die alten Kontrollen nicht bewegen

Im hellen $N=2$-Sektor erzeugen Konversion und Bosonzahl

$$\mathcal A_{\rm hell}=M_2(\mathbb C)\otimes I_{60}.$$

Die erste Komponente verändert die Zusammensetzung „Paar oder Boson“. Die zweite bezeichnet den inneren Zustand. Die ursprünglichen beiden Kontrollen erzeugen darauf keine beliebige innere Rotation.

Der in Abschnitt 6 konstruierte geschützte Bereich reduziert dies auf $M_2\otimes I_{15}$. Die native Dynamik kann die Zusammensetzung ändern und zugleich 15 logische Dimensionen erhalten. Eine Operation, die diese logische Information gezielt verarbeitet oder zu einem anderen räumlichen Teil überträgt, ist dadurch nicht gewonnen.

Das ist eine konkrete Unterscheidung zwischen **gespeicherter Information**, **zugänglicher Information** und **steuerbarer Information**. Ein großer Kommutant kann unzugängliche Unterschiede enthalten. Seine Dimension ist keine Anzahl bereits verfügbarer Orte.

## 4.2 Die Operationsfreiheit ist keine universelle Ja/Nein-Frage

Die nachgereichten Texte U1/U2 formulieren eine zu starke Dichotomie: volle Symmetrie als Handgriff verfügbar oder keinerlei Zwischenfortschritt. R4 hatte diese Behauptung bereits korrigiert. Hier wurde die Korrektur in einer treuen kleinen rationalen Darstellung erneut nachgerechnet:

| Hinzugefügter Operationsvertrag im N=3-Sektor | Algebra-Dimension |
|---|---:|
| Nur $X,N_b$ | 14 |
| Zusätzlich ein Projektor, der einen der drei dunklen Typen abtrennt | 15 |
| Zusätzlich bereits **ein** getrennter Spin-Casimir | 16 |

Die Spin-Casimirwerte der drei dunklen Typen sind in der gemeinsamen Vierfachnormierung $165,141,117$. Ein einzelner Operator mit diesen drei verschiedenen Werten unterscheidet alle drei Typen. Die Summe aus Spin- und Farbcasimir ist dagegen jeweils 180.

Die zwei fehlenden Algebradimensionen bedeuten daher nicht zwei zwingend fehlende physische Messgeräte. Umgekehrt reduziert das Hinzufügen eines Casimirs den vollständigen Kommutanten nicht schon auf sieben. Sieben gilt für den stärkeren Vertrag mit der gesamten inneren Gruppe zusammen mit $X,N_b$. Eine erhaltene Symmetrie, eine aktive Symmetrieoperation und eine Casimirmessung sind verschiedene Voraussetzungen.

## 4.3 Wirkungstest und räumliche Bedeutung

Für tatsächlich unabhängig zugängliche Teile A und B ist eine geeignete Größe

$$\delta_{A\to B}(t)=\operatorname{tr}\big[B U_t\mathcal E_A(\rho)U_t^\dagger\big]
-\operatorname{tr}\big[B U_t\rho U_t^\dagger\big],$$

wobei $\mathcal E_A$ ein verfügbares lokales spurtreues Instrument sein muss. Die beiden Ausführungen beginnen mit demselben Zustand. Eine Korrelation allein misst diesen Einfluss nicht.

Bei zwei ausdrücklich kopierten Banken mit zusätzlich eingesetzter Bosonkopplung entsteht der bereits bekannte Viererblock. Sein Endpunkt erfüllt $(H_4^3)_{4,1}=a^2J$, $a=\sqrt8g$. Für $J=0$ zerfällt er in zwei getrennte Blöcke. Die neue symbolische Prüfung bestätigt somit zugleich den Übergang und die Abhängigkeit von der eingesetzten Verbindung. Aus voneinander unabhängigen lokalen Hamiltonfolgen entsteht diese Kopplung nicht von selbst.

Der Erfolg dieser Folgeaufgabe ist ein genau lokalisierter Ursprungstest: Welche ursprüngliche Operation koppelt welche unabhängig zugänglichen Teile? Die vorliegenden nativen Spektren und Kontrollalgebren beantworten ihn noch nicht.

# 5. Folgeaufgabe 4: gemischte Matrixmomente tatsächlich berechnet

## 5.1 Vier Richtungen statt einer skalaren Leiter

Auf der gefüllten Referenz F im Sektor $N=64$ definiere $v_2=T_+^2F$. Die Quellen R1 bestimmen vier orthogonale Projektionen

$$v_R=P_Rv_2,\quad
R=(54,1),(1,20'),(54,20'),(45,15).$$

Ihre exakten Normquadrate sind

$$D=\operatorname{diag}(17280,7680,241920,172800).$$

Die neue Rechnung stellt diese vier Vektoren einschließlich aller Bosonfaktoren gemeinsam dar. Ihre vereinigte Besetzungsliste hat 306720 von null verschiedene Konfigurationen. Die Summe ist exakt der ursprüngliche $v_2$; sämtliche Kreuzskalarprodukte verschwinden.

## 5.2 Die neue vollständige Rückwirkungsmatrix

Setze

$$y_R=T_+v_R,\qquad u_R=T_-T_+v_R,\qquad
M_{RS}=\langle v_R,u_S\rangle.$$

Die Rechnung bildet die dritte Bosonstufe nicht als vollständigen Zustandsvektor ab. Sie kontrahiert jeden erlaubten Hin- und Rückweg direkt und erhält den folgenden Koeffizientenoperator:

$$\boxed{C=D^{-1}M=
\begin{pmatrix}
480&16&504&320\\
36&468&504&324\\
36&16&906&344\\
32&72/5&2408/5&786
\end{pmatrix}.}$$

C ist in dieser unnormierten Basis nicht euklidisch symmetrisch. Es gilt $DC=C^TD=M$. Der physische hermitesche Operator in der orthonormalen Basis ist $D^{1/2}CD^{-1/2}$.

**Vollständigkeitsprüfung der Kontraktion.** Die Rechnung bestimmt zusätzlich $U_{RS}=\langle u_R,u_S\rangle$ und bestätigt exakt

$$\boxed{U-M^TD^{-1}M=0.}$$

Die linke Seite ist die Gram-Matrix der außerhalb des Viererraums verbleibenden Reste. Ihre Nullheit beweist daher, dass jede kontrahierte Rückwirkung wirklich im vollständigen zweiten Singulettniveau schließt. Das bedeutet nicht, dass die Hamiltonentwicklung dort schließt: $T_+v_R$ liegt auf der dritten Bosonstufe.

Die Kontrollsummen reproduzieren unabhängig

$$\sum_{R,S}M_{RS}=575078400,$$

$$\sum_{R,S}U_{RS}=752194252800,$$

sowie die bekannte transversale Norm $5001523200/229$. Die C++-Rechnung wurde mit und ohne Optimierung ausgeführt; die Ergebnisse sind byteidentisch. Konservative Zählschranken schließen Ganzzahlüberlauf sowohl in den Zustandskoeffizienten als auch in den Gram-Akkumulatoren aus.

![Die vier Richtungen sind dynamisch gekoppelt. Die Heatmap zeigt die normalisierte hermitesche Matrix; die Dezimalzahlen in dieser Abbildung dienen der Darstellung. Die zugrunde liegende Matrix und ihr Polynom sind exakt.](figures/matrixmomente.pdf)

## 5.3 Spektrum und eine genaue Restkopplung

Das charakteristische Polynom von C lautet

$$\begin{aligned}
p(z)={}&z^4-2640z^3+2333412z^2\\
&-860650512z+114340723200.
\end{aligned}$$

Alle vier Eigenwerte sind positiv und einfach. Numerisch liegen sie bei

$$426.40581894,\quad448.75175917,\quad456.83834641,
\quad1308.00407548.$$

Rationale Sturm-Intervalle befinden sich im Prüfpaket. Insbesondere ist $\lambda_{\max}<1309$ exakt zertifiziert. Es gibt vier unabhängige ausgehende Richtungen auf der dritten Stufe.

Sei P die orthogonale Projektion auf den vollständigen sechsdimensionalen Singulettbereich mit Bosonzahl bis zwei. Die ausgelassene Kopplung $R=(I-P)HP$ erfüllt exakt

$$\boxed{\|R\|^2=g^2\lambda_{\max}(C)<1309g^2.}$$

Die früher abstrakte Restnorm ist damit am nativen Tensor bestimmt. Für $\operatorname{Im}z=\eta_z\ne0$ folgt beispielsweise

$$\|P(z-H)^{-1}P-(z-PHP)^{-1}\|
\le\frac{1309g^2}{|\eta_z|^3}.$$

Die zweite Resolvente ist auf dem P-Raum zu verstehen. Nahe der reellen Achse ist diese allgemeine Schranke grob. Sie ist kein Ersatz für einen isolierten Polnachweis oder eine genaue Grundenergie.

## 5.4 Zehndimensionale Kompression und ehrlicher Vergleich

Die Zustände $F,v_1,v_R,y_R$ spannen einen zehndimensionalen Raum. Sein vollständiger Gramoperator und seine Hamiltonkompression sind rational bestimmbar. Die ersten acht Energiemomente von F stimmen exakt mit der unabhängigen skalaren Rechnung überein.

Bei $g/\Delta=1/20$ liegt der kleinste Ritz-Wert zwischen

$$-1531138/1399281\quad\text{und}\quad-1562781/1428199,$$

also ungefähr bei $-1.0942319663\,\Delta$. Dies verbessert die viergliedrige skalare Kompression geringfügig. Die bereits bekannte fünfgliedrige H-Lanczos-Kompression erreicht jedoch etwa $-1.1296381239\,\Delta$ und bleibt die stärkere der hier verglichenen Energieobergrenzen. Ein größerer Kompressionsraum ist nur dann automatisch besser, wenn er den anderen Raum enthält; hier sind die Räume verschieden.

Der Gewinn der neuen Rechnung ist die gemeinsame Richtungs- und Restinformation. Die gute ältere Energiegrenze wird nicht durch eine schwächere neue Zahl ersetzt.

## 5.5 Ein wiederverwendbarer gemischter Spurnetzwerk-Rechner

Für antisymmetrische Paarmatrizen A und B ist der formale Überlappungskern um den Ursprung

$$\mathcal Z(A,B)=\exp\left[
\frac12\sum_{n\ge1}\frac{(-1)^{n+1}}n
\operatorname{tr}\big((A^\dagger B)^n\big)\right].$$

Er entspricht der bei eins beginnenden formalen Quadratwurzel von $\det(I+A^\dagger B)$. Setzt man $A=\sum_i x_iA_i$ und $B=\sum_j y_jB_j$, liefern die gemischten Koeffizienten die Überlappungen der entsprechenden Paarwörter. Die linkseitigen Variablen werden dabei als formale Bra-Variablen behandelt. Die Entwicklung um eins fixiert die lokale Vorzeichenwahl; sie beansprucht keine globale numerische Wurzelwahl über beliebige geschlossene Parameterwege. Pfaffianmethoden behandeln solche Vorzeichenfragen systematisch. [E4]

Der neue Rechner speichert nur quadratfreie Monome der benötigten Variablen. Er führt Matrixprodukte entlang der Spurnetzwerke und anschließend die skalare Exponentialkombination aus. Für die hier tatsächlich implementierten reellen ganzzahligen Paarmatrizen wurden 32 native Vieroperator-Überlappungen und zwölf gemischte Sechsoperator-Überlappungen auf acht Moden mit einer unabhängigen Fock-Besetzungsrechnung verglichen. Darunter sind nichtverschwindende Interferenz- und Nullkontrollen; alle Vergleiche sind exakt.

Damit ist ein ausführbarer Anfang der vorgeschlagenen Fortsetzung vorhanden. Die vollständige native Sechsoperator-Projektorrechnung, beliebige Observableinschübe und alle höheren Bosonstufen sind dadurch nicht bereits berechnet.

# 6. Folgeaufgabe 5: ein optimaler geschützter nativer Code

## 6.1 Vom Rang-60-Kodierer zum Untercode

Wie bisher ist

$$V=W^\dagger/\sqrt8:\mathbb C^{60}\to\Lambda^2\mathbb C^{64}$$

eine Isometrie. Der gesamte 60er-Code korrigiert eine einzelne Modenlöschung nicht, denn $V^\dagger n_rV$ besitzt die Eigenwerte $0$ und $1/8$ mit Vielfachheiten 45 und 15.

Die neue Konstruktion nutzt die native Beschriftung $\mathbb C^{60}\simeq\mathbb C^{10}\otimes\mathbb C^6$. Paare entgegengesetzter Vektorlabels sind $(k,k+5)$, $k=0,\ldots,4$. Die sechs Farbpaare werden in die drei perfekten Paarungen der vier Farben zerlegt:

$$m_0=\{01,23\},\qquad m_1=\{02,13\},\qquad
m_2=\{03,12\}.$$

Für jedes k und jedes $m_a=\{p_a,\bar p_a\}$ definiere

$$C|k,a\rangle=\frac12\big(
|k,p_a\rangle+|k,\bar p_a\rangle+
|k+5,p_a\rangle+|k+5,\bar p_a\rangle\big).$$

Die 15 Vierergruppen sind disjunkt und erschöpfen die 60 Labels. Daher gilt $C^\dagger C=I_{15}$. Der physische Paarencoder ist $Q=VC$.

## 6.2 Eine anschauliche Graphbeschreibung

Jede der 15 Spalten von Q besteht aus genau 32 Fermionpaaren mit Amplituden $\pm1/\sqrt{32}$. Jede der 64 Moden tritt darin genau einmal auf. Somit ist jede Spalte eine vorzeichenbehaftete perfekte Paarung der Moden. Die 15 Paarungen sind kantendisjunkt und zerlegen sämtliche 480 Kanten des nativen 15-regulären Graphen.

Für einen bekannten verlorenen Modus r besitzt jede Paarung genau einen Partner. Die 15 Partner sind verschieden. Im besetzten Verlustzweig bleibt deshalb für jedes logische Basislabel ein anderer orthogonaler Einteilchenzustand übrig. Genau diese Partnerstruktur trägt die rekonstruierbare Information.

Die Datei `Kodierung_15_Kanaele.csv` listet alle 480 Paare, ihre Kanalzuordnung und ihre tatsächlichen Vorzeichen auf.

![Nach Verlust einer bekannten Mode bleibt im besetzten Zweig einer von 15 verschiedenen Partnerzuständen. Die Abbildung verwendet die tatsächlichen Partner der nativen Mode 0. Für Superpositionen erfolgt die Rückabbildung kohärent.](figures/code15_partner.pdf)

## 6.3 Exakter Korrektursatz und Decoder

Für jede Mode $r=0,\ldots,63$ gilt

$$\boxed{Q^\dagger n_rQ=\frac1{32}I_{15}.}$$

Wegen der festen Fermionzahl zwei verschwinden außerdem die Codekompressionen von $f_r$ und $f_r^\dagger$. Die Umgebung erhält bei Verlust dieser einzelnen Mode deshalb keine Information über den logischen Zustand. Dies ist die Knill–Laflamme-Bedingung für den angegebenen Erasure-Vertrag. [E1]

Die Decoder können direkt angegeben werden. Nach Entfernen der Mode seien $A_{0,r}$ und $A_{1,r}$ die beiden verbleibenden Amplitudenabbildungen für „Mode leer“ und „Mode besetzt“. Dann

$$A_{0,r}^\dagger A_{0,r}=\frac{31}{32}I_{15},\qquad
A_{1,r}^\dagger A_{1,r}=\frac1{32}I_{15}.$$

Ihre Ausgänge liegen in verschiedenen verbleibenden Teilchenzahlsektoren. Die normalisierten Isometrien

$$\widetilde A_{0,r}=\sqrt{32/31}\,A_{0,r},\qquad
\widetilde A_{1,r}=\sqrt{32}\,A_{1,r}$$

haben orthogonale Bilder. Eine Recovery verwendet deren Adjungierte auf den beiden Bildern und ergänzt außerhalb des Fehlerbilds einen beliebigen spurtreuen Kanal. Auf jedem kodierten Zustand, auch bei Verschränkung mit einer externen Referenz, ist die wiederhergestellte logische Abbildung exakt die Identität. Der besetzte Zweig hat Wahrscheinlichkeit $1/32$, der leere $31/32$; beide tragen dieselbe logische Information.

Es handelt sich um den Verlust einer **bekannten Fermionmode** mit der entsprechenden CAR-kompatiblen Teilung. Die fermionischen Vorzeichen werden in der Konstruktion und im Decoder geführt. Ein stiller Wechsel zu einer anderen Tensorfaktor-Konvention ist nicht Teil des Beweises.

## 6.4 Optimalität innerhalb des ursprünglichen hellen Codes

Sei $C_K:\mathbb C^K\to\mathbb C^{60}$ irgendein Untercode, der jede bekannte einzelne Modenlöschung korrigiert. Dann muss

$$C_K^\dagger(V^\dagger n_rV)C_K=c_r I_K$$

gelten. Da $\sum_rV^\dagger n_rV=2I_{60}$, ist $\sum_rc_r=2$. Für mindestens ein r gilt somit $c_r>0$. Dessen komprimierter Operator hat Rang K, während $V^\dagger n_rV$ Rang 15 besitzt. Also

$$\boxed{K\le15.}$$

Die explizite Konstruktion erreicht diese Grenze. Sie ist daher innerhalb des nativen hellen Paarcodes optimal. Das ist keine Schranke für beliebige Codes auf dem gesamten Fermion-Fockraum oder für andere Fehlerverträge.

## 6.5 Ein nativer invarianter 30-dimensionaler Unterraum

Ergänze zu den Paarzuständen $Q|\alpha\rangle$ die Bosonzustände

$$|B,\alpha\rangle=\sum_A C_{A\alpha}b_A^\dagger|0\rangle.$$

Wegen $WW^\dagger=8I$ gilt auf dem gemeinsamen Raum

$$\boxed{H|_{\mathcal K_{30}}
=\begin{pmatrix}0&\sqrt8g\\\sqrt8g&\Delta\end{pmatrix}
\otimes I_{15}.}$$

Dieser 30-dimensionale Raum ist unter dem unveränderten nativen H exakt invariant. Der erste Faktor beschreibt die Zusammensetzung, der zweite die geschützte logische Information.

Auf ihm ist die Kompression der verlorenen Modenbesetzung

$$n_r\big|_{\rm komprimiert}
=\begin{pmatrix}1/32&0\\0&0\end{pmatrix}\otimes I_{15}.$$

Die Umgebung kann somit etwas über die Zusammensetzung erfahren, aber nichts über den logischen Faktor. Die logische Information bleibt im Sinn der Subsystem-Fehlerkorrektur rekonstruierbar, auch wenn die Paar-Boson-Umwandlung vor dem einzelnen bekannten Verlust stattgefunden hat. Die Zusammensetzung selbst muss nicht wiederhergestellt werden. [E2]

Das ist stärker als ein nur auf der Paarseite gespeicherter Code. Es ist zugleich enger als ein 30-dimensionaler vollständig geschützter Quantencode: Der zweidimensionale Zusammensetzungsfaktor ist kein zusätzlich geschütztes logisches Qubit.

## 6.6 Nachgewiesene Grenzen

- Bereits die gemeinsame Löschung der Moden 0 und 29 verletzt die Korrekturbedingung: Die Kompression von $n_0n_{29}$ ist ein nichtskalarer Rang-eins-Operator.
- Für einen Verlust an unbekannter Position reichen die Bedingungen nicht. Ein konkreter Defekt entsteht bei $Q^\dagger f_0^\dagger f_1Q$.
- Der gewählte 15er-Unterraum ist nicht unter der gesamten inneren Gruppe invariant. Bereits ein Cartanoperator führt ihn aus sich heraus. Seine Auswahl benötigt daher einen zusätzlichen Bezugs- oder Präparationsvertrag.
- Die zwei ursprünglichen Kontrollen wirken auf dem logischen Faktor als Identität. Sie erzeugen den Kodierer, den Decoder und beliebige logische Gatter nicht allein.
- Mehrere Verluste während einer fortgesetzten Dynamik, ein unbekannter Fehlerzeitpunkt und die Umsetzung der Recovery durch native Geräte sind nicht bewiesen.

Die Konstruktion liefert also einen exakten nativen Speicher- und Rekonstruktionsbaustein. Sie identifiziert noch keinen holografischen Rand oder physikalischen Raum.

# 7. Folgeaufgabe 6: Größenfolge, Zusammensetzung und Erinnerung

## 7.1 Eine vollständig kontrollierte bedingte Folge

Wenn unabhängige Kopien der Bank als zusätzliche Kompositionsregel zugelassen werden, besitzt jede Kopie den Unterraum $\mathcal K_{30}$. Für L Kopien ergibt sich

$$\mathcal K_L\simeq(\mathbb C^2)^{\otimes L}
\otimes(\mathbb C^{15})^{\otimes L},$$

$$H_L|_{\mathcal K_L}
=\left(\sum_{j=1}^L h_2^{(j)}\right)\otimes I_{15^L}.$$

Dies ist für jedes endliche L exakt; es gibt keinen mit L wachsenden Kompressionsfehler. Die lokale Recovery korrigiert einen bekannten Modenverlust in einer ausgewählten Bank. Auch ein bekannter einzelner Verlust je Bank kann durch das Produkt der lokalen Recoverys auf dem logischen System korrigiert werden.

Wählt man für eine angehängte Bank einen Eigenzustand von $h_2$ mit Energie e und einen festgelegten logischen Zustand, ist die Anhängeabbildung $J_L$ isometrisch und erfüllt

$$H_{L+1}J_L=J_L(H_L+eI).$$

Bis auf die unwesentliche zusätzliche Gesamtphase bleiben alle schon vorhandenen Vorhersagen erhalten. Ein konkretes Zweibankbeispiel wurde exakt geprüft; die allgemeine Aussage folgt aus der Tensorproduktform.

Diese Folge zeigt, dass ein konsistenter Aufbau möglich ist. Die Kopierregel, die Auswahl des hinzugefügten Zustands und die lokale Adressierung sind Voraussetzungen. Die Folge besitzt keine hergeleitete Interaktion zwischen den logischen Registern und wählt keine Raumdimension. Sie funktioniert außerdem für viele Kopplungsverhältnisse und bestätigt daher die Auswahlgrenze aus Abschnitt 2.

## 7.2 Warum eine verkleinerte Zustandsansicht ihre eigene Zeitentwicklung verlieren kann

Für zwei Qubits sei

$$H=X_A X_B,\qquad
\rho_A=|+y\rangle\langle+y|.$$

Die beiden Gesamtzustände $\rho_A\otimes|+x\rangle\langle+x|$ und $\rho_A\otimes|-x\rangle\langle-x|$ haben dieselbe reduzierte Ansicht in A. Trotzdem ist

$$\frac{d}{dt}\langle Z_A\rangle\Big|_{t=0}=+2
\quad\text{beziehungsweise}\quad-2.$$

Die weggeworfene Information beeinflusst die Zukunft. Es gibt deshalb auf dieser uneingeschränkten Zustandsklasse keine eindeutige autonome Dynamik, die nur den aktuellen reduzierten A-Zustand benutzt. Das ist ein exaktes kleines Gegenbeispiel zur Annahme, jede Schattenkarte liefere automatisch einen geschlossenen kleineren Prozess.

Ein weiterer Test komprimiert den Laplaceoperator einer Viererkette auf zwei normierte Zweierblöcke. Die kleine Matrix lautet $\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$, doch die ausgelassene Kopplung hat Norm eins. Die Kompression ist daher keine exakt invariante Dynamik.

## 7.3 Konsequenz für die vorgeschlagene Fixpunktsuche

Eine physisch sinnvolle Vergröberung muss neben effektiven Zuständen auch die für weitere Eingriffe relevante Erinnerung mitführen oder ihren Einfluss kontrolliert beschränken. Geeignete Objekte sind deshalb ganze Prozesse einschließlich ihrer Instrumente und nicht nur einzelne Spektren oder Dichtematrizen. Der etablierte Rahmen von Quantennetzwerken beschreibt genau solche Verknüpfungen. [E5]

Die hier untersuchte Konsistenzforderung führt zu zwei Ergebnissen: Sie lässt exakte Produktfolgen zu und verlangt bei allgemeinen Wechselwirkungen zusätzliche Erinnerungsdaten. Sie liefert noch keinen eindeutigen physikalischen Fixpunkt. Ein künftiger stärkerer Satz müsste eine konkrete Quellregel, einen festgelegten Vergröberungsoperator und eine Vergleichsklasse enthalten. Ein beliebiger passend gewählter Fixpunkt würde die Auswahlfrage voraussetzen.

# 8. Abgleich der vier zusätzlich eingesandten Texte

## 8.1 Was davon bereits berücksichtigt war

U2 ist byteidentisch mit dem aktuellen Repositorybericht *Operationssatz, Feldwörterbuch, Grundzustandssonde* (Pfad im Quellenmanifest). U1 ist eine vereinfachende Darstellung derselben Arbeitslinie. U3 fasst die andere v1.6.3-Linie zu Handgriffen, Grundzustand und Feldtyp zusammen. Viele ihrer Befunde standen bereits im Hauptpaper oder den historischen Anhängen von R1/R4.

Insbesondere sind die 14/7-Kommutantenverträge, das exakte Lochbild, die niedrigen Normen, der verschwindende gleichhändige Weyl-Skalarkanal und die begrenzte Stärke der jeweiligen Grundzustandssonde übernommen. Die neue Fortsetzung verwendet die Texte als Quellenmaterial und behandelt darin stehende Arbeitsanweisungen nicht als zusätzliche Autorität.

## 8.2 Was weiterhin interessant ist

**Reduzierte Räume für die geladene Antwort.** Die in U2 berichteten Stabilisator-Orbits können eine konkrete alternative Datenstruktur für die geladene Antwort auf dem nativen Grundzustand liefern. Die Zahl der Orbits ist noch keine fertige Hamiltonkompression. Für eine belastbare Nutzung müssten Orbitgewichte, Vorzeichen, Zustandsnormierung und die Hamiltonwirkung gemeinsam geprüft werden. Diese neue große Antwortrechnung wurde in dieser Fortsetzung nicht durchgeführt.

**Getrennte Casimir-Auslesung.** Die dunklen Typen sind ein präziser Testfall für eine zusätzliche symmetrieverträgliche Observable. Die bereits bekannte und hier erneut geprüfte Zwischenstufe 14→15→16 zeigt, wie sich die Suche auf eine konkrete minimale Messressource richten lässt.

**Gemischte Spurnetzwerke.** Diesen Vorschlag haben die Abschnitte 5.2–5.5 tatsächlich weitergeführt: vier native Richtungen, ihre Kreuzterme, ein ausführbarer gemischter Koeffizientenrechner und eine reale Restnorm ersetzen die bloße Forderung nach weiteren skalaren Normen.

## 8.3 Welche Aussagen enger gefasst werden müssen

| Aussage der nachgereichten Texte | Präzisierung anhand des neueren Stands |
|---|---|
| Die gesamte operative Freiheit ist eine binäre Ja/Nein-Frage | Zu stark: invariante Zwischenalgebren existieren; aktive Symmetrie, Casimir und Modenmessung sind verschiedene Ressourcen. |
| Beide getrennten Casimire werden zur Unterscheidung der dunklen Typen benötigt | Bereits einer besitzt drei verschiedene relevante Eigenwerte. |
| Der Clock ist wegen seiner nichtskalaren Wirkung äußerlich | Die konkrete Clock besitzt einen Spin-Lift; Nichtskalarität beweist keinen Austritt aus der zusammenhängenden Gruppe. |
| Singuletts nur bei $N\equiv0\pmod4$ beschränken automatisch alle Grundzustandskandidaten auf diese Sektoren | Die Zentrumsregel beschränkt Singuletts. Ein symmetrischer Hamiltonoperator kann einen entarteten Nicht-Singulett-Grundsektor besitzen. Dessen Ausschluss braucht Energieargumente. |
| 33 Bosonstufen entsprechen einer durch 33 skalare Normen bestimmten vollständigen Kette | Die Bosonstufen sind nicht alle eindimensional. Die Zahl 33 ist keine Obergrenze der vollständigen Krylov- oder Singulettdimension. |
| Ein winziger Seitenzweig beweist globale Genauigkeit | Nur eine kontrollierte Restkopplung und ihre spektrale Lage liefern eine solche Aussage. |
| Der physische relativistische Feldtyp ist endgültig festgelegt | Der Nullsatz betrifft einen bestimmten gleichhändigen lokalen Ansatz. Eine positive, kausale Kinetik und die Herkunft dieses Ansatzes bleiben eigenständige Aufgaben. |

Die Zentrumspräzisierung lässt sich an einem einfachen Gegenmodell sehen: Auf dem endlichen Fermion-Fockraum ist $(N_f-1)^2$ positiv und innerlich symmetrisch, hat aber den 64-dimensionalen Nicht-Singulett-Sektor $N_f=1$ als Grundraum. Dieses Quartikmodell ist kein Gegenbeispiel zum nativen kubischen Grundzustandssatz; es widerlegt nur den allgemeinen Schluss von Symmetrie auf einen Singulett-Grundzustand.

## 8.4 Zahlen und Versionen nicht vermischen

Die Sonde in U2 hat die schwächere Grenze etwa $-1.0942308\Delta$; R1 besitzt bereits die stärkere H-Lanczos-Grenze etwa $-1.12963812\Delta$. Dass die schwächere Sonde Nachbarsektoren nicht trennt, widerlegt den stärkeren, anders bewiesenen Modellgrundzustandssatz nicht.

U3 nennt weitere Zahlen zur fünften Norm, Ritz-Überlappung, Verschränkung und Antwortgewichten. Solche Werte werden hier nicht allein auf Grundlage des erläuternden Textes als neue zertifizierte Grundzustandsdaten übernommen. Der frühere Quellenabgleich dokumentierte bereits unterschiedliche Rechner- und Berichtshashes sowie eine falsch skalierte historische Restnorm. Die jetzigen neuen Resultate sind an ihre eigenen Eingaben und tatsächlichen Ergebnisdateien gebunden.

Auch die in U2 offen gelassene Bilinearzerlegung ist durch v1.6.7 weitergeführt: $4096=1+45+210+15+675+3150$. Ein historischer offener Rest ist kein zusätzlicher aktueller Blocker.

## 8.5 Der vierte Nachtrag: „Die fundamentale Reduktion“

Der anschließend eingesandte Text U4 beginnt **bytegenau mit der bereits im Hauptpaper enthaltenen Quelle S003**. Auf diese Forschungsnotiz folgt eine erläuternde Zusammenfassung. Ihr Hauptargument war deshalb schon berücksichtigt. Neu in dieser Fortsetzung sind der unabhängige Rang-Replay, die Verbindung zum 15er-Code und die folgende Präzisierung des Prozessvertrags.

**Gesamte Einloch-Antwort.** Unter den ausdrücklich genannten Voraussetzungen — innerlich invarianter H, Singulettzustand $\Omega$, irreduzible Darstellung der 64 Entnahmeoperatoren — ist $T:e_r\mapsto f_r\Omega$ ein Intertwiner der entsprechenden, gegebenenfalls konjugierten Darstellung. Für jede beschränkte Spektralfunktion F kommutiert $T^\dagger F(H-E_0)T$ mit dieser irreduziblen Darstellung. Schurs Lemma liefert exakt

$$T^\dagger F(H-E_0)T=\gamma_F I_{64},\qquad
C_{rs}(t)=\delta_{rs}c(t).$$

Das gilt einschließlich aller Nebenlinien. Es ist keine Einpolnäherung. Weitere Genauigkeit von $c(t)$ erzeugt innerhalb dieser festen Operatorfamilie keinen nichttrivialen Ortsindex. Die Aussage schließt andere Operatorfamilien, präparierte nichtinvariante Zustände und größere gemeinsame Träger nicht aus. Ein kleines exaktes Multiplizitätsbeispiel im Prüfpaket illustriert diesen Satz; der allgemeine Beweis ist das ausgeschriebene Schur-Argument. Die großen Grundzustands- und Polzertifikate wurden dafür nicht erneut ausgeführt.

**Multiplizitäten.** Die Zerlegung $\mathcal H=\bigoplus_\lambda R_\lambda\otimes\mathcal M_\lambda$ erlaubt für symmetrieerhaltende Dynamik $H=\bigoplus_\lambda I\otimes h_\lambda$. Genau hier können unterschiedliche Vorkommen desselben inneren Typs gekoppelt werden. Dass solche Räume existieren, bestimmt jedoch weder eine bevorzugte Ortsbasis noch lokale Instrumente oder eine Dimension. Der isolierte 64er-Pol hat nach dem Quellvertrag Multiplizität eins. Die Zerlegungsmethode ist etablierte Operatoralgebra, siehe [Holbrook, Kribs und Laflamme](https://arxiv.org/abs/quant-ph/0402056).

Der neue 15er-Code darf mit diesem Raum nicht gleichgesetzt werden: Sein logischer Faktor ist eine Multiplizität der **eingeschränkten Operationsalgebra**, während der gewählte Code nicht unter der vollen inneren Gruppe invariant ist. „15 geschützte Dimensionen“ bedeutet deshalb nicht „15 hergeleitete Orte“.

## 8.6 Die Tensorbehauptungen stimmen im frischen Replay

Die direkte Rechnung am gepinnten W bestätigt sämtliche angegebenen Zahlen:

| Struktur | Exaktes Ergebnis |
|---|---:|
| Fermionmoden / verschiedene Paarungen | 64 / 480 |
| Grad jeder Mode | 15 |
| Zusammenhangskomponenten | 1 |
| Rang der Paritätsbedingungen über $\mathbb F_2$ | 63 |
| Rationale Besetzungsbedingungen | 480 Gleichungen, 124 Variablen |
| Rang / freie diagonale Ladungen | 115 / 9 |

Wenn die Bosonen unter der betrachteten Paritätsoperation unverändert bleiben, erzwingt jede vorhandene Paarung $s_i+s_j=0$ modulo zwei. Zusammenhang macht alle $s_i$ gleich. Es bleiben Identität und globale Fermionparität. Das ist kein Satz über Paritäten, die zugleich Bosonen transformieren, und keine Klassifikation sämtlicher nichtdiagonaler Symmetrien.

Dieser Befund passt unmittelbar zur neuen Kodierung: Die 480 Kanten dieses einen zusammenhängenden Graphen zerfallen in die 15 perfekten Paarungen aus Abschnitt 6. Ein kohärentes Codewort nutzt eine solche Paarung; der Hamiltonoperator verwendet alle Paarungen. Die kombinatorische Verbindung ist exakt. Eine Kante ist weiterhin ein erlaubter innerer Vertex und kein nachgewiesener räumlicher Abstand.

Die Zusammensetzungsdiagnose in U4 ist damit berechtigt: Separate Kopien mit ausschließlich lokal geraden Fermionoperationen können zusätzliche lokale Paritäten einführen, die innerhalb der einen nativen Bank nicht existieren. Daraus folgt die Notwendigkeit, eine vorgeschlagene Kopier- oder Identifikationsregel zu prüfen. Es folgt nicht, dass beliebiges Teilen von Ressourcen bereits eine zulässige, symmetrieverträgliche räumliche Quelle konstruiert.

## 8.7 Zustandsregel und beobachtbare Äquivalenz

Für $[H,N]=0$ und $[O,N]=0$ ist die einzelne neutrale Heisenbergobservable unter $H$ und $H+\mu N$ identisch. Bei festem Gesamt-N gilt allgemeiner: Jede hinzugefügte Funktion dieses Gesamt-N ist innerhalb des Sektors ein skalarer Energieversatz. Diesen Unterschied muss eine physikalische Auswahlregel nicht bestimmen, sofern der gesamte zugelassene Prozess ihn nicht beobachten kann.

**Präzisierung:** Eine neutrale Schlussmessung allein reicht für Prozessäquivalenz nicht. Werden zwischenzeitlich ladungsändernde Eingriffe oder eine passende Referenz zugelassen, können relative Phasen sichtbar werden. Ein exaktes Zweizustands-Gegenbeispiel beginnt in $|0\rangle$, führt eine Hadamard-Rotation, eine freie Entwicklung mit $\mu N$ und eine zweite Hadamard-Rotation aus. Die neutrale Messung $|0\rangle\langle0|$ liefert

$$p_0(t)=\frac{1+\cos(\mu t)}2.$$

Die Rotationen sind hier ausdrücklich zusätzliche Ressourcen. Bei vollständig ladungserhaltenden Instrumenten auf dem gesamten beschriebenen System bleibt der passende Äquivalenzsatz bestehen. Eine mitmodellierte Referenz hebt eine bloß globale Phase bei festem Gesamt-N nicht auf. Die Frage ist stets, welches N zum gesamten Prozess gehört und welche Eingriffe zugelassen sind.

Auch der Vakuumgegenvergleich ist korrekt. Aus der bereits in R5 bewiesenen Voll-Fock-Casimirschranke $\sum_A P_A^\dagger P_A\le15N_f/2$ folgt durch quadratische Ergänzung

$$H+\mu N\ge\left(\mu-\frac{15g^2}{2\Delta}\right)N_f+2\mu N_b.$$

Bei $g=\Delta/20$, $\mu=\Delta/50$ folgt $H+\mu N\ge\Delta N/800$. Das leere Vakuum ist eindeutig. Dagegen hat H schon im hellen $N=2$-Sektor eine negative Energie. Für den logischen Gegenvergleich wird der große N=64-Beweis daher nicht benötigt. Der neue Rechner prüft die exakten Koeffizienten; die Casimiridentität selbst wird aus ihrer bezeichneten Quelle übernommen.

U4 korrigiert zudem eine mögliche Überinterpretation unseres Präparationsausschlusses: Eine fundamentale Theorie braucht keinen äußeren Experimentator, der ihren globalen Zustand aus dem leeren Zustand herstellt. Sie braucht eine begründete Zustands- oder Randbedingungsregel. Die spätere Erklärung interner Präparationen und Detektoren ist eine damit verbundene eigene Aufgabe.

## 8.8 Intervention und Forschungspriorität

Die vorgeschlagene unbedingte Interventionsdifferenz ist ein geeigneter Wirkungstest. Für einen tatsächlich verfügbaren Eingriff $e^{-i\epsilon A}$ ist ihr linearer Term $i\epsilon\,\omega([A,B(t)])$. **Jede von null verschiedene Differenz**, auch eine negative, zeigt eine Veränderung der Statistik. Ein verschwindender linearer Term reicht nicht zum Ausschluss: Schon eine Rotation von $|0\rangle$ mit A=X ändert die Rückkehrwahrscheinlichkeit zu $\cos^2\epsilon$, obwohl die erste Ableitung null ist.

Bei unabhängig kommutierenden Teilen fehlt ein unmittelbarer Zugriffseffekt. Spätere Wirkung erhält erst zusammen mit einer hergeleiteten Lokalitäts- und Abstandsstruktur eine räumliche Bedeutung. Lieb–Robinson-Schranken setzen geeignete lokale Wechselwirkungen voraus; sie beweisen für sich weder Lorentzsymmetrie noch drei Raumdimensionen. [Bravyi, Hastings und Verstraete](https://arxiv.org/abs/quant-ph/0603121).

Die Priorisierung von U4 ist deshalb überzeugend: Eine gemeinsame Quell-, Kompositions- und Zustandsregel ist der entscheidende verbindende Gegenstand. Lokale Spektren, der neue Code und Matrixmomente liefern dazu belastbare Bauteile und Tests. Sie wählen diese Regel nicht aus. Die Reduktion auf $(\mathcal A_L,H_L,\omega_L,\mathfrak I_L)_L$ bezeichnet das gesuchte Ergebnis; sie ist noch kein Herleitungssatz. Feldtyp und Kinetik können parallel geprüft werden, müssen am Ende aber zu derselben Konstruktion gehören.

# 9. Was sich der vollständigen Lösung tatsächlich angenähert hat

Die stärkste neue Verbindung lautet:

$$\begin{aligned}
\text{nativer Tensor}&\longrightarrow\text{optimale Paar-Kodierung}\\
&\longrightarrow\text{invariante Zusammensetzungsdynamik}\\
&\longrightarrow\text{kontrollierte lokale Rekonstruktion}.
\end{aligned}$$

Parallel dazu wurde aus derselben Paarregel eine gemeinsame mehrdimensionale Antwortstruktur berechnet. Damit stehen Kodierung und Antwort nicht mehr nur als lose Möglichkeiten im Raum; es gibt konkrete Matrizen, Zustandsvektoren, Decoder und Fehlerverträge.

Die zentrale Grenze lässt sich nun ebenfalls konkret ausdrücken: Der native Hamiltonoperator erhält die logische Information des neuen Codes, aber die bisher gewährten Kontrollen bewegen sie nicht frei. Der optimale Kodierer und seine Decoder sind mathematische Abbildungen, deren physische Verfügbarkeit nicht aus derselben Rechnung folgt. Eine zusätzliche Kopie erzeugt eine konsistente größere Darstellung, aber noch keinen ausgewählten Nachbarn oder räumlichen Ort.

Der nächste verbindende Nachweis müsste deshalb eine **Quell- und Kompositionsregel für einen gemeinsam dynamischen Prozess** liefern. Der geschützte logische Faktor ist ein möglicher konkreter Testträger; die Lösung muss nicht zwingend über diesen Code verlaufen. Er müsste Präparation, tatsächlichen Eingriff, Aufzeichnung, Ladung und Energie mitführen. Erst dann kann geprüft werden, ob viele solcher Ausführungen eine bestimmte lokale Feldtheorie und Raumzeit tragen.

Die physikalische Auswahl von Hamiltonoperator und Zustand bleibt offen. Dasselbe gilt für den Ursprung der Raumzeit mit drei Raum- und einer Zeitdimension, Chiralität, Kontinuum, Parametertransfer und Gravitation. Kein T1–T8-Tor wurde als vollständig geschlossen markiert. RH, Faktorisierung und P versus NP sind nicht Gegenstand dieser Rechnungen.

# 10. Reproduzierbarkeit und Prüfgrenzen

Das Prüfpaket enthält die native Tensorquelle, die explizite Abbildung des Codes, die Referenzkomponente mit 35 Zuständen, alle eigenen Rechner, die vollständigen gemischten Matrizen, normale und optimierte Ergebnisdateien sowie eingefrorene relevante Quelltexte. Die neuen Tabellen und Ergebnisse sind mit SHA-256 nachvollziehbar.

Die sieben neuen Python-Prüfungen bestätigen insgesamt **537 explizite Bedingungen**, jeweils mit identischem Ergebnis im normalen und im optimierten Lauf. Die unabhängige C++-Kontraktion stimmt ebenfalls mit und ohne Optimierung bytegenau überein.

Die Prüfsuite kontrolliert insbesondere alle 64 einzelnen Modenlöschungen, sämtliche 15 perfekten Paarungen, alle 60 Lie-Erzeuger, die rationalen Matrixreste und unabhängigen Wick-Vergleiche. Die Prüfanzahl zählt explizite Bedingungen einschließlich der wiederholten Komponentenprüfungen; sie ist keine Anzahl unabhängiger Theoreme.

Die analytischen Beweise der Normalform, der Codeoptimalität und der allgemeinen Produktfolge stehen im Text. Sie wurden nicht in einem formalen Beweisassistenten verifiziert. Die große native Grundzustandsrechnung, sämtliche höheren Singulettstufen, die großen geladenen Orbitmatrizen sowie die physische Umsetzung von Apparaten wurden nicht neu ausgeführt. Ergebnisse dieser Art werden nur dort übernommen, wo die jeweilige Quelle und Voraussetzung ausdrücklich benannt sind.

Während der Entwicklung wurde eine falsch abgeschriebene historische Kontrollsumme verworfen und durch den Wert der eingefrorenen Originaldatei ersetzt. Die neu berechnete Kontraktion stimmte mit dieser Originaldatei überein. Fehlgeschlagene Entwicklungsläufe sind keine erfolgreichen Prüfungen.

```{=latex}
\clearpage
```

# 11. Quellen

## Lokale Quellen und eingegebene Texte

**R0:** *TFPT und Universalraum — Von der markierten Algebra zum gemeinsamen physikalischen Prozess*, Forschungspaper vom 15.09.2026, 33 Seiten. Diese Fortsetzung aktualisiert insbesondere dessen §§5.5–5.6, 6.4 und 15.

**R1:** *TFPT / Universalraum: Die richtige einfache Kette*, v1.6.7 einschließlich des Nachtrags *Derselbe Prozess in verschiedenen Ansichten*, eingefrorene Quelle S074. Tensor, vier Singuletts, H-Kette, Z4-Familie, ursprünglicher 60er-Code und dessen Modenverlustgrenze.

**R2:** Repositorybericht *Minimale Forschungsfortsetzung nach v1.6*, vom 15.09.2026 (Pfad im Quellenmanifest). Vollständige kleine Sektoren und ursprünglicher 35D-Übergang.

**R3:** Repositorybericht *Relationaler Lochanschluss* vom 15.09.2026 (Pfad im Quellenmanifest). Relationaler Lochanschluss, kleine Antwortsektoren und Grenzen der nativen Kontrollalgebra.

**R4:** *Clock, gemeinsame Quelle und tatsächlicher Transport*, v1.6.6, Quelle S033. Insbesondere Ein-Casimir-Trennung, Zwischenalgebren und konkrete Spin-Identifikation des Clock.

**R5:** *TFPT / Universalraum: Ergebnisse v1.6*, Quelle S038. Voll-Fock-Casimiridentität und Vakuumgegenvergleich.

**U1:** Eingesandter Text *Gern — die einfache, bildliche Version*, 15.09.2026.

**U2:** Eingesandter Text *Operationssatz, Feldwörterbuch, Grundzustandssonde*. Byteidentisch mit dem am Abgleichstag vorhandenen Repositorybericht *Operationssatz, Feldwörterbuch, Grundzustandssonde* (Pfad im Quellenmanifest).

**U3:** Eingesandter Text *Handgriffe, Grundzustand und Feldtyp — einfach erklärt*, bezeichnet als v1.6.3. Aussagen werden gegen die neueren gepinnten Belege abgegrenzt.

**U4:** *TFPT / Universalraum: die fundamentale Reduktion*, Analyse bis v1.6.6, mit angehängter Erläuterung. Der Haupttext ist byteidentisch mit der bereits im Hauptpaper verwendeten Quelle S003; die zusätzliche Prüfung steht in §§8.5–8.8.

## Externe Primärliteratur

**E1:** E. Knill, R. Laflamme, *A Theory of Quantum Error-Correcting Codes*. Grundlage der exakten Korrekturbedingungen. [Originalarbeit](https://arxiv.org/abs/quant-ph/9604034).

**E2:** D. W. Kribs, R. Laflamme, D. Poulin, M. Lesosky, *Operator quantum error correction*. Rahmen für den Schutz eines logischen Faktors bei ungeschütztem zusätzlichem Faktor. [Originalarbeit](https://arxiv.org/abs/quant-ph/0504189).

**E3:** P. T. Nam, M. Napiórkowski, J. P. Solovej, *Diagonalization of bosonic quadratic Hamiltonians by Bogoliubov transformations*. Methodischer Kontext; die konkrete kubische Normalform dieser Arbeit ist oben ausgeschrieben. [Originalarbeit](https://arxiv.org/abs/1508.07321).

**E4:** L. M. Robledo, *The sign of the overlap of HFB wave functions*. Pfaffianbehandlung der Vorzeichenfrage bei fermionischen Überlappungen. [Originalarbeit](https://arxiv.org/abs/0901.3213).

**E5:** G. Chiribella, G. M. D’Ariano, P. Perinotti, *Theoretical framework for quantum networks*. Zusammensetzung von Zuständen, Messungen und Kanälen zu Prozessen mit Erinnerung. [Originalarbeit](https://arxiv.org/abs/0904.4483).
