# Gemischte Quellenantwort: stärkster positiver TFPT-Anschluss und erste fehlende Prämisse

Datum: 21. September 2026  
Auftrag: vorhandene TFPT-Quellenmechanismen auf

\[
\Gamma_{Aij}(H_{\rm src})
=\left\{\left[[B_A,H_{\rm src}],\Psi_i^\dagger\right],
\Psi_j^\dagger\right\}
=gW_{Aij}I
\]

prüfen, ohne den nativen Zieloperator \(H_W\) in die Quelle einzusetzen.  
Methode: Leseaudit des frischen Theoriegraphen (255 Contracts), der maßgeblichen
Original-Contracts und des neuen Rekonstruktionssatzes. Kein neuer Checker und
keine Vollsuite wurden ausgeführt; das Repository wurde nicht verändert.

## Entscheidung

Der stärkste vorhandene **positive** Quellenanschluss ist die Kombination aus

1. dem affinen \(E_8\)-Vakuumkubik aus
   `compiler-vacuum-current-cubic-20260918`, und
2. der vorhandenen 3+2-Besetzungsmarkierung \(S\) aus
   `common-source-gauge-grade-transfer-20260920`.

Sie bestimmt belastbar einen geordneten kubischen Koeffizienten:

\[
C_{(A,i)(B,j)(C,k)}=d_{ABC}\epsilon_{ijk}.
\]

Die \(E_6\)-Wardmatrix hat Rang 44 auf 45 neutralen Monomen. Daher sind die
relativen Koeffizienten eindeutig; Level und Stromnormierung fixieren die
Gesamtnormierung. Unter \(27=16_1+10_{-2}+1_4\) liegen 40 der 45 Monome im
gewünschten \(16\cdot16\cdot10\)-Typ. Das ist echte Quellenprovenienz für die
Tensorform und mehr als eine Dimensions- oder Spektrumsübereinstimmung.

Die unmarkierte Übernahme ist statistisch falsch: \(d\) ist intern symmetrisch,
der Familienfaktor \(\epsilon\) antisymmetrisch. Die bereits vorhandene
3+2-Markierung repariert genau diesen Austauschtyp:

\[
\{S,d_H\}=0,
\qquad
Y_{\rm mark}(h)=(S d_H)\otimes A(h),
\qquad
Y_{\rm mark}^{T}=Y_{\rm mark}.
\]

Damit kann die positive Kette die **Form, Nullstruktur und relativen
Vorzeichen eines \(W\)-artigen Koeffizienten** liefern. Sie liefert nicht die
kanonischen Felder und nicht die physische Hamiltonantwort.

Das Urteil lautet deshalb:

\[
\boxed{
\text{affines Kubik + Markierung}
\Longrightarrow
\text{Koeffizientenkandidat }W,
\quad
\not\Longrightarrow
\Gamma(H_{\rm src})=gW I.
}
\]

Die vier Ausgangs-Contracts bleiben im Theoriegraphen `PARTIAL`; insbesondere
bleiben `QGEO.KERNEL.01`, der gemeinsame Operator-/Zustandsanschluss und die
physische Transduktion offen.

## Was die OPE tatsächlich liefert

Der positive affine Vertrag beweist die Modenalgebra

\[
[J_m^a,J_n^b]
=J_{m+n}^{[a,b]}+mk\,\kappa(a,b)\delta_{m+n,0}I
\]

und daraus die radiale Vakuumantwort

\[
\langle\Omega|J_1^aJ_0^bJ_{-1}^c|\Omega\rangle
=\kappa(a,[b,c]).
\]

Das ist ein geordneter Drei-Strom-Koeffizient im affinen Vakuum. Es ist kein
gleichzeitiger Heisenberg-Kommutator mit einer unabhängig ausgewählten
physischen Zeit. Der Originalvertrag sagt ausdrücklich, dass kein
Hamiltonoperator hinzugefügt wurde und dass die Gewicht-eins-Operatoren
bosonische Randströme sind, nicht schon die benötigten fermionischen Felder.

Ein singulärer OPE-Term könnte also den **numerischen Tensor im kubischen
Hamiltondichtekanal** festlegen, falls eine zusätzliche Rekonstruktion zeigt,
dass genau diese lokale Dichte die physische Zeit erzeugt. Der OPE-Term allein
beweist diese Aussage nicht. Radiale Modenordnung und gleichzeitige
Hamiltonentwicklung sind hier verschiedene Strukturen.

## Die erste nicht gelieferte Operatoridentität

Für die gewünschte Antwort genügt nicht, dass ein Tensor \(W\) irgendwo in
einem Dreipunktkoeffizienten vorkommt. Die Quelle muss auf einem gemeinsamen
invarianten Definitionskern die Paarprojektion

\[
\boxed{
\Pi_{\Psi\Psi}[B_A,H_{\rm src}]
=g\sum_{i<j}W_{Aij}\Psi_j\Psi_i
}
\tag{M}
\]

liefern. Zusätzlich müssen alle zu \(W\) orthogonalen skalaren Komponenten
und alle operatorwertigen Restterme in der doppelten Antwort verschwinden.
Dann folgt durch CAR unmittelbar

\[
\left\{\left[[B_A,H_{\rm src}],\Psi_i^\dagger\right],
\Psi_j^\dagger\right\}=gW_{Aij}I.
\]

Identität (M) ist die erste fehlende **dynamische** Prämisse. Sie ist kein
anderer Name für eine nichtverschwindende OPE-Konstante: Sie sagt, dass die
physische Quellenzeit den markierten kubischen Kanal tatsächlich als
Paarvernichter ausführt.

Logisch liegt davor noch eine Typisierungsbedingung: \(B_A\) und \(\Psi_i\)
müssen als gerade CCR- beziehungsweise ungerade CAR-Operatoren derselben
Quellenrepräsentation konstruiert sein, mit demselben Adjunkten,
Ladungswörterbuch, Zustand und derselben Zeit. Der derzeitige
`source-critical-local-fields`-Kandidat liefert zwar explizite lokale ungerade
Feldvektoren, aber im Zweig

\[
(16,\bar4)+(\bar{16},4),
\]

während der alte affine Kubikzweig anders orientiert ist. Der Contract warnt
ausdrücklich, dass \((16,\bar4)\) nicht durch Umbenennen mit dem alten
\((16,4)\)-Zweig identifiziert ist. Der gemeinsame physische Transport von
Operator, Hyperladung und Energie fehlt. Seine kritische Energie und sein
IR-Zustand sind ebenfalls zusätzliche Wahlen. Daher darf man die beiden
positiven Teilstücke noch nicht als eine gemeinsame Darstellung in (M)
multiplizieren.

Die präziseste Form der ersten Gesamtprämisse ist damit:

> Es existiert eine aus derselben Quelle gewonnene graduierte
> Operatorrepräsentation samt physischer Zeitderivation
> \(\delta_{\rm src}(X)=i[H_{\rm src},X]\), die den markierten affinen
> Kubikkoeffizienten in den Paaranteil von
> \(\delta_{\rm src}(B_A)\) überführt.

Ohne diese eine gemeinsame Abbildung sind sowohl die Feldnamen als auch die
Zeit in \(\Gamma\) nachträglich gewählt.

## Kleinster entscheidender Nulltest

Die vorhandenen linearen, gaußschen oder quadratischen Quellenzeiten können
die fehlende Identität nicht liefern. Wenn

\[
[B_A,H_0]
=\sum_C u_{AC}B_C+\sum_C v_{AC}B_C^\dagger
\]

und die Bosonoperatoren mit den Fermionerzeugern kommutieren, gilt exakt

\[
\Gamma_{Aij}(H_0)=0.
\]

Unter denselben kanonischen Kommutationsvoraussetzungen gilt dasselbe für den affinen Clockgenerator \(L_0-Q/4\), sofern seine
Wirkung auf dem gewählten Feldwörterbuch nur linear ist: Nach dem ersten
Kommutator bleibt eine lineare kanonische Bosonkombination übrig;
beide Fermionantworten liefern null. Für nichtkanonische affine Ströme
folgt diese Nullantwort nicht allein aus einer linearen Clockwirkung. Ein Basiswechsel kann Null nicht in \(gW\neq0\)
verwandeln.

Das ist der präzise Grund, warum das vorhandene OPE-Kubik und eine Clock zwar
miteinander verträglich sein können, aber die gemischte Antwort nicht
automatisch erzeugen. Ein nichtverschwindendes \(\Gamma\) ist gerade der
Fingerabdruck einer nichtgaußschen Boson↔Fermionpaar-Wechselwirkung.

## Unmittelbares Zustandstor nach einem erfolgreichen \(\Gamma\)-Nachweis

Der neue Rekonstruktionssatz trennt die Herkunft des Generators von der
Zustandsfrage. Er macht aber eine zusätzliche, kleine Zustandsprüfung sofort
möglich. Für die allgemein rekonstruierte Form mit freien Antworten
\(\epsilon_f,\epsilon_b\) besitzt jeder normierte helle \(W\)-Paarkanal wegen
\(WW^\dagger=8I\) zusammen mit seinem Einbosonzustand den Block

\[
H_{2,\mathrm{hell}}=
\begin{pmatrix}
2\epsilon_f & \sqrt8\,\overline g\\
\sqrt8\,g & \epsilon_b
\end{pmatrix}.
\]

Wenn der von allen \(\Psi_i\) und \(B_A\) annihilierte leere Fockvektor nach
Abzug der Konstanten ein globaler Grundzustand sein soll, muss dieser Block
positiv semidefinit sein. Notwendig ist daher

\[
\epsilon_f\ge0,\qquad \epsilon_b\ge0,
\qquad
\boxed{2\epsilon_f\epsilon_b\ge8|g|^2}.
\]

Im nativen Fall \(\epsilon_f=0\), \(\epsilon_b=\Delta>0\), \(g\ne0\) ist die
Determinante negativ. Der kleinere Eigenwert

\[
E_-=
\frac{\Delta-\sqrt{\Delta^2+32|g|^2}}2<0
\]

liegt unter der Energie null des leeren Vakuums. Ein positiver physischer
Quellengrundzustand kann dann nicht gleichzeitig von allen identifizierten
\(\Psi_i\) und \(B_A\) annihiliert werden. Ein erfolgreicher
\(\Gamma\)-Nachweis erzwingt also in diesem Zweig unmittelbar einen
Quellenzustand, der vom leeren kanonischen Fockvakuum verschieden ist.

Diese Folgerung ist im vorhandenen Korpus durch das schon berechnete
\(N=2\)-Spektrum vorbereitet, wird dort aber nicht als dieses allgemeine
\((\epsilon_f,\epsilon_b,g)\)-Zustandstor formuliert. Sie ist eine analytische
Konsequenz des neuen Rekonstruktionssatzes, kein neu ausgeführter
Verifikationstest.

Umgekehrt gilt im engen nativen Bereich
\(0<|g|/\Delta\le1/20\) der vorhandene eindeutige globale Grundzustandssatz
für \(\Omega\) im Sektor \(Q=64\). Falls eine Quelle unabhängig einen Vektor
als **globalen** Grundzustand liefert und die Operatorabbildung eine volle
irreduzible Äquivalenz der 64-CAR/60-CCR-Fockdarstellung samt rekonstruiertem
Hamiltonoperator ist, folgt die Zustandsabbildung bedingt aus der
Eindeutigkeit; sie muss dann nicht nochmals frei gewählt werden. Das ist ein
endliches Quellen-/Zustandstor. Es wählt keinen kosmologischen Anfangszustand
und schließt T8 nicht.

## Bereits bekannte Schranke, nicht neuer Negativbefund

Die direkte Reparatur durch Transport eines freien Modells auf dieselben
64 CAR- und 60 CCR-Moden ist bereits ausgeschlossen. Der Contract
`universalraum-source-equivalence-decision-20260915` beweist im Ladungssektor
\(N=2\)

\[
\det(\lambda I-H_2)
=\lambda^{1956}
(\lambda^2-\Delta\lambda-8g^2)^{60}.
\]

Für \(g\neq0\) besitzt das native Modell 1956 Nullmoden. Ein freier,
quadratischer, ladungserhaltender Ersatz mit demselben \(N=1\)-Nullspektrum
hätte schon 2016 Null-Zweifermionenzustände. Der vorhandene Contract schließt
daher auch eine allgemeine ladungserhaltende unitäre Isospektralität in
dieser **freien Ersatzklasse** aus, nicht nur lineare oder Bogoliubov-
Feldwechsel. Neue Hilfsfreiheitsgrade, neue Nebenbedingungen und echte
nichtgaußsche Quellen sind von diesem Satz nicht erfasst.

Diese Schranke bestätigt die Richtung der positiven Suche: Eine erfolgreiche
Quelle muss die Mehrpunktwechselwirkung selbst enthalten. Sie darf nicht als
frei transportierte Quelle mit nachträglich eingesetztem \(H_W\) auftreten.

## Einziger begründeter nächster Schritt

Für den nächsten Quellenkandidaten, der behauptet, den markierten Kubikzweig
und die ungeraden Felder in **einem** Wörterbuch zu tragen, ist genau eine
Rechnung entscheidend:

1. \(H_{\rm src}\), \(B_A\) und \(\Psi_i\) ausschließlich aus dessen eigener
   Quelle und deren gewähltem Zustand/Zeit fixieren; keine Koeffizienten aus
   \(H_W\) übernehmen.
2. Den vollständigen Operator
   \(\Gamma^{\rm src}_{Aij}\) auf einem gemeinsamen dichten Kern berechnen.
3. Auf \(W\) und sein Orthogonalkomplement projizieren.

Erfolgskriterium:

\[
\Gamma^{\rm src}_{Aij}=gW_{Aij}I
\]

für alle Komponenten, mit einem einzigen aus der Quelle bestimmten \(g\),
und exakt null in allen orthogonalen beziehungsweise operatorwertigen
Antwortkanälen.

Abbruchkriterium: \(\Gamma^{\rm src}=0\), eine operatorwertige Restantwort,
ein nur zustandsabhängiger Erwartungswert oder ein erforderlicher Import des
Zieloperators. Dann trägt dieser Kandidat den OPE-Koeffizienten nicht als
physische Zeitwechselwirkung.

Vor diesem Test ist keine weitere OPE-, Dimensions-, Spektrums- oder
Hodge-Übereinstimmung entscheidungsrelevant.

## Belegstellen

- `compiler-vacuum-current-cubic-20260918/PROOF.txt`, Z. 20–39: affine
  Modenalgebra; ausdrücklich kein hinzugefügter Hamiltonoperator.
- Ebenda, Z. 66–100: exakter Drei-Strom-Tensor, \(E_6\times A_2\)-Faktorisierung,
  40 \(16\cdot16\cdot10\)-Monome und Eindeutigkeit des Kubiks.
- Ebenda, Z. 115–131: offener Rohquelle→Stromnetz-Anschluss und Grenze
  „bosonischer Strom ≠ physisches Fermion“.
- `common-source-gauge-grade-transfer-20260920/flavor/PROOF.txt`, Z. 26–81:
  Austauschproblem, \(S\)-Reparatur und ausdrücklich fehlender
  current-to-CAR/boson-to-fermion-Intertwiner.
- Ebenda, Z. 127–137 und 287–298: physische Anwendung von \(S\) auf den
  geordneten Vertex ist nicht hergeleitet; Stromnullmoden liefern keine
  Yukawa-/Diracdynamik.
- `source-critical-local-fields-20260920/ERGEBNIS.md`, Z. 68–112 und
  186–220: explizite ungerade Felder, aber anderes Familienwörterbuch und
  fehlender gemeinsamer Operator-/Energie-/Clocktransport.
- `source-charged-extension-selection-20260921/PROOF.txt`, Z. 31–58 und
  66–106: statische Clifford-Vervollständigung reicht nicht für physische
  Fermionparität; selbst volle gerade Dynamik bestimmt die relative
  geladene Zeit nicht.
- `universalraum-source-equivalence-decision-20260915/RESULTS.md`, Z. 209–229:
  vorhandener \(N=2\)-Spektralausschluss der freien gleichen Modenzahl.

Die externe Standardliteratur wird hier nur für die bereits in den Contracts
verwendete Typisierung benötigt: Knizhnik–Zamolodchikov für affine
Stromalgebra/WZW (`https://strings.itp.ac.ru/Papers/knizhnik1984.pdf`) und
Dreiner–Haber–Martin für zweikomponentige Fermionbilineare
(`https://arxiv.org/abs/0812.1594`). Diese Quellen liefern keine
TFPT-Ursprungsherleitung und keine Identität (M).

## Ergänzung aus dem unabhängigen Rekonstruktionsaudit

Nach bereits bewiesenen unteren Operatoridentitäten genügt alternativ D_F=0 am vollbesetzten Fermionzustand zusammen mit g_F≠0. Definition, Beweis und Geltungsbereich stehen im Hauptbericht und Algebraaudit. Der vollbesetzte Vektor ist ein Prüfzustand; ein Quellenwert des Defekts oder der Kopplung ist noch nicht ausgewertet.
