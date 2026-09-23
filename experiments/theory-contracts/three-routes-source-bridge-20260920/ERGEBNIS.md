# Drei TFPT-Lösungswege: ausgeführte Rechnungen und gemeinsamer Anschluss

20. September 2026 · Forschungsstand, keine vollständige TOE-Herleitung.

Die drei Wege sind über die vorherige Korrelation hinaus bearbeitet. Dabei wurden ein konkreter geometrischer Phasenkandidat, ein konstruktiver Clock-Anschluss der E8-Randtheorie und ein exakt lösbarer erster Rückwirkungsblock der ursprünglichen Compilerquelle gewonnen. Die Ergebnisse gelten auf ihren benannten Quellen und Räumen; deren vollständige physische Identifikation bleibt zu liefern.

| Weg | Neu berechnet | Was dadurch genauer feststeht |
|---|---|---|
| Phase und volle Wirkung | Native Nahtschleife plus bedingter holomorpher Flavor-Lift: relative e/d-Monodromie \(i\), gewöhnliche Phasentangente \(1/4\) | Ein vorhandener geometrischer Ursprung ist als Kandidat benannt. Die physische Antwort hängt noch von der Quellabbildung und der Determinantenlinienverbindung ab. |
| E8-Herkunft | Ganzzahlige native C/J-Lifts, individuelle Kokzykluslifts, gemeinsame Zentralrelation, gemeinsam invariante Energieformen | Geforderte gemeinsame Clock-Invarianz fixiert den E8-Energieblock bis auf eine Skala; die Clocks drehen jedoch die feste mikroskopische U(1)-Ladung. |
| Vakuum und Rückwirkung | Exakt geschlossener erster Komplementblock des tatsächlichen lokalen Hamiltonoperators | Die Zustandsänderung bleibt bei kleiner positiver Kopplung endlich. Eine schwache Kopplung rechtfertigt hier keine schwache Zustandskorrektur. |

## 1. Ein geometrischer Phasenkandidat aus dem vorhandenen Bestand

Die native, clock-invariante Nahtfamilie lautet

\[
XY=Z^4+a_0.
\]

Ein Umlauf von \(a_0\) dreht die Gewicht-eins-Periodensektion \(t\) um eine Viertelphase:

\[
a_0\mapsto e^{i\alpha}a_0,
\qquad t\mapsto e^{i\alpha/4}t,
\qquad \alpha=2\pi:\quad t\mapsto it.
\]

Diese geometrische Familie ist bereits im TFPT-Bestand vorhanden. Neu in dieser Runde ist ihre explizite Verbindung mit den bisherigen Massendeterminantengraden \((6,9,10)\). **Unter der zusätzlichen Annahme, dass dieselbe Periodensektion holomorph in die Yukawa-Monomiale eingeht**, folgt

\[
(\det Y_u,\det Y_d,\det Y_e)
\mapsto(-1,i,-1)(\det Y_u,\det Y_d,\det Y_e).
\]

Der relative Lepton-/Down-Faktor erhält somit \(i\), und seine gewöhnliche Phasentangente beträgt

\[
\partial_\alpha\arg(\det Y_e/\det Y_d)=\frac{10-9}{4}=\frac14.
\]

Eine gemeinsame geometrische Phase muss also nicht aus jeder Ausgabe verschwinden: Verschiedene Potenzen können sie verschieden lesen. Die betreffende Komponente schließt nach vier Umläufen auf der gehobenen Winkelachse. Das ist eine Aussage über die bedingte Sektion, keine physische Domain-Wall-Zahl.

**Der entscheidende Unterschied zur fertigen physikalischen Phase:** Die geometrische Familie ist bei festem Betrag lokal durch Koordinatenrotation identifizierbar. Die sichtbare Phase kann daher eine Rahmenphase sein. In der Konvention

\[
\operatorname{Im}(s^{-1}\nabla_\alpha s)
=\partial_\alpha\arg s+A_{e-d}
\]

würde die lokale Verbindung \(A_{e-d}=-1/4\) die gewöhnliche Viertelphase punktweise aufheben. Eine Holonomie \(-i\) allein entscheidet nur die Kompensation nach einem geschlossenen Umlauf, nicht den lokalen Verlauf.

Der ausgeführte Test trennt außerdem zwei Sackgassen ab: Glatte Deformationen der vorhandenen C6-Clock mit unveränderter Relation \(U^6=I\) sind infinitesimal reine Konjugationen. Ihr voller Resolventdeterminant bleibt konstant. Auch die vorhandenen A3-Lepton-Classfunctions gewinnen durch Basisrotation keine Phase.

Damit liegt die Herkunftsfrage jetzt an einem konkreten Übergang: **die vorhandene Periodenlinie auf die Yukawaoperatoren abbilden und ihre Verbindung aus derselben Quelle bestimmen**. Erst dann darf die volle kovariante Ward-Antwort mit Higgs, Fermionmaß und Komplementdeterminant ausgewertet werden. Die beiden Quellen nur über das Symbol \(t\) zu identifizieren, wäre noch keine Herleitung.

Details: [Phasenbeweis](phase/PROOF.txt), [Ergebnisdaten](phase/phase_family_result.json).

## 2. Die tatsächlichen Clocks passen zum rekonstruierten E8-Gitter

Die im Projekt gepinnten Matrizen \(C\) und \(J\) wurden auf den konkreten ganzzahligen E8-plus-Zusatzpaar-Rahmen übertragen. Beide erhalten die Statistikform \(K\), die gewählte Energiematrix \(V_*\) und die Nullwechselwirkungsrichtung \(n\). Die Abbildung respektiert alle 240 E8-Wurzeln.

Auch die nötigen individuellen Operatorvorzeichen wurden konstruiert. Die beiden Lifts können ohne Ordnungsverdopplung so gewählt werden, dass

\[
\widehat C^{15}=\widehat J^2=\widehat{-I}
\]

gilt. Damit ist diese gemeinsame Relation geprüft; sämtliche weiteren gemischten Relationen der erzeugten Gruppe und der mikroskopische Fermionlift sind damit nicht automatisch bewiesen.

Fordert man Energieinvarianz unter beiden Clocks, ergibt sich ein zusätzlicher Auswahlsatz:

\[
\dim\operatorname{Sym}(E_8)^C=4,
\quad\dim\operatorname{Sym}(E_8)^J=16,
\quad\dim\operatorname{Sym}(E_8)^{C,J}=1.
\]

**Gemeinsame Invarianz unter beiden Clocks lässt im E8-Block nur eine Energieskala zu.** Dass gerade diese Invarianz die physische Energie auswählen soll, bleibt eine Voraussetzung. Die positive Energiematrix des massiven Zweiersektors behält drei weitere Parameter. Die komplette Matrix \(V_*\) ist deshalb noch nicht eindeutig aus den Clocks ausgewählt. Am gewählten \(V_*\) bleibt außerdem innerhalb der geprüften Klasse relevanter, neutraler, primitiver Selbstnull-Cosinusse nur die Richtung \(\pm n\).

Die Ladungsprüfung verhindert eine falsche physische Identifikation: Im gewählten Quellmodell trägt der rekonstruierte Spinorstrom Teilchenzahl vier. Die native C- oder J-Wirkung erhält die feste Gesamtteilchenzahl nicht. Sie kann hier als Automorphismus wirken, der die Ladungsmarkierung mitdreht; sie kann bei festgehaltener erhaltener Quellladung nicht einfach die physische Zeitentwicklung sein. Diese Quellladung ist noch nicht mit elektromagnetischer Ladung oder Hyperladung identifiziert.

Der konstruktive Fortschritt ist somit ein tatsächlicher Gitter- und Operatoranschluss samt eingeschränkter Energieform. Offen bleiben die Herkunft des Zusatzpaares und der konkreten Wechselwirkung, der vollständige mikroskopische Lift sowie die physische Rolle der Clocks. Die geometrische A3-Vierteldrehung aus Weg 1 und dieses \(J\) sind trotz gleicher Ordnung nicht ohne Abbildung identisch.

Details: [Clock- und Herkunftsbeweis](e8/PROOF.txt), [Matrizen und Zertifikat](e8/RESULTS.json).

## 3. Die erste Rückwirkung der ursprünglichen Quelle ist exakt lösbar

Verwendet wird der vorhandene lokale Quellterm

\[
H_{\rm loc}=\kappa L+JH_E.
\]

Hier bezeichnet \(J\) die Kopplung, nicht die Clockmatrix aus Weg 2. Die Rechnung setzt den bereits deklarierten Compiler-Hamiltonoperator voraus; dessen physische Auswahl wird durch die lokale Lösung nicht neu hergeleitet.

Seine tatsächlichen Reflexionsoperatoren erfüllen

\[
[L,H_E]=0,\qquad H_E^2=2H_E.
\]

Für einen Paketvektor mit \(L\)-Eigenwert \(\lambda\) und \(\eta=\langle H_E\rangle\), \(0<\eta<2\), bilden das Paket und sein erster orthogonaler \(H_E\)-Anteil daher einen **exakt invarianten** Zweierblock:

\[
H_{\rm block}=
\begin{pmatrix}
\kappa\lambda+J\eta & J\sqrt{\eta(2-\eta)}\\
J\sqrt{\eta(2-\eta)} & \kappa\lambda+J(2-\eta)
\end{pmatrix}.
\]

Seine Eigenwerte sind exakt \(\kappa\lambda\) und \(\kappa\lambda+2J\). Es handelt sich weder um einen Fit noch um eine auf wenige Momente begrenzte Näherung.

| Nativer lokaler Kanal | Eigenwerte nach Einbeziehen des Komplements | Komplementanteil im unteren Zustand für \(J>0\) |
|---|---|---:|
| Ungebundenes Paket, symmetrischer Materieanteil | \(3\kappa/5\), \(3\kappa/5+2J\) | \(3/10\) |
| Ungebundenes Paket, antisymmetrischer Materieanteil | \(\kappa\), \(\kappa+2J\) | \(1/2\) |
| Einfach gebundenes \(\Phi\)-Paket | \(\kappa/2\), \(\kappa/2+2J\) | \(3/4\) |
| \(\Omega\)-Paket | \(0\); kein erzeugter zweiter Zustand | \(0\) |

Die Anteile bleiben bei \(J\to0^+\) endlich, weil auch die zugehörige Energietrennung verschwindet. Das ist eine resonante Zustandsänderung. Die lokale Selbstenergie lautet exakt

\[
\Sigma(E)=\frac{J^2\eta(2-\eta)}{\kappa\lambda+J(2-\eta)-E},
\qquad H_{\rm eff}(E)=PHP-\Sigma(E).
\]

Die bisherige kritische Paketbedingung \(2\mu=\kappa+9J\) beruhte auf unmodifizierten Paketerwartungen. Die neue Rechnung verändert diese lokalen Zutaten unterschiedlich. Sie beweist **noch keine Verschiebung der globalen kritischen Linie** und liefert keinen Ersatzwert für die neun. Benachbarte Quellterme teilen Materieregister; der Transferterm und alle Observablen müssen mit derselben gemeinsamen Zustandsabbildung neu berechnet werden.

Die konkrete lokale Abbildung ist jetzt vorhanden:

\[
P_0=I-H_E/2,
\qquad W_0p=\frac{P_0p}{\sqrt{1-\eta/2}}.
\]

Sie liefert den niedrigeren Zustand im jeweiligen Kanal mit festem \(\eta\). Für mehrere Kanäle lautet der lineare Operator \(W_0=P_0P(PP_0P)^{-1/2}\), definiert auf dem Träger von \(PP_0P\). Ein anschließender physischer Antworttest muss \(W_0^*OW_0\) verwenden. Die bloße Übernahme der bisherigen Hopping- oder Ortsobservablen wäre inkonsistent.

Auch der erste Test benachbarter Quellterme ist ausgeführt. Für ein natives, weder paralleles noch orthogonales Wurzelpaar auf drei Materieregistern hat der gemeinsame Nullereignisraum **Dimension 18**, während der Kommutator der beiden lokalen Projektoren **Rang 32** hat. Ihr geordnetes Produkt ist kein Projektor. Die orthogonale und parallele Kontrolle ergeben dagegen kommutierende Projektoren mit gemeinsamen Räumen der Dimension 24 beziehungsweise 28. Damit scheitert die naive Multiplikation lokaler Nullprojektoren; eine passend normalisierte gemeinsame Isometrie wird dadurch nicht ausgeschlossen. Der 18-dimensionale gemeinsame Raum ist ein konkreter Ausgangspunkt für diese Konstruktion, noch kein globaler Grundzustand.

Details und Überlappungsprüfung: [Quellbeweis](vacuum/PROOF.txt), [Zertifikat](vacuum/results.json).

## Gemeinsame Konsequenz

Die zentrale Ladung liefert einen zusätzlichen Test für das Zusammenführen der Wege: Eine einzelne kritische Ising-CFT hat je chiraler Richtung \(c=1/2\), während die affine E8-Stromtheorie auf Level eins \(c=248/31=8\) benötigt. Unter den üblichen unitären Voraussetzungen und mit demselben Stressoperator würde die behauptete Einbettung einen Restsektor mit negativer Vakuumnorm erzeugen. Sie ist deshalb ausgeschlossen. Das betrifft einen **Ising-only-Grenzwert**, nicht die unbekannte volle Quellenphysik. Die Ising-Zuordnung folgt der Standardliteratur; hier wird sie auf die beiden konkreten Zielbeschreibungen angewandt. [Calabrese–Cardy](https://arxiv.org/abs/hep-th/0405152)

Für die Gesamtlösung müssen daher die tatsächlich benötigten geladenen Niederenergiefelder erhalten bleiben. Eine perfekt kontrollierte Paketordnung allein wäre noch nicht die E8-Stromquelle. Ebenso wenig ersetzt eine gewöhnliche geometrische Phase ihre kovariante physische Wirkung, oder eine Gitter-Clock die ladungserhaltende physische Zeit.

Der begründete gemeinsame Anschluss lautet jetzt: **native Phase und Verbindung, native Clock-/Ladungswirkung und die veränderten Quellzustände auf derselben lokalen Operatorfamilie zusammenführen.** Für jeden dieser drei Übergänge liegt nun eine konkretere Konstruktion oder Entscheidungsrechnung vor. Noch fehlt der gemeinsame physische Lift; kein T1–T8-Gate wird durch diese Runde geschlossen.

Die Primärliteratur zu Randrekonstruktion und Schur-Reduktion liefert den mathematischen Rahmen, nicht diese TFPT-spezifischen Herkunftsnachweise. [Cano et al.](https://arxiv.org/abs/1310.5708), [Dusson–Sigal–Stamm](https://arxiv.org/abs/2105.02058)

Die Prüfbelege, Quellenpins und [separaten Gegenprüfungen](GEGENPRUEFUNG.md) liegen zusammen mit diesem Bericht vor. Die Statusgrenze bleibt `PARTIAL`: neue exakte lokale und bedingte Resultate, keine vollständige physische Theorie. Der Forschungsbezeichner lautet `TFPT.SOURCE.THREE_ROUTES.20260920`.
