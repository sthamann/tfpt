"""Build the follow-up report from immutable run outputs."""
import json,hashlib
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
read=lambda name:json.loads((R/name).read_text())
d=read('results.json');v=d['summary']['validation'];precision=read('precision_results.json');selection=read('selection_results.json')
text='''# π, arithmetische Ereignisse und Faktorisierung: bedingte Gegenprüfung

8. September 2026. **Es gibt einen klaren Effekt der arithmetischen Vorauswahl,
aber keinen nachgewiesenen Zusatznutzen der π-Ziffern.** Die Phasenform von π ist
präzise mit Teilbarkeit verbunden; ihre vollständige Auswertung ist dieselbe
Information wie ein klassisches Sieb. Eine festgelegte verkürzte Phasensumme ist
numerisch brauchbar, ergibt hier aber keine nachgewiesene neue Abkürzung.

Diese Fortsetzung beantwortet zwei bisher getrennte Fragen:

1. Kann π als Phasennormalisierung direkt an Q=x²−N gekoppelt werden?
2. Enthalten π-Ziffern noch nützliche Auswahlinformation, nachdem die kleinen
   Faktoren von Q in allen verglichenen Methoden gleichermaßen bekannt sind?

## Die exakte Brücke zum Ereignislog

Für jede positive ganze Zahl q definiere

    P_q(Q) = (1/q) sum_{k=0}^{q−1} exp(2π i kQ/q).

Dann gilt exakt

    P_q(Q) = 1, falls q | Q; sonst 0.

**Beweis:** Bei q|Q ist jeder Summand eins. Andernfalls ist
z=exp(2πiQ/q) ungleich eins, aber z^q=1; die geometrische Summe
(1−z^q)/(1−z) verschwindet. Das gilt auch für Primzahlpotenzen q=p^a.
Diese elementare Charakterorthogonalität ist Teil der klassischen endlichen
Fourieranalyse; [NIST DLMF 27.10](https://dlmf.nist.gov/27.10) beschreibt die
entsprechenden Fourierdarstellungen periodischer zahlentheoretischer Funktionen.
Es ist hier eine angewandte klassische Identität, kein neuer Satz.

Wer die Ereignisse bei Primzahlpotenzen mit log(p) gewichtet, erhält für einen
festen kleinen Primzahlbereich

    sum_{p≤43} sum_{a≥1} log(p) P_{p^a}(Q)
      = sum_{p≤43} v_p(Q) log(p)
      = log(Q) − log(R_43(Q)),

wobei R_43(Q) nach Entfernen sämtlicher kleiner Primfaktoren aus Q übrig bleibt.
Nur endlich viele Summanden sind ungleich null. Das ist ein konkreter gewichteter
Primereignislog und eine präzise π–Arithmetik-Verbindung. Die Perioden p^a und ihre
Gewichte werden allerdings als bekannte kleine Primdaten hineingegeben. Unbekannte
Faktoren von N werden hierdurch nicht aus π herausgelesen.

Der vollständige Phasenprojektor liefert **keine zusätzlichen Daten gegenüber
der Restrechnung Q mod q**. Man kann dieselbe Fourierdarstellung auch in Umläufen
statt Radianten schreiben; π ist dabei die Winkelnormalisierung, kein kostenloser
separater Informationskanal. Eine positive endliche Phasensumme liefert zudem
keinen globalen Weil-/RH-Positivitätssatz.

## Die neue, vorher festgelegte Ausleseregel

Wieder gilt x=ceil(sqrt(N))+j mit 65.536 möglichen Offsets j. Vor der teureren
vollständigen Glattheitsprüfung werden in allen Kandidaten Q=x²−N sämtliche
Potenzen der geeigneten Primzahlen bis 43 entfernt. Dieser ganze Vorscan wird
berechnet und in die Kosten aufgenommen. Die vollständige Faktorbasis reicht,
abhängig von der Eingabegröße, bis 200/500/1200/2500.

Die π-Regel sortiert nach

    (Bitlänge von R_43(Q), achtstelliger π-Schlüssel, Offset j).

Die Schlüsseladresse ist wie vorher aus N und j bestimmt; die Faktoren von N
werden nicht benutzt. e, √2 und fünf Zufallsquellen erhalten dieselben Restklassen
und Bitlängen. Die genaue arithmetische Kontrolle sortiert direkt nach
(R_43(Q),j), ohne Quantisierung und Ziffernquelle. Sie nutzt also die ohnehin
verfügbare Restinformation genauer. Zusätzlich läuft die fortlaufende Suche.

Die Begrenzung durch Bitlängen ist vor der Rechnung festgelegt. Im Validierungssatz
liegen im Mittel 12,66 % der ausgewählten Plätze im entscheidenden Rand-Bucket,
in dem der Ziffernschlüssel überhaupt wählen darf. Die ausgewählten Mengen von π
und einer Zufallskontrolle überschneiden sich im Mittel zu 95,71 %. Damit ist der
Test gezielt auf Zusatzinformation nach der arithmetischen Bedingung beschränkt;
er ist keine umfassende Poweranalyse für beliebige π-Algorithmen.

## Die verkürzte Phasenvariante

Separat, als explorative Variante, wurde fest H=8 gewählt:

    F_8(r/q) = |(1/9) sum_{k=0}^8 exp(2π i kr/q)|².

Für p≤43 und q=p^a≤4096 bekommt ein Kandidat den Score

    sum_{q=p^a} log(p) F_8((Q mod q)/q) − log(Q).

Das ist ein normalisierter Fejér-artiger Filter. Er besitzt breite Seitenwerte
und ist nicht der vollständige exakte Teilbarkeitsprojektor. Die ganzzahligen
Reste werden vor jeder Gleitkomma-Auswertung exakt berechnet. Die Tabellen aller
verwendeten Phasen und ihre Erzeugungskosten werden pro Eingabe mitgezählt.

Dieser Filter ist außerdem bei Potenzen q≤4096 abgeschnitten, während die
arithmetische Kontrolle alle kleinen Primzahlpotenzen entfernt. Der Vergleich
ist daher ein Vergleich der vollständig spezifizierten Verfahren; ein Unterschied
kann aus Approximation UND Potenzabschneidung entstehen. Eine isolierte optimale
Harmonischenzahl oder eine neue Spektraltheorie wird daraus nicht abgeleitet.

## Frische Daten und Resultate

128 neue, verschiedene ausgeglichene Semiprime mit exakt 32,40,48,56 Bit,
ohne Überschneidung mit den beiden früheren Faktorversuchen. Zwei vorab getrennte
Sätze mit je 64 Zahlen, 16 pro Größe. Elf Methoden, insgesamt 1.408 vollständige
Läufe. Jeweils 16.384 Kandidaten werden vollständig geprüft; zusätzlich anfallende
Vorscans im größeren Pool zählen ausdrücklich zur Arbeit. Auch nach einem ersten
Faktor läuft jeder Versuch bis zum Ende seines festen Budgets weiter.

| Methode im Validierungssatz | Glatte Relationen | Faktorisierte Zahlen | Gesamtzeit, anteilige Vorbereitung |
|---|---:|---:|---:|
'''
for method,label in [('sequential','Fortlaufend'),('exact_cofactor','Exakter kleiner Kofaktor'),('phase8','Verkürzte π-Phasensumme'),('bucket_pi','Kofaktor-Bucket + π-Ziffern'),('bucket_e','Kofaktor-Bucket + e-Ziffern'),('bucket_sqrt2','Kofaktor-Bucket + √2-Ziffern')]:
 row=v[method];text+=f"| {label} | {row['smooth']} | {row['factor_successes']}/64 | {row['amortized_total_seconds']:.3f} s |\n"
text+=f"| Kofaktor-Bucket + Zufall, Mittel aus fünf Läufen | {np.mean([v[f'bucket_random{j}']['smooth'] for j in range(5)]):.1f} | 61/64 | {np.mean([v[f'bucket_random{j}']['amortized_total_seconds'] for j in range(5)]):.3f} s |\n"
text+='''
Der arithmetische Filter erhöht bei diesem Budget vollständiger Restprüfungen
Ausbeute und Erfolgszahl. Die **Gesamtlaufzeit steigt zugleich**. Das ist kein
belegter Vorteil bei gleichem Gesamtzeitbudget. Insbesondere darf man die
65.536-fache kleine Vorprüfung nicht verschwinden lassen.

Die Verbesserung gegenüber der fortlaufenden Suche im selben neuen Datensatz
ist messbar. Sie kann nicht allein π zugeschrieben werden: Alle fünf Zufallsläufe,
e, √2 und der exakte kleine Kofaktor erreichen dieselben 61/64 wie π. Im ersten
Satz erreichen π und die exakte Kontrolle ebenfalls 61/64, die Zufallsläufe
60–61/64. Die früheren unbedingten π-Läufe benutzten andere N; ihre Trefferquoten
werden hier nicht als gepaarter Vorher/Nachher-Beweis behandelt.

![Faktorerfolg und Gesamtzeit](comparison.png)

## Der eigentliche π-Zusatztest

| Vergleich | Differenz glatter Relationen pro N | Einseitiges p | Holm-p |
|---|---:|---:|---:|
'''
for t in d['tests']:
 label=('Erster Satz' if t['split']=='discovery' else 'Validierung')+' / '+('gleicher Bucket mit Zufall' if t['control']=='random_mean' else 'exakter kleiner Kofaktor')
 text+=f"| {label} | {t['mean_difference']:.5f} | {t['p_one_sided']:.5f} | {t['holm_p']:.2f} |\n"
text+='''
Alle π-Differenzen sind negativ; keine der vier vorgesehenen Überlegenheitsprüfungen
besteht. Im Validierungssatz ist π mit p=0,616 gegen das Zufallsmittel unauffällig.
Die gepaarten Vorzeichenpermutationen (19.999 pro Vergleich) setzen die im Protokoll
benannte Symmetrie/Austauschbarkeit voraus. Der Befund ist auf die feste Bucketregel,
diese Generatorverteilung und die endliche Datengröße begrenzt.

Auch das vorab gesetzte Kostentor fehlt: Der unabhängige Relationenrang pro
verrechneter Sekunde erreicht bei π das 0,777-Fache der passenden Zufallskontrolle
und das 0,662-Fache der exakten Kofaktorkontrolle; verlangt war mindestens das
Zweifache beider. Gleichbleibende Faktor-Erfolgszahl allein reicht nicht aus.

Die Phasenvariante ist etwas schneller als die hier implementierte exakte
Kofaktorauswahl, produziert aber weniger Relationen und löst eine Aufgabe weniger.
Ihr Rangdurchsatz liegt nur etwa 4,4 % über dieser Kontrolle und deutlich unter
der fortlaufenden Suche. Das sind einzelne, kurze Implementierungsmessungen,
keine nachgewiesene robuste Zeitverbesserung. Es wurde kein optimaler QS-/NFS-
Vergleich durchgeführt, kein Zeitbudget nachträglich angepasst und kein weiterer
Phasenparameter nach einem günstigen Ergebnis gesucht.

## Exaktheit, Stabilität und tatsächliche Kosten

**1.327 gespeicherte Erfolgszertifikate unabhängig bestätigt, null falsche Faktoren.**
Die Nachprüfung rekonstruiert jedes Q=x²−N, bildet das exakte ganzzahlige Produkt,
prüft dessen Quadratwurzel, die modularen Werte und die ggT-Zerlegung von N.
Das Suchprogramm liest nur die öffentliche N-Liste; die Antwortdatei wird erst
im getrennten Nachprüfprogramm verwendet. Der ursprüngliche Relationenkern wird
über einen festen Quellhash eingebunden und blieb unverändert.

Sieben Tests prüfen die skalare Kofaktorzerlegung unabhängig gegen die
Vektorrechnung, die bedingte π-Auswahl anhand direkter Stringauslese, komplexe
Phasensummen, Teilbarkeitsprojektoren und positive Faktorisierungskontrollen.

Für vier vorher bestimmte Validierungseingaben, eine pro Bitgröße, wurden jeweils
112 Scores mit 80 Dezimalstellen nachgerechnet, darunter 32 Kandidaten auf jeder
Seite der Auswahlgrenze. Maximaler Float64-Fehler: etwa 7,94·10^−13; kleinster
hochauflösender Abstand über die geprüfte Grenze: etwa 3,76·10^−5. Keine Änderung
der überprüften Grenzzugehörigkeit. Die vollständigen Projektorsummen zeigten in
der numerischen Regression höchstens 2,15·10^−80 Rest. Das ergänzt den elementaren
Beweis, ersetzt aber keine Intervallzertifizierung sämtlicher Float-Sortierungen.

Alle 1.408 Varianten zusammen brauchten rund 45,7 Sekunden ohne erneute Erzeugung
der vorhandenen Zifferndateien. In den Methodenvergleichen werden deren Erzeugung
und aktuelles Einlesen anteilig belastet; zusätzlich sind komplette kalte
Vorbereitungskosten pro Eingabe gespeichert. Exakte Ops-Zähler unterscheiden den
vollen Poolvorscan von den 16.384 vollständigen Screenings. Dateiausgabe und
Berichterstellung sind getrennt vom Algorithmusdurchsatz zu verstehen. Die
Phasenvariante verwendet die gewöhnliche Gleitkomma-Konstante π, nicht den
Zwei-Millionen-Ziffernspeicher; dort fallen stattdessen Phasentabellenkosten an.

## Was sich gegenüber den ersten beiden Versuchen geändert hat

Es ist jetzt eine echte Kopplung an die Arithmetik von N vorhanden. Ihre Herkunft
ist aber nachvollziehbar: bekannte kleine Primzahlpotenzen, Restklassen und die
klassische Beziehung zwischen kleiner Restgröße und Glattheitschancen. Die
Kreisphasen können diese Teilbarkeitsereignisse exakt ausdrücken. Sie erzeugen
bei vollständiger Auflösung dieselben Informationen, die der integerbasierte
Filter schon besitzt.

Die Dezimalhypothese ist enger geprüft: Selbst nach arithmetischer Bedingung
liefert die festgelegte π-Auswahl keinen Restvorteil gegenüber kontrollierten
Zufallsziffern. Ein allgemeiner Ausschluss anderer π-Mechanismen folgt nicht.
Die starke Überlappung der ausgewählten Kandidaten begrenzt zugleich, wie groß
der verbleibende Testspielraum hier ist.

Für r644 ist die Unterscheidung weiter wichtig: Quadratkongruenzen über Exponenten
modulo zwei sind noch keine orientierten Relationen, aus denen ein Regulator
rekonstruiert wird. Weder ein Regulator noch eine globale all-place Realisierung
oder RH-Positivität werden in diesem Versuch gewonnen.

**Nächste sachliche Grenze:** Ein neuer Ansatz muss Information liefern, die nicht
bereits in den hineingegebenen kleinen Restklassen steckt, oder dieselbe relevante
Information nachweisbar mit weniger Gesamtarbeit gewinnen. Ein größeres π-Präfix,
eine neue Schreibweise der exakten Fourieridentität oder ungeprüfte Änderungen
an H genügen dafür nicht. Die getestete digitale Zusatzregel besteht dieses Tor
nicht; die funktionierende arithmetische Vorauswahl ist als klassische Kontrolle
für spätere, begründete Mechanismen wiederverwendbar.

## Artefakte und Wiederholung

[PROTOCOL.md](PROTOCOL.md) enthält den vorab festgelegten Plan. [results.json](results.json)
enthält alle Zusammenfassungen und Tests; `runs.jsonl` die einzelnen Messungen und
Zertifikate. `precision_results.json` und `selection_results.json` dokumentieren
Stabilität und Spielraum der digitalen Auswahl.

```sh
python3 make_inputs.py
python3 engine_arithmetic.py
python3 analyze.py
python3 -m unittest discover -p 'test_arithmetic.py' -v
python3 precision_audit.py
python3 selection_audit.py
python3 write_report.py
```

Python benötigt numpy, sympy und mpmath; matplotlib nur für den Bericht. Der
unveränderte Kern und die geprüften Zifferndateien aus den vorherigen Versuchen
werden relativ zum Experimentordner geladen. Keine anderen Theorie-, Queue-,
Paper- oder Website-Dateien wurden verändert. Ergebnisse lokal; kein Commit/Push.
'''
(R/'README.md').write_text(text)
fig,axes=plt.subplots(1,2,figsize=(11,4.7),layout='constrained')
methods=['sequential','exact_cofactor','phase8','bucket_pi','bucket_random0'];labels=['Fortlaufend','Kleiner Kofaktor','π-Phasenfilter','Kofaktor + π-Ziffern','Kofaktor + Zufall'];colors=['#64748b','#0d9488','#8b5cf6','#2563eb','#94a3b8']
y=np.arange(len(methods))
for ax,field,title,unit in [(axes[0],'factor_successes','Mehr gelöste Eingaben','Faktorisierungen von 64'),(axes[1],'amortized_total_seconds','Zusätzliche Arbeit bleibt sichtbar','Sekunden inkl. anteiliger Vorbereitung')]:
 vals=[v[m][field] for m in methods];ax.barh(y,vals,color=colors);ax.set_yticks(y,labels if ax==axes[0] else []);ax.invert_yaxis();ax.set_title(title,loc='left',weight='bold');ax.set_xlabel(unit);ax.spines[['top','right']].set_visible(False)
 for yy,val in zip(y,vals):ax.text(val+.015 if field.endswith('seconds') else val+.3,yy,f'{val:.2f}' if field.endswith('seconds') else str(val),va='center',fontsize=9)
axes[0].set_xlim(0,68);axes[1].set_xlim(0,3.3)
fig.savefig(R/'comparison.png',dpi=180);fig.savefig(R/'comparison.svg');plt.close(fig)
print('report written')
