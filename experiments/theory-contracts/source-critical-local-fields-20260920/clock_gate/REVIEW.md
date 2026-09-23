# Unabhängiges Review des Clock-Gates

**Verdikt:** `PASS_EXACT_WITH_SCOPE`

Die tragenden Aussagen in `PROOF.md` folgen aus den gepinnten Daten und
werden durch `checker.py` korrekt geprüft. Ich finde keinen mathematischen
Fehler in den vier entscheidenden Identitäten. Die Schlussfolgerung zur
stationären Clock ist ausdrücklich bedingt formuliert und setzt nicht
unzulässig voraus, dass jede denkbare physikalische Clock mit einem festen
Hamiltonoperator kommutieren muss.

## 1. Gepinnte Eingaben und Reproduktion

Der Checker verifiziert vor der Rechnung SHA-256-Pins für

* die korrigierten 10D-Lifts in `gauge_section.json`,
* die nativen 8D-Clockmatrizen in
  `compiler-integral-triality-20260918/certificate.json`,
* `source-graded-locality-20260920/PROOF.txt` und dessen Contract-Index.

Die beiden Läufe

```text
python3 checker.py
python3 -OO checker.py
```

ergeben jeweils `538/538` bestandene Prüfungen. Die große Zahl stammt
vorwiegend aus der endlichen Wiederholung derselben Orbit-Paarungsidentität
und ist zu Recht nicht als 538 unabhängige physikalische Evidenzen
interpretiert.

## 2. Nichttriviale Clock-Bahnen sind unter dem festen `Y` geladen

Für die konkret gespeicherten Lifts werden die vollständigen orientierten
Bahnen der Länge 30 beziehungsweise 4 erzeugt. Der Checker zeigt exakt:

\[
Y(S_C^kz)\ne0\quad(1\le k<30),\qquad
Y(S_J^kz)\ne0\quad(1\le k<4).
\]

Die ersten Werte sind wie berichtet

\[
Y(S_Cz)=-\frac43,qquad Y(S_Jz)=-\frac83.
\]

Damit kann eine Summe über die gesamte feste Clock-Bahn den einzelnen
neutralen `z`-Cosinus nicht innerhalb desselben unveränderten
Hyperladungs-\(U(1)\) vervollständigen. Die Bahnelemente sind verschiedene
Ladungseigenoperatoren; bei einer kontinuierlichen \(U(1)\)-Transformation
heben sich verschiedene Nichtnullladungen nicht lediglich durch eine Summe
ihrer Koeffizienten auf. Ein mittransformierender geladener Spurion oder ein
Transport auch des Ladungsoperators wäre eine zusätzliche Struktur.

Diese Aussage betrifft das feste ursprüngliche `Y` und die gespeicherten
Lifts. Sie ist kein Ausschluss einer anderen, gemeinsam transportierten
Ladungsdefinition.

## 3. Die Paarungsformel und ihre genaue Konsequenz

Weil die Lifts `e_R` und `m` punktweise fixieren und auf dem E8-Anteil als
\(A^k\) wirken, gilt

\[
z_k=F_{aux}(-A^ka)-e_R-3m.
\]

Mit \(A^TA=I\) und \(\|a\|^2=8\) folgt für \(k\ne l\)

\[
\begin{aligned}
B(z_k,z_l)
 &=a^TA^{l-k}a-8\\
 &=-\frac12\|A^ka-A^la\|^2<0.
\end{aligned}
\]

Der Checker prüft sowohl die Co-Frame-Formel als auch Selbstnullheit und
diese Paarung für jedes Bahnpaar. Die strikte Ungleichung folgt zusätzlich
aus der geprüften vollen Orbitlänge: verschiedene Potenzen liefern
verschiedene \(A^ka\).

Die im Beweis gezogene Konsequenz ist richtig begrenzt. Die Bahn bildet
kein gemeinsam pinnbares isotropes Nullgitter. Daraus folgt kein allgemeines
Verbot konkurrierender, nicht gegenseitig nuller Wechselwirkungen.

## 4. Ein hyperladungsneutraler reiner Paar-Dress kann nicht ungerade sein

Für

\[
x_{pair}=A e_R+B m
\]

gelten im festgelegten Wörterbuch

\[
Y(x_{pair})=q(x_{pair})=B-A,qquad
(-1)^F=(-1)^{A+B}.
\]

Aus \(Y=0\) folgt \(A=B\), also \(A+B=2A\) und gerade Parität. Der
No-go betrifft damit exakt einen **reinen Paar-Dress**. Er schließt keine
neutralen ungeraden Felder des gesamten Gitters aus; insbesondere bleibt
der bereits genannte Familien-Vektorzweig außerhalb dieser eingeschränkten
Aussage.

Der Checker testet den algebraisch entscheidenden Schritt über
`Y=q=B-A`; die letzte Modulo-2-Folgerung steht korrekt im Beweis, ist aber
nicht als eigener boolescher Modulo-2-Test codiert. Das ist keine Lücke im
Argument, lediglich eine mögliche kleine Verbesserung der
Maschinenzertifizierung.

## 5. `T(Y8)` und `F_aux(Y8)` dürfen nicht verwechselt werden

Die drei geprüften Identitäten

\[
K T(\mathbf1_8)=q,qquad K T(Y_8)=Y,qquad
F_{aux}(Y_8)=T(Y_8)+n
\]

sind konsistent. Für ein allgemeines lokales Feld \(x\) unterscheiden sich
die beiden Cartanpaarungen um

\[
B(F_{aux}(Y_8),x)-B(T(Y_8),x)=B(n,x).
\]

Sie stimmen daher auf \(n^\perp\) überein und nicht auf dem ganzen lokalen
Gitter. `T(Y8)` und `F_aux(Y8)` sind hier eingebettete Cartanvektoren im
reellen Raum; die Gleichung allein behauptet nicht, dass beide neue lokale
Vertexoperatoren seien. Die daraus gezogene Warnung vor einer bloßen
Umbenennung der neuen ungeraden Klasse als alten E8-Spinorzweig ist
gerechtfertigt.

## 6. Reichweite der stationären Clock-Inkompatibilität

Für eine interne Symmetrie eines festen zeitunabhängigen Hamiltonoperators
müssten die nichttrivialen Clockelemente insbesondere die quadratische
Energie erhalten. Exakt geprüft ist jedoch

\[
(S_A^k)^T V_cS_A^k=V_c
\quad\Longleftrightarrow\quad k=0
\]

für die betrachteten Potenzen von `C` und `J`. Ebenso erhalten nur die
Identitätspotenzen den `z`-Cosinus bis auf Vorzeichen. Damit scheitert die
Interpretation dieser **festen Lifts** als Symmetrie genau dieses
**stationären ausgewählten Hamiltonoperators**.

Der Beweis verlangt nicht allgemein \([S,H]=0\). Eine Clock könnte
beispielsweise einen zeitabhängigen Hamiltonian, verschiedene Zustände,
Markierungen oder eine Familie von Hamiltonoperatoren ineinander
transportieren. Dann wäre die passende Bedingung ein kovarianter Transport
wie \(S H_tS^{-1}=H_{t+1}\), nicht die Invarianz eines einzelnen `H`.
`PROOF.md` lässt diese Möglichkeiten ausdrücklich offen und verlangt zu
Recht eine zusätzliche Herleitung des gemeinsamen Transports aus der
Quelle.

## Ergebnis

Das Clock-Gate belegt einen präzisen bedingten Ausschluss:

> Mit dem ausgewählten `V_c`, dem festen ursprünglichen `Y` und den bereits
> konstruierten 10D-Lifts bilden weder `C` noch `J` eine nichttriviale
> stationäre Symmetrie, welche den neutralen `z`-Term durch ihre volle Bahn
> vervollständigt.

Es belegt keinen universellen Clock-No-go, keine Source-Auswahl des
Konkurrenzpunkts und keine Forderung, dass jede physikalische Clock mit
jedem Hamiltonoperator kommutieren müsse.
