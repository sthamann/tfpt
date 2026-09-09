import csv,json
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent
s=json.loads((R/'summary.json').read_text());sensitivity=json.loads((R/'sensitivity_summary.json').read_text())
a=json.loads((R/'audit.json').read_text());m=json.loads((R/'data_manifest.json').read_text())
diagnostic=json.loads((R/'baseline_diagnostic.json').read_text())
null=[json.loads(x) for x in (R/'null_runs.jsonl').read_text().splitlines()]

def label(offsets):return 'keine Korrektur' if not offsets else ', '.join('p' if i==0 else f'p+{i}' for i in offsets)

lines=['# Nichtlineare Ziffernbeziehungen und getrennte Modellauswahl','',
'Stand: 8. September 2026. Ausgeführte Fortsetzung der π-/Primzahl-Untersuchung.','',
'**Ergebnis:** Keine der 28 Ziffernpaar- und sechs Dreierfolgen-Korrekturen aus π verbessert die arithmetische Vorhersage im separaten Auswahlbereich. Die festgelegte Auswahlregel bleibt deshalb bei der Vorhersage ohne Ziffernkorrektur. Das gilt auch nach einer separat dokumentierten Gegenprüfung einer gefundenen Extrapolationsschwäche des Basismodells. Ein starkes, ausschließlich gemeinsam kodiertes Kontrollsignal wird dagegen erkannt.','',
'## Neue Daten und neue Hypothese','',
'Eine Beziehung zwischen zwei Ziffern kann unsichtbar bleiben, wenn man jede Ziffer nur einzeln betrachtet. Deshalb werden die gemeinsamen Ziffernwerte als Kategorien gelernt: 100 mögliche Werte je Paar und 1.000 je Dreierfolge. Das ergänzt die vorherigen linearen Modelle um eine klar begrenzte nichtlineare Suchfamilie.','',
'π, e und √2 wurden auf jeweils 13.200.032 Nachkommastellen erweitert. Alle tatsächlich gelesenen Stellen liegen jenseits des vorherigen 10,4-Millionen-Präfixes. Drei getrennte Bereiche verhindern, dass die abschließenden Prüfwerte die Modellwahl bestimmen:','',
'| Bereich | Primzahlpositionen | Anzahl | Zweck |','|---|---|---:|---|',
f'| Lernen | 11.000.001–11.200.000 | {s["phase_counts"]["train"]:,} | Basismodell und Korrekturtabellen lernen |',
f'| Auswahl | 12.000.001–12.200.000 | {s["phase_counts"]["selection"]:,} | Beste vorher festgelegte Kombination wählen |',
f'| Abschließende Prüfung | 13.000.001–13.200.000 | {s["phase_counts"]["test"]:,} | Gewähltes Modell einmal bewerten |','',
'Ziel bleibt log((nächste Primzahl−p)/log(p)). Die arithmetische Ridge-Vorhersage nutzt vorherige Lücken, Restklassen und im ursprünglichen Lauf log(p). Korrekturtabellen lernen ausschließlich die Fehler im Lernbereich; für eine Kategorie c lautet die Korrektur Summe der Lernfehler/(Anzahl+50). Die Glättung 50 ist fest. Nach der Auswahl wird nichts neu angepasst.','',
'Aus den acht Ziffern an Positionen p bis p+7 werden alle 28 Paare und sechs zusammenhängenden Dreierfolgen geprüft. Eine zusätzliche Option erlaubt ausdrücklich, keine Ziffernkorrektur zu verwenden. Ein zweiter Auswahlprozess über acht einzelne Ziffern und dieselbe Nulloption dient als Kontrolle.','',
'## Unveränderter primärer Lauf','',
'| Quelle | Gewählte Einzelziffer | Gewählte nichtlineare Korrektur | Fehlerreduktion nichtlinear gegen Arithmetik im Abschlusstest |',
'|---|---|---|---:|']
for kind in ['pi','e','sqrt2','planted']:
    ob=s['observed'][kind];name={'pi':'π','e':'e','sqrt2':'√2','planted':'Eingebautes gemeinsames Signal'}[kind]
    lines.append(f'| {name} | {label(ob["chosen"]["single"])} | {label(ob["chosen"]["nonlinear"])} | {100*ob["phases"]["test"]["nonlinear_vs_arithmetic"]["reduction"]:+.4f} % |')
lines+=['',
'Die 0 % bei π bedeuten, dass die vorher festgelegte Auswahlregel bereits im Auswahlbereich keine nützliche nichtlineare Korrektur fand. Es wurde keine Kombination aufgrund ihrer Leistung im Abschlusstest nachträglich bevorzugt. Auch die beste von Null verschiedene π-Korrektur war im Auswahlbereich schlechter als das Basismodell. Die einzeln ausgewählte Ziffer p+7 verschlechtert den Prüfungsfehler geringfügig; die kleine Differenz zu dieser Kontrolle ist kein π-Signal.','',
'999 vollständige, unabhängige Zufallsströme durchlaufen jeweils sämtliche Lern- und Auswahlentscheidungen. Für die beiden vorab definierten Vergleiche ergeben sich:','',
'| Primärer π-Vergleich | Fehlerreduktion im Abschlusstest | p, unkorrigiert | p, Holm-korrigiert |',
'|---|---:|---:|---:|']
for comp,title in [('nonlinear_vs_arithmetic','Nichtlinear gegen Arithmetik'),('nonlinear_vs_single','Nichtlinear gegen ausgewählte Einzelziffer')]:
    ob=s['observed']['pi']['phases']['test'][comp];c=s['pi_calibration'][comp]
    lines.append(f'| {title} | {100*ob["reduction"]:+.4f} % | {c["raw_p"]:.3f} | {c["holm_p"]:.3f} |')
none=sum(not row['chosen']['nonlinear'] for row in null)
lines+=['',f'In {none} von 999 Null-Läufen wird ebenfalls keine nichtlineare Korrektur gewählt. Entsprechend hat die Nullverteilung eine große Punktmasse bei exakt null; einschließlich Gleichständen berechnete Monte-Carlo-Ränge berücksichtigen das. Ein Nullwert ist hier weder ein Rundungsfehler noch eine Schätzung vollständiger statistischer Unabhängigkeit.','',
'Das Kandidatenkriterium verlangt mindestens 1 % Fehlerreduktion gegen Arithmetik, beide korrigierten p-Werte unter 0,05 und Verbesserungen gegen beide Kontrollen in beiden Prüfhälften. π erfüllt dieses Kriterium nicht. Die Korrektur betrifft diese zwei Tests, nicht alle denkbaren oder künftig ausprobierten Suchfamilien.','',
'## Gemeinsames Signal als Positivkontrolle','',
'In einen separaten Zufallsstrom wird künstlich eingebaut: (Ziffer an p + Ziffer an p+1) mod 10 ist 2 bei kleinen und 7 bei großen folgenden Lücken. Die Klassengrenze stammt aus den Lernzielen. Beide Einzelziffern bleiben unter dieser Zufallskonstruktion marginal gleichverteilt; gemeinsam kodieren sie die Klasse. Die Zielinformation wird hier bewusst auch in Auswahl- und Prüfdaten geschrieben und ist ausschließlich ein Sensitivitätstest.','',
f'Die Auswahl findet das Paar p,p+1. Der Fehler im Abschlusstest sinkt um {100*s["observed"]["planted"]["phases"]["test"]["nonlinear_vs_arithmetic"]["reduction"]:.2f} %, mit korrigiertem p=0,002 für beide Vergleiche. Die Einzelziffernkontrolle wählt keine Korrektur. Das zeigt die Erkennung dieses starken gemeinsamen Signals, aber keine allgemeine Teststärke für beliebig schwache, längere oder anders strukturierte Beziehungen.','',
'## Gefundene Schwäche des arithmetischen Vergleichs','',
'Die Qualitätsprüfung fand eine reale Modellschwäche: Das arithmetische Basismodell ist im Abschlusstest schlechter als die konstante Vorhersage des Lernmittelwerts. Der Grund lässt sich auf einen Term zurückführen.','',
f'Der lokal gelernte log(p)-Koeffizient beträgt {diagnostic["logp_coefficient"]:.6f}. Im Abschlusstest liegt dieses Merkmal 30,4 bis 33,3 Lern-Standardabweichungen über dem Lernmittel. Dadurch verschiebt dieser einzelne Term die mittlere Vorhersage um {diagnostic["test"]["mean_logp_contribution"]:.5f}, obwohl sich das Zielmittel nur um {diagnostic["test"]["target_mean"]-diagnostic["train"]["target_mean"]:+.5f} verschiebt. Die starke Extrapolation eines kleinen lokalen Trends erzeugt den Fehler.','',
'Das Entfernen allein dieses Beitrags bei ansonsten unverändertem Modell bestätigt die Ursache. Anschließend wurde als **nachträgliche Sensitivitätsprüfung** das Basismodell ohne das rohe log(p)-Merkmal neu auf dem Lernbereich angepasst. Zielnormierung, vorherige Lücken, Restklassen, Glättung, Ziffernkombinationen, Auswahlregel und die 999 Kontrollströme blieben gleich.','',
'| Arithmetische Vorhersage | Abschlusstest-MSE |','|---|---:|',
f'| Konstanter Lernmittelwert | {s["training_mean_test_mse"]:.6f} |',
f'| Ursprüngliche feste Arithmetik | {s["baseline_test_mse"]:.6f} |',
f'| Ohne extrapoliertes log(p)-Merkmal, neu gelernt | {sensitivity["baseline_test_mse"]:.6f} |','',
f'Die geänderte Arithmetik verbessert den Fehler gegenüber der konstanten Vorhersage um {100*(1-sensitivity["baseline_test_mse"]/sensitivity["training_mean_test_mse"]):.2f} %. Trotzdem wählt die nichtlineare Suche auch jetzt für π, e und √2 jeweils keine Korrektur. Das eingebaute Paar-Signal bleibt erkennbar ({100*sensitivity["observed"]["planted"]["phases"]["test"]["nonlinear_vs_arithmetic"]["reduction"]:.2f} % Fehlerreduktion, diagnostisch korrigiertes p=0,002).','',
'Diese Sensitivitätsprüfung ist **keine unabhängige Replikation und kein neuer vorab festgelegter Signifikanztest**: Der Anlass zur Änderung stammt aus dem ursprünglichen Ergebnis. Die primären Daten, Protokolle und Resultate wurden nicht ersetzt. Ihre Einschränkung und die separate Gegenprüfung bleiben sichtbar. Die Sensitivitäts-p-Werte kalibrieren nur den festen geänderten Ablauf, nicht die nachträgliche Entscheidung, ihn zu untersuchen.','',
'## Audit, Kosten und Reichweite','',
f'- Primärer Lauf und Sensitivitätslauf bestehen jeweils den Audit: {a["prime_gap_rows"]} Primzahl-/Lückenpositionen mit SymPy geprüft, {a["winner_tables_audited"]} gewählte Korrekturtabellen durch direkte Zählung nachgerechnet und {a["metrics_checked"]} Metriken aus den Einzelvorhersagen rekonstruiert.',
'- Veränderungen ausschließlich der Abschlusstest-Zielwerte verändern weder die gewählten Kombinationen noch deren gelernte Tabellen. Der erste vollständige Null-Lauf wurde jeweils reproduziert.',
'- Fünf Testgruppen prüfen Suchfamilie, Kodierung und direkte Tabellensummen, ein exakt balanciertes Signal mit unauffälligen Einzelziffern, Gleichstandsregeln und die Schnittstelle ohne Abschlusstest-Zielwerte.',
'- Die neuen Präfixe stimmen bis 10,4 Millionen Stellen mit den vorherigen, hashgeprüften Dateien überein. π wurde mit höherer Genauigkeit wiederholt. Für das neue Suffix ist dies eine Präzisionskontrolle, keine unabhängige Berechnungsmethode.',
f'- Hauptauswertung einschließlich 999 Null-Läufen: {s["analysis_seconds"]:.3f} s; Sensitivitätsauswertung: {sensitivity["analysis_seconds"]:.3f} s. Datenerzeugung und separater Audit kommen hinzu. π/e/√2-Erzeugung: '+', '.join(f'{kind} {m[kind]["generation_seconds"]:.3f} s' for kind in ['pi','e','sqrt2'])+f'; π-Wiederholung {m["repeat_seconds"]:.3f} s.',
'- Es wurden ausschließlich die festgelegten lokalen Ziffernpaare und Dreierfolgen untersucht. Der Befund ist kein Ausschluss aller nichtlinearen Beziehungen, kein Normalitäts- oder RH-Beweis und keine Faktorisierungsbeschleunigung.','',
'Diese Stufe liefert eine überprüfte Suche, die bei fehlendem Zusatznutzen tatsächlich auf eine Ziffernkorrektur verzichtet, und eine konkret diagnostizierte Grenze der früheren Vergleichsarchitektur. Ein weiterer Erkenntnisanspruch benötigt eine andere begründete Hypothese und wieder frische Prüfbereiche.','',
'## Reproduktion und Artefakte','',
'```sh','cd experiments/pi-prime-event-log-2026-09-08/nonlinear-gate',
'PYTHONPATH=/tmp/tfpt-pi-event-deps python3 prepare_data.py',
'OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -m unittest -v test_nonlinear.py',
'OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 nonlinear.py',
'OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 audit.py',
'OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 diagnose_baseline.py',
'OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 sensitivity.py',
'OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 audit.py --sensitivity',
'python3 write_report.py','```','',
'gmpy2 befindet sich in dieser Sitzung unter `/tmp/tfpt-pi-event-deps`; alternativ in der eigenen Umgebung installieren. Vorhandene geprüfte Zifferndateien erlauben das Überspringen ihrer Erzeugung. Neue Läufe überschreiben nur die jeweiligen Ergebnisdateien dieses Unterordners.','',
'[Primäres Protokoll](PROTOCOL.md) · [Primäre Ergebnisse](summary.json) · [Audit](audit.json) · [Alle beobachteten Auswahlwerte](selection_catalog.csv) · [Einzelvorhersagen](predictions.npz) · [Null-Läufe](null_runs.jsonl)','',
'[Nachträgliches Sensitivitätsprotokoll](SENSITIVITY_PROTOCOL.md) · [Ursachendiagnose](baseline_diagnostic.json) · [Sensitivitätsergebnisse](sensitivity_summary.json) · [Sensitivitätsaudit](sensitivity_audit.json)','']
(R/'README.md').write_text('\n'.join(lines))
with (R/'selection_catalog.csv').open('w',newline='') as f:
    writer=csv.writer(f);writer.writerow(['run','source','family','offsets_from_p','selection_mse','selected'])
    for run,summary in [('primary',s),('post_outcome_sensitivity',sensitivity)]:
        for kind,ob in summary['observed'].items():
            for family,detail in ob['selection_details'].items():
                for row in detail['candidates']:
                    writer.writerow([run,kind,family,','.join(map(str,row['offsets'])) or 'none',row['selection_mse'],row['offsets']==detail['winner']['offsets']])
print('wrote README.md and selection_catalog.csv')
