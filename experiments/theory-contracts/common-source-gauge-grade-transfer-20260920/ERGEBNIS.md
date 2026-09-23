# TFPT: gemeinsamer Quellenanschluss – Fortsetzung vom 20. September 2026

**Forschungsverdict: PARTIAL. Eine vollständige physikalische Gesamtlösung ist nicht bewiesen.**

Die Korrelation der bisherigen drei Wege mit dem neueren Flavor-Entwurf liefert
zwei konkrete Reparaturen: Eine gemeinsame E8-Sektion verträgt sich jetzt mit
der ursprünglichen Farb-/schwachen Markierung, und ein bereits vorhandenes
Vorzeichen macht den nativen kubischen Tensor algebraisch als fermionischen
Massenkoeffizienten verwendbar. Zugleich lässt sich der tatsächliche
Zweiquellen-Hamiltonoperator in einem benannten Kopplungsbereich gemeinsam
für Zustand, Transfer und Observablen reduzieren.

Der verbliebene Anschluss ist damit präziser: **Die Quelle muss eine reale
Wechselwirkung liefern, die den fehlenden Familienkanal erreicht.** Ein weiteres
Nachrechnen desselben einzelnen Higgs-Hintergrunds kann dies in der unten
angegebenen kovarianten Klasse nicht leisten. Das bisherige massive Zusatzpaar
ist im untersuchten Randmodell dynamisch entkoppelt und erzeugt diese
Wechselwirkung ebenfalls nicht von selbst.

Anschaulich: Die Steckverbindungen passen jetzt an zwei zuvor widersprüchlichen
Stellen. Die noch fehlende Verbindung muss aber tatsächlich ein Signal tragen.
Das ist durch eine passende Form und Beschriftung allein nicht bewiesen.

## Was gegenüber dem letzten Ergebnis konkret geändert ist

| Anschluss | Bisher | Jetzt belastbar | Weiter fehlend |
|---|---|---|---|
| E8, Eichmarkierung und Clocks | Zusätzlich gewählte Farbachse; positives Energiebeispiel verletzt ursprünglichen Farbtausch | Hilfsrichtung des schon vorhandenen Zusatzpaares liefert eine gemeinsame positive Sektion; Paarladungen −1,+1 | Herkunft dieser Sektion und der geänderten 10D-Clock-Wirkung; Clocks erhalten feste Hyperladung weiterhin nicht |
| Kubischer Tensor → Fermionmasse | Direkte Übernahme des bosonischen Stromtensors hat falschen vollständigen Austauschtyp | Vorhandene 3+2-Markierung S korrigiert den Austauschtyp exakt auf den tatsächlichen up/down-Higgs-Slots | Physische Umsetzung dieser geordneten Abbildung; dritte Familienmasse |
| Benachbarte Quellen → gemeinsamer Zustand | Lokale Reduktion; benachbarte Ereignisprojektoren kommutieren nicht | Gemeinsamer Nullraum, exakte Komplementlücke und eine gemeinsame Spektralisometrie W für den gesamten Zweiquellenraum unter expliziter Bedingung | Kopplungsauswahl, längere Ketten und Raumzeitgrenzwert |
| Periodenphase → Dynamik | Bedingte Perioden-/Yukawa-Viertelphase | Gemeinsame Quellenphase ist exakt unsichtbar; relative Phase hat eine berechnete reale Operatorantwort | Herleitung der relativen Phase aus a₀ und derselben physikalischen Quelle |

Die QWZ-Quelle, die erweiterte E8-Randtheorie und die native Compilerkette
bleiben dabei verschiedene Konstruktionen. Ihre Identifikation ist nicht
bewiesen. Insbesondere ist die unten konstruierte Zweiquellen-Isometrie W
noch keine Abbildung von dieser Kette in die E8-Rand- oder vierdimensionale
Fermiontheorie.

## 1. Die ursprünglichen Ladungen bestimmen eine bessere Sektion

Im vorhandenen erweiterten Randmodell mit
\(K=\operatorname{diag}(1^9,-1)\) und
\(n=(1,1,1,-1,-1,-1,-1,-1,-1,3)\) wurde bisher zusätzlich die erste
Farbrichtung als Komplement ausgewählt. Bei festgehaltenen alten Clock-Lifts
ist der Konflikt stärker als ein unglückliches Energiebeispiel: Der ursprüngliche
Farbtausch erzwingt für jede gemeinsam invariante symmetrische Energieform
\(n^TVn=0\). Da \(n\ne0\), kann keine dieser Formen positiv definit sein.

Die bereits vorhandene zusätzliche rechte Richtung erlaubt eine Reparatur:
\(e=-e_9\), \(v=n+e_9\). Daraus folgt eine ganzzahlige unimodulare
Zerlegung in E8 und das Zusatzpaar. Sie erhält die ursprünglichen Farb-,
schwachen und Familienblockvertauschungen. Die Paarladungen sind jetzt
\((-1,+1)\), also die kinematischen Plätze des geladenen Lepton-Singulettpaars
im neuen Flavor-Entwurf. Die ursprünglichen Farb- und schwachen Wurzeln
benötigen keine zusätzliche Verkleidung durch die massive Nullrichtung.

Die nativen acht-dimensionalen C-/J-Matrizen bleiben erhalten; ihre
zehn-dimensionalen Wirkungen ändern sich. Auch die neuen Wirkungen erhalten
die feste Hyperladungsmarkierung nicht. Die Rechnung darf daher weder als
unveränderte mikroskopische Clock-Wirkung noch als ladungserhaltende interne
Zeitentwicklung ausgegeben werden. Die Eindeutigkeit der Hilfsrichtung wurde
nur unter neun vorgegebenen Koordinatenachsen gezeigt.

Beleg: [Sektion, exakte Matrizen und Scope](joint/GAUGE_SECTION.md),
[maschinell überprüfte Identitäten](joint/gauge_section.json).

## 2. Ein vorhandenes Vorzeichen repariert den Flavor-Austauschtyp

Der native E6-Kubiktensor ist intern symmetrisch. Sein Familienfaktor lautet
\(A(h)_{ij}=\epsilon_{ijk}h_k\) und ist antisymmetrisch. Die direkte Übernahme
des gesamten Stromtensors wäre damit antisymmetrisch in den vollständigen
Fermionindizes. Eine lokale skalare Kopplung zweier linkshändiger Weyl-Felder
braucht dort einen symmetrischen Koeffizienten.

Der vorhandene 3+2-Träger liefert aber bereits eine diskrete Markierung:
\(S=+1\) auf den schwachen Dubletts Q,L und \(S=-1\) auf den Singuletts
\(u^c,d^c,e^c,\nu^c\). Sie folgt aus der Parität der beiden schwachen
Besetzungszahlen. An den tatsächlichen neutralen up/down-Higgs-Komponenten
des gepinnten 45-Monom-Kubiktensors gilt exakt

\[
\{S,d_H\}=0,\qquad
Y_{\rm mark}=(Sd_H)\otimes A(h),\qquad
Y_{\rm mark}^T=Y_{\rm mark}.
\]

Das ist eine algebraische Reparatur aus vorhandener Markierung, ohne neu
angepasste Flavorzahlen. Sie verwandelt einen bosonischen Stromoperator noch
nicht in ein physisches Fermionfeld. S ist weder die CAR-Fermionparität noch
die Einschränkung der v252-Graduierung auf das gesamte linkshändige
Weyl-Multiplett. Erst die korrekt bezeichnete Umordnung zum Teilchenraum
führt aus dem rechteckigen Massenblock M zum hermiteschen Diracoperator
\(\begin{psmallmatrix}0&M\\M^\dagger&0\end{psmallmatrix}\), der zur
Links-/Rechts-Graduierung ungerade ist. Der Weyl-Koeffizient verwendet dagegen
die symmetrische Ergänzung mit \(M^T\).

Der Rang ändert sich durch S nicht: Jeder einzelne Familienblock hat weiterhin
höchstens Rang zwei. Die vollständige markierte neutrale Higgs-Matrix hat
generisch Rang 16 von 48, entsprechend Rang 8 intern mal Rang 2 in der Familie.

Beleg: [vollständiger Flavor-Nachweis](flavor/PROOF.txt),
[geprüfte originale Ladungs-, Besetzungs- und Tensorplätze](flavor/certificate.json).
Die verwendete Weyl-Austauschregel ist in der Primärdarstellung von
[Dreiner, Haber und Martin](https://arxiv.org/abs/0812.1594) dokumentiert.

## 3. Warum weitere Korrekturen aus nur demselben Hintergrund nicht reichen

Der Ausschluss lässt sich über die einzelne kubische Näherung hinaus beweisen.
Sei F irgendeine wohldefinierte Funktion des einen Familienvektors h mit
den für diesen Koeffizienten vorgeschriebenen Transformationen

\[
 F(gh)=\bar gF(h)\bar g^T\quad(g\in SU(3)),\qquad
 F(e^{it}h)=e^{it}F(h).
\]

Dann folgt allein aus dem Stabilisator von h und seinem Ladungsgrad:

\[
\boxed{F(h)=f(h^\dagger h)A(h),\qquad F(h)h=0.}
\]

Der skalare Faktor f darf beliebig sein; Analytizität ist nicht erforderlich.
Der scheinbar passende ergänzende Rang-eins-Term \(\bar h\bar h^T\)
hat den falschen Higgs-Ladungsgrad −2 statt +1. Die Aussage gilt ausdrücklich
bei exakter SU(3)-Kovarianz, festem Koeffiziententyp und ohne weitere
Familientensoren oder Zustandsdaten. Die vollständige Compilerquelle besitzt
weitere Markierungen; deren möglicher Beitrag ist damit nicht ausgeschlossen.

Auch die bereits geprüften elementaren Umgehungen schließen die Lücke nicht:
\(A(h)FA(h)^T\) behält für jedes F die Nullrichtung h. Im großzügigen
3+1-Massenblock gilt

\[
\det\begin{pmatrix}A(h)&b\\c^T&M\end{pmatrix}
=-(h^Tb)(c^Th).
\]

Beide Überlappungen müssen aus einer wirklichen Kopplung ungleich null werden.
Aus \(b=A(h)u\) oder \(c^T=v^TA(h)\) folgt jeweils wieder null. Eine
Phase ausschließlich in M verschwindet außerdem aus dieser vollständigen
endlichen Determinante.

Die neue Sektion macht das Zusatzpaar passend geladen. In der bisher
verwendeten C/J-invarianten quadratischen Randwirkung ist es jedoch
entkoppelt: \(H=H_{E8}\otimes I+I\otimes H_{\rm Paar}\). Der Projektor
auf einen tatsächlichen Paareigenzustand erfüllt \(QHP=0\). Natürliches
Ausintegrieren dieses Paars erzeugt deshalb in dieser Klasse keine fehlende
Mischung. Nichtfaktorisierende höhere Wechselwirkungen sind offen.

Belege: [Ein-Hintergrund-Satz](joint/ONE_BACKGROUND.md),
[unabhängiger Review](joint/REVIEW_ONE_BACKGROUND.md),
[Komplementidentität und Faktorisierung](flavor/PROOF.txt).

## 4. Der vorhandene Zweiquellenoperator lässt sich gemeinsam reduzieren

Im nativen Operator
\(H=\kappa(L_1+L_2)+J(E_1+E_2)+\mu V\) ist V auf den Quellenlabels
diagonal und auf Materie skalar. Es erhält daher den gemeinsamen
Ereignisnullraum exakt: \(QVP=0\). Die erste reale Leckage kommt aus L.
Ein expliziter nativer Zweig hat \(\|QL_1Px\|^2=1/7200\); sie ist
also nicht nur eine grobe Normabschätzung.

Für zwei benachbarte Quellen ist die kleinste positive Eigenzahl des
vollständigen gemeinsamen Ereignisoperators exakt
\(\delta=2-\sqrt3\). Mit
\(d=J\delta-4\kappa-2\mu>0\) erhält man

\[
\|Qg\|^2\leq\frac{4\kappa^2}{d^2+4\kappa^2}
\]

für einen normierten Grundvektor. Unter der stärkeren hinreichenden Bedingung
\(d>2\kappa\) ist mit dem tatsächlichen unteren Spektralprojektor \(\Pi\)

\[
W=\Pi P(P\Pi P)^{-1/2}
\]

eine gemeinsame Isometrie definiert. Damit werden H, V und alle Observablen
auf denselben wirklichen unteren Spektralraum abgebildet. Die Zustands- und
Transferabbildung müssen nicht mehr unabhängig voneinander gewählt werden.

Dies ist ein Satz im gesamten endlichen Zweiquellenraum unter der genannten
Kopplungsbedingung. Er wählt diese Kopplungen nicht aus, gilt nicht automatisch
für längere Ketten und begründet nicht rückwirkend die schwach gekoppelte
Ising-Näherung. Der frühere positive endliche Vierquellen-Grundzustandssatz
wird dadurch nicht aufgehoben.

Belege: [gemeinsame Spektralreduktion](joint/SPECTRAL_REDUCTION.md),
[native Operatoren und exakter Leckagezeuge](transfer/PROOF.md).

## 5. Für die Phase ist die relative Wirkung entscheidend

Eine gemeinsame kontinuierliche Phase aller Quellenwurzeln lässt den
vorhandenen H exakt unverändert. Die zugehörigen Spektralprojektoren sind
konstant; ihr offener Kato-Paralleltransport ist trivial. Eine zusätzliche
Endpunktvernähung kann weiterhin nichttriviale Holonomie tragen, muss aber
eigenständig hergeleitet werden.

Eine relative Phase zwischen zwei Quellen verändert dagegen
\(V_\delta=1-\operatorname{Re}(e^{i\delta}z)\). Über alle 240²
Quellenlabelpaare ist exakt

\[
\mathbb E[(\operatorname{Re}(e^{i\delta}z))^8]
=\frac{35}{4096}+\frac7{5120}\cos4\delta+\frac1{4096}\cos8\delta.
\]

Bis zur siebten Ordnung sind nur diese vollständigen Labelspurmomente
phasenunabhängig. Gerichtete Observablen wie \(\operatorname{Im}z\)
sehen die relative Quadratur schon unmittelbar. Die Spurdifferenz von
\(V^8\) zwischen \(\delta=0\) und \(\pi/4\) beträgt \(315/2\).
Im vollständigen Zweiquellenraum ist die Differenz des führenden
\(\mu^8\)-Koeffizienten von \(\operatorname{Tr}H^8\) gleich 10080.
Damit ist die relative Diagnose keine bloße Umbenennung für generische μ.

Die zusätzliche Diagnosevariable δ ist weder als natives dynamisches Feld
noch als a₀ identifiziert. Die frühere bedingte Viertelphasenrechnung wird
also präzisiert, nicht in eine abgeleitete CP- oder Axionantwort umgedeutet.

Beleg: [Phasenoperator und vollständiges exaktes Histogramm](phase_operator/PROOF.md).

## Was eine vollständige Lösung jetzt konkret liefern müsste

Für diesen untersuchten Anschluss fehlt ein **aus der gemeinsamen Quelle
hergeleiteter, korrekt graduierter Wechselwirkungskern**, der einen weiteren
Familienkanal erreicht und dieselben Ladungs- und Phasenregeln erfüllt.
Die Quelle muss seine Gruppenwirkung, seinen Zustand, seine relative Phase
und seine Kopplungsstärke bestimmen. Ein frei eingesetztes zusätzliches
Yukawa-Element würde die fehlende Herkunft nur verschieben.

Der nächste entscheidende Nachweis ist deshalb konkret: Einen schon in der
vollständigen Quelle enthaltenen markierten Operator auf den richtigen
Fermionraum abbilden und zeigen, dass er entweder unabhängige äußere
Familienrichtungen oder beide Komplementüberlappungen erzeugt. Zugleich muss
der Operator den richtigen Austauschtyp, die tatsächlichen Eichladungen
und nach der Raumumordnung die Dirac-Graduierung erhalten. Die abstrakte
Möglichkeit zweier unabhängiger Kanäle ist vorhanden; ihre physische Auswahl
ist nicht bewiesen.

Diese Teilherleitungen ersetzen auch nicht die weiter offenen globalen
Anschlüsse: gemeinsame physische Raumzeit und Zeitentwicklung, der
vierdimensionale chirale Grenzwert, die Auswahl des Zustands und der Kopplungen,
die elektromagnetische Antwort aus derselben Quelle und Gravitation.
Kein T1–T8-Gate wird hier als geschlossen markiert. Bereits vorhandene
positive Compiler-, Gitter-, Grundzustands- und bedingte Vorhersageergebnisse
bleiben bestehen; ihre Herkunftsbedingungen werden nicht stillschweigend
mitgelöst.

## Reproduzierbarkeit und Quellenstatus

Die Paketprüfung wiederholt die begrenzten algebraischen Rechnungen,
vergleicht normalen und optimierten Lauf und überprüft die Bytes der
benutzten Originalquellen vor und nach der Rechnung. Sie ersetzt keinen
formalen Beweisassistenten und keine vollständige physikalische Validierung.
Die mathematischen Begründungen und ihre Voraussetzungen stehen in den
verlinkten Proof-Dateien; die Ergebnisdateien enthalten zusätzlich konkrete
Matrizen, Histogramme, Gegenbeispiele und Prüflabel.

Der neue Flavor-Ursprungsstand wurde als gepinnter Entwurf mit eigenen
Voraussetzungen benutzt, nicht als automatisch bestätigte Gesamtherleitung.
Die vorangegangene Archiv- und Lane-Auswertung bleibt über
`../TFPT_Lane_Korrelation_2026-09-20/SYNTHESE.md` und
`../TFPT_Drei_Wege_2026-09-20/ERGEBNIS.md` nachvollziehbar.

Ergebnisse: [zusammengeführtes Zertifikat](results.json),
[Ausführungsnachweis](validation.json),
[Quellenmanifest](source_manifest.json),
[Forschungsindex mit offenen Gates und begrenzten Ausschlüssen](contract_index.json).
