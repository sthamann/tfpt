# Quellenfrage: gerichtete Rekonstruktion und der fehlende Feldlift

21. September 2026 · `UR.SOURCE.ORIENTED_POLARIZATION.01` · **PARTIAL**

Der Auftrag ist die Herleitung der tatsächlich geladenen P1-Felder, ihres Zustands und ihrer gemeinsamen Zeitantwort. Ein passendes freies Fermionmodell allein erfüllt ihn nicht. Dieser Contract liefert eine konstruktive skalare Rekonstruktion, prüft ihre Anwendbarkeit am Original und lokalisiert die erste noch fehlende Abbildung. Kein physisches Gate wird geschlossen.

## 1. Das Vorzeichen aus der Orientierung gewinnen

Sei M eine glatte kompakte orientierte Riemannsche Fläche mit glattem, zusammenhängendem Rand. Λ sei ihr echter masseloser skalarer Laplace-Dirichlet-to-Neumann-Operator (DtN), mit auswärts gerichtetem Normalenvektor. ∂s bezeichnet die positiv orientierte Einheitstangente. Dann gilt

\[
\mathcal A_{\rm hol}:=\ker(\Lambda+i\partial_s)
=\operatorname{Tr}_{\partial M}\mathcal O(M).
\tag{1}
\]

Für glatte Randfunktionen ist das eine unital multiplikative Algebra. Für ζ=a+ib lauten die reellen Bedingungen Λa=∂s b und Λb=−∂s a. Dies ist der etablierte Rand-Cauchy–Riemann-Satz, kein neues TFPT-Axiom; siehe [Belishev–Korikov, Gleichungen (3), (7) und den anschließenden Beweis](https://arxiv.org/pdf/2103.03944).

Auf der Einheitskreisscheibe ist D=−i∂θ und Λ=|D|. Daher

\[
(\Lambda+i\partial_\theta)e^{in\theta}=(|n|-n)e^{in\theta}.
\tag{2}
\]

Der L²-Abschluss von (1) ist der Hardy-Raum n≥0. Die umgekehrte Orientierung liefert n≤0. Es wird kein Median und keine Ziel-Gram-Matrix eingesetzt. Der frühere Ausschluss „eine Spektralfunktion von |D| allein kann ±n nicht unterscheiden“ bleibt richtig: Hier kommt die bereits vorausgesetzte Randorientierung hinzu.

Für g'=e^(2σ)g gilt Δg'=e^(−2σ)Δg. Harmonie bleibt unverändert; Normalen- und Tangentialableitung erhalten am Rand denselben Faktor e^(−σb). Somit

\[
\Lambda_{g'}+i\partial_{s'}=e^{-\sigma_b}(\Lambda_g+i\partial_s),
\qquad\ker(\Lambda_{g'}+i\partial_{s'})=\mathcal A_{\rm hol}.
\tag{3}
\]

Dies ist eine Gleichheit von Unterräumen glatter Funktionen. Der orthogonale Projektor benötigt zusätzlich ein bestimmtes Rand-L²-Produkt. Bei Änderung der Randdichte muss die Hilbertraumidentifikation gesondert behandelt werden. Konische Punkte, ausgeschnittene Marken und andere Operator-Domänen sind nicht automatisch durch den glatten Satz abgedeckt. Eine positive Matrix mit Hauptsymbol |n| ist noch kein solcher DtN.

## 2. Ursprungstest am tatsächlichen v210-Kandidaten

`verification/v210_mark_local_dtn.py` definiert genau

\[
\Lambda_f=|D|+M_f,\quad
f(\theta)=\sum_{j=0}^3e^{4(\cos(\theta-j\pi/2)-1)}>0.
\tag{4}
\]

Jeder echte masselose skalare DtN annihiliert Konstanten, weil die harmonische Fortsetzung von 1 konstant ist. Dagegen ist Λf 1=f≠0. Mehr noch:

\[
\Lambda_f+i\partial_\theta=|D|-D+M_f
\ge(\min f)I\ge4e^{-8}I>0.
\tag{5}
\]

Sein CR-Kern ist leer. Nicht einmal die Einheit liegt darin. Der literal eingesetzte additive Operator (4) kann deshalb kein masseloser skalarer Laplace-DtN auf diesem Funktionenraum sein. Als Potential-/Massenterm oder Näherung an einen anders definierten Operator ist er dadurch nicht ausgeschlossen; dann müssten Operator und Domäne angegeben werden, und (1) wäre nicht einfach anwendbar.

Mit den unveränderten Originalfunktionen erhält der Prüfer:

| Fourier-Cutoff N | kleinster Eigenwert von Λf−D | Norm Λf 1 |
|---:|---:|---:|
| 16 | 0.6490204475 | 0.8409102361 |
| 32 | 0.6318091103 | 0.8409102361 |
| 64 | 0.6249901560 | 0.8409102361 |

Die gemessene Profiluntergrenze beträgt 0.6219234320. Die Zahlen illustrieren (5); der Ausschluss folgt bereits analytisch. Clock-Invarianz und die ursprünglichen Kommutatorchecks bleiben gültig.

## 3. Holomorphe Funktionen sind noch keine Majorana-Felder

Für einen reellen 16-dimensionalen Multiplizitätsraum und die Konjugation Γ(e_n⊗v)=e_(−n)⊗v̄ benötigt eine selbstduale CAR-Kovarianz C

\[
0\le C\le I,\quad C=C^*,\quad C+\Gamma C\Gamma=I.
\tag{6}
\]

Ein Projektor mit (6) definiert einen reinen quasifreien Fockzustand. Siehe [Böckenhauer–Fuchs, Abschnitt 2, Gleichungen (2.6)–(2.11)](https://arxiv.org/pdf/hep-th/9602116). Das Vorzeichen für den besetzten Projektor ist konventionsabhängig; hier wird die positive Frequenz als C-Konvention gewählt.

Auf periodischen Moden gilt für die skalare Hardy-Projektion

\[
P_{\ge0}+\Gamma P_{\ge0}\Gamma=I+P_0.
\tag{7}
\]

Die kompatible Ergänzung der festen nichtnulligen Moden hat genau die Form

\[
C=P_{n>0}\otimes I+P_0\otimes C_0,
\quad C_0+\overline{C_0}=I.
\tag{8}
\]

Reinheit verlangt C0²=C0=C0*. Im Nullsektor folgt rank C0=8. Solche Projektoren entsprechen orthogonalen komplexen Strukturen auf R16; pro orientierter Komponente ist ihre Familie SO16/U8. Ein mit der vollen irreduziblen Spin16-Vektorwirkung kommutierender C0 ist hingegen skalar: (8) erzwingt I/2, also einen gemischten Zustand. Diese bedingte Symmetrieaussage setzt Spin16 nicht als physische Eichgruppe voraus.

v113 konstruiert eine endliche Rang-8-Polarisierung als gesamte endliche Seam-Kovarianz. Sie ist dort nicht als räumlicher Nullsektor P0⊗C0 identifiziert. Diese neue Einbettung würde einen eigenen Ursprungssatz benötigen.

Auch die v210-Median-Kovarianz löst (6) nicht mit der natürlichen skalaren Konjugation: Λf ist reell, also ΓCΓ=C. Dann würde (6) C=I/2 verlangen. Ein nichttrivialer reeller Signprojektor ist keine selbstduale Majorana-Kovarianz dieses Raumes. Eine gewöhnliche komplexe CAR-Kovarianz kann er trotzdem sein.

## 4. Konstruktiver Anschluss über das Spinbündel

Ein holomorphes Spinorfeld auf einer Scheibe hat lokal die Form ψ=h(z)(dz)^(1/2). Auf z=e^(iθ) erscheint in der mitrotierenden Tangentialtrivialisierung der Faktor e^(iθ/2). Reguläre holomorphe h mit Potenzen z^n, n≥0, liefern positive Frequenzen

\[
r=n+\tfrac12,\qquad r\in\mathbb Z+\tfrac12.
\tag{9}
\]

Das ist die bounding-/Neveu–Schwarz-Struktur (NS). Beim untwisted freien Kreis-Dirac gibt es keinen Nullmodus. Auf diesem tatsächlich identifizierten Spinorraum erfüllt C=P_(r>0) bereits (6) und ist rein. Eine Medianverschiebung und ein C0 sind dann unnötig.

Die hinreichende Voraussetzung lautet: Das geladene Originalfeld ist als Spinorsektion der ursprünglichen Normalfläche nachgewiesen, einschließlich Ladungsbündel, Verbindung, CAR-Konjugation und Domäne. Im untwisted freien Scheibenfall führt das zu (9) und zum eindeutigen quasifreien Grundzustand. Eine zusätzliche Eichholonomie kann das Dirac-Spektrum verschieben und Nullmoden erzeugen; NS allein garantiert bei beliebiger Verbindung keine Lücke.

Wenn außerdem der tatsächliche Transfer den freien positiven Rotations-/Zylinderenergien r entspricht, lautet der zeitlich geordnete Zweipunktkern für τ>0 in der Konvention dθ/(2π)

\[
S_{\rm NS}(\tau,\theta)
=\sum_{r\in\mathbb N_0+1/2}e^{-r(\tau-i\theta)}
=\frac{1}{2\sinh((\tau-i\theta)/2)}.
\tag{10}
\]

Der interne Faktor ist I. Gleichung (10) ist der τ>0-Zweig; die vollständige fermionische zeitgeordnete Distribution wird für negative Zeitdifferenz mit dem Austauschvorzeichen fortgesetzt. Höhere Korrelatoren folgen aus der quasifreien Pfaffianregel. Im periodischen freien Fall wäre S_R=I/(e^(τ−iθ)−1)+C0. Die geometrische Summe wird exakt geprüft; (10) ist **noch keine physische P1-Zeitantwort**, weil der Feld- und Transferanschluss fehlt. Die Energien 3,4,5 werden weder eingesetzt noch als notwendiges Spektrum jeder TFPT-Lösung verlangt.

## 5. Stärkste vorhandene Spinbegründung am Original geprüft

P1 steht in `tfpt_1_architecture_e8.tex:167` als primitiver reflexionspositiver Randkern mit Einheitswindung. Die Normalflächen-Kompaktifizierung zu S² wird ab Zeile 1640 als bedingtes, mit mC markiertes P1-Hardening eingesetzt; sie ist dort kein geschlossener Folgesatz allein aus dem abstrakten P1. S² besitzt tatsächlich eine eindeutige Spinstruktur, deren von einer Scheibe induzierte Randstruktur bounding ist. Unter dieser Geometrievoraussetzung zeigt das, **welche Struktur ein solches Spinorfeld hätte**. Ein skalares Feld wird dadurch nicht zum Spinor.

- v492 `section5` berechnet SU2-Lifts geometrischer Rotationen: Vierteldrehung zu Ordnung 8, ihr Quadrat zur Deckwirkung. Kein geladener P1-Feldgenerator wird auf eine Spinorsektion abgebildet.
- v506 `part_b` setzt `D_ns=shift_matrix(16,8,-1)` und als Kontrolle `D_r=shift_matrix(16,8,+1)` ein. Das angeführte S²-Argument ist geometrisch richtig, sofern die Felder diesen induzierten Spinlift tragen. Diese Voraussetzung wird im Check nicht konstruiert.
- Beide Matrizen haben dieselben absoluten Permutationseinträge, aber D_NS²=−I und D_R²=+I. Die geometrische Halbwendung allein legt den Spinlift des Feldes nicht fest.
- v510 klassifiziert Fock-Lifts innerhalb der eingesetzten NS-Wirkung. v110s endliche Sheet-Oddness S+↔S− ist keine nachgewiesene räumliche NS-Monodromie. v113 wählt zunächst einen Fock-Vakuumzustand.

Die algebraische Grenze ist direkt beweisbar: Implementiert U auf einer irreduziblen vollen Clifford-Darstellung eine Majorana-Wirkung O mit O²=I, dann kommutiert U² mit allen Majoranas und ist skalar. Fermionparität wirkt auf jeder Majorana mit Minuszeichen und ist nicht skalar. Für U²=Fermionparität muss daher die Einteilchenwirkung bereits O²=−I haben, bis auf den skalaren Implementerfaktor. Der NS-signierte Lift liefert genau das. Die Clifford-Rechnung erzeugt das räumliche Vorzeichen nicht aus der bloßen Permutation.

## 6. Mitwandernder v210-Kandidat: erhalten, aber nicht überbewertet

Der vorherige Contract bewies den Nullgrenzwert der Median-Kovarianz auf fest identifizierten Fouriermoden. Das schließt eine mitwandernde Beschreibung nicht aus. Für N∈8Z, m=N/2, V=f−f0 ergeben feste lokale Kompressionsmatrizen um +m und −m nach Subtraktion von m+f0 exakt

\[
H_+=D+V,\quad H_-=-D+V;
\qquad H_+=UDU^*,\quad H_-=U^*(-D)U,
\tag{11}
\]

wobei F'=V periodisch und U=e^(−iF). Beim analytischen Profil verschwinden Kreuzmatrixelemente f_(N+k−l) für feste k,l. Das ergibt einen begründeten lokalen Kandidaten aus zwei gegenläufigen Zweigen. Ihre Clockwirkung ist für diese Cutoffs jeweils i^k und wählt keinen aus.

Ein vollständiger Beweis der asymptotischen Medianlage und der Konvergenz der Signprojektoren folgt nicht aus den lokalen Identitäten. Die endliche Rechnung stützt ihn außerhalb der Schwelle. Auf der Schwelle kollabiert die Aufspaltung auf etwa 4·10^−6, 1.5·10^−13 und 4.1·10^−30 für N=16,32,64; Double-Precision wird dort unzuverlässig.

Bei flachem Profil ist die Regulatorabhängigkeit exakt sichtbar: μ_N=N/2. Gerade N geben ganzzahlige lokale Frequenzen mit Nullmode, ungerade N halbzahlige ohne Nullmode. Das ist keine Herleitung einer physischen Spinstruktur. Der beigefügte Rezentrierungsbericht bewahrt diese Grenzen. Er verhindert einen voreiligen Ausschluss aller mitwandernden Kandidaten; die P1-Auswahl liefert er nicht.

## 7. Was zum Schluss der Quellenfrage konkret fehlt

Die skalare Richtungsauswahl ist konstruktiv. Der erste ungelieferte Ursprungssatz ist eine Abbildung

\[
\iota_{\rm spin}:\text{geladene P1-Randgeneratoren}
\longrightarrow\Gamma(\partial M,S_{\partial M}\otimes E),
\tag{12}
\]

die das tatsächliche Spin-/Ladungsbündel, die CAR-Konjugation, Ladungen, Produkte und Gram-Form erhält. Danach muss der ursprüngliche Transfer auf demselben Raum mit dem geometrischen/geladenen Generator verflochten werden. Eine natürlich mögliche Cliffordisierung der skalaren Algebra ist noch kein Nachweis von (12). Internes Spin10, Spin16, räumlicher Spinlift und Lorentzspin sind verschiedene Gruppenwirkungen.

Bestehende Compiler-, Flavor- und Yukawa-Rechnungen bleiben bestehen. Ihr physischer Quellzustand wird hier nicht rückwirkend hergeleitet. Die Quellenfrage ist konstruktiver gefasst, aber noch nicht vollständig gelöst: Der ursprüngliche skalare Randkern und die behaupteten geladenen Feldgeneratoren müssen als konkrete Operatoren aufeinander bezogen werden.

## Nachweise

`source_pins.json` fixiert die gelesenen Originale samt Repository-HEAD. `checker.py` prüft Fourier-/CAR-Identitäten, die beiden Original-Spinlifts, den unveränderten v210-Kandidaten und die Korrelatorsumme. Unendlichdimensionale Aussagen folgen aus den angegebenen Beweisen bzw. dem zitierten Satz, nicht aus endlich vielen Checks. Ein unabhängiger Review liegt bei. Research-Firewall: keine Ledger-/Paper-/Website-Promotion, keine T1–T8-Schließung, kein Vollständigkeitsanspruch.
