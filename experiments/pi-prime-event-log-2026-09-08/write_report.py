"""Render the finite research report from recorded results."""
import json,hashlib,subprocess,math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
load=lambda f:json.loads((R/f).read_text())
p=load('primary_results.json'); rev=load('reverse_results.json');fac=load('factor_results.json');full=load('full_block_results.json');ver=load('verification.json')
repo=R.parents[1]
source_names=['rh/catalog/analysis/pi_prime_correlations.md','verification/v942_pi_pattern_transfer_specificity.py','_newest/RH_Tagesbilanz_2026-09-05.md','experiments/tfpt-discovery/regulator_relation_result.json','experiments/theory-contracts/second-matter-round50/validation.json','experiments/theory-contracts/charged-cocycle-lift/README.md']
provenance={'git_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip(),'sources':{f:hashlib.sha256((repo/f).read_bytes()).hexdigest() for f in source_names},'boundary':'Current working tree read on 2026-09-08; theory rounds above 27 are local uncommitted work. Historical verifiers not rerun; their recorded results are cited as historical.'}
(R/'source_manifest.json').write_text(json.dumps(provenance,indent=2)+'\n')
rows=p['tests']['pi'];lookup={r['name']:r for r in rows}
text='''# π und Primzahlen als Ereignislog — neue automatisierte Untersuchung

Stand: 8. September 2026. **Ergebnis: In den untersuchten Regeln kein belastbares
zusätzliches Primzahlsignal und kein Faktorisierungsvorteil.** Die Untersuchung
liefert einen reproduzierbaren Datensatz, eine exakte Erklärung einer sehr starken
Scheinkorrelation und konkrete Grenzen für die nächste Forschungsfrage.
Keine Aussage für oder gegen RH; kein Normalitätsbeweis; kein allgemeiner
Unmöglichkeitsbeweis für Beziehungen zwischen π-Ziffern und Primzahlen.

## Was konkret gerechnet wurde

Zwei Millionen Nachkommastellen jeweils von π, e und √2; π erneut mit höherer
Präzision gerechnet und die erste Million vollständig mit dem veröffentlichten
[Angio-Datensatz](https://assets.angio.net/pi1000000.txt) verglichen. Beide Vergleiche
sind identisch. Hashes und Rechenzeiten stehen in `data_manifest.json`.

Index 1 ist die erste Nachkommastelle, also die 1 von 3.14159. Die führende 3 zählt
nicht. Führende Nullen bleiben in Blöcken erhalten. Zwei Interpretationen:

- B_p = d_p … d_(2p−1): p Ziffern ab Primzahlposition p.
- C_p = d_p … d_(p+ell(p)−1): so viele Ziffern wie die Dezimaldarstellung von p.

Die Hauptmessung umfasst 22.044 Primzahlen p≤250.000 und eine spätere Gegenprüfung
mit 29.400 Primzahlen 600.001≤p≤1.000.000. Auch die VOLLEN langen Blöcke der beiden
Gruppen greifen auf getrennte Ziffernbereiche zu. Die Gegenprüfung ist intern und
vor der neuen Rechnung festgelegt; π ist eine bekannte deterministische Konstante,
kein im wörtlichen Sinn zufällig gezogenes unabhängiges Experiment.

Pro Bereich 15 Messgrößen: Ziffernverteilung, Primlücke, mod-4-Klassen, lange
Blocksummen und deren Restklassen, kurze Blockzahlen, sechsstellige Primzahlen,
umgekehrte Wert/Positions-Korrelation und Selbstverweise. Die sechsstellige Regel
prüft ALLE entsprechenden Werte an den geprüften Positionen, nicht nur ausgesuchte
Internetmuster. Jede Messung läuft durch dieselbe Pipeline auf 1.999 vollständigen
Zufallsziffernfolgen, einschließlich aller Überlappungen. Holm-Korrektur über die
30 primären π-Tests; e/√2 sind deskriptive Vergleichsdatensätze.

## Primäre Ergebnisse

Der kleinste rohe π-p-Wert ist **0,065**. Alle 30 Holm-korrigierten Werte sind 1.
Das bedeutet fehlende Auffälligkeit in dieser Testfamilie, nicht bewiesene
Unabhängigkeit. Ein künstliches Signal (Ziffer 9 an Primzahlpositionen) wird in
beiden Bereichen erkannt, sogar nach Holm: jeweils p=0,03. Das belegt Empfindlichkeit
für diesen starken Effekt, keine umfassende Poweranalyse für subtile Mechanismen.

| Messung | Früher Bereich: Wert / rohes p | Später Bereich: Wert / rohes p |
|---|---:|---:|
'''
for key,label in [('prime_digit_mean','Mittlere Ziffer an Primzahlposition'),('gap_digit_correlation','Korrelation Ziffer / nächste Primlücke'),('long_block_z_mean','Mittlere normalisierte lange Blocksumme'),('short_block_prime','Primzahlanteil in C_p'),('six_prime_rate_excess','Sechsziffern-Primanteil: Primposition minus alle Positionen'),('reverse_prime_chi4_correlation','χ₋₄: extrahierter Primwert / Primposition')]:
 a=lookup['discovery.'+key];b=lookup['validation.'+key]
 text+=f"| {label} | {a['observed']:.8g} / {a['p']:.3f} | {b['observed']:.8g} / {b['p']:.3f} |\n"
text+='''
Die vollständigen Ergebnisse, einschließlich aller Kontrollen und Nullstreuungen,
stehen in `primary_results.json` und `null_metrics.npz`. Die Rohmessungen in e und
√2 können ebenfalls gelegentlich klein ausfallende p-Werte produzieren; auch dort
überlebt in dieser Familie nichts die jeweilige Holm-Korrektur.

## Der wichtigste strukturelle Befund: Die Ausleseregel baut Korrelation ein

Für unabhängige uniforme Ziffern X_i haben die Summen S_p über B_p exakt

    Cov(S_p, S_q) = 8,25 · |[p,2p−1] ∩ [q,2q−1]|.

Mit Z_p=(S_p−4,5p)/sqrt(8,25p) folgt

    Corr(Z_p,Z_q) = Überlappung / sqrt(pq).

Bei p=101 und q=103 sind 99 Ziffern gemeinsam. Die Korrelation beträgt daher
**0,9706348836**, obwohl die Ziffern in diesem Modell vollkommen unabhängig sind.
Für q=p+g<2p gilt (p−g)/sqrt(p(p+g), asymptotisch 1−3g/(2p).
Eine glatte Kurve oder sehr hohe Nachbarblock-Korrelation ist deshalb ohne weitere
Kontrolle bereits eine Eigenschaft der Ausleseregel. Sie ist keine neue Eigenschaft
von π. Die Formel wurde außerdem über eine unabhängig gebaute Inzidenzmatrix geprüft.

![Überlappung und Messungen](analysis.png)

Die Ausleseregel kann als Inzidenzmatrix A der Primzahlfenster formuliert werden:
S=A d. Schon AAᵀ trägt die Primzahlabstände. Wer daraus Primstruktur zurückliest,
kann also die selbst eingespeisten Primzahlpositionen wiederentdecken. Das schließt
einen zusätzlichen Effekt in d nicht aus; genau diesen müsste ein Residuum gegen
das vollständige A-basierte Nullmodell zeigen.

## Die vollständigen p-stelligen Zahlen

Zusatzuntersuchung, klar getrennt von der primären Testfamilie: alle 168 Primzahlen
p≤997, mit 999 vollständigen Zufallsfolgen als Kontrolle. Die beiden primen π-Blöcke:

| p | Voller B_p | Status |
|---:|---:|---|
| 2 | 41 | prim |
| 7 | 6535897 | prim |

Alle übrigen getesteten π-Blöcke sind zusammengesetzt. Die allgemeine Routine
unterscheidet bewiesene und wahrscheinliche Primzahlen; beide tatsächlichen Treffer
haben GMP-Status 2 (definitiv prim). Der Nullmittelwert liegt bei 1,067 Treffern,
das zentrale 95%-Intervall bei 0 bis 3; für die beobachteten zwei Treffer p=0,564.
Nur bei p=3 und p=97 ist B_p durch p teilbar; auch das ist unauffällig (p=1).
Hier wird kein Primzahltest für sämtliche millionenstelligen B_p behauptet.

## Rückwärts von bekannten Ziffernfolgen zur Arithmetik

Die [Pi-Search Page](https://www.angio.net/pi/) dokumentiert Selbstverweise und
Suchketten. Die [Irrational Numbers Search Engine](https://www.subidiom.com/pi/)
bietet laut ihrer Oberfläche je zwei Milliarden Ziffern von π/e/√2 an. Diese
Dienste wurden als Quellen geprüft; die Messungen erfolgten lokal auf zwei Millionen
Ziffern. Der größere Webseitenbestand wurde nicht als durchsuchter Datensatz ausgegeben.

| Folge | Erste Position im lokalen Datensatz | Anzahl überlappender Treffer | Davon an Primpositionen |
|---|---:|---:|---:|
'''
for word in ['999999','888888','235711','112358','314159','16470','44899','424242','240','480','1024','65536','1048576','123456','0123456789']:
 a=next(a for a in rev['catalog'] if a['word']==word)
 text+=f"| `{word}` | {a['first'] or 'nicht im Bereich'} | {a['count']} | {a['prime_positions']} |\n"
text+='''
Alle 27 vorab benannten Folgen wurden gegen 9.999 Verschiebungen der Primpositionsmaske
geprüft, bei erhaltenen Abständen zwischen ihren Treffern. Keine korrigierte
Primpositionsanreicherung. Die historischen Folgen sind bereits nach Auffälligkeit
in π ausgesucht: Dieser Auswahlbias verschwindet durch Holm nicht. Die Verschiebung
ist ein endliches Alignment-Nullmodell, kein Satz über die stationäre Primverteilung.
Die Faktoren jeder ersten Fundposition und sämtliche Treffer stehen in `reverse_results.json`.

**Selbstverweise:** Vollständiger Scan ergibt 1, 16470 und 44899. Dabei
16470=2·3³·5·61 und 44899=59·761; 1 ist ebenfalls keine Primzahl.
Ein Selbstverweis bedeutet nicht erste Fundstelle: „16470“ steht schon bei 1602,
„44899“ schon bei 13714. Diese beiden Begriffe werden auf Musterseiten leicht vermischt.
Unter unabhängigen Uniformziffern ist die erwartete Zahl primer Selbstpositionen
bis zwei Millionen exakt Σ_(p≤2M)10^(−ell(p)) ≈ 1,01868. Null beobachtete Treffer
sind daher keine Überraschung. Für alle k-stelligen Positionen erwartet man grob
0,9 Selbsttreffer pro vollständiger Größenordnung, nicht exponentiell viele.

**Suchketten:** Die erste Fundstelle von 169 ist 40, von 40 ist sie 70, und so weiter;
der bekannte 20er-Zyklus wird exakt reproduziert. 211→93→14→1→1 landet in einem
Fixpunkt. Für jede Bahn einer endlichen, überall definierten Selbstabbildung muss
irgendwann ein Zyklus entstehen. Unsere begrenzte Suche kann außerdem am Datenrand
enden. Das Vorhandensein eines Zyklus allein liefert somit keinen Primmechanismus.

**Indexkorrektur:** Die Anekdote zu „424242“ nennt auf Angio 242423. Unsere mit Angios
Millionendatei vollständig abgeglichene Rechnung findet bei der dort angegebenen
einsbasierten Nachkommazählung bereits **242422**. Gerade hier ist ein Positionsversatz
arithmetisch entscheidend; keine nachträglichen ±1-Korrekturen zur Erzeugung von Mustern.

## Abgleich mit dem aktuellen Forschungsstand

- **Frühere π-Arbeit:** `pi_prime_correlations.md` prüfte 100.000 Ziffern mit einem
  negativen Befund. r184/v942 dokumentiert darüber hinaus fünf π-basierte Ereignisfolgen,
  einschließlich Kettenbrüchen und BBP, ohne primespezifische Detektorauffälligkeit.
  Diese historischen Läufe wurden hier in den Quellen geprüft, nicht erneut ausgeführt.
- **RH:** Der aktuelle All-place/Tate-Bericht isoliert den Zeta-Faktor, lässt aber
  die globale Tate–Weil-Realisierung und unabhängige Positivität offen. Ein endlicher
  Ziffernscan liefert diese fehlenden Objekte nicht. Die RH bleibt auch nach dem
  [Clay-Status](https://www.claymath.org/problem/unsolved/) ungelöst.
- **Faktorisierung:** r643 weist den bedingten Sprung bei bekanntem Regulator nach.
  Der neuere r644 liefert `RELATIONS_RECOVER_REGULATOR_BASELINE`: Regulatorgewinnung
  über glatte Relationen und ganzzahlige Abhängigkeiten, als bekannter SIQS/Buchmann-
  Mechanismus klassifiziert. Die [Arbeit von Murru/Salvatori, v2 Januar 2025](https://arxiv.org/abs/2409.03486v2)
  macht die Zusatzinformation des Regulators ausdrücklich sichtbar.
- **Allgemeine Theorie bis 8. September:** Die lokalen Round50-Artefakte behalten
  Frequenzen mit ihren Strompräfixen gepaart und erhalten Vorzeichen; die neue
  geladene Kokzykelarbeit zeigt fehlende Zeicheninformation in einem gröberen
  Compilerquotienten. Für diese π-Untersuchung ist das eine methodische Lehre:
  Position, Wert, Vorzeichen, Reihenfolge und verlorene Information müssen explizit
  bleiben. Es entsteht daraus noch keine Herleitung einer Dezimalcodierung.
  Round50 ist lokale, teilweise bedingte NON-RH-Forschung, keine geschlossene TOE.

Gezielter externer Aktualitätsabgleich: [Guth–Maynard, April-2026-Version](https://arxiv.org/abs/2405.20552v2)
verbessert Nullstellendichten und Primzahlen in kurzen Intervallen; die Arbeit ist
2026 in den Annals erschienen. [Kahanamoku-Meyer/Ragavan/Van Kirk, Juli-2026-Version](https://arxiv.org/abs/2510.08432v3)
verbessert Ressourcen für Regevs Quantenfaktorisierung. Beide Fortschritte wurden auf
Relevanz geprüft; keiner liefert in der geprüften Darstellung einen π-Dezimaldecoder.
Dies ist ein gezielter Quellenabgleich, keine erschöpfende Sichtung sämtlicher
2026-Preprints oder Prüfung jeder behaupteten RH-Lösung.

## Faktorisierungsprobe mit ausschließlich N als Eingang

200 feste kleine Semiprime in den angeforderten Größenklassen 16–24 Bit (193
verschiedene N), je 32 sechsstellige Kandidaten aus π. Die Ausleseadresse benutzt
nur N und feste öffentliche Konstanten. Die Faktoren werden nur zur Erstellung und
Kontrolle der Testdaten verwendet. Verglichen werden exakt dieselben Adressen in
e, √2 und 999 vollständigen Zufallsströmen; doppelte N und überlappende Lesezugriffe
bleiben im endgültigen Nullmodell erhalten.

| Ziffernquelle | Eingaben mit gefundenem nichttrivialem Faktor |
|---|---:|
'''
for k in ['pi','e','sqrt2']:text+=f"| {k} | {fac[k]['successes']}/200 |\n"
text+=f"| Zufallsmodell, Mittel | {fac['null_mean']:.2f}/200 |\n"
text+='''
π verbessert diesen eingefrorenen ggT-Versuch nicht: einseitiges p für einen
Vorteil 0,995. Die geringe π-Ausbeute ist keine allgemeine Aussage, π sei als
Zufallsquelle schlechter; es ist eine einzelne begrenzte Testfamilie mit kleinen
Faktoren. Dies ist auch kein Lauf des Regulatoralgorithmus, keine RSA-Demonstration
und kein Nachweis einer asymptotischen Komplexität. Digitgenerierung, Adressregel,
Datenumfang und Zufallskosten sind mitprotokolliert.

## Wo die echte π–Prim-Verbindung liegt und welches neue Ergebnis zählen würde

Klassisch bestimmt das Eulerprodukt π über ζ(2)=π²/6; siehe
[NIST DLMF](https://dlmf.nist.gov/25.6). Die vollständige Zeta-Funktion enthält
π^(−s/2)Γ(s/2), siehe [DLMF 25.4](https://dlmf.nist.gov/25.4).
Numerisch liefert unser endliches ζ(2)-Produkt über Primzahlen bis eine Million
π≈3,1415925471279884. Das χ₋₄-Produkt liefert π≈3,141599411556697.
Das sind klassische positive Verbindungen, keine neuen Dezimalmuster.

Der mathematisch passende Ereignislog zur expliziten Formel besteht aus Ereignissen
bei k·log(p) mit Gewichten log(p), nicht allein aus ungewichteten Dezimalpositionen.
π gehört dort zur reellen/Fourier-/Gamma-Normalisierung. Eine neue Brücke müsste
nachweisen, wie ein π-Auslesemechanismus diese **Gewichte und multiplikativen
Beziehungen** ohne vorher eingespeiste Primantwort erhält. Die BBP-Formel extrahiert
binäre/hexadezimale π-Ziffern effizient im Speicher; sie liefert keine solche Brücke
([Originalarbeit](https://www.davidhbailey.com/dhbpapers/digits.pdf)).

Auch rechnerisch ist eine Grenze relevant: Wer einen Block von p Ziffern explizit
ausgibt, benötigt mindestens Ω(p) Ausgabearbeit, also exponentiell in der Bitlänge
von p. Für eine Faktorisierungsabkürzung muss eine kleine benötigte Funktion des
Blocks direkt berechnet werden. Unsere Summen benutzen deshalb Präfixsummen statt
sämtliche überlappenden Blöcke zu materialisieren. Dass π berechenbar ist, verbietet
keinen algorithmischen Vorteil; es stellt aber keinen kostenlosen neuen Oracle dar.

**Nächstes sinnvolles Gate:** Eine einzige konkrete Regel aus π und N muss eine
zuvor unbekannte regulatorbezogene Größe oder eine nichttriviale Kongruenz liefern,
dann auf neuen Semiprimen mit vollständigen Erzeugungs-/Suchkosten gegen gleiche
Zufallsbudgets bestehen. Für einen reinen Ziffernbefund wäre zuvor ein eingefrorener
Effekt mit Replikation in einem neuen, größeren Bereich nötig. Aktuell überlebt
keine der getesteten π-Regeln dieses vorgelagerte Signal-Gate.

## Reproduktion und Grenzen

Abhängigkeiten: Python, numpy, gmpy2, sympy; matplotlib nur für diesen Bericht.
Keine Änderungen an bestehenden Theorie-/Queue-/Paper-Dateien. Ergebnisse sind
lokale Forschungsartefakte. `source_manifest.json` enthält HEAD und Quellenhashes.

```sh
python3 probe.py
python3 supplement.py
python3 audit_resolution.py
python3 audit.py
python3 write_report.py
```

Diese Sitzung benutzte die vorhandenen Python-Pakete und gmpy2 separat unter
`/tmp/tfpt-pi-event-deps`; entsprechend `PYTHONPATH=/tmp/tfpt-pi-event-deps` setzen,
oder gmpy2 in der eigenen Forschungsumgebung installieren. `--reuse-data` spart
Neuberechnung/Download vorhandener Zifferndateien. Datenfiles werden vor Benutzung
über die separate Auditprüfung verifiziert; bei frischer Erzeugung außerdem über
Präzisionswiederholung und externen Millionenziffernvergleich.

63 unabhängige Checks prüfen Sieve gegen Sympy, direkte Stringauslese gegen die
Vektorrechnung, exakte χ₋₄-Behandlung inklusive p=2, Primtests, Kovarianzmatrix,
Testdaten und Hashes. Zusätzlich wird die Auflösung der Monte-Carlo-Korrektur geprüft.
Der erste 999-Lauf hatte eine zu grobe minimale zweiseitige p-Auflösung für 30 Holm-
Tests; die Erhöhung auf 1.999, eine korrekte χ₋₄(2)-Behandlung und das überlappungstreue
Faktorisierungsnullmodell sind offen in `PROTOCOL.md` dokumentiert. Vorläufige
Resultate bleiben in `preliminary_999/`; maßgeblich sind die finalen Dateien im
Hauptordner. Keine nachträgliche Auswahl eines vorteilhaften π-Signals.

Normalität von π ist nicht bewiesen; endliche Zufallstests ersetzen diesen Beweis
nicht ([Bailey et al., Normality and the Digits of π](https://www.davidhbailey.com/dhbpapers/normality-digits-pi.pdf)).
Dezimalbasis, endlicher Datenumfang, kleine Faktorinputs und begrenzte Testfamilie
sind die Reichweitengrenzen der vorliegenden Untersuchung.
'''
# Fix displayed parenthesis explicitly.
text=text.replace('(p−g)/sqrt(p(p+g),','(p−g)/sqrt(p(p+g)),')
(R/'README.md').write_text(text)
# Standalone scientific chart using real recorded Monte Carlo outputs.
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})
fig,axes=plt.subplots(1,2,figsize=(12,4.8),layout='constrained')
ax=axes[0]
ax.broken_barh([(101,101)],(1.2,.5),facecolors='#2563eb',alpha=.8)
ax.broken_barh([(103,103)],(.3,.5),facecolors='#0d9488',alpha=.8)
ax.axvspan(103,202,alpha=.1,color='#111827')
ax.set_xlim(95,213);ax.set_ylim(0,2);ax.set_yticks([1.45,.55],['p = 101','q = 103']);ax.set_xlabel('Position nach dem Dezimalpunkt')
ax.set_title('99 gemeinsame Ziffern erzeugen r = 0,9706\nBereits bei unabhängigen Zufallsziffern',loc='left',weight='bold')
null=np.load(R/'null_metrics.npz')['values'];ax=axes[1]
indices=[4,19]
for j,index in enumerate(indices):
 vals=null[:,index];lo,hi=np.quantile(vals,[.025,.975]);med=np.median(vals)
 ax.plot([lo,hi],[j,j],lw=13,color='#cbd5e1',solid_capstyle='round',label='95 % des Nullmodells' if j==0 else None)
 ax.plot(med,j,'|',color='black',markersize=16)
 for kind,color,delta in [('pi','#2563eb',-.1),('e','#e87924',0),('sqrt2','#0d9488',.1)]:
  ob=p['tests'][kind][index]['observed'];ax.plot(ob,j+delta,'o',color=color,label={'pi':'π','e':'e','sqrt2':'√2'}[kind] if j==0 else None)
ax.set_yticks([0,1],['Früher Bereich','Später Bereich']);ax.set_ylim(-.5,1.5);ax.set_xlabel('Mittlere normalisierte lange Blocksumme')
ax.set_title('π-Blocksummen liegen im Zufallsbereich\n1.999 vollständig ausgewertete Nullfolgen',loc='left',weight='bold');ax.legend(frameon=False,fontsize=9)
for ax in axes:
 ax.spines[['top','right']].set_visible(False)
fig.savefig(R/'analysis.png',dpi=180);fig.savefig(R/'analysis.svg');plt.close(fig)
print('report and figures written')
