# Compiler-Herkunft: Die Übergangsregel ist vorhanden, ihre vollständige Bedeutung nicht

13. September 2026. NON-RH. Quellenaudit und exakte endliche Gegenmodelle.
Keine T1–T8-Hochstufung, kein identifiziertes Universalobjekt. Die vorherigen
Kettenresultate bleiben gültige bedingte Ergebnisse; sie werden hier nicht weiter optimiert.

**Aktuell: Zusammensetzung und Registervertrag.** Die gemeinsame
Gleichheitsphasen-Kopplung zerfällt in zwei registerübergreifende CZ-Gates
plus lokale Clifford-Operationen. Für alle 15 Quellkontexte ist die explizite
Vor-Messung unitär und selbstinvers: kohärente Registerwiederverwendung kann
einen Schritt rückgängig machen, während frische Register die iterierte
Messabbildung erzeugen. Alle nichtselektiven Kontextmessungen komponieren
über den Schnitt ihrer Pauli-Achsen; ausgewählte Ergebnisprotokolle behalten
jedoch Reihenfolgeinformation. [Herleitung und Grenzen](RECORD_COMPOSITION.md).
Die eigentliche Interregister-Kopplung und die Bereitstellung der Register
sind noch nicht aus der mikroskopischen Quelle hergeleitet.

**Neue Fortsetzung:** Die Originalquelle v783 ordnet die Labels bereits
vollständigen Messkontexten mit insgesamt 60 Gaussian-E8-Strahlen zu.
Unter expliziten Born-/Wiederholbarkeits- und K-Ausführungsprämissen ist
darauf ein eindeutiger endlicher Prozess konstruiert; seine beiden exakt
geschlossenen Projektionen sind K und eine Quantenkontraktion um 3/7.
Siehe [Kontext-Instrument: Konstruktion, Herkunftsgrenze und Beweis](CONTEXT_INSTRUMENT.md).
Das präzisiert die unten dokumentierte erste Runde, ersetzt aber keine
mikroskopische Herleitung der Messprämissen.

Zusätzlich sind die Kontextmessabbildung und eine kohärente selektive
Realisierung durch bereits vorhandene Wurzelspiegelungen dargestellt.
Der gemeinsame aktuelle Laufbeleg umfasst alle drei Prüfer, 10.574 Guards
pro Modus und acht erkannte Mutationen. Die unten genannten zwei Prüfer
und fünf Mutationen dokumentieren den vorherigen Stand.

## 1. Die wichtige Korrektur des Neustarts

Die Aussage „Der ursprüngliche Compiler liefert nur Wortkomposition und gar
keinen Prozess“ wäre zu stark. Bereits
[v752:576](../../../verification/v752_projective_hamming_incidence.py#L576)
enthält den klassischen Übergangskern

\[
P=\mathbb F_2^4\setminus\{0\},\quad
B_{xy}=\mathbf1_{\bar h(x,y)=0},\quad K=B/7.
\]

Jedes Label besitzt sieben inzidente Ziele einschließlich sich selbst. Die
Normierung ist **bei festgehaltener gleichmäßiger Inzidenzregel** eindeutig.
Dass die Natur genau diese Regel ausführt, ist eine weitere Aussage. Der
[Schluss der Originalnote](../../../note_e8_gaussian_code.tex#L701)
behauptet ausdrücklich keine physikalische Auslesestruktur.

Es fehlt also nicht einfach „noch eine Matrix“. Zu prüfen ist, welches
Zustands-/Ereignismodell die vorhandene Matrix tatsächlich beschreibt.

## 2. Herkunftsbuch: nichts doppelt als Herleitung zählen

| Ebene | Vorhandene Quelle | Nicht dadurch bewiesen |
|---|---|---|
| Gitter und Quotient | Construction A, komplexe Struktur J, sigma, V=L/(1+i)L, Paarung; v752/v774 | Physische Zustände, Messungen oder Ereigniszeiten |
| Markierungen und Selektoren | Zwei J/sigma-invariante Codeplatzierungen, eine Koordinatenkonvention; q-Selektor sigma-invariant, q(A)=1, q(Fsum)=0 | Voraussetzungslos eindeutige Weltwahl; Chart-Konventionen sind aber auch nicht automatisch physikalische Zusatzparameter |
| Darstellung | Geordneter Kokzyklus, Clifford-Wörter auf C4; compiler-clifford-bridge | Identifikation des Kokzyklus mit der geladenen Seam oder einer ausführbaren Operation |
| Ursprünglicher klassischer Prozess | K=B/7 auf 15 nichttrivialen Labels | Vollständige Quanten-Zustandsänderung und kontinuierliche Uhr |
| Frühere bedingte Vervollständigung | Räumliche Kette, Paar-Hamiltonoperator, Zustandsansatz | Herkunft dieser Modellwahl aus dem Compiler |

Die Selektorzählung 4→2→1 steht in
[v774:713](../../../verification/v774_arf_spinor_compiler.py#L713).
Die beiden Codeplatzierungen sind in
[Originalnote:102](../../../note_e8_gaussian_code.tex#L102) beschrieben.
Die konkrete Klassen-zu-Materie-Lesart wurde bereits durch
[v775](../../../verification/v775_gaussian_class_d5_purity.py) eingeschränkt;
der Quellenaudit hebt diesen negativen Befund nicht auf.

## 3. Exakter Test an K selbst: gleicher klassischer Prozess, andere Quantenantwort

**Zusätzlicher, ausdrücklich bedingter Versuchsraum:** Wir erweitern das
klassische 15-Label-Register zu H_label=C15. Das ist NICHT der C4-Spinorträger,
keine Ableitung physischer Hilbertraumdimension und keine Realisierung der
gesamten vorzeichenbehafteten Compiler-Wortalgebra.

### Modell M: messen und neu präparieren

\[
\mathcal M(\rho)=\sum_{x,y}K_{xy}\rho_{yy}|x\rangle\langle x|.
\]

Kraus-Operatoren sind sqrt(K_xy)|x><y|. Nichtnegative K-Einträge und
Spaltensumme eins beweisen vollständige Positivität und Spurerhaltung.
Dies ist die bekannte Measure-and-prepare-Konstruktion, keine neu erfundene
Kanaltheorie; siehe [Horodecki–Shor–Ruskai](https://arxiv.org/abs/quant-ph/0302031).

### Modell R: zufällige kohärente Umordnung

Der 7-reguläre bipartite Inzidenzgraph zerfällt in sieben perfekte Matchings.
Der Prüfer konstruiert sie ausdrücklich, ohne eine Zerlegung nur vorauszusetzen:

\[
B=\sum_{j=1}^7 P_j,\qquad
\mathcal R(\rho)=\frac17\sum_jP_j\rho P_j^\dagger.
\]

Jedes P_j ist eine Permutationsmatrix, also unitär. Das beweist wiederum
vollständige Positivität und Spurerhaltung. R ist eine Mischung unitärer
Operationen, **nicht selbst als Ganzes eine reversible Operation**.

Beide Modelle senden jede diagonale Eingabe diag(p) auf diag(Kp).
Damit stimmen alle klassischen Historien überein, die aus diagonaler
Präparation und aufeinanderfolgenden projektiven Labelmessungen bestehen.
Unbeobachtete Zwischenintervalle ergeben K^n. Dies ist kein Gleichheitssatz
für beliebige kohärente Eingriffe oder vollständige Quanten-Prozesstensoren.

### Dieselbe Symmetrie beseitigt den Unterschied nicht

Die beliebige Matching-Wahl kann die sichtbare Symmetrie brechen. Daher
verwenden wir als Gegenmodell tatsächlich den Gruppendurchschnitt

\[
\overline{\mathcal R}=\frac1{|G|}\sum_{g\in G}
\operatorname{Ad}_{P_g}\circ\mathcal R\circ\operatorname{Ad}_{P_g^{-1}},
\quad G=\operatorname{Sp}(4,2).
\]

Der Prüfer enumeriert alle 720 linearen Paarungsautomorphismen und überprüft
K-Invarianz. Die 5040 so erhaltenen Permutations-Kraus-Terme induzieren
weiterhin genau K. Der Gruppendurchschnitt ist kovariant; M ist es ebenfalls.
Diese stärkere Symmetrie ist ein Test, keine Behauptung, alle diese
Transformationen seien physisch auszuführen oder müssten die markierte
Anker-/Familienstruktur erhalten. Die Konstruktionen erhalten insbesondere
deren relevante symplektische Untergruppen.

### Eine einzige feste Messung trennt die Modelle

Für |+> = (1/sqrt(15)) sum_y |y> gilt

\[
\mathcal M(|+\rangle\langle+|)=I_{15}/15,\qquad
\overline{\mathcal R}(|+\rangle\langle+|)=|+\rangle\langle+|.
\]

Die Messung des Projektors |+><+| hat somit Wahrscheinlichkeit **1/15**
beziehungsweise **1**. Der zweite Kanal erhält diesen kohärenten Zustand,
nicht zwangsläufig beliebige Quanteninformation. Physische Verfügbarkeit
dieser Präparation und Messung wird gerade NICHT aus dem klassischen K gefolgert.

Insbesondere: K hat einen eindeutigen gleichverteilten stationären Zustand,
denn K² hat strikt positive Einträge. M hat entsprechend nur I/15 als
stationäre Dichtematrix. R-bar fixiert dagegen mindestens I/15 und |+><+|.
**Ein eindeutiger klassischer Fixpunkt wählt nicht automatisch einen
eindeutigen Zustand einer kohärenten Erweiterung.**

Dieser Test vervollständigt denselben ursprünglichen klassischen Ausschnitt
auf zwei verschiedene Arten. Er beweist weder, dass beide Erweiterungen den
gesamten Compiler realisieren, noch, dass keine weiteren Quellregeln zwischen
ihnen entscheiden können.

## 4. Die ursprüngliche Regel enthält diskrete Vorzeicheninformation

Der erneut exakt geprüfte charakteristische Ausdruck lautet

\[
\operatorname{spec}(K)=\{1,(2/7)^{\times9},(-2/7)^{\times5}\},\qquad
\det K=-(2/7)^{14}<0.
\]

Für jede reelle Matrix L gilt det(exp(tL))=exp(t tr L)>0. Deshalb kann
**ein Schritt K auf demselben geschlossenen klassischen 15-Label-Raum
nicht die endliche Zeit eines reellen autonomen kontinuierlichen
Markovprozesses sein**. Das ist ein Spektralhindernis, kein numerischer Fit.
Diskrete Markovschritte bleiben völlig zulässig; verborgene Zustände,
Quantenkohärenz zwischen Abtastpunkten und andere erweiterte Modelle werden
dadurch nicht ausgeschlossen.

Mit Pi=J/15 gilt hingegen

\[
K^2=\frac4{49}I+\frac{45}{49}\Pi
=\exp\!\left[\log(49/4)(\Pi-I)\right].
\]

Denn Pi ist ein Projektor und exp[t(Pi-I)]=Pi+exp(-t)(I-Pi).
Der kontinuierliche Generator hat positive Übergangsraten außerhalb der
Diagonale und Zeilen-/Spaltensumme null. Die Zeiteinheit bleibt beliebig.

Die stochastische positive Wurzel

\[
K_+=\tfrac27 I+\tfrac57\Pi
\]

besitzt dasselbe Quadrat wie K, ist aber ein anderer Einzelschritt: Auf
einem fünfdimensionalen Kontrastraum wirkt K mit -2/7 und K+ mit +2/7.
Wer nur das Zweischrittbild erhält, hat diese Alternation verloren.
Eine positive kontinuierliche Interpolation des Quadrats darf deshalb
nicht nachträglich als Herleitung der ursprünglichen Einzelschrittuhr gelten.

## 5. Zusätzliche unabhängige Einfachheitsprüfung am C4-Spinor

Dies ist ein ANDERER typisierter Raum als Abschnitt 3, keine Identifikation.
Unter den zusätzlich verlangten Voraussetzungen „CPTP-Kanal auf M4,
kovariant unter allen Wortkonjugationen und unter dem vollen q*-Stabilisator
S5“ lässt sich die ganze Kanalfamilie klassifizieren.

Die 15 nichttrivialen Wörter zerfallen in fünf mit q=0 und zehn mit q=1.
Bezeichne die gleichmäßigen Konjugationsmittel über diese Mengen mit T5,T10.
Dann sind alle zulässigen Kanäle genau

\[
\Phi=p_0\,\mathrm{id}+p_5T_5+p_{10}T_{10},\qquad
p_j\ge0,\quad p_0+p_5+p_{10}=1.
\]

Begründung: Wortkovarianz diagonalisiert den Kanal in den 16 verschiedenen
Paarungscharakteren. S5 reduziert die Eigenwerte auf zwei nichttriviale
Bahnen. Die Fouriergewichte sind die Eigenwerte der Choi-Matrix in der
orthonormalen maximal verschränkten Wort-Bell-Basis und müssen nichtnegativ sein.
Das ist eine konkrete Anwendung bekannter Pauli-Kanalmethodik, kein
Neuheitsanspruch für diese allgemeine Methode;
[Petz–Ohno](https://arxiv.org/abs/0812.2668) behandeln verallgemeinerte Pauli-Kanäle.

Auch zeitlich homogene kontinuierliche Markov-Dynamik wird damit nicht
eindeutig. Ihr vollständiger Generatorenkegel ist

\[
\mathcal L=\gamma_5(T_5-\mathrm{id})+
\gamma_{10}(T_{10}-\mathrm{id}),\qquad\gamma_j\ge0.
\]

Notwendigkeit folgt aus den nichtnegativen Ableitungen der bei t=0
verschwindenden Choi-Gewichte; hinreichend ist die explizite
Poisson-Mischung der unitären Sprünge. Die beiden Zerfallsraten lauten

\[
r_5=(8\gamma_5+4\gamma_{10})/5,\quad
r_{10}=(4\gamma_5+6\gamma_{10})/5,
\quad 2/3\le r_5/r_{10}\le2
\]

für jeden nichttrivialen Prozess. Eine relative Rate bleibt sogar nach
Festlegung einer Zeiteinheit frei. Dies ist mehr als das frühere einzelne
Kanalgegenbeispiel, aber keine universelle Klassifikation aller TFPT-Prozesse.
Das volle S5 ist eine bewusste Symmetrieverstärkung und nicht aus der
markierten Quelle als physikalische Symmetrie abgeleitet.

## 6. Was jetzt als nächster Schritt gerechtfertigt ist

Nicht eine zusätzliche Struktur als „das Universalobjekt“ benennen. Zuerst
die fehlende Verbindung gezielt suchen:

1. **Träger und Ereignis:** Was ist ein Label in der Quelle — Zustand,
   Operator, Messkontext oder Ergebnis? Die 15 nichttrivialen Wörter sind
   nicht 15 orthogonale Zustände eines Viererträgers. Eine Quellabbildung muss
   diese Typen ausdrücklich verbinden.
2. **Phasenregel:** Aus den ursprünglichen Seam-/Compiler-Operationen die
   Zustandsänderung samt erhaltenen oder ausgelesenen relativen Phasen
   ableiten. Der Testfall lautet: Welchen Wert erzwingt dieselbe Quelle
   für eine festgelegte Interferenzantwort? Eine bloß festgelegte
   Dephasierung würde Modell M zwar auswählen, wäre aber noch keine Herleitung.
3. **Uhr und Komposition:** Danach prüfen, ob die gewählte Operation einen
   diskreten Schritt, eine Zeitabtastung eines größeren Systems oder einen
   offenen Prozess darstellt. K und K² müssen mitsamt den verlorenen
   Vorzeichen unterschieden werden. Physische Dauer separat herleiten.

**Abbruchkriterium:** Eine Konstruktion, die Träger, Messung, Dephasierung,
Raten oder Uhr nach gewünschtem Ergebnis frei setzt, bleibt bedingtes Modell.
Eine kleine zusätzliche Regel wäre ein Erfolg, wenn ihre Herkunft gezeigt
wird und sie mindestens eines der expliziten Gegenmodelle ausschließt,
ohne nur dessen abweichende Antwort per Definition zu verbieten.

Die unabhängige Herkunftsprüfung fand außerdem c=J sigma und J=iI im
ursprünglichen komplexen Chart: c hat dort Ordnung zwölf, Ad_c=Ad_sigma
auf isolierten Dichtematrizen jedoch nur Periode drei. Relative Referenzen
könnten den zentralen Phasenfaktor zugänglich machen; ihre Herkunft bleibt
ebenfalls offen. Dies ist keine universelle Aussage über alle Uhren.

## 7. Reproduktion und Reichweite

`label_lift.py` rekonstruiert die v752-Inzidenzregel mit der tatsächlichen
v774-Paarungsfunktion; beide Quelldateien sind SHA256-gepinnt. Es prüft
Matching-Zerlegung, sämtliche Paarungsautomorphismen, Gruppendurchschnitt,
Interferenzzeugen und das exakte Ein-/Zweischrittspektrum. Die ursprüngliche
E8-Wurzelklassifikation wird dabei nicht nochmals vollständig gerechnet.

`spinor_symmetry.py` prüft den gesonderten C4-Symmetriesatz direkt an den
gepinnten Clifford-Matrizen und den 120 q-erhaltenden Slotpermutationen.

Die gemeinsamen Wiederholungsläufe in `run_checks.py` bestanden:
7.361 endliche Guards im Labeltest und 575 im Spinortest, jeweils normal
und unter `-OO` mit byte-identischer JSON-Ausgabe. Fünf gezielt im Speicher
veränderte Varianten wurden unter `-OO` an der erwarteten Prüfstelle
zurückgewiesen. Sie verändern Inzidenz, Kraus-Normierung, Phasenerhaltung,
Spektralvorzeichen beziehungsweise Orbitgewicht. Kein Original wird verändert.
Der maschinenlesbare Laufbeleg mit Skript- und Quellhashes steht in
[`verification.json`](verification.json).

```sh
python3 -B experiments/theory-contracts/compiler-origin-audit-20260913/label_lift.py
python3 -B -OO experiments/theory-contracts/compiler-origin-audit-20260913/label_lift.py
python3 -B experiments/theory-contracts/compiler-origin-audit-20260913/spinor_symmetry.py
python3 -B -OO experiments/theory-contracts/compiler-origin-audit-20260913/spinor_symmetry.py
python3 -B experiments/theory-contracts/compiler-origin-audit-20260913/run_checks.py
```

Die Zahl endlicher Guards ist keine Zahl geschlossener Forschungsprobleme.
Alle T1–T8 bleiben offen. RH, Faktorisierung, P versus NP und Hylæans
Fähigkeiten wurden hier nicht untersucht; diese Resultate lösen keines
dieser Probleme durch bloße Übertragung.
