# A3-Gewichte, D5-Glue und die kleinste projektive Translationsbrücke

Stand: 2026-09-14. NON-RH; keine Marker-/Paperänderung. Originalquellen wurden nur gelesen. Der kleine eigene Prüfer extrahiert ausschließlich die vollständig gelesene Funktion `build_roots` aus v128; keine fremden Forschungsprogramme wurden gestartet. 48 exakte Prüfgruppen bestanden, normale und `-OO`-Ausgabe sind bytegleich. Darunter sind 729 vorzeichenbehaftete Produktprüfungen je Cocyclegauge und 512 Assoziativitätsprüfungen. Kein numerisches Spektrum und keine physische Raumableitung.

## Ergebnis in einem Absatz

Die vier Gewichte der definierenden A3-Darstellung liefern tatsächlich ein Tetraeder und erzeugen das BCC-Gewichtsgitter. Im ursprünglichen E8-Glue sind sie aber keine ladungsfreien Ortsverschiebungen: Ein solcher Grundschritt muss gleichzeitig die D5-Spinorladung ändern. Es gibt eine explizite Auswahl von vier echten Grade-1-E8-Wurzeln, deren Tetraederschleife auch in der vollständigen Ladung schließt. Auf ihrem Rang-3-Untergitter zieht der übliche E8-Gittercocycle eine nichttriviale alternierende Form vom Rang 2 zurück. Daraus folgt eine minimale zweidimensionale irreduzible projektive Faser — kein unabhängig dazu erfundener Coin. Nicht ausgewählt sind dadurch die Liftsektion, der zentrale Charakter, eine unendliche räumliche Adressdarstellung oder eine Weyl-Dynamik. Zudem ist die geerbte E8-Metrik dieses Untergitters FCC/A3, nicht die BCC-Metrik seiner A3-Projektion.

## 1. Was in den Originalquellen wirklich steht

- [v128, Wurzelbauer](/Users/stefanhamann/Projekte/tfpt-theoryv4/verification/v128_graded_hull.py:46): Zeilen 60–63 bauen die beiden D5-Spinorchiralitäten, 73–80 die A3-Gewichte, 88–96 die Grade 1, 2, 3. Es handelt sich um interne Gewichte in `D5 (+) A3`, nicht um definierte Ortsoperatoren. Die Grade-Additivität wird in Zeilen 117–136 ausdrücklich nur für Summen geprüft, die wieder Wurzeln sind.
- [v983, ursprünglicher Gluegenerator](/Users/stefanhamann/Projekte/tfpt-theoryv4/verification/v983_simple_current_generator.py:11): Zeilen 11–33 geben den Spinor/Fundamental-Lift, seine Norm, den diagonalen Z4-Glue und die vier Wurzelsektoren. Zeilen 45–52 halten die analytische Implementer-/Skalierungsgrenze offen und sagen ausdrücklich „1+1D in and out“.
- [v143, gradierter Lie-Anschluss](/Users/stefanhamann/Projekte/tfpt-theoryv4/verification/v143_graded_frobenius.py:14): Zeilen 14–37 behandeln Cosetdualität, Liebracket und interne Weylorbits. Das ist nicht die Definition einer assoziativen unitären Ortsverschiebung.
- [v117, A3-Weylgruppe](/Users/stefanhamann/Projekte/tfpt-theoryv4/verification/v117_monodromy_weyl_a3.py:12): Zeilen 12–35 definieren eine konkrete endliche 24-elementige Holonomiegruppe. Der dortige A3-Weylbezug ist keine affine Translationsgruppe.
- [v783, Compiler](/Users/stefanhamann/Projekte/tfpt-theoryv4/verification/v783_two_qubit_clifford.py:15): Zeilen 15–24 erklären die 60 Reflexionen, die endliche Gruppe G31 der Ordnung 46080 und ihre Cliffordwirkung. Die konkrete Ordnungsprüfung steht bei Zeilen 654–685. Ein längeres Wort in derselben Darstellung erzeugt keinen zusätzlichen unendlichen Adressträger.
- [v774, Markierung](/Users/stefanhamann/Projekte/tfpt-theoryv4/verification/v774_arf_spinor_compiler.py:714): Zeilen 714–736 wählen q* durch σ-Invarianz, q(A)=1 und q(Fσ)=0. Zeilen 124–138 unterscheiden Familienbits, Trägerplätze und die nicht daraus folgende physische Materielesart. Das liefert eine endliche Markierung, keinen räumlichen Shift.
- [v782, tatsächliche endliche Adressvorstufe](/Users/stefanhamann/Projekte/tfpt-theoryv4/verification/v782_e8_transition_bus.py:19): Zeilen 19–57 haben echte (1+i)-adische Quotienten und einen F2³-Paartorsor. Die Deckaktion auf ganzen Wurzeln hat jedoch Ordnung 4, während diese Torsortranslationen Ordnung höchstens 2 haben. Dieser ursprüngliche Ausschluss verbietet gerade eine naive Gleichsetzung beider Aktionen.
- [v746, vorhandene skalierende Struktur](/Users/stefanhamann/Projekte/tfpt-theoryv4/verification/v746_phys_gnet_local_functor.py:13): Zeilen 13–20 setzen einen Quotientenkreis mit N/2 Stellen ein; Zeilen 35–45 prüfen Clockkovarianz und die N=48/96/192-Leiter. Die Quelle ist daher **nicht insgesamt endlich**. Sie enthält eine wachsende eindimensionale Netzstruktur, aber diese ist kein aus A3-Gewichten abgeleitetes BCC-Raumgitter.

Die andere tatsächliche Session liefert zusätzlich einen phasentreuen endlichen `g1 × g1 -> g2`-Tensor: [Bericht, Abschnitt 3](/Users/stefanhamann/Documents/Codex/2026-09-14/scha-3/outputs/TFPT_Der_einfache_Kern_2026-09-14.md:153). Dieser Audit übernimmt nicht ungeprüft eine räumliche Deutung daraus. Der Parent rekonstruiert dessen Tensor separat und prüft Gewichtserhaltung, Gramidentitäten und additive Ladungen; der vollständige Wurzelbasis-Cocycleadapter der anderen Session wird nicht nochmals als Ganzes gerechnet.

Eine präzise endliche Filtrationsgrenze ist unabhängig davon elementar: Ist F_n der lineare Raum der bis Länge n ausgewerteten Wörter in der festen komplexen Compileralgebra M4, dann dim F_n ≤16 und die aufsteigende Filtration stabilisiert. Nicht ausgewertete Wortgeschichten können unbeschränkt wachsen, sind dann jedoch zusätzliche gespeicherte Geschichte. Dies ist **kein** Ausschluss der unendlichen E8-Gitter-/VOA-Sektoren oder wachsender Netze.

## 2. BCC-Projektion und der erzwungene Ladungswechsel

Schreibe μ_a=e_a−(1,1,1,1)/4. Das sind die **vier Gewichte der definierenden Darstellung**, nicht vier verschiedene fundamentale höchste Gewichte. Ihr Gram ist

\[
G_\mu=I_4-\tfrac14\mathbf1\mathbf1^T.
\]

Eine explizite Isometrie des A3-Hyperraums nach R³ bildet sie auf

\[
\tfrac12(1,1,1),\quad\tfrac12(1,-1,-1),\quad
\tfrac12(-1,1,-1),\quad\tfrac12(-1,-1,1)
\]

ab. Ihr ganzzahliger Spann ist BCC mit Kovolumen 1/2; ihre Differenzen erzeugen das FCC-Wurzelgitter mit Kovolumen 2. Der Index ist 4.

Die tatsächliche diagonale Glueform ist mit ω_s=(1/2)^5

\[
L=\bigcup_{k=0}^3(D_5+k\omega_s)\oplus(Q(A_3)+k\mu_1).
\]

Damit gilt exakt: `(0,μ_a)` liegt nicht in L; `(s_a,μ_a)` mit passender D5-Spinorladung ist eine ursprüngliche Grade-1-Wurzel. Wenn eine Verschiebung ihre **exakte** D5-Komponente nicht ändern darf, bleibt für ihren A3-Anteil nur Q(A3), also FCC. Die bloße Neutralität der Z4-Klasse ist schwächer als die Neutralität der D5-Ladung.

## 3. Positiver geschlossener Lift und präziser Dreifachkonflikt

Wähle die vier tatsächlichen Spinorgewichte durch

\[
2s_1=(1,1,1,1,1),\quad2s_2=(-1,-1,1,1,1),
\]
\[
2s_3=(1,-1,-1,-1,-1),\quad2s_4=(-1,1,-1,-1,-1).
\]

Alle haben gerade Minusparität. Für λ_a=(s_a,μ_a) bestätigt der unveränderte Originalbauer: λ_a ist eine Grade-1-Wurzel und Σ_a λ_a=0. Weil Σ_a μ_a=0 die einzige ganzzahlige Relation der vier μ_a ist, definiert μ_a↦λ_a eine additive Gittersektion P(A3)→L. Sie ist nicht als kanonische Auswahl aus der Quelle bewiesen.

**Kleiner exakter Dreifachkonflikt für feste additive Lifts:** Grundschritte der Form `(s_a,μ_a)`, exakte D5-Neutralität **aller** FCC-Differenzen und verschwindende volle Tetraederschleife können nicht gleichzeitig vorliegen. Die zweite Forderung ergibt s_a=s für alle a; die dritte ergibt 4s=0, also s=0; die erste verbietet aber den reinen Lift `(0,μ_a)` im diagonalen E8-Glue.

Das ist kein universelles Bewegungs-No-go: zustandsabhängige Vertices, zusätzliche Ladungsträger oder andere Darstellungen sind nicht ausgeschlossen. Es benennt genau, was ein fester schrittweiser Lift nicht gleichzeitig leisten kann.

Zwei konkrete Kontrollen machen die Alternative sichtbar:

- Konstantes Dressing s_a=ω_s erlaubt alle exakt neutralen FCC-Differenzen. Die räumlich geschlossene Viererschleife hinterlässt aber `(2,2,2,2,2;0,0,0,0)`, eine nichtverschwindende D5-Wurzelgitterladung. Für a≠b hat λ_a+λ_b sogar Normquadrat 6 und ist keine Wurzel; der entsprechende native Grade-1-Liebracket ist null.
- Der obige geschlossene Lift löst die volle Schleifenbedingung, ändert aber bei jeder nichtverschwindenden Verschiebung die D5-Komponente. Sein D5-Projektionsrang ist 3.

Der volle Gram dieses positiven Lifts ist

\[
G_\lambda=\begin{pmatrix}
2&0&-1&-1\\0&2&-1&-1\\-1&-1&2&0\\-1&-1&0&2
\end{pmatrix}.
\]

Das ist ein affiner A3-Zyklus; Rang 3, Determinante einer Dreierbasis 4. Der Spann trägt folglich die FCC/A3-Wurzelmetrik. Die Projektion λ↦μ ist **nicht isometrisch**. „Rang drei“ und „BCC-Projektion“ dürfen daher nicht als bereits identische physische Metrik eingesetzt werden.

## 4. Cocycle: die zweidimensionale Faser entsteht algebraisch

Für den Standard-Even-Lattice-Cocycle lautet der phasenstabile Vertrag

\[
T_\lambda T_\nu=\epsilon(\lambda,\nu)T_{\lambda+\nu},\qquad
\frac{\epsilon(\lambda,\nu)}{\epsilon(\nu,\lambda)}=(-1)^{\lambda\cdot\nu}.
\]

Die vollständige ursprüngliche Wurzelbasis-Eichung wird hier nicht neu identifiziert. Der folgende Schluss braucht nur diesen üblichen alternierenden Cocyclevertrag. Auf der Basis λ1,λ2,λ3 ist

\[
B=G_\lambda\bmod2=\begin{pmatrix}0&0&1\\0&0&1\\1&1&0\end{pmatrix},
\quad\ker_{\mathbb F_2} B=\{000,110\}.
\]

Also Rang 2. Der zentrale Unterverband besteht aus n mit n1+n2 gerade und n3 gerade; er hat Index 4. Nach Wahl eines zentralen Charakters ist die verbleibende komplexe Algebra M2: Ihre vier Basisreste werden durch I,X,Z,XZ vertreten. Wegen XZ=−ZX gibt es keine eindimensionale Darstellung, und die expliziten Pauli-Matrizen zeigen Existenz einer irreduziblen zweidimensionalen Darstellung. Somit ist die Zweierfaser minimal und kann als **projektive Faser selbst** gelesen werden, nicht als zusätzlich gesetzter Coin neben ihr.

Ein expliziter, ausdrücklich gewählter Cocyclegauge auf Z³ ist

\[
\epsilon(n,m)=(-1)^{n_3(m_1+m_2)},\qquad
\rho(n)=X^{n_1+n_2}Z^{n_3}.
\]

Er erfüllt die Produktrelation und Assoziativität exakt. λ4 hat Koordinaten (−1,−1,−1), daher

\[
\rho(\lambda_1),\ldots,\rho(\lambda_4)=(X,X,Z,Z),
\quad XXZZ=I,\quad XZXZ=-I.
\]

Die verschwindende **additive** Schleife garantiert also nicht eine für jede Reihenfolge identische Operatorphase. Der relative Minuskommutator lässt sich nicht durch skalare Rephasierung entfernen. Zur Kontrolle ist auch der cochain-äquivalente diagonal-normalisierte Gauge geprüft: Addiere Σn_i m_i zum Exponenten und setze ρ_diag(n)=(-1)^{Σ binom(n_i,2)}ρ(n). Dann ist ρ_diag(λ4)=−Z, die erste Viererphase −I, die vertauschte +I. Die absolute Viererphase hängt an der gewählten Wurzelvektor-Eichung; das Verhältnis bleibt −1.

Diese Darstellung allein enthält keine unendlich vielen unterscheidbaren Ortszustände. Für solche Adressen wäre etwa die reguläre projektive Wirkung `T_n|m⟩=ε(n,m)|n+m⟩` auf ℓ²(Z³) hinzuzunehmen bzw. aus einem vorhandenen Quellenfeld herzuleiten. Die Gitterarithmetik existiert bereits, ihre Deutung als räumliche Adresse ist damit noch nicht gegeben. Der zentrale Charakter und die Liftsektion sind ebenfalls nicht ausgewählt. Weder eine isotrope BCC-Metrik noch Weyldispersion oder eine Uhr folgt allein aus der Zweierfaser.

## 5. Der kleinste operative Anschluss ist noch nicht der Liebracket

Die konkrete Reihenfolge λ1,λ3,λ2,λ4 besitzt in den ersten drei Summen echte ursprüngliche Wurzeln der Grade 1,2,3. Die letzte Summe ist null, das letzte Paar also (−λ4,λ4). Im nativen Liebracket folgt daraus ein Cartanelement, kein Identitätsoperator einer geschlossenen Translation. Dies ist der entscheidende Typunterschied:

\[
[E_\alpha,E_{-\alpha}]\propto H_\alpha
\quad\ne\quad T_\alpha T_{-\alpha}\propto I.
\]

Ein phasentreuer W-Vertex schließt deshalb eine echte endliche **Ladungsfusionsbrücke**, aber nicht automatisch die assoziative Verschiebungswirkung auf beliebigen Adressen. Die jetzt positiv ausgewiesene Kette ist enger und überprüfbar: ursprünglicher Z4-Glue → gewählte geschlossene Rang-3-Liftsektion → geerbter Rang-2-Cocycle → minimale projektive C²-Faser. Die Auswahl der Sektion und der Operatordarstellung, Raum-/Metrikdeutung, Zustand, Ablauf und beobachtbare Dynamik bleiben klar benannte zusätzliche Aufgaben.

## Reproduzierbarkeit und Negativkontrollen

[Prüfer](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/session-reorientation-20260914/native/checker.py), [48 Prüfgruppen als JSON](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/session-reorientation-20260914/native/verification.json), [optimierter Replay](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/session-reorientation-20260914/native/verification_optimized.json).

Die Negativkontrollen bleiben erhalten: reine μ-Shifts fehlen im Glue; konstantes Dressing lässt eine nichtnullige geschlossene D5-Ladung zurück; sein paarweiser Grade-1-Wurzelsummenansatz scheitert an Normquadrat 6; der geschlossene Lift ist nicht neutral und nicht projektionsisometrisch; der Cocycle ist nicht trivial; die primitive Lie-Schleife endet in Cartan. Der einzige korrigierte Prüferfehler war ein Python-Dezimalwert bei `(-1)**(-1)` in einem strukturellen Matrixvergleich; der Nullrest war bereits exakt null, und Parität im Exponenten entfernt diese Typmischung. Die systematische Fehleranalyse beeinflusste nur diese Testkorrektur, keinen mathematischen Anspruch.
