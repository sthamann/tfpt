# Primitive Clock-Dynamik: exakte Antwort und präzise Vakuumgrenze

2026-09-08. Fortsetzung des [Clock-Zensus](../compiler-involution-types/CLOCK_READOUT.md).
Die endliche Operator- und Gibbs-Rechnung dieses Sektors ist geschlossen;
die physikalische TFPT-Zustandswahl, lokale Feldabbildung und das Kontinuum
sind damit nicht hergeleitet. Keine neue Hamiltonian-Kopplung eingesetzt.

## Ergebnis

Die vorhandenen Majorana-Bilineare der primitiven C6-Grade sind dynamisch,
nicht nur algebraisch vorhanden. Zwei erhalten die Gesamtteilchenzahl und
haben die Frequenzbeträge

    (sqrt(3)+1)t,   (sqrt(3)-1)t,

unabhängig von der Grundfrequenz u. Die komplexe Zweipunktfunktion und ihr
thermisches Gewicht folgen exakt aus derselben Quelle. Aber am geprüften
Quellpunkt u=1,t=1/8 verschwinden beide langsamen Kanäle im Grundzustand.
Die drei Bereiche, in denen diese Nulltemperatur-Aussage wechselt, werden
unten vollständig für t>0,u>=0 angegeben. Eine Auswahl des hilfreichen
Bereichs durch TFPT ist nicht bewiesen.

## 1. Quelle und typisierte CAR-Hebung

Unverändert ist D=u A0+t B, mit den originalen reellen antisymmetrischen
16x16-Matrizen, A0=I8 tensor J, J=[[0,1],[-1,0]], und H_source=-iD.
Alle Eingabepins des früheren Extraktors werden vor Verwendung geprüft.
Es gilt exakt [A0,B]=[O,B]=0.

Um Majorana-Bilineare als Operatoren zu untersuchen, verwenden wir die
CAR {gamma_i,gamma_j}=2 delta_ij und die explizite quadratische Hebung

    Hhat=(i/4) sum_ij gamma_i D_ij gamma_j.

Das ist ein Operator auf 2^8=256 Fock-Zuständen, nicht auf den 16 Zuständen
der E8-Ladungszeichen-Darstellung. Es werden keine 16 Erzeugungsmoden
aus den 16 reellen Majorana-Koordinaten gemacht. Der Vorzeichen- und
Normierungsvertrag wird direkt kontrolliert: Für gamma(v)=sum v_i gamma_i
gilt [Hhat,gamma(v)]=i gamma(Dv). Hat Dv=i lambda v, ist das
[Hhat,gamma(v)]=-lambda gamma(v).

In der durch A0 gegebenen komplexen Struktur sind
c_j=(gamma_(2j)+i gamma_(2j+1))/2 und N=sum c_j^*c_j.
Aus [A0,B]=0 folgt [Hhat,N]=0. Mit B=R tensor I+S tensor J,
R^T=-R und S^T=S, ist dieselbe Hebung

    Hhat = c^* [u I+t(S+iR)] c - (1/2) Tr[u I+t(S+iR)].

Auf den Koeffizienten von gamma(v) wirkt die transponierte Matrix
u I+t(S-iR). Diese ist nicht die Fock-Einteilchenmatrix selbst. Beide
haben gleiche Spektren und führende Hauptminoren; ihre Operatorwirkung
darf trotzdem nicht gleichgesetzt werden.

Die Gibbs-Präparation rho_beta=exp(-beta Hhat)/Tr exp(-beta Hhat) wird
ausdrücklich als grandkanonische Wahl erklärt. Die mathematische CAR-Hebung
allein beweist nicht, dass TFPT diese Präparation oder einen konkreten
chemischen Zustand physikalisch auswählt.

## 2. Alle vier primitiven Eigenoperatoren

Die originalen Clock-Sektoren V3 und V4 sind unter D invariant. In ihren
jeweiligen zweidimensionalen internen Koordinaten gilt exakt

    D|V3=(u-t)J,        D|V4=uJ-i sqrt(3)t I.

Eine explizite orthonormale Darstellung benutzt eta=exp(4 pi i/3),

    f3=(0,0,0,1,-1,0,0,0)/sqrt(2),
    f4=(1,eta,eta^2,0,0,0,0,0)/sqrt(3),
    z_s=(1,i s)/sqrt(2),  v_(3,s)=f3 tensor z_s,
    v_(4,r)=f4 tensor z_r,   s,r in {+1,-1}.

J z_s=i s z_s. Die normierten CAR-Operatoren
a_(3,s)=gamma(v_(3,s))/sqrt(2), a_(4,r)=gamma(v_(4,r))/sqrt(2)
erfüllen innerhalb jedes Paares die unabhängigen kanonischen Relationen.
Setze A_sr=a_(3,s) a_(4,r). Diese vier Operatoren bilden den ganzen
primitiven Grad-1-Bilinearraum; ihre Adjungierten bilden Grad 5.

Mit lambda3=s(u-t), lambda4=r u-sqrt(3)t ist

    [Hhat,A_sr]=-Omega_sr A_sr,
    Omega_sr=(s+r)u-(s+sqrt(3))t,
    [N,A_sr]=-(s+r)A_sr.

| s,r | Omega_sr | N-Ladung | Typ |
| --- | --- | ---: | --- |
| +,+ | 2u-(1+sqrt(3))t | -2 | Paarvernichtung bezüglich A0 |
| +,- | -(1+sqrt(3))t | 0 | Transfer zwischen den Carrier-Blöcken |
| -,+ | (1-sqrt(3))t | 0 | Gegenläufiger Transfer |
| -,- | -2u+(1-sqrt(3))t | +2 | Paarerzeugung bezüglich A0 |

Alle sind fermionparität-gerade. Für N3 auf den drei Carrier-Paaren und
N2 auf den zwei Carrier-Paaren gilt [N3,A_sr]=-r A_sr,
[N2,A_sr]=-s A_sr. Die neutralen Operatoren transportieren also Teilchenzahl
zwischen den Blöcken, statt sie zu erzeugen. Sie sind keine einzeln
markierungsneutralen Observablen.

Das ist kein Widerspruch zu einer bereits bewiesenen Erhaltung dieser
beiden Blockzahlen: Diese separate Erhaltung besteht in der Quelle gar
nicht. Genau rank[B,P3]=rank[B,P2]=rank[B,P_B]=4. Marker sind nicht allein
dadurch Gauge-Constraints. Die Quelle erhält N und die Familienwirkung O^2;
A_sr ist unter letzterer geladen. Ob physikalische Observablen unter ihr
invariant sein müssen, muss aus der TFPT-Constraint-Deutung folgen.

Die neuen Operatoren haben ausschließlich P3-P2-Support, keinen Boundary-
Support. Sie sind in der endlichen internen Algebra explizit, aber noch
keine als raumzeitlich lokal nachgewiesenen TFPT-Felder. Neutrale Produkte
wie A_sr^* A_sr sind familieninvariant, nicht A_sr allein.

### Stärkerer Zugangstest: der gesamte bisherige Boundary-Zugang ist blind

Für Pi0=(1/6) sum O^j ist rank Pi0=10. Die tatsächlichen Spalten von
B^k P_B für k=0,...,4 erzeugen genau diesen Fixraum. Für t!=0 gilt das
auch mit D statt B: A0 erhält im(P_B), kommutiert mit D, und
B=(D-uA0)/t. Die erzeugte Boundary-Feldalgebra ist somit Cl_10(C).
Jede primitive Koeffizientenmatrix M erfüllt Pi0 M=M Pi0=0. Ihr gerader
Clifford-Operator kommutiert folglich mit der gesamten Boundary-Feldalgebra,
nicht nur mit den anfänglichen sechs Boundary-Koordinaten.

In der vollen komplexen CAR-Algebra Cl_16(C)=M256(C) ist der Kommutant
dieser M32(C)-Unteralgebra ein M8(C), also 64-dimensional. Die primitiven
Bilineare liefern explizite nichtskalare Elemente. Das ist eine Aussage
über die volle endliche Feldalgebra; eine physikalisch eingeschränkte gerade
Observable-Algebra oder ein anderer Parent ist damit nicht klassifiziert.

Insbesondere verschwindet die lineare Kreuzantwort eines solchen A auf
jedes bisherige Boundary-Observable exakt, weil die betreffenden
zeitentwickelten Operatoren kommutieren. Dies gilt unabhängig von der
Präparation. Kommutation allein bedeutet dagegen nicht statistische
Unkorreliertheit in jedem möglichen verschränkten Zustand.

Damit ist auch bei thermischem Signal oder geändertem u/t noch keine
Boundary-zu-Clock-Brücke gebaut. Ein zusätzlicher, aus TFPT begründeter
Carrier-Zugang beziehungsweise ein anderer belegter Observable-Vertrag
ist zwingend. Der bisherige endliche volle Parent ist nicht minimal aus
diesem Boundary-Feldzugang erzeugt; kein allgemeines No-go für eine andere
TFPT-Vervollständigung folgt daraus.

## 3. Exakte Gibbs-Korrelation, nicht nur ein positives Testsignal

Sei n_beta(lambda)=1/(1+exp(beta lambda)). Die beiden kanonischen Moden
diagonalisieren Hhat unabhängig vom übrigen Spektrum; daher

    w_sr=rho_beta(A_sr^* A_sr)=n_beta(lambda3)n_beta(lambda4),
    wrev_sr=rho_beta(A_sr A_sr^*)=n_beta(-lambda3)n_beta(-lambda4),
    C_sr(tau)=rho_beta(A_sr^*(tau) A_sr)=w_sr exp(i Omega_sr tau),
    rho_beta([Hhat,A_sr]^* [Hhat,A_sr])=Omega_sr^2 w_sr.

Diese Formeln folgen entweder durch diagonalisierten CAR-Produktzustand
oder Wick-Faktorisierung. Sie sind zusätzlich durch direkte Spuren auf dem
vollständigen 256-dimensionalen Fockraum geprüft, ohne eine Kovarianzformel
für diese Gegenrechnung einzusetzen.

Die KMS-Gewichtsrelation ist wrev_sr=exp(beta Omega_sr) w_sr. Das
Kommutatorkorrelat rho([A_sr(tau),A_sr^*]) ist
exp(-i Omega_sr tau)(wrev_sr-w_sr). Bei beta=0 verschwindet es, obwohl
w_sr=1/4 und das zeitabhängige Rauschen nicht verschwinden. Daher wird
dynamische Autokorrelation nicht pauschal mit linearer Antwort gleichgesetzt.
Für beta>0 und Omega_sr!=0 ist auch dieses Kommutatorkorrelat nicht null.

Am ursprünglichen Vergleichspunkt u=1,t=1/8,beta=1:

| Kanal | Frequenzbetrag | rho(A^*A) | rho([H,A]^*[H,A]) |
| --- | ---: | ---: | ---: |
| +,- | 0.3415063509 | 0.2269715953 | 0.0264709227 |
| -,+ | 0.0915063509 | 0.2213111857 | 0.0018531298 |

Das sind quellenbasierte endliche Modellwerte, keine beobachteten
Naturkonstanten und kein experimenteller Beleg der TFPT.

## 4. Warum die beiden langsamen Kanäle im bisherigen Vakuum fehlen

Am Punkt u=1,t=1/8 hat h8=I+(S+iR)/8 die exakten führenden Hauptminoren

    1, 63/64, 61/64, 3721/4096, 14091/16384,
    207095/262144, 94367/131072, 170373/262144.

Alle sind positiv. Nach dem Sylvester-Kriterium ist h8 strikt positiv;
der volle CAR-Hamiltonian hat den eindeutigen A0-leeren Grundzustand mit
E0=-4. Jeder zahlneutrale Transfer enthält einen Vernichter dieses Vakuums.
Sowohl A_+-, A_-+ als auch ihre Adjungierten annihilieren den Grundzustand.
Die langsame Vakuumkorrelation und ihre lineare Antwort sind deshalb exakt
null, nicht nur numerisch klein. Die Paarerzeugungskanäle werden damit
nicht ausgeschlossen, haben hier jedoch Frequenzen der Größenordnung 2u.

Auch der thermische Grenzwert ist kontrolliert:

    w_+- <= exp[-beta (u-t)],
    w_-+ <= exp[-beta (u-sqrt(3)t)]      für u>sqrt(3)t>0.

Die Rückwärtsgewichte verschwinden ebenfalls exponentiell. Die endlichen
positiven Werte aus Abschnitt 3 können also nicht als fertige langsame
Vakuumfelder weiterverwendet werden.

## 5. Präzise Alternative innerhalb der erklärten Parameterfamilie

Für t>0,u>=0 ergibt der feste endliche grandkanonische Nulltemperaturlimes
folgende Vorwärtsgewichte der beiden langsamen Operatoren:

| Bereich | w_+- bei beta→infinity | w_-+ bei beta→infinity |
| --- | ---: | ---: |
| 0<=u<t | 1 | 0 |
| u=t | 1/2 | 1/2 |
| t<u<sqrt(3)t | 0 | 1 |
| u=sqrt(3)t | 0 | 1/2 |
| u>sqrt(3)t | 0 | 0 |

Beweis: Einsetzen von lambda3,lambda4 in n_infinity(lambda)=1 für
lambda<0, 0 für lambda>0 und 1/2 für lambda=0. Andere entkoppelte
Clock-Sektoren ändern dieses reduzierte Gibbs-Produkt nicht, auch wenn
dort zusätzliche Nullmoden auftreten. Die halben Werte wählen eine
thermische Nullmodenmischung, nicht einen beliebigen reinen Grundzustand.

Der Bereich t<u<sqrt(3)t ist somit ein **konkreter Kandidat für eine
zahlneutrale Clock-Antwort im Grundzustand derselben endlichen Familie**.
Bei u=3/16,t=1/8 wurde der vollständige Fockvergleich zusätzlich gerechnet.
Der Parameterwechsel wird nicht als TFPT-Herleitung verbucht. Wir brauchen
eine unabhängige Quellen-Auswahl von u/t oder einen begründeten besetzten
Sektor, und danach weiterhin das geladene räumliche Feld samt Kontinuum.

## 6. Die neue algebraische Zahl und ihre Grenze

Die beiden langsamen Frequenzbeträge haben exakt das Verhältnis

    (sqrt(3)+1)/(sqrt(3)-1)=2+sqrt(3).

Die konjugierte Zahl ist 2-sqrt(3), ihr Produkt ist 1. Die Multiplikation
mit 2+sqrt(3) auf der Basis (1,sqrt(3)) wird durch [[2,3],[1,2]] dargestellt;
deren Eigenwerte sind 2±sqrt(3). Das liefert einen präzisen algebraischen
Vergleich zur logarithmischen Kaskadenidee, keine bloße Dezimalähnlichkeit.

Aber: Die berechnete physische Zeitentwicklung ist exp(-i Omega tau), nicht
Iteration dieser reellen 2x2-Matrix. Ein Frequenzverhältnis macht noch
keinen quellenbestimmten hyperbolischen Transfer und kein Primzahlspektrum.
Kein RH-/Faktorisierungsclaim folgt daraus. Ein behaupteter Anschluss müsste
genau diese fehlende dynamische Operation zuerst aus der Quelle erzeugen.

## 7. Reproduktion und unabhängige Kontrollen

    python3 -B experiments/theory-contracts/clock-bilinear-response/checker.py --fock --output experiments/theory-contracts/clock-bilinear-response/validation.json
    python3 -B -m unittest discover -s experiments/theory-contracts/clock-bilinear-response -p test_checker.py
    python3 -B -OO -m unittest discover -s experiments/theory-contracts/clock-bilinear-response -p test_checker.py

17 Tests je Modus. Alle 256 paarweisen Majorana-CAR-Relationen im
unabhängig aufgebauten Jordan-Wigner-Raum, volle Operator- und Zahl-
Kommutatoren, direkte Gibbs-Spuren an zwei Parameterpunkten, KMS,
exakte Vakuum-Positivität, Nulltemperaturbereiche, Pin-Mutation und
Schutz gegen überstarke Abschlussaussagen. Größter absoluter Unterschied
der vollen Fock-Spuren zur Gewichtsformel: 5.2e-15; zur Kommutatorformel:
5.4e-15. Das sind Kontrollreste endlicher Identitäten, keine Grenzwertrate.

Die unabhängige Prüfung fand zunächst die Verwechslung von Fock-
Einteilchenmatrix und Koeffiziententransponierter im Sylvester-Abschnitt.
Systematische Reproduktion ergab zum falschen Vorzeichen den Matrixrest
0.25, zum richtigen exakt 0. Die Hauptminoren, Frequenzen und Gibbs-Werte
bleiben unverändert. Das Vorzeichen wurde korrigiert und ein direkter
Ein-Teilchen-Sektor-Test gegen den vollständigen Fock-Operator ergänzt.
Diese Korrektur betrifft nur die neue Ableitung, keine fremde Quelldatei.

Methodischer Hintergrund, nicht TFPT-Identifikationsbeweis:
[Surace und Tagliacozzo, Fermionic Gaussian states](https://arxiv.org/html/2111.08343v2),
Abschnitte 3.2, 3.4 und thermische Zustände. Die konkreten Quellen-
Restriktionen und Frequenzen oben wurden hier direkt hergeleitet.

Bestehende Quelldateien, Paper, Website und Abschlussmarker unverändert.
Die bekannte Docstring-Importbesonderheit wird durch den schon geprüften
Adapter behandelt; dessen unveränderte alte ResourceWarning bleibt sichtbar.
Lokal, kein Commit oder Push. Keine T1-T8-/TOE-/RH-Promotion.
