# Nichtlineare Ziffernbeziehungen und getrennte Modellauswahl

Stand: 8. September 2026. Ausgeführte Fortsetzung der π-/Primzahl-Untersuchung.

**Ergebnis:** Keine der 28 Ziffernpaar- und sechs Dreierfolgen-Korrekturen aus π verbessert die arithmetische Vorhersage im separaten Auswahlbereich. Die festgelegte Auswahlregel bleibt deshalb bei der Vorhersage ohne Ziffernkorrektur. Das gilt auch nach einer separat dokumentierten Gegenprüfung einer gefundenen Extrapolationsschwäche des Basismodells. Ein starkes, ausschließlich gemeinsam kodiertes Kontrollsignal wird dagegen erkannt.

## Neue Daten und neue Hypothese

Eine Beziehung zwischen zwei Ziffern kann unsichtbar bleiben, wenn man jede Ziffer nur einzeln betrachtet. Deshalb werden die gemeinsamen Ziffernwerte als Kategorien gelernt: 100 mögliche Werte je Paar und 1.000 je Dreierfolge. Das ergänzt die vorherigen linearen Modelle um eine klar begrenzte nichtlineare Suchfamilie.

π, e und √2 wurden auf jeweils 13.200.032 Nachkommastellen erweitert. Alle tatsächlich gelesenen Stellen liegen jenseits des vorherigen 10,4-Millionen-Präfixes. Drei getrennte Bereiche verhindern, dass die abschließenden Prüfwerte die Modellwahl bestimmen:

| Bereich | Primzahlpositionen | Anzahl | Zweck |
|---|---|---:|---|
| Lernen | 11.000.001–11.200.000 | 12,356 | Basismodell und Korrekturtabellen lernen |
| Auswahl | 12.000.001–12.200.000 | 12,225 | Beste vorher festgelegte Kombination wählen |
| Abschließende Prüfung | 13.000.001–13.200.000 | 12,149 | Gewähltes Modell einmal bewerten |

Ziel bleibt log((nächste Primzahl−p)/log(p)). Die arithmetische Ridge-Vorhersage nutzt vorherige Lücken, Restklassen und im ursprünglichen Lauf log(p). Korrekturtabellen lernen ausschließlich die Fehler im Lernbereich; für eine Kategorie c lautet die Korrektur Summe der Lernfehler/(Anzahl+50). Die Glättung 50 ist fest. Nach der Auswahl wird nichts neu angepasst.

Aus den acht Ziffern an Positionen p bis p+7 werden alle 28 Paare und sechs zusammenhängenden Dreierfolgen geprüft. Eine zusätzliche Option erlaubt ausdrücklich, keine Ziffernkorrektur zu verwenden. Ein zweiter Auswahlprozess über acht einzelne Ziffern und dieselbe Nulloption dient als Kontrolle.

## Unveränderter primärer Lauf

| Quelle | Gewählte Einzelziffer | Gewählte nichtlineare Korrektur | Fehlerreduktion nichtlinear gegen Arithmetik im Abschlusstest |
|---|---|---|---:|
| π | p+7 | keine Korrektur | +0.0000 % |
| e | p+7 | keine Korrektur | +0.0000 % |
| √2 | keine Korrektur | keine Korrektur | +0.0000 % |
| Eingebautes gemeinsames Signal | keine Korrektur | p, p+1 | +51.5145 % |

Die 0 % bei π bedeuten, dass die vorher festgelegte Auswahlregel bereits im Auswahlbereich keine nützliche nichtlineare Korrektur fand. Es wurde keine Kombination aufgrund ihrer Leistung im Abschlusstest nachträglich bevorzugt. Auch die beste von Null verschiedene π-Korrektur war im Auswahlbereich schlechter als das Basismodell. Die einzeln ausgewählte Ziffer p+7 verschlechtert den Prüfungsfehler geringfügig; die kleine Differenz zu dieser Kontrolle ist kein π-Signal.

999 vollständige, unabhängige Zufallsströme durchlaufen jeweils sämtliche Lern- und Auswahlentscheidungen. Für die beiden vorab definierten Vergleiche ergeben sich:

| Primärer π-Vergleich | Fehlerreduktion im Abschlusstest | p, unkorrigiert | p, Holm-korrigiert |
|---|---:|---:|---:|
| Nichtlinear gegen Arithmetik | +0.0000 % | 0.982 | 0.982 |
| Nichtlinear gegen ausgewählte Einzelziffer | +0.0138 % | 0.405 | 0.810 |

In 981 von 999 Null-Läufen wird ebenfalls keine nichtlineare Korrektur gewählt. Entsprechend hat die Nullverteilung eine große Punktmasse bei exakt null; einschließlich Gleichständen berechnete Monte-Carlo-Ränge berücksichtigen das. Ein Nullwert ist hier weder ein Rundungsfehler noch eine Schätzung vollständiger statistischer Unabhängigkeit.

Das Kandidatenkriterium verlangt mindestens 1 % Fehlerreduktion gegen Arithmetik, beide korrigierten p-Werte unter 0,05 und Verbesserungen gegen beide Kontrollen in beiden Prüfhälften. π erfüllt dieses Kriterium nicht. Die Korrektur betrifft diese zwei Tests, nicht alle denkbaren oder künftig ausprobierten Suchfamilien.

## Gemeinsames Signal als Positivkontrolle

In einen separaten Zufallsstrom wird künstlich eingebaut: (Ziffer an p + Ziffer an p+1) mod 10 ist 2 bei kleinen und 7 bei großen folgenden Lücken. Die Klassengrenze stammt aus den Lernzielen. Beide Einzelziffern bleiben unter dieser Zufallskonstruktion marginal gleichverteilt; gemeinsam kodieren sie die Klasse. Die Zielinformation wird hier bewusst auch in Auswahl- und Prüfdaten geschrieben und ist ausschließlich ein Sensitivitätstest.

Die Auswahl findet das Paar p,p+1. Der Fehler im Abschlusstest sinkt um 51.51 %, mit korrigiertem p=0,002 für beide Vergleiche. Die Einzelziffernkontrolle wählt keine Korrektur. Das zeigt die Erkennung dieses starken gemeinsamen Signals, aber keine allgemeine Teststärke für beliebig schwache, längere oder anders strukturierte Beziehungen.

## Gefundene Schwäche des arithmetischen Vergleichs

Die Qualitätsprüfung fand eine reale Modellschwäche: Das arithmetische Basismodell ist im Abschlusstest schlechter als die konstante Vorhersage des Lernmittelwerts. Der Grund lässt sich auf einen Term zurückführen.

Der lokal gelernte log(p)-Koeffizient beträgt -0.010297. Im Abschlusstest liegt dieses Merkmal 30,4 bis 33,3 Lern-Standardabweichungen über dem Lernmittel. Dadurch verschiebt dieser einzelne Term die mittlere Vorhersage um -0.32835, obwohl sich das Zielmittel nur um +0.00940 verschiebt. Die starke Extrapolation eines kleinen lokalen Trends erzeugt den Fehler.

Das Entfernen allein dieses Beitrags bei ansonsten unverändertem Modell bestätigt die Ursache. Anschließend wurde als **nachträgliche Sensitivitätsprüfung** das Basismodell ohne das rohe log(p)-Merkmal neu auf dem Lernbereich angepasst. Zielnormierung, vorherige Lücken, Restklassen, Glättung, Ziffernkombinationen, Auswahlregel und die 999 Kontrollströme blieben gleich.

| Arithmetische Vorhersage | Abschlusstest-MSE |
|---|---:|
| Konstanter Lernmittelwert | 0.756319 |
| Ursprüngliche feste Arithmetik | 0.836410 |
| Ohne extrapoliertes log(p)-Merkmal, neu gelernt | 0.721815 |

Die geänderte Arithmetik verbessert den Fehler gegenüber der konstanten Vorhersage um 4.56 %. Trotzdem wählt die nichtlineare Suche auch jetzt für π, e und √2 jeweils keine Korrektur. Das eingebaute Paar-Signal bleibt erkennbar (63.14 % Fehlerreduktion, diagnostisch korrigiertes p=0,002).

Diese Sensitivitätsprüfung ist **keine unabhängige Replikation und kein neuer vorab festgelegter Signifikanztest**: Der Anlass zur Änderung stammt aus dem ursprünglichen Ergebnis. Die primären Daten, Protokolle und Resultate wurden nicht ersetzt. Ihre Einschränkung und die separate Gegenprüfung bleiben sichtbar. Die Sensitivitäts-p-Werte kalibrieren nur den festen geänderten Ablauf, nicht die nachträgliche Entscheidung, ihn zu untersuchen.

## Audit, Kosten und Reichweite

- Primärer Lauf und Sensitivitätslauf bestehen jeweils den Audit: 106 Primzahl-/Lückenpositionen mit SymPy geprüft, 8 gewählte Korrekturtabellen durch direkte Zählung nachgerechnet und 60 Metriken aus den Einzelvorhersagen rekonstruiert.
- Veränderungen ausschließlich der Abschlusstest-Zielwerte verändern weder die gewählten Kombinationen noch deren gelernte Tabellen. Der erste vollständige Null-Lauf wurde jeweils reproduziert.
- Fünf Testgruppen prüfen Suchfamilie, Kodierung und direkte Tabellensummen, ein exakt balanciertes Signal mit unauffälligen Einzelziffern, Gleichstandsregeln und die Schnittstelle ohne Abschlusstest-Zielwerte.
- Die neuen Präfixe stimmen bis 10,4 Millionen Stellen mit den vorherigen, hashgeprüften Dateien überein. π wurde mit höherer Genauigkeit wiederholt. Für das neue Suffix ist dies eine Präzisionskontrolle, keine unabhängige Berechnungsmethode.
- Hauptauswertung einschließlich 999 Null-Läufen: 22.135 s; Sensitivitätsauswertung: 22.121 s. Datenerzeugung und separater Audit kommen hinzu. π/e/√2-Erzeugung: pi 11.285 s, e 5.593 s, sqrt2 2.658 s; π-Wiederholung 10.886 s.
- Es wurden ausschließlich die festgelegten lokalen Ziffernpaare und Dreierfolgen untersucht. Der Befund ist kein Ausschluss aller nichtlinearen Beziehungen, kein Normalitäts- oder RH-Beweis und keine Faktorisierungsbeschleunigung.

Diese Stufe liefert eine überprüfte Suche, die bei fehlendem Zusatznutzen tatsächlich auf eine Ziffernkorrektur verzichtet, und eine konkret diagnostizierte Grenze der früheren Vergleichsarchitektur. Ein weiterer Erkenntnisanspruch benötigt eine andere begründete Hypothese und wieder frische Prüfbereiche.

## Reproduktion und Artefakte

```sh
cd experiments/pi-prime-event-log-2026-09-08/nonlinear-gate
PYTHONPATH=/tmp/tfpt-pi-event-deps python3 prepare_data.py
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -m unittest -v test_nonlinear.py
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 nonlinear.py
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 audit.py
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 diagnose_baseline.py
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 sensitivity.py
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 audit.py --sensitivity
python3 write_report.py
```

gmpy2 befindet sich in dieser Sitzung unter `/tmp/tfpt-pi-event-deps`; alternativ in der eigenen Umgebung installieren. Vorhandene geprüfte Zifferndateien erlauben das Überspringen ihrer Erzeugung. Neue Läufe überschreiben nur die jeweiligen Ergebnisdateien dieses Unterordners.

[Primäres Protokoll](PROTOCOL.md) · [Primäre Ergebnisse](summary.json) · [Audit](audit.json) · [Alle beobachteten Auswahlwerte](selection_catalog.csv) · [Einzelvorhersagen](predictions.npz) · [Null-Läufe](null_runs.jsonl)

[Nachträgliches Sensitivitätsprotokoll](SENSITIVITY_PROTOCOL.md) · [Ursachendiagnose](baseline_diagnostic.json) · [Sensitivitätsergebnisse](sensitivity_summary.json) · [Sensitivitätsaudit](sensitivity_audit.json)
