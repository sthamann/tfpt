# Lokale Skalierung: stärkere Stabilität, exakte Propagation und der kritische Engpass

14. September 2026. Eigene Fortsetzung für T3/T4/T5/T7. Keine TOE-Promotion.

## Ergebnis in einfachen Worten

Es gibt jetzt drei neue, konkret prüfbare Aussagen:

1. **Lokale Vermittler bleiben kontrollierbar, auch wenn sie zwischen Zellen wandern.**
   Die bisherige grobe Stabilitätskonstante 1920 wird für die C16-Zellbank auf
   **320** verbessert; für eigene Kantenmoden genügt **80**. Der räumlich entfernte
   Anteil der vermittelten statischen Kopplung besitzt eine explizite geometrische
   Restschranke pro Zelle.
2. **Das bloße positive Vertauschen ganzer Zellen erzeugt keine masselose Welt.**
   Für eine ganze wachsende Familie ist der volle Anregungsgap exakt der Gap einer
   einzigen Zelle – auch bei beliebig starker positiver Swapkopplung. Das ist ein
   Ausschluss eines besonders einfachen Klebeprinzips, kein Ausschluss von Lokalität.
3. **Kritische Dynamik muss nicht die hohen Vermittlermoden zerstören.** Ein explizit
   gewählter anderer Transfer wird bereits auf der kleinen inneren Zellskala kritisch.
   Seine eindimensionale einkomponentige Version ist vollständig lösbar: erst eine
   gapped Vakuumphase, dann ein quadratischer kritischer Rand, danach ein gefüllter
   Zustand mit linearen niederenergetischen Anregungen. Die volle erste Zellmultiplet
   hinterlässt zunächst eine große Farbdegeneration. Ein anschließend konstruierter
   positiver Farbaustausch entfernt deren extensive Entropie exakt, ohne den
   linearen Ladungssektor zu zerstören; er hinterlässt aber zusätzlich quadratische
   oder weichere Farbmoden.

Diese Ergebnisse wählen noch keinen nativen Compiler-Hamiltonoperator, keine drei
Raumrichtungen und keine chirale 3+1D-Materie. Sie sagen genauer, **welcher einfache
Übergang funktionieren kann und welcher sicher nicht**.

## 1. Quellenvertrag und unterschiedliche Zellbegriffe

Die Stabilitätssätze beziehen sich auf die C16-Architektur aus Abschnitt 5 des
gelieferten Dokuments `TFPT_Universalraum_Fortsetzung_2026-09-14NEU.md`:
40 Kanten, zehn Vermittlerlabels mit jeweils vier Kanten, sechs antisymmetrische
Farbkanäle. Dabei sind eine Bank pro C16-Zelle und eigene Moden pro Kante verschieden.

Für die anschließend vollständig gerechnete Propagationsfamilie wird dagegen
ausdrücklich der **vierörtige 544-dimensionale Stern** aus v1.4 benutzt. Für ihn
ist das kleine Spektrum analytisch bekannt. Sein Gap wird **nicht** als rigoroser
Gap der größeren C16-Zelle ausgegeben. Die allgemeinen Kopplungssätze gelten
für jede identische endliche Zelle mit einem tatsächlich bekannten eindeutigen
Grundzustand und Gap; der Stern ist eine ausführbare Referenz dafür.

Die Zwischenzelloperationen werden unten vollständig deklariert, aber nicht
als bereits aus dem TFPT-Compiler hergeleitet ausgegeben.

## 2. Neuer Stabilitätssatz mit um Faktor sechs besserer Zellbankkonstante

Sei `K_e,A` der harte Paarannihilator auf einer Kante e im antisymmetrischen
Farbkanal A. Bei der bestehenden Normierung gilt auf der harten Materie einschließlich
Löchern

\[
\sum_{A=1}^{6}K_{e,A}^{\dagger}K_{e,A}
=2P_{e,\mathrm{occ}}^-,\qquad 0\le P_{e,\mathrm{occ}}^-\le I.
\]

Das ist stärker, als sechs getrennte Normen `||K_e,A||²≤2` zu addieren.
Für eigene Moden pro Kante und m Zellen folgt sofort

\[
\sum_{c,e,A}K_{c,e,A}^{\dagger}K_{c,e,A}\le 80m I.
\]

Für eine Bank pro Zelle ist `K_c,r,A=Σ_{e:r(e)=r}K_c,e,A`. Jedes Label hat vier
Kanten. Die operatorwertige Cauchy-Identität

\[
4\sum_{i=1}^{4}K_i^\dagger K_i
-\Bigl(\sum_iK_i\Bigr)^\dagger\Bigl(\sum_iK_i\Bigr)
=\sum_{i<j}(K_i-K_j)^\dagger(K_i-K_j)\ge0
\]

benötigt keine Kommutativität der K_i. Somit

\[
\boxed{\sum_{c,r,A}K_{c,r,A}^{\dagger}K_{c,r,A}\le320m I.}
\]

Sei jetzt `h≥δ_b I>0` eine positiv definite, zahlenwertige Transportmatrix
auf allen Vermittlermoden. Für

\[
H=b^\dagger h b+t(b^\dagger K+K^\dagger b)
\]

liefert die exakte quadratische Ergänzung

\[
H=(b+t h^{-1}K)^\dagger h(b+t h^{-1}K)
-t^2K^\dagger h^{-1}K
\ge-{t^2\over\delta_b}\sum_\mu K_\mu^\dagger K_\mu.
\]

Daraus folgen die größenuniformen Schranken

\[
\boxed{H_{\mathrm{Zellbank}}\ge-320m\,t^2/\delta_b,\qquad
H_{\mathrm{Kanten}}\ge-80m\,t^2/\delta_b.}
\]

Bei unbewegten Vermittlern ist `δ_b=Δ`. Damit verbessert sich die im neuen
Dokument gegebene Zellbankschranke `−1920m t²/Δ` um Faktor sechs.
Die Schranken gelten auch nach Einschränkung auf einen erhaltenen harten
Gesamtladungssektor. Sie beweisen Stabilität, nicht den exakten Grundzustand.

## 3. Neue größenuniforme Reichweitenkontrolle des statischen Vermittlerterms

Sei `h=ΔI−ηA`, wobei A die symmetrische Adjazenzmatrix eines deklarierten
Vermittlertransportgraphs mit Maximalgrad D ist. Für `q=|η|D/Δ<1` gilt

\[
h^{-1}={1\over\Delta}\sum_{n=0}^{\infty}
\left({\eta A\over\Delta}\right)^n,\qquad
h\ge(\Delta-|\eta|D)I.
\]

Jeder Summand mit n ist durch Wege der Länge n getragen. Der Abbruch nach R
liefert einen strikt endlichen Reichweitenterm und die Operatornormschranke

\[
\left\|h^{-1}-{1\over\Delta}\sum_{n=0}^{R}
({\eta A/\Delta})^n\right\|
\le {q^{R+1}\over\Delta(1-q)}.
\]

Für einen Ausgangsmodus x ist zudem die absolute Zeilensumme außerhalb
des Abstands r durch `q^r/[Δ(1−q)]` beschränkt. Mit `C=320` bzw. `80` folgt
für den **statischen Term der exakten quadratischen Ergänzung**

\[
\boxed{\|W-W_R\|\le
C m {t^2\over\Delta}{q^{R+1}\over1-q},\qquad
W=-t^2K^\dagger h^{-1}K.}
\]

Pro Zelle bleibt der Fehler somit uniform; er verschwindet geometrisch mit R.
Im Prüfer wird die Schranke auf Ringen der Größen 8,16,32,64 kontrolliert.
Für regelmäßige Ringe sättigt der konstante Vektor sogar die Restnormschranke.
Bei `Δ=1,η=0.2,D=2` ist `q=0.4`.

**Grenze:** W ist nicht automatisch der vollständige dynamische Feshbach- oder
Schrieffer–Wolff-Hamiltonoperator. Die exakte quadratische Ergänzung beweist
Untergrenze und statische Quasilokalität; sie kontrolliert noch nicht die
Nichtkommutativität der verschobenen Moden, dynamische Retardierung oder alle
höheren Störungsordnungen. Hier bleibt ein zusätzlicher lokaler dynamischer
Restnachweis notwendig. Die einschlägige Linked-Cluster-SW-Theorie liefert dafür
ein allgemeines Verfahren, nicht seine bereits erfolgte modellspezifische Anwendung.
[Primärquelle](https://arxiv.org/abs/1105.0675)

## 4. Exakter Allgrößen-Satz: positive ganze Zell-Swaps schließen den Gap nicht

Eine einzelne Zelle habe Hamiltonoperator h mit eindeutigem Grundzustand `|0>`,
Grundenergie e0 und erstem Gap g>0. Setze `N_c=I−|0><0|_c`. Auf einem beliebigen
endlichen verbundenen Graphen ist

\[
H_{\rm swap}=\sum_c(h_c-e_0)
+\kappa\sum_{\{c,d\}}(I-S_{cd}),\qquad\kappa\ge0,
\]

wobei `S_cd` **die gesamte identische Zelle** vertauscht. Weil jeder Summand
`I−S_cd` positiv ist,

\[
H_{\rm swap}\ge g\sum_cN_c.
\]

Der Produktgrundzustand hat Energie null und ist eindeutig. Außerhalb davon
ist `ΣN_c≥1`, also ist der Gap mindestens g. Sei |a> ein Zellzustand mit Energie
e0+g. Dann hat der gleichförmige Einanregungszustand

\[
|W_a\rangle=m^{-1/2}\sum_c|a\rangle_c\bigotimes_{d\ne c}|0\rangle_d
\]

Energie exakt g und wird von jedem Swap festgehalten. Damit gilt für jede Größe
und beliebige nichtnegative Kopplungsstärke

\[
\boxed{\operatorname{gap}(H_{\rm swap})=g.}
\]

Im Einanregungsraum lautet der vollständige Operator `gI+κL_graph`; er propagiert,
bleibt aber massiv. Das ist ein konkreter Ausschluss des naheliegenden Vorschlags
„vorhandene gapped Zellen nur durch positive ganze Zellpermutationen verkleben“.
Es ist kein Ausschluss von negativ gewichteten Termen, teilweisen Zelloperationen,
anderen Grundzuständen, Grenzprozessen mit g→0 oder Wechselwirkungen, welche
den Produktzustand destabilisieren.

## 5. Eine explizite alternative Transferfamilie und ihre exakte Vakuumphase

Seien `|a>` die angeregten Zellzustände, Energien `ε_a≥g`, und
`E_c,a=|a><0|_c`. Deklariere

\[
T_{cd}=\sum_a(E_{c,a}E_{d,a}^\dagger+E_{c,a}^\dagger E_{d,a}),\qquad
H_{\rm tr}=\sum_c(h_c-e_0)-\kappa\sum_{\{c,d\}}T_{cd}.
\]

T vertauscht `|a,0>` und `|0,a>` und verschwindet bei zwei nichtleeren Zellen.
Die Zweizellenblockstruktur beweist exakt

\[
-(N_c+N_d)\le T_{cd}\le N_c+N_d.
\]

Bei Graphgrad≤D und κ≥0 folgt

\[
H_{\rm tr}\ge(g-\kappa D)\sum_cN_c.
\]

Auf einem verbundenen D-regulären Graphen besitzt die gleichförmige erste
Anregung Energie `g−κD`. Für `κD<g` ist daher

\[
\boxed{\operatorname{gap}(H_{\rm tr})=g-\kappa D.}
\]

Dieser Satz ist ein Vollraumargument, nicht bloß eine Einteilchennäherung.
Die gewählten E_c,a sind allerdings zusätzliche spektral definierte
Transferoperatoren. Dass der native Compiler sie bereitstellt, bleibt offen.

### 5.1 Der Stern als zertifizierter Referenzbaustein

Die ganzzahlige 256×256-Matrix `G=Σ_{j=1}^3(I−S_0j)` besitzt das Spektrum

| Eigenwert | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Multiplizität | 35 | 90 | 15 | 40 | 45 | 30 | 1 |

Der Prüfer bestätigt exakt das annihilierende Polynom `Π_{k=0}^6(G−kI)=0`
und die sieben ganzzahligen Momente p=0,…,6. Weil G symmetrisch ist, bestimmen
diese Identitäten die angegebenen Multiplizitäten. Es ist keine nur numerische
Rundung von Eigenwerten.

Die zugehörigen unteren mikroskopischen Zweiblockenergien sind
`E_−(λ)=(Δ−sqrt(Δ²+4t²λ))/2`. Deshalb ist der Grundzustand eindeutig und

\[
g={\sqrt{\Delta^2+24t^2}-\sqrt{\Delta^2+20t^2}\over2}.
\]

Bei `Δ=1,t=0.05` ist **g=0.0024339687513700303**. Die erste Anregung ist
30-fach. Das ist der Viersite-Stern, nicht der C16-Spektralbeweis.

## 6. Zwei verschiedene kritische Aussagen: quadratischer Rand, lineares Inneres

Für eine deklarierte eindimensionale Kette und einen ausgewählten angeregten
Zellzustand reduziert sich H_tr auf harte Bosonen/Spin-1/2 mit

\[
H=g\sum_xn_x-\kappa\sum_x(b_x^\dagger b_{x+1}+\mathrm{h.c.}).
\]

Die offene Kette ist durch Jordan–Wigner exakt auf freie Fermionen abbildbar.
Ihre Einteilchenwerte sind

\[
\epsilon_n=g-2\kappa\cos{n\pi\over L+1},\quad n=1,\ldots,L,
\]

und **das gesamte Vielteilchenspektrum** besteht aus den Teilsummen dieser Werte.
Der Prüfer vergleicht hierfür vollständige Matrizen bis Dimension 512 mit allen
Teilsummen, nicht nur einige niedrige Moden.

- **κ<g/2:** leeres eindeutiges Vakuum, uniformer thermodynamischer Gap g−2κ.
- **κ=g/2:** `ε(k)=g(1−cos k)~g k²/2`. Der Rand hat z=2. Dieser Ausdruck
  betrifft die Einteilchendispersion; er wird nicht als exakter erster positiver
  Vielteilchenwert bei jeder Randbedingung behauptet.
- **κ>g/2:** der Grundzustand füllt die negativen ε_n. Mit
  `k_F=arccos(g/(2κ))` entstehen zwei lineare Ferminahzweige
  `ε(±k_F+q)=±v_F q+O(q²)`, `v_F=sqrt(4κ²−g²)` in Gitter-/ℏ=1-Einheiten.

Bei **κ=g≈0.002434Δ** ist `k_F=π/3`, die Grenzdichte 1/3 und `v_F=√3 g`.
Für offene Ketten L=12,24,…,1536 bestätigt der Prüfer die festzahlige
Teilchen-Loch-Lücke `L gap_N/g→π√3`. Wir haben damit einen konkret berechneten
masselosen, linearen Grenzsektor bei einer Kopplung, die viel kleiner ist als Δ.

**Der entscheidende Schluss:** Man muss nicht die hohe Vermittlerlücke Δ schließen,
um niedrige kollektive Moden masselos zu machen. Man muss aber die massive
Produktvakuumphase verlassen oder einen anderen geeigneten Grenzprozess angeben.
Ein Verbot masseloser Moden in einer uniform gapped Produktphase ist kein Verbot
dieser inneren kritischen Route. Eine Lieb–Robinson-Geschwindigkeitsgrenze allein
wäre andererseits noch kein Lorentzkegel.
[Primärquelle zu lokalen Ausbreitungsgrenzen](https://arxiv.org/abs/quant-ph/0603121)

## 7. Der Preis der vollen 30-fachen Multiplet: neue explizite Entartungswarnung

Die Einkomponentenreduktion ist eine zusätzliche Auswahl. Behält man alle 30
ersten Sternzustände und nur den oben deklarierten Transfer, können besetzte
Farben auf einer offenen eindimensionalen Kette nicht aneinander vorbeigehen.
Die geordnete Farbfolge bleibt erhalten. Für jede Folge trägt der Positionsraum
denselben harten Vielteilchen-Hamiltonoperator.

Bei N besetzten Zellen gibt es deshalb **30^N isospektrale Farbfolgen**. Im
gefüllten Grundzustand führt dies zu mindestens dieser Grundzustandsentartung,
solange keine zusätzliche Farbaustauschwechselwirkung wirkt. Bei Dichte 1/3
ist die Restentropie pro Zelle `log(30)/3≈1.13373`.

Der Prüfer konstruiert sämtliche geordneten Farbsektoren für drei Farben,
zwei Teilchen und fünf Orte und vergleicht die vollständigen Positionsspektren.
Der allgemeine 30^N-Satz folgt aus der erhaltenen Reihenfolge, nicht aus einer
Extrapolation einiger numerischer Werte.

Dieser Mangel ist präziser als „es fehlt noch Materie“: Die nächste physikalische
Aufgabe ist ein **quellenseitiger lokaler Austausch, der diese Entartung kontrolliert
hebt**, ohne den gewünschten gaplosen Ladungssektor durch eine willkürliche
Farbauswahl zu ersetzen. Die Konstruktion gibt nicht drei Familien.

### 7.1 Diese Reparatur lässt sich bereits explizit lösen

Ergänze innerhalb derselben deklarierten Kette den positiven Term

\[
H_{\rm col}=J\sum_xN_xN_{x+1}(I-S_{x,x+1}),\qquad J>0.
\]

Hier wird nur bei **zwei besetzten Nachbarzellen** deren gesamter angeregter
Zustand vertauscht. Der Term wählt keine der q Farben aus und erhält jede
gemeinsame identische Wirkung der lokalen Farbsymmetrie.

Die Voraussetzungen des folgenden Satzes sind ausdrücklich: eine endliche
offene verbundene Kette, festes `1≤N≤L`, `κ>0` für den Nachbartransfer,
`J>0` für den Farbaustausch und q energetisch identische erste Farben.
Bei `N<L` ist der Positionsgraph irreduzibel; bei `N=L` besteht er aus genau
einer Position. Ein Ring, ein verzweigter Graph, κ=0 oder J=0 sind nicht durch
diesen Groundspace-Gleichheitssatz abgedeckt.

Bei fester Teilchenzahl N ist der Ladungsgrundzustand der offenen Kette in jedem
geordneten Farbsektor derselbe. Seine Positionsamplituden können wegen der
negativen Hoppingmatrixelemente und des verbundenen Positionsgraphs strikt
positiv gewählt werden. Da H_col≥0 ist, kann die Grundenergie nicht sinken.
Ein vollständig symmetrischer Farbzustand wird von H_col vernichtet und erreicht
die alte Energie: Die Grundenergie bleibt **exakt unverändert**.

Umgekehrt muss ein Grundzustand jeden positiven Austauschterm vernichten. Jede
Nachbartransposition in der geordneten Farbfolge wird bei manchen Positionen
tatsächlich benachbart; diese Positionen haben strikt positives Grundzustandsgewicht.
Deshalb muss der Farbzustand unter sämtlichen Nachbartranspositionen invariant sein.
Der Grundraum ist genau

\[
\boxed{\mathrm{Sym}^{N}(\mathbb C^q),\qquad
\dim\mathcal G_N={N+q-1\choose q-1}.}
\]

Für q=30 wird aus 30^N nun `binomial(N+29,29)`: nur noch polynomielles Wachstum,
also **verschwindende Restentropiedichte**. Dies ist kein eindeutiges Vakuum,
aber eine vollständige Lösung des zuvor identifizierten extensiven
Entartungsproblems im ausdrücklich genannten Vertrag.

Jeder Zustand mit vollständig symmetrischer Farbe wird von H_col vernichtet,
nicht nur der Ladungsgrundzustand. Deshalb ist das vollständige freie
Ladungsspektrum als invarianter Sektor erhalten, einschließlich der linearen
Ferminahzweige. Der Prüfer bestätigt die Grundenergie und Multiplizität in
Vollmatrizen bis Dimension 540 für verschiedene positive J.

### 7.2 Der neue Preis ist eine beweisbar weiche Farbmode

Diese einfache ferromagnetische Reparatur liefert noch keinen gemeinsamen
relativistischen Spektralzweig. Für N≥2 und q≥2 wähle im Ladungsgrundzustand
eine einzelne Farbabweichung an der j-ten Position der **geordneten Teilchenfolge**.
Ihre Amplituden f_j seien orthogonal zum konstanten Vektor. Der Ladungsteil
bleibt exakt in seinem Grundraum, und die Farbenergie des normierten Testzustands ist

\[
J\sum_{j=1}^{N-1}p_j|f_{j+1}-f_j|^2,
\]

wobei `0≤p_j≤1` die Wahrscheinlichkeit ist, dass die geordneten Teilchen j,j+1
auch physisch Nachbarorte besetzen. Mit dem ersten nichtkonstanten Eigenvektor
des Pfadlaplaceoperators folgt die Variationsschranke

\[
\boxed{\operatorname{gap}_{N}\le2J\left(1-\cos{\pi\over N}\right)
\sim {J\pi^2\over N^2}.}
\]

Der Testzustand ist zum symmetrischen Farbgrundraum orthogonal. Die Entropiereparatur
hinterlässt somit mindestens einen **quadratisch oder noch weicher** schließenden
Anregungssektor. Sie selektiert keine drei Familien und keinen einheitlichen
Lorentzkegel. Diese Folgehürde ist nicht bloß vermutet, sondern durch die
angegebene allgemeine Variationsschranke konkretisiert.

### 7.3 Die zwei Klebeprinzipien unterscheiden sich durch erkennbare Terme

Die exakte Zweizellenidentität

\[
I-S_{cd}=N_c+N_d-2N_cN_d-T_{cd}+N_cN_d(I-S_{cd})
\]

trennt chemische Verschiebung, Dichtewechselwirkung, Transfer und besetzten
Farbaustausch. Sie wird zusätzlich ganzzahlig geprüft. Dadurch ist die Frage
an den Compiler konkreter geworden: Nicht nur „gibt es einen Swap?“, sondern
**welche dieser gebundenen Koeffizienten werden gemeinsam erzeugt?**
Beliebiges Weglassen der positiven Verschiebung und Dichtewirkung ist eine
Modelländerung, kein unschuldiger Wechsel der Darstellung.

## 8. Was dies für T3, T4, T5 und T7 wirklich leistet

| Front | Neuer belastbarer Beitrag | Nicht geschlossen |
|---|---|---|
| T3, Raumzeit/Propagation | Zwei ganze wachsende Hamiltonfamilien; ihre Propagation, exakten gapped Bereiche und ein berechneter linearer Grenzsektor | Kette und Transfer sind gewählt; keine Auswahl von 3 Raumdimensionen, kein gemeinsamer 3+1D-Lorentzkegel |
| T4, chirale Materie | Zwei lineare Ferminahzweige; die 30^N-Entartung wird durch einen expliziten symmetrischen Austausch auf polynomielle Grundraumdimension reduziert | Zusätzliche weiche Farbmode; kein chirales 3+1D-Maß, keine Spiegelentkopplung, keine abgeleiteten drei Familien |
| T5, Skalierung/Dynamik | Stärkere lineare Untergrenzen, uniformer statischer Reichweitenrest, exakte Allgrößen-Gaps und vollständige Vielteilchen-Kettenlösung | Keine dynamische lokale Feshbach-Restkontrolle der tatsächlichen gekoppelten C16-Quelle, keine Streukonstruktion |
| T7, Gravitation | In der positiven Swapfamilie bleibt jeder Vakuumanregungszustand mindestens g hoch; deshalb fehlt dort jeder masselose Vakuumpol, auch Spin 2 | Der lineare Kettensektor erzeugt weder Spin 2 noch universelle gravitative Kopplung; ein Tensorlabel würde daran nichts ändern |

Für eine uniforme Lücke und lokale beschränkte Wechselwirkungen ist die Beziehung
zu kurzreichweitigen verbundenen Grundzustandskorrelationen außerdem durch die
allgemeine Exponential-Clustering-Theorie gestützt. Unsere konkrete positive
Swapfamilie hat sogar exakt den unkorrelierten Produktgrundzustand.
[Primärquelle](https://arxiv.org/abs/math-ph/0507008)

## 9. Die nun präzisesten Folgeaufgaben

1. **Welche Zwischenzelloperation entsteht tatsächlich?** Positive ganze Swaps und
   spektral selektiver Transfer führen trotz identischer Einzelzelle zu verschiedenen
   Phasen. Der Compiler muss die Operation und ihr Vorzeichen entscheiden.
2. **Kritischer niedriger Sektor bei massiven Vermittlern:** Für die tatsächlich
   abgeleitete Wechselwirkung eine uniforme lokale Reduktion auf der Skala Δ
   beweisen und im daraus entstehenden niedrigen Modell den Phasenübergang auf
   der kleineren Skala g untersuchen. Beide Skalen dürfen nicht verwechselt werden.
3. **Die gelöste Entropiereparatur nativ überprüfen:** Der explizite positive
   Farbaustausch entfernt die extensive 30^N-Entartung, hinterlässt aber die
   1/N²-Schranke einer weichen Farbmode. Seine Herkunft und eine tatsächlich
   gemeinsame relativistische Sektorstruktur müssen nun zusammen geprüft werden.
   Keine willkürliche Einkomponentenauswahl als Familienerklärung deklarieren.
4. **Erst dann Geometrie, Chiralität und Spin 2 gemeinsam prüfen:** Derselbe skalierende
   Träger muss die drei Anforderungen erfüllen. Ein ausgewählter eindimensionaler
   Referenzsektor ist eine kontrollierte Zwischenstufe, keine vollständige Physik.

## 10. Reproduktion und Evidenzklasse

Ausführung: `python3 replay.py` in diesem Verzeichnis. Benötigt NumPy und SciPy.

- **400 Prüfbedingungen**, normale und `-OO`-Ausführung byteidentisch.
- **Sechs gezielt falsche Varianten abgefangen:** symmetrisches statt antisymmetrisches
  Paar, falsche Stabilitätskonstante 160, falsches Vorzeichen der quadratischen
  Ergänzung, fehlender positiver Swap-Diagonalterm, Entfernen negativer
  Einteilchenwerte aus der Vielteilchenlösung, negatives Vorzeichen des angeblich
  positiven Farbaustauschs.
- Ganzzahlige Identitäten, numerische Vollspektrumsvergleiche und allgemeine
  analytische Beweise sind getrennt angegeben. Die Prüfzahl ist keine Zahl
  unabhängiger Entdeckungen.
- Kein fremder Prüfer importiert; keine langen fremden C16-/RH-Kampagnen gestartet.
- `scaling.json`, `scaling_optimized.json`, `replay.json` enthalten Werte und
  Checker-Prüfsumme. T1–T8 bleiben insgesamt offen.
