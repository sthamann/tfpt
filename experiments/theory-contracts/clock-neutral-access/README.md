# Kleinster neutraler Clock-Zugang: Quadratik-Grenze und quartischer Zeuge

2026-09-08. Begrenzte Fortsetzung von
[clock-bilinear-response](../clock-bilinear-response/README.md) und
[clock-marking-audit](../clock-marking-audit/README.md).

**Ergebnis:** Mit Erhaltung der vollständigen Quellen-Clock O und der
Gesamtzahl N ist CAR-Grad vier der kleinste gerade Grad einer echten
Boundary/Clock-Wechselwirkung. Zwei explizite quartische Terme erlauben eine
neutrale Randkorrelation, aus deren vier Linien die gemeinsame Besetzung
zweier dunkler Moden rekonstruiert werden kann. Dazu gehört das Gewicht
des primitiven Clock-Bilinears A* A. Der primitive Einzeloperator bleibt
geladen. Unter O² **allein** ist dagegen bereits eine bestimmte quadratische
Anbindung zulässig; dieser Unterschied darf nicht unterschlagen werden.

Die Terme und die Probe-Präparation sind deklarierte Modellvariationen auf
derselben vorhandenen 16-Majorana-Algebra. Weder ihre Auswahl durch TFPT noch
eine räumliche Feldabbildung oder ein Kontinuum wurden hergeleitet.

## 1. Warum die Quadratik nur unter vollständigem O ausgeschlossen ist

Die komplexifizierten Boundary-Koordinaten haben ausschließlich Clock-Grad
0; die sechs dunklen Koordinaten haben Grade 2, 3, 4 mit Dimensionen 2, 2, 2.
Ein gemischtes Bilinear liegt in V_B wedge V_dark. Sein Grad ist folglich
2, 3 oder 4 und niemals 0. Kein nichtnull solches Bilinear ist O-invariant.
Skalare koppeln keine Sektoren; somit liegt der niedrigste mögliche gerade
Grad mindestens bei vier.

Bezüglich der originalen A0-Komplexstruktur gibt es drei komplexe Boundary-
Moden und je eine dunkle Vernichtungsmode in den Clock-Graden 2, 3, 4. Die
N-neutralen gemischten quadratischen Monome sind b_j* d_k und ihre
Adjungierten. Ihre komplexifizierten Graddimensionen sind jeweils 6 für
Grad 2, 3 und 4. Unter O² wird Grad 3 neutral. Daher hat der O²- und
N-invariante gemischte quadratische Raum Dimension 6; sein hermitescher
Teil hat reelle Dimension 6. Ein expliziter Zeuge ist

    T = b1* d3 + d3* b1,
    alpha_O(T)=-T,   alpha_(O²)(T)=T,   [N,T]=0.

Dies koppelt nur den C2-ungeraden, familienfixen Clock-Teil an. Es ist kein
voller C6-erhaltender Zugang zu einem primitiven Grad-1-Einzeloperator.
Die unter voller O-Erhaltung gerade bewiesene Quadratik-Grenze bleibt gültig.

Auch der niedrigste vollständige gemischte Grad-4-Raum lässt sich klein
klassifizieren. Neben B (sechs Boundary-Felder) und D (sechs dunkle Felder)
gibt es F (vier weitere Clock-fixe Carrier-Felder). Die ganze Quelle hat
fünf komplexe Clock-fixe und je eine komplexe Mode der Grade 2, 3, 4.
Das gemeinsame Clock-/N-Spektrum wird direkt aus der originalen Paar-
Permutation geprüft. Unter O und N invariant, mit mindestens einem B-
und einem D-Feld, ergeben die äußeren Monome exakt:

| Reiner CAR-Grad-4-Support | Komplexe Dimension |
| --- | ---: |
| Zwei B- und zwei D-Felder | 33 |
| Ein B-, ein F- und zwei D-Felder | 48 |
| Alle anderen gemischten Verteilungen | 0 |

Insgesamt sind es 81 komplexe Richtungen; der hermitesche Teil hat
entsprechend 81 reelle Dimensionen. Der unten benutzte Zeuge liegt im
33-dimensionalen ersten Teil. Diese Zählung klassifiziert die angegebenen
zwei Symmetrien, nicht sämtliche unbekannten physikalischen TFPT-Constraints.

## 2. Ausschließlich vorhandene Moden der gepinnten Quelle

Wir behalten c_j=(gamma_(2j-1)+i gamma_(2j))/2 und
H0=(i/4) gamma^T(u A0+t B) gamma bei. In den acht ursprünglichen Paaren:

    b1 = (c6-c7)/sqrt(2),
    b2 = (c6+c7-2c8)/sqrt(6),
    d3 = (c4-c5)/sqrt(2),
    d4 = (c1+zeta c2+zeta² c3)/sqrt(3),
    zeta=exp(2 pi i/3).

Die beiden b-Moden liegen vollständig in der ursprünglichen Boundary und
in ker B. Die vier Moden sind orthonormal bezüglich der CAR. Direkt aus
derselben Quelle folgen

    [H0,b1]=-u b1,          [H0,b2]=-u b2,
    [H0,d3]=-(u-t)d3,       [H0,d4]=-(u+sqrt(3)t)d4,
    alpha_O(b1)=b1,         alpha_O(b2)=b2,
    alpha_O(d3)=-d3,        alpha_O(d4)=zeta d4.

Damit ist A=d3 d4* genau der schon vorhandene zahlneutrale primitive Kanal
A_(+,-), mit alpha_O(A)=omega A, omega=exp(pi i/3), und

    A* A = n3(1-n4),   n_j=d_j* d_j.

Es wurden keine zusätzlichen Moden oder ein unabhängiges Hilbert-Raum-
Tensorprodukt eingeführt. Der Prüfer rechnet mit geordneten Monomen der
originalen sechzehn gamma_i und überprüft alle 256 ursprünglichen CAR-
Relationen. Diese Clifford-Algebra ist dieselbe volle CAR-Algebra wie zuvor.

## 3. Ein minimaler reiner CAR-Grad-4-Zeuge

Schreibe q_a=n_a-1/2. Jedes q_a ist rein quadratisch in Majoranas. Wegen
orthogonaler Boundary- und Carrier-Unterräume ist

    K = q_b1 (g3 q_d3 + g4 q_d4)

rein CAR-Grad vier: jeder Monomterm enthält genau zwei Boundary- und zwei
Carrier-Majoranas. Für reelle g3,g4 gilt exakt

    K*=K,   alpha_O(K)=K,   [N,K]=0,   [H0,K]=0.

Der neue Hamiltonian ist ausdrücklich H_g=H0+K, nicht die unveränderte
TFPT-Quelle. Die freien Kopplungen sind zusätzliche Modellauswahl. Der
Zeuge erlaubt eine Informationskopplung, keinen Teilchentransfer zwischen
Boundary und Carrier; er erhält deren getrennte Zahlen sogar selbst.
Er begründet keine räumliche Lokalität aus den Kanalbezeichnungen.

Dass K mit H0 kommutiert, macht die Kopplung nicht trivial: Die neutrale
Boundary-Observable X=b1* b2 erfüllt

    [H0,X]=0,
    [K,X]=X F,    F=g3 q_d3+g4 q_d4,
    X(tau)=X exp(i F tau).

Die vier gemeinsamen Carrier-Projektoren P_(a,b), a,b in {0,1}, liefern
die exakten Eigenoperatoren X P_(a,b) mit Frequenzen

    F_(a,b)=g3(a-1/2)+g4(b-1/2).

Diese vier Zahlen sind genau dann verschieden, wenn g3 und g4 beide
nichtnull sind und g3 != g4 sowie g3 != -g4. Für gleiche Kopplungen fallen
zwei Linien zusammen; dann können die beiden mittleren Besetzungen aus
diesem einen Zugriff nicht getrennt werden. Der Prüfer enthält diesen
negativen Kontrollfall.

Der primitive Operator selbst wird nicht invariant gemacht. Auch seine
Dynamik ist durch die Probe verändert:

    [H_g,A]=[-Omega+(g4-g3)q_b1] A,
    Omega=-(1+sqrt(3))t.

Deshalb wird das ausgelesene A* A-Gewicht nicht stillschweigend mit dem
vollständigen ungestörten Zwei-Zeit-Kern bei beliebiger endlicher
Messkopplung gleichgesetzt.

## 4. Explizite neutrale Korrelation – und die Nichtantwort daneben

Für eine deklarierte, in den gewählten Besetzungen diagonale
Produktpräparation sei p_(a,b) die gemeinsame Carrier-Verteilung,
r_f=Pr(n_b1=0,n_b2=1), r_r=Pr(n_b1=1,n_b2=0). Dann

    <X*(tau) X> = r_f sum_(a,b) p_(a,b) exp(-i F_(a,b) tau),
    <[X(tau),X*]> = (r_r-r_f) sum_(a,b) p_(a,b) exp(i F_(a,b) tau).

Bei vier aufgelösten Linien und bekanntem r_f>0 erhält man aus der Linie
(a,b)=(1,0) exakt

    <A* A> = p_(1,0) = Gewicht_der_Linie_(1,0) / r_f.

Dies ist ein neutraler Zugriff auf die gemeinsame Besetzung, keine
Messung des geladenen Einpunktmittels <A>. Für verschränkte oder unbekannte
Boundary/Carrier-Präparationen liefern die Linien zunächst gemeinsame
bedingte Gewichte; die einfache Division ist dann nicht gerechtfertigt.

**Vorhandene thermische Quellen-Präparation:** Für das bereits deklarierte
rho0 proportional exp(-beta H0) ist die benötigte Faktorisierung exakt,
weil die vier gewählten Moden eigenständig diagonalisieren. Es gilt

    n3=n_beta(u-t),  n4=n_beta(u+sqrt(3)t),
    p_(a,b)=n3^a(1-n3)^(1-a) n4^b(1-n4)^(1-b),
    r_f=r_r=n_beta(u)(1-n_beta(u)).

Da [H0,K]=0, bleibt rho0 unter H_g stationär; es ist im Allgemeinen nicht
der Gibbs-Zustand des variierten Hamiltonians. Für endliche beta gibt es
vier positive Rauschgewichte, aber der obige retardierte Kommutator ist
**exakt null**. Die entarteten Boundary-Moden sind gleich besetzt.

Am bisherigen Punkt u=1,t=1/8,beta=1 rekonstruiert der Zugriff
p_(1,0)=0.2269715953, also dasselbe primitive neutrale Gewicht wie zuvor.
Die Kopplungswerte g3=1/64,g4=1/32 dienen im Prüfer ausschließlich als
rationale, nichtentartete Zeugen. Sie sind keine vorhergesagten Konstanten.
Die Linien sind dann {-3,-1,1,3}/128; über die Periode 256 pi ergibt
die entsprechende Fourier-Koeffiziente die vier Gewichte exakt. Insbesondere
ist p_(1,0) die Koeffiziente der Frequenz -1/128, geteilt durch r_f.
Im Grenzwert verschwindender Messkopplung kollabieren die Linien wieder;
die zur Trennung erforderliche Beobachtungszeit wächst. Das ursprüngliche
Clock-Blindheitsresultat bei K=0 wird nicht umgangen.

**Expliziter Response-Zeuge:** Präpariert man die vorhandenen Boundary-
Moden in |n_b1,n_b2> = |0,1>, so ist r_f=1,r_r=0. Bei derselben diagonalen
Carrier-Verteilung sind die vier Kommutatorgewichte -p_(a,b) nichtnull.
Die Präparation ist N-definit auf diesen zwei Boundary-Moden und O-invariant,
aber eine zusätzliche Probe-Wahl, keine aus TFPT abgeleitete Präparation.
Sie demonstriert eine mögliche lineare Antwort, nicht deren Existenz im
bisherigen Quellvakuum.

## 5. Das vorhandene Vakuum bleibt dunkel

Am bisherigen Quellenpunkt hat h8=I+(S+iR)/8 durch exakte Gershgorin-
Zeilenschranken einen kleinsten Eigenwert mindestens 1/8. H0 besitzt den
leeren, eindeutigen A0-Grundzustand. Für die angegebenen rationalen
Zeugenkopplungen gilt

    2 ||K|| <= (|g3|+|g4|)/2 = 3/128 < 1/8.

K erhält das Vakuum als Eigenvektor; die Schranke verhindert einen
Grundzustandswechsel. Dort annihilieren X und X* den Zustand, und
n3(1-n4)=0. Sowohl die Boundary-Korrelation als auch die primitive langsame
Vakuumantwort bleiben null. Eine quartische Informationskopplung allein
ersetzt die fehlende besetzte beziehungsweise thermische Präparation nicht.

## 6. Was geschlossen ist und der nächste kleine Gate

Geschlossen sind die O-versus-O²-Auswahlregel, der minimale gerade Grad
unter voller O-Erhaltung und ein exakter quartischer Zugriff auf ein
neutrales primitives Korrelationsgewicht in derselben endlichen Algebra.
Die ursprüngliche Aussage über Clock-Blindheit gilt weiterhin für H0;
H_g ist ausdrücklich eine neue Kopplungsvariation.

Der Zeuge liefert außerdem keine volle Erzeugtheit der dunklen CAR-Algebra:
Sowohl n3 als auch n4 kommutieren mit H_g und mit jedem anfänglichen
Boundary-Operator. Nach der Jacobi-Identität gilt das für die gesamte daraus
dynamisch erzeugte Algebra. Die ausgelesene dunkle Information ist hier
besetzungsdiagonal; ein Operator wie A, der diese Besetzungen ändert, wird
dadurch nicht erzeugt. Das volle Common-Parent-/Kommutantenproblem bleibt
offen. Allgemeiner kann eine O-invariante Dynamik aus ausschließlich
O-invarianten Boundary-Operatoren keinen geladenen Einzeloperator erzeugen.

Als nächster Gate ist aus der TFPT-Quelle zu entscheiden, ob eine solche
gemischte quartische Wechselwirkung zulässig oder erzeugt ist und welcher
besetzte Zustand beziehungsweise welche Probe-Präparation tatsächlich
ausgewählt wird. Dieser Zeuge bietet dafür einen kleinen, falsifizierbaren
Operatorvertrag. Er löst keine T1-T8-, Raumzeit-, E8-Feld- oder RH-Pflicht.

## Reproduktion

    python3 -B experiments/theory-contracts/clock-neutral-access/checker.py
    python3 -B -m unittest discover -s experiments/theory-contracts/clock-neutral-access -p test_checker.py
    python3 -B -OO -m unittest discover -s experiments/theory-contracts/clock-neutral-access -p test_checker.py

Der Adapter und alle ursprünglichen Quellen werden vor Konstruktion über
SHA-256-Pins geprüft. Die bekannte Legacy-Docstring/Assertion-Behandlung
bleibt im unveränderten Adapter; dies ist keine OO-Härtung der Originalquelle.
Die neue Algebra und alle neuen Guards laufen auch unter OO.

Ein anfänglicher Prüffehler wurde mithilfe des vollständig gelesenen
`systematic-debugging`-Skills auf verschiedene faktorisierte Schreibweisen
identischer Radikalkoeffizienten zurückgeführt. Ihre exakte Differenz war
null. Die gemeinsame Koeffizienten-Normalisierung wurde erweitert und ein
Regressionsfall hinzugefügt; weder die Clock-Phase noch ein Quellenoperator
wurde geändert. Details und abschließende Ergebnisse stehen in
[TEST_RESULTS.md](TEST_RESULTS.md).

Nur dieses neue Experimentverzeichnis verändert. Keine Indizes, Quellen,
Paper, Website, Abschlussmarker, Commits oder Pushes.
