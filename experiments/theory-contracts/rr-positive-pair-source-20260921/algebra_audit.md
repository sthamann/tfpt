# Audit des positiven RR/W-Lifts und quartisch erweiterte Rekonstruktion

## Urteil

Der vorgeschlagene Operator

\[
H_+=2\kappa\sum_A
\left(b_A+\frac{P_A}{\sqrt8}\right)^\dagger
\left(b_A+\frac{P_A}{\sqrt8}\right),
\qquad
P_A=\sum_{i<j}W_{A,ij}f_jf_i,
\qquad \kappa>0,
\]

ist als bedingter endlicher Fockraumkandidat algebraisch korrekt. Er ist
positiv, selbstadjungiert in der unten präzisierten Formrealisierung, erhält
\(Q=N_f+2N_b\) und reproduziert bei \(WW^\dagger=8I_{60}\) im hellen
Paar/Boson-Zweiraum exakt den aktiven RR-Block
\(\kappa\left(\begin{smallmatrix}2&2\\2&2\end{smallmatrix}\right)\).
Der mitgelieferte native Tensor wurde erneut als

```text
SHA-256 3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763
```

identifiziert.

Der frühere Contract `UR.SOURCE.LOWQ.01` widerlegt diesen Kandidaten nicht.
Seine fermionische untere Antwort war auf eine Zahlenmatrix beschränkt; der
neue Operator besitzt zusätzlich die besetzungsabhängige Antwort eines
normalgeordneten Vierfermionterms. Die richtige Erweiterung der Klasse ist

\[
D(V)=\sum_{I,J}a_I^\dagger V_{IJ}a_J,
\qquad a_{ij}=f_jf_i\quad(i<j),
\qquad V=V^*\text{ auf }\Lambda^2\mathbb C^{n_f}.
\]

In dieser erweiterten Klasse bleibt der stärkste Rekonstruktionssatz erhalten:
globale untere Antworten, starke \(Q\)-Erhaltung und eine einzige globale
untere Schranke entfernen weiterhin alle Umwandlungen vom Grad \(m\ge3\);
die gesamte Kompression auf \(Q\le4\) rekonstruiert dann eindeutig
\((c,h,\Omega,V,C_1,C_2)\) und damit den ganzen Generator.

Die Schur-Sättigung im \(Q=2\)-Block allein bestimmt dagegen **nicht** den
globalen Grundraum. Der exakte \(2^{n_f}\)-dimensionale Nullraumsatz gilt,
wenn der globale Operator tatsächlich die vervollständigte Quadratform ist
(also insbesondere kein direkter \(C_2\)-Term und kein weiterer erst bei
\(Q\ge4\) sichtbarer positiver Term vorhanden ist). Für \(H_+\) ist diese
stärkere Voraussetzung erfüllt.

Ein davon unabhängiges Positivitätsargument liefert die stärkste neue
Obstruktion: Jede positive selbstadjungierte Erweiterung, deren Formkompression
auf \(Q\le3\) mit der von \(H_+\) übereinstimmt, behält mindestens

\[
\sum_{q=0}^{3}{64\choose q}
=1+64+2016+41664
=\boxed{43745}
\]

exakte Nullzustände. Dazu ist nicht einmal starke \(Q\)-Erhaltung der
Erweiterung nötig. Eine solche Erweiterung kann deshalb keinen eindeutigen
globalen Zustand auswählen.

## 1. Präzise Klasse und Domains

Seien \(n_f,n_b<\infty\) und

\[
\mathcal F=\Lambda(\mathbb C^{n_f})\otimes
\Gamma_s(\mathbb C^{n_b}),
\qquad Q=N_f+2N_b.
\]

Mit \(\mathcal D_{\rm fin}\) wird der algebraische Endlichteilchenkern
bezeichnet. Für den erweiterten Rekonstruktionssatz werden folgende
Voraussetzungen benötigt:

1. Die CAR/CCR-Felder erzeugen die volle irreduzible Fockdarstellung, ohne
   Zuschauerfaktor.
2. \(H=H^*\) kommutiert stark mit \(Q\). Der Raum
   \(\mathcal D_{\rm fin}\subset\operatorname{Dom}H\) ist invariant und ein
   Kern für \(H\).
3. Auf ganz \(\mathcal D_{\rm fin}\) gelten die globalen Operatoridentitäten

   \[
   [[b_A,H],b_B^\dagger]=\Omega_{AB}I,
   \]

   \[
   \{[f_i,H],f_j^\dagger\}
   =h_{ij}I+
   \{[f_i,D(V)],f_j^\dagger\},
   \]

   mit \(h=h^*\), \(\Omega=\Omega^*\) und \(V=V^*\). Die zweite Gleichung
   ist eine Operatorgleichung, nicht nur eine Vakuum- oder
   Niedrigsektor-Erwartung.
4. Es gibt eine einzige sektorunabhängige Schranke

   \[
   H\ge-\gamma I,
   \qquad \gamma<\infty,
   \]

   auf dem gesamten Fockraum.

Da der fermionische Fockraum endlichdimensional ist, ist \(D(V)\) beschränkt.
Somit ist \(\widehat H=H-D(V)\) auf derselben Domain selbstadjungiert,
weiterhin global halbbeschränkt und besitzt genau die skalaren unteren
Antworten des früheren Satzes. Das ist der entscheidende saubere Übergang zur
alten Normalform; der neue Kandidat wird nicht künstlich in die engere Klasse
gezwungen.

Für die positive Quadratform unten sei \(K_A\) ein beschränkter gerader
Fermionoperator. Der gemeinsame Spaltenoperator

\[
B=(B_A)_A,
\qquad B_A=b_A+K_A,
\]

ist als beschränkte Störung des Bosonvernichter-Spaltenoperators auf
\(\operatorname{Dom}N_b^{1/2}\) geschlossen. Eine einzelne Komponente
\(B_A\) ist dagegen auf ihrer natürlichen Domain
\(\operatorname{Dom}b_A\) geschlossen; ihre Restriktion auf die wegen der
anderen Moden kleinere gemeinsame Domain
\(\operatorname{Dom}N_b^{1/2}\) muss für sich nicht geschlossen sein. Bei
\(\Omega>0\) ist

\[
q_B[\Psi]=\sum_{A,B}\langle B_A\Psi,\Omega_{AB}B_B\Psi\rangle
\]

eine geschlossene nichtnegative Form mit
\(\operatorname{Dom}q_B=\operatorname{Dom}N_b^{1/2}\). Der zugehörige
Friedrichsoperator ist die kanonische selbstadjungierte Realisierung von
\(B^\dagger\Omega B\). Weil die \(K_A\) beschränkt sind, ist der ausgeschriebene
Polynomoperator auch eine relativ \(N_b\)-beschränkte Störung mit relativer
Schranke null; \(\mathcal D_{\rm fin}\) ist ein Formkern und Operatorcore.
Damit wird weder Positivität noch der Nullraumsatz auf formale Vektoren
gestützt.

## 2. Quartisch erweiterter Normalform- und Rekonstruktionssatz

Auf \(\mathcal D_{\rm fin}\) folgt aus den Voraussetzungen zunächst

\[
H=cI+d\Gamma_f(h)+d\Gamma_b(\Omega)+D(V)
 +\sum_{m=1}^{\lfloor n_f/2\rfloor}(T_m+T_m^\dagger),
\]

\[
T_m=\sum_{|\alpha|=m,\ |I|=2m}
C_{\alpha I}(b^\dagger)^\alpha f_I.
\]

Die Begründung ist exakt die frühere Normalform für \(H-D(V)\). Der
Vierfermionterm verändert die Bosonantwort nicht und seine gesamte
fermionische Antwort wurde in der Hypothese explizit abgezogen.

Nehme nun einen höchsten nichtverschwindenden Grad \(M\ge3\) an. Für eine
Bosonenrichtung \(z\) wählt der bereits geprüfte kohärente-Zustandsbeweis eine
fermionische negative Eigenrichtung des führenden hermiteschen Koeffizienten.
Entlang endlicher Abschneidungen eines kohärenten Zustands gilt dann

\[
\langle H\rangle=-a r^M+O(r^{M-1})+O(r^2)+O(1),
\qquad a>0.
\]

Der neue Anteil \(D(V)\) steckt vollständig im \(O(1)\)-Term, weil er auf dem
endlichen fermionischen Fockraum beschränkt ist. Er kann den Widerspruch zur
globalen unteren Schranke daher nicht beheben. Folglich

\[
\boxed{T_m=0\quad(m\ge3).}
\]

Jeder Operator der erweiterten stabilen Klasse hat somit die Form

\[
\boxed{
H=cI+d\Gamma_f(h)+d\Gamma_b(\Omega)+D(V)
 +(T_1+T_1^\dagger)+(T_2+T_2^\dagger).
}
\]

Seien \(P_{rs}\) die Projektionen auf
\((N_f,N_b)=(r,s)\). Aus der Kompression auf \(Q\le4\) erhält man ohne
Mehrdeutigkeit

\[
c=P_{00}HP_{00},
\]

\[
h=P_{10}(H-cI)P_{10},
\qquad
\Omega=P_{01}(H-cI)P_{01},
\]

\[
V=P_{20}\bigl(H-cI-d\Gamma_f(h)\bigr)P_{20},
\]

\[
C_1=P_{01}HP_{20},
\qquad
C_2=P_{02}HP_{40}.
\]

Hier werden die Sektoren mit den normierten natürlichen Fockbasen
identifiziert; insbesondere ist \(D(V)|_{\Lambda^2}=V\), und \(C_2\) enthält
die üblichen \(\sqrt{\alpha!}\)-Faktoren der normierten Zweibosonbasis.
Damit gilt innerhalb genau dieser global definierten Klasse

\[
P_{Q\le4}HP_{Q\le4}=P_{Q\le4}H'P_{Q\le4}
\iff
(c,h,\Omega,V,C_1,C_2)=(c',h',\Omega',V',C_1',C_2')
\iff H=H'.
\]

Die letzte Gleichheit gilt zuerst auf \(\mathcal D_{\rm fin}\) und dann wegen
der Kern- und Selbstadjungiertheitsannahmen für die Abschließungen.

Der Satz sagt nicht, dass jede frei gewählte Liste dieser sechs Koeffizienten
eine global halbbeschränkte Fortsetzung besitzt. Insbesondere muss der
bosonisch quadratische führende Operatorpencil, der \(\Omega\) und \(T_2\)
enthält, in jeder kohärenten Bosonenrichtung nichtnegativ sein; Nullrichtungen
bringen weitere Verträglichkeitsbedingungen für \(T_1\) mit sich.

## 3. Audit von \(H_+\)

Mit \(a=(a_I)_I\) und \(C=(\kappa/\sqrt2)W\) lautet die Expansion

\[
H_+=b^\dagger\Omega b+b^\dagger Ca+a^\dagger C^\dagger b+a^\dagger Va,
\]

\[
\Omega=2\kappa I_{60},
\qquad
C=\frac{\kappa}{\sqrt2}W,
\qquad
V=\frac{\kappa}{4}W^\dagger W.
\]

Also

\[
C_1=C,
\qquad C_2=0,
\qquad c=0,
\qquad h=0.
\]

Der alte reine Umwandlungsdefekt sieht \(C_1\propto W\) und \(C_2=0\), aber
nicht \(V\). Die globale fermionische Antwort enthält die Antwort von
\(D(V)\) und ist daher keine Zahlenmatrix. Genau das erklärt, weshalb der
alte Contract mit skalarem beziehungsweise matrixwertigem \(h\) den neuen
Operator weder klassifiziert noch ausschließt.

Aus \(WW^\dagger=8I_{60}\) folgt für
\(|p_A\rangle=P_A^\dagger|0\rangle/\sqrt8\) und
\(|b_A\rangle=b_A^\dagger|0\rangle\)

\[
H_+\big|_{\operatorname{span}\{|p_A\rangle,|b_A\rangle\}}
=\kappa
\begin{pmatrix}2&2\\2&2\end{pmatrix}.
\]

Die Positivität ist global und folgt schon vor dieser nativen
Normierungsidentität aus der Quadratform. Die Identität \(WW^\dagger=8I\)
wird für den exakten aktiven RR-Block und die Projektoraussage
\(W^\dagger W/8=\Pi_W\) benötigt.

## 4. Schur-Positivität: exakte Aussage und notwendige Zusatzbedingung

Sei nun allgemein \(H\ge0\), \(c=0\), \(h=0\), \(\Omega>0\). Der
\(Q=2\)-Block in der Reihenfolge „Fermionpaar, Boson“ ist

\[
H_{Q=2}=
\begin{pmatrix}
V&C^\dagger\\
C&\Omega
\end{pmatrix}.
\]

Dann gilt die echte Äquivalenz

\[
\boxed{
H_{Q=2}\ge0
\iff
V-C^\dagger\Omega^{-1}C\ge0.
}
\]

Bei nur semidefinitem \(\Omega\) müsste dies durch die
Moore-Penrose-Inverse zusammen mit der Reichweitenbedingung
\(\operatorname{Ran}C\subseteq\operatorname{Ran}\Omega\) ersetzt werden. Diese
zusätzliche Fallunterscheidung wird hier durch \(\Omega>0\) vermieden.

Im Sättigungsfall

\[
V=C^\dagger\Omega^{-1}C
\]

setze

\[
K=\Omega^{-1}C,
\qquad K_A=\sum_IK_{AI}a_I,
\qquad B_A=b_A+K_A.
\]

Dann stimmt der Operator

\[
H_B=B^\dagger\Omega B
\]

mit den rekonstruierten Daten \((c,h,\Omega,V,C_1,C_2)
=(0,0,\Omega,C^\dagger\Omega^{-1}C,C,0)\) überein.
Innerhalb der erweiterten stabilen Rekonstruktionsklasse folgt aus diesen
**gesamten \(Q\le4\)-Daten** daher global \(H=H_B\).

Wichtig ist die Reihenfolge der Aussage:

\[
\text{Schur-Sättigung in }Q=2
\quad\not\Rightarrow\quad
H=H_B.
\]

Ein \(T_2\)-Term oder ein positiver Term wie
\(\varepsilon N_b(N_b-1)\) ist im \(Q=2\)-Block unsichtbar. Für den
Quadratform- und Nullraumsatz muss deshalb zusätzlich global \(H=H_B\)
feststehen, etwa durch die vollständige \(Q\le4\)-Rekonstruktion mit
\(C_2=0\) und ohne weitere außerhalb der Klasse zugelassene Antwortterme.

Beim RR/W-Kandidaten ist

\[
C^\dagger\Omega^{-1}C
=\frac{\kappa}{4}W^\dagger W
=V,
\qquad
K=\frac{W}{\sqrt8},
\]

und die globale Quadratdarstellung ist bereits seine Definition. Hier gibt
es diese Lücke nicht.

## 5. Vollständiger Nullraum: Konstruktion und Umkehrung

Die Operatoren \(K_A\) bestehen nur aus geraden Fermionvernichtern. Daher

\[
[K_A,K_B]=0.
\]

Setze

\[
Y=\sum_A b_A^\dagger K_A,
\qquad
S\psi=e^{-Y}(|0_b\rangle\otimes\psi),
\qquad
\psi\in\Lambda(\mathbb C^{n_f}).
\]

Da jedes \(K_A\) die Fermionzahl um zwei senkt, endet die Exponentialreihe
nach spätestens \(\lfloor n_f/2\rfloor\) Schritten. Jeder Vektor \(S\psi\)
liegt somit in \(\mathcal D_{\rm fin}\). Aus

\[
[b_A,Y]=K_A,
\qquad [K_A,Y]=0
\]

folgt

\[
B_Ae^{-Y}=e^{-Y}b_A,
\]

also \(B_AS\psi=0\) und \(H_BS\psi=0\).

Für die Umkehrung schreibe einen Vektor im Formbereich als

\[
\Psi=\sum_\alpha|\alpha_b\rangle\otimes\psi_\alpha.
\]

Wegen \(\Omega>0\) gilt

\[
\Psi\in\ker H_B
\iff B_A\Psi=0\quad\text{für alle }A.
\]

Die normierte Bosonkomponente der Gleichung \(B_A\Psi=0\) liefert die
Rekursion

\[
\sqrt{\alpha_A+1}\,\psi_{\alpha+e_A}
=-K_A\psi_\alpha.
\]

Da die \(K_A\) kommutieren, ist sie konsistent und besitzt die eindeutige
Lösung

\[
\psi_\alpha
=\frac{(-1)^{|\alpha|}}{\sqrt{\alpha!}}K^\alpha\psi_0.
\]

Sie endet wieder durch Fermionnilpotenz. Somit ist jeder Nullvektor von der
Form \(S\psi_0\). Die bosonleere Projektion von \(S\psi_0\) ist genau
\(\psi_0\), also ist \(S\) injektiv. Damit

\[
\boxed{
\ker H_B=\operatorname{Ran}S,
\qquad
\dim\ker H_B=2^{n_f}.
}
\]

Weil \(Y\) eine Fermionpaarvernichtung mit einer Bosonerzeugung koppelt,
erhält \(S\) die Ladung \(Q\). Daher genauer

\[
\boxed{
\dim(\ker H_B\cap\mathcal H_{Q=q})={n_f\choose q}
\quad(0\le q\le n_f),
}
\]

und für \(q>n_f\) gibt es keinen Nullzustand.

Dieser Satz enthält die genaue metrische Starrheitsaussage. Für festes
\(K\) verändert eine beliebige Wahl \(\Omega>0\) nur die positive Gewichtung
der Bedingungen \(B_A\Psi=0\), nicht den Nullraum. Wenn zugleich \(K\)
verändert wird, ändert sich dessen Einbettung \(S\), seine Dimension bleibt
aber \(2^{n_f}\). Eine positive Quellenmetrik wählt daher keinen einzelnen
globalen Zustand aus.

## 6. Positivitätsgeschützte Mindestentartung jeder Erweiterung

Der folgende Satz benötigt weder die Antwortidentitäten noch die
Normalformklassifikation.

Sei \(P_{\le3}\) die Projektion auf \(Q\le3\), und sei
\(\widetilde H\ge0\) selbstadjungiert. Angenommen,
\(P_{\le3}\mathcal F\) liegt in ihrem Formbereich und ihre Formkompression
stimmt dort mit der von \(H_+\) überein:

\[
q_{\widetilde H}(u,v)=\langle u,H_+v\rangle
\qquad
(u,v\in P_{\le3}\mathcal F).
\]

Dies ist insbesondere erfüllt, wenn die vollständige Operatorkompression
\(P_{\le3}\widetilde H P_{\le3}=P_{\le3}H_+P_{\le3}\) auf diesem endlichen
Raum gilt.

Für jeden \(x\in\ker H_+\cap P_{\le3}\mathcal F\) ist dann

\[
q_{\widetilde H}[x]=0.
\]

Positivität liefert

\[
0=q_{\widetilde H}[x]
=\|\widetilde H^{1/2}x\|^2,
\]

also \(x\in\ker\widetilde H\). Mögliche Kopplungen an höhere
\(Q\)-Sektoren können diese Schlussfolgerung nicht umgehen; bei einem
positiven Operator kann ein Vektor mit verschwindender Quadratform keine
versteckte Offdiagonalkopplung tragen. Somit

\[
\dim\ker\widetilde H
\ge
\sum_{q=0}^{3}{n_f\choose q}.
\]

Für \(n_f=64\) ergibt das

\[
\boxed{\dim\ker\widetilde H\ge43745.}
\]

Der Term \(\varepsilon N_b(N_b-1)\), \(\varepsilon\ge0\), zeigt zugleich die
Grenze: Er ist auf \(Q\le3\) null, kann aber ab \(Q=4\) Teile des höheren
Grundraums anheben. Die volle \(2^{64}\)-Entartung ist deshalb eine exakte
Aussage der globalen Quadratform \(H_+\), während die Zahl \(43745\) unter
beliebigen positiven, niedrigsektorerhaltenden Erweiterungen robust bleibt.

## 7. Physischer Status und nächster entscheidender Test

Das Ergebnis ist ein algebraischer Fortschritt innerhalb eines bereits
gewählten CAR/CCR-Feldraums:

\[
\text{positive RR-Form}
\xrightarrow{\text{zusätzliche Feldliftregel}}
(\Omega,C,V)
\xrightarrow{\text{Schur-Sättigung}}
H_+\ge0
\xrightarrow{\text{Quadratform}}
\ker H_+.
\]

Die erste Pfeilbeschriftung bleibt eine zusätzliche Wahl. Weder die primitive
Naht noch P1/P2 haben bisher unabhängig hergeleitet,

* warum die aktive RR-Richtung gerade auf \(P_A/\sqrt8\) und die zweite auf
  \(b_A\) abgebildet wird,
* warum die Quelle genau \(\Omega=2\kappa I\),
  \(C=(\kappa/\sqrt2)W\) und
  \(V=(\kappa/4)W^\dagger W\) liefert,
* wie \(\kappa\) zur physischen Zeit kalibriert wird,
* warum ein bestimmter \(Q\)-Sektor oder ein einzelner Zustand physisch
  ausgewählt wird,
* oder wie daraus die lokale chirale wechselwirkende 3+1D-Theorie,
  Kontinuum und Gravitation folgen.

Im aktuellen Theoriegraphen bleiben
`source-stable-low-charge-reconstruction-20260921` und
`source-mixed-response-reconstruction-20260921` deshalb `PARTIAL`; T1–T8
sind offen. `QGEO.KERNEL.01` ist weiterhin `[O]`,
`TRANS.RAWKERNEL.GDELTA.01` steht auf `missing`, und
`TRANS.TARGETOP.RAWSELECT.01` auf `obstructed`.

Der kleinste entscheidende Herkunftstest ist nun scharf formuliert: Aus der
primitiven Quelle muss auf **demselben** Feldraum und bei **demselben**
Energiebezug die gesamte \(Q=2\)-Antwort

\[
\begin{pmatrix}
V&C^\dagger\\ C&\Omega
\end{pmatrix}
\]

bestimmt werden, nicht nur der kubische Block \(C\). Erst wenn die Quelle
unabhängig die Schur-Sättigung und zusätzlich die \(Q=4\)-Daten
\(C_2=0\) sowie das Fehlen weiterer Antwortterme liefert, folgt der globale
Quadrat- und Nullraumsatz als physische Quellenfolgerung. Bis dahin ist
\(H_+\) ein konsistenter positiver Liftkandidat, aber keine hergeleitete
Universalraum- oder TFPT-Dynamik.

## Appendix A. Unabhängiger Nachaudit: Feshbach-Resolvente im \(Q=2\)-Block

Dieser Appendix benutzt nur den endlichen \(Q=2\)-Block

\[
H_2=
\begin{pmatrix}
V&C^\dagger\\
C&\Omega
\end{pmatrix}
\]

auf „Fermionpaar \(\oplus\) Einboson“. Für
\(z\in\rho(H_2)\cap\rho(\Omega)\) liefert das Schurkomplement von \(z-H_2\)

\[
P_{20}(z-H_2)^{-1}P_{20}
=\bigl(z-H_{\rm eff}(z)\bigr)^{-1},
\]

\[
\boxed{
H_{\rm eff}(z)=V+C^\dagger(z-\Omega)^{-1}C.
}
\]

Das Pluszeichen in \(H_{\rm eff}\) ist korrekt: In \(z-H_2\) stehen die
Offdiagonalblöcke \(-C^\dagger\) und \(-C\), sodass der paarseitige
Schurblock

\[
z-V-C^\dagger(z-\Omega)^{-1}C
=z-H_{\rm eff}(z)
\]

lautet.

Für den positiven RR/W-Lift gelten

\[
\Omega=2\kappa I,
\qquad
C=\frac{\kappa}{\sqrt2}W,
\qquad
V=\frac{\kappa}{4}W^\dagger W.
\]

Damit folgt exakt

\[
\begin{aligned}
H_{\rm eff}(z)
&=\frac{\kappa}{4}W^\dagger W
+\frac{\kappa^2}{2(z-2\kappa)}W^\dagger W\\
&=\boxed{\frac{\kappa z}{4(z-2\kappa)}W^\dagger W}
=\boxed{\frac{2\kappa z}{z-2\kappa}\Pi_W},
\end{aligned}
\]

weil \(W^\dagger W=8\Pi_W\). Insbesondere ist \(z=0\) kein Pol der
eliminierten Bosonresolvente, da \(\Omega>0\), und

\[
\boxed{H_{\rm eff}(0)=0.}
\]

Das ist genau die statische Schur-Sättigung
\(V-C^\dagger\Omega^{-1}C=0\). Sie bedeutet nicht, dass die dynamische
Paarantwort verschwindet; für \(z\ne0\) trägt sie die beiden gekoppelten
Pole des hellen Zweiraums.

Zerlegt man den Paarraum in dunkle und helle Richtungen,
\(I=(I-\Pi_W)+\Pi_W\), ergibt sich die paar-komprimierte Resolvente

\[
\boxed{
P_{20}(z-H_2)^{-1}P_{20}
=\frac{I-\Pi_W}{z}
+\frac{z-2\kappa}{z(z-4\kappa)}\Pi_W.
}
\]

Auf dem hellen Raum gilt

\[
\frac{z-2\kappa}{z(z-4\kappa)}
=\frac12\frac1z+\frac12\frac1{z-4\kappa}.
\]

Die paarseitigen Residuen an den hellen Eigenwerten \(0\) und \(4\kappa\)
sind daher jeweils exakt \(1/2\). Das stimmt mit den normierten Eigenvektoren
\((|p_A\rangle\mp|b_A\rangle)/\sqrt2\) des aktiven Blocks überein: Jeder
besitzt Paargewicht \(1/2\).

Die Feshbach-Darstellung selbst setzt \(z\ne2\kappa\) voraus, weil dort
\((z-\Omega)^{-1}\) nicht existiert. Die geschlossene Resolventform rechts
besitzt auf dem hellen Paarraum bei \(z=2\kappa\) jedoch einen Nullwert und
kann dort fortgesetzt werden; \(2\kappa\) ist kein Eigenwert des gekoppelten
hellen \(2\times2\)-Blocks. Die tatsächlichen Resolventpole bleiben
\(z=0\) und \(z=4\kappa\).

Diese Rechnung ist eine exakte endliche Fockraum-Resolventenrechnung. Sie ist
keine Raumzeit-Streuamplitude, kein LSZ-Resultat, keine lokale Propagator- oder
S-Matrix-Herleitung und kein Kontinuumsnachweis. Die Variable \(z\) ist hier
der komplexe Spektralparameter des endlichen \(Q=2\)-Hamiltonblocks.

## Appendix B. Kein zyklischer Einbau von \(V\) in die Antwortklasse

Die quartisch erweiterte globale Antwortklasse wäre tatsächlich zirkulär,
wenn man nach Kenntnis aller Antworten ein beliebiges \(V\) wählen dürfte,
bis

\[
\{[f_i,H],f_j^\dagger\}
=h_{ij}I+\{[f_i,D(V)],f_j^\dagger\}
\]

formal passt. So ist der Rekonstruktionssatz nicht zu lesen. Die unabhängige
Reihenfolge lautet:

1. \(c\) wird aus dem Vakuumblock bestimmt.
2. \(h\) wird aus dem Einfermionblock bestimmt.
3. Danach wird aus dem reinen Zweifermionblock eindeutig

   \[
   \boxed{
   V_{\rm data}
   =P_{20}\bigl(H-cI-d\Gamma_f(h)\bigr)P_{20}
   }
   \]

   gelesen. Weil \(D(V)|_{\Lambda^2}=V\), gibt es hier keine freie Wahl und
   keine Kernrichtung der Parametrisierung.
4. Erst anschließend muss auf dem gesamten gemeinsamen Kern
   \(\mathcal D_{\rm fin}\) unabhängig verifiziert werden, dass

   \[
   \boxed{
   \{[f_i,H-D(V_{\rm data})],f_j^\dagger\}=h_{ij}I
   \quad\text{für alle }i,j.
   }
   \]

Der vierte Schritt folgt nicht aus den \(Q=2\)-Daten. Er prüft, ob derselbe
aus zwei Fermionen gelesene Koeffizient seine festgelegte normalgeordnete
Fortsetzung in **allen** Besetzungssektoren besitzt. Ein zusätzlicher
Sechsfermionterm, eine andere höhere Besetzungsantwort oder ein
Zuschaueroperator kann denselben niedrigen Block haben und diese globale
Identität trotzdem verletzen.

Damit ist die Logik nicht

\[
\text{„wähle }V\text{ so, dass der Satz gilt“},
\]

sondern

\[
\boxed{
Q=2\text{ bestimmt }V_{\rm data}
\quad\Longrightarrow\quad
\text{globale Antwortidentität ist ein zusätzlicher falsifizierbarer Test}.
}
\]

Genau dieser globale Test bleibt für eine primitive TFPT-Quelle noch zu
liefern. Die Ablesbarkeit von \(V\) aus \(Q=2\) beweist weder die globale
Antwortklasse noch ihre Herkunft; sie verhindert lediglich, dass \(V\) als
nachträglich angepasster Parameter verborgen wird.
