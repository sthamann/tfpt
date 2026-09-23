# Quellenfrage: skalare Konformalklasse und geladener Zustand

Datum: 21. September 2026. Contract: `UR.SOURCE.CONFORMAL_KERNEL_SELECTION.01`.
Gesamturteil: **PARTIAL**. Die skalare geometrische Reduktion und die unten
angegebenen Gegenprüfungen sind exakt. Eine ursprüngliche geladene P1-Quelle
und die vollständige TFPT-Theorie werden hier nicht hergeleitet.

## 1. Was tatsächlich auszuwählen ist

P1 postuliert eine orientierte Naht, einen reflexionspositiven Randkern,
Einheitswindung und die Normierung c3=1/(8π). Die Definition in
`tfpt_1_architecture_e8.tex:166–175` enthält keine vollständige geladene
Feldalgebra oder Formel für deren Zweipunktfunktion. P2 stellt das
Fünf-Slot-Interface bereit. Der endliche Drei-Zustands-Transfer, die
Compiler-Flavorarithmetik und das gemeinsame D4-Wörterbuch bleiben bestehen.
Ihre Identifikation mit einem rohen geladenen Feldzustand ist gerade die
zu beweisende Quellenkarte.

Der erste hier untersuchte Originalpfad v156/v176 benutzt einen
**potentialfreien skalaren Laplace-Operator in zwei Dimensionen**.
v156 berechnet die harmonische Fortsetzung exp(ikx−|k|y) und die
Normalableitung |k|. Er setzt danach die 16 Majoranas und die Erweiterung
zum E8-Netz an. Die skalare Rechnung allein führt diese Schritte nicht aus.

Es gibt insbesondere vier verschiedene Objekte:

- die skalare Dirichlet-Energie als Randform;
- deren DtN-Operator in einem festgelegten Rand-Hilbertraum;
- eine fermionische CAR-Kovarianz samt Realstruktur und Spinstruktur;
- ein Transfer beziehungsweise Zeitgenerator auf dieser Feldalgebra.

Keines dieser Objekte darf allein wegen der Bezeichnung „Kern“ durch ein
anderes ersetzt werden. Gewöhnliche Operatorpositivität ist außerdem nicht
dasselbe wie Osterwalder–Schrader-Reflexionspositivität.

## 2. Exakte Korrektur am additiven Krümmungsansatz

Sei Λ der skalare masselose DtN einer kompakten verbundenen Fläche mit Rand
mit der üblichen harmonischen Fortsetzung. Green liefert

\[
 \langle f,\Lambda f\rangle_{L^2(\partial M,ds)}
 =\int_M|du_f|_g^2\,dV_g\ge0,
 \qquad \Lambda1=0.
\]

Dies gilt vor Entfernung des konstanten Modus. Betrachte nun wörtlich
den Ansatz aus v201/v210/v288/v290 auf dem vollen periodischen Raum:

\[
 A_f=|D_\theta|+M_f.
\]

Aus A_f1=0 folgt sofort f=0. Auch die schwächere Voraussetzung A_f≥0
zusammen mit dem Nullmittelwert f_0=0 genügt: Die nichtnegative quadratische
Form hat auf 1 den Wert null, also A_f^(1/2)1=0 und A_f1=0. Äquivalent
hat jede Kompression auf span{1,e^(ikθ)} mit k≠0 die Matrix

\[
 \begin{pmatrix}0&f_{-k}\\f_k&|k|\end{pmatrix},
 \qquad \det=-|f_k|^2.
\]

Für den unveränderten Originalprüfer v290 mit f=0.3 cos(4θ), N=40, erhält
man genau [[0,0.15],[0.15,4]]. Die Determinante ist −9/400; der kleinste
Eigenwert des vollständigen 81-dimensionalen Operators beträgt numerisch
−0.011226376446229484. Gleichzeitig kommutiert er exakt mit der Viererclock.
Das widerlegt nicht die berechnete Kommutatoraussage; es widerlegt seine
Eignung als positiver **masseloser skalarer DtN**.

Das liefert keinen allgemeinen Beweis physischer Flachheit. In einer
Zerlegung Λ=|D|+M_f+S_cone+R muss der vollständige Rest auf 1 den Wert −f
haben. Eine Symbolentwicklung ist keine exakte Operatorgleichheit ohne
Rest. Auf einem projizierten, antiperiodischen oder massiven Raum fehlt
die obige Nullmodusanwendung möglicherweise vollständig. Insbesondere
garantiert Positivität einer gewählten CAR-Kovarianz nicht Λ≥0.

## 3. Die eigentliche Abkürzung: Randenergie statt flacher Innenmetrik

Für den im Original verwendeten zweidimensionalen skalaren Laplace-Fall
ist die vollständige Antwort zugänglicher als das additive Prüfmodell.
Setze g'=exp(2σ)g. Dann gelten exakt

\[
 \Delta_{g'}=e^{-2\sigma}\Delta_g,
 \qquad \nu_{g'}=e^{-\sigma_b}\nu_g,
 \qquad ds_{g'}=e^{\sigma_b}ds_g,
 \quad \sigma_b=\sigma|_{\partial M}.
\]

Die harmonische Fortsetzung desselben Randwertes bleibt daher dieselbe,
und auf Randfunktionen gilt

\[
 \boxed{\Lambda_{g'}=e^{-\sigma_b}\Lambda_g.}
\]

Insbesondere ist Λ_g'=Λ_g, wenn σ_b=0. Noch stärker: Die Randform

\[
 B_g(f,h)=\int_{\partial M}\bar f\Lambda_g h\,ds_g
         =\int_M\langle du_f,du_h\rangle_g\,dV_g
\]

erfüllt **B_g'=B_g auch bei nichtverschwindendem σ_b**. Die beiden
Randgewichte heben sich auf. Das ist eine Aussage über die vollständige
Form, nicht lediglich das führende Symbol oder einige Eigenwerte.

Diese Identitäten stehen auch im Originalartikel von Guillarmou–Guillopé,
*The determinant of the Dirichlet-to-Neumann map for surfaces with boundary*,
Einleitung und Abschnitt 2, insbesondere S.6:
https://arxiv.org/pdf/math/0701727 . Hier wird nur die skalare Identität
verwendet, kein Satz über geladene Felder oder Quasifreiheit.

Bei Kegelpunkten reicht für die vorliegende Schlussfolgerung eine glatte
Deformation mit Träger außerhalb der Kegel und des Randes; dadurch bleibt
auch die gewählte Operator-Domäne unverändert. Man kann solche Deformationen
über eine vorhandene endliche D4-/Reflexionswirkung mitteln. Sie erhalten
Marken, Winkel und Symmetrien, ändern die innere Gaußkrümmung und lassen den
vollständigen DtN unverändert. Eine bereits vorhandene Randantwort samt
Spektrum kann daher innere Weyl-Flachheit nicht selektieren. Über zusätzliche
Bulk-Gap- oder Gravitationsbedingungen wird damit nichts entschieden.

Ein besonders einfacher exakter Test der universellen Krümmungsdeutung
verwendet auf derselben skalaren Diskklasse σ=a(1−r²). Der Rand behält
seine Metrik, der DtN bleibt |D|, während

\[
 K_{g'}=4a\,e^{-2a(1-r^2)},\qquad
 \kappa_{\partial,g'}=1-2a.
\]

Sowohl innere als auch geodätische Randkrümmung ändern sich. Eine freie
additive Multiplikation mit dieser Krümmungsänderung ist folglich keine
korrekte allgemeine Darstellung des skalaren 2D-DtN. Dieses Beispiel
prüft die Operatorbehauptung; es wird nicht als P1-Geometrie ausgewählt.

**Gelöster Teil:** Wenn die markierte Konformalklasse bereits aus der
Originalquelle bestimmt ist, braucht die skalare Randenergie keine weitere
Auswahl eines flachen metrischen Repräsentanten. Die Suche nach einem
positiven Zusatzfunktional ∫f² ist für diesen Teil unnötig. Wird die
Konformalklasse erst angenommen, bleibt genau diese Annahme bestehen.

## 4. Randmetrik und Zeit verschwinden nicht automatisch

Der Übergang von einer Form zu einem selbstadjungierten Operator benötigt
ein Hilbertprodukt. Bei ds=w(θ)dθ lautet in einer ausgewählten Disk-
Uniformisierung der DtN

\[
 \Lambda_w=w^{-1}|D|\quad\hbox{auf }L^2(w\,d\theta),
 \qquad \widehat\Lambda_w=w^{-1/2}|D|w^{-1/2}
       \quad\hbox{auf }L^2(d\theta).
\]

Das sind positive Operatoren. Der konstante Nullmodus ist auf dem ersten
Raum 1, auf dem zweiten √w. Ein Beweis mit dem falschen konstanten Vektor
nach diesem unitären Transport wäre ungültig.

Die Randdichten w=1+ε cos(4θ), |ε|<1, sind positiv, D4-invariant und haben
alle Umfang 2π. Vier Marken, diskrete Symmetrie und Umfang allein wählen
daher w nicht. Das Eigenwertproblem lautet |D|f=λwf. Auf der ungestörten
entarteten Eigenfläche e^(±2iθ) ist die Gewichtsform

\[
 \begin{pmatrix}1&\epsilon/2\\\epsilon/2&1\end{pmatrix}.
\]

Die Ableitung des unitär transportierten Operators ist
−(M_cos4 |D|+|D| M_cos4)/2; ihre Kompression ist [[0,−1],[−1,0]].
Die beiden echten Eigenwertzweige aus λ=2 haben daher Ableitungen ±1.
Dies ist eine korrekte positive skalare Gegenkontrolle der Behauptung,
dass die genannten geometrischen Randdaten schon den ganzen DtN festlegen.
Sie widerlegt keine zusätzlichen P1-Bedingungen, die eine Randdichte oder
einen kontinuierlichen Zeitgenerator unabhängig festlegen könnten.

Eine kontinuierliche Rotationsisometrie würde w konstant machen. Die
vorhandene diskrete Viererclock darf nicht ohne Nachweis durch eine solche
kontinuierliche Isometrie ersetzt werden. Ebenso ist Λ nicht automatisch
der physische Hamiltonoperator der geladenen Theorie.

## 5. Der vorhandene Zustandsselektor hat den falschen Grenzwert

Die tatsächliche Funktion `v210_mark_local_dtn.covariance` setzt

\[
 \mu_N=\tfrac12(\lambda_{N-1}+\lambda_N),\qquad
 C_N=\tfrac12\bigl(I+\operatorname{sgn}(\Lambda_N-\mu_N)\bigr)
\]

für 2N+1 sortierte Eigenwerte. Bereits für Λ_N=diag(|n|), −N≤n≤N,
ist λ_j=ceil(j/2) und daher **μ_N=N/2 für jedes N**. Somit

\[
 C_Ne_n=\tfrac12(1+\operatorname{sgn}(|n|-N/2))e_n.
\]

Auf jedem vorher festgehaltenen Fourierblock verschwindet C_N ab
hinreichend großem N. Mit der festen Fourier-Einbettung und Fortsetzung
durch null gilt C_N→0 stark. Bei geradem N haben die beiden Schwellenmoden
Besetzung 1/2; C_N ist dann kein Projektor. Eine gültige komplexe
CAR-Kovarianz darf gemischt sein; die Feststellung widerlegt also nicht
ihre Positivität, sondern eine reine vakuumartige Polarisation.

Unabhängig vom Cutoff gilt F(|D|)e_n=F(|D|)e_−n. Ein skalares
Spektralfunktional von |D| kann keinen gerichteten Hardyprojektor wählen.
Der Übergang zum gerichteten Dirac-Operator, zur Spinstruktur und zur
CAR-Realstruktur ist zusätzliche Information. Auch die korrekte
Vererbung einer Clock-Symmetrie liefert diese Information nicht.

Der Originalprüfer v210 kennzeichnet sich als bedingte Symmetrieprüfung;
sein Konvergenzabschnitt prüft den Kommutator, nicht den Zustandsgrenzwert.
Die hier festgestellte Grenze ersetzt diesen gültigen endlichen Check
nicht, sondern verhindert seine Verwendung als Quellenrekonstruktion.

**Der Schluss gilt auch für das tatsächliche positive Markenprofil.**
Die v210-Toeplitzmatrix erfüllt für die G gesampelten Profilwerte f_l≥0

\[
 x^*M_Nx=\frac1G\sum_{l=0}^{G-1}f_l
             \left|\sum_a x_a e^{in_a\theta_l}\right|^2\ge0.
\]

Somit Λ_N≥diag(|n|) und μ_N≥N/2. Für jede Eigenzahl λ≥0 ist
((1+sgn(λ−μ_N))/2)²≤λ/μ_N, daher

\[
 \|C_Nv\|^2\le\frac{\langle v,\Lambda_Nv\rangle}{\mu_N}
             =O(N^{-1})
\]

für jedes feste Fourierpolynom v. Sein Erwartungswert rechts ist ab
hinreichend großem N konstant. Dichtheit und ||C_N||≤1 ergeben wiederum
starke Konvergenz gegen null. Die FFT-Positivität gilt auch bei Aliasing;
eine obere Normschranke für M_N wird für diesen Beweis nicht benötigt.
Der feste Block |n|≤2 hat im Original bei N=16,32,64 die Normen
||C_NΠ_K||₂≈6.03e−4, 7.77e−8 und 1.66e−15.

Die Aussage benutzt die feste Fourier-Einbettung. Eine neue Zentrierung
um wandernde Fermi-Punkte und eine andere Kontinuumsskalierung wären
zusätzliche Rekonstruktionsdaten; sie sind hier nicht ausgeschlossen,
werden aber von v210 nicht aus P1 ausgewählt. Der Nullgrenzwert ist
selbst eine zulässige komplexe CAR-Kovarianz in passender Konvention,
jedoch nicht die behauptete gerichtete chirale Polarisation.

## 6. Auch nach einem korrekt ausgewählten CAR-Vakuum bleibt die Erweiterungswahl

Die gemeinsame gerade Stromalgebra V_D8 besitzt unter anderem die
Felderweiterungen

\[
 F_{16}=V_{D8}\oplus V_v,\qquad
 V_{E8}=V_{D8}\oplus V_s.
\]

Die vier D8-Sektoren haben Gewichte (0,1/2,1,1), v×s=c und damit

\[
 M_{v,s}=\exp(2\pi i(h_c-h_v-h_s))=-1.
\]

Beide Erweiterungen haben c=8 und dieselben geraden D8-Stromdaten,
aber verschiedene geladene Felder und Lokalität/Gradierung. Die
Holomorphie-/GSO-Voraussetzung wählt die zweite Erweiterung nur bedingt.
Das ist im Original durch v973, insbesondere N1/N2/N4, bereits als
Anwendbarkeitsgrenze dokumentiert. Es ist kein Gegenbeispiel gegen alle
TFPT-Prinzipien, sondern gegen die ausreichende Auswahl durch c=8 und
den neutralen Stromsektor allein.

## 7. Entscheidung und verbleibende Quellenangabe

Die skalare Innenmetrik muss in diesem Pfad nicht zuerst durch ein neues
Energieprinzip bestimmt werden. Die gleichzeitige Auswahl einer geladenen
Quelle ist damit aber nicht erreicht. Die erste fehlende Angabe ist eine
aus P1/P2 konstruierte **graduierte Feldalgebra mit unabhängigem
Calderón-/Zweipunktdatum und Zeitwirkung auf genau diesem Raum**.

Im freien Kandidaten wäre die erste entscheidende Überprüfung die
Kovarianz auf einem festen Paar entgegengesetzter gerichteter Moden,
einschließlich begründeter Spinstruktur, CAR-Normierung und physischer
Zeitwirkung. Der bestehende Medianselektor liefert auf diesem Test im
Grenzwert null. Ihn stillschweigend durch den gewünschten Hardyprojektor
zu ersetzen würde den fehlenden Quellenbeweis nur voraussetzen.

Dieser Contract schließt deshalb kein physisches T1–T8-Gate und ändert
keinen Ledger. Er entfernt einen vermeidbaren metrischen Umweg, korrigiert
eine unzulässige DtN-Gegenkontrolle und isoliert einen nachweislich
ungeeigneten Zustandsselektor. Neue Rechnungen hinter einer erneut
eingesetzten Zielkovarianz wären keine Fortsetzung der Quellenherleitung.
