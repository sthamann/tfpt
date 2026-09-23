# Audit: globale Stabilität und Rekonstruktion aus `Q <= 4`

## Urteil

Der stärkste belastbare Satz ist **bedingt exakt**:

> Bei endlich vielen CAR- und CCR-Moden, voller irreduzibler Fockdarstellung,
> globalen unteren Operatorantworten, stark erhaltener Ladung
> `Q = N_f + 2 N_b`, gemeinsamem invariantem Endlichteilchenkern und einer
> **einzigen globalen unteren Energieschranke über alle Q-Sektoren** entfernt
> Stabilität alle Umwandlungen vom Grad `m >= 3`. Danach bestimmt die
> Kompression von `H` auf `Q <= 4` den gesamten Generator.

Ohne die globalen unteren Operatoridentitäten ist die Aussage falsch. Eine
positive Funktion von `N_f`, die auf den Besetzungen null bis vier
verschwindet, ist auf `Q <= 4` unsichtbar und verändert trotzdem höhere
Sektoren. `Q <= 4` ist daher kein voraussetzungsloser Tomograph des
Hamiltonoperators.

Der neue Satz rekonstruiert eine Zielseitendynamik im bereits gewählten
CAR/CCR-Feldraum. Er leitet weder diesen Feldraum noch `h`, `Omega`, `W`, die
Kopplung, die Zeit oder den Zustand aus P1/P2 oder der primitiven Quelle her.
Der Theoriegraph führt den einschlägigen Contract
`source-mixed-response-reconstruction-20260921` weiterhin als `PARTIAL`; die
Transitions `TRANS.RAWKERNEL.GDELTA.01` und
`TRANS.TARGETOP.RAWSELECT.01` bleiben fehlend beziehungsweise blockiert.

## 1. Voraussetzungen und algebraische Normalform

Seien `n_f,n_b < infinity` und

\[
\mathcal F=\Lambda(\mathbb C^{n_f})\otimes
\Gamma_s(\mathbb C^{n_b}),\qquad
Q=N_f+2N_b.
\]

`D_fin` sei der algebraische Endlichteilchenkern. Vorausgesetzt werden:

1. Die CAR/CCR-Felder erzeugen die volle irreduzible Fockdarstellung, ohne
   Zuschauerfaktor.
2. `H=H*` kommutiert stark mit `Q`; `D_fin` liegt in `Dom(H)`, ist unter `H`
   invariant und ein Kern für `H`.
3. Auf ganz `D_fin` gelten die **globalen** Identitäten

\[
\{[f_i,H],f_j^\dagger\}=h_{ij}I,
\qquad
[[b_A,H],b_B^\dagger]=\Omega_{AB}I,
\]

mit hermiteschen Matrizen `h` und `Omega`. Sie müssen nicht skalar sein.

Die bereits geprüfte Normalordnungsargumentation ergibt dann auf `D_fin`

\[
H=cI+d\Gamma_f(h)+d\Gamma_b(\Omega)
 +\sum_{m=1}^{\lfloor n_f/2\rfloor}(T_m+T_m^\dagger),
\]

\[
T_m=\sum_{|\alpha|=m,\ |I|=2m}
C_{\alpha I}(b^\dagger)^\alpha f_I.
\]

Die Endlichkeit dieser Hierarchie folgt aus der endlichen Fermionzahl, nicht
aus einer vorausgesetzten Polynomabschneidung. `h` und `Omega` tragen die
allgemeine quadratische Kinetik. Die frühere skalare Form ist nur der
Spezialfall `h=epsilon_f I`, `Omega=epsilon_b I`.

## 2. Warum globale Stabilität exakt `m >= 3` entfernt

Nehme an, es gebe einen höchsten nichtverschwindenden Grad `M >= 3`. Für eine
Bosonenrichtung `z` ist der führende fermionische Koeffizient

\[
A_M(z)=\sum_{|\alpha|=M,\,|I|=2M}\bar z^\alpha C_{\alpha I}f_I.
\]

Weil `T_M` nicht null ist, kann `z` so gewählt werden, dass `A_M(z)` nicht
null ist. Der hermitesche Operator

\[
S_M(z)=A_M(z)+A_M(z)^\dagger
\]

verbindet verschiedene Fermionzahlsektoren. Er ist nicht null und spurlos;
damit besitzt er eine negative Eigenrichtung `xi`.

Auf dem Produkt aus `xi` und einem kohärenten Bosonenzustand der Amplitude
`r z` gilt

\[
\langle H\rangle
=-a r^M+O(r^{M-1})+O(r^2),\qquad a>0.
\]

Für `M>2` geht dieser Ausdruck gegen minus unendlich. Es gibt dabei keine
Domain-Lücke: Nach der Normalform ist `H` auf `D_fin` ein Polynom endlichen
Grades. Für jedes feste `r` konvergieren die endlichen
Bosonzahlabschneidungen des kohärenten Zustands in allen dafür benötigten
Polynomnormen. Die negativen Erwartungswerte werden somit bereits durch
Vektoren aus `D_fin` beliebig genau erreicht.

Entscheidend ist die Quantifizierung der Stabilität:

\[
H\ge -C I
\]

muss mit **einem** endlichen `C` auf dem gesamten Fockraum gelten. Jeder feste
`Q`-Block ist endlichdimensional und daher für sich automatisch nach unten
beschränkt. Blockweise Schranken, die mit `Q` gegen minus unendlich laufen,
genügen nicht. Da `H` blockdiagonal in `Q` ist, erzwingen die kohärenten
Erwartungswerte, dass die Minimalwerte einer Folge von `Q`-Blöcken gegen
minus unendlich laufen.

Damit folgt rigoros

\[
H\ge-CI\quad\Longrightarrow\quad T_m=0\quad(m\ge3).
\]

Der Beweis benutzt den vollen Fockraum. Bei einer späteren Beschränkung auf
einen Eich- oder sonstigen physischen Unterraum muss separat gezeigt werden,
dass geeignete Zeugen in diesem Unterraum liegen. Die volle
Fockraumfolgerung darf nicht automatisch auf eine andere physische
Hilbertstruktur übertragen werden.

## 3. Der bedingte `Q <= 4`-Rekonstruktionssatz

Unter den Voraussetzungen der Abschnitte 1 und 2 hat jeder zulässige
Generator die Form

\[
H=cI+d\Gamma_f(h)+d\Gamma_b(\Omega)
 +(T_1+T_1^\dagger)+(T_2+T_2^\dagger).
\]

Alle Koeffizienten stehen bereits in normierten Besetzungsbasen von
`Q <= 4`:

\[
c=\langle0|H|0\rangle,
\]

\[
h_{ij}=\langle i_f|H|j_f\rangle-c\delta_{ij},
\qquad Q=1,
\]

\[
\Omega_{AB}=\langle A_b|H|B_b\rangle-c\delta_{AB},
\qquad Q=2,
\]

\[
C_{A,ij}=\langle A_b|H|ij_f\rangle,
\qquad Q=2,
\]

und für `|alpha|=2`, `|I|=4`

\[
C_{\alpha I}
=\frac{\langle\alpha_b|H|I_f\rangle}{\sqrt{\alpha!}},
\qquad Q=4.
\]

Folglich sind für zwei Hamiltonoperatoren dieser stabilen, global
klassifizierten Klasse äquivalent:

\[
P_{\le4}HP_{\le4}=P_{\le4}H'P_{\le4}
\iff
(c,h,\Omega,T_1,T_2)=(c',h',\Omega',T_1',T_2')
\iff H=H'.
\]

Die letzte Gleichheit gilt zunächst auf `D_fin` und wegen der starken
`Q`-Blockzerlegung und der Kernannahme auch für die selbstadjungierten
Abschließungen.

Das ist ein **Eindeutigkeits- und Rekonstruktionssatz**, kein Beweis, dass eine
beliebige vorgegebene `Q <= 4`-Matrix eine global halbbeschränkte Fortsetzung
besitzt. Beim quadratischen Term `T_2` enthält die Existenzfrage zusätzlich
eine Positivitätsbedingung an den bosonischen Hauptteil; in Nullrichtungen
müssen auch die linearen Terme kontrolliert werden.

## 4. Direkte Doppelumwandlung und zwei aufeinanderfolgende Ereignisse

Definiere die direkten Blöcke

\[
C_1=P_{(N_b,N_f)=(1,0)}H P_{(0,2)},
\]

\[
C_2=P_{(2,0)}H P_{(0,4)}.
\]

Dann ist `C_2` genau der Koeffizientenblock von `T_2`, einschließlich der
Faktoren `sqrt(alpha!)` der normierten Bosonbasis. Deshalb unterscheidet die
erste Kurzzeitordnung beide Fälle:

\[
\langle\alpha_b|e^{-itH}|I_f\rangle
=-it\,(C_2)_{\alpha I}
-\frac{t^2}{2}\langle\alpha_b|H^2|I_f\rangle+O(t^3).
\]

Bei `T_2=0` verschwindet die lineare Ordnung, während zwei `T_1`-Schritte in
der quadratischen Ordnung nicht verschwinden müssen. Für einen euklidischen
Transfer `e^{-tH}` ist der erste Jet `-C_2`; bei unitärer Zeit ist er
`-i C_2`. Die Ereignisordnung ist daher direkt messbar und nicht nur eine
Interpretation desselben Endzustands.

## 5. Positiver Niedrigladungsdefekt

Für den nativen Tensor mit

\[
\|W\|_{HS}^2=480
\]

setze

\[
g_4=\frac{\langle W,C_1\rangle_{HS}}{480}
\]

und

\[
D_4=
\|C_1\|_{HS}^2
-\frac{|\langle W,C_1\rangle_{HS}|^2}{480}
+\|C_2\|_{HS}^2.
\]

Dies ist die Summe zweier orthogonaler Projektionsreste. Daher

\[
D_4\ge0,
\qquad
D_4=0
\iff
C_1=g_4W\ \text{und}\ C_2=0.
\]

Nach dem Stabilitätssatz gibt es keine Grade `m>=3`. In genau dieser Klasse
gilt außerdem

\[
\boxed{D_4=D_F}.
\]

Der Grund ist rein orthogonal: `T_1F` trägt genau dieselben Koeffizienten wie
`C_1`, nur als Zwei-Lochzustände des gefüllten Zustands; `T_2F` trägt genau
die normgewichteten Koeffizienten von `C_2`. Der quadratische kinetische Teil
wird durch den Abzug von `E_F` entfernt, und die adjungierten Umwandlungen
vernichten das Bosonvakuum.

Damit kann der bisherige gefüllte `Q=64`-Test algebraisch durch Daten aus
`Q<=4` ersetzt werden. Das ist keine kleine praktische Matrix: Für 64
Fermion- und 60 Bosonmoden hat

\[
C_1: 60\times {64\choose2}=60\times2016,
\]

\[
C_2:{61\choose2}\times{64\choose4}
=1830\times635376,
\]

also über 1,16 Milliarden formale Einträge im zweiten Block. Symmetrie und
Sparsität können diese Zahl reduzieren; der Satz allein tut es nicht.

## 6. Warum es keinen unbedingten Niedrigladungs-Tomographen gibt

Für `n_f>=5` und `kappa>0` ist

\[
R=\kappa\prod_{j=0}^{4}(N_f-j)
\]

selbstadjungiert, `Q`-erhaltend und positiv: Auf einem Zustand mit `n`
Fermionen ist sein Eigenwert null für `n=0,...,4` und positiv für
`n>=5`. Daher

\[
P_{\le4}RP_{\le4}=0,
\qquad R\ne0.
\]

`H` und `H+R` besitzen also dieselbe gesamte `Q<=4`-Kompression und können
beide stabil sein. `R` verletzt jedoch die **globale** untere
Operatorantwort; genau deshalb widerspricht dieses Gegenbeispiel dem
bedingten Satz nicht. Äquivalent kann ein positiver Projektor auf
`N_f>=5` verwendet werden.

Das bloße Prüfen von `H` oder einiger Antwortmittel in niedrigen Sektoren
ersetzt die globalen Operatoridentitäten nicht.

## 7. Audit der stabilen Gegenfamilie `H_eta`

Sei

\[
X=\sum_A b_A^\dagger P_A,
\qquad
H_\eta=H_W+\eta X^2+\bar\eta X^{\dagger2}.
\]

Für reelles `eta` stimmt dies mit der Schreibweise
`eta(X^2+X^{dagger 2})` überein. Es genügt die operatorwertige Bankschranke

\[
\sum_A P_A^\dagger P_A\le K I.
\]

Für den nativen Fall wird `K=480` verwendet. Der Ausgangstext nennt zusätzlich
die per tatsächlicher Teilchen-Loch-Unitäre übertragene Schranke
`sum_A P_A P_A^dagger<=K I`. Sie folgt nicht allein aus der Zahl
`||W||^2=480`, ist für die folgende Abschätzung aber nicht erforderlich.

Für einen normierten Vektor und `n=<N_b>` folgt sogar die etwas stärkere
Zeilenoperator-Schranke

\[
\|X^\dagger\psi\|^2\le Kn,
\qquad
\|X\psi\|^2\le K(n+1).
\]

Hierzu fasst man `P_A` als Spaltenoperator
`P: psi -> (P_A psi)_A` auf. Dann ist `||P||^2<=K`; der
Bosonvernichter-Spaltenoperator hat Quadratnorm `N_b`, und der adjungierte
Erzeuger erhöht die Bosonzahl genau um eins. Die Teilchen-Loch-Schranke ist
für diesen Schritt daher nicht einmal nötig.

Somit

\[
|\langle X^2+X^{\dagger2}\rangle|
\le 2K\sqrt{n(n+1)}
\le 2Kn+K.
\]

Gilt `Omega >= Delta I` und ist
`Delta>2K|eta|`, liefert Youngs Ungleichung

\[
H_\eta\ge
c+e_-(h)
-K|\eta|
-\frac{K|g|^2}{\Delta-2K|\eta|},
\]

wobei

\[
e_-(h)=\min\operatorname{spec}d\Gamma_f(h)
=\sum_{\lambda_a(h)<0}\lambda_a(h)
\]

endlich ist. Für `K=480`, `c=e_-(h)=0` wird daraus die verschärfte Schranke

\[
H_\eta\ge
-480|\eta|I
-\frac{480|g|^2}{\Delta-960|\eta|}I,
\qquad
|\eta|<\frac{\Delta}{960}.
\]

Da `480 <= 28800`, ist die im Ausgangstext angegebene schwächere Schranke mit
`-28800|eta|` ebenfalls eine korrekte **hinreichende Spezialfallschranke**.
Bei allgemeinem `h` fehlt dort lediglich die endliche additive
Fermionkonstante; bei allgemeinem `Omega` muss dessen positive Unterkante
`Delta` eingesetzt werden. Beide Versionen beweisen ausdrücklich, dass
Stabilität einen nichtverschwindenden Grad `m=2` zulässt.

Für den archivierten nativen Tensor bleiben die bereits exakt enumerierten
Zahlen

\[
\|XF\|^2=480,
\qquad
\|X^2F\|^2=439680
\]

und damit

\[
D_F(H_\eta)=439680|\eta|^2>0
\]

für `eta != 0` bestehen. Der kleine Checker dieses Audits rechnet den großen
W-Tensor nicht erneut aus; diese Zahlen werden im separaten nativen Audit dieser Fortsetzung erneut geprüft. Der verwendete Tensor hat SHA-256
`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

## 8. Audit der kinetischen Aussagen

Für

\[
H_{kin}=\sum_{ij}f_i^\dagger h_{ij}f_j
\]

und den vollständig besetzten Fermionzustand `F` gilt exakt

\[
H_{kin}F=(\operatorname{tr}h)F.
\]

Deshalb fällt dieser Anteil aus `(H-E_F)F`, aus `D_F` und aus der Projektion
auf `XF` heraus. Der gefüllte Test bestimmt die Umwandlung, nicht `h`.

Für die Einlochzustände `|i^h>=f_iF` gilt dagegen, auch bei vorhandenen
`T_1,T_2`,

\[
\langle i^h|(H-E_F)|j^h\rangle=-h_{ji}.
\]

Die Umwandlungen ändern die Bosonzahl und haben in dieser direkten
Einlochkompression keinen Matrixanteil. Die Formel rekonstruiert die
quadratische Einteilchenmatrix. Eine Zahlenmatrix `h` ist noch kein
dynamisches Eichfeld, keine Herleitung räumlicher Nachbarschaft und keine
Bestimmung gekleideter physischer Massen.

### Allgemeine Kinetik korrigiert den Momenteninvarianten

Der Wert `349/120` gilt unverändert nur im skalaren Vertrag, in dem der
Einboson-/Zweilochvektor `v=XF` ein Eigenvektor des kinetischen Restes ist.
Setze allgemein

\[
K=d\Gamma_f(h)-\operatorname{tr}(h)I+d\Gamma_b(\Omega),
\qquad \widehat v=v/\sqrt{480}.
\]

Dann ist `KF=0`. Für den nativen Generator ohne direkten `T_2`-Term folgt
aus der Orthogonalität der Fermionloch- und Bosonzahlsektoren

\[
\mu_2=480|g|^2,
\qquad
\mu_3=|g|^2\langle v,Kv\rangle,
\]

\[
\mu_4=|g|^2\|Kv\|^2+670080|g|^4.
\]

Damit gilt exakt

\[
\boxed{
\frac{\mu_2\mu_4-\mu_3^2}{\mu_2^3}
=\frac{349}{120}
+\frac{\operatorname{Var}_{\widehat v}(K)}{480|g|^2}.
}
\]

`349/120` ist in der allgemeinen kinetischen Klasse daher eine Untergrenze,
keine universell unveränderte Gleichheit. Gleichheit gilt genau dann, wenn
`Kv` proportional zu `v` ist. Diese zusätzliche Varianz ist kinetische
Mischung innerhalb des einfachen Umwandlungssektors und kein Beleg für einen
direkten `T_2`-Term; gleichzeitig kann `D_4=D_F=0` gelten.

## 9. Endliches Volumen und Grenzübergang

Der Satz gilt zunächst bei endlich vielen Moden. Für eine Folge endlicher
Volumina `Lambda` bestimmen die jeweiligen `Q<=4`-Blöcke die formalen
Koeffizienten genau dann konsistent, wenn die Daten auf überlappenden lokalen
Unterräumen übereinstimmen. Daraus folgt noch kein selbstadjungierter,
halbbeschränkter unendlicher Generator.

Für den Grenzübergang werden mindestens benötigt:

* kompatible lokale Koeffizienten beziehungsweise ein festgelegtes
  Lokalitätsgesetz;
* volumenunabhängige relative Formschranken und eine kontrollierte
  Energierenormierung;
* Konvergenz der quadratischen Formen oder starke Resolventenkonvergenz;
* ein gemeinsamer dichter Kern und ein Nachweis der Selbstadjungiertheit;
* bei physischer Beschränkung die Verträglichkeit mit dem Eichunterraum.

Eine untere Schranke in jedem endlichen Volumen, die mit dem Volumen gegen
minus unendlich läuft, genügt nicht. Im unendlichen Vakuum-Fockraum existiert
außerdem der global vollständig gefüllte Zustand im Allgemeinen nicht; die
`D_F`-Formulierung ist dann eine endliche-Volumen- oder andere-GNS-Aussage.
Der lokale `D_4`-Block ist konzeptionell besser übertragbar, benötigt aber
weiterhin die genannten Konsistenz- und Existenzbedingungen.

## 10. Exakter kleiner Check

`checker.py` baut für vier Fermion- und eine Bosonmode die vollständige
normierte Besetzungsbasis bis `Q=4` auf und rechnet mit exakten SymPy-Zahlen
und Radikalen. Der ausgeführte Lauf ergab:

* Dimension der kleinen `Q<=4`-Kompression: 28;
* `c,h,Omega,T_1,T_2` vollständig aus den angegebenen Blöcken
  zurückgewonnen;
* `D_4=D_F=188` für einen nichttrivialen exakten Test;
* direkter Vierfermion-zu-Zweiboson-Block bei `T_2=0`: null;
* entsprechender Block von `H^2`: `2 sqrt(2)`;
* versteckter positiver Term `prod_{j=0}^4(N_f-j)`: Werte
  `0,0,0,0,0,120` auf `N_f=0,...,5`;
* native Formdimension von `C_2`: `1830 x 635376`.

Normaler Lauf und `python3 -OO` lieferten dieselbe Ausgabe und endeten mit
`status=PASS`; alle Guards benutzen explizite Ausnahmen und bleiben unter
`-OO` aktiv. Der Check prüft die endliche lineare Algebra und das
Gegenbeispiel, nicht den allgemeinen kohärenten Stabilitätsbeweis und nicht
die Herkunft der Felder aus der TFPT-Quelle.

## Schluss

Die neue Stabilitätsidee liefert einen echten, aber genau begrenzten
Fortschritt: Sie komprimiert die zuvor mögliche Hierarchie von 32 Graden auf
die beiden direkt in `Q=2` und `Q=4` sichtbaren Blöcke. Der stärkere Satz
lautet daher nicht „Niedrigladung bestimmt jeden stabilen Generator“, sondern:

\[
\boxed{
\text{globale untere Antworten}
+\text{volle Fockannahmen}
+\text{globale Stabilität}
\Longrightarrow
\text{vollständige Rekonstruktion aus }Q\le4.
}
\]

Die erste offene physische Implikation liegt davor: Dieselbe primitive Quelle
müsste die CAR/CCR-Felder, die Matrizen `h,Omega`, den W-Block, seine
elementare Zeitordnung und die erforderliche globale Positivität unabhängig
erzeugen. Dafür liegt in diesem Audit weiterhin kein Herkunftsbeweis vor.
