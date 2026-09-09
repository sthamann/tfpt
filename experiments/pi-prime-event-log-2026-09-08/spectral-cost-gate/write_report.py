import json
from pathlib import Path
R=Path(__file__).resolve().parent
s=json.loads((R/'summary.json').read_text());meta=json.loads((R/'run_metadata.json').read_text())
labels={'direct_mod':'Dichte Modulo-Prüfung','root_stride':'Modulares Wurzelsieb','fourier_fft':'Fourier-Rekonstruktion / FFT'}
lines=['# Exakte Ereignisse: Fourier-Darstellung gegen modulares Sieb','',
'Stand: 8. September 2026. Ausgeführte Fortsetzung der π-/Primzahl-Untersuchung.','',
'**Ergebnis:** Die drei Verfahren liefern dieselben Kandidaten, Relationen und Faktoren. Die untersuchte Fourier-Auswertung ist in beiden Kohorten langsamer als das klassische Wurzelsieb. Der vorab definierte Faktor-2-Vorteil wird nicht erreicht. Dies grenzt die konkrete Konstruktion ein; es ist kein allgemeiner Unmöglichkeitsbeweis für spektrale Faktorisierungsverfahren.','',
'## Was genau verglichen wurde','',
'128 neue, balancierte Semiprime mit tatsächlichen 32, 40, 48 und 56 Bit; je 16 pro Größe und Kohorte. Kein Input kommt in den drei vorangegangenen Datensätzen vor. Pro N: 65.536 Kandidaten Q_j=(ceil(sqrt(N))+j)²−N; 16.384 werden nach einem identischen ganzzahligen Restwert ausgewählt. Für die Vorauswahl werden dieselben zulässigen Primzahlen p≤43 und dieselben Potenzen p^k≤4096 verwendet. Diese endliche Potenzgrenze unterscheidet den Score vom vorherigen arithmetic-gate. Trefferzahlen sind deshalb auch unabhängig von den neuen Inputs kein direkter Vorher-nachher-Vergleich.','',
'Die dichte Variante prüft jede Teilbarkeit. Das Wurzelsieb markiert nur die arithmetischen Folgen mit Q_j≡0 mod p^k. Die Fourier-Variante baut aus genau diesen kleinen modularen Wurzeln die Fourier-Koeffizienten und rekonstruiert die periodischen Ereignismasken mit inverser FFT. Jede Methode übernimmt danach dieselbe exakte Glattheitsprüfung, binäre Elimination, Quadratkongruenz und ggT-Prüfung. N ist der einzige Faktorinput des Laufzeitprogramms; die getrennte Lösungsliste dient erst dem Audit.','',
'Fünf vollständige Wiederholungen mit rotierender Methodenreihenfolge. Alle Zeiten unten sind Summen der Mediane je N. Aufbau der Faktorbasis, Ermittlung kleiner Wurzeln, Koeffizienten, FFT, Rundungskontrolle, Allokationen, Sortierung und anschließende Faktorprüfung werden jeweils dort berechnet, wo sie benötigt werden. Es gibt keinen N-abhängigen Cache. Gemeinsamer Python-Start/Import und Audit-/JSON-Ausgabe liegen außerhalb der Einzelfallzeiten. Auch Operationszähler gehören zur gemessenen Implementierung; dies ist kein produktionsoptimierter Leistungsvergleich.','',
'## Gemessene Ergebnisse','',
'| Kohorte | Verfahren | Faktoren | Glatte Relationen | Rang | Auswahlzeit | Gesamtzeit |',
'|---|---|---:|---:|---:|---:|---:|']
for split in ['discovery','validation']:
    for m,v in s[split]['methods'].items():
        lines.append(f'| {split} | {labels[m]} | {v["factors"]}/64 | {v["smooth"]:,} | {v["rank"]:,} | {v["selector_seconds"]:.4f} s | {v["runtime_seconds"]:.4f} s |')
v=s['validation']['methods'];d=v['direct_mod'];r=v['root_stride'];f=v['fourier_fft']
lines+=['',f'In der Validierung braucht die Fourier-Variante {(f["runtime_seconds"]/r["runtime_seconds"]-1)*100:.1f}% mehr Gesamtzeit als das Wurzelsieb. Die reine Vorauswahl einschließlich Sortierung dauert {f["selector_seconds"]/r["selector_seconds"]:.2f}-mal so lange. Gegenüber der dichten Modulo-Implementierung ist das Wurzelsieb in diesem Lauf insgesamt {d["runtime_seconds"]/r["runtime_seconds"]:.2f}-mal so schnell.','',
f'Der Gewinn vor der abschließenden Division und Sortierung ist wesentlich größer: {d["score_seconds"]/r["score_seconds"]:.1f}× für den gemessenen Aufbau und die Ereignisaktualisierung. Mit Division und Sortierung bleiben {d["selector_seconds"]/r["selector_seconds"]:.2f}×, mit vollständiger Faktorprüfung {d["runtime_seconds"]/r["runtime_seconds"]:.2f}×. Die {d["dense_modular_tests"]:,} dichten Modulo-Tests der Vorauswahl werden durch {r["event_updates"]:,} gezielte Multiplikationsereignisse plus Wurzelaufbau ersetzt. Sortierung macht {100*r["sort_seconds"]/r["selector_seconds"]:.1f}% der Auswahlzeit des Wurzelsiebs aus. Ein lokaler Siebgewinn darf deshalb nicht als gleich großer Faktorisierungsgewinn ausgegeben werden.','',
'| Kohorte | Wurzelsieb-Zeit / FFT-Zeit | 95%-Bootstrapintervall | Modulo-Zeit / Wurzelsieb-Zeit | 95%-Bootstrapintervall |',
'|---|---:|---:|---:|---:|']
for split in ['discovery','validation']:
    a=s[split]['fft_speed_vs_stride'];b=s[split]['stride_speed_vs_direct']
    lines.append(f'| {split} | {a["ratio"]:.3f} | {a["bootstrap_95"][0]:.3f}–{a["bootstrap_95"][1]:.3f} | {b["ratio"]:.3f} | {b["bootstrap_95"][0]:.3f}–{b["bootstrap_95"][1]:.3f} |')
lines+=['','19.999 gepaarte Bootstrap-Ziehungen je Kohorte; die Intervalle beschreiben Variation über diese Inputs und sind keine hardwareunabhängige Genauigkeitsgarantie. Die FFT müsste nach Protokoll in beiden Kohorten einen Quotienten von mindestens 2 und eine Untergrenze über 1 erreichen. Tatsächlich liegt der Quotient in beiden Kohorten unter 1.','',
'## Skalierungsprüfung','',
'Jeweils der erste Validierungsinput jeder Bitgröße; fünf Auswahlwiederholungen pro Fall, ohne nachfolgende Faktorisierung. Der Tabellenwert summiert die vier Mediane. Faktorbasiserzeugung ist in dieser Zusatzprüfung ausgeschlossen, der Wurzelaufbau enthalten.','',
'| Kandidaten pro N | Modulo-Auswahl | Wurzelsieb-Auswahl | Fourier-Auswahl |',
'|---:|---:|---:|---:|']
for pool in [65536,262144,1048576]:
    vals={m:sum(row['methods'][m] for row in s['scale'] if row['pool']==pool) for m in labels}
    lines.append(f'| {pool:,} | {vals["direct_mod"]:.4f} s | {vals["root_stride"]:.4f} s | {vals["fourier_fft"]:.4f} s |')
lines+=['','Auch in allen zwölf Einzelfällen dieser Zusatzprüfung ist das Wurzelsieb schneller als die Fourier-Auswahl. Daraus folgt keine Aussage über ungetestete Modulusgrenzen, andere Spektralalgorithmen oder kryptographische Eingabegrößen.','',
'## Die mathematische Aussage hinter dem Ereignislog','',
'Sei A_q={s mod q : (a+s)²≡N mod q}. Die verwendeten Koeffizienten sind','',
'```text','C_k = Σ_(s in A_q) exp(−2π i k s/q)','E_q(j) = (1/q) Σ_(k=0..q−1) C_k exp(2π i k j/q)','       = 1, falls j mod q in A_q liegt; sonst 0.','```','',
'Die letzte Gleichheit folgt aus der endlichen geometrischen Summe: jede Wurzel erzeugt einen Indikator ihrer Restklasse. Es ist die klassische endliche Fourier-Darstellung periodischer zahlentheoretischer Funktionen, siehe [DLMF 27.10](https://dlmf.nist.gov/27.10). Die Implementierung nutzt die [NumPy-Konvention der inversen FFT](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html).','',
'Für die Ausgangsidee bedeutet das: Ein solches arithmetisches Ereignislog lässt sich exakt als Überlagerung von Kreisphasen schreiben. In dieser Konstruktion sind die Ereignispositionen aber bereits vollständig in den kleinen modularen Wurzeln enthalten. Die Transformation fügt ihnen keine zusätzliche Faktorinformation hinzu. π dient als Winkelmaß der Darstellung; seine Dezimalziffern werden hier nicht abgefragt. Die frühere Suche nach Ziffernkorrelationen und der jetzige Kostentest beantworten daher unterschiedliche, aufeinander aufbauende Fragen.','',
'Auch die modulare Wurzelmarkierung ist im Projekt bereits vorhanden: [regulator_relation_probe.py](../../tfpt-discovery/regulator_relation_probe.py) hebt Wurzeln auf Primzahlpotenzen und aktualisiert arithmetische Folgen. Die lokale Verbesserung gegenüber der dichten Kontrollimplementierung ist ein klassischer Siebeffekt, keine neue TFPT- oder RH-Brücke.','',
'## Nachweise und Reichweite','',
f'- {s["audit"]["full_array_runtime_comparisons"]:,} vollständige Ergebnisvergleiche im Hauptlauf und 180 im Skalierungslauf: alle Restwert-Arrays und ausgewählten Indizes identisch.',
f'- {s["audit"]["saved_certificates_verified"]} gespeicherte Erfolgszertifikate unabhängig über beliebig große ganze Zahlen nachgerechnet, kein falsches Zertifikat. Das sind dieselben 124 verschiedenen erfolgreich zerlegten N in drei Methoden, keine 372 unabhängigen Faktorprobleme.',
'- Alle 32-, 40- und 48-Bit-Inputs werden zerlegt. Pro Kohorte scheitern innerhalb des festen Budgets dieselben zwei von 16 Inputs mit 56 Bit.',
'- Vier Testgruppen prüfen vollständige Wurzelmengen gegen Restklassen-Bruteforce, einschließlich p=2 und singulärer Wurzeln, ganze Fourier-Perioden gegen exakte Teilbarkeit, Restwerte und Indexgleichheit sowie Überlauf-/Methodenfehler.',
f'- Maximaler beobachteter FFT-Rundungs-/Imaginärrest: {s["audit"]["max_fft_residual"]:.3g}, Grenzwert 1e-10. Die gesamten Ergebnis-Arrays sind zusätzlich exakt verglichen; das ist ein endlicher Audit, kein allgemeiner Intervallbeweis für größere Transformationen.',
f'- Hauptlauf-Wandzeit einschließlich Wiederholungen und Ausgabe: {meta["batch_wall_seconds"]:.3f} s. Umgebung: Python {meta["python"]}, NumPy {meta["numpy"]}, {meta["platform"]}. Gemeinsamer Prozess-RSS-Höchstwert: {meta["peak_process_rss_platform_units"]/1048576:.1f} MiB auf macOS; keine Speichervergleichsmessung je Methode.',
'- Noch kein Nachweis eines π-spezifischen Informationsgewinns, einer RH-Folgerung, einer neuen asymptotischen Faktorisierungsmethode oder eines Vorteils bei großen RSA-Zahlen. Die negative Aussage betrifft diese exakt spezifizierte Konstruktion.','',
'Ein weiterer spektraler Ansatz wäre erst eine neue Hypothese, wenn seine aus N berechenbaren Koeffizienten zusätzliche prüfbare Relationen liefern oder dieselben Relationen mit weniger Gesamtarbeit erzeugen. Das bloße Fourier-Umkodieren schon bekannter Teilbarkeitspositionen erfüllt beides hier nicht.','',
'## Reproduktion','',
'```sh','cd experiments/pi-prime-event-log-2026-09-08/spectral-cost-gate','python3 -m unittest -v test_spectral.py','python3 make_inputs.py','python3 engine_spectral.py','python3 scale_check.py','python3 analyze.py','python3 write_report.py','```','',
'Abhängigkeiten: Python, NumPy, SymPy. Kein Download von π-Ziffern nötig. Neue Läufe überschreiben nur die lokalen Ergebnisse dieses Unterordners; Messzeiten variieren. Das unveränderte Elternmodul wird vor dem Lauf über SHA256 geprüft. Das vor der Datenerzeugung gespeicherte [Protokoll](PROTOCOL.md), [Inputmanifest](input_manifest.json), [Laufmanifest](run_metadata.json), [Rohdaten](runs.jsonl), [Skalierungsdaten](scale_runs.json) und [maschinenlesbare Zusammenfassung](summary.json) liegen neben diesem Bericht.','']
(R/'README.md').write_text('\n'.join(lines))
print('wrote README.md')
