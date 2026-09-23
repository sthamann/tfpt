# Herleitungen zur Universalraum-Inversion

Vier argumentative Kerne des Contracts. Die maschinellen Instanzen stehen in
`checker.py` / `validation.json`; hier stehen die allgemeinen Argumente.
NON-RH, keine T1–T8-Schließung.

## P1 — Kein geschlossenes endliches Quantensystem erzeugt exaktes exponentielles Abklingen für alle Schritte

**Satz.** Sei \(\mathcal H\) endlich-dimensional, \(U\) unitär, \(\rho\) ein
Zustand, \(A\) eine Observable und \(f(n)=\operatorname{Tr}[A\,U^n\rho U^{-n}]\).
Gilt \(|f(n)|\le C r^n\) für ein \(r<1\) und alle \(n\in\mathbb N\), so ist
\(f\equiv 0\).

**Beweis.** Mit der Spektralzerlegung \(U=\sum_k e^{i\theta_k}P_k\) ist

\[
f(n)=\sum_{k,l} e^{i(\theta_k-\theta_l)n}\operatorname{Tr}[A P_k\rho P_l]
=\sum_m c_m e^{i\varphi_m n},
\]

wobei die zweite Summe nach Zusammenfassen gleicher Frequenzen paarweise
verschiedene \(\varphi_m\) und höchstens \((\dim\mathcal H)^2\) Terme hat.
Für paarweise verschiedene Frequenzen gilt der Cesàro-Grenzwert
\(\frac1N\sum_{n<N} e^{i(\varphi_m-\varphi_{m'})n}\to\delta_{mm'}\), also

\[
\frac1N\sum_{n<N}|f(n)|^2 \;\longrightarrow\; \sum_m |c_m|^2 .
\]

Aus \(|f(n)|\le C r^n\) folgt
\(\frac1N\sum_{n<N}|f(n)|^2 \le \frac{C^2}{N(1-r^2)} \to 0\),
also \(\sum_m|c_m|^2=0\), also \(f\equiv0\). ∎

**Folgerung für TFPT.** Der reduzierte Prozess dämpft Kontraste exakt mit
\((3/7)^n\neq0\) (maschinell: `depol^n` auf dem Kontraststrahl, n=1..4). Nach
P1 kann **keine** geschlossene endliche unitäre Ausführung diesen Verlauf für
alle \(n\) erzeugen. Übrig bleiben: fortlaufende frische Register (offene
Ausführung), ein unbeschränkter Grenzprozess, oder eine Näherung über
endlich viele Schritte mit anschließender (teilweiser) Rekurrenz.

**Maschinelle Instanz.** Die kohärente Quellausführung mit wiederverwendetem
Register erfüllt \(U^2=I\); der Kontrast ist
\(c(n)=\tfrac12+\tfrac12(-1)^n\) — Periode 2, Cesàro-Mittel von \(|c|^2\)
gleich \(1/2>0\). Das ist zugleich der Fall „endliches Gedächtnis \(m=1\)":
ein Schritt Auslöschung, dann volle Rückkehr.

## P2 — Auf dem reinen Systemschatten existiert keine autonome Regel

**Formal.** Innerer Raum: Zustände auf \(\mathcal H_S\otimes\mathcal H_R\)
(System ⊗ Register). Schatten: \(P(X)=\operatorname{Tr}_R X\). Erlaubte
Fortsetzung: \(\Phi(X)=UXU^\dagger\) mit der Quell-Vormessung \(U\) eines
tatsächlichen Kontexts (die Rechenbasis ist ein Quellkontext).

**Zeugen.** \(X_1 = U|0,{+}\rangle\langle 0,{+}|U^\dagger\) (ein Schritt,
Register kohärent behalten) und
\(X_2 = |0\rangle\langle 0|\otimes\Delta(|+\rangle\langle+|)\)
(dephasierte Alternative, frisches Register). Maschinell:
\(P(X_1)=P(X_2)=I_4/4\), aber

\[
P(\Phi(X_1)) = |+\rangle\langle+| \;\neq\; I_4/4 = P(\Phi(X_2)),
\]

weil \(U^2=I\) den ersten Zweig rückgängig macht, den zweiten aber erneut
verschränkt. Gäbe es ein \(D\) mit \(P\circ\Phi = D\circ P\), folgte
\(D(I_4/4)=|+\rangle\langle+|\) und zugleich \(D(I_4/4)=I_4/4\). Widerspruch. ∎

**Präzisierung.** Für die Teil-Ausführung „jedes Schritt frisches Register"
existiert sehr wohl eine autonome Schattenregel: die Dephasierung
\(\Delta\). Der Satz sagt also nicht „keine Regel möglich", sondern: **der
Schatten allein bestimmt nicht, welche Ausführung vorliegt** — das
Registerprotokoll ist Prozessdatum, nicht Zustandsdatum. Ebenso: Der
Kontextschatten allein ist autonom (\(K\)), der volle CQ-Zustand ist autonom
(\(\sigma'_D=\sum_C K_{DC}\Delta_D(\sigma_C)\)), aber System- plus
Kontext**marginalie** ohne ihre Korrelation sind es nicht (Zeugenpaar in
`minimal_envelope`: gleiche Marginalien, verschiedene Korrelation,
verschiedene Zukunft). Die minimale autonome Hülle in diesem Modell ist
damit der volle CQ-Zustand.

## P3 — Auswahl des Kontextpunkts (1/7, 6/7, 0)

Auf dem Symmetriesimplex \(K_{abc}=aI+\frac b6(B-I)+\frac c8(J-B)\) gilt
\(T_{abc}=\frac14 C^\top K_{abc}C+\lambda P_f+\mu P_h\) mit
\(\lambda=a+\frac b3\), \(\mu=a-\frac b6\) (Orbitzerlegung unter voller
symplektischer Kontextsymmetrie; maschinell an allen drei Extremen geprüft).

**Behauptung.** Die Bedingungen (L) \(c=0\) (nur quell-inzidente Nachfolger)
und (H) \(\mu=0\) (keine für beide Auslesungen unsichtbare Richtung lebt in
\(T\) fort) zusammen wählen eindeutig \((a,b,c)=(1/7,6/7,0)\), also \(K=B/7\).

**Beweis.** Lineares System \(a+b+c=1,\ c=0,\ a=b/6\): eindeutige Lösung
\(a=1/7,\ b=6/7\). Maschinell: jede Bedingung allein lässt eine Familie
(\(c=0\) mit \(a=1/2\); \(\mu=0\) mit \(c=1/2\)). ∎

**Äquivalenz.** \(\mu=0 \iff \ker T_{abc}=\ker(C,F)\): Die drei
Sektorprojektoren \(P_c,P_f,P_h\) sind orthogonal; auf \(\mathrm{im}\,P_c\)
wirkt \(T_{abc}\) wie \(K_{abc}\), das am Quellpunkt invertierbar ist
(\(B^2=4I+3J\)); auf \(\mathrm{im}\,P_f\) wirkt \(\lambda\neq0\); auf
\(\mathrm{im}\,P_h\) wirkt \(\mu\). Also wird genau der unsichtbare Sektor
ausgelöscht gdw \(\mu=0\). ∎

**Entropie-Äquivalent.** Bei \(c=0\) ist die Entropie der sieben einzelnen
Übergänge \(H(a)=-a\ln a-(1-a)\ln\frac{1-a}{6}\); \(H'(a)=0\iff a=1/7\).

**Ehrlichkeit.** (L) hat Quellenstütze (der Träger von \(B\) ist Quelldatum,
v752). (H) ist ein Informationsprinzip über die reduzierte Regel. **Keines**
der beiden Prinzipien ist aus einer tieferen Dynamik abgeleitet; die
Auswahl ist damit präzisiert, nicht hergeleitet.

## P4 — Relationale Lesarten ohne relationale Dynamik (Vierträgerzelle)

Zelle: \(\mathcal H=(\mathbb C^4)^{\otimes4}\),
\(H=J\sum_{i<j}\frac{I+S_{ij}}2\), Grundzustand
\(|\Omega\rangle=\frac1{\sqrt{24}}\sum_\pi\mathrm{sgn}(\pi)|\pi(0..3)\rangle\)
(eindeutig, \(\Lambda^4\mathbb C^4\)).

**(i) Lesarten sind unterscheidbar.** Der bedingte Zustand
\(\psi_t=(\langle t|_0\otimes I^{\otimes3})|\Omega\rangle\) ist der
antisymmetrische Zustand der drei übrigen Träger auf der Wertemenge
\(\{0,1,2,3\}\setminus\{t\}\): Träger disjunkter Basiswerte, also
\(\langle\psi_t|\psi_{t'}\rangle=0\) für \(t\neq t'\), und
\(\|\psi_t\|^2=3!/24=1/4\). Vier Lesarten, paarweise orthogonal, rein,
gleichwahrscheinlich. (Maschinell: Gram \(=6\,\mathbb 1_4\), Reinheit,
Träger = Permutationen des Komplements.)

**(ii) Keine kollektive Zeit.** Für jedes \(A\) gilt
\(A^{\otimes4}\Omega=\det(A)\,\Omega\) (Determinantendarstellung auf
\(\Lambda^4\)); für unitäres \(A\) ist das eine globale Phase, der
Dichteoperator bleibt invariant. (Maschinell an \(A=\mathrm{diag}(1,i,-1,-i)\)
und einer Transposition.)

**(iii) Keine PW-Uhr aus dem gegebenen \(H\).** \(H\Omega=0\): unter der
einzigen gegebenen Dynamik ist \(\Omega\) stationär, die bedingten Zustände
konstant. Und \(P_{t'}S_{01}P_t\neq0\) für \(t'\neq t\): die Kopplung
verändert die Anzeige von Träger 0, d.h. Träger 0 ist keine
Page–Wootters-Uhr dieses Modells. Eine uhr-erhaltende Aufspaltung
\(H=H_c+H_s+V\) mit \([V,\text{Uhr}]=0\) wäre eine zusätzliche, hier nicht
ausgewählte Struktur. ∎

**Fazit.** „Global stationär" und „intern relational strukturiert" fallen
hier auseinander: Die Lesarten existieren, ihre Ordnung/Dynamik nicht.
