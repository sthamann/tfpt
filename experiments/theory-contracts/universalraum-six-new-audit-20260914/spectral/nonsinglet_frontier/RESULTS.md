# Nichtsingulett-Front: exakte lokale Casimir-Untergrenzen

## Gesicherter Stand

**58 der 63 Nichtsingulett-Youngtypen des C16-Modells sind exakt ausgeschlossen**
unterhalb von `H0/J = 579/50 = 11.58`. Dies ist ein neuer globaler
Darstellungssatz aus kleinen lokalen Spektren, keine Übernahme des numerischen
Nichtsingulett-Minimums `12.133537149...`.

Der Prüfer `checker.py certify` erzeugt `cluster_certificate.json`: 504 explizite
Guards, alle 15 physikalischen S8-Youngsektoren, größte Matrix 90D, vollständig
rationale Coxeter- und Casimir-Identitäten, ganzzahlige charakteristische
Polynome, exakte Sturmzählungen und eine absichtlich zu starke, verworfene
Untergrenze. `checker.py rows` erzeugt separat die exakte 64-Typen-Zählung.

`cluster_scout_8.json`, `cluster_scout_9.json` und `cluster_scout_10.json` sind
ausdrücklich **nur numerisches Scouting**. Sie besitzen keinen Zertifikatsstatus.
Der Achtplatzbeweis hängt nicht von ihren gerundeten Eigenwerten ab.

Die stärkere Neunplatzfassung in `cluster_certificate_9.json` ist ebenfalls
exakt fertig: 727 Guards, alle 18 lokalen S9-Typen, maximale Dimension 216.
Die abschließende Zehnplatzfassung in `cluster_certificate_10.json` ist ebenfalls
fertig: 1134 Guards, alle 23 lokalen S10-Typen, maximale Dimension 768.
Der unabhängige leichte Replay lief normal und zusätzlich unter `python -O`
jeweils mit 298 aktiven Guards für alle drei abgeschlossenen Zertifikate.
Es laufen keine eigenen Prüfer mehr. Auf ausdrücklichen Wunsch wird keine
weitere Clustervergrößerung oder Spektralsuche begonnen.

## 1. Sofortiger Ausschluss der 30 Typen mit höchstens drei Zeilen

Es seien `X = sum_edges S_ij`, `H0/J = 20 I + X/2` und `r` die Zeilenzahl von
`lambda`. Jeder Grad-5-Stern `B_v = sum_(j~v) S_vj` ist konjugiert zu einem
Jucys–Murphy-Element `J6`. Bei Restriktion auf die sechs beteiligten Plätze kommen
nur Youngformen `nu` mit `nu subset lambda` vor. Die Eigenwerte sind Inhalte
der zuletzt entfernten Ecke; sie sind mindestens `1-r`.

Aus `sum_v B_v = 2X` folgt damit exakt

`H0/J >= 24 - 4r`.

Also gilt für die 30 physikalischen Typen mit `r<=3` bereits `H0/J>=12`.
Die verbleibenden 33 Vierzeiler zerfallen nach ihrer vierten Zeile in
19 Typen mit `lambda4=1`, 10 mit `lambda4=2` und 4 mit `lambda4=3`.
Der einzige Typ mit `lambda4=4` ist der schon separat behandelte Singuletttyp
`(4,4,4,4)`.

## 2. Ein exaktes Achtplatz-Casimir-Zertifikat schließt weitere 22 Typen

Mit der C16-Vertexreihenfolge aus dem unabhängigen Young-Basisprüfer ist der
gewählte induzierte Cluster

`V_M = [0,1,2,4,5,6,7,10]`.

In lokaler Nummerierung `0,...,7` hat er genau die elf Kanten

`[(0,5),(0,6),(0,7),(1,4),(1,5),(2,3),(2,5),(2,7),(3,6),(4,6),(4,7)]`.

Definiere `H_M = sum_(e in M) (I+S_e)/2` und
`C8 = sum_(0<=i<j<8) S_ij`. Der vollständige lokale exakte Spektraltest zeigt

`H_M - C8/5 > (8/3) I` auf dem gesamten physikalischen Raum `(C^4)^tensor8`.

Für einen lokalen Youngtyp `nu` wirkt `C8` als der ganzzahlige Inhaltssaldo
`c_nu = sum_(r,c in nu) (c-r)`. Daher ist lediglich nachzuweisen, dass der
ganzzahlige lokale Operator `X_M=sum_(e in M)S_e` keine Eigenwerte unterhalb von
`-17/3 + 2 c_nu/5` hat. Genau dies prüfen die gespeicherten Polynome und
Sturmzählungen; alle Grenzpunkte sind strikt wurzelfrei.

Die 1920 Automorphismen des C16 liefern in der Gruppenmittelung pro globaler
Kante genau 528 Beiträge und pro globaler Nichtkante genau 408 Beiträge zur
vollständigen lokalen Paarsumme. Somit

`avg_G H_M = (11/40) H0/J`,

`avg_G C8 = (11/40) X + (17/80)(C16-X)`.

Auf dem globalen Youngtyp `lambda` ist `C16=c_lambda I`. Einsetzen von
`X=2H0/J-40I` in die gemittelte lokale Ungleichung ergibt

**`H0/J > 26/3 + 17 c_lambda/100`.**

Das ist eine globale Operatoruntergrenze auf jedem der 64 physikalischen
Youngtypen. Insbesondere sind alle 22 Vierzeiler mit `c_lambda>=18` strikt
oberhalb von `1759/150 = 11.726666...`, also oberhalb von `11.58`.

Unter der bereits separat bewiesenen lokalen F4-Ungleichung
`Htr/J >= (93/100) H0/J + 42/25` liegen diese 22 Typen sogar oberhalb von
`62929/5000 = 12.5858`. Für die 30 höchstens dreizeiligen Typen ist die stärkere
affine Schranke `Htr/J >= (47/50) H0/J +39/25 >=12.84` verfügbar.
Damit können diese 52 Typen das exakt zertifizierte Singulettquartett bei
höchstens `12.447023843544 J` nicht unterlaufen.

## 3. Stärkerer Neunplatzsatz: 55/63 ausgeschlossen

Der induzierte Neunplatzcluster mit den globalen Vertices
`[0,1,2,3,5,6,8,10,11]` besitzt 14 Kanten. Exakt bestätigt ist

`H_M - (8/45) C9 > (18/5) I`.

Die vollständige Gruppenmittelung hat die Koeffizienten `a=14/40` für Kanten
und `b=22/80` für Nichtkanten. Daraus folgt der stärkere globale Satz

**`H0/J > 920/97 + (44/291)c_lambda`.**

Damit sind auch die drei Formen mit `c_lambda=15,15,16` ausgeschlossen:
`(7,4,3,2)`, `(6,5,4,1)` und `(6,6,2,2)`. Der niedrigste neue Ausschlusswert
ist `1140/97 = 11.7525773195... >11.58`.

Der einseitige exakte Spektraltest vermeidet vollständige Faktorisierung:
Für `cut = 2(ell+t c_nu)-m` berechnet er
`q(z)=det(zI + X_M - cut I) = (-1)^d p(cut-z)`.
Alle Koeffizienten von `q` sind strikt positiv. Da die rationale Young-
Darstellung einer endlichen Gruppe unitarisierbar ist, ist das Spektrum von
`X_M` reell. Ein Eigenwert `<=cut` würde eine nichtnegative reelle Nullstelle
von `q` erzeugen, was die strikte Koeffizientenpositivität ausschließt.
Dies ist ein exakter einseitiger Positivitätsbeweis, kein Floating-Point-Test.

Nach diesem Neunplatzsatz allein blieben genau acht Typen offen:

`(7,3,3,3), (6,5,3,2), (5,5,5,1), (6,4,4,2),`

`(6,4,3,3), (5,5,4,2), (5,5,3,3), (5,4,4,3)`.

## 4. Abschließender Zehnplatzsatz: 58/63 ausgeschlossen, fünf offen

Der bereits vor dem Stopp gestartete letzte Prüfer wurde vollständig fertig.
Für den induzierten Zehnplatzcluster
`[0,1,2,4,5,6,7,8,10,11]` mit 17 Kanten ist exakt bewiesen:

`H_M - (9/50) C10 > (447/100) I`.

Die exakte Gruppenmittelung mit `a=17/40` und `b=28/80` ergibt

**`H0/J > 1965/199 + (63/398)c_lambda`.**

Damit sind nun alle 28 Vierzeiler mit `c_lambda>=12` oberhalb von
`2343/199 = 11.7738693467... >11.58`. Zusammen mit den 30 Typen mit höchstens
drei Zeilen sind 58 der 63 Nichtsinguletttypen ausgeschieden. Unter der
separat bewiesenen F4-Untergrenze liegt diese ausgeschlossene Menge in Htr
oberhalb von `251331/19900 = 12.6296984924...`, klar über dem Singulettquartett.

Die fünf noch offenen Typen und ihre tatsächlich zertifizierten Untergrenzen
lauten:

| Youngtyp | `c_lambda` | bewiesene strikte Untergrenze `H0/J` |
| --- | ---: | ---: |
| `(6,4,4,2)` | 10 | `2280/199 = 11.4572864321...` |
| `(6,4,3,3)` | 8 | `2217/199 = 11.1407035175...` |
| `(5,5,4,2)` | 8 | `2217/199 = 11.1407035175...` |
| `(5,5,3,3)` | 6 | `2154/199 = 10.8241206030...` |
| `(5,4,4,3)` | 4 | `2091/199 = 10.5075376884...` |

Keine dieser fünf Untergrenzen überschreitet 11.58. Insbesondere ist der
numerisch tiefste Nichtsinguletttyp `(5,4,4,3)` noch **nicht ausgeschlossen**.
Der vollständige Nichtsingulettabschluss und damit die globale Quartettordnung
über alle SU4-Sektoren bleiben offen.

## 5. Nachvollziehbare Grenze der Clusterfamilie

Nach dem Achtplatzsatz allein waren noch die elf Typen offen

`(6,6,2,2), (7,4,3,2), (6,5,4,1), (7,3,3,3), (6,5,3,2), (5,5,5,1),`

`(6,4,4,2), (6,4,3,3), (5,5,4,2), (5,5,3,3), (5,4,4,3)`.

Die numerisch engste Form ist weiterhin `(5,4,4,3)`, Spechtdimension 180180,
mit berichtetem numerischem Minimum `12.133537149... J`. Das wird hier **nicht**
als rigorose Untergrenze verwendet. Selbst der beste numerische Achtplatz-
Casimir-Dualbound erreicht dort nur `9.795753729... J`; Neun- und Zehnplatz-
Scouting erreichen `10.258612944...` beziehungsweise `10.583559973... J`.
Der hier eingesetzte lokale Ansatz schließt diese entscheidende Lücke also
noch nicht.

Die vollständigen induzierten Teilmengen-Orbits wurden kleinräumig enumeriert:
25 für acht Plätze, 19 für neun Plätze und 18 für zehn Plätze. Die exakten
Orbitgrößen summieren sich auf die jeweiligen Binomialkoeffizienten. Dieser
Census belegt Vollständigkeit **dieser Clusterfamilie**, nicht Vollständigkeit
eines globalen Spektralbeweises.

## 6. Warum der frühere unverschobene Singulett-Trace nicht übernommen wird

Die singulettspezifische Symmetrie `X -> -X` und `||X||<=24` gilt nicht auf
allen Nichtsinguletts. Im vollständig symmetrischen Typ ist beispielsweise
`X=40I`, obwohl seine Energie harmlos hoch ist. Ein unverschobener gerader
Momententest würde gerade diesen großen positiven Eigenwert bestrafen.

Ein zulässiger nächster Schritt wäre ein einseitig verschobener oder
Chebyshev-gefilterter Test auf den tatsächlich verbleibenden Typen, kombiniert
mit einer exakten Mackey-Reduktion. Ein Ritzresiduum allein liefert weder
Vollzählung noch den hierfür benötigten Ausschluss tieferer Eigenwerte.

## Geltungsgrenzen

Dieser Ordner ergänzt den schon vollständig zertifizierten 24024D-
Singulettsektor. Er beweist noch nicht die globale Ordnung über sämtliche
physikalischen SU4-Sektoren. Die exakte Vierfachheit des einzelnen
Singulett-Standardniveaus, seine einfache Multiplizität im reduzierten Block,
die globale Reihenfolge über Nichtsinguletts und die Kontrolle eines
Mikrorests sind unterschiedliche Aussagen. Die beiden letzten dürfen aus
diesem partiellen Ausschluss nicht gefolgert werden.

Keine Mikrorestnorm, keine Universalraum-Vollrekonstruktion und kein SHARED-
Bank-Spektralsatz werden hier behauptet. Frühere Zertifikate wurden nicht
verändert und es wurde nichts committed.

## Welche einfache Regel wird hier geprüft — und welche nicht erklärt?

Die gesamte C16-Zählung dient einer einzigen **bedingten Konsistenzfrage**:
Wenn auf den 16 Plätzen bereits vier lokale Zustände und auf jeder der 40
C16-Kanten dieselbe Austauschenergie `J(I+S_ij)/2` gewählt sind, welche
Symmetrietypen können energetisch unter einem vorgeschlagenen niedrigen
Singulettquartett liegen? Die Young- und Casimir-Zählung organisiert die
vollständigen Alternativen innerhalb genau dieser Regel.

Die Acht-, Neun- und Zehnplatzrechnungen sind dabei lediglich lokale
Beweiszeugen innerhalb des unveränderten 16-Platz-Modells. Sie fügen ihm keine
neuen physikalischen Freiheitsgrade hinzu. Größere Beweiszeugen sind jedoch
auch keine fundamentalere Begründung der Ausgangsregel.

Keine noch so vollständige Eigenwertzählung entscheidet, **warum** die
physikalische Natur vier lokale Zustände, gerade die C16-Geometrie, gleiche
Kopplungen, dieses Austauschgesetz, die konkrete F4-Korrektur oder ihren
Parameterwert auswählen sollte. Ebenso wenig bestimmt sie den Zusammenhang
mit Raumzeit, Materie, tatsächlich beobachteten Messgrößen oder einem
kontrollierten Mikrorest. Diese physikalische Auswahl bzw. Herleitung muss aus
einer unabhängigen Grundstruktur kommen. Der hier erreichte Teilsatz ersetzt
sie nicht.

## Reproduktion

Aus dem Repository-Verzeichnis mit `/opt/homebrew/bin/python3`:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 experiments/theory-contracts/universalraum-six-new-audit-20260914/spectral/nonsinglet_frontier/checker.py rows
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 experiments/theory-contracts/universalraum-six-new-audit-20260914/spectral/nonsinglet_frontier/checker.py certify
```

Die explorativen Modi heißen `scout --n 8`, `scout --n 9` und `scout --n 10`.
Sie bauen keine vollständige S16-Spechtmatrix auf.

Für die größeren Beweise heißen die Modi `certify --n 9` und `certify --n 10`;
für den unabhängigen
leichten Nachlauf `replay`, auch unter `python -O`. Dieser prüft Vollständigkeit
der lokalen Youngtypen, Schur-Weyl-Dimension `4^n`, Hook-Dimensionen, unabhängige
Charakterspuren, die einseitigen Koeffizienten und sämtliche globalen
Ausschlusszählungen neu.

Optional liegt ausschließlich in diesem Arbeitsordner ein ignoriertes
`.deps/` mit dem lokal isolierten Paket `python-flint==0.9.0`. Es verändert
keine globale Python-Installation. Mit `PYTHONPATH` auf dieses Verzeichnis und
`SYMPY_GROUND_TYPES=flint` erzwingt `matrix_charpoly` den dichten exakten
FLINT-Kern. Ohne dieses Backend ist die mathematisch identische reine
SymPy-Variante langsamer. Die gespeicherten Zertifikate benötigen für ihren
leichten Replay keine erneute große Matrixrechnung.
