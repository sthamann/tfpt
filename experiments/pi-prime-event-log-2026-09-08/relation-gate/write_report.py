"""Write sourced finite-gate report and chart from recorded measurements."""
import json,math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
d=json.loads((R/'results.json').read_text());meta=json.loads((R/'runs.jsonl.meta.json').read_text());rows=[json.loads(x) for x in (R/'runs.jsonl').read_text().splitlines()]
s=d['summary'];v=s['validation']
rngsmooth=np.mean([v[f'random{j}']['smooth'] for j in range(5)]);rngsuccess=np.mean([v[f'random{j}']['factor_successes'] for j in range(5)])
text='''# Fortsetzung: Kann π aus N nützliche Faktorisierungsrelationen auswählen?

8. September 2026. **Die konkrete π-Regel liefert echte Quadratkongruenzen und
Faktorzerlegungen, aber keinen π-spezifischen Vorteil.** Das zuvor vorgeschlagene
Informations-Gate wurde durchgeführt. Alle drei vorab definierten Erfolgskriterien
werden verfehlt. Dieser Befund betrifft genau diese Regel und die getesteten Größen,
nicht jede denkbare π-basierte Rechnung.

## Eine feste Regel, ausschließlich N als arithmetischer Eingang

Für a=ceil(sqrt(N)) werden 65.536 mögliche Offsets j betrachtet. Der Kandidat ist
x=a+j, sein positiver quadratischer Rest Q=x²−N. Jedem j wird ein achtstelliger
π-Ziffernschlüssel zugeordnet, beginnend an der Adresse (N mod 2.000.000 + 8j)
modulo des bekannten Präfixes. Kleine Schlüssel werden zuerst gewählt; gleiche
Schlüssel behalten ihre ursprüngliche Reihenfolge. Die ersten 16.384 Kandidaten
werden exakt geprüft, ohne Vorwissen über ihre Glattheit.

Die Suche behält Q, wenn seine Primfaktoren vollständig in der festgelegten kleinen
Faktorbasis liegen. Lineare Algebra über den Exponenten modulo zwei kombiniert
solche Relationen. Bei geraden Exponentensummen gilt exakt

    X² ≡ Y² (mod N),  X = Produkt der ausgewählten x,
    Y = Quadratwurzel aus dem Produkt der zugehörigen Q.

Aus gcd(X−Y,N) oder gcd(X+Y,N) kann dann ein nichttrivialer Faktor entstehen.
π steuert nur die Kandidatenreihenfolge. Die eigentliche Quadratkongruenz ist
klassische Faktorisierungsarithmetik. Dies ist eine neue Prüfung dieser Auswahlregel,
kein neuer Satz über das quadratische Sieb.

`engine.py` läuft separat und liest nur die öffentliche N-Liste und die verifizierten
Ziffernpräfixe. `make_inputs.py` erzeugt die Testzahlen und eine getrennte Antwortdatei;
`analyze.py` liest diese erst bei der nachfolgenden Kontrolle. Das ist eine geprüfte
Programm-/Datenflussgrenze, keine Betriebssystem-Sandbox. Das Suchprogramm importiert
keinen Faktorisierungsdienst, keinen Regulator und keine Antwortdatei.

## Umfang und faire Kontrollen

128 neue, paarweise verschiedene ausgeglichene Semiprime mit genau 32, 40, 48 oder
56 Bit; keine Überschneidung mit dem früheren 16–24-Bit-ggT-Test. 64 Zahlen im ersten
Satz, 64 im vorab getrennten Validierungssatz, jeweils 16 pro Größe. Beide Sätze
wurden ohne zwischenzeitliche Anpassung vollständig ausgeführt.

Neun Varianten pro N: π, e, √2, fünf reproduzierbare Zufallsreihenfolgen sowie die
klassische fortlaufende Suche ab a. Alle verwenden dieselbe Faktorbasis, dieselbe
exakte Restprüfung, dieselbe Eliminierung und dasselbe Budget von 16.384 Kandidaten.
Die klassische Suche nimmt die ersten 16.384 Offsets aus demselben 65.536er Pool;
π und die Zufallskontrollen wählen über ihren Schlüssel. Alle Varianten laufen auch
nach einem ersten Faktor bis zum Budgetende weiter. Es gibt keine nachträgliche
Erweiterung der Faktorbasis, keine Large-prime-Variante und keine vollständige Suche
über alle Kombinationen der gefundenen linearen Abhängigkeiten.

## Ergebnis im getrennten Validierungssatz

| Variante | Vollständig glatte Relationen | Unabhängiger Exponentenrang | Zahlen mit Faktor |
|---|---:|---:|---:|
'''
for method,label in [('pi','π'),('e','e'),('sqrt2','√2'),('sequential','Klassisch fortlaufend')]:
 z=v[method];text+=f"| {label} | {z['smooth']:,} | {z['rank']:,} | {z['factor_successes']}/64 |\n"
text+=f"| Zufall: Mittel der fünf Läufe | {rngsmooth:.1f} | {np.mean([v[f'random{j}']['rank'] for j in range(5)]):.1f} | {rngsuccess:.1f}/64 |\n"
text+='''
Die einzelnen Zufallsläufe lösen 38, 39, 41, 40 beziehungsweise 39 der 64 Aufgaben.
π liegt mit 40 mitten in diesem Bereich. Im ersten Satz sind es bei π 39/64,
bei den Zufallsläufen 37–39/64 und bei der klassischen Reihenfolge 50/64.

![Erfolgreiche Faktorisierungen nach Eingabegröße](comparison.png)

| Vorab festgelegter Vergleich | Differenz glatter Relationen pro N | Einseitiges p | Holm-p |
|---|---:|---:|---:|
'''
for t in d['tests']:
 label=('Erster Satz' if t['split']=='discovery' else 'Validierung')+' / '+('Zufallsmittel' if t['control']=='random_mean' else 'klassisch')
 text+=f"| {label} | {t['mean_difference']:.4f} | {t['p_one_sided']:.5f} | {t['holm_p']:.2f} |\n"
text+='''
Die 19.999 gepaarten Vorzeichenpermutationen pro Vergleich benötigen eine
Symmetrie-/Austauschbarkeitsannahme für die Differenzen. π ist deterministisch;
die Zahlen sind aus einer festgelegten Generatorverteilung gewählt. Die p-Werte
sind daher begrenzte Modelltests, keine mathematischen Unabhängigkeitssätze.
Alle Einzelzeilen bleiben in `runs.jsonl` erhalten.

## Kosten statt kostenloser π-Vorbereitung

Im Validierungssatz benötigt π einschließlich des anteilig auf alle 128 Eingaben
verteilten Präfixaufbaus und Einlesens rund 1,815 Sekunden; die klassische Variante
rund 0,949 Sekunden. Ein Zufallslauf benötigt rund 1,140 Sekunden im Mittel. Diese
kleinen Zeiten hängen stark von Implementierung, Hardware und Laufreihenfolge ab;
sie sind keine universellen Benchmarks. Die Methodenreihenfolge rotiert pro N.

Der unabhängige Relationenrang pro so verrechneter Sekunde liegt bei π beim
**0,633-Fachen des Zufallswerts** und beim **0,439-Fachen des klassischen Werts**.
Die geforderte mindestens zweifache Verbesserung fehlt klar. Die zweite Rechnung
in `results.json` belastet jede einzelne Eingabe mit einem kompletten frischen
Präfixaufbau und fällt für π entsprechend ungünstiger aus.

Erfasst wurden Faktorbasiserzeugung, alle 65.536 Schlüssel einschließlich Sortierung,
exakte Prüfung der gewählten Kandidaten, lineare Algebra und ggT. Die früher gemessene
Erzeugung der zwei Millionen π-Ziffern wird mit 1,097 Sekunden angesetzt und aktuell
über den SHA-256-Hash verifiziert. Der tatsächliche Lauf aller 1.152 Varianten dauerte
rund 22 Sekunden ohne erneute Präfixberechnung. Datei-/Berichts-I/O gehört nicht zur
algorithmischen Durchsatzmessung; Laufzeitmetadaten und exakte Operationszähler sind
separat vorhanden. Speicher-, Bitkomplexität und der Vergleich mit optimiertem
QS/NFS sind nicht zertifiziert.

## Ein konkretes überprüftes Beispiel

Im Validierungssatz liefert die π-Reihenfolge unter anderem

    38.353.420.057.279.849 = 175.639.271 × 218.364.719.

37 glatte Relationen kombinieren sich hier beim ersten erfolgreichen Schritt zu

    X mod N = 22.835.559.743.939.767,
    Y mod N =  3.943.164.116.658.018.

Es gilt X²≡Y² mod N; gcd(X−Y,N)=175.639.271 und
gcd(X+Y,N)=218.364.719. Die erste erfolgreiche Kombination kommt nach 11.451
geprüften Kandidaten. Die vollständigen x- und Q-Listen stehen im Zertifikat
`validation-56-04` / `pi` in `runs.jsonl`. Dieser Erfolg bestätigt den ausgeführten
klassischen Rechenweg, nicht die Überlegenheit der π-Auswahl.

Alle **722 gespeicherten Erfolgszertifikate** aus sämtlichen Varianten wurden
unabhängig kontrolliert: Q=x²−N, exaktes Quadrat des Produkts aller Q, beide modularen
Werte, ggT und die Faktorzerlegung. **Keine falschen Faktoren.** Sieben zusätzliche
Tests vergleichen insbesondere vektorisierte Restzerlegung mit einer unabhängigen
skalaren Fassung, prüfen zyklische Ziffernadressen und gleiche Schlüssel und enthalten
eine kleine positive Faktorisierungskontrolle. Die Ausführungshashes passen zu Quelltext,
Eingaben und vorab festgelegtem Protokoll.

## Bedeutung für die ursprüngliche Frage und r644

Das Informations-Gate wird hier erstmals über ganze Relationenkombinationen bis zum
Faktor geprüft; es bleibt nicht beim früheren direkten ggT mit ausgelesenen Zahlen.
Es erzeugt neue experimentelle Daten, aber keinen Hinweis auf zusätzliche
π-spezifische arithmetische Information in dieser Regel.

Die π-Reihenfolge hängt hier nur von N mod 2.000.000 ab. Für N und N+2.000.000 ist
sie identisch, während die anschließenden Reste Q das volle N verwenden. Das begrenzt
die getestete Hypothese auf eine endliche Familie von π-basierten Auswahlmustern.
Es ist kein allgemeiner No-go für andere, stärker N-abhängige π-Verfahren.

Die fortlaufende Suche hält die Offsets und damit Q=x²−N systematisch kleiner.
Das erklärt plausibel ihre bessere Glattheitsausbeute; die exakte Monotonie von Q
ist dabei ein Satz, eine monotone Glattheit jedes einzelnen Q wäre es nicht.
π und die Zufallsreihenfolgen greifen typischerweise weiter in den Pool und liefern
nahezu dieselbe Ausbeute. Für einen nächsten Vorteil bräuchte man einen vorab
berechenbaren Bezug der Auswahl zur multiplikativen Struktur von Q.

r644 arbeitet mit **orientierten** Relationen und ganzzahligen Abhängigkeiten zur
Regulatorgewinnung. Hier werden Exponenten nur modulo zwei kombiniert; das reicht
für die verifizierten Quadratkongruenzen, rekonstruiert aber keinen Regulator.
Die neue Messung schließt daher weder den Regulator-Engpass noch eine RH- oder
all-place-Lücke. Der vorhandene r644-Skalierungsdatensatz zu 64/72/80 Bit wurde
als Kontext gelesen, nicht durch diesen kleineren Pi-Vergleich übertroffen oder
neu validiert. Die Originaldateien bleiben unverändert.

**Entscheidung:** Diese feste π-Schlüsselregel rechtfertigt keinen größeren
Faktorisierungslauf. Eine Fortsetzung müsste eine andere, ausdrücklich begründete
Kopplung zu N liefern; bloß mehr Ziffern oder mehr gleiche Zufallsreihenfolgen beheben
den hier fehlenden Vorteil nicht.

## Reproduktion

Vom Ordner dieses Berichts aus, mit Python, numpy und sympy:

```sh
python3 make_inputs.py
python3 engine.py
python3 analyze.py
python3 -m unittest discover -p 'test_engine.py' -v
python3 write_report.py
```

matplotlib wird nur für die Grafik gebraucht. Die vorhandenen drei Zifferndateien
im übergeordneten Ordner werden anhand ihres Manifests geprüft; sie stammen aus der
[ersten π-Untersuchung](../README.md). Das feste Protokoll steht in
[PROTOCOL.md](PROTOCOL.md), vollständige Messwerte in [results.json](results.json).
Neue Forschung lokal gespeichert; kein Commit, Push oder Eingriff in andere Arbeiten.
'''
(R/'README.md').write_text(text)
# Exportable comparison with seed variability, no confidence-interval claim.
fig,ax=plt.subplots(figsize=(9,4.6),layout='constrained');bits=[32,40,48,56];pos=np.arange(4);w=.24
counts=lambda m:[sum(x['factor_found'] for x in rows if x['method']==m and x['bits']==b) for b in bits]
pi=counts('pi');seq=counts('sequential');rnd=np.array([counts(f'random{j}') for j in range(5)]);mean=rnd.mean(axis=0)
ax.bar(pos-w,pi,w,label='π',color='#2563eb');ax.bar(pos,mean,w,label='Zufall: fünf Läufe',color='#94a3b8')
ax.errorbar(pos,mean,yerr=[mean-rnd.min(axis=0),rnd.max(axis=0)-mean],fmt='none',ecolor='#334155',capsize=4)
ax.bar(pos+w,seq,w,label='Klassisch fortlaufend',color='#0d9488')
ax.set_xticks(pos,[f'{b} Bit' for b in bits]);ax.set_ylim(0,34);ax.set_ylabel('Erfolgreiche Faktorisierungen von jeweils 32 Zahlen');ax.set_title('π liefert keinen Vorteil gegenüber gleicher Zufallsauswahl',loc='left',weight='bold');ax.legend(frameon=False,loc='upper right');ax.spines[['top','right']].set_visible(False)
fig.savefig(R/'comparison.png',dpi=180);fig.savefig(R/'comparison.svg');plt.close(fig)
print('report written')
