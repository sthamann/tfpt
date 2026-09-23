# Zertifizierter, begrenzter Regulator-Sprung

6. September 2026. Ergebnis: Eine ausführbare N-only-Route verbindet den neu zertifizierten Sammler mit dem Sprung. Für den festen Kontrollfall N=1.254.389 findet sie 1019, ohne vorgegebenen Regulator, gespeicherte Faktoren oder expandierte Pell-Einheit im Solver. Sie ist weiterhin ein begrenzter Algorithmus mit sichtbar erfolglosen Eingaben. Es ist kein Geschwindigkeitsvorteil gegenüber heutigen Faktorisierungsverfahren bewiesen.

## Was gegenüber r643 geändert wurde

Der aktuelle Repository-Quelltext `experiments/tfpt-discovery/regulator_jump_probe.py` wurde zuerst über den Graphen lokalisiert. Da dessen Snippet-Zeilen veraltet waren, wurde die tatsächliche Datei anschließend direkt gelesen. Die bestehende Rechnung benutzt `mpmath.mpf`, feste Zusatzpräzision und direkte Quotienten mit b−√D. Diese Zahlen sind keine garantierten Fehlerintervalle.

`certified_jump.py` implementiert die betreffenden ganzzahligen Formenoperationen isoliert und verwendet ausschließlich Arb für reelle Rechnungen. Die verfügbare Laufzeit ist python-flint 0.9.0. Arb liefert einschließende Ballarithmetik; für gespeicherte Grenzen werden `lower()` und `upper()` mit exakten dyadischen Mantissen/Exponenten verwendet. Es wird kein Mittelpunkt für eine Algorithmusentscheidung ausgelesen. [Arb-Dokumentation](https://python-flint.readthedocs.io/en/latest/arb.html)

Die Distanz eines Reduktionsschritts wird algebraisch identisch, aber ohne den gefährlichen Nenner berechnet:

\[
 d_b=\operatorname{sgn}(b)\left(\log(|b|+\sqrt D)-\tfrac12\log|b^2-D|\right).
\]

Für b=0 ist sie exakt null. Positive und negative b bleiben unterschieden. Die Formel wird auch an nicht reduzierten Zwischenformen verwendet. Diese Stabilisierung verhindert den Verlust des Nenners nahe b²=D. Sie beweist keine feste, für alle Eingaben ausreichende Präzision; bei großer Auslöschung müssen die Intervalle weiterhin verfeinert werden.

## Quellenvertrag und eigener Suchradius

Die zugrunde liegende Quelle ist **v2**, nicht v1. Algorithmus 2 und Bemerkung 5.4 enthalten 33/4. Bemerkung 5.5 behandelt bekannte Regulatorvielfache; eine allgemeine Garantie, dass der zentrale Koeffizient einen echten Faktor enthält, gilt dabei nicht für sämtliche zusammengesetzten N. Die Quelle benennt insbesondere anwendbare Fälle in Korollar 3.12. [Murru–Salvatori, v2](https://arxiv.org/html/2409.03486v2)

Die neue Implementierung benutzt nicht blind eine auf einen approximierten Skalar gerundete Formel für Ψ. Neben der Teilmengensumme der Potenzleiter wird die **tatsächliche, angehobene Distanz** der jeweils komponierten Form einschließlich aller Reduktionskorrekturen mitgeführt. Für den Zielwert T und die erreichte Form F ergibt Arb eine garantierte obere Grenze

\[
 E\ge |d(F)-T|.
\]

Zwei aufeinanderfolgende reduzierte Schritte überdecken mehr als log 2. Wenn der gesuchte Mittelpunkt genau bei T liegt, reichen deshalb konservativ ceil(2E/log 2)+2 Schritte in jeder Richtung. Für das ungerade Periodenziel wird vorsorglich log(D)/4 zur möglichen Distanzabweichung addiert. Der ausgeführte Radius ist

\[
 S=\left\lceil\frac{2(E+\tfrac14\log D)}{\log 2}\right\rceil+2,
\]

wobei jede reelle Rechnung nach außen gerundet wird. Seine Herleitung verwendet die Distanzaddition aus Proposition 4.15, die Zweischrittschranke aus Proposition 4.16 und den Mittelpunktsfehler aus Korollar 4.19. Die algebraische Erreichbarkeit im Hauptzyklus und diese Infrastrukturresultate sind ausdrücklich die mathematischen Voraussetzungen der Standortgarantie. Die am Ende zurückgegebene echte Teilbarkeit wird davon unabhängig exakt geprüft.

Damit lässt sich auch ein echter Vergleichsgleichstand behandeln. Wenn zwei Intervalle überlappen, wird keine Ordnung behauptet. Ein insgesamt auf höchstens 2⁻²⁰ eingeschlossener Unterschied darf als protokolliertes `certified_near_tie` behandelt werden: an der Potenzleiter wird die nahe Form übernommen, bei der Teilmengenauswahl der fragliche Summand ausgelassen. Der endgültige Abstand E wird danach aus der tatsächlich ausgeführten Rechnung berechnet und bezahlt. Der Radius enthält damit auch diese Entscheidung. Bei größerer Unentschiedenheit beginnt die ganze kurze Spur mit höherer Präzision neu; alle vorherigen Kosten bleiben erhalten. Nach dem letzten zulässigen Präzisionsniveau heißt das Ergebnis `PRECISION_UNRESOLVED`.

Der Modulcode benutzt die korrekte inverse Reduktion mit r(−b,a) und Nenner 4a; die gedruckte erste Komponente der inversen Formel in Definition 4.5 enthält uneinheitliche Variablen. Die implementierte Variante wird durch beide inversen Identitäten kontrolliert.

Eine Form auf dem Zyklus bestimmt ihre Distanz nur modulo R⁺. Die mitgeführte Zahl ist daher ein **gewählter reeller Lift**, nicht zwangsläufig die Distanz im ersten Fundamentalintervall. Unter der verwendeten primitiven Gaußkomposition ist der gemeinsame Teiler im führenden Koeffizienten eine rationale Normalisierung des Idealprodukts. Er verändert log|α|−½log|Norm(α)| nicht. Die anschließend explizit ausgeführten Reduktionen liefern die gesamte Zusatzdistanz. Ein weiterer numerisch ignorierter Kompositionsdefekt wird nicht eingeführt; die möglichen ganzzahligen R⁺-Windungen sind Teil des Lifts. Das ist die konkrete Anwendung von Proposition 4.15, keine aus den kleinen Tests neu bewiesene allgemeine Aussage.

`distance_audit.py` kontrolliert diese Stelle zusätzlich unabhängig und exakt: Die vollständigen Hauptzyklen für N=21,77,221,731 entstehen durch die P/Q-Kettenbruchrekursion, ohne den getesteten Reduktionsoperator. Für **alle 112 Formpaare** wird die exponentierte Distanz in Q(√N) berechnet. Ein Reduktionsschritt multipliziert exp(2d) exakt mit (b²+4N+4b√N)/|b²−4N|. Das Produkt aus beiden Eingangsdistanzen und sämtlichen Reduktionsfaktoren stimmt exakt mit der Referenzdistanz der Zielform mal einer ganzzahligen Potenz von exp(2R⁺) überein. Die Windung wird zunächst durch ein Intervall eingegrenzt und anschließend durch Gleichheit rationaler Koeffizienten geprüft. Bloße Nähe zu einer ganzen Zahl würde diesen Test nicht bestehen.

## Regulatorvielfachheit ohne externen Regulator

`n_only_adapter.py` ruft zunächst `collect_first_unit(N,B,X)` aus dem neuen Nachbarmodul `regulator/certified_regulator.py` auf. Bei Erfolg wird dessen unverändertes Zertifikat durch `CertifiedRegulatorLog` erneut exakt geprüft. Erst danach geht `.evaluate_lambda(bits)` an den Sprung. Der Provider erzeugt bei jeder Präzision ein Intervall um denselben positiven Einheitenlogarithmus.

Der relevante Regulator ist R⁺ der konkreten Ordnung **Z[√N]**. Das zertifizierte Produkt ist eine total positive Norm-1-Einheit dieser Ordnung. Daher ist λ=kR⁺ mit positivem ganzzahligem k. Eine zusätzliche Verdopplung ist hier unnötig. Die Umrechnung zum Regulator des maximalen Ganzheitsrings wird nicht benutzt. Ebenso wenig wird ein reeller ggT mehrerer approximierter Logarithmen benutzt.

Ohne k zu kennen, liefert R⁺>log 2 die konservative Abschätzung k<λ/log 2. Die Zahl benötigter dyadischer Ziele lässt sich daher durch ceil(log₂(λ/log 2))+2 nach oben begrenzen. Ist das konfigurierte Halbierungsbudget kleiner, wird dies als `BUDGET_EXHAUSTED` ausgegeben. Dass diese Grenze logarithmisch in λ ist, ist kein Beweis einer guten Bitkomplexität in log N: Größe und Erzeugungskosten des ersten brauchbaren λ müssen vollständig gezählt werden.

Der Kern `split(N, callback)` allein hat einen expliziten Providervertrag. Er kann die Herkunft eines beliebigen fremden Callbacks nicht beweisen. Der vollständige Adapter schließt diese Lücke durch den exakten Zertifikatsprüfer. Nichts wird allein deshalb zum zertifizierten Regulatorvielfachen, weil es als Arb-Ball übergeben wird.

Die Präzisionsgrenzen sind getrennt: Einheitenzertifizierung und erneute Providerkonstruktion beginnen bei 64 Bit und dürfen bis 4096 Bit gehen; nur die nachfolgenden Sprungversuche sind auf 64,128,256,512,1024 Bit beschränkt. Die Eingangsvalidierung wird dadurch nicht stillschweigend als Teil einer globalen 1024-Bit-Grenze dargestellt.

## Feste Kontrollen und Integrationsabnahme

Der Plan wurde vor Ausführung als `plan.json` gespeichert. Die kleine Kontrollsammlung verwendet N=21,77,221,731,1048189 und Vielfache 1,2,16. Diese Zahlen sind algebraische Kontrollen, keine neue zufällige Semiprim-Benchmarkkohorte. Die benötigten Einheiten werden **nur im getrennten Testprogramm** langsam über Kettenbrüche konstruiert; dieser Aufwand ist protokolliert und gehört nicht zur N-only-Leistungsbehauptung.

Die 15 Kontrollen liefern neun exakte Faktoren und sechs begrenzte Nichterfolge. Der Fall N=731 bleibt auch mit bekanntem korrektem Einheitenlogarithmus ohne Faktor in diesem Koeffizientenleser. Seine kleine Hauptperiode enthält nur die Formen (1,54,−2) und (−2,54,1); alle Koeffizienten haben ggT 1 mit 731. Dies ist ein exakter Gegenbeleg gegen eine universelle Faktorgarantie dieses Lesers auf unverändertem N, keine Untergrenze für andere Faktorisierungsverfahren.

176 fest gewählte kleine Formkompositionen bestehen den Vergleich mit dem kleinen Auditzyklus, einschließlich der Distanzlage modulo dem separat bekannten Einheitenlogarithmus. Das ist eine endliche Kontrolle der Umsetzung und kein Ersatz für den allgemeinen Infrastrukturbeweis. Zusätzlich bestehen Nullintervall-, dauerhaft breites Intervall-, Operationsbudget-, falsche Diskriminanten- und echte Überlappungskontrollen. Bei b=2^j+1 und D=b²−1 für j=32,128,512 ist die alte direkte Quotientenformel bereits bei 64 Bit nicht endlich einschließbar; die stabile Formel bleibt endlich und überlappt die jeweils separat stark verfeinerte Referenz.

Die drei bereits erzeugten N-only-Sammlerkontrollen wurden ohne neue Sammlung integriert:

| N | Ergebnis der vollständigen Zertifikats-/Sprungroute |
|---:|---|
| 31.613 | Sammlerbudget erreicht, kein Einheitenzertifikat und kein Sprung |
| 10.403 | Faktor 101; Norm-1-Direktrelation und kleiner Scan |
| 1.254.389 | Faktor 1019; tatsächlich sieben Kompositionen im Sprung |

Der finale Replay bezieht sich auf `regulator/fixed_controls.json` und den eingefrorenen Sammlerhash `7ed4e1a079f5c914d4fc833c0e81dbeb1344154f47b471045086dc583e626896`. Im separaten Gleichrelationsvergleich des Sammlers liefern dieselben 16 Normrelationen für N=1.254.389 auch klassisch über GF(2) einen Faktor. Der Erfolg ist somit kein Beleg, dass gerade der Umweg über einen Regulator mehr Faktorisierungsinformation gewinnt.

Für N=1.254.389 wurde anschließend die **gesamte** Route erneut von N,B=100,X=25.000 aus ausgeführt (`end_to_end_control.json`). Der Sammler findet 16 Relationen; drei Abhängigkeiten sind exakt null, die vierte liefert den positiven Logarithmus ungefähr 1037,5904. Der Sprung erreicht zunächst die Form (319,1896,−1115). Der nach außen berechnete Suchradius ist 81; nach 19 Vorwärtsschritten wird (−212,2038,1019) erreicht und ggT(1019,N)=1019 liefert den Faktor. Zur Laufroute gehören sieben Kompositionen, 14 erweiterte ggT-Aufrufe, 72 Vorwärts- und 19 Rückwärtsschritte. Die gespeicherte Wandzeit dieses kleinen Gesamtlaufs beträgt ungefähr 0,003 Sekunden und ist laufabhängig. Sie begründet keinen Vergleichsvorteil.

## Frischer Pilot ohne Faktorwissen

Nach dem Distanz-Audit wurde `cohort_plan.json` **vor Erzeugung der Eingaben** gespeichert: Seed 202609063212, je drei ausgeglichene Semiprimzahlen mit tatsächlich 20,24,28 Bit; Schranken B=100,200,400 und X=25.000,50.000,100.000. Die vorhandenen Sprunggrenzen blieben unverändert. Jede Methode erhielt dieselben öffentlichen Eingaben, ein gleiches äußeres Zeitlimit von zehn Sekunden und einen frischen Unterprozess. Die bei der Erzeugung bekannten Faktoren liegen getrennt und wurden keinem Worker übergeben.

| Verfahren | Faktoren | Summe vollständige Algorithmuszeit | Summe Unterprozesszeit einschließlich Imports |
|---|---:|---:|---:|
| Zertifizierter Sammler → Einheitenlog → Sprung | 3/9 | 0,07764 s | 0,90639 s |
| Repository-SQUFOF ohne Rho-Fallback | 9/9 | 0,000848 s | 0,47599 s |
| Repository-Rho | 9/9 | 0,000670 s | 0,47575 s |

Es gab eine Wiederholung pro Eingabe und Methode; die Zeiten sind weder Mediane noch Skalierungsexponenten. Alle neun neuen Eingaben lieferten ein korrektes nichttriviales Einheitenzertifikat, aber der Sprungleser fand nur drei Faktoren. Die sechs übrigen Ergebnisse lauten `NO_FACTOR_IN_BOUNDED_READER`, nicht Timeout oder verdeckter Fallback. Das kleine Ergebnis spricht klar gegen einen bislang beobachteten Performancevorteil dieser Route.

`cohort_verify.py` liest keine bekannte Faktorzerlegung. Er prüft alle neun Einheitenzertifikate erneut, bindet die verwendeten Arb-Eingangsintervalle an den Provider, kontrolliert die Grenzen und prüft die drei neuen Form-/Faktorzertifikate direkt. Die 18 klassischen Vergleichsfaktoren werden als echte Teiler überprüft. Alle Prüfungen bestehen. Eine unabhängige vollständige Wiederholung des Hauptagenten kann die Ausführung zusätzlich reproduzieren; die Zertifikatsprüfung allein beweist keine Benchmarkzeit.

## Nutzung, Kosten und Grenzen

Abhängigkeiten: Python 3.10+ und python-flint; für den vollständigen Adapter zusätzlich das benachbarte, eingefrorene `regulator/certified_regulator.py`. Keine Repository-Imports oder NumPy/mpmath-Abhängigkeit. Beispiel vom Verzeichnis `regulator_jump` aus:

```sh
python n_only_adapter.py --n 1254389 --bound 100 --x-limit 25000 --output result.json
python test_jump.py
python distance_audit.py
python integration_check.py
python cohort_verify.py
```

Die Ergebnisschemata enthalten `status`, `factor`, das exakte Form-/ggT-Zertifikat, Grenzen, alle Präzisionsversuche, die eingeschlossenen Vergleichsdifferenzen, Ziel-/Distanz-/Fehlerintervalle, Suchradien, Operationszähler und Quellhashes. Im Adapter bleiben Sammlerkosten, erneute Zertifikatsprüfung, Callback-Auswertungen und Sprungkosten erhalten; `factor_from_n` misst außerdem den kompletten Gesamtlauf. Die `operations` sind ein instrumentierter Zähler benannter Vorgänge, keine vollständigen Bitkosten. Byte- und Bitgrößenbegrenzungen stehen gesondert im Protokoll.

Das Operationsbudget wird vor dem jeweiligen Vorgang geprüft. Auch ein gescheiterter Versuch hat deshalb `operations <= max_operations`; ein Vorgang nach ausgeschöpftem Budget wird nicht als ausgeführt gezählt. Eine zusätzliche Kontrolle demonstriert erfolgreiches Verfeinern eines korrekten, anfangs nullhaltigen Logintervalls: der erste Versuch wird als unentschieden verworfen, der zweite liefert einen exakt geprüften Faktor und beide Callback-Auswertungen bleiben im Kostenprotokoll.

Erfolglosigkeit lautet `COLLECTOR_SEARCH_LIMIT`, `PRECISION_UNRESOLVED`, `BUDGET_EXHAUSTED` oder `NO_FACTOR_IN_BOUNDED_READER`. Der letzte Status besagt nicht, dass N prim ist. Ein vollständig abgelaufener kleiner Hauptzyklus beweist nur das Fehlen eines Faktors in dessen drei Koeffizientenauslesern. Es gibt keinen automatischen Fallback, keine universelle Faktorisierungsgarantie und keine Verbindung dieser Kontrollen zu einem RH-Beweis.
