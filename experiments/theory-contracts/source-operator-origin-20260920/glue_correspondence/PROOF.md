# Der genaue Austauschvertrag für die beiden Randwechselwirkungen

**Verdikt: PARTIAL.** Die folgenden Aussagen sind exakt für das bereits angesetzte Gitter `Gamma=Z^(9,1)`. Sie sind kein aus P1/P2 gewonnener Quelloperator. Neu gegenüber dem bekannten charakteristischen Hindernis ist die vollständige gemeinsame Index-2-Untergruppe samt Wirkung auf die vier lokalen Klassen und der präzise, noch zu realisierende Austauschvertrag.

## 1. Frage und Voraussetzung

Die letzte Feldanalyse benötigte eine ausgewählte positive Metrik `Vc` und normierte gleich starke Wechselwirkungen in den Richtungen `n` und `z`. Ein noch so guter Rotor- oder Fock-Hamiltonian schließt diese Herkunftslücke erst, wenn er genau diese lokalen Operatoren und ihre Zeitentwicklung erreicht. Wir prüfen daher, welche Art Austausch überhaupt mit dem vollen lokalen Gitter verträglich ist. Erfolg ist ein exakter notwendiger Vertrag; Abbruch ist ein frei eingesetzter neuer Parent.

Es gelten unverändert

```
K = diag(1,1,1,1,1,1,1,1,1,-1),  B(x,y)=x^T K y,
a = (1,1,1,-1,-1,-1,-1,-1),
n = (a,-1,3),  z=e9-e10,
u=(n+z)/2,  v=(n-z)/2,
T(p)=(p,-a.p/2,a.p/2),  Vc=K+2 K v v^T K.
```

`n,z` sind neutral bezüglich der tatsächlichen Zeilenfunktionale `q=(1,...,1)` und `Y=(-1/3,-1/3,-1/3,1/2,1/2,0,0,0,1,1)`. `B(u,u)=1`, `B(v,v)=-1`, `B(u,v)=0`. Der gemeinsame D8-Raum ist zu beiden orthogonal.

Bereits bekannt: `n` ist charakteristisch, `z` nicht. Jede integrale Isometrie erhält charakteristische Vektoren. Deshalb kann keine integrale Isometrie von Gamma die beiden Richtungen vertauschen, auch nicht mit Vorzeichen. Dies ist kein Ausschluss emergenter oder nichtinvertierbarer Dualitäten.

## 2. Der rationale Austausch und seine exakte Integritätsgrenze

Der eindeutige lineare Austausch, der den gemeinsamen acht-dimensionalen T-Raum punktweise fixiert und `u` fixiert, ist

```
R = I + 2 v v^T K,
R n=z, R z=n, R u=u, R v=-v.
```

Er erfüllt `R^2=I`, `R^T K R=K`, `R^T Vc R=Vc`, `q R=q`, `Y R=Y`. Aber R ist keine ganzzahlige Matrix. Für jedes `x in Gamma` gilt

```
R x = x + B(x,n-z) (n-z)/2,
B(x,n-z) = a.x[1:8] - 2*x9 - 4*x10.
```

Weil die ersten acht Einträge von `n-z` ungerade sind, ist `R x` genau dann integral, wenn die Summe der ersten acht Einträge von x gerade ist. Folglich

```
Gamma0 = Gamma intersection R(Gamma)
       = {x in Gamma : sum(x1,...,x8) = 0 mod 2},
[Gamma:Gamma0] = [R(Gamma):Gamma0] = 2.
```

R wirkt auf Gamma0 bijektiv. Das ist ein unendlicher Gittersatz aus der Kongruenz, keine Schlussfolgerung aus einer endlichen Vektorprobe.

Man kann die fehlenden Labels nicht einfach als weitere lokale Vertizes danebenlegen: Für `e1 in Gamma` und `R e1 in R(Gamma)` ist `B(e1,R e1)=3/2`. Damit ist `Gamma+R(Gamma)` nicht integral. Jede Konstruktion mit beiden Mengen braucht eine explizite Regel für Defekt-/Twist-Sektoren oder eine veränderte lokale Algebra; eine gewöhnliche integrale Gittererweiterung, die beide unverändert enthält, reicht nicht.

## 3. Anschluss an die bereits gefundenen lokalen Felder

Die letzte Analyse verwendete `M=T(D8) + Z n + Z z`, Index vier in Gamma, und die Repräsentanten

```
0,  f=e1,  b=T((1/2)^8)+n/2=(1,1,1,0,0,0,0,0,0,1),  f+b.
```

Setze `eta(x)=(-1)^sum(x1,...,x8)`. M liegt im eta-geraden Untergitter. Daher gilt auf den **vollständigen** vier Klassen:

| T(D8)-Klasse | 0 | v (Vektor) | s (alter Spinor) | c (gekreuzter Spinor) |
|---|---:|---:|---:|---:|
| eta | +1 | -1 | -1 | +1 |
| in Gamma0 | ja | nein | nein | ja |
| ursprüngliche Fermionparität | gerade | ungerade | gerade | ungerade |

Eta ist somit ausdrücklich nicht die volle Fermionparität. Der gemeinsame Austauschbereich enthält gerade den vorher gefundenen lokalen ungeraden c-Zweig. Das liefert eine konkrete Anschlussbedingung, keine dynamische Auswahl dieses Zweigs. Die v- und s-Felder des vollen Gitters dürfen dabei nicht stillschweigend entfernt werden.

Für jedes minimale c-Gewicht p mit integralem `T(p)+u` beziehungsweise `T(p)+v` gilt

```
R(T(p)+u)=T(p)+u,
R(T(p)+v)=T(p)-v.
```

Die zweite Verschiebung ist `-(n-z)` und bleibt in derselben M-Klasse. R verändert die T(D8)-Gewichte nicht. Es leistet daher insbesondere **nicht** den noch fehlenden Familiendualitäts-Intertwiner vom ursprünglichen FW64 zum neuen c-Feld.

## 4. Ein präziser Labelvertrag, kein konstruierter physischer Defekt

Auf dem Hilbertraum orthonormaler formaler Gitterlabels `ell^2(Gamma)` lässt sich der beschränkte Operator

```
D |x> = sqrt(2) |R x>  falls x in Gamma0,
D |x> = 0             sonst
```

definieren. Direkt folgen `D*=D`, `D^2=D*D=1+eta`. Für die **cocyclefreien Labelverschiebungen** `S_l|x>=|x+l>` mit `l in Gamma0` gilt `D S_l = S_(R l) D`. Insbesondere werden S_n und S_z vertauscht. Für das Label-Energiemodell `H_V|x>=(x^T V x/2)|x>` gilt `[D,H_V]=0` genau dann, wenn `R^T V R=V`, weil Gamma0 vollen Rang hat.

Somit würde dieser Vertrag für die normierten Labelpotentiale `C_l=(S_l+S_-l)/2` die Relation

```
D H(V,gn,gz) = H(V,gz,gn) D
```

liefern, wenn V R-invariant ist. Für dieses Modell ist D eine Symmetrie bei `gn=gz`. Die beiden verschobenen Vakuumlabels ±n und ±z sind verschieden; die Gleichheit folgt nicht schon allein aus neutralen Ladungen.

Diese einfache algebraische Konstruktion liefert **keinen** lokalen topologischen Defekt der ursprünglichen Feldtheorie: Oszillatoren, CAR-/Vertex-Cocycles, Spinstruktur, vollständige Twistsektoren, Normierungen und ein source-geerbter Zustand samt Hamiltonian fehlen. Auch die Relation `D^2=1+eta` allein beweist keine Defektfusion. Ein beliebiger Projektor plus Permutation kann einen solchen Labelvertrag erfüllen. Der Vertrag dient dazu, die vorhandenen Quellen scharf zu prüfen, nicht dazu, ihnen eine Symmetrie hineinzubauen.

## 5. Welche Energie würde eine solche Symmetrie festlegen?

Die Matrix `S=[T(e1),...,T(e8),u,v]` bringt K auf `diag(I9,-1)` und R auf `diag(I9,-1)`. Eine positive R-invariante Energieform hat in dieser Basis die Form `diag(A,b)` mit beliebigem positivem 9x9-A und `b>0`. **Symmetrie allein wählt Vc also nicht aus.**

Nur innerhalb der zusätzlich vorausgesetzten, gleichgeschwindigen verallgemeinerten Metriken `V K V=K` erzwingt sie `A^2=I`, `b^2=1` und durch Positivität `A=I`, `b=1`. In dieser eingeschränkten Klasse ist dann eindeutig `V=Vc`.

Die zusätzliche Geschwindigkeits-/Kompatibilitätsannahme ist keine Ableitung aus P1/P2. Für den zuletzt geprüften direkten Quellpfad war `(V_theta)9,10=0`, während `(Vc)9,10=4`; kein Punkt dieses Pfades erfüllt daher diesen eingeschränkten Austauschvertrag. Das präzisiert die fehlende Dynamik, ohne die alte Pfadobstruktion als neue Entdeckung auszugeben.

## 6. Der vorhandene metaplektische Half-Deck ist nicht dieser Austausch

Der Theoriegraph verweist tatsächlich auf eine ursprüngliche zusätzliche Dualitätsstruktur: `SEAM.CLIFFORD.MODULAR_S.01`, implementiert in `verification/v798_seam_clifford_modular_s.py`. Sie ist im aktuellen Originalledger als endliche metaplektische Identität mit offenem physikalischem Anschluss geführt. In ihrem festen rationalen Gaussian-E8-Chart ist `J^2=-I` rational und

```
Zeta=(I+J)/sqrt(2),   L subset Q^8,   Zeta^2=J.
```

Die fehlende Clifford-Gruppennebenklasse besteht aus `Zeta*g` mit rationalen Gitterautomorphismen g. Ihre Gruppenindexzahl zwei darf nicht mit dem obigen Gitterindex zwei gleichgesetzt werden. Für jedes rationale x ist Zeta*x genau dann rational, wenn x=0: Die Galoiskonjugation `sqrt(2)->-sqrt(2)` fixiert jeden rationalen Vektor und negiert Zeta*x; also müsste dieser null sein. Da I+J invertierbar ist, folgt x=0. Somit

```
L intersection Zeta L = {0}.
```

Dies gilt ebenfalls für die ganze Nebenklasse, denn gL=L. Auch mit einem unveränderten neutralen Rang-2-Paar ist der Schnitt nur von Rang zwei. Beim gerade benötigten Paar `(Gamma,R Gamma)` hat er dagegen Rang zehn und Index zwei. Schnitt und Rang werden unter jeder einzigen gemeinsamen invertierbaren linearen Abbildung beider Gitter erhalten. **Der vorhandene Half-Deck-Austausch mit unverändertem Zusatzpaar kann daher nicht durch einen bloßen Koordinatenwechsel zum benötigten n/z-Austausch werden.**

Das schließt keine neue Quellrealisierung mit anderem Paartransport, Gauging oder echter Operatorrekonstruktion aus. Die Aussage gilt für die konkret vorhandene Half-Deck-Lattice-Pair-Identifikation. Sie verbindet den neuen Austauschtest mit dem älteren Compilerresultat und verhindert, dass zwei verschiedene Zweierstrukturen als fehlende Herleitung ausgegeben werden. Die 27 älteren v798-Prüfungen werden hier nicht erneut ausgeführt oder als neue Verifikation gezählt; geprüft werden die erforderlichen exakten Matrizen und das neue Schnittargument.

## 7. Entscheidung für die weitere Quellarbeit

Ein gewöhnlicher integraler Clock-Austausch kann die kritische Balance nicht begründen. Ein Quellweg über eine verallgemeinerte Dualität wäre nur dann belastbar, wenn dieselbe Originalquelle (i) eta, (ii) die gemeinsame Index-2-Algebra, (iii) die vollständige lokale Sektoren-/Cocycleregel und (iv) den zeitlichen Intertwiner liefert. Alternativ muss die konkrete Dynamik die kritische Relation unabhängig von einer Dualität herleiten. Die Labelrechnung allein eröffnet keinen neuen physikalischen Parent und schließt kein T1–T8-Gate.

Die Forschungsliteratur unterscheidet ebenfalls exakte Hilbertraumdualität, IR-Dualität und diskretes Gauging; eine Projektion ist kein globaler Zustandsisomorphismus. Sie liefert hier den methodischen Rahmen, keine TFPT-Quellherleitung: [Pace, Chatterjee und Shao, Abschnitte 1 und 2.3](https://arxiv.org/html/2412.18606v2).

## Reproduktion

`python3 checker.py` und `python3 -OO checker.py`; der Prüfer zertifiziert rationale Matrizen, Untergitterindex, Klassenzeichen und die konkreten Labelrelationen. Der Text liefert die universellen Kongruenz- und Positivitätsargumente. Er prüft keinen physikalischen RG-Fluss.
