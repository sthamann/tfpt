# Tatsächliche QWZ-Kovarianz am PS.DIRAC.03-Quellenanschluss

Stand: 21. September 2026  
Verdict: **Der geprüfte unveränderte Drei-Moden-Carrier nähert sich dem reinen
NS-Projektor. Er liefert keinen stabilen treuen endlichen modularen
Yukawablock.** Das ist ein enger Quellenbefund, kein allgemeines TFPT-No-go.

## Frage und unveränderte Quelle

`PS.DIRAC.03` verwendet die korrekte Standardidentität

\[
D_{\rm mod}=\log((1-C_F)C_F^{-1}).
\]

Im vorhandenen `v258` wird jedoch zuerst ein gewünschtes `D` gewählt und
anschließend `C_F=(1+e^D)^{-1}` gebildet. Die hier geprüfte physische Richtung
ist die Umkehrung: Was ergibt sich aus der bereits vorhandenen QWZ-Quelle ohne
Ziel-Yukawa?

Verwendet wurden ausschließlich

- der width-8, mass-1, sector-1 QWZ-Hamiltonoperator `h_N`;
- sein gefüllter Zustand `P_N=1_(h_N<0)`;
- der korrekt skalierte Zeitgenerator `D_N=N h_N/(2π)`;
- derselbe rohe Top-row-Fourierblock `R_N` mit den Labels `j=(-1,0,1)`, der
  zuvor im Charged-CAR-Quellencheck benutzt wurde.

Es gibt keine Fitparameter. Weil die numerische Gram-Matrix ohnehin bis auf
`6.1e-16` die Identität ist, ändert die klar benannte Basisnormierung

\[
S_N=R_N(R_N^\dagger R_N)^{-1/2}
\]

keinen physikalischen Inhalt. Sie sorgt nur für `S_N†S_N=I`.

## Berechnete Objekte

Die tatsächliche komprimierte Kovarianz ist

\[
A_N=S_N^\dagger P_NS_N.
\]

Zusätzlich wurden ohne Eigenwert-Clipping berechnet:

\[
\|A_N-A_N^2\|,
\]

\[
E_N=S_N^\dagger P_N(1-S_NS_N^\dagger)P_NS_N,
\]

\[
\operatorname{logit}(A_N)=\log((1-A_N)A_N^{-1}),
\]

und die ersten beiden echten Zeitmomente

\[
B_N=S_N^\dagger D_NS_N,\qquad
M_N^{(2)}=S_N^\dagger D_N^2S_N,
\]

mit dem Defekt

\[
V_N=M_N^{(2)}-B_N^2
=((1-S_NS_N^\dagger)D_NS_N)^\dagger
 ((1-S_NS_N^\dagger)D_NS_N).
\]

Die beiden positiven Gramidentitäten wurden direkt geprüft:

\[
E_N=A_N-A_N^2,\qquad
V_N=(Q_ND_NS_N)^\dagger Q_ND_NS_N,\quad Q_N=1-S_NS_N^\dagger.
\]

## Analytischer Quellenabschluss

Der Grenzschluss folgt direkt aus der originalen QWZ-/Fourierdefinition und
nicht aus drei numerischen Datenpunkten. Um eine Verwechslung mit dem im
Quellenbericht anders verwendeten \(k_j=j-1/4\) zu vermeiden, sei hier

\[
\theta_{N,j}={2\pi(j-1/4)\over N}.
\]

Für den normierten rohen oberen Randspinor \(R_{N,j}\) gilt exakt

\[
h(\theta)r=-\sin\theta\,r+(1-\cos\theta)\chi_-,
\qquad \langle r,\chi_-\rangle=0.
\]

Mit \(D_N=Nh_N/(2\pi)\) erhält man daher

\[
d_{N,j}:=\langle R_{N,j},D_NR_{N,j}\rangle
=-{N\over2\pi}\sin\theta_{N,j},
\]

\[
\langle D_N^2\rangle_{N,j}
=\left({N\over2\pi}\right)^2 4\sin^2(\theta_{N,j}/2),
\]

und somit exakt

\[
\boxed{\operatorname{Var}_{N,j}(D_N)
=\left({N\over2\pi}\right)^2(1-\cos\theta_{N,j})^2.}
\]

Verschiedene \(j\) bleiben wegen der longitudinalen Translation orthogonal;
alle drei Momentmatrizen sind also in dieser Fourierbasis diagonal.

Sei \(\mu_{N,j}\) das Spektralmaß von \(D_N\) im Zustand \(R_{N,j}\). Hat
\(d_{N,j}\) das positive Vorzeichen, ist die negative Spektralhälfte eine
Falschbesetzung; bei negativem \(d_{N,j}\) ist es die positive Hälfte.
Chebyshev liefert in beiden Fällen

\[
p^{\rm wrong}_{N,j}
\le {\operatorname{Var}_{N,j}(D_N)\over d_{N,j}^2}
=\tan^2(\theta_{N,j}/2).
\]

Für \(j=(-1,0,1)\) ist der größte Betrag \(|j-1/4|=5/4\). Deshalb

\[
\boxed{\|A_N-\operatorname{diag}(0,0,1)\|
\le b_N:=\tan^2\!\left({5\pi\over4N}\right)\longrightarrow0.}
\]

Für \(N\ge8\) gilt \(b_N<1/2\). Ist ein Eigenwert bereits exakt \(0\) oder
\(1\), ist sein Logit mathematisch singulär. Für jeden endlichen Logit folgt
andernfalls

\[
\boxed{|\ell_{N,j}|\ge
\log\!\left({1-b_N\over b_N}\right)\longrightarrow\infty.}
\]

Damit ist analytisch ausgeschlossen, dass dieses echte feste Quellfenster bei
festem modularen Maßstab gegen einen vollen treuen endlichen KMS-/Diracblock
konvergiert. Der Satz betrifft genau diese QWZ-Kompression; er sagt nichts
über einen noch herzuleitenden anderen physischen Carrier.

## Rohzahlen

Die Eigenwerte sind jeweils aufsteigend sortiert.

| `N` | Eigenwerte von `A_N` | `||A_N-A_N²||` | Logit-Eigenwerte, ohne Clipping |
|---:|---|---:|---|
| 8 | `0.0001492504, 0.0339818187, 0.9927387823` | `0.0328270547` | `8.8097361, 3.3473570, -4.9179200` |
| 16 | `0.0000104625, 0.0039883174, 0.9993315303` | `0.0039724108` | `11.4677042, 5.5203895, -7.3098509` |
| 32 | `0.0000006899, 0.0003430027, 0.9999499299` | `0.0003428850` | `14.1867057, 7.9774292, -9.9020369` |

Die analytischen uniformen Schranken sind:

| \(N\) | \(b_N=\tan^2(5\pi/(4N))\) | garantierte Untergrenze jedes endlichen \(|\operatorname{Logit}|\) |
|---:|---:|---:|
| 8 | 0.2857021545 | 0.9163501758 |
| 16 | 0.0627437172 | 2.7038983099 |
| 32 | 0.0152123205 | 4.1703204058 |

Nach ursprünglichem Modenlabel ist die Diagonale:

| `N` | `j=-1` | `j=0` | `j=1` |
|---:|---:|---:|---:|
| 8 | `0.0339818187` | `0.0001492504` | `0.9927387823` |
| 16 | `0.0039883174` | `0.0000104625` | `0.9993315303` |
| 32 | `0.0003430027` | `0.0000006899` | `0.9999499299` |

Offdiagonale Einträge liegen nur auf Rundungsniveau. Damit nähert sich

\[
A_N\longrightarrow \operatorname{diag}(0,0,1)=P_{\rm NS}
\]

im geprüften Modenfenster.

Die Eigenwerte des Block-Entanglement-Grams `E_N` lauten:

| `N` | Eigenwerte von `E_N` | Identitätsresiduum `||E_N-(A_N-A_N²)||` |
|---:|---|---:|
| 8 | `0.0001492281, 0.0072084924, 0.0328270547` | `8.12e-17` |
| 16 | `0.0000104624, 0.0006680228, 0.0039724108` | `2.73e-16` |
| 32 | `0.0000006899, 0.0000500676, 0.0003428850` | `2.22e-16` |

Er verschwindet gemeinsam mit dem Projektordefekt. Die endlichen inneren
Eigenwerte sind daher Leakage aus der nicht exakt invarianten rohen
Top-row-Basis, keine sich stabilisierende gemischte Carrierkovarianz.

Die echten Zeitmomente zeigen dasselbe Bild:

| `N` | Eigenwerte von `S_N†D_NS_N` | Eigenwerte von `V_N` |
|---:|---|---|
| 8 | `-0.7073740, 0.2483967, 1.0586600` | `0.0005985, 0.0460444, 0.3202038` |
| 16 | `-0.7392039, 0.2495986, 1.2004019` | `0.0001504, 0.0120232, 0.0904115` |
| 32 | `-0.7472922, 0.2498996, 1.2374879` | `0.0000376, 0.0030386, 0.0232958` |

Die ersten Momente nähern sich dem wirklichen Quellspektrum

\[
(-3/4,1/4,5/4),
\]

und der positive zweite Momentdefekt geht gegen null. Die Residuen der
Gramidentität für `V_N` liegen bei `6.98e-16, 1.47e-15, 8.06e-15`.

## Entscheidung für PS.DIRAC.03

Für jedes endliche `N` sind alle drei Eigenwerte von `A_N` strikt zwischen
null und eins. Rein mathematisch existiert daher jeweils ein endlicher
modularer Logit. Dieser endliche Logit ist aber **nicht stabil**:

- zwei Kovarianzeigenwerte laufen gegen null;
- einer läuft gegen eins;
- die entsprechenden Logits laufen gegen `+∞,+∞,-∞`;
- Projektordefekt, Entanglement-Gram und Zeitmomentdefekt verschwinden;
- die Zeitmomente konvergieren zum unveränderten linearen NS-Spektrum.

Der exakte Chebyshev-/Fourierbound beweist somit für dieses feste Modenfenster
den bekannten reinen NS-Projektor; die Rohzahlen illustrieren nur die
Konvergenzrate. Die Quelle liefert hier keinen treuen endlichen modularen
Yukawablock mit stabilen endlichen Eigenwerten oder chiralen
Offdiagonal-Massen.

Das berührt nicht die exakte algebraische Inversionsidentität von `v258` und
auch nicht bereits geschlossene Yukawaformeln innerhalb ihres Vertrags. Es
zeigt nur: Die dortige physische Gleichsetzung
`C_F=P_F C_Σ P_F` ist durch diesen tatsächlichen einquelligen QWZ-Carrier
nicht realisiert. `R_N` ist außerdem nicht der physische 48/96-Träger.

## Bedingter KMS-Kontrollzweig

Als ausdrücklich bedingte Kontrolle wurde derselbe unveränderte Grenzgenerator

\[
h(r)=r-1/4
\]

in seinem KMS-Zustand bei allgemeinem, zusätzlich gesetztem `β` betrachtet:

\[
C_\beta(r)={1\over1+e^{\beta(r-1/4)}},\qquad
\log((1-C_\beta)C_\beta^{-1})=\beta(r-1/4).
\]

Bei `β=1` und `r=(3/2,1/2,-1/2)` ergibt sich

| | Eigenwerte |
|---|---|
| `h` | `1.25, 0.25, -0.75` |
| `C_β` | `0.2227001388, 0.4378234991, 0.6791786992` |
| `logit(C_β)` | `1.25, 0.25, -0.75` |

Das Logitresiduum beträgt `2.22e-16`. Thermalisation entfernt also die
Singularität, gibt aber exakt das schon festgelegte Modenspektrum `βh` zurück.
Sie erzeugt keine neue Flavor-Massenhierarchie. Die Auswahl von `β`, die
absolute Temperaturinterpretation und `μ_geo` bleiben eigene Voraussetzungen.

## Reproduktion

```text
cd /Users/stefanhamann/Documents/Codex/2026-09-21/l-s/work/yukawa_native_covariance_20260921
python3 checker.py
```

`python3 checker.py` und `python3 -OO checker.py` erzeugten bytegleiches
`results.json` mit SHA-256
`8fd461b25193f160572a87a963990c07b8e3f2f9e75d21bb910c131dc21b2823`.

Gebundene Quellenhashes:

- `v258_dirac_covariance_induction.py`:
  `16c60e831dceba773f3629466895f1009654827286e5b760ae01bd755fd5c0b1`
- `microscopic-charged-car-limit/README.md`:
  `39c613b80a1fe64200d269b782f6fb86c98f92c78058891a6144605e09c4532b`
- `microscopic-charged-car-limit/checker.py`:
  `2259bd7d6ab890c8cca562774b1b5cdc574e60fb72a04a8c8c8f6ed8292f113a`
- `microscopic-energy-linearization/checker.py`:
  `393ee8e6362ca96c4fbf0354f5f9250ed445a56ba32e22659573649346cd2ce9`

Keine Repositorydatei und kein Claimstatus wurde geändert.
