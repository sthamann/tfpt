# Neue exakte Spektralsätze für das lokale trunkierte C16-Modell

14. September 2026. Dieses Verzeichnis gehört ausschließlich zum neuen Audit.
Keine fremden Dateien wurden geändert, keine Commits erstellt. Die vier
gelieferten Texte wurden hinsichtlich ihrer Spektralpassagen vollständig
gelesen. Gegenstand ist ausschließlich

\[
H_0=20I+X/2,\quad X=\sum_{40\ \mathrm{Kanten}}S_e,\qquad
H_{\rm tr}=H_0+F_4/800,
\quad F_4=\sum_{v=1}^{16}A_v(A_v-I).
\]

Die Einheit ist J, und epsilon=t/Delta=1/20. Keine Aussage dieses Dokuments
kontrolliert den Schrieffer-Wolff-Rest oder bestimmt eine native Architektur.

## Ergebnis

Die zuvor fehlende **rigorose korrigierte Quartett-Obergrenze 12,45** ist jetzt
geschlossen. In den zwei kontrollierten Symmetriesektoren gilt, mit nach außen
gerundeten Dezimalgrenzen:

| Sektor | Multiplizitätsblock | Trägerdimension | Unterstes Niveau Htr/J | Untergrenze des zweiten Blockniveaus |
|---|---:|---:|---|---:|
| Trivial | 28 | 28 | (11,960507412; 11,960507414) | 14,558318450 |
| S5-Standard | 80 | 320 | [12,4469215409; 12,4470238436] | 14,011697122 |

`filtered_certificate.json` enthält die exakten rationalen Grenzen. Für den
trivialen Block ist zusätzlich das ganze korrigierte Polynom zertifiziert;
seine exakten Wurzelzählungen verbessern das Momentenintervall. Diese
Dezimalanzeigen sind keine aus Gleitkomma-Eigenwerten hochgestuften Zertifikate.
Die Zahlen folgen aus exakt rekonstruierten ganzzahligen Spuren und einer
bewiesenen zweiten Eigenwertschwelle.

Im **348-dimensionalen direkten Summenraum** aus trivialem und Standardsektor
liegen daher zuerst ein einfaches Niveau und danach ein exakt vierfaches
Niveau. Ihr Abstand ist rigoros größer als

\[
0.4864141269280\,J.
\]

Im Standard-Multiplizitätsblock liegt das nächste Niveau mehr als
1,5646732784 J über seinem Minimum. Die korrigierten charakteristischen
Polynome beider kleinen Blöcke sind modulo 99999989 quadratfrei. Damit sind
bei diesem festgelegten epsilon sogar **alle 28 beziehungsweise 80
Multiplizitäts-Eigenwerte einfach** in Charakteristik null.

Das ist noch keine globale Spektralordnung: Die übrigen 16 Singuletttypen und
sämtliche Nichtsingulettsektoren können durch diesen Satz nicht ausgeschlossen
werden.

## 1. Die neuen Texte: Was bestätigt wird

Eine unabhängige Hook-/Verzweigungsrechnung ergibt für den sechsstelligen
physischen SU(4)-Stern A=5I-J6 exakt

| A-Eigenwert | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Multiplizität | 84 | 560 | 1050 | 360 | 250 | 912 | 190 | 600 | 90 |

Die Summe beträgt 4096. Die behaupteten physischen Schranken

\[
0\le F_4\le896I,\quad F_4\le1120I-28H_0,
\]

\[
F_4\ge1248I-48H_0,\qquad F_4\ge1344I-56H_0
\]

sind korrekt. Die erste affine Untergrenze liefert die in `neu_1.md`
verwendete Gerade 47 H0/50+39/25. Die zweite liefert die in `BEWEISE.md`
verwendete, unterhalb H0=12 stärkere Gerade 93 H0/100+42/25.

Das lokale Spektrum ist ein vollständiger exakter Darstellungssatz, keine
Eigenwertstichprobe. Mit fünf Farben kommt A=9 vor: Die Negativkontrolle
verhindert eine Übertragung der SU(4)-Grenze auf beliebige Farbdimension.

## 2. Zusätzliche Singulettschranke, die in den neuen Texten fehlte

Im Spechtmodul (4,4,4,4) können bei Einschränkung auf eine sechstellige
Permutationsuntergruppe nur Youngformen auftreten, die im 4x4-Quadrat liegen.
Der zuletzt entfernbare Kasten hat daher Inhalt zwischen -3 und +3. Nach
Konjugation gilt dies für jeden Stern. Somit gilt im ganzen Singulett

\[
\operatorname{spec}A_v\subseteq\{2,3,4,5,6,7,8\}.
\]

Für 2<=a<=8 ist a(a-1)<=9a-16. Summation liefert den neuen Satz

\[
\boxed{F_4\le1184I-36H_0\quad\text{im gesamten SU(4)-Singulett}.}
\]

Insbesondere 8I<=H0<=32I und 0<=800Htr<=26496I. Die Singulettschranke ist
keine Vollraumschranke: Bei a=0 scheitert der verwendete Skalarvergleich,
was als Negativkontrolle ausdrücklich getestet wird.

Schon ohne neue F4-Matrizen ergeben diese Schranken aus den in v1.5 exakt
isolierten ersten zwei Standardblock-Eigenwerten:

\[
12.43243877346<E_{\mathrm{std},0}^{\rm tr}<12.521482827465,
\]

\[
E_{\mathrm{std},1}^{\rm tr}>14.011697122,
\quad g_{\mathrm{std}}^{\rm tr}>1.490214294535.
\]

Hier werden einzelne affine Operatorvergleiche mit dem Min-Max-Satz
angewandt. Es wird kein unzulässiges punktweises Maximum nichtkommutierender
Operatoren gebildet. Selbst die reine Normschranke 896 hätte die in v1.5
offene epsilon=1/20-Einfachheit bereits mit Gap >0,564724177 geschlossen.

## 3. Die 28D- und 80D-Matrizen sind jetzt konkret aufgebaut

`checker.py` verwendet die unabhängig erzeugte rationale seminormale
Youngdarstellung aus v1.5. Für den trivialen Block wird PT PS5 verwendet,
für den Standardblock PT(PS4-PS5). Die Dimensionen 28 und 80 stammen aus der
bereits exakten ganzzahligen Charakterrechnung; exakte modulare Pivots
zertifizieren den Rang der konstruierten Basis.

Auf jeder Basisspalte werden die Gruppenfixbedingungen und anschließend

\[
XB=B X_{\rm red},\qquad F_4B=B F_{4,\rm red}
\]

an **allen 24024 mal 28 beziehungsweise 24024 mal 80 Einträgen** geprüft.
Für F4 wird die unabhängig ausgeschriebene Identität

\[
F_4=320I-18X+\sum_v B_v^2,\qquad B_v=\sum_{e\ni v}S_e
\]

verwendet. Die Dateien `modular_*.json` enthalten die vollständigen kleinen
Matrizen X, F4 und T=800Htr in jedem verwendeten endlichen Körper. Ihr
charakteristisches Polynom wird mit Newton-Identitäten berechnet und durch
Cayley-Hamilton geprüft. Ein absichtlich veränderter F4-Matrixeintrag wird
vom vollständigen Intertwinercheck zurückgewiesen.

Die quadratfreien T-Polynome modulo 99999989 beweisen die Einfachheit in
Charakteristik null: Ein mehrfacher rationaler Faktor kann bei einer guten
Primzahl nicht quadratfrei werden. Die rationalen Projektoren und die
modular invertierbaren Basispivots sichern, dass der richtige Block reduziert
wird. Das Vierfachsein folgt zusätzlich aus der Standard-Irrep-Dimension 4.

Der triviale nackte 28D-Block ist ebenfalls neu exakt zertifiziert:
`exact_trivial_H0.json` enthält sein durch CRT rekonstruiertes ganzzahliges
Polynom und rationale Wurzelzählungen für seine ersten beiden Niveaus.

Auch das **vollständige korrigierte 28D-Polynom** ist in `exact_trivial.json`
rekonstruiert: 16 Primzahlen ergeben 426 Bits und überschreiten die vorab
bewiesene 413-Bit-Koeffizientengrenze. Eine 17. unbenutzte Primzahl bestätigt
alle Koeffizienten. Die exakte Verfeinerung in `filtered_certificate.py`
isoliert das Minimum in (11,960507412; 11,960507414) und das zweite Niveau
in (14,558318450; 14,558318452).

## 4. Exakte enge Intervalle ohne vollständiges 80D-Polynom

Das Verfahren in `filtered_certificate.py` benutzt

\[
W=16^{20}T_{20}((X-2I)/16),\qquad T=800H_{\rm tr}.
\]

W ist ein ganzzahliges Polynom in X: W0=I, W1=X-2I und
W(k+1)=2(X-2I)W(k)-256W(k-1). Es werden exakt rekonstruiert:

\[
D=\operatorname{tr}W^2,\quad N=\operatorname{tr}(W^2T),\quad
N_2=\operatorname{tr}(W^2T^2).
\]

Diese Spuren sind ganze Zahlen, weil ganzzahlige Gruppenalgebraoperatoren
das Schnittgitter eines rationalen invarianten Raums mit einem ganzzahligen
Spechtgitter erhalten. Die bereits exakt rekonstruierten X-Polynome beweisen
||X||<18 auf beiden Räumen. Daher ||X-2I||<20 und ||W||<=32^20. Die vorab
bewiesenen Rekonstruktionsgrenzen lauten

\[
|D|\le n32^{40},\quad |N|\le n32^{40}26496,\quad
|N_2|\le n32^{40}26496^2.
\]

**Neun Primzahlen** nahe 10^8 überschreiten zweimal alle diese Grenzen.
Die CRT-Rekonstruktion ist damit eindeutig. Eine **zehnte unbenutzte
Primzahl** bestätigt unabhängig D, N und N2. Ein veränderter Spurwert wird
von dieser Kontrolle zurückgewiesen.

W^2/D ist eine positive Dichtematrix. Mit

\[
\mu=N/(800D),\qquad v=N_2/(640000D)-\mu^2
\]

und einer bewiesenen Schranke L2<=lambda2 oberhalb mu gilt

\[
\mu-\frac{v}{L_2-\mu}\le\lambda_1\le\mu.
\]

Dies ist die Temple-Ungleichung auch für die positive spektrale Verteilung
einer Dichtematrix: (H-lambda1)(H-L2) ist positiv, sodass die Ungleichung nach
Spurbildung folgt. W muss mit Htr nicht kommutieren. Die Untergrenze für das
zweite korrigierte Niveau folgt zuvor aus der exakten nackten Wurzelzählung
und dem affinen Min-Max-Vergleich. Damit besteht kein Zirkelschluss.

Die engere 80D-Grenze ist somit ein exaktes Momentenzertifikat. Ein vollständiges
korrigiertes 80D-Polynom wurde nicht rekonstruiert und wird nicht behauptet.

## 5. Was der Nichtsingulettvergleich jetzt noch benötigt

Die Quartett-Obergrenze ist kein offener numerischer Vorbehalt mehr. Ein
noch zu beweisender Nichtsingulettbound H0>=11,6 würde jetzt rigoros

\[
H_{\rm tr}\ge12.468>12.4470238436
\]

liefern. Schon der in `BEWEISE.md` genannte schwächere nackte Bound
H0>=11,58 genügt: 0,93 mal 11,58+1,68=12,4494, also mehr als die nun bewiesene
Quartett-Obergrenze. **Dieser Nichtsingulettbound selbst bleibt unbewiesen.**

Auch dieser Erfolg würde die 16 anderen Singuletttypen noch nicht ersetzen.
Die Gleichheit vier geschützter Eigenwerte, die Einfachheit ihres
Multiplizitätsoperators, die Gesamtenergieordnung und die Übertragung auf die
volle Mikrodynamik sind vier verschiedene Beweispflichten. Hier wurden die
ersten beiden und eine Spektralordnung in 348 Dimensionen geschlossen.

## 6. Reproduktion und Status

Die gespeicherten modularen Matrizen gestatten die schnelle exakte Wiedergabe:

```text
/opt/homebrew/bin/python3 checker.py analytic
/opt/homebrew/bin/python3 filtered_certificate.py
/opt/homebrew/bin/python3 -O filtered_certificate.py
/opt/homebrew/bin/python3 checker.py crt --sector trivial
```

Neubau der orthogonalen numerischen Vergleichsblöcke und einzelner exakter
modularer Blöcke:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 checker.py floating
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 checker.py modular --prime 99999989
```

Die normale und optimierte Momentenausführung bestehen. Die Prüfer benutzen
explizite Fehlerbedingungen, keine durch Python -O entfernbaren Assertions.
Die numerischen Matrizen stehen separat in `floating.json`; sie bestätigen
die älteren Näherungswerte, sind aber nicht Grundlage der zertifizierten
Ungleichungen. Es gibt keine Lean-Kernprüfung. Die Zertifikate beruhen auf den
angegebenen Darstellungssätzen und überprüfbarer Ganzzahl-/Modulararithmetik.
