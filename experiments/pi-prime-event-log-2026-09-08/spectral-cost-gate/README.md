# Exakte Ereignisse: Fourier-Darstellung gegen modulares Sieb

Stand: 8. September 2026. Ausgeführte Fortsetzung der π-/Primzahl-Untersuchung.

**Ergebnis:** Die drei Verfahren liefern dieselben Kandidaten, Relationen und Faktoren. Die untersuchte Fourier-Auswertung ist in beiden Kohorten langsamer als das klassische Wurzelsieb. Der vorab definierte Faktor-2-Vorteil wird nicht erreicht. Dies grenzt die konkrete Konstruktion ein; es ist kein allgemeiner Unmöglichkeitsbeweis für spektrale Faktorisierungsverfahren.

## Was genau verglichen wurde

128 neue, balancierte Semiprime mit tatsächlichen 32, 40, 48 und 56 Bit; je 16 pro Größe und Kohorte. Kein Input kommt in den drei vorangegangenen Datensätzen vor. Pro N: 65.536 Kandidaten Q_j=(ceil(sqrt(N))+j)²−N; 16.384 werden nach einem identischen ganzzahligen Restwert ausgewählt. Für die Vorauswahl werden dieselben zulässigen Primzahlen p≤43 und dieselben Potenzen p^k≤4096 verwendet. Diese endliche Potenzgrenze unterscheidet den Score vom vorherigen arithmetic-gate. Trefferzahlen sind deshalb auch unabhängig von den neuen Inputs kein direkter Vorher-nachher-Vergleich.

Die dichte Variante prüft jede Teilbarkeit. Das Wurzelsieb markiert nur die arithmetischen Folgen mit Q_j≡0 mod p^k. Die Fourier-Variante baut aus genau diesen kleinen modularen Wurzeln die Fourier-Koeffizienten und rekonstruiert die periodischen Ereignismasken mit inverser FFT. Jede Methode übernimmt danach dieselbe exakte Glattheitsprüfung, binäre Elimination, Quadratkongruenz und ggT-Prüfung. N ist der einzige Faktorinput des Laufzeitprogramms; die getrennte Lösungsliste dient erst dem Audit.

Fünf vollständige Wiederholungen mit rotierender Methodenreihenfolge. Alle Zeiten unten sind Summen der Mediane je N. Aufbau der Faktorbasis, Ermittlung kleiner Wurzeln, Koeffizienten, FFT, Rundungskontrolle, Allokationen, Sortierung und anschließende Faktorprüfung werden jeweils dort berechnet, wo sie benötigt werden. Es gibt keinen N-abhängigen Cache. Gemeinsamer Python-Start/Import und Audit-/JSON-Ausgabe liegen außerhalb der Einzelfallzeiten. Auch Operationszähler gehören zur gemessenen Implementierung; dies ist kein produktionsoptimierter Leistungsvergleich.

## Gemessene Ergebnisse

| Kohorte | Verfahren | Faktoren | Glatte Relationen | Rang | Auswahlzeit | Gesamtzeit |
|---|---|---:|---:|---:|---:|---:|
| discovery | Dichte Modulo-Prüfung | 62/64 | 18,039 | 5,318 | 0.5009 s | 1.7532 s |
| discovery | Modulares Wurzelsieb | 62/64 | 18,039 | 5,318 | 0.2286 s | 1.4784 s |
| discovery | Fourier-Rekonstruktion / FFT | 62/64 | 18,039 | 5,318 | 0.4647 s | 1.7151 s |
| validation | Dichte Modulo-Prüfung | 62/64 | 17,760 | 5,291 | 0.4944 s | 1.7443 s |
| validation | Modulares Wurzelsieb | 62/64 | 17,760 | 5,291 | 0.2282 s | 1.5018 s |
| validation | Fourier-Rekonstruktion / FFT | 62/64 | 17,760 | 5,291 | 0.4469 s | 1.7091 s |

In der Validierung braucht die Fourier-Variante 13.8% mehr Gesamtzeit als das Wurzelsieb. Die reine Vorauswahl einschließlich Sortierung dauert 1.96-mal so lange. Gegenüber der dichten Modulo-Implementierung ist das Wurzelsieb in diesem Lauf insgesamt 1.16-mal so schnell.

Der Gewinn vor der abschließenden Division und Sortierung ist wesentlich größer: 18.9× für den gemessenen Aufbau und die Ereignisaktualisierung. Mit Division und Sortierung bleiben 2.17×, mit vollständiger Faktorprüfung 1.16×. Die 130,416,640 dichten Modulo-Tests der Vorauswahl werden durch 9,129,263 gezielte Multiplikationsereignisse plus Wurzelaufbau ersetzt. Sortierung macht 93.4% der Auswahlzeit des Wurzelsiebs aus. Ein lokaler Siebgewinn darf deshalb nicht als gleich großer Faktorisierungsgewinn ausgegeben werden.

| Kohorte | Wurzelsieb-Zeit / FFT-Zeit | 95%-Bootstrapintervall | Modulo-Zeit / Wurzelsieb-Zeit | 95%-Bootstrapintervall |
|---|---:|---:|---:|---:|
| discovery | 0.862 | 0.849–0.874 | 1.186 | 1.168–1.206 |
| validation | 0.879 | 0.862–0.894 | 1.161 | 1.136–1.188 |

19.999 gepaarte Bootstrap-Ziehungen je Kohorte; die Intervalle beschreiben Variation über diese Inputs und sind keine hardwareunabhängige Genauigkeitsgarantie. Die FFT müsste nach Protokoll in beiden Kohorten einen Quotienten von mindestens 2 und eine Untergrenze über 1 erreichen. Tatsächlich liegt der Quotient in beiden Kohorten unter 1.

## Skalierungsprüfung

Jeweils der erste Validierungsinput jeder Bitgröße; fünf Auswahlwiederholungen pro Fall, ohne nachfolgende Faktorisierung. Der Tabellenwert summiert die vier Mediane. Faktorbasiserzeugung ist in dieser Zusatzprüfung ausgeschlossen, der Wurzelaufbau enthalten.

| Kandidaten pro N | Modulo-Auswahl | Wurzelsieb-Auswahl | Fourier-Auswahl |
|---:|---:|---:|---:|
| 65,536 | 0.0305 s | 0.0141 s | 0.0277 s |
| 262,144 | 0.1334 s | 0.0683 s | 0.1050 s |
| 1,048,576 | 0.5972 s | 0.3334 s | 0.4684 s |

Auch in allen zwölf Einzelfällen dieser Zusatzprüfung ist das Wurzelsieb schneller als die Fourier-Auswahl. Daraus folgt keine Aussage über ungetestete Modulusgrenzen, andere Spektralalgorithmen oder kryptographische Eingabegrößen.

## Die mathematische Aussage hinter dem Ereignislog

Sei A_q={s mod q : (a+s)²≡N mod q}. Die verwendeten Koeffizienten sind

```text
C_k = Σ_(s in A_q) exp(−2π i k s/q)
E_q(j) = (1/q) Σ_(k=0..q−1) C_k exp(2π i k j/q)
       = 1, falls j mod q in A_q liegt; sonst 0.
```

Die letzte Gleichheit folgt aus der endlichen geometrischen Summe: jede Wurzel erzeugt einen Indikator ihrer Restklasse. Es ist die klassische endliche Fourier-Darstellung periodischer zahlentheoretischer Funktionen, siehe [DLMF 27.10](https://dlmf.nist.gov/27.10). Die Implementierung nutzt die [NumPy-Konvention der inversen FFT](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html).

Für die Ausgangsidee bedeutet das: Ein solches arithmetisches Ereignislog lässt sich exakt als Überlagerung von Kreisphasen schreiben. In dieser Konstruktion sind die Ereignispositionen aber bereits vollständig in den kleinen modularen Wurzeln enthalten. Die Transformation fügt ihnen keine zusätzliche Faktorinformation hinzu. π dient als Winkelmaß der Darstellung; seine Dezimalziffern werden hier nicht abgefragt. Die frühere Suche nach Ziffernkorrelationen und der jetzige Kostentest beantworten daher unterschiedliche, aufeinander aufbauende Fragen.

Auch die modulare Wurzelmarkierung ist im Projekt bereits vorhanden: [regulator_relation_probe.py](../../tfpt-discovery/regulator_relation_probe.py) hebt Wurzeln auf Primzahlpotenzen und aktualisiert arithmetische Folgen. Die lokale Verbesserung gegenüber der dichten Kontrollimplementierung ist ein klassischer Siebeffekt, keine neue TFPT- oder RH-Brücke.

## Nachweise und Reichweite

- 1,920 vollständige Ergebnisvergleiche im Hauptlauf und 180 im Skalierungslauf: alle Restwert-Arrays und ausgewählten Indizes identisch.
- 372 gespeicherte Erfolgszertifikate unabhängig über beliebig große ganze Zahlen nachgerechnet, kein falsches Zertifikat. Das sind dieselben 124 verschiedenen erfolgreich zerlegten N in drei Methoden, keine 372 unabhängigen Faktorprobleme.
- Alle 32-, 40- und 48-Bit-Inputs werden zerlegt. Pro Kohorte scheitern innerhalb des festen Budgets dieselben zwei von 16 Inputs mit 56 Bit.
- Vier Testgruppen prüfen vollständige Wurzelmengen gegen Restklassen-Bruteforce, einschließlich p=2 und singulärer Wurzeln, ganze Fourier-Perioden gegen exakte Teilbarkeit, Restwerte und Indexgleichheit sowie Überlauf-/Methodenfehler.
- Maximaler beobachteter FFT-Rundungs-/Imaginärrest: 5.22e-16, Grenzwert 1e-10. Die gesamten Ergebnis-Arrays sind zusätzlich exakt verglichen; das ist ein endlicher Audit, kein allgemeiner Intervallbeweis für größere Transformationen.
- Hauptlauf-Wandzeit einschließlich Wiederholungen und Ausgabe: 50.522 s. Umgebung: Python 3.14.3, NumPy 2.4.2, macOS-26.4.1-arm64-arm-64bit-Mach-O. Gemeinsamer Prozess-RSS-Höchstwert: 78.9 MiB auf macOS; keine Speichervergleichsmessung je Methode.
- Noch kein Nachweis eines π-spezifischen Informationsgewinns, einer RH-Folgerung, einer neuen asymptotischen Faktorisierungsmethode oder eines Vorteils bei großen RSA-Zahlen. Die negative Aussage betrifft diese exakt spezifizierte Konstruktion.

Ein weiterer spektraler Ansatz wäre erst eine neue Hypothese, wenn seine aus N berechenbaren Koeffizienten zusätzliche prüfbare Relationen liefern oder dieselben Relationen mit weniger Gesamtarbeit erzeugen. Das bloße Fourier-Umkodieren schon bekannter Teilbarkeitspositionen erfüllt beides hier nicht.

## Reproduktion

```sh
cd experiments/pi-prime-event-log-2026-09-08/spectral-cost-gate
python3 -m unittest -v test_spectral.py
python3 make_inputs.py
python3 engine_spectral.py
python3 scale_check.py
python3 analyze.py
python3 write_report.py
```

Abhängigkeiten: Python, NumPy, SymPy. Kein Download von π-Ziffern nötig. Neue Läufe überschreiben nur die lokalen Ergebnisse dieses Unterordners; Messzeiten variieren. Das unveränderte Elternmodul wird vor dem Lauf über SHA256 geprüft. Das vor der Datenerzeugung gespeicherte [Protokoll](PROTOCOL.md), [Inputmanifest](input_manifest.json), [Laufmanifest](run_metadata.json), [Rohdaten](runs.jsonl), [Skalierungsdaten](scale_runs.json) und [maschinenlesbare Zusammenfassung](summary.json) liegen neben diesem Bericht.
