# Primitive Clock-Bilineare: Ladung ist keine Verletzung einer Quellen-Symmetrie

2026-09-08. Unabhängiger, begrenzter Gegencheck der unveränderten
16-Majorana-Quelle. Keine neue Dynamik, Präparation, räumliche Interpretation
oder Identifikation mit E8-Ladungsfeldern wird angesetzt.

## Ergebnis

Genau zwei der vier komplexen primitiven C6-Grad-1-Bilineare erhalten die
Gesamtzahl aus der bereits vorhandenen komplexen Struktur A0. Beide sind
dynamisch nichtstatische Transfers zwischen dem Dreier- und Zweiersektor.
Kein nichtnull primitives Bilinear erhält deren Zahlen separat oder ist unter
der konkreten Familienwirkung O² invariant. Das ist zunächst eine
**Ladungsklassifikation**, kein TFPT-Markierungs- oder Gauge-No-go.

Die Originalquelle erhält die separaten Sektorzahlen selbst nicht. Außerdem
sind diese Clock-Bilineare für den vorhandenen neutralen Boundary-Zugriff
weiterhin unzugänglich. Eine messbare physikalische Brücke bleibt offen.

## Quelle und Konventionen

Verwendet wurde ausschließlich
[`exact_source_prefix()`](../compiler-involution-types/checker.py), mit den
unveränderten dortigen Pins. Der originale Aufbau steht in
[`seam_state_derivation_probe.py`](../../tfpt-discovery/seam_state_derivation_probe.py),
Zeilen 548–627; der Adapter endet vor `Aint_f` und behält alle fünf originalen
Präfix-Prüfungen. Quell-SHA-256:

    5e54c416be72a125a8ce6e235b4300f9f9c2344b3ada796d2dc4c7e2ea01482b

Präfix-SHA-256:

    866a15cefce4a113c292924deb54e28d4d5d8e16506c8c9fc62e0a97b79eaeb0

Auf den acht Zweierpaaren gilt J=A0=I8 tensor [[0,1],[-1,0]], B=A_int,
D=uJ+tB. Die Projektoren P3, P2, PB markieren die ersten drei, nächsten zwei
und letzten drei Paare. Ihre reellen Ränge sind 6, 4, 6. O permutiert die
ersten drei Paare gemäß (1,2,3) -> (3,1,2), tauscht 4 und 5 und fixiert
die Boundary. O² ist die hier konstruierte Familienwirkung.

Für CAR {gamma(v),gamma(w)}=2 v^T w benutzen wir den vorhandenen quadratischen
Lift Hhat_D=(i/4) gamma^T D gamma. Dann

    [Hhat_D, gamma(v)] = i gamma(Dv).

Dies ist von der Hermiteschen Einteilchenmatrix H=-iD zu unterscheiden.
Mit c_j=(gamma_(2j-1)+i gamma_(2j))/2 gilt Hhat_J=Ntotal-4.
Für die drei Sektoren sind die entsprechenden Konstanten 3/2, 1 und 3/2.
Die folgenden Kommutatoren benötigen keine Zustands- oder Vakuumwahl.

## Vollständige primitive Basis und Ladungen

Setze zeta=exp(2 pi i/3), omega=exp(pi i/3), w_s=(1,i s)^T für s=±1.
Im achtteiligen Paarraum seien

    v_(3,s) = (e4-e5) tensor w_s,
    v_(4,r) = (e1+zeta² e2+zeta e3) tensor w_r,
    A_sr = gamma(v_(3,s)) gamma(v_(4,r)),       s,r=±1.

Die Vektoren verschiedener Sektoren sind orthogonal, also ist dieses Produkt
zugleich ihr antisymmetrisiertes Clifford-Bilinear. Direkt aus der Quelle:

    O v_(3,s)=-v_(3,s),       O v_(4,r)=zeta² v_(4,r),
    J v_(3,s)=i s v_(3,s),    J v_(4,r)=i r v_(4,r),
    B v_(3,s)=-i s v_(3,s),   B v_(4,r)=-i sqrt(3) v_(4,r).

Die vier A_sr bilden den ganzen Grad-1-Raum V3 wedge V4. Ihre Adjungierten
bilden den Grad-5-Raum. Damit ist die folgende Klassifikation vollständig
für diese primitive bilineare Komponente, nicht für alle Operatorgrade:

    alpha_O(A_sr) = omega A_sr,
    alpha_(O²)(A_sr) = zeta A_sr,
    alpha_(O³)(A_sr) = -A_sr,
    [N3,A_sr] = -r A_sr,
    [N2,A_sr] = -s A_sr,
    [NB,A_sr] = 0,
    [Ntotal,A_sr] = -(s+r) A_sr.

Gesamtfermionparität ist +1, weil der CAR-Grad gerade ist. Sie darf nicht mit
der Clock-C2-Wirkung O³ verwechselt werden. Die separaten Dreier- und
Zweiersektor-Paritäten geben beide -1. Für Grad 5 sind die komplexen Clock-
und Zahlenladungen entsprechend adjungiert beziehungsweise negiert.

| Anforderung | Komplexe Dimension innerhalb Grad 1 |
| --- | ---: |
| Gesamtfermionparität gerade | 4 |
| Boundary unangetastet; mit ihrer CAR-Algebra kommutierend | 4 |
| Gesamtzahl erhalten | 2 |
| Dreiersektorzahl erhalten | 0 |
| Zweiersektorzahl erhalten | 0 |
| Unter der konkreten Familienwirkung O² invariant | 0 |

Die beiden zahlneutralen Fälle r=-s tragen (N3,N2)-Ladungen (s,-s).
Hermitesche Real- und Imaginärteile erhalten dann ebenfalls Ntotal, aber
weder die separaten Zahlen noch O². In Grad 1 plus Grad 5 existiert auch kein
nichtnull Familien-invariantes hermitesches Element: die beiden Eigenwerte
zeta und zeta-bar sind beide von 1 verschieden.

## Dynamik und die Bedeutung der notwendigen Kreuzstruktur

Für alle vier Operatoren gilt exakt

    [Hhat_D,A_sr] = -Omega_sr A_sr,
    Omega_sr = (s+r)u - (s+sqrt(3))t.

Bei r=-s verschwindet u. Die zwei Beträge sind (sqrt(3)-1)|t| und
(sqrt(3)+1)|t|, ihr Verhältnis ist 2+sqrt(3), sofern t != 0. Das ist eine
endliche Quellenidentität, weder ein Beweis logarithmischer Zeit noch ein
Primzahl-/RH-Mechanismus. Bei t=0 sind gerade diese Transfers statisch.

Die unabhängige Prüfung des zustandsabhängigen Gegenstücks aus
[`clock-bilinear-response/checker.py`](../clock-bilinear-response/checker.py)
bestätigt: Für kanonisch normierte Modenprodukte und ausdrücklich gewählte
großkanonische Gibbs-Präparation ist

    w_sr = <A_sr* A_sr> = n_beta(s(u-t)) n_beta(r u-sqrt(3)t),
    n_beta(x) = 1/(1+exp(beta x)).

Hier ist A kanonisch normiert, anders als die obigen unnormierten
Basisprodukte; das Gewicht der unnormierten Produkte hat den entsprechenden
quadratischen Normfaktor. Für t>0, u>=0 gilt im Gibbs-Grenzwert beta -> infinity:

| Parameterbereich | w_(+,-) | w_(-,+) |
| --- | ---: | ---: |
| u<t | 1 | 0 |
| u=t | 1/2 | 1/2 |
| t<u<sqrt(3)t | 0 | 1 |
| u=sqrt(3)t | 0 | 1/2 |
| u>sqrt(3)t | 0 | 0 |

Die halben Endpunktwerte betreffen den Gibbs-Grenzzustand bei Nullmoden,
nicht jeden beliebig ausgewählten reinen Grundzustand. Insbesondere bleiben
am geprüften Quellenpunkt u=1,t=1/8 beide langsamen Kanäle im Vakuum dunkel.
Bei beta=0 sind Vorwärts- und Rückwärtsgewicht beide 1/4: Eine positive
quadratische Schwankung ist daher nicht automatisch ein nichtnull
retardierter Kommutator. Die Auswahl eines anderen Parameterfensters ist
keine TFPT-abgeleitete Reparatur.

Beim direkten Vergleich des Jordan-Wigner-Einteilchenblocks wurde außerdem
ein Vorzeichen-/Transpositionsfehler im zunächst gelesenen Comparator
identifiziert und dem Besitzer gemeldet: Mit der obigen c-Konvention und
R=B[::2,::2], S=B[::2,1::2] ist die Matrix in c* h c gleich
h=u I+t(S+iR), während S-iR auf den linear mit Koeffizienten kontrahierten
Vektoren wirkt. Die beiden Matrizen sind transponiert und haben dieselben
führenden Hauptminoren. Deshalb bleiben die positive Definitheit und das
Vakuum-Zertifikat erhalten. Diese Diagnose verwendete das vollständig
gelesene systematische Debugging-Verfahren und einen direkten 256D-Fock-
Blockvergleich; keine fremde Datei wurde verändert.

Jeder reine primitive Grad-1-Operator hat Koeffizientenmatrix
M=v3 v4^T-v4 v3^T, beziehungsweise eine Linearkombination dieser vier Matrizen.
Er liegt zwingend in den Kreuzblöcken P3 M P2 und P2 M P3. Für jedes
nichtnull reine Grad-1-Element sind alle sechs 3-mal-2 Paar-Kreuzblöcke
nichtnull: ihre Koeffizienten sind dieselbe nichtnull interne 2x2-Matrix,
multipliziert mit den sechs Fourier-Phasen. Eine einzelne lokale Kanalkante
allein ist daher kein reiner primitiver Clock-Eigenoperator. Eine räumliche
Nichtlokalitätsbehauptung folgt daraus nicht; die Kanalmarkierung ist noch
keine abgeleitete Raumgeometrie.

Diese Kreuzstruktur betrifft den **Operator**, nicht einen neu benötigten
Hamiltonian-Term. Der unveränderte D ist O-invariant; ein geladener
Eigenoperator darf trotzdem eine nichtverschwindende Zeitentwicklung haben.
Insbesondere liegt der vorhandene Hamiltonian-Kreuzblock P3 B P2 nur im
Clock-Fixraum Pi0=(1/6) sum_(k=0)^5 O^k:

    P3 B P2 = Pi0 P3 B P2 Pi0.

## Warum kein Markierungs-No-go folgt – und welcher Zugang noch fehlt

Direkt auf den gepinnten Originalmatrizen ergibt sich

    [B,J]=0,
    rank[B,P3]=rank[B,P2]=rank[B,PB]=4,
    rank[B,P3 J]=rank[B,P2 J]=rank[B,PB J]=4,
    rank(P3 B P2)=rank(P3 B PB)=rank(P2 B PB)=2.

Somit ist Ntotal eine Symmetrie der gekoppelten Quelle, die drei separaten
Zahlen bei t != 0 jedoch nicht. Die Existenz von Markerprojektoren allein
postuliert keine Superselektionsregel. Sollte TFPT unabhängig beweisen,
dass O² als Gauge-Redundanz dividiert werden muss und physische Observablen
unter genau dieser Wirkung invariant sein müssen, wären die primitiven
Einzeloperatoren ohne weitere geladene Ergänzung ausgeschlossen. Eine solche
Zusatzregel wird durch diesen Gegencheck weder abgeleitet noch angenommen.

Umgekehrt erhält O den gesamten Boundary-erzeugten Raum im Clock-Fixraum.
Für jedes primitive M gilt stärker

    Pi0 M = M Pi0 = 0.

Der entsprechende gerade CAR-Operator kommutiert deshalb mit jeder
gamma(D^n b), b in im(PB), n>=0, und mit der daraus erzeugten Algebra.
Die neue primitive Dynamik repariert also nicht den bisherigen neutralen
Boundary-Zugang. Kommutation allein beweist keine statistische
Unkorreliertheit in jedem denkbaren Zustand.

**Nächster scharfer Gate:** aus derselben TFPT-Quelle einen erlaubten
Carrier-Zugriff und seine Präparation herleiten, der eines der beiden
zahlneutralen A_(s,-s) oder eine geeignete neutrale Zweipunktantwort tatsächlich
erreicht. Ein vorhandener Marker ist noch keine Gauge-Ladung; ein algebraisch
existierender Operator ist noch kein physikalisch erreichbarer Readout.

## Unabhängiger Reproduktionskern

Vom Repository-Stamm aus kann der folgende reine Lesetest mit `python3 -B -`
oder `python3 -B -OO -` ausgeführt werden. Der lokale Adapter kompiliert die
gepinnten Legacy-Assertions mit optimize=0; das ist keine OO-Härtung der
Originalquelle. Die hier geprüften Bedingungen benutzen explizite Fehler.
Normaler Modus und OO-Modus wurden am 2026-09-08 erfolgreich geprüft.

```python
import importlib.util
from pathlib import Path
import sympy as S

p = Path('experiments/theory-contracts/compiler-involution-types/checker.py')
spec = importlib.util.spec_from_file_location('clock_audit_source', p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
d = m.exact_source_prefix()
J, B = S.Matrix(d['A16_dep']), S.Matrix(d['A_int'])
O = S.zeros(16)
for i, k in enumerate(d['img']):
    O[k, i] = 1
P3 = S.diag(*([1]*6+[0]*10))
P2 = S.diag(*([0]*6+[1]*4+[0]*6))
PB = S.eye(16)-P3-P2
Pi0 = sum((O**k for k in range(6)), S.zeros(16))/6
zeta, omega = (-1+S.sqrt(3)*S.I)/2, (1+S.sqrt(3)*S.I)/2
u, t = S.symbols('u t', real=True)
D = u*J+t*B

def check_zero(x):
    if S.simplify(x) != S.zeros(*x.shape):
        raise ValueError('exact identity failed')

check_zero(B*J-J*B)
check_zero(P3*B*P2-Pi0*P3*B*P2*Pi0)
for s in (-1, 1):
    v3 = S.kronecker_product(S.Matrix([0,0,0,1,-1,0,0,0]),
                             S.Matrix([1,S.I*s]))
    for r in (-1, 1):
        v4 = S.kronecker_product(S.Matrix([1,zeta**2,zeta,0,0,0,0,0]),
                                 S.Matrix([1,S.I*r]))
        M = S.simplify(v3*v4.T-v4*v3.T)
        Omega = (s+r)*u-(s+S.sqrt(3))*t
        check_zero(O*M*O.T-omega*M)
        check_zero(O**2*M*(O**2).T-zeta*M)
        check_zero(D*M+M*D.T-S.I*Omega*M)
        check_zero(P3*J*M+M*(P3*J).T-S.I*r*M)
        check_zero(P2*J*M+M*(P2*J).T-S.I*s*M)
        check_zero(Pi0*M)
        check_zero(M*Pi0)
        print(s, r, Omega, 'total-number charge', -(s+r))
print('marker-commutator ranks', [(B*P-P*B).rank() for P in (P3,P2,PB)])
```

Keine anderen Dateien verändert; keine Statuspromotion, kein Commit/Push.
