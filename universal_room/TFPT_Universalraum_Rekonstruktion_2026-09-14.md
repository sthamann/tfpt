# TFPT und Universalraum: kanonische Rekonstruktion

Stand: 14. September 2026. Konsolidierter Forschungsstand für Stefan Hamann.

**Status:** Forschungsmanuskript, NON-RH, kein begutachteter Abschluss. Keine
Promotion nach `verification/`, Ledger, Papers oder Website. Die
physikalischen Tore T1–T8 bleiben offen.

## 0. Ergebnis, Evidenz und Quellenhierarchie

Die Arbeitsstände lassen sich zu einem gemeinsamen mathematischen Bild
zusammenführen: TFPT beschreibt markierte algebraische Strukturen und
Operationen; ein vollständiger Prozess legt zusätzlich fest, wie sie
zusammengesetzt, präpariert, ausgeführt und ausgelesen werden. Aus
hinreichend vollständigen Prozessdaten lassen sich TFPT-Strukturen bis auf
operationelle Äquivalenz zurückgewinnen. Die bisher verwendeten Schatten sind
dafür nicht vollständig: Explizite Registerzeugen besitzen gleiche
Ein-Schritt-Ausgaben und verschiedene erlaubte Fortsetzungen.

Eine präzise relative Rekonstruktion ist damit möglich. Nicht bestimmt ist
bislang ein einzigartiger physikalischer Universalraum, der zugleich
Raumzeit, chirale Materie, Kopplungen, Zustand und Gravitation auswählt.
Mehrere Ausführungen erfüllen dieselben endlichen Bedingungen. Ein größerer
Zustandsraum, ein Symmetriename oder eine passende Dimensionszahl beseitigt
diese Mehrdeutigkeit nicht.

Der konsolidierte positive Kern besteht aus:

1. der markierten \(D_5\oplus A_3\)-Verklebung zur \(E_8\)-Hülle;
2. dem passiven Prozess auf 60 Strahlen und seinen zugriffsabhängigen
   Quotienten;
3. dem Vierträger-Hüllensatz und dem exakt lösbaren Tetramer;
4. einer belegungsabhängigen Vermittlung mit kontrolliertem Paarterm;
5. dem allkopplig gelösten Zweizellenmodell;
6. ausführbaren, aber zusätzlich gesteuerten Präparations- und
   Mehrzeitprotokollen;
7. einer operationellen Rekonstruktion aus vollständigen Zukunftstests.

Der stärkste Gesamtkandidat ist eine **einzige reversible lokale
Ereignisregel**, in der \(E_8\) die Vertexgrammatik liefert, aber nicht mit der
gesamten Dynamik gleichgesetzt wird. Dieser Kandidat wird unten vollständig
als Forschungsvertrag formuliert. Er ist keine bewiesene allesumfassende
Lösung.

### Evidenzkonvention

- **gesetzt:** Ausgangsregel, Zustandswahl oder physikalische Zuordnung;
- **exakt:** Identität oder Beweis unter den ausdrücklich genannten
  Voraussetzungen;
- **numerisch:** endliche Rechnung mit ausgewiesener Größe und Genauigkeit;
- **bedingt:** Folgerung nach einer zusätzlichen, benannten Annahme;
- **Gegenmodell:** explizite Widerlegung einer stärkeren Auswahlbehauptung;
- **offen:** Herkunfts-, Eindeutigkeits-, Grenzwert- oder Existenzfrage.

Exakte Mathematik in einem gesetzten Modell ist zugleich *exakt* und
*bedingt*. Viele erfolgreiche Checks sind keine entsprechend vielen
unabhängigen physikalischen Bestätigungen.

### Quellenhierarchie und Versionsgrenze

1. Primärquellen sind das 21-seitige
   [`tfpt_compiler_universalraum_2026-09-13.pdf`](tfpt_compiler_universalraum_2026-09-13.pdf)
   und das 7-seitige
   [`tfpt_anschluss_zellen_seam_2026-09-14.pdf`](tfpt_anschluss_zellen_seam_2026-09-14.pdf).
2. Das 90-seitige
   [`TFPT_Universalraum_Gesamtdarstellung_2026-09-14.pdf`](TFPT_Universalraum_Gesamtdarstellung_2026-09-14.pdf)
   und das
   [`TFPT_Universalraum_LaTeX_Quellen_2026-09-14.zip`](TFPT_Universalraum_LaTeX_Quellen_2026-09-14.zip)
   bilden den eingefrorenen Snapshot v1.1. Das ZIP enthält 46 Dateien und ein
   Manifest mit elf Quellen; sein Eintrag S06 ist bytegleich mit der
   ursprünglichen Fassung dieses Markdown-Manuskripts.
3. Vier maßgebliche Audits liegen außerhalb dieses Snapshots:
   [`TFPT_Rekonstruktion_2026-09-14.md`](TFPT_Rekonstruktion_2026-09-14.md),
   [`TFPT_Sechs_Pruefpunkte_Analyse.md`](TFPT_Sechs_Pruefpunkte_Analyse.md),
   [`TFPT_UNIVERSALRAUM_FUGEN_2026-09-14.md`](TFPT_UNIVERSALRAUM_FUGEN_2026-09-14.md)
   und
   [`TFPT_UNIVERSALRAUM_Q_AUDIT_UND_U_REGEL_2026-09-14.md`](TFPT_UNIVERSALRAUM_Q_AUDIT_UND_U_REGEL_2026-09-14.md).
   Ihre expliziten Gegenbeispiele und stärkeren Sätze ersetzen widersprechende
   Formulierungen des Snapshots.

Die im Snapshot verarbeiteten Markdown-Arbeitsstände bleiben als Provenienz
erhalten:
[`TFPT_Fortsetzung.md`](TFPT_Fortsetzung.md) trennt die Prozessklassen und
korrigiert die Vermittlung,
[`Analyse_und_Rekonstruktion.md`](Analyse_und_Rekonstruktion.md) formuliert
die operationelle Rekonstruktion,
[`TFPT_UNIVERSALRAUM_INVERSION_2026-09-14.md`](TFPT_UNIVERSALRAUM_INVERSION_2026-09-14.md)
liefert die Schattenzeugen,
[`TFPT_Omega_Praeparation_Mehrzeittest_2026-09-14.md`](TFPT_Omega_Praeparation_Mehrzeittest_2026-09-14.md)
die ausführbare Präparation,
[`TFPT_TOE_GEMEINSAMER_URSPRUNG_2026-09-14.md`](TFPT_TOE_GEMEINSAMER_URSPRUNG_2026-09-14.md)
die Zweizellen- und Propagatorbrücke und
[`TFPT_UNIVERSALRAUM_GESAMTSYNTHESE_2026-09-14.md`](TFPT_UNIVERSALRAUM_GESAMTSYNTHESE_2026-09-14.md)
die frühe, an mehreren Stellen später korrigierte Gesamtsicht.

Notation: \(U_{\rm proc}\) bezeichnet einen vollständigen Prozess,
\(U_{\rm mess}\) die konkrete involutive Vormessung und \(U_{\rm step}\) den
unten formulierten Kandidaten einer primitiven Ereignisregel.

## 1. Der algebraische Kern

TFPT besitzt einen substanziellen algebraischen Kern. Die historische Schnittstelle besteht aus einem orientierten Rand beziehungsweise einer Naht mit positivem Kern und Normierung \(c_3=1/(8\pi)\), sowie einem fünfteiligen Träger mit einer später als \(3+2\) interpretierten Zerlegung. Das sind strukturelle Annahmen. Die Kurzform „zwei Zahlen“ beschreibt ihren Informationsgehalt unzureichend: Orientierung, Positivität, Trägerart und Auslesung gehören dazu.

Aus dem komplexen Fünferträger entsteht die gerade äußere Algebra

\[
S^+=\Lambda^{\mathrm{even}}\mathbb C^5,
\qquad \dim S^+=1+10+5=16.
\]

Damit steht eine konkrete Spinorstruktur zur Verfügung. Hyperladung und ihre Anomaliesummen sind innerhalb der gewählten Darstellungszuordnung kontrollierbar. Die Verklebung von \(D_5\) und \(A_3\) liefert unter ihrer markierten \(\mathbb Z_4\)-Identifikation die E₈-Hülle. Das ist wesentlich stärker als die isolierten Dimensionsgleichungen \(5+3=8\) oder \(45+15+64+64+60=248\).

Die endliche Seite desselben Programms liefert im ausgewählten komplexen Viererträger 60 Strahlen in 15 vollständigen Messkontexten. Ihre Projektoren, Überlappungen und Symmetrien sind explizit vorhanden. Auch die gemeinsame Verwendung kleiner dimensionsloser Parameter macht das Programm prüfbar: Eine Änderung am Seed verschiebt mehrere Ausgaben gleichzeitig.

Ich habe den elektromagnetischen Formelwert und den Flavor-Seed unabhängig nachgerechnet:

\[
\varphi_0=\frac1{6\pi}+48c_3^4
=0{,}0531719521768455\ldots,
\]
\[
\lambda_C=\sqrt{\varphi_0(1-\varphi_0)}
=0{,}2243762368847218\ldots,
\qquad
\alpha^{-1}=137{,}0359992168407125\ldots.
\]

Der Vergleich mit dem ausdrücklich datierten CODATA-2022-Wert \(137{,}035999177(21)\) ergibt etwa 1,897 experimentelle Standardabweichungen. Die NIST-Tabelle wurde direkt überprüft. Das ist ein genauer Formelwert nahe einer Messgröße. Für eine physikalische Vorhersage bleibt zu zeigen, warum die Quellgleichung genau die Thomson-Kopplung liefert; eine vollständige Theorieunsicherheit ist durch die hohe Rechengenauigkeit nicht bestimmt. [NIST/CODATA](https://physics.nist.gov/cuu/Constants/Table/allascii.txt)

Bei den übrigen phänomenologischen Ausgaben sind Schema und Eingaben entscheidend. Eine Quellmasse ist nicht automatisch eine Polmasse. Ein aus Oszillationssplittings gebildeter Neutrinosummenwert enthält diese Splittings als Inputs. Eine Ausgabe in GeV benötigt den dimensionalen Skalenanker. Das Hauptmanuskript benennt selbst ungünstige Leptonverhältnisse, eine zu kleine einfache Inflationsamplitude und einen verfehlten älteren Higgs-Zweig. Die Universalraum-Idee erklärt diese Abweichungen bisher nicht. Sie wäre erst dann eine Verbesserung, wenn sie einen vorher festgelegten Transfer aus derselben Dynamik herleitet.

Der physikalische Abschluss ist deshalb weiterhin umfassender als die endliche Algebra: Eine gemeinsame lokale Dynamik in 3+1 Dimensionen, chirale Materie mit Spiegelentkopplung, wechselwirkender Kontinuumsgrenzwert, physikalischer Zustand, vollständige Kopplungen und universell gekoppelter quantisierter Spin 2 sind nicht gemeinsam konstruiert. Dies stimmt mit der aktuell gelesenen Datei `docs/OPEN_PROBLEMS.md` überein. Ein erneuter Gesamt-Lean-Lauf und eine vollständige externe Datenanpassung waren nicht Teil dieser Analyse.

## 2. Zwei Rekonstruktionsrichtungen

Die beiden Richtungen beantworten zunächst verschiedene Fragen. Mit \(T\) als TFPT-Präsentation, \(U_{\rm proc}\) als vollständigem Prozess und \(P\) als Auslesung lautet die erste Richtung schematisch

\[
(T,\theta)\longmapsto U_{{\rm proc},T,\theta}.
\]

Hier enthält \(\theta\) die bisher zusätzlichen Angaben: Kopplungen, Zustand, Kontextregel, Registerprotokoll, Zeitstruktur und gegebenenfalls Grenzwert. Die zweite Richtung lautet

\[
U_{\rm proc}\overset{P}{\longmapsto}T.
\]

Im ersten Fall entsteht eine Realisierung aus einer Beschreibung; im zweiten entsteht eine Beschreibung aus beobachtbaren Strukturen. Beide Richtungen können gleichzeitig gelten. Daraus folgt keine zeitliche oder ontologische Selbsterschaffung.

Für eine echte inverse Rekonstruktion müsste zusätzlich gelten:

\[
P(U_1)=P(U_2)\quad\Longrightarrow\quad U_1\simeq U_2,
\]

wobei \(\simeq\) Äquivalenz unter allen zugelassenen Experimenten bezeichnet. Die Registerzeugen widerlegen diese Aussage für die bloße Systemauslesung. Deshalb ist die Umkehrhypothese eine sinnvolle Deutung der Unvollständigkeit des Schattens, aber noch kein Beweis, dass TFPT ontologisch aus einem bestimmten tieferen Raum entsteht.

## 3. Prozess, Register und Schatten

Der Registerzeuge trägt, seine Reichweite muss präzise bleiben. Im tatsächlichen Quellmodell besitzt die Vormessung \(U_{\rm mess}\) die Eigenschaft \(U_{\rm mess}^2=I\). Ein kohärent behaltenes Register und eine dephasierte Alternative können denselben sichtbaren Systemzustand \(I_4/4\) besitzen. Dieselbe Fortsetzung mit \(U_{\rm mess}\) liefert anschließend einmal einen reinen Zustand und einmal wieder \(I_4/4\). Daher gibt es auf diesem Schatten keine für alle diese inneren Zustände gültige autonome Entwicklung.

Das ist ein exakter Nachweis verlorener Vorhersageinformation. Er sagt nicht, dass jede TFPT-Auslesung nichtautonom ist: Für das ausdrücklich eingeschränkte Protokoll mit frischen Registern existiert eine autonome reduzierte Regel. Ebenso gelten auf dem ursprünglichen 60-Strahlen-Modell genau die Beziehungen

\[
CT=KC,\qquad FT=\frac37F.
\]

Es gibt hier drei unterschiedliche Klassen: Verteilungen über die bereits gemessenen 60 Strahlen; allgemeine klassische Kontext-Quanten-Zustände; und kohärente System-Register-Zustände. Aussagen zwischen diesen Klassen zu übertragen verursacht einen scheinbaren Widerspruch. Ein System kann auf der größeren Ebene einen vollständigen Zustand besitzen und auf der kleineren Ebene ein Prozess mit Gedächtnis sein. Der Befund erzwingt daher keinen Gegensatz zwischen „Zustandsraum“ und „Prozessraum“.

Dies ist eng mit der etablierten Theorie von Prozesstensoren verbunden. Dort wird ein Prozess durch seine Antworten auf Folgen von Eingriffen beschrieben, sodass auch Gedächtnis erfasst wird, das in einzelnen Dichteoperatoren nicht sichtbar ist. TFPT liefert hierfür einen konkreten kleinen Testfall; die allgemeine Idee ist bereits Teil der Theorie offener Quantensysteme. [Pollock et al., Operational Markov condition for quantum processes](https://arxiv.org/abs/1801.09811)

### 3.1 Minimalität ist zugriffsabhängig

Die behauptete Minimalität des vollen CQ-Zustands ist nicht bewiesen; für die im Folgenden festgelegte Auslesung ist sie zu stark. Der Originalprüfer konstruiert zwei Zustände mit gleichen Marginalien und verschiedenen nächsten Marginalien. Damit widerlegt er eine bestimmte Kompression. Er untersucht nicht alle kleineren Beschreibungen.

Die konkrete CQ-Regel lautet

\[
(\mathcal L\sigma)_D=\sum_C K_{DC}\Delta_D(\sigma_C),
\qquad K=B/7,
\]

mit 15 positiven \(4\times4\)-Blöcken \(\sigma_C\), deren Spuren sich zu eins summieren. Der allgemeine CQ-Raum hat 240 reelle lineare Koordinaten, beziehungsweise affine Dimension 239 nach Normierung. Für einen festgelegten Ablauf ohne Eingriffe, bei dem für jeden Horizont getrennt nur System- und Kontextmarginalie ausgewertet werden, reicht jedoch eine kleinere Beschreibung.

Seien \(P_u\), \(u=1,\ldots,15\), die nichttrivialen Paulis und

\[
p_C=\operatorname{tr}\sigma_C,
\qquad a_{uC}=\operatorname{tr}(P_u\sigma_C),
\qquad x_u=\sum_C a_{uC}.
\]

Setze \(m_{uC}=1\), wenn Kontext \(C\) das Pauli \(P_u\) enthält, sonst null, und

\[
y_u=\frac17\sum_C(1+2m_{uC})a_{uC}.
\]

Die Quellinzidenz ergibt exakt

\[
\boxed{p'=Kp,\qquad x'_u=y_u,\qquad y'_u=\frac37y_u.}
\]

Begründung: Die Dephasierung in Kontext \(D\) erhält \(P_u\) genau dann, wenn \(m_{uD}=1\). Die 15 Kontextkoeffizienten eines Paulis entwickeln sich mit \(L_u=\operatorname{diag}(m_u)K\). Jedes Pauli liegt in drei Kontexten. Aus den tatsächlichen Quellmatrizen folgt

\[
\mathbf1^T L_u=\frac17(\mathbf1^T+2m_u^T),
\qquad
\mathbf1^T L_u^2=\frac37\mathbf1^T L_u.
\]

Die beiden Zeilen \(\mathbf1^T\) und \(\mathbf1^TL_u\) sind linear unabhängig. Zusammen mit den 15 unabhängigen Kontextspuren ergibt das einen beobachtbaren linearen Rang von \(15+2\cdot15=45\). Nach Normierung verbleiben **44 unabhängige reelle Größen**. Das ist die minimale affine lineare Beschreibung relativ zu genau diesen passiven Marginalausgaben; der positive Zustandsbereich ist das Bild der CQ-Zustandsmenge und kein beliebiger 44-dimensionaler Würfel.

Die Gegenprüfung benutzt auch positive Zustände. Für ein Pauli \(P\), das in zwei Kontexten \(C_0,C_1\) liegt, wähle

\[
\sigma_C^\pm=\frac{I_4}{60}\pm\frac{v_C}{120}P,
\qquad v_{C_0}=1,\quad v_{C_1}=-1,
\]

mit sonst \(v_C=0\). Alle Blöcke sind strikt positiv. Die beiden CQ-Zustände unterscheiden sich, besitzen aber dieselben \(p,x,y\) und damit dieselben hier betrachteten Marginalausgaben zu allen zukünftigen Zeiten.

Auf der bereits gemessenen Strahlenklasse gilt darüber hinaus \(y=(3/7)x\). Dort reichen 30 lineare beziehungsweise 29 normierte affine Koordinaten. Die 30 Nullrichtungen der 60-dimensionalen Übergangsmatrix werden tatsächlich ausgelöscht. Sie sind kein verstecktes Gedächtnis dieses Übergangs.

| Beschreibung | Lineare Dimension | Dimension nach Normierung | Gültigkeit |
|---|---:|---:|---|
| Allgemeiner CQ-Zustand | 240 | 239 | Beliebige positive Kontextblöcke |
| Bild nach einer CQ-Messrunde | 60 | 59 | Jeder Ausgangsblock diagonal in seinem Kontext |
| Vorhersagegrößen \((p,x,y)\) | 45 | 44 | Festes \(\mathcal L\), separat ermittelte Marginalien aller Horizonte |
| Strahlen-Marginalquotient \((p,x)\) | 30 | 29 | Bereits gemessene Strahlenklasse, dieselbe eingeschränkte Auslesung |

Diese Reduktion gilt ausdrücklich nicht für beliebige selektive Messgeschichten, Kontext-System-Korrelationen am selben Zeitpunkt oder kohärente Eingriffe in Register. Mit zusätzlichem Zugriff können zuvor unsichtbare Richtungen sichtbar werden. Die richtige Minimalitätsfrage lautet immer: minimal für welche Präparationen, Eingriffe und Ausgaben?

### 3.2 Die Kontextregel und ihr fehlendes Auswahlprinzip

Die kovariante Konstruktion von \(K=B/7\) ist korrekt, wählt die Regel aber nicht allein durch Symmetrie aus. Der Follow-up-Prüfer zerlegt die siebenreguläre bipartite Inzidenzmatrix als \(B=\sum_{j=1}^7P_j\) und mittelt die sieben Permutationen mit gleichen Gewichten. Danach wird unter der Symplektikgruppe konjugiert. Weil \(B\) invariant ist, gilt bereits algebraisch

\[
\frac1{|G|\,7}\sum_{g\in G}\sum_jgP_jg^{-1}
=\frac1{|G|\,7}\sum_ggBg^{-1}=\frac B7.
\]

Die 4500 verschiedenen Orbit-Matchings sind interessante kombinatorische Daten dieser Zerlegung. Die Gleichgewichtung war jedoch schon in \(\frac17\sum_jP_j\) enthalten. Sie folgt nicht erst daraus, dass die Konjugationsgruppe 720 Elemente besitzt.

Ein explizites Gegenmodell zur Symmetrie-Eindeutigkeit ist

\[
K_{\mathrm{alt}}=\frac12I+\frac1{12}(B-I).
\]

Es ist stochastisch, besitzt denselben Inzidenzträger und dieselbe Symmetrie, unterscheidet sich aber von \(B/7\). Symmetrie kann den Selbstübergang und die sechs anderen inzidenten Nachfolger verschieden gewichten. Die Markierung \(a=1/7\) benötigt eine zusätzliche Auswahl, etwa die gleichgewichtete Matching-Ausführung, maximale Übergangsentropie oder das benannte Auslöschungsprinzip. Eine davon dynamisch aus der Quelle herzuleiten bleibt eine echte Aufgabe. „Zur Hälfte geschlossen“ ist hier keine mathematisch definierte Fortschrittsgröße.

Innerhalb der ausdrücklich eingeschränkten Familie

\[
K_a=aI+\frac{1-a}{6}(B-I)
\]

ist der induzierte Strahlenprozess

\[
T_a=\frac{7(1-a)}6T+\frac{7a-1}{6}I_{60}.
\]

**Exakt:** \(a=1/7\) ist in dieser Familie die eindeutige Wahl mit Rang 30;
generisch ist der Rang 60. **Bedingt:** Das zusätzliche Prinzip „maximale
einmalige Kompression“ würde \(B/7\) auswählen. Dass dieses Prinzip
fundamental gilt, ist offen.

## 4. Zelle, Hülle und Dynamik

### 4.1 Der Hüllensatz

Der Hüllensatz für die Vierträgerzelle ist richtig, die physikalische Prämisse ist stärker als die E₈-Zerlegung. Für einen Zustand auf \((\mathbb C^4)^{\otimes N}\) erzwingt die Bedingung

\[
\operatorname{supp}\rho_{ij}\subseteq\Lambda^2\mathbb C^4
\quad\text{für alle Paare}
\]

die totale Antisymmetrie. Denn jeder Swap hat auf dem Zustand Eigenwert \(-1\), und Transpositionen erzeugen die Permutationsgruppe. Für \(N=4\) bleibt das eindeutige Singulett

\[
|\Omega\rangle=\frac1{\sqrt{24}}\sum_{\pi\in S_4}
\operatorname{sgn}(\pi)|\pi(0,1,2,3)\rangle.
\]

Für \(N\ge5\) existiert kein solcher Zustand. Dass \(N=2,3\) ebenfalls antisymmetrische Zustände erlauben, zeigt zugleich: Genau vier Träger werden erst mit einer zusätzlichen Forderung wie maximaler Größe oder eindeutiger Singulettzelle ausgewählt.

In der E₈-Adjungierten tritt unter \(D_5\times A_3\) der Sektor \((10,6)\) auf; der symmetrische SU(4)-Zweiträgersektor \(10\) tritt in dieser Zerlegung nicht als entsprechender Bestandteil auf. Daraus folgt eine Auswahlregel für diese Adjungiertenstruktur und ihre Klammer. Es folgt nicht automatisch, dass im Hilbertraum zweier unabhängiger physischer Träger alle symmetrischen Zustände verboten sind. Dafür braucht man eine konkrete Zuordnung zwischen der Lie-Algebra-Zerlegung, physischen Freiheitsgraden und erlaubtem Zustandsraum.

Ein einfaches mathematisches Gegenbeispiel ist \(|0\rangle^{\otimes4}\): Es liegt im Träger-Tensorprodukt und ist für alle Paare symmetrisch. Die vorhandene SU(4)-Wirkung oder eine als Observable definierte antisymmetrisierende Klammer entfernt diesen Zustand nicht. Erst eine harte Einschränkung oder ein energetischer Mechanismus tut das.

Auch die Grundzustandskenntnis bestimmt die Dynamik nicht. Alle Hamiltonoperatoren

\[
H_{\mathbf J}=\sum_{i<j}J_{ij}\frac{I+S_{ij}}2,
\qquad J_{ij}>0,
\]

besitzen dieselbe eindeutige Vierträger-Nullmode \(\Omega\). Ihre Anregungsspektren unterscheiden sich. Als numerische Gegenprobe wurden die sechs Gewichte \(1,2,3,4,5,6\) verwendet: Der Grundzustand bleibt eindeutig, die Lücke beträgt etwa 3,847309 in diesen Einheiten; beim gleichgewichteten Modell beträgt sie 2. Die beiden Operatoren unterscheiden sich auch nach Herausrechnen einer gemeinsamen Skala.

Ein zusammenhängender, positiv gewichteter Austauschgraph auf vier Trägern genügt bereits für dieselbe Nullmode: Seine Kantentranspositionen erzeugen \(S_4\). Deshalb wählt der Grundzustand auch den vollständigen Sechs-Kanten-Graphen nicht aus. Bei mehr als vier über harte antisymmetrische Kanten verbundenen Trägern ist die gemeinsame Nullmode dagegen unmöglich. Vielzellenmodelle benötigen daher eine endliche energetische Strafe oder eine abgeschwächte Randbedingung an den Brücken.

### 4.2 Drei Graphrollen dürfen nicht verschmolzen werden

Der vollständige Vierergraph \(K_4\) definiert den exakt lösbaren
Tetramer-Elternoperator. Der Clebsch-Graph \((16,5,0,2)\) entsteht dagegen
**exakt unter der gesetzten Lesart** „Ort = Spinorgewicht“ aus der
gleichgradigen \(E_8\)-Klammer und besitzt 16 Knoten und 40 Kanten. Die
uniforme SU(4)-Kette ist ein drittes Modell für die Untersuchung eines
kritischen Grenzfalls. Gemeinsamer lokaler Träger und gemeinsame
Austauschform machen diese drei Hamiltonoperatoren nicht identisch.

Der Fugen-Audit ergibt unter der Clebsch-Lesart einen uniformen positiven
Paarterm

\[
J_{\rm eff}=\frac{2t^2}{\Delta_{\rm eff}}>0.
\]

Graph und Uniformität sind dann bestimmt; die Ortslesart, Statistik,
\(t\), \(\Delta_{\rm eff}\) und der Fockraum bleiben zusätzliche Daten. Das
erste angeregte Singulettniveau des Clebsch-Modells ist numerisch mindestens
vierfach und nicht das im Snapshot behauptete Dublett. Die Aussage
„Clebsch-Singulett“ darf außerdem nicht ohne Sektorprüfung zum globalen
Grundzustandssatz verstärkt werden.

Ist die reduzierte Dichtematrix einer Zelle exakt rein
\(|\Omega\rangle\langle\Omega|\), faktorisiert jeder Gesamtzustand über diese
Zelle. Ein gekoppeltes Netz kann daher nicht zugleich unverändert reine
\(\Omega\)-Marginalien und Verschränkung zwischen den Zellen besitzen.
Konsistent ist \(\Omega\) als isolierter Referenzzustand, Eltern-Groundstate
oder lokale Verknüpfungsamplitude; bei Kopplung dürfen sich die Marginalien
ändern.

### 4.3 Präparation und ihre Zusatzressource

Die Präparation von \(\Omega\) benötigt im beschriebenen Qubit-Baukasten eine zusätzliche Ressource. Seine Paarmarginalie lautet

\[
\rho_{ij}=\frac{I-S_{ij}}{12}
\]

und besitzt Rang 6 mit sechs Eigenwerten \(1/6\). Für einen reinen Stabilizer-Zustand ist jede Reduktion auf eine Qubit-Teilmenge ein normierter Stabilisatorprojektor; ihr Rang ist eine Zweierpotenz. Rang 6 schließt damit aus, dass \(\Omega\) ein reiner achtqubitiger Stabilizer-Zustand in der festgelegten Kodierung ist. Das folgt auch aus der bekannten ganzzahligen bipartiten Stabilizer-Entropie: Hier ist sie \(\log_2 6\). [Fattal et al., Entanglement in the stabilizer formalism](https://arxiv.org/abs/quant-ph/0406168)

Clifford-Gatter, Stabilizer-Präparationen und Pauli-Messungen mit klassischer Rückkopplung können diesen reinen Zustand folglich nicht exakt präparieren, auch nicht durch eine erlaubte Folge solcher Messungen mit Nachselektion. Man muss eine Ressource außerhalb dieser Klasse identifizieren. Kandidaten sind eine geeignete nicht-Cliffordsche kontinuierliche Austauschdynamik, eine andere Messoperation oder eine zusätzliche Zustandsquelle. Ein unitärer Swap ist selbst ein Clifford-Gatter; daraus folgt nicht, dass beliebige kontinuierliche Entwicklungen \(e^{-itS}\) oder eine Messung des Swap-Eigenwerts zur gleichen freien Operationsklasse gehören.

Das macht die offene Präparationsfrage schärfer: Sie ist im eingeschränkten Baukasten ein konkretes Hindernis, das durch bloßes weiteres Zusammensetzen derselben erlaubten Gatter nicht verschwindet. Diese Aussage ist relativ zur genannten Kodierung und Operationsklasse. Sie ist kein allgemeines Präparationsverbot für das Singulett.

Der spätere Präparationsanschluss löst die **Ausführungsfrage bedingt**. Der
Antisymmetrisierer

\[
A_4=\frac1{24}\sum_{\pi\in S_4}\operatorname{sgn}(\pi)U_\pi
=|\Omega\rangle\langle\Omega|
\]

wurde als vollständige \(256\times256\)-Matrix geprüft. Kontrollierte Swaps
liefern eine konkrete nichtstabilisierende Ressource; das 20-Qubit-Protokoll
reproduziert nach erfolgreicher Präparation die Mehrzeit-Rückkehrwerte

\[
F_{\rm behalten}=1,\qquad F_{\rm frisch}=\frac{17}{32}.
\]

Einschließlich beider Filter betragen die gemeinsamen Rohwahrscheinlichkeiten
\(27/512\) und \(459/16384\). Ein separates ideales Achtpunkt-Energiefilter
des Tetramers realisiert

\[
P_\Omega=\frac18\sum_{k=0}^7
\exp\!\left(-\frac{2\pi i kH_{\rm tet}}{8J}\right)
\]

und erhöht am benannten Eingang die Projektionsausbeute von \(3/32\) auf
\(1/6\). Beide Konstruktionen setzen kontrollierte Entwicklung,
Hilfszustände, Registerauslesung und eine Energieskala voraus. Sie zeigen
Ausführbarkeit in ergänzten Modellen, nicht die Herkunft dieser Kontrolle aus
P1/P2.

## 5. Vermittlung und Kopplung

### 5.1 Die beiden \(E_8\)-Klammerkanäle

Die vorgeschlagene Superaustauschrechnung muss zwei Klammerkanäle auseinanderhalten. Die direkte Wurzelprüfung bestätigt 960 geordnete Wurzelpaare für

\[
[(16,4),(16,4)]\longrightarrow(10,6).
\]

Für den gemischten Kanal gilt dagegen

\[
[(16,4),(\overline{16},\overline4)]
\longrightarrow(45,1)\oplus(1,15).
\]

Die unabhängige Enumeration ergibt hier 640 nichtverschwindende Wurzelsummen im ersten und 192 im zweiten Sektor; außerdem gibt es 64 Gegenwurzelpaare mit möglichem Cartan-Beitrag. Es gibt keinen \((10,6)\)-Zielsektor dieser gemischten Wurzelklammer. Das stimmt mit \(16\otimes\overline{16}=1\oplus45\oplus210\) und \(4\otimes\overline4=1\oplus15\) überein. Der nächste Schritt auf Seite 6 des Anschluss-Papers vermischt diese Kanäle und sollte vor einer effektiven Kopplungsrechnung korrigiert werden.

Ein kleiner konstruktiver Mechanismus lässt sich dennoch genau angeben. Sei \(P_-=\frac12(I-S)\) der antisymmetrische Zweiträgersektor. Ein Übergang \(W\) in einen Hilfssektor der Energie \(\Delta>0\), mit \(W^\dagger W=P_-\), erzeugt für die Kopplung \(g(W+W^\dagger)\) in zweiter Ordnung

\[
H_{\mathrm{eff}}=-\frac{g^2}{\Delta}P_-
=\frac{g^2}{\Delta}P_+-\frac{g^2}{\Delta}I.
\]

Bis auf die additive Konstante entsteht tatsächlich das Vorzeichen des Tetramer-Elternoperators. Das ist eine explizite hinreichende Konstruktion unter zusätzlichen Annahmen. Sie erklärt auch, warum Strukturkonstanten allein \(J\) oder \(\lambda\) noch nicht festlegen: Man benötigt die Kopplung \(g\), den Energieabstand \(\Delta\), den ausgewählten Hilfssektor und die Liste der gekoppelten Paare. Die Lie-Klammer kann die Form von Übergängen einschränken; diese Energie- und Graphdaten folgen daraus nicht ohne weitere Dynamik. [Bravyi, DiVincenzo und Loss, Schrieffer-Wolff transformation](https://arxiv.org/abs/1105.0675)

### 5.2 Globaler Klammerkern und lokale Energie sind verschieden

Für eine einzelne Kante gilt exakt

\[
K_e^\dagger K_e=I-S_e=2P^-_e.
\]

Werden jedoch vier Clebsch-Kanten mit demselben Vermittlerlabel kohärent in
denselben Zielraum abgebildet, können sich Amplituden verschiedener Kanten
auslöschen. Für den gesamten gleichgradigen Klammeroperator gilt

\[
Q_{11}:g_1\otimes g_1\to g_2,\qquad
\operatorname{rank}Q_{11}=60,\qquad
\dim\ker Q_{11}=4036.
\]

Darum ist der globale Projektor \(P_{\ker Q_{11}}\) nicht die Summe der
lokalen Projektoren \(P_{\ker K_e}\). Ein Hamiltonoperator
\(\sum_eP_e^+\) ist eine zusätzliche Ausführungsregel, solange der Prozess
nicht erklärt, wodurch die Kantenwege unterscheidbar bleiben.

### 5.3 Belegung löst die zweite Ordnung, nicht alle Ordnungen

Ein konkreter Kandidat gibt jedem Ort den Raum

\[
H_s=\mathbb C|\emptyset\rangle\oplus\mathbb C^4
\]

und erhält einen vollständig besetzten Niedrigenergiesektor. Ein Vertex
entfernt die beiden Belegungen einer Kante und erzeugt einen Vermittler. Die
zurückbleibenden Löcher speichern, welche Kante benutzt wurde. Bei der
Rückprojektion gilt deshalb für \(e\ne f\)

\[
PK_{e,A}^\dagger K_{f,A}P=0.
\]

Mit \(\Delta_{\rm eff}>0\) folgt in zweiter Ordnung

\[
H_{\rm eff}^{(2)}
=-\frac{t^2}{\Delta_{\rm eff}}\sum_eK_e^\dagger K_e
=\frac{2t^2}{\Delta_{\rm eff}}\sum_eP_e^+
+\text{Konstante}.
\]

Das ist ein exakter Satz im benannten Belegungsmodell. In vierter Ordnung
bleiben bei gemeinsam benutzten Vermittlern echte Vierträgerterme, im
geprüften Zwei-Kanten-Modell etwa

\[
H_{\rm eff}^{(4)}
=\frac{16t^4}{\Delta_{\rm eff}^3}
P_-^{(\mathrm{Paarlabels})}.
\]

Ihr relatives Gewicht skaliert wie
\((t/\Delta_{\rm eff})^2\), verschwindet aber nicht durch den Namen
\(E_8\). Ein kontrollierter Vielzellenlimes benötigt lokale
Fehlerabschätzungen und darf nicht allein aus einer kleinen endlichen
Gesamtnorm gefolgert werden.

Die Aufzeichnung liegt im symmetrischen Sektor
\(\operatorname{Sym}^2(4)\), der in der 248 nicht als entsprechender
Cross-Register-Kanal vorkommt. **Exaktes Negativresultat:** Die gepinnte
248-Klammer allein erzeugt diese Aufzeichnung nicht. Eine größere Darstellung
wie die 3875 oder \(U_{\rm step}\) kann sie nur als ausdrücklich neue
Struktur einführen.

## 6. Zwei Zellen: ein vollständig gelöster endlicher Sektor

Für zwei vollständige Tetramerzellen mit genau einer Brücke

\[
H=H_A+H_B+\lambda P^+_{ab},\qquad J>0,\quad\lambda\ge0,
\]

setze

\[
R=\sqrt{16J^2-2J\lambda+\lambda^2},\qquad
Q=\sqrt{4J^2+\lambda^2}.
\]

Dann gelten für jede endliche positive Kopplung

\[
E_0=\frac{4J+\lambda-R}{2},\qquad
E_1=3J+\frac\lambda2-\frac Q2,
\]

\[
\boxed{\Delta_{\rm gap}=E_1-E_0
=J+\frac{R-Q}{2}>\frac J2.}
\]

Der Grundzustand ist eindeutig. Die frühere Marke
\(\lambda<8J\) war nur die Grenze eines älteren Beweises; bei
\(\lambda=8J\) beträgt die Lücke noch ungefähr \(0{,}876894J\), und für
\(\lambda\to\infty\) nähert sie sich \(J/2\). Dieser Satz betrifft zwei
\(K_4\)-Zellen mit einer Brücke. Er ist kein allkoppliger Satz für den
Clebsch-Graphen und kein thermodynamischer Vielzellennachweis.

## 7. Uhr, Mehrzeitprozess und Zeitpfeil

### 7.1 Eine relationale Vier-Anzeigen-Uhr

Die Uhrfrage lässt sich konstruktiv verbessern. Das Anschluss-Paper zeigt richtig, dass ein auf einem Träger angewendeter unitärer Tick am Singulett sichtbar wird:

\[
\langle\Omega|A_1|\Omega\rangle=\frac14\operatorname{tr}A,
\qquad
p_{1j}=\frac{16-|\operatorname{tr}A|^2}{24}.
\]

Die zweite Formel gilt in dieser Form für unitäres \(A\); bei einem allgemeinen nichtunitären Filter müssen Normierung und Erfolgswahrscheinlichkeit mitgeführt werden. Die Periode 3 in den Paartests ist ein reales endliches Lesemuster. Die Periode 12 eines gewählten Lifts benötigt eine relative Phasenreferenz. Beides setzt zunächst voraus, dass ein Tick angewendet wird; eine autonome Uhrendynamik folgt daraus noch nicht.

Die Inversionsnotiz findet für den gleichgewichteten System-Swap-Hamiltonoperator drei Energieniveaus. Ein stärkeres Argument erfasst unmittelbar den relevanten Zustandssektor: Auf \(\Lambda^3\mathbb C^4\) wirkt jede Systemtransposition als \(-I\). Die gesamte durch diese Permutationen erzeugte Algebra wirkt dort skalar. Deshalb kann keine aus dieser Algebra allein gewählte Dynamik die vier antisymmetrischen bedingten Zustände nichttrivial ineinander entwickeln. Ein allgemeines Uhrverbot folgt daraus nicht. Auch die Zahl unterscheidbarer Uhranzeigen ist außerhalb der dort gewählten idealen nichtentarteten Uhrklasse nicht einfach gleich der Zahl orthogonaler Energieniveaus.

Eine genaue Ergänzung derselben Zelle ist folgende. Schreibe

\[
|\Omega\rangle=\frac12\sum_{a=0}^3|a\rangle_C|\omega_a\rangle_S,
\]

wobei die \(\omega_a\) orthonormale antisymmetrische Zustände der übrigen drei Träger sind. Wähle dimensionslos

\[
h=\operatorname{diag}(0,1,2,3)
=\frac32I-Z_1-\frac12Z_2,
\qquad
H_S=h_1+h_2+h_3-6I.
\]

Da \(\omega_a\) genau die drei anderen Basiswerte enthält, gilt

\[
H_S\omega_a=-a\omega_a,
\qquad (h_C+H_S)\Omega=0.
\]

Definiere die vier Uhranzeigen durch die Fourierbasis

\[
|t_k\rangle=\frac12\sum_{a=0}^3i^{-ak}|a\rangle,
\qquad k=0,1,2,3.
\]

Jede Anzeige tritt mit Wahrscheinlichkeit \(1/4\) auf. Der normierte bedingte Systemzustand ist

\[
|\phi_k\rangle=\frac12\sum_{a=0}^3i^{ak}|\omega_a\rangle,
\]

und erfüllt exakt

\[
\boxed{e^{-iH_S\pi/2}|\phi_k\rangle=|\phi_{k+1\;\mathrm{mod}\;4}\rangle.}
\]

Die vier Zustände sind orthogonal. Der Gesamtzustand ist stationär, die bedingten Zustände besitzen eine genaue zyklische Schrödinger-Entwicklung. Das ist eine ausdrückliche Page-Wootters-Konstruktion auf der vorhandenen Zelle. Die Identitäten wurden symbolisch überprüft. Die allgemeine relationale Zeitidee ist etabliert; die hier angegebene Einbettung ist eine eigene Anwendung auf das untersuchte Singulett. [Moreva et al., Time from quantum entanglement](https://arxiv.org/abs/1310.4691)

Die Konstruktion fügt eine bevorzugte Basis, die äquidistanten Energien und ihre Koeffizienten hinzu. Dass \(h\) im linearen Raum der Quell-Paulis liegt, bedeutet nicht, dass der Compiler gerade diese Linearkombination als Hamiltonoperator auswählt. Eine Energieskala \(\varepsilon\) würde den Schritt zu \(\Delta t=\pi\hbar/(2\varepsilon)\) machen; \(\varepsilon\) ist nicht hergeleitet. Dies ersetzt auch nicht unbemerkt die ursprüngliche volle Tetramer-Dynamik. Es ist eine alternative ergänzte Zwangsdynamik, die denselben Zustand trägt. Der Fortschritt lautet: Die Uhr ist explizit konstruierbar; ihre Quellauswahl bleibt offen.

### 7.2 Statische Uhr, Uhrwerk und Zeitpfeil

Der reine paarweise Swap-Hamiltonoperator besitzt im relevanten
antisymmetrischen Systemsektor nur drei Energieniveaus für vier Lesarten und
wirkt dort zu stark entartet. Er trägt eine statische
Page–Wootters-Korrelation, wählt aber keine nichtentartete Vierer-Uhr. Die
oben konstruierte Uhr ergänzt genau die fehlende Aufspaltung; sie folgt nicht
aus dem Tetramer allein.

Zeit ist in diesem Rahmen zuerst die Reihenfolge komponierter Ereignisse.
Eine relationale Uhr liest diese Ordnung aus. Ein Zeitpfeil benötigt darüber
hinaus einen besonderen Zustand, Zugriffsbeschränkung, Reservoir oder
Grenzprozess. Diese drei Aussagen dürfen nicht unter dem Wort „Clock“
zusammenfallen.

### 7.3 Irreversibilität und Vielzellenphysik

Irreversibilität und Vielzellenphysik benötigen getrennte Grenzwertaussagen. Der Beweis gegen exaktes nichttriviales exponentielles Abklingen in einem geschlossenen endlichen Quantensystem mit festem unitärem Schritt ist korrekt. Eine Erwartungswertfolge ist eine endliche Summe von Phasen. Nach Zusammenfassung gleicher Frequenzen besitzt ihr mittleres Betragsquadrat einen positiven Cesàro-Grenzwert, sofern die Folge nicht identisch null ist. Eine echte \((3/7)^n\)-Dämpfung für alle \(n\) verlangt somit einen offenen Nachschub, einen unbeschränkten Grenzprozess oder eine andere Erweiterung dieser Voraussetzungen.

Die Rückkehr nach \(2m\) Schritten ist eine exakte Eigenschaft der hier untersuchten zyklischen Wiederverwendung von \(m\) Registern bei der festgelegten Vormessung im selben Kontext. Sie ist kein allgemeines Gesetz „Gedächtnis gleich Rekurrenzzeit“. Andere Kopplungen und Spektren können andere oder nur näherungsweise Rekurrenzen besitzen. Ebenso ist die Nichtumkehrbarkeit eines reduzierten Kanals noch keine Auswahl des kosmischen Anfangszustands oder eines thermodynamischen Zeitpfeils.

Die offene SU(4)-Kettenrechnung des Anschluss-Papers wurde reproduziert. Die angegebenen Lücken für zwei, drei und vier Vierersegmente erscheinen erneut. Zwei Einschränkungen sind für ihre Bewertung wesentlich: Erstens wechselt das Paper vom vollständigen Sechs-Kanten-Tetramer zu Vierersegmenten mit nächsten Nachbarn; damit ändert sich der Hamiltonoperator. Zweitens untersucht der Prüfer bei 16 Trägern eine ausgewählte Familie von Darstellungen, die aus den kleineren Ketten motiviert wurde. Der dort ausgegebene erste Anregungswert ist ohne zusätzlichen Ausschlusssatz nicht als global über alle Darstellungen zertifiziert.

Die SU(4)₁-WZW-Zuordnung des uniformen Kettenmodells ist fachlich plausibel und passt zu etablierter Spin-Ketten-Literatur. Die endlichen Spektren stützen diese Zuordnung. Sie beweisen aus den wenigen Größen allein weder eine thermodynamische Lücke für jedes \(\lambda<J\) noch eine neue TFPT-Kontinuumstheorie. Die größere Ringrechnung und eine neue vollständige Skalierungsanalyse wurden hier nicht wiederholt. [Führinger et al., DMRG studies of critical SU(N) spin chains](https://arxiv.org/abs/0806.2563)

## 8. Die \(E_8\)-Hülle und die chirale Naht

### 8.1 Exakte Rückrekonstruktion des Gitters

Die Rückrichtung zur E₈-Hülle kann exakt geschlossen werden, sobald die markierten Faktoren gegeben sind. Man kann den \(A_3\)-Faktor als \(D_3\) im euklidischen \(\mathbb R^3\) realisieren. Beginne mit

\[
L_0=D_5\oplus D_3\subset\mathbb R^5\oplus\mathbb R^3,
\qquad
g=(\tfrac12,\ldots,\tfrac12)\in\mathbb R^8,
\]

und setze

\[
L=L_0+\mathbb Zg.
\]

Die Klasse von \(g\) hat Ordnung 4 modulo \(L_0\). Das Skalarprodukt mit \(L_0\) ist ganzzahlig, und \(g^2=5/4+3/4=2\). Deshalb ist \(L\) gerade und ganzzahlig. Sein Index über \(L_0\) ist 4 und

\[
\det L=\frac{\det D_5\,\det A_3}{4^2}=\frac{4\cdot4}{16}=1.
\]

Das ist die positive gerade unimodulare Rang-8-Hülle E₈. Explizit besteht ihr ganzzahliger Teil aus den D₈-Vektoren und ihr halbzahliger Teil aus der zugehörigen Spinorklasse. Die Wurzeln lassen sich nachrechnen: 40 aus D₅, 12 aus D₃, 60 gemischte ganzzahlige und 128 halbzahlige Wurzeln, zusammen 240. Die Cartanrichtungen ergänzen auf 248.

Auch die konforme Zielstruktur ist konkret. Bei Niveau 1 lauten die zentralen Ladungen

\[
c(D_5)=\frac{45}{1+8}=5,\qquad
c(A_3)=\frac{15}{1+4}=3,\qquad
c(E_8)=\frac{248}{1+30}=8.
\]

Für die gekoppelten Spinorfelder ergänzen sich die Gewichte zu \(5/8+3/8=1\); für Vektor und antisymmetrischen Zweiträger zu \(1/2+1/2=1\). Die vier passenden \(\mathbb Z_4\)-Klassen organisieren die lokale Gittererweiterung. Auf Stufe 1 erscheinen genau

\[
(45,1)\oplus(1,15)\oplus(16,4)
\oplus(\overline{16},\overline4)\oplus(10,6).
\]

Dies ist eine echte gegenseitige algebraische Rekonstruktion der markierten Hülle und ihrer Faktoren. Ihre Ausgangsannahmen dürfen jedoch nicht verschwinden: D₅, A₃, Metrik, Markierungen und die passende lokale Verklebung sind gegeben. Weder \(c=8\) noch eine Vierträgerzelle allein wählt sie aus.

### 8.2 Konforme Einbettung statt Kondo-Fixpunkt

Die Beziehung

\[
(D_5)_1\otimes(A_3)_1\subset(E_8)_1,\qquad c=5+3=8,
\]

ist eine konforme Einbettung beziehungsweise
\(\mathbb Z_4\)-Simple-Current-Erweiterung. Sie benötigt keinen
RG-Fluss zu einem „\(c=8\)-Kondo-Fixpunkt“. Die gewöhnliche uniforme
SU(4)-Kette ist nichtchiral, \(c_L=c_R=3\). Der Übergang zu einer
holomorphen \(E_8\)-Naht verlangt daher eine eigene chirale Architektur.
Ein gapped 2+1-dimensionaler Bulk mit \((E_8)_1\)-Rand ist ein
strukturverträglicher Kandidat, aber sein lokaler Hamiltonoperator ist noch
nicht aus derselben primitiven Regel konstruiert.

Die 240 CQ-Koordinaten und die 240 \(E_8\)-Wurzeln sind nicht natürlich
identifiziert. Der Fugen-Audit schließt eine äquivariante Bijektion unter der
getesteten Symmetrie durch inkompatible Bahngrößen aus. Eine beliebige
Mengenbijektion bleibt mathematisch trivial und trägt keine Physik.

## 9. Operationelle Rekonstruktion

Eine universelle Rekonstruktion lässt sich als präziser mathematischer Auftrag formulieren. Man beginne nicht mit einem unbestimmt großen Raum, sondern mit einer vollständigen Liste zulässiger Präparationen, Operationen, Zusammensetzungen und Ausgaben. In einer quantenmechanischen Realisierung seien \(\mathfrak A\) die Observablenalgebra, \(\rho\) der Anfangszustand und \(\mathcal I_{a|x}\) die Operation zum Ergebnis \(a\) bei gewähltem Experiment \(x\). Dann definiert

\[
p(a_1,\ldots,a_n\mid x_1,\ldots,x_n)
=\operatorname{tr}\!\left[
\mathcal I_{a_n|x_n}\circ\cdots\circ
\mathcal I_{a_1|x_1}(\rho)\right]
\]

die Prozessstatistik. Verdeckte Register werden dabei in den gemeinsamen Zustand aufgenommen. Adaptive Entscheidungen können als Teil des Experiments mitgeführt werden.

Zwei Zustände oder Vorgeschichten werden identifiziert, wenn jede erlaubte Fortsetzung dieselben Ergebniswahrscheinlichkeiten liefert:

\[
h\sim h'
\quad\Longleftrightarrow\quad
p(f\mid h)=p(f\mid h')\quad\text{für jede erlaubte Zukunft }f.
\]

Die Fortsetzungen müssen unter weiterer Zusammensetzung geschlossen sein; für quantenmechanische Vollständigkeit werden gegebenenfalls auch erlaubte Hilfssysteme mitgeführt. Der Quotient ist die kanonische operationelle Beschreibung relativ zu diesem Experimentbestand. Er bewahrt genau die Information, die irgendeine zugelassene Zukunft noch unterscheiden kann. Er setzt nicht voraus, dass die physische Welt aus klassischen Vorgeschichten besteht.

Im endlichen linearen Fall ist diese Definition konstruktiv berechenbar. Man startet mit dem linearen Raum der Auslese-Effekte und erweitert ihn wiederholt durch alle adjungierten zulässigen Operationen:

\[
V_0=\operatorname{span}(\text{Auslese-Effekte}),
\qquad
V_{k+1}=V_k+
\operatorname{span}\{\mathcal I^*(E):E\in V_k\}.
\]

Sobald sich der Raum nicht mehr vergrößert, ist \(V_\infty\) der vollständige Raum der unterscheidenden linearen Zukunftstests. Zwei Zustände sind genau dann operationell gleich, wenn sie auf allen Effekten dieses Raums übereinstimmen. Der Annihilator enthält die unsichtbaren Zustandsunterschiede; die duale Quotientenbeschreibung ist autonom. Die oben berechneten 45 und 30 linearen Dimensionen sind konkrete eingeschränkte Instanzen dieses Verfahrens.

Für allgemeine Mehrzeitprozesse ist die entsprechende quantenmechanische Beschreibung eine konsistente Familie positiver Prozesstensoren beziehungsweise Quantenkämme. Die Positivität und kausalen Normierungsbedingungen sind wesentlich. Das Entfernen einer Zeitstelle erfolgt durch Einsetzen einer Identitätsoperation; das bloße Summieren über Messergebnisse kann eine störende Messung zurücklassen. Geeignete Konsistenzbedingungen erlauben eine Erweiterung auf einen umfassenderen Prozess. Sie wählen keine eindeutige unbeobachtbare Umweltmikroskopie. [Chiribella et al., Theoretical framework for quantum networks](https://arxiv.org/abs/0904.4483), [Milz et al., Kolmogorov extension theorem for causal modelling](https://arxiv.org/abs/1712.02589)

Damit erhält man eine gemeinsame Definition des Kandidaten:

\[
\mathcal U_{\mathrm{op}}=
\bigl(\text{komponierbare Operationen},\;
\text{positive konsistente Prozessstatistik}\bigr)/\!\sim.
\]

TFPT kann eine markierte Präsentation eines Teils dieser Struktur liefern. Eine freie Erweiterung seiner Generatoren und Relationen beschreibt zunächst eine Klasse von möglichen Realisierungen. Die positive Statistik und die physisch erlaubte Komposition wählen daraus erst einen bestimmten operationellen Prozess. In einer kategorischen Formulierung muss die Beobachtungsäquivalenz alle zulässigen Einbettungen in größere Experimente berücksichtigen, damit sie mit Zusammensetzung verträglich ist.

Die beiden Pfeile schließen sich dann in einer präzisen Form: Aus \(U_{\rm proc}\) gewonnene vollständige Operations- und Prozessdaten rekonstruieren \(U_{\rm proc}\) bis auf operationelle Äquivalenz. Aus unvollständigen Daten rekonstruieren sie die Klasse kompatibler Erweiterungen. Die Bedingung für eine eindeutige physische Auswahl ist ein zusätzlicher Satz über diese Klasse; sie ist nicht durch die Definition des Quotienten erledigt.

Allgemeine Quantenrekonstruktionen aus Informationsprinzipien zeigen, wie man Hilbertraumstruktur mit zusätzlichen operationellen Annahmen begründen kann. Sie benötigen konkrete Prinzipien, etwa Kausalität, Unterscheidbarkeit, Kompression, lokale Unterscheidbarkeit, reine Konditionierung und Purifikation im betreffenden Rahmen. „Veränderungen sind miteinander verbunden“ allein enthält diese Auswahl nicht und erzwingt weder komplexe Quantenmechanik noch E₈. [Chiribella, D’Ariano und Perinotti, Informational derivation of Quantum Theory](https://arxiv.org/abs/1011.6451)

### 9.1 Teilsysteme aus Beziehungen

Teilsysteme können innerhalb dieses Rahmens aus Beziehungen rekonstruiert werden. Im endlichen algebraischen Fall liefern hinreichend große, miteinander kommutierende Matrixfaktoren, die gemeinsam die Gesamtalgebra erzeugen, eine Tensorproduktzerlegung bis auf die üblichen unitären Äquivalenzen und Umbenennungen. Mit nichttrivialem Zentrum oder unvollständigem Zugriff bleibt eine direkte Sektorzerlegung beziehungsweise weitere Mehrdeutigkeit. Die klassische Referenz hierfür ist die beobachtungsinduzierte Tensorproduktstruktur. [Zanardi, Lidar und Lloyd](https://arxiv.org/abs/quant-ph/0308043)

Die Enumeration der 105 Qubit-Paarungen passt dazu: Innerhalb dieser endlichen Klasse erkennt die Zwei-Körper-Struktur der sechs Swaps eine einzige Paarung. Sie ist jedoch keine Enumeration aller Faktorisierungen des 256-dimensionalen Hilbertraums. Außerdem bleibt zu begründen, weshalb gerade die verwendeten Wechselwirkungen die privilegierten physikalischen Beziehungen sind. Ein einzelner Zustand reicht hierfür im Allgemeinen nicht.

## 10. Von Ausbreitung zu Raumzeit

### 10.1 Der Lorentzkegel als Teilrekonstruktion

Der Lorentzkegel ist eine genaue geometrische Teilrekonstruktion. Sobald ein markierter \(M_2(\mathbb C)\)-Block samt hermitescher Struktur und positivem Kegel gegeben ist, gilt

\[
H=\begin{pmatrix}t+z&x-iy\\x+iy&t-z\end{pmatrix},
\qquad
\det H=t^2-x^2-y^2-z^2,
\]

und \(H\succeq0\) entspricht \(t\ge\sqrt{x^2+y^2+z^2}\). Die Kongruenz \(H\mapsto AHA^\dagger\), \(A\in SL(2,\mathbb C)\), erhält diese Form. Diese etablierte Spinor-Lorentz-Struktur ist in den Unterlagen konkret anschließbar. Sie rekonstruiert eine Kinematik des ausgewählten Blocks. Für Raumzeit fehlen die Zuordnung solcher Blöcke zu Ereignissen oder Regionen, eine kausale Lokalitätsstruktur, geometrische Skalen, ein geeigneter Grenzwert und eine gemeinsame Dynamik. Insbesondere ist die Dimension eines internen Viererträgers kein Beweis für vierdimensionale Raumzeit.

Für eine umfassende Theorie müsste die Prozessstruktur deshalb zusätzliche, quellenseitig bestimmte Daten liefern: lokale Observablen, verträgliche Überlappungen, Ausbreitungsregeln und die Auswahl eines physikalischen Zustands. Erst daraus wäre zu prüfen, ob eine vierdimensionale Lorentzgeometrie mit universeller Materiekopplung entsteht. Der vorhandene Lichtkegel macht dieses Ziel mathematisch konkret; er löst es nicht allein.

### 10.2 Warum Grad fünf keine drei Raumrichtungen auswählt

Die lokale Clebsch-Regel ist fünfregulär. Sie legt keine globale räumliche
Dimension fest. Explizite Überlagerungen desselben lokalen Bausteins mit
\(\mathbb Z^d\) existieren für verschiedene \(d\); Grad, Zyklusrang und
interne Trägerdimension sind daher keine Dimensionsbeweise.

Ein schärferer bedingter Mechanismus beginnt mit dem **tatsächlichen**
inversen Propagator eines aus \(U_{\rm step}\) gewonnenen kohärenten
Zweikomponentensektors:

\[
G^{-1}(\omega,\mathbf q)
=Z^{-1}\!\left[
(\omega-\mathbf w\!\cdot\!\mathbf q)I
-\sum_{a,j=1}^3V_{aj}q_j\sigma_a
\right]+O(q^2).
\]

Dann gilt

\[
\det G^{-1}\propto
(\omega-\mathbf w\!\cdot\!\mathbf q)^2
-\mathbf q^TV^TV\mathbf q.
\]

Eine generische isolierte Zweibandberührung hat Kodimension drei. **Bedingt:**
Wenn ein thermodynamischer Impulsraum, ein isolierter stabiler Weyl-Pol und
Transversalität aus derselben Mikrodynamik folgen, wird \(d=3\) ausgewählt.
Der Impulsraum und der Pol dürfen dabei nicht als Eingabe eingeführt werden.
Für mehrere Materiesektoren muss zusätzlich
\(v_i(\ell)\to c\) an einem gemeinsamen infrarotstabilen Lorentz-Fixpunkt
gezeigt werden.

Zeit ist in diesem Kandidaten keine vierte Graphachse. Sie ist die
Kompositionsrichtung der reversiblen Ereignisse; erst im Grenzwert wird sie
zur kontinuierlichen Frequenzvariable \(\omega\).

Die weiteren Anschlussbefunde fügen sich in dieselbe Logik. Eine Hamiltonoperator-Rekonstruktion \(H\to\psi\to H\) innerhalb einer festgelegten Operatorliste prüft Identifizierbarkeit; sie ist keine unabhängige Vorhersage des ursprünglichen \(H\). Kleine Varianzen für HH-Hop und \(E^4\) zeigen dort fehlende Empfindlichkeit des untersuchten niedrigen Energiesektors. Die Zweischleifen-Protonzerfallsrechnung ist im Paper ein bedingtes negatives Resultat des gaugeten SO(10)-Zweigs; sie wurde hier nicht erneut gerechnet und darf die Universalraum-Rekonstruktion nicht als schon gelöst voraussetzen. Die Unterscheidung innerer Glue-\(\mathbb Z_4\) und geometrischer Rotation ist wichtig: Ihre verschiedenen Spuren schließen die behauptete Operatorgleichheit aus. Eine Indexgleichheit beim Hecke-/Jones-Anschluss beschreibt eine Inklusion; sie bestimmt für sich allein keinen physikalischen Zeitgenerator.

## 11. Materie, Familien, Eichfelder und Gravitation

Materie ist im konsolidierten Kandidaten nicht jeder \(E_8\)-Generator,
sondern ein stabiler propagierender Pol mit innerer Darstellung und
topologischer Ladung. Die Formel \((16-1)/5=3\) ist kein Familienindex. Der
erforderliche Satz lautet stattdessen

\[
N_{\rm fam}=\operatorname{index}D_{\rm eff}
=\dim\ker D_L-\dim\ker D_R=3.
\]

Eine topologische Ladung drei ist ein plausibler Mechanismus, aber sie ist
noch nicht aus der primitiven Dynamik berechnet. Ebenso sind der
\(A_3\)-Trägerfaktor und der innerhalb von \(D_5\) liegende
Pati–Salam-Faktor \(SU(4)_c\) verschiedene Symmetrien; sie dürfen nicht ohne
neue Brechungsregel identifiziert werden.

Lokale Änderungen innerer Vergleichsrahmen können bedingt
Eichverbindungen erzeugen,

\[
A_{xy}\mapsto V_xA_{xy}V_y^\dagger.
\]

Langsame Änderungen des gemeinsamen Ausbreitungsrahmens können ein Vierbein
\(e^a{}_\mu(x)\) und damit

\[
g_{\mu\nu}=\eta_{ab}e^a{}_\mu e^b{}_\nu
\]

definieren. Das Hinschreiben dieser Variablen erzeugt noch keine Gravitation.
Zu zeigen sind ein positiver masseloser Spin-2-Pol, genau zwei physische
Helizitäten, die zugehörigen Ward-Identitäten und ein kontrollierter
langwelliger Einstein-Term. Erst **nach** Existenz dieses Pols und unter der
Voraussetzung, dass alle Materiepole denselben Rahmen benutzen, kann
universelle Kopplung folgen.

Auch die Kopplungskonstanten müssen aus demselben Vakuum entstehen, etwa als
Steifigkeiten

\[
\frac1{g_i^2}\sim
\frac{\partial^2\Gamma}{\partial A_i^2}.
\]

Der reproduzierte historische Formelwert
\(\alpha^{-1}=137{,}0359992168407\ldots\) liegt etwa \(1{,}897\)
experimentelle CODATA-2022-Standardabweichungen vom Referenzwert entfernt.
Ohne Transfer zur Thomson-Kopplung und Theorieunsicherheit ist dies kein
fundamentaler Herkunftssatz. Die dokumentierten Spannungen bei
Leptonverhältnissen, älterem Higgszweig, einfacher Inflationsamplitude und
bedingtem Protonzerfallszweig bleiben im Befund; sie dürfen nicht durch
nachträglich freie Transfers verschwinden.

## 12. Der umfassende Lösungskandidat: eine feste Regel \(U_{\rm step}\)

### 12.1 Minimaler Quellenvertrag

Der stärkste gemeinsame Kandidat lautet nicht „\(E_8\) ist das Universum“ und
auch nicht „\(Q=[\,\cdot,\cdot\,]_{E_8}\) ist bereits die gesamte Physik“.
Er lautet:

> Fundamentale Struktur ist eine lokale, reversible, phasentreue
> Kompositionsdynamik. Die \(\mathbb Z_4\)-graduierte \(E_8\)-Struktur
> bestimmt ihre erlaubten Vertizes und relativen Phasen; Belegung,
> Vermittler, History, Zustand und globale Zusammensetzung vervollständigen
> den Prozess.

Auf einem explizit festzulegenden Hilbertraum

\[
\mathcal H=
\mathcal H_{\rm matter}\otimes
\mathcal H_{\rm mediator}\otimes
\mathcal H_{\rm history}
\]

soll ein selbstadjungierter lokaler Generator \(H_{\rm mic}\) mit
kontrollierter Domäne und den \(E_8\)-typisierten Vertexamplituden definiert
werden. Dann ist

\[
\boxed{U_{\rm step}(\tau)=e^{-i\tau H_{\rm mic}}}
\]

unitär und reversibel. History- und Lochzustände speichern, welche
Vertizes ausgeführt wurden. \(E_8\) bestimmt dabei die Grammatik, nicht ohne
Weiteres die Beträge \(t\), Vermittlerenergien, den globalen Graphen,
\(\tau\) oder den Anfangszustand.

### 12.2 Der No-Switch-Vertrag

Eine umfassende Lösung muss **dieselbe** feste Instanz

\[
\mathfrak U=
(\mathcal H,H_{\rm mic},\rho_0,\mathcal O_{\rm erlaubt},
\mathcal I_{\rm erlaubt},\mathcal P)
\]

in allen Rechnungen verwenden. Danach dürfen Tetramer, Clebsch-Graph, Kette,
Clock, Register und Kontinuum nicht unabhängig passend gewählt werden. Sie
müssen als Sektoren, effektive Grenzen oder Instrumente derselben
\(\mathfrak U\) abgeleitet werden.

Der aktuelle Korpus liefert dafür notwendige Bausteine, aber keinen
Eindeutigkeitssatz. Insbesondere sind die drei im Q-Audit hervorgehobenen
Rechnungen — vollständiges \(U_{\rm step}\), thermodynamischer
Propagatorgrenzwert und topologischer Vakuumsektor — notwendig, nach heutigem
Stand jedoch nicht gemeinsam hinreichend: Kopplungswerte, physikalischer
Zustand und gemeinsame Auslesung bleiben zusätzliche Beweislasten.

### 12.3 Zusammenhängender Herkunftstest

Der nächste entscheidende Herkunftstest betrifft die Operation, die die Zelle tatsächlich herstellen kann. Es ist sinnvoll, den folgenden zusammenhängenden Nachweis anzustreben:

1. Die primitive TFPT-Operationsklasse und ihre zulässige Verbindung zwischen Trägern werden vollständig festgelegt. Dabei wird jede Ressource außerhalb des Stabilizer-Baukastens benannt.
2. Aus dieser Quelle wird ein Übergang zu einem bestimmten Zwischenzustandssektor mit Energieabstand und Kopplung konstruiert. Die beiden E₈-Klammerkanäle werden dabei korrekt getrennt.
3. Derselbe Mechanismus erzeugt die effektive Paarwechselwirkung und ein physisch ausführbares Präparationsverfahren für \(\Omega\), einschließlich Umwelt- oder Messressourcen.
4. Daraus wird eine vorher festgelegte Mehrzeitstatistik berechnet, die alternative Lifts oder Registerprotokolle unterscheidet.
5. Mindestens eine Auslesung wird vorher eingefroren und anschließend aus diesem Ursprung berechnet, ohne die Zusatzparameter am Zielwert nachzustellen.

Ein Scheitern von Schritt 1 oder 2 ist informativ: Dann enthält die bisherige Quelle die erforderliche Ausführung noch nicht. Ein Gelingen wäre stärker als weitere Symmetrie- oder Spektralübereinstimmungen, weil es die bislang fehlende Ursache mit dem beobachtbaren Effekt verbindet. Die konkrete Uhrkonstruktion kann anschließend prüfen, ob diese neue Dynamik die erforderlichen relativen Energien auswählt oder eine andere, ebenfalls messbare Zeitstruktur erzeugt.

## 13. T1–T8: Herkunftssätze, Erfolgstests und Kill-Kriterien

| Tor | Gesicherter Teilstand | Noch erforderlicher Herkunftssatz | Vorab bestimmter Erfolgstest | Kill-Kriterium des Kandidaten |
|---|---|---|---|---|
| T1 Primitive Quelle | Endliche Algebra, Klammer, Belegungs- und Registermodelle | Eine vollständig definierte und minimale \(\mathfrak U\) wählt Träger, Vertizes, Beträge, Zustand und Instrumente | Unitarität, Lokalität, Symmetrien und alle endlichen Replays folgen ohne Modellwechsel | Zwei nicht äquivalente Regeln erfüllen denselben Quellenvertrag, sagen aber für eine eingefrorene Auslesung Verschiedenes voraus |
| T2 Chirale Naht | \(E_8\)-Gitter, Cocycle und konforme Erweiterung sind abstrakt konstruierbar | Derselbe \(H_{\rm mic}\) besitzt einen kontrollierten Bulk/Rand-Grenzwert mit chiraler \((E_8)_1\)-Naht | Konvergente Korrelatoren, Level 1, korrekte Gewichte, Cocycles und \(c_L-c_R=8\) | Unvermeidliche Gegenchiralität, falsches Level oder kein phasentreuer Adapter |
| T3 3+1D und gemeinsamer Kegel | Lorentzdeterminante und Weyl-Kodimension sind bedingte Mechanismen; Dimensionsgegenmodelle existieren | Der thermodynamische Grenzwert derselben Regel erzeugt genau drei räumliche Richtungen und einen gemeinsamen IR-Kegel | Isolierte stabile Pole, kontrollierte Dispersion, \(v_i(\ell)\to c\) für alle Materiesektoren | Kein kohärenter Pol, mehrere dauerhafte Kegel oder gleichberechtigte Dimensionsfortsetzungen |
| T4 Chirales Standardmodell | Darstellungen und endliche Anomaliesummen sind vorhanden | Ein aus \(\mathfrak U\) abgeleiteter Diracoperator hat Index 3, richtige Ladungen und gegappte Spiegel | \(\operatorname{index}D=3\), Anomaliefreiheit und Spiegelentkopplung im selben Maß | Index 0/falsch, ungepaarte Anomalie oder nicht entkoppelbare Spiegel |
| T5 Wechselwirkung und Kontinuum | Paarterm, Modell-Vierkörperterm und Zweizellenlücke sind kontrolliert | Ein lokaler Vielkörper- und Kontinuumsgrenzwert derselben Regel existiert mit kontrollierten Fehlern | Einheitliche endliche Größenfolge, Clusterstruktur, Unitarität und stabile Fehlergrenzen | Störreihe unkontrolliert, nötiger Sektor verschwindet oder widersprüchliche Graphwechsel |
| T6 Kopplungen und Massen | Historische Formelwerte und Spannungen sind reproduziert | Eichkopplungen, Yukawas, Neutrinos und Skala sind Vakuumantworten derselben \(\mathfrak U\) | Vor Daten eingefrorene Werte mit Theorieunsicherheit und eindeutigem Transfer | Nachträgliche Parameter/Skalen oder Scheitern außerhalb der vorab festgelegten Unsicherheit |
| T7 Gravitation | Kegel und gemeinsamer Frame sind Zielstruktur | Die kollektive Frame-Fluktuation besitzt einen positiven masselosen Spin-2-Pol mit zwei Helizitäten und universeller Kopplung | Pol, Ward-Identitäten, Einstein-Term und gleicher Materievertex im kontrollierten IR | Massiver/ghostartiger Pol, zusätzliche Helizitäten oder nichtuniverselle Kopplung |
| T8 Zustand und Prozess | Prozessquotient, Registerzeugen, Präparations- und Echo-Protokolle sind exakt in ihren Modellen | \(\rho_0\), zugängliche History und positives Quellfunktional werden von derselben Quelle ausgewählt | Alle eingefrorenen Mehrzeitwahrscheinlichkeiten folgen ohne Wahl „frisch/behalten“ nach Sichtung des Ziels | Weiterhin kompatible Register- oder Zustandsausführungen mit verschiedenen Zukunftsstatistiken |

Diese acht Herkunftssätze sind gemeinsam der Schließungsvertrag. Das Erfüllen
einzelner Zeilen darf nicht als prozentuale oder logische Schließung der
übrigen Zeilen ausgegeben werden.

## 14. Konsolidiertes Urteil und Reproduktion

Die wissenschaftlich stärkste Fassung lautet:

> Ein gemeinsamer komponierbarer Prozess trägt die beobachtbare Struktur;
> TFPT gibt dafür eine markierte algebraische Präsentation. Vollständige
> Prozessdaten erlauben eine Rückrekonstruktion bis auf operationelle
> Äquivalenz. Die Auswahl gerade des physikalischen Prozesses verlangt die
> acht überprüfbaren Herkunftssätze oben.

Vor dieser Konsolidierung wurden die im Repository verfügbaren direkten
Contracts erneut ohne Repo-Ausgaben ausgeführt:

- Inversion: 325/325 und 147/147 Checks; 19/19 Tests normal und unter
  `-OO`; beide Ergebnisdateien bytegleich;
- Fugen: 27.288/27.288 Bedingungen; 14/14 Tests normal und unter `-OO`;
  Ergebnisdatei bytegleich;
- sechs Anschlussprüfer des 7-seitigen Papers: jeweils
  `ALL CHECKS PASSED`, alle Ergebnisdateien bytegleich.

Die vorhandene Clebsch-Datei dokumentiert einen vollständigen numerischen
Lauf über 64 Irreps und Ringgrößen \(n=5,\ldots,13\); der etwa
1.021-sekündige Lauf wurde für diese Redaktion nicht wiederholt. Die
Präparations-, Rekonstruktions- und Q-Audit-Pakete sind in den vorliegenden
Texten beziehungsweise Lieferarchiven beschrieben, aber nicht als
eigenständige ausführbare Ordner im aktuellen Repository vorhanden. Ihre
Resultate werden deshalb zugeschrieben und nicht als in dieser Runde erneut
ausgeführt bezeichnet.

RH-, Faktorisierungs- und P-vs-NP-Passagen der frühen Gesamtsynthese gehören
nur zur historischen Katalogeinordnung. Sie sind kein Bestandteil des
Universalraum-Schließungsvertrags.

Die wesentlichen Belege sind nicht die Checkzahlen, sondern die expliziten
Formeln, Gegenmodelle, Gültigkeitsbereiche und Kill-Kriterien. Bis
\(U_{\rm step}\), sein Grenzwert, sein topologischer Sektor, seine
Kopplungsantworten und sein Zustand aus **einer** unveränderten Quelle
vorliegen, bleibt der Universalraum ein präziser, falsifizierbarer
Gesamtkandidat und keine bewiesene allesumfassende Physik.
