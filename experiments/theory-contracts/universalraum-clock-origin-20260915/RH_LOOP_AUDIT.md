# Zusatzprüfung: Schleifen, Primzahlen und der Universalraum-Vorschlag

15. September 2026, v1.6.6. Quellenprüfung des nachgereichten Textes
`59dc0059-8914-48ca-953d-85933f66e00b`, kein neuer RH-Beweis und kein neuer
arithmetischer Quellenoperator. Seine Aussagen über gemeinsame lokale
Beschreibungen werden getrennt im Überlappungsaudit behandelt.

## Urteil

**Ein globaler Wegraum ist eine sinnvolle Suchklasse; ein Eulerprodukt über
primitive Wege ist noch nicht das Eulerprodukt der Riemannschen Zetafunktion.**
Die im Text vorgeschlagene Xi-Determinante bleibt ein hinreichendes Ziel unter
expliziten Operatorannahmen. Das Umbenennen ihres noch fehlenden Operators in
„Generator der primitiven Schleifen“ konstruiert ihn nicht.

## 1. Was die endliche Bank tatsächlich ausschließt

Der beibehaltene Beweis aus v1.6.5 gilt für den ursprünglichen Hamiltonoperator
mit 64 Fermion- und 60 Bosonmoden, Δ>0. Der Hilbertraum ist wegen der Bosonen
**nicht endlichdimensional**. Endlich ist die Zahl der Moden. Mit
`C=960g²/Δ` folgt aus quadratischem Ergänzen

\[
H\ge\frac\Delta2N_b-C,
\qquad
N_H(E)\le2^{64}\binom{\lfloor2(E+C)/\Delta\rfloor+60}{60}.
\]

Dies widerspricht einem vollständigen energieerhaltenden Spektrum
`E_* log n + E_off`, E_*>0, weil dessen Zählfunktion exponentiell wächst.
Es ist kein Ausschluss beliebiger arithmetischer Untersektoren oder eines
anderen Operators mit nichtlinearer Energiezuordnung.

Ein großer Wegraum kann eine andere Zählfunktion besitzen. Die Gleichsetzung
„mehr Wege = mehr orthogonale Zustände unter derselben Energie“ muss aber
bewiesen werden. Verschiedene Wörter können denselben Operator oder Zustand
darstellen; ein Quantenüberlagerungsraum ist nicht ohne Weiteres der freie
Wortraum. Bei unendlich vielen identischen Zellen kann stattdessen die globale
Wärmespur divergieren. Der Text entfernt diese Fragen nicht durch Vergrößerung.

## 2. Der kleinste Gegencheck zur Primzahl-Automatik

Nehmen wir einen gerichteten Knoten mit zwei erlaubten Schleifen a und b.
Neben a und b ist auch ab ein primitiver periodischer Weg: Es ist keine Potenz
eines kürzeren Wortes. Ebenso entstehen weitere gemischte primitive Wörter.
Setzen wir nachträglich L(a)=log 2, L(b)=log 3, so hat ab die Länge log 6.
Die 6 ist keine Primzahl. „Primitiver Weg“ bedeutet nicht „arithmetische
Primzahl“.

Schon formal unterscheiden sich die zugehörigen erzeugenden Funktionen:

\[
Z_{\rm Wege}(x,y)=\frac1{1-x-y},\qquad
Z_{\rm zwei\ Primarten}(x,y)=\frac1{(1-x)(1-y)}.
\]

Der Koeffizient von xy ist links 2 und rechts 1. Links werden die beiden
Wörter ab und ba gezählt; rechts eine kommutative Besetzung. Im periodischen
Eulerprodukt bilden ab und ba eine zyklische Klasse, aber diese ist ein
**neuer primitiver Faktor**. Die Abweichung verschwindet damit nicht.

Eine kommutative freie Halbgruppe über vorgegebenen Primarten reproduziert
eindeutige Faktorzerlegung. Sie leitet aber weder die natürliche arithmetische
Markierung noch die logarithmischen Längen oder die passende Spur her.
Eine gekoppeltere Geometrie müsste gemischte Bahnen mit den richtigen
Amplituden, Relationen oder nachgewiesenen Auslöschungen behandeln. Dies ist
kein allgemeiner Ausschluss von Schleifenmodellen mit Interferenz.

Der Unterschied ist in den Originalarbeiten sichtbar: Kuipers, Hummel und
Richter konstruieren Quantengraphen mit dem passenden oszillierenden Anteil
der Nullstellendichte, weisen aber auf den anderen glatten Anteil und damit
das andere Spektrum hin. Das ist ein nützlicher Vorläufer, kein RH-Operator.
[Originalarbeit, Phys. Rev. Lett. 112, 070406](https://arxiv.org/abs/1307.6055)

Graphische Eulerprodukte besitzen ihre eigene Theorie. Auch eine aus einer
Graph-Zetafunktion bestimmbare Größe ist nicht automatisch effizient auslesbar.
Storm trennt in seiner Arbeit ausdrücklich berechenbare Zeta-Darstellung und
teure Auswertung bestimmter Graphinformationen.
[Originalarbeit zu Edge-Zetafunktionen](https://arxiv.org/abs/0708.1923)

## 3. Die richtige RH-Zielbedingung

Sei A strikt positiv und selbstadjungiert, mit kompakter Inverser und
`A^{-2}` von Spurklasse. Dann ist der Fredholm-Ausdruck

\[
D(z)=\det(I-z^2A^{-2})
\]

ganz, und seine Nullstellen liegen bei den reellen Zahlen ±λ_j(A), mit ihren
Multiplizitäten. Würde unabhängig und auf ganz C bewiesen

\[
\Xi(z)/\Xi(0)=D(z),\qquad \Xi(z)=\xi(1/2+iz),
\]

so folgte RH. Das ist die korrekte bedingte Implikation. Nicht ausreichend
sind ein paar passende Eigenwerte, die imaginären Teile bereits eingesetzter
Nullstellen, ein Eulerprodukt nur für Re(s)>1 oder eine Formaldeterminante ohne
Domäne, Spurklasse und vollständige archimedische Faktoren.

Der vorgelegte Text liefert A nicht, bestimmt keine Domäne und leitet weder
die vollständige Spurformel noch die ganze Funktionsidentität her. Die
allgemeine Selbstadjungiertheit eines anderen Operators hilft dabei nicht.

## 4. Vorarbeiten und aktuelle Grenze der Quellenprüfung

Der installierte Leitfaden `rh-graph-research` und die projektspezifische
Korpussuche wurden angewandt. Die aktuelle Konsistenzprüfung und der
anschließende Wiederaufbauversuch brachen mit

`SOURCE_UNAVAILABLE: /Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research`

ab. Die gesonderte Paper-Abfrage meldete `PAPER_SOURCE_OR_REVIEW_DRIFT`.
Keine dieser Prüfungen wurde durch Ersetzen von Pins grün gemacht. Der
Forschungsindex darf hier **nicht als global aktuell geprüft** bezeichnet
werden. Vorhandene Suchresultate dienten lediglich zum Auffinden real
verfügbarer Originaldateien; die aktuelle Queue ist keine Beweisquelle.

Gezielt gelesen wurden die relevanten Abschnitte von
`rh/catalog/analysis/geometry_audit.md` (Quantengraphen) und
`rh/catalog/analysis/event_log_function.md` (arithmetische Ereignisse), sowie
die vollständige maßgebliche Zählungs-/Determinantenpassage aus v1.6.5.
Die Dateien werden für diese Revision eingefroren. Ihre historischen
Korpus-Abwesenheitsangaben werden nicht als aktueller Vollständigkeitsbeweis
übernommen.

Im bestehenden Index berühren `r618 / STRUCTURAL_MISMATCH` die Verwechslung
RH-neutraler E8-Daten mit einer Xi-Identität und
`ledger:E8.COXETER.EULER.COMPLETION.01 / NO_BRIDGE` die fehlende globale
Vervollständigung. Solche Treffer allein widerlegen kein neues Objekt; die
hier tragende Prüfung ist der explizite Unterschied zwischen gemischten
primitiven Wegen und arithmetischen Primarten. Es wird kein neuer globaler
RH-Beweisstatus registriert oder freigegeben.

## 5. Tragfähiger Anschluss, ohne acht Versprechen an ein unbekanntes Objekt

Der nächste arithmetische Test wäre erst nach Definition einer tatsächlichen
Quell-Wegstruktur sinnvoll: primitive Bahnen, ihre Längen, Amplituden und die
Spur gemeinsam bestimmen, ohne Primlisten oder Nullstellen einzusetzen.
Ein positiver Kontrolltest muss insbesondere gemischte Zyklen erklären und
den archimedischen Anteil auf demselben Träger liefern. Gelingt nur ein
generisches Graph-Eulerprodukt, ist das ein Graphresultat und bleibt von RH
getrennt.

Faktorisierung und P versus NP werden dadurch nicht gelöst. Außerdem ist
„P≠NP bedeutet notwendigerweise exponentielle Suchkosten“ zu stark: Aus einer
fehlenden polynomialen Zeitgrenze folgt nicht allein eine exponentielle
untere Schranke. Für Hylæan enthält der Text ein mögliches Operationsbild,
aber keinen neu überprüften Lern- oder Gedächtnisnachweis.
