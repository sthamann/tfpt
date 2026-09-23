# Nichttrivialer kontinuierlicher Collar mit kontrollierter Renormierung

12. September 2026. **Konstruktive Lösung einer ausdrücklich geänderten
mathematischen Teilaufgabe**, nicht Herleitung der ursprünglichen TFPT-Dynamik.

## Ergebnis

Für die vier quadratisch angeordneten Markierungen lässt sich ein
nichttrivialer selbstadjungierter kontinuierlicher Operator konstruieren,
der eine einheitliche untere Energieschranke, einen eindeutigen Grundzustand,
Quadratsymmetrie, Wärmetransfer und unitäre Zeitentwicklung besitzt.

Der Fourier-Cutoff verschwindet in Normresolvente. Der benötigte nackte
Gegenbeitrag ist NEGATIV. Nach einer festgelegten Energieverschiebung ist
der Gesamtoperator nichtnegativ. Dies widerspricht nicht dem vorherigen
freien Grenzwert für ausschließlich nichtnegative nackte Punktkopplungen.

Ein positives Datum kappa bleibt frei. Es legt den ausgewählten Zustand
und relative Energielücken fest und ist NICHT nur eine gemeinsame
Zeiteinheit. Eine Bestimmung von kappa aus TFPT wurde nicht gefunden.

## 1. Unveränderte geometrische Daten, geänderte Kopplungsregel

Nutze dieselben theta_j=j*pi/2, Fouriermoden und V_M wie in
[COLLAR_LIMIT.md](COLLAR_LIMIT.md). Quelle: die vollständig eingesehene
Funktion dtn in `verification/v331_necessity_of_H.py`, Hash
`5dee9560ad3ca3a6b19984e251bcdbba65b8b645d188f1f0296bfe7a182e041b`.
Die Quelldatei wurde nicht verändert.

Sei A=|D| auf l2(Z). Wähle kappa>0 ausdrücklich als neues Datum und
Cutoffs M=4N. Definiere

    g_(r,N)(z)=4 sum_(|k|<=4N, k congruent r mod4) 1/(|k|+z),
    lambda_N=-1/g_(0,N)(kappa),
    A_N=A+lambda_N V_(4N)V_(4N)*.

lambda_N<0, lambda_N ->0 von unten. Sein inverser Betrag divergiert
logarithmisch. Die Form enthält weiterhin gleich starke Punktbeiträge an
den vier Marken; ihre Stärke und ihr Vorzeichen sind gegenüber dem
ursprünglichen eps=0.4 aber geändert. Die Vorschrift ist durch die
gewählte Bindungsenergie kappa kalibriert, nicht aus P1/P2 bewiesen.

## 2. Stabilität bei JEDEM Cutoff, nicht nur im Grenzwert

Für jedes z>0 gilt

    g_(0,N)(z)>g_(1,N)(z)=g_(3,N)(z),
    g_(0,N)(z)>g_(2,N)(z).

Beweis: Setze f(x)=1/(x+z). Für r=1,2 ergeben sich die Differenzen,
geteilt durch 4, als

    sum_(n=0)^(N-1) [f(4n)+f(4n+4)-f(4n+1)-f(4n+3)]+f(4N),
    sum_(n=0)^(N-1) [f(4n)+f(4n+4)-2f(4n+2)]+f(4N).

Die Klammern sind wegen strikter Konvexität positiv. Schon die erste
Klammer bleibt eine strikt positive Schranke bei N->infinity.

Mit B_N=(A+kappa)^(-1/2)V_(4N) ist ||B_N||^2=g_(0,N)(kappa).
Somit gilt als Formidentität

    A_N+kappa I
      =(A+kappa)^(1/2) [I-B_N B_N*/g_(0,N)(kappa)] (A+kappa)^(1/2)
      >=0.

Der Kern ist eindimensional, weil der größte Gram-Eigenwert einfach ist.
Sein normierter Vektor hat die Fourierkoeffizienten

    psi_N(k)=c_N 1_(k in4Z, |k|<=4N)/(|k|+kappa).

Daher ist -kappa der exakte einfache Grundwert jedes A_N. Die negative
nackte Kopplung verursacht hier KEIN Weglaufen der unteren Energie nach
minus unendlich. Stabilität wird durch die gemeinsame Schranke bewiesen,
nicht durch Weglassen negativer Eigenwerte nach einer Rechnung.

## 3. Expliziter nichttrivialer Normresolventengrenzwert

Für q>kappa schreibe R_q=(A+q)^(-1), B_(q,N)=R_q V_(4N). Die
Woodbury-Identität lautet

    (A_N+q)^(-1)
      =R_q+B_(q,N)[g_(0,N)(kappa)I-G_N(q)]^(-1)B_(q,N)*,
    G_N(q)=V_(4N)* R_q V_(4N).

Die vier Spalten von B_(q,N) konvergieren in l2, also in Operatornorm,
zu B_q. Die Fourierdiagonalisierung auf den vier Marken ist unabhängig
von N. Ihre Nenner sind

    C_(r,N)(q)=g_(0,N)(kappa)-g_(r,N)(q).

Die divergenten harmonischen Terme heben sich auf. Die Grenzen C_r(q)
existieren als absolut konvergente Differenzreihen. Explizit:

    C0(q)=4(1/kappa-1/q)
           +8 sum_(n=1)^infinity [1/(4n+kappa)-1/(4n+q)],

    C1(q)=C3(q)=4/kappa
           +4 sum_(n=0)^infinity [2/(4n+4+kappa)
                    -1/(4n+1+q)-1/(4n+3+q)],

    C2(q)=4/kappa
           +8 sum_(n=0)^infinity [1/(4n+4+kappa)-1/(4n+2+q)].

Die Summanden sind O(n^-2). Außerdem gilt für alle N

    C_(r,N)(q)>=g_(0,N)(kappa)-g_(0,N)(q)
                 >=4(1/kappa-1/q)>0.

Deshalb konvergieren auch die inversen Nenner gleichmäßig. Bezeichne mit
C(q) die vierdimensionale Matrix mit den genannten Fourier-Eigenwerten.
Dann gilt in Operatornorm

    (A_N+q)^(-1) -> R_kappa(q):=R_q+B_q C(q)^(-1)B_q*.

Die Korrektur ist nicht null: B_q hat vier linear unabhängige Spalten
(disjunkte Restklassen in ihrer Fourierbasis) und C(q)>0.

### Warum dies der Resolvent eines echten Operators ist

R_kappa(q) ist selbstadjungiert, positiv und injektiv, denn
R_kappa(q)>=R_q>0. Sein Wertebereich ist dicht. Die Resolventenidentität
geht für je zwei q>kappa durch Normkonvergenz aus den Cutoff-Identitäten
über. Daher definiert

    A_kappa=R_kappa(q)^(-1)-q I,
    Dom(A_kappa)=Ran(R_kappa(q)),

einen q-unabhängigen selbstadjungierten Operator. Die gemeinsame
Schranke A_kappa>=-kappa bleibt erhalten. R_kappa ist kompakt (kompakter
freier Resolvent plus endlicher Rang), also besitzt A_kappa diskretes
Spektrum mit endlichen Vielfachheiten.

Der Grundvektor konvergiert in Norm zu

    psi_kappa(k)=c_kappa 1_(k in4Z)/(|k|+kappa).

Bei q gegen kappa hat nur C0(q) eine Nullstelle; C1(kappa),C2(kappa)
bleiben nach §2 strikt positiv. Die Resolventenpolstelle hat deshalb Rang
eins. Damit ist -kappa auch im Grenzoperator ein einfacher isolierter
Grundwert. Alternativ identifiziert Normkonvergenz der endlichen
Grundvektoren die zugehörige Eigenrichtung; die Polstelle prüft zusätzlich
deren Vielfachheit.

Somit ist H_kappa=A_kappa+kappa I nichtnegativ und hat einen eindeutigen
Nullzustand. Sein Wärmetransfer exp(-tH_kappa) für t>=0 und die unitäre
Gruppe exp(-itH_kappa) für reelles t sind durch den Spektralsatz eindeutig
definiert. Dies ist Existenz auf DEM HIER KONSTRUIERTEN Rand-Hilbertraum,
keine Identifikation mit der Zeitentwicklung von H70 oder einer 3+1D-QFT.
Insbesondere ist ein eindeutiger Einteilchen-Nullzustand kein eindeutiges
Fock-Vakuum: Bei fermionischer zweiter Quantisierung von H_kappa kann die
Nullmode leer oder besetzt sein, ohne die Energie zu verändern. Ein
Ladungssektor, eine weitere Vorschrift oder ein anders begründeter
Vielteilchenparent wären dafür zusätzliche Angaben.

## 4. Quantifizierte Restkontrolle statt bloßer größerer Matrizen

Für q=kappa+1 erhält man bei N>=2 einfache rationale Schwanzschranken:

    0 < C0-C_(0,N) <= 1/(2N),
    0 < C_(1,N)-C1 <= 1/[2(N-1)],
    0 < C_(2,N)-C2 <= 1/[2(N-1)].

Sie folgen aus den oben gepaarten Differenzen und
sum_(n>N) n^-2 <=1/N. Für C1 sind die Schwanzsummanden
-8/[(4n+4+kappa)(4n+2+kappa)], für C2
-8/[(4n+4+kappa)(4n+3+kappa)]; jeweils höchstens 1/(2n^2)
im Betrag. C3=C1. Diese Intervalle sind im Prüfer rational berechnet.

Für die Vektorschwänze gilt bei q>0 und M=4N>=1

    ||B_q-B_(q,N)||^2 <= ||...||_HS^2
       =4 sum_(|k|>4N) 1/(|k|+q)^2 <=2/N.

Zusammen mit der positiven Nenneruntergrenze liefert dies eine
ausdrückliche Operatornorm-Restkontrolle der Resolventenformel. Eine
optimale Konvergenzrate wird nicht beansprucht.

## 5. Warum kappa nicht einfach die frei wählbare Uhr ist

Die ursprüngliche Kreisskala und die markierten Fourieroperationen bleiben
fest. Die Funktionen sin(4 theta) und sin(8 theta) verschwinden an allen
vier Marken und bleiben exakte Eigenfunktionen: für A_kappa mit Energien
4 und 8, für H_kappa mit Energielücken 4+kappa und 8+kappa über dem
Grundzustand. Das dimensionslose Verhältnis

    (8+kappa)/(4+kappa)

ändert sich von 9/5 bei kappa=1 zu 5/3 bei kappa=2. Eine gemeinsame
Energieskalierung entfernt diesen Unterschied in derselben markierten
Operationszuordnung nicht. Schon der Grundzustand unterscheidet sich:

    psi_kappa(4)/psi_kappa(0)=kappa/(4+kappa).

Damit existieren unterschiedliche stabile, symmetrieverträgliche
kontinuierliche Konstruktionen. Stabilität, Vierersymmetrie und eindeutiger
Grundzustand allein wählen kappa nicht aus.

## 6. Herkunft und Abgrenzung

Renormierte Punktstörungen fraktionaler Laplaceoperatoren sind bestehende
Mathematik, kein Anspruch auf eine neue allgemeine Weltformel. Primärer
Literaturkontext: Michelangeli–Scandone,
https://arxiv.org/abs/1803.10191 . Die hier benutzte Kreiskonstruktion,
Viererrestklassen, Stabilität und Grenzformeln sind oben eigens bewiesen;
der R^d-Artikel wird nicht als Beweis dieser konkreten Aussagen ausgegeben.

Gelöst: Existenz und kontrollierter nichttrivialer Grenzübergang einer
stabilen, explizit renormierten Vierpunktfamilie. Nicht gelöst: warum die
physische Quelle diesen Ausgleichsterm und genau ein kappa liefert, wie
dieser Randoperator in den Materie-/Rotorparent eingebettet wird, und die
weiteren T1–T8-Verträge. Der zuvor ausgeschlossene positive nackte Weg
bleibt ausgeschlossen.

## Reproduktion

`renormalized_collar.py`: rationale Gram-/Stabilitäts- und Schwanztests,
Vergleich der Grundvektoren und Resolventen mit der tatsächlichen
Quellfunktion bei bewusst geänderter Kopplung, Kontrollen der nicht
wegskalierbaren kappa-Abhängigkeit. Numerische Quellprüfungen sind von
den allgemeinen analytischen Beweisen getrennt. Kein Quelldatei-Patch,
kein Paper-/Website-/Ledger-Update, keine neue Vollständigkeitsbehauptung.
