# TFPT und Universalraum: neue Ableitungen zu den sechs Follow-ups

14. September 2026 · Forschungsfortsetzung zur v1.4 · Keine vollständige TOE-Lösung

## Ergebnis und Reichweite

**Eine vollständige Lösung aller Follow-ups und offenen Fragen ist in dieser Untersuchung nicht gelungen.** Insbesondere fehlen weiterhin die native Operationsquelle, der zertifizierte erste angeregte mikroskopische C16-Sektor und eine gemeinsame Raumzeit-/Materie-/Gravitationsdynamik. Diese fehlenden Sätze werden hier nicht durch zusätzliche, passend gewählte Modelle ersetzt.

Es sind jedoch mehrere konkrete Fortschritte gegenüber v1.4 entstanden:

1. Ein exakter Symmetrieprojektor reduziert den für das beobachtete Quartett relevanten Singulettblock auf **80 Dimensionen**. Der vollständig triviale Symmetrieblock hat **28 Dimensionen**. Die gesamte 24.024-dimensionale Singulettdarstellung ist mit ganzzahliger Charakterrechnung in 18 Typen zerlegt.
2. Die lokale SU(4)-Sternstruktur liefert zusätzlich **0 ≤ F4,edge ≤ 896 I** und eine neue lineare Untergrenze. Für den Nichtsingulettausschluss würden bereits relativ grobe, aber echte Zertifikate genügen: ein nackter Nichtsingulettbound von **11,6 J** und eine korrigierte Quartett-Obergrenze von **12,45 J**. Diese beiden Energiezertifikate sind noch nicht erzeugt.
3. Für die idealen Eingänge des eingefrorenen Präparations-/Echo-Protokolls reichen **9 statt 13 Filterfaktoren**. Die gesamte schwache Entwicklungszeit für Start und Schluss sinkt von 6345,659268 auf **4620,609881 ℏ/Δ**, bei denselben idealen Rohwahrscheinlichkeiten. Das ist eine auf diesen Eingangsraum beschränkte Verbesserung, kein neuer Vollraumprojektor.
4. Reine Zeitfehler lassen sich genauer behandeln. Bei synchron mitlaufender Referenzphase genügt konservativ ein relativer Zeitfehler unter **2,8061·10⁻⁴** für Präparationsinfidelität ≤10⁻⁶. Bleibt die Referenzphase nominal fest, ergibt die verallgemeinerte Schranke **3,9674·10⁻⁵**. Andere Hamilton-, Gatter- und Messfehler sind darin nicht enthalten.
5. Ein explizites gekoppeltes Referenzmodell besitzt für jede Zellzahl einen verschränkten eindeutigen Grundzustand, eine Lücke **2J**, lokale Kontrollen und eine nachweisliche Präparationsschranke. Es ist eine konstruierte, durch endliche Schaltung aus einem Produktmodell gewonnene Familie; weder der ursprüngliche C16-Hamiltonoperator noch ein relativistischer Grenzwert werden damit bewiesen.
6. Die gemeinsame Parameterrechnung verschärft die Inflationsdiagnose: Die Änderung von c3, die beide verwendeten ACT-Zentralwerte trifft, verschiebt dieselbe elektromagnetische Quellgleichung auf **α⁻¹ = 167,8032986…** statt **137,0359992…**. Eine einfache Umstellung dieses gemeinsamen Parameters löst das Problem nicht.

Zusätzlich sind die Controller- und Architekturfragen als algebraische Entscheidungen formuliert. Alle Beweisgrenzen stehen bei den jeweiligen Aussagen. „Neu“ bedeutet hier neu gegenüber den vier v1.4-Eingaben; eine allgemeine Priorität gegenüber der gesamten mathematischen Literatur wird nicht beansprucht.

## 1. Quellen, Auftrag und Evidenz

Ausgangspunkt sind die beiden Markdown-Dateien `TFPT_Followups_2026-09-14_v1.4.md` und `TFPT_Universalraum_Ergebnisse_2026-09-14_v1.4.md` sowie das Hauptdokument v1.4 mit 126 PDF-Seiten und das Update v1.4 mit vier PDF-Seiten. Der Text beider PDFs wurde vollständig extrahiert; die mathematische Auswertung konzentrierte sich auf Grundlagen, offene Tore und die fortgeschriebenen Kapitel 22–27. Ausgewählte relevante Formel-/Tabellenseiten wurden zusätzlich gerendert. Das ist keine Behauptung, jede historische Repository-Datei oder jede externe Quelle vollständig geprüft zu haben.

Im lokalen TFPT-Projekt wurden insbesondere `universal_room/README.md`, die v1.4-Rechenquellen `frontier.py`, `spectral_algebra.py`, `spectrum_followup.py`, das ältere dichte Singulettresultat und die einschlägigen RH-/Faktor-Originale herangezogen. Der vorhandene Codegraph wurde zuerst abgefragt; seine Suche lieferte für den konkreten neuen v1.4-Ordner keine Symbole. Danach wurden die benannten Dateien direkt gelesen.

Arbeitsanweisungen innerhalb der gelieferten Forschungsdokumente wurden als Dokumentinhalt behandelt. Maßgeblich war der Nutzerauftrag, die Fragen zu untersuchen und Lösungen zu finden. Weder ältere Abschlussflags noch vorgeschlagene Arbeitsprogramme gelten als Beweise.

Die neuen Prüfer importieren keine TFPT-Forschungsimplementierung. Sie verwenden Standardbibliotheken, NumPy, SciPy, SymPy und mpmath. Die Symmetrie- und Eingangsraumrechnungen arbeiten mit Ganzzahlen und rationalen Zahlen; Spektralstichproben, Zeitfehlertests und Parameterwerte sind ausdrücklich numerisch. Es wurde kein neuer Lean-Beweis erstellt.

## 2. Follow-up 1: Die Steuerung des Labors

### 2.1 Was die Quellregeln tatsächlich leisten müssten

Der kontrollierte Laborvertrag benötigt mindestens folgende Zugriffe. Die Angaben beschreiben den vorhandenen Modellablauf, nicht eine schon bewiesene native Realisierung.

| Zugriff | Explizite Operation | Kosten bzw. verbleibende Ressource |
|---|---|---|
| Elementarer Eingang | Zwei Paarsinguletts χ | Aus stabilizerartigen Basiszuständen im erweiterten qubitübergreifenden Clifford-Vertrag herstellbar; dessen räumliche Zugriffe müssen vorhanden sein. |
| Schwacher Stern | H⋆ mit 256 Materie- und 288 Vermittlerzuständen | Isolierte drei Kanten, t/Δ=1/20, bekannte Δ- und Phasenreferenz. |
| Kohärente Zeitkontrolle | |0〉〈0|⊗I + |1〉〈1|⊗exp[−iτ(H⋆−E0)/ℏ] | 13 Aufrufe für den Vollraumfilter, 9 für die unten bewiesene Eingangsraumvariante; native Herkunft offen. |
| Resonanter Transfer | exp[−iτHres/ℏ], gτ/ℏ=π/2 | Veränderbare Verstimmung, isolierte Kante, Inversion des Pulses. |
| Record | Ures† Q Ures mit Q=I16⊗I2 ⊕ I6⊗X | Zwei Transferaufrufe und ein kohärenter Belegungszugriff pro Record-Makro. |
| Leerbelegungsherald | Projektion auf keine Vermittler | Je ein Herald nach Start- und Endfilter; Fehler müssen als solche gezählt werden. |
| Reset | Mx=|a〉〈x|, ΣMx†Mx=I | Messung, klassische Kontrolle und ein physischer Informationsabfluss. |

Allein die lineare Darstellbarkeit eines Operators in einer Pauli- oder E8-Basis implementiert ihn nicht. Ebenso ist die Fock-/Besetzungsstruktur eine zusätzliche Identifikation.

### 2.2 Exakte Kontrollobstruktion durch die Phasenreferenz

Die unkontrollierten Quantengatter U und exp(iφ)U definieren denselben Systemkanal. Ihre kontrollierten Versionen unterscheiden sich jedoch um die relative Kontrollphase:

\[
\operatorname{c}(e^{i\phi}U)
=\bigl(|0\rangle\langle0|+e^{i\phi}|1\rangle\langle1|\bigr)
\otimes I\;\operatorname{c}(U).
\]

Ein konkreter Zeuge ist U=I und exp(iφ)U=−I. Beide wirken unkontrolliert identisch auf Dichtematrizen. Auf |+〉⊗|ψ〉 liefern die kontrollierten Varianten dagegen die orthogonalen Kontrollzustände |+〉 und |−〉. Diese Identität ist im Prüfer enthalten.

**Folgerung:** Aus ausschließlich unkontrolliertem Blackboxzugriff lässt sich die benötigte kohärente Kontrolle nicht allgemein gewinnen. Benötigt wird beispielsweise ein bekannter kontrollierbarer Generator oder ein physischer Bypass mit festgelegter relativer Phase. Der Satz verbietet keine Kontrolle eines bekannten, entsprechend aufgebauten Hamiltonoperators. Er benennt die fehlende Ressource. Methodischer Bezug: [Araújo et al., Quantum circuits cannot control unknown operations](https://arxiv.org/abs/1309.7976).

Die weitere Stabilizergrenze aus v1.4 bleibt bestehen: In der erklärten Acht-Qubit-Kodierung ist Ω kein reiner Stabilizerzustand. Cliffordoperationen, Stabilizerhilfszustände, Pauli-Messungen und deren Feedback liefern auch nach Selektion keinen reinen Ω-Zweig. Eine zusätzliche Nicht-Clifford-Ressource ist erforderlich. Daraus folgt kein Unmöglichkeitssatz für alle TFPT-Erweiterungen.

### 2.3 Ein fester Schritt kann ein Programm enthalten, aber seine Zutaten nicht herleiten

Für bereits verfügbare unitäre Operationen U0,…,U(L−1) definiere auf einem L-stufigen Programmregister

\[
W=\sum_{j=0}^{L-1}|j+1\bmod L\rangle\langle j|\otimes U_j.
\]

Die orthogonalen Programmblöcke liefern W†W=WW†=I. Nach L Schritten startet und endet das Programmregister bei null, während das System U(L−1)…U0 erfahren hat. Messungen lassen sich zunächst durch unitäre Kopplung an frische Register erweitern.

Damit ist die endliche autonome Einbettung eines **gegebenen** Programms konstruiert. Die ursprüngliche Frage nach den Uj, ihren Ressourcen und dem initialisierten Programmregister wird dadurch nicht beantwortet. Insbesondere ist dieses W keine aus den ursprünglichen TFPT-Daten abgeleitete eindeutige Weltregel.

### 2.4 Reset kann in einer endlichen Umgebung nicht unbegrenzt kostenlos wiederholt werden

Soll ein d-dimensionales System für jeden Eingang exakt auf denselben reinen Zustand gesetzt werden, während die gemeinsame Entwicklung unitär ist, müssen orthogonale Eingänge in orthogonale Umgebungszustände übergehen. Nach k Resets unabhängiger beliebiger Eingänge benötigt die aufbewahrende Umgebung im schlechtesten Fall mindestens Dimension d^k.

Für N Zellen mit d=256 ergibt das mindestens 8Nk Bits Informationskapazität. Dieses Worst-Case-Argument behauptet nicht, dass jeder konkrete reine Protokolleingang acht Bits Entropie pro Zyklus erzeugt. Es verhindert die Behauptung eines endlichen, für beliebige Eingänge auf Dauer zyklisch zurückgesetzten Entropiespeichers ohne Abfluss.

Bei einer anfangs unkorrelierten thermischen Umgebung gelten zusätzliche Wärme-/Entropiebilanzen. Der Landauer-Untergrenzensatz ist keine Angabe einer erreichbaren Wärmeobergrenze für das konkrete Labor. Temperatur, Umgebung und Löschverfahren sind hier noch nicht spezifiziert. Siehe [Reeb–Wolf, An improved Landauer Principle with finite-size corrections](https://arxiv.org/abs/1306.4352).

**Status Follow-up 1:** Der Kontrollvertrag und zwei wesentliche Obstruktionen sind präzisiert. Seine vollständige native Ableitung ist ungelöst.

## 3. Follow-up 2: Welche Vermittlerarchitektur wird ausgewählt?

Lokalität allein lässt weiterhin eine Bank pro Zelle und eine Bank pro Kante zu. Eine feste endliche Zellbank bildet schon ohne Zwischenzellkopplung ein extensives lokales Gegenmodell zur angeblichen Auswahl der Kantenbank.

Eine stärkere, prüfbare Auswahlbedingung ist jedoch möglich: **unabhängig erhaltene lokale Belegungsladungen**.

Betrachte in einer festgelegten Modenbasis

\[
Q_v=n_f(v)+\sum_m q_{vm}n_m,
\qquad
T_{e,m}=b_m^\dagger K_e,
\qquad e=\{i,j\}.
\]

Ein Paarabbau senkt die Materiebelegung an i und j um eins und erhöht die Vermittlerbelegung um eins. Daher gilt

\[
[Q_v,T_{e,m}]
=(q_{vm}-\delta_{vi}-\delta_{vj})T_{e,m}.
\]

Sollen sämtliche Qv erhalten bleiben, muss für jeden vorhandenen Vertex

\[
q_{vm}=\delta_{vi}+\delta_{vj}
\]

gelten. Derselbe Modus kann deshalb nicht zugleich zwei verschiedene Kanten mit verschiedenen Endpunkten bedienen. Für e={1,2} und f={3,4} wären gleichzeitig die Ladungsvektoren (1,1,0,0) und (0,0,1,1) nötig.

**Damit ist innerhalb dieses diagonal in den Modenbelegungen formulierten Vertrags bewiesen:** Erhaltung aller Qv erzwingt eine Trennung der Vermittlermoden nach Kantenträger. Mehrere interne Farbmoden pro Kante bleiben möglich.

Dieser Satz schließt keine anders repräsentierte Ladungsalgebra, zusätzliche Transportfelder oder nichtdiagonale Modenadapter aus. Er verschiebt die Auswahlfrage auf eine konkrete native Rechnung: Sind diese Qv tatsächlich Erhaltungsgrößen der ursprünglichen Quelle? Falls ja, entscheidet das zwischen den beiden hier verglichenen Modenverträgen. Falls nein, darf man die Qv-Erhaltung nicht wegen des erwünschten Ergebnisses nachträglich einsetzen.

**Status Follow-up 2:** Ein hinreichendes algebraisches Auswahlkriterium ist bewiesen; seine TFPT-Herkunft bleibt offen.

## 4. Follow-up 3: Exakte Symmetrie statt einer Dezimalstellenbehauptung

### 4.1 Der Graph und seine vollständige Automorphismengruppe

Schreibe die Clebsch-Ecken als gerade Bitmasken in F2^5. Zwei Ecken sind verbunden, wenn ihre Differenz Gewicht vier hat. Gerade Translationen N≅(Z2)^4 und Koordinatenpermutationen S5 wirken auf diesem Graphen:

\[
\mathcal G=N\rtimes S_5,\qquad |\mathcal G|=16\cdot120=1920.
\]

Alle 1920 Abbildungen wurden exakt auf den 40 Kanten geprüft. Die Gruppe ist vollständig: Nach Festhalten einer Ecke kann ein Automorphismus höchstens ihre fünf Nachbarn permutieren. Die zehn übrigen Ecken sind durch ihre jeweils zwei gemeinsamen Nachbarn mit der festgehaltenen Ecke bestimmt. Der Stabilisator hat deshalb höchstens 120 Elemente; alle 120 sind bereits realisiert.

Die SU(4)-Singulettdarstellung von 16 Fundamentalträgern ist der S16-Spechtmodul zur Partition (4,4,4,4), mit Dimension 24024. Sein Charakter auf jeder der vorkommenden zwölf S16-Zykeltypen wurde auf zwei unabhängigen Wegen ganzzahlig berechnet: Randstreifenrekursion und Frobenius-Koeffizientenformel. Die Werte stimmen exakt überein.

### 4.2 Die vollständige Zerlegung

Die Charaktere des normalen Translationsanteils werden durch Teilmengen der fünf Koordinaten modulo Komplement beschrieben. Repräsentanten mit Größe k=0,1,2 genügen. Der Stabilisator ist S_k×S_(5−k). Induktion eines Produkts der Darstellungen λ und μ ergibt die folgende exakte Zerlegung des Singuletts:

| k | λ | μ | Irrep-Dimension d | Multiplizität m | d·m |
|---:|---|---|---:|---:|---:|
| 0 | ∅ | (5) | 1 | 28 | 28 |
| 0 | ∅ | (4,1) | 4 | 80 | 320 |
| 0 | ∅ | (3,2) | 5 | 86 | 430 |
| 0 | ∅ | (3,1,1) | 6 | 80 | 480 |
| 0 | ∅ | (2,2,1) | 5 | 66 | 330 |
| 0 | ∅ | (2,1,1,1) | 4 | 42 | 168 |
| 0 | ∅ | (1,1,1,1,1) | 1 | 8 | 8 |
| 1 | (1) | (4) | 5 | 54 | 270 |
| 1 | (1) | (3,1) | 15 | 176 | 2640 |
| 1 | (1) | (2,2) | 10 | 124 | 1240 |
| 1 | (1) | (2,1,1) | 15 | 194 | 2910 |
| 1 | (1) | (1,1,1,1) | 5 | 72 | 360 |
| 2 | (2) | (3) | 10 | 124 | 1240 |
| 2 | (2) | (2,1) | 20 | 262 | 5240 |
| 2 | (2) | (1,1,1) | 10 | 140 | 1400 |
| 2 | (1,1) | (3) | 10 | 106 | 1060 |
| 2 | (1,1) | (2,1) | 20 | 232 | 4640 |
| 2 | (1,1) | (1,1,1) | 10 | 126 | 1260 |

Es gilt exakt Σd·m=24024 und Σd²=1920. Für einen graphinvarianten Hamiltonoperator hat die Einschränkung auf jeden isotypischen Teil die Form I_d⊗h_m. Der größte erforderliche Multiplizitätsblock im Singulett hat damit nur 262 Dimensionen. Die Blockmatrizen selbst wurden in dieser Runde nicht sämtlich konstruiert oder diagonalisiert.

### 4.3 Ein expliziter Projektor für das Quartett

Für die vierdimensionale Standarddarstellung von S5 ist χ4(π)=fix(π)−1. Auf dem Singulettträger mit Darstellung R gilt der exakte zentrale Projektor

\[
P_4=\frac1{480}\sum_{a\in N,\pi\in S_5}
(\operatorname{fix}(\pi)-1)R(a,\pi),
\qquad \operatorname{rank}P_4=320.
\]

Die Idempotenz wurde zusätzlich durch exakte Faltung des Standardcharakters in der S5-Gruppenalgebra geprüft. Das vollständige Translationsmittel ist unabhängig davon ein Projektor.

Noch kleiner wird die Rechnung mit \(\mathcal H=N\rtimes S_4\), wobei S4 eine Koordinate fixiert. Sei P_H das Mittel über diese 384 Elemente und P_G das Mittel über alle 1920 Elemente. Dann

\[
E_4=P_H-P_G,
\qquad E_4^2=E_4=E_4^\dagger,
\qquad \operatorname{rank}E_4=108-28=80.
\]

Dies folgt auch direkt aus Ind_(S4)^(S5)1=1⊕(4,1): Das S4-Mittel behält pro Standardkopie genau eine Richtung, und die Subtraktion entfernt den trivialen Anteil. Da H0 und F4,edge mit der Graphgruppe kommutieren, ist ran E4 ein exakt invarianter Spektralblock. Sein Spektrum ist das Spektrum des 80-dimensionalen Multiplizitätsoperators; im 320-dimensionalen isotypischen Raum erscheint jeder einfache Eigenwert vierfach.

**Was damit bewiesen ist:** Die betreffende Symmetrie trägt exakt Vierfachentartung, und es gibt einen expliziten 80-dimensionalen Reduktionsprojektor.

**Was nicht bewiesen ist:** Dass sein niedrigster Eigenwert einfach ist, dass kein anderer Block dieselbe Energie besitzt, und dass gerade dieser Eigenwert die erste Anregung des ganzen Modells bildet. Das ältere numerische Charakterresultat ordnet den beobachteten Vierercluster diesem Typ zu; seine numerische Zuordnung wird hier nicht zum exakten Energienachweis hochgestuft.

Die verwendete Young-/Inhaltsmethodik ist Standarddarstellungstheorie, siehe [Okounkov–Vershik](https://arxiv.org/abs/math/0503040).

### 4.4 Schärfere lokale Schranken

Für eine Ecke mit fünf Nachbarn ist A_v=5I−Σ_j S_(vj). Die Transpositionssumme ist ein Jucys–Murphy-Element nach Umnummerierung. Ihre Eigenwerte sind die Inhalte des zuletzt hinzugefügten Youngkastens. In (C4)^⊗6 treten nur Partitionen mit höchstens vier Zeilen auf. Deshalb ist der Inhalt zwischen −3 und 5 und

\[
\operatorname{spec}A_v\subset\{0,1,2,3,4,5,6,7,8\}.
\]

Die exakten Multiplizitäten im 4096-dimensionalen lokalen Tensorraum lauten:

| a | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Multiplizität | 84 | 560 | 1050 | 360 | 250 | 912 | 190 | 600 | 90 |

Aus 0≤a(a−1)≤7a folgt auf dem ganzen Materieraum

\[
0\le F_{4,\rm edge}\le7\sum_vA_v=14A,
\quad A=80I-2H_0\le64I,
\quad H_0\ge8I.
\]

Somit **∥F4,edge∥≤896**. Der Satz betrifft die kantenlokale vierte Ordnung auf dem SU(4)-Materieraum. Er ist keine Normschranke für den gesamten mikroskopischen Rest und keine entsprechende Aussage über die geteilte Bank.

Die Ganzzahligkeit liefert außerdem für jedes ganzzahlige k

\[
(a-k)(a-k-1)\ge0,
\quad
F_{4,\rm edge}\ge16k(19-k)I-8kH_0.
\]

Insbesondere gilt für k=6: F4,edge≥1248I−48H0. Bei t/Δ=1/20 folgt

\[
H_{\rm tr}=H_0+\frac1{800}F_{4,\rm edge}
\ge\frac{47}{50}H_0+\frac{39}{25}I.
\]

Falls auf jedem Nichtsingulett H0≥58/5=11,6 und eine korrigierte Quartettenergie ≤249/20=12,45 zertifiziert werden, folgt dort

\[
H_{\rm tr}\ge\frac{1558}{125}=12{,}464>12{,}45.
\]

Damit reicht für diesen Vergleich eine wesentlich gröbere Zertifizierung als die Reproduktion von 12,133537149348086 auf viele Stellen. **Beide Voraussetzungen sind weiterhin zu zertifizieren.** Die ältere Ritz-Numerik allein liefert insbesondere keine garantierte Untergrenze.

Mehrere nichtkommutative Operatoruntergrenzen dürfen nicht ohne weiteres durch ihr punktweises Maximum ersetzt werden. Die obige Folgerung benutzt nur eine feste lineare Schranke mit positivem H0-Koeffizienten und vermeidet dieses Problem.

### 4.5 Was ein wirklicher Abschluss jetzt noch erfordert

Die Reduktion gibt einen konkreten Zertifizierungsweg: rationale Darstellung und Gram-Matrix auf den reduzierten Räumen bauen; für rationale Schwellen die Trägheit des entsprechenden hermiteschen Matrixbüschels bestimmen; Eigenwertanzahlen unterhalb und oberhalb des Quartetts beweisen; anschließend die Nichtsingulettschwelle prüfen. Ein kleiner Residualvektor beweist Existenz eines nahen Eigenwerts, nicht die Abwesenheit weiterer kleinerer Eigenwerte.

Für die volle Mikrodynamik muss zusätzlich ein kanonisch passender Rest kontrolliert werden. Ein energieabhängiger Feshbachrest ist ohne weitere Umrechnung nicht der Normrest des symmetrisch normalisierten H2+H4-Operators. Die [Schrieffer–Wolff-Methodik](https://arxiv.org/abs/1105.0675) löst diese modellspezifischen Zertifikate nicht automatisch.

**Status Follow-up 3:** Die exakte Symmetriereduktion und zusätzliche Operatorgrenzen sind geschlossen. Spektralreihenfolge, exakte Multiplizität des ersten Niveaus im Gesamtmodell und mikroskopischer Rest bleiben ungelöst.

## 5. Follow-up 4: Filter, Clockfehler und gekoppelte Zellen

### 5.1 Exakte Eingangsraumreduktion des gemeinsamen Filters

Setze M=2G⋆=3I+S01+S02+S03 auf den 256 Materiedimensionen. Neben dem Zweisingulett χ und Ω benötigt das ideale Echo nur

\[
z=C^\dagger S_{01}C\Omega,
\qquad B_\pm\Omega=(\Omega\pm z)/2.
\]

Ganzzahlige Rechnung auf allen 256 Komponenten ergibt für χ, Ω und z

\[
M(M-I)(M-3I)(M-4I)(M-5I)v=0.
\]

Die Eigenwerte M=2 und M=6 werden also nicht besetzt. Die exakten Gewichte sind:

| Zustand | M=0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| χ | 1/6 | 1/3 | 0 | 1/3 | 1/6 | 0 | 0 |
| Ω | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| z | 1/16 | 7/48 | 0 | 1/8 | 5/48 | 9/16 | 0 |
| B+Ω | 25/64 | 7/192 | 0 | 1/32 | 5/192 | 9/64 | 0 |
| B−Ω | 9/64 | 7/192 | 0 | 1/32 | 5/192 | 9/64 | 0 |

Die letzten beiden Zeilen sind Gewichte unnormierter Ergebniszweige. Ihre Normen sind 5/8 und 3/8.

Jeder besetzte Materieeigenraum g=M/2 erzeugt unter H⋆ seinen niedrigen und hohen Partner. Das dunkle reine Vermittlerband hat keinen Überlapp mit einem nackten Materieeingang. Der benötigte H⋆-invariante Raum besteht daher aus den beiden Partnern zu g∈{0,1/2,3/2,2,5/2}. Seine Dimension ist 2(1+30+40+15+90)=352.

Es gibt dort zehn verschiedene Energien. Ein Faktor pro unerwünschter Energie benötigt **neun Faktoren**:

\[
F_9(H)=\prod_{E\in\mathcal S\setminus\{E_0\}}
\frac{I+\exp[-i\pi(H-E_0)/(E-E_0)]}{2}.
\]

Auf diesem Raum ist F9 exakt der angekleidete Grundzustandsprojektor. Derselbe F9 funktioniert für Start und Ende. Nach dem Leerbelegungsherald ergeben sich unverändert wPΩ und die v1.4-Rohwahrscheinlichkeiten w²/6, w⁴/6 und 17w⁴/192.

| Aufwand | Vollraumfilter v1.4 | Neue Eingangsraumvariante |
|---|---:|---:|
| Zeitfaktoren pro Filter | 13 | 9 |
| Zeitfaktoren Start + Schluss | 26 | 18 |
| Zeit pro Filter in ℏ/Δ | 3172,829634 | 2310,304940 |
| Zeit Start + Schluss in ℏ/Δ | 6345,659268 | 4620,609881 |

Das spart rund 27,18 % der schwachen Entwicklungszeit. Nicht eingerechnet sind Recordpulse, Herald-Messungen, Reset und fehlgeschlagene Versuche. Es ist keine Optimalitätsbehauptung.

Die Negativkontrolle prüft ausdrücklich, dass F9 außerhalb dieses Raums unerwünschte Energien durchlassen kann. Deshalb bleibt F13 der geeignete Ausgangspunkt für beliebige unbekannte Materie-/Vermittlereingänge und für Fehler, die die ausgeschlossenen Sektoren besetzen. Eine nur zeitlich fehlerhafte Funktion desselben H erhält die Spektralstütze; allgemeine Zustands- oder Operatorfehler tun das nicht.

### 5.2 Eine schärfere Schranke für reine Zeitfehler

Zunächst bleibt H exakt und die Referenzphase läuft mit derselben tatsächlichen Zeit wie H. Für τ′j=(1+ξj)τj, |ξj|≤u≤1, bleibt der Zielwert jedes Faktors eins. Auf einem unerwünschten Eigenwert Ej hat dessen eigener Löschfaktor den Betrag

\[
\left|\frac{1+e^{-i\pi(1+\xi_j)}}2\right|
=|\sin(\pi\xi_j/2)|\le\eta,
\qquad \eta=\sin(\pi u/2).
\]

Alle anderen Faktoren haben Betrag ≤1. Daher gilt für den vollständigen F13

\[
\|F_{13}'-P_{0,\rm dressed}\|\le\eta.
\]

Der Operatorfehler wird hier nicht mit der Summe aller langen Zeiten multipliziert. Entscheidend ist der eigene Löschfaktor jedes unerwünschten Niveaus.

Nach dem Leerbelegungsherald ist der Ω-Anteil mindestens w−(1−w)η; der orthogonale Teil wird höchstens mit η multipliziert. Weil χ die Gewichte 1/6 und 5/6 trägt, folgt für die **bedingte Präparationsinfidelität**

\[
1-F_{\rm prep}\le
\frac{5\eta^2}{[w-(1-w)\eta]^2+5\eta^2}.
\]

Bei t/Δ=1/20 liefert u≤2,80615835·10⁻⁴ die Zielgrenze 10⁻⁶. Beispielsweise ergibt u=10⁻⁴ eine Schranke von ungefähr 1,26991·10⁻⁷. Eine numerische Stichprobe verschiedener unabhängiger Zeitfehler liegt unter den bewiesenen Schranken; die Stichprobe ist nicht deren Beweis.

### 5.3 Eine fest programmierte Referenzphase muss gesondert behandelt werden

Wenn nur die physische H-Entwicklung länger läuft, die kompensierende Phase aber beim Nominalwert bleibt, ist der Zielwert nicht mehr exakt eins. Allgemein sei θ0,j die tatsächliche Phasenabweichung auf E0 und |θ0,j|≤vj. Dann genügen

\[
\eta=\max_j\sin[(\pi u+v_j)/2],
\quad
a=w\prod_j\cos(v_j/2)-(1-w)\eta>0,
\quad
1-F_{\rm prep}\le\frac{5\eta^2}{a^2+5\eta^2},
\]

sofern die verwendeten Winkel im monotonen Bereich liegen. Bei nominal festgehaltener Referenzphase ist vj=|E0|τj u/ℏ. Die entsprechende ausreichende Grenze beträgt **u≤3,96741926·10⁻⁵**.

Diese Aussagen betreffen ein einzelnes Präparationsinstrument mit idealem Eingang und idealem Belegungsherald. Sie sind kein vollständiges Fehlerbudget der Echo-Rohstatistik. Nichtkommutierende Hamiltonfehler, fehlerhafte Resonanz, Tick-, Record-, Mess- und Resetfehler benötigen zusätzlich eine gemeinsame Instrument-/Kanalabschätzung. Die alte allgemeine δH-Schranke und die neue reine Zeitschranke haben verschiedene Voraussetzungen und dürfen nicht gegeneinander als experimentell gemessene Toleranzen ausgespielt werden.

### 5.4 Eine vollständig lösbare gekoppelte Referenzfamilie

Für N vollständige Tetramerzellen sei

\[
H_{0,N}=\sum_iH_{{\rm tet},i},
\qquad \Omega_N=\Omega^{\otimes N}.
\]

Jede Zelle hat genau diesen Grundzustand und eine Lücke 2J. Wähle einen lokalen spurfreien Pauli A_i auf einem Materieträger der Zelle und θ=π/8. Auf einer offenen Kette definiere

\[
V_N=\prod_{i=1}^{N-1}\exp[-i\theta A_iA_{i+1}],
\quad H_N=V_NH_{0,N}V_N^\dagger,
\quad \Psi_N=V_N\Omega_N.
\]

Alle Brückengatter kommutieren und lassen sich in zwei Schichten gerader/ungerader Kanten ausführen. Die konjugierten Zellterme besitzen nur endliche Nachbarschaftsreichweite. Es entstehen tatsächliche zellübergreifende Operatoren; der Grundzustand ist verschränkt.

Unitäre Äquivalenz beweist für **jede** Zellzahl E0=0, eindeutigen Grundzustand ΨN und Gap 2J auf dem ganzen 256^N-dimensionalen Raum. Für zwei Zellen lautet der Zustand exakt

\[
\Psi_2=\cos\theta\,\Omega\Omega-i\sin\theta\,(A\Omega)(A\Omega),
\]

mit orthogonalen Schmidtvektoren. Die Entropie des ersten Schnitts ist h2(sin²θ)=0,600876… Bits. Sie bleibt für die dargestellte offene Kette an diesem Schnitt gleich. Die numerischen Kontrollen für 2,3,4,6,8 Zellen laufen im exakt invarianten logischen Teilraum span{Ω,AΩ}^⊗N, nicht durch vollständige Speicherung von 256^N Komponenten. Die Behauptung für den Vollraum folgt aus der unitären Konjugation, nicht aus diesen kleinen Diagonalisierungen.

Für den v1.4-Feedbackkanal E definiere

\[
\mathcal F_N=\operatorname{Ad}_{V_N}\circ\mathcal E^{\otimes N}
\circ\operatorname{Ad}_{V_N^\dagger}.
\]

Dann ist ΨN der eindeutige stationäre Zustand und für beliebige, auch verschränkte Eingänge gilt

\[
1-F_{\Psi_N}(\mathcal F_N^m\rho)\le Nr^m,
\quad r=1-\frac{1-(9+\sqrt{17})/32}{24}.
\]

Bei lokalen Fehlern ε pro dekodiertem Zellzyklus in halber Diamantnorm und idealen V-Gattern folgt

\[
1-F_{\Psi_N}\le Nr^m+N\varepsilon\frac{1-r^m}{1-r}.
\]

Für N=4096 und je die Hälfte des Gesamtbudgets 10⁻⁶ für Konvergenz und Zyklusfehler genügen m=918 und ε≤3,0004·10⁻¹². Das ist eine konservative globale Genauigkeitsforderung; eine lokale Genauigkeitsforderung hat keinen zusätzlichen Faktor N. Fehler des abschließenden V-Networks verbrauchen ein weiteres Budget und sind hier nicht mit null gleichzusetzen.

Mehrere ideale konjugierte Zyklen lassen sich als V(E^m)^⊗N V† ausführen, weil die inneren V†V wegfallen. Reset und deren Informationsabfluss bleiben reale Ressourcen.

**Entscheidende Grenze:** Diese Familie ist absichtlich aus einem Produktmodell konstruiert. Ihre konjugierten Zellterme kommutieren miteinander; sie besitzt keine dadurch hergeleitete propagierende relativistische Vielteilchendynamik. Sie ist ein kontrollierter positiver Prüfmaßstab für gekoppelte Präparation und ein negativer Prüfmaßstab für zu starke Raumzeitfolgerungen. Die allgemeine Stabilität schwach gestörter Produktphasen ist zudem Gegenstand bekannter Sätze, etwa [Yarotsky](https://arxiv.org/abs/math-ph/0411042); eine numerische Gültigkeitsschwelle für den ursprünglichen TFPT-Hamiltonoperator wurde daraus hier nicht abgeleitet.

**Status Follow-up 4:** Eingangsraumfilter und reine Zeitfehler sind mathematisch bearbeitet; eine skalierende gekoppelte Referenzpräparation ist konstruiert. Das vollständige reale Fehler-/Reset-/Umgebungsbudget und die ursprüngliche native Vielzellenfamilie bleiben offen.

## 6. Follow-up 5: Eine gemeinsame Welt, T2/T3/T4/T5/T7

Die Forderung nach derselben Familie ist notwendig. Keine der obigen Verbesserungen liefert die noch fehlende Familie mit 3+1D-Ausbreitung, chiralem Maß und dynamischem Spin 2.

**Analytische Halbladung T2.** Auf einer halbganzzahligen Ladungsleiter bewahren ausschließlich ganzzahlige Shifts die Parität Π=(−1)^(2Q). Produkte, Adjungierte und starke Grenzwerte beschränkter Operatoren im Paritätskommutanten bleiben dort. Eine Halbladungsoperation, die Π antikommutiert, entsteht dadurch nicht. Eine volle E8-Glue-Erweiterung kann zusätzliche intersektorielle Operatoren tragen; gerade deren Abbildung auf die tatsächliche Quelle und die gemeinsame dichte Domäne mit Energie- und Adjungiertenkontrolle fehlen. Der Satz betrifft die eingeschränkte gerade Algebra, nicht jede mögliche E8-Quelle. Die freie Boson-Vakuumnorm aus v1.4 ersetzt diese Kontrolle auf allgemeinen Zuständen nicht.

**Raumzeit T3.** Dieselben endlichen Clebsch-Zellen lassen verschiedene periodische Familien und unterschiedliche Geschwindigkeitstensoren zu. Die zusätzliche endliche Spektralinformation wählt daraus keine drei Raumrichtungen und keinen gemeinsamen Lorentzkegel aus. Erforderlich sind die aus der Quelle bestimmte Verbindungsvorschrift, ihre Skalierung sowie tatsächliche kohärente Korrelatoren, deren Pole für verschiedene Sektoren dieselbe Geometrie ergeben.

**Chirale Materie T4.** Drei Indexnullmoden bei eingesetztem Fluss drei erklären die Zahl drei nicht. Ein Index fixiert zudem die Differenz linker und rechter Nullmoden; zusätzliche vektorartige Paare können vorhanden sein. Die Ladungstabelle und ihre Anomaliesummen sind notwendige Konsistenzprüfungen, kein konstruiertes globales chirales Maß. Eine beliebige ganzzahlige Kopienzahl einer bereits anomaliefreien Familie bleibt perturbativ anomaliefrei; daraus wird keine Auswahl auf drei gewonnen.

**Wechselwirkender Grenzwert T5.** Die exakte gekoppelte Familie aus Abschnitt 5 ist für feste J durchgehend gapped und durch eine Schaltung endlicher Tiefe an die Produktphase gebunden. Ihre Existenz zeigt gerade, dass Lokalität, Verschränkung, Präparierbarkeit und ein stabiler Gap noch keinen interessanten relativistischen Kontinuumslimes implizieren. Ein kritischer Grenzprozess kann dadurch nicht ausgeschlossen werden; er ist aber zusätzlich zu konstruieren.

**Gravitation T7.** Für einen positiv gapped Hamiltonoperator besitzen verbundene Vakuum-Spektralfunktionen unterhalb des Gaps keine Anregungspole. Eine Projektion der Tensorindizes erzeugt keine neuen Energien. Auch in der neuen gekoppelten Referenzfamilie entsteht deshalb kein masseloser Spin-2-Pol in den angegebenen festen Energieeinheiten. Für den behaupteten gravitativen Sektor braucht es eine andere, aus derselben Quelle abgeleitete kritische Dynamik, physische Constraints, zwei Helizitäten und universelle Materiekopplung. Ein vorab angesetzter weicher Spin-2-Pol kann universelle Kopplung erzwingen; das Argument konstruiert den Pol nicht.

**Status Follow-up 5:** Keine vollständige Lösung gefunden. Die vorhandenen Gegenmodelle und die neue gekoppelte Familie widerlegen mehrere verkürzte Schlussfolgerungen. Sie widerlegen nicht die Möglichkeit einer stärkeren, noch nicht konstruierten TFPT-Theorie.

## 7. Follow-up 6: Gemeinsame Parameter statt getrennter Anpassung

Die ACT-Primärquelle wurde erneut direkt geprüft: Tabelle 5, Spalte P-ACT-LB2, v2 gibt ns=0,9752±0,0030 und log(10¹⁰As)=3,062 an. Das ist eine spezifische gemeinsame Datenauswertung im dortigen Modell, keine datensatzunabhängige Messung von ns. Quelle: [ACT DR6, v2](https://arxiv.org/abs/2503.14452v2).

Die unveränderte einfache TFPT-Inflationsbranche liefert nach Eliminierung von N

\[
A_s(1-n_s)^2=\frac{c_3^7}{6\pi^2},
\qquad r=3(1-n_s)^2.
\]

Um beide angegebenen Zentralwerte gleichzeitig zu treffen, müsste

\[
c_{3,\rm ACT}
=[6\pi^2 A_s(1-n_s)^2]^{1/7}
=0{,}03596504269049945\ldots
\]

statt c3=1/(8π)=0,03978873577297383… gelten. Die relative Änderung beträgt −9,60998888… Prozent.

Nun wird genau dieser geänderte Wert in die bereits im Hauptdokument vorgegebene elektromagnetische Gleichung eingesetzt, während deren übrige Koeffizienten unverändert bleiben:

\[
q(\alpha)=48c_3^4e^{-2\alpha},
\quad \phi_s=\frac1{6\pi}+q(1-q)^{-5/4},
\]
\[
\alpha^3-2c_3^3\alpha^2-\frac45\,41c_3^6\log(1/\phi_s)=0.
\]

Mit 65 Dezimalstellen Arbeitspräzision ergeben sich

| Parametervertrag | α⁻¹ aus derselben Gleichung |
|---|---:|
| Ursprüngliches c3 | 137,0359992168407125… |
| Auf die ACT-Zentralpaarung geändertes c3 | 167,8032986296328993… |

Dies ist eine konkrete gemeinsame Gegenrechnung. Eine unabhängige Änderung weiterer Koeffizienten wäre eine neue Theorieannahme und müsste gemeinsam begründet werden.

Bleibt c3 fest und wird ns auf den verwendeten Zentralwert kalibriert, müsste die führende Amplitude mit **0,4929956404…** multipliziert werden, um As zu treffen. Das ist die erforderliche Größe einer solchen Korrektur, kein hergeleiteter Korrekturmechanismus. Eine gemeinsame Likelihood mit Reheating, Schleifen, systematischen Fehlern und Theorieunsicherheiten wurde hier nicht gerechnet. Die Diagnose ist daher weder ein vollständiger statistischer Ausschluss der Theorie noch eine Reparatur ihrer Inflation.

Für Flavour fehlt weiterhin eine aus derselben Wirkung und demselben Zustand bestimmte Überlappstruktur. Ein konstantes Skalarprofil und identische orthonormale linke/rechte Nullmoden liefern Y_ab=yδ_ab; daraus folgen keine Massenhierarchie oder nichttriviale Mischung. Frei gewählte Texturen würden den geforderten Ursprung ersetzen. Weitere im Hauptdokument genannte Lepton-, Higgs-, Proton-, Neutrino- und Kosmologiewerte brauchen jeweils ihr einheitliches Massenschema, RG, Schwellen und Transfer; diese vollständigen Rechnungen wurden nicht neu durchgeführt.

**Status Follow-up 6:** Die einfachste gemeinsame c3-Reparatur ist im fixierten Gleichungsvertrag ausgeschlossen. Eine konsistente gemeinsame Wirkung mit Flavour und empirischem Transfer ist ungelöst.

## 8. Weitere ausdrücklich offene Fragen

| Frage | Was für eine vollständige Lösung fehlt | Ergebnis dieser Runde |
|---|---|---|
| RH / signierte Weil-Form | Identität der ursprünglichen vollständigen Form mit einer unabhängig konstruierten positiven Norm für die ganze erforderliche Testklasse, inklusive Ränder und Grenzübergänge. | Kein Beweis. Die aktuelle Quellenprüfung scheitert weiterhin an einem fehlenden gepinnten Forschungsordner. |
| Faktorisierung | Ein nativer skalierender Compiler und eine Auslesung mit vollständig bilanzierten Ressourcen in der Bitlänge. | Die zugängliche r647-Route kodiert Faktoren, besitzt aber keine daraus bewiesene schnelle Auslesung. |
| P versus NP | Ein eigener uniformer klassischer Algorithmus mit Beweis und polynomiellen Kosten für eine NP-vollständige Aufgabe oder ein entsprechender Unmöglichkeitssatz. | Unentschieden; auch effiziente Quantenfaktorisierung allein würde P=NP nicht beweisen. |
| Dunkle Materie | Stabiler Sektor, Kopplungen, Produktion und quantitative kosmologische Dichte. | Kein solcher Sektor aus derselben Quelle berechnet. |
| Dunkle Energie | Gravitative Vakuumwirkung, Zustand, Renormierung und radiative Stabilität. | Ein kleiner dimensionsloser Formelwert schließt diese Aufgaben nicht. |
| Baryogenese | Dynamische CP-/B-Verletzung und Nichtgleichgewichtsentwicklung mit berechneter Ausbeute. | Eine Eingangsgröße Ωb oder ein umgerechnetes ηB ist keine Herleitung. |
| Starkes CP | Schutz von θ̄ im fertigen fermionischen Maß inklusive Massenphasen und Anomalien. | Interne Vorzeichenmuster und formale Pfaffianpositivität liefern diesen Transfer nicht. |
| Schwarze Löcher | Zunächst der native gravitative Sektor, dann Horizonte, Entropie und konsistente Quantendynamik. | Keine Lösung aus dem endlichen Record-/Reset-Labor. |
| Zeitpfeil und Zustandsauswahl | Ein aus der Quelle bestimmter Zustand und eine physische Umgebungs-/Korrelationsstruktur. | Endliche Resetkapazität ist bilanziert; kosmologische Anfangsbedingungen sind nicht hergeleitet. |
| Messproblem | Vollständige gemeinsame Dynamik und Wahrscheinlichkeitsregel oder überprüfbare Abweichung. | Der Laborvertrag setzt Born-Regel und Instrumente voraus; er leitet sie nicht her. |

Die lokale RH-Prüfung meldet konkret `SOURCE_UNAVAILABLE` für `/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research`. Aus dem vorhandenen Katalog wurden r404 und r647 ausgewählt und zugängliche Originale gelesen. r404 trägt die eingegrenzte Fehlerklasse **RESTATEMENT**: die gesuchte quellenseitige Gram-Identität ist nicht durch nachträgliche Choleskyzerlegung bewiesen. r647 trägt **STRUCTURAL_MISMATCH**: die konkrete E8-Gauss-/ggT-Momentroute enthält noch keine effiziente vollständige Auslesung. Diese Klassifikationen werden nicht auf jede denkbare andere RH-/Faktorroute verallgemeinert. Eine Vollkenntnis der nicht verfügbaren neueren externen Quellen wird nicht behauptet.

## 9. Konkreter verbleibender Arbeitsstand

| Follow-up | Neu geschlossen | Weiter offen |
|---|---|---|
| 1: Controller | Phasenreferenzobstruktion, expliziter Ressourcenvertrag, endliche Programmeinbettung, Resetkapazitätsargument. | Native Umsetzung sämtlicher Kontrollen und deren physischer Ursprung. |
| 2: Architektur | Erhaltung aller angegebenen lokalen Qv erzwingt in der benannten Modenbasis Kantenadressierung. | Ableitung dieser Ladungen und der Modenbasis aus TFPT. |
| 3: Quartett | Exakte 18-Typ-Zerlegung; Projektoren mit Rang 320 und 80; neue F4-Unter-/Obergrenzen. | Zertifizierte Energieordnung, Nichtsingulettkonkurrenz und mikroskopischer Rest. |
| 4: Robustheit | Exakter 9-Faktor-Eingangsraumfilter; zwei reine Zeitfehlerbounds; gekoppelte lösbare Referenzfamilie. | Vollständiges physisches Fehlerbudget, Umgebung und native skalierende Dynamik. |
| 5: Gemeinsame Welt | Präzisierte Gegenmodelle; die gekoppelte Referenz liefert keinen masselosen Pol. | Native 3+1D-Familie, Halbladungsdomänen, chirales Maß, Streuung und Spin 2. |
| 6: Gemeinsame Daten | c3-Verschiebung im fixierten Inflations-/Alpha-Vertrag nachgerechnet und unvereinbar. | Gemeinsame Wirkung, Flavour, Korrekturen und Likelihood. |

Der nächste tatsächlich endliche Beweisengpass ist jetzt enger: die durch E4 definierte 80-dimensionale Quartettmatrix und die 28-dimensionale triviale Matrix exakt aufbauen, die Energieordnung gegen die übrigen Symmetrietypen zertifizieren und den gröberen Nichtsingulettbound prüfen. Das schließt bei Erfolg zunächst den trunkierten Spektralteil. Die native Kontrollquelle und der mikroskopische Rest bleiben eigene Anforderungen.

Die größere Forschungsfrage hat weiterhin dieselbe Form: Ein einziges explizites Quellobjekt muss Operationsalgebra, Zustand, lokale Kopplung, Skalierung und Auslesung zusammen bestimmen. Solange verschiedene zugelassene Fortsetzungen unterschiedliche Architekturen, Dimensionen oder physikalische Ausgaben liefern, ist eine eindeutige vollständige Lösung aus den bisherigen Daten nicht ableitbar. Das ist eine nachgewiesene Unterbestimmtheit bestimmter Rekonstruktionsschlüsse, kein Beweis, dass eine vollständigere Theorie unmöglich wäre.

## 10. Reproduktion

Das beiliegende Prüfarchiv enthält drei Rechenprogramme, ihre Ergebnisse und einen Replay-Prüfer:

- `exact_symmetry.py`: exakte Gruppe, Charaktere, Zerlegung und zentrale Projektorprüfung.
- `continuation_checks.py`: unabhängiger Charaktervergleich, Sternspektrum, Zeitfehler, gekoppelte Referenz und gemeinsame Parameterrechnung.
- `protocol_support.py`: exakte Spektralstütze, 9-Faktor-Filter und rationale Ausschlussschwelle.
- `replay.py`: normale und optimierte Ausführung sowie gezielt fehlerhafte Varianten.

Ausführung mit Python und installierten `numpy scipy sympy mpmath`: `python3 replay.py`.

Die normale und die mit `-OO` optimierte Ausführung liefern bytegleiche Resultate. Fünf gezielte Fehlvarianten werden am erwarteten inhaltlichen Prüfpunkt erkannt: falsche Charakternormierung, weggelassene Echoenergie, entfernte Antisymmetrie, entfernte Zwischenzellkopplung und geänderter Alpha-Koeffizient. Das ist eine Integritätskontrolle der benannten Rechnungen, keine automatische Verifikation der gesamten Theorie.

Die Ergebnisdateien führen die nicht ausgeführten vollständigen Zertifikate ausdrücklich mit. Originalpapiere und vorhandene Abschlussmarker wurden nicht überschrieben. Das Dokument ist eine neue Forschungsfortsetzung mit partiellen Lösungen und offenen Beweisen.
