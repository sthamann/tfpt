# Prüfung der zehn Bilder: TFPT, RH und Faktorisierung

Die anschließende Quellenrechnung zur Seam-Kovarianz steht in
[SEAM_FORTSETZUNG.md](SEAM_FORTSETZUNG.md): explizite QWZ-Reflexion,
Clock-Hindernis und algebraische Clock-Umkehr im gekoppelten 16D-Compiler.

Stand: 8. September 2026. Geprüfter lokaler Commit: `b803b7e5`.
Der Arbeitsbaum enthielt bereits weitere, teils unveröffentlichte Forschungsarbeiten.
Diese Untersuchung erzeugt nur den vorliegenden eigenen Ordner. Keine Promotion,
keine Änderung am Statusledger. **Kein RH-Beweis, kein neuer Faktorisierungsalgorithmus.**

Das Material enthält eine fachlich sinnvolle Analogie — primitive Bahnen,
Spurformeln und arithmetische Korrespondenzen —, aber keine bereits hergeleitete
TFPT-Geometrie der Primzahlen. Mehrere vorgeschlagene Schritte existieren im
Repository bereits mit engeren Ergebnissen und ausdrücklich offenen Übergängen.
Die behauptete Priorität des Double-Cover-Wegs folgt aus den Bildern nicht.

## 1. Was an den Bildern stimmt und was korrigiert werden muss

| Aussage | Befund |
|---|---|
| Primzahlen / primitive periodische Bahnen / Spektrum sind durch Spurformeln verbunden | Tragfähiger Forschungsrahmen. Die Riemann–Weil-Explizitformel ist bewiesen; offen ist die passende unabhängige geometrische und positive Spektralrealisierung. |
| Zusammengesetzte Zahlen seien Wiederholungen primitiver Bahnen | Nur **Primzahlpotenzen** sind Wiederholungen einer einzelnen Primzahlbahn. `6=2·3` ist eine Kombination verschiedener primitiver Faktoren. |
| Eine solche Geometrie erkläre automatisch die GUE-Statistik | Zu stark. Statistik hängt von Dynamik, Symmetrien und Mittelung ab. Arithmetische hyperbolische Systeme können andere Statistik besitzen. GUE-Übereinstimmung identifiziert keinen Operator. |
| Double cover erzwinge die Funktionalgleichung | Eine lineare Involution liefert zunächst eine ±-Zerlegung. Für eine Wirkung auf den Mellin-Parameter fehlt ein Skalenraum samt Maß und Intertwiner. |
| Die kritische Linie sei der Fixbereich von `s↦1−s` | Falsch: diese Abbildung fixiert nur `s=1/2`. Die Linie ist die Fixmenge von `s↦1−conj(s)`. |
| Funktionalgleichung plus Double cover sei stärker als Selbstadjungiertheit | Falsch. Symmetrie erlaubt Nullstellen abseits der Linie in Paaren bzw. Quartetten. |
| Hecke-Worte gäben bereits die passende Fredholm-Determinante | Im vorhandenen Versuch falsch: endliche reine Verschiebungsmatrizen haben Determinante 1. Euler-Faktoren und Pfadresolvente müssen getrennt werden. |
| CY-Dualität könne Positivität in den Zeta-Faktor übertragen | Das ist gerade der offene Übergang. Der kanonische Tate-Faktor ist eine universelle skalare Linie; er transportiert nicht automatisch die besondere TFPT-Geometrie. |

Zur Funktionalgleichung gilt präzise

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\xi(s)=\xi(1-s).
\]

Es ist nicht die unvollständige Zeta-Funktion allein, die ohne Vorfaktoren gerade
um `1/2` ist. Quelle: [NIST DLMF §25.4](https://dlmf.nist.gov/25.4).
Spurformelkontext: [Connes, 1998](https://arxiv.org/abs/math/9811068).
GUE und die besondere Rolle arithmetischer Systeme:
[Bogomolny, Quantum and Arithmetical Chaos](https://arxiv.org/abs/nlin/0312061).

Die ergänzenden Beispiele aus Foto 10 liefern keine gemeinsame TFPT-Ableitung:
Das Ionenexperiment programmiert die Mikrowellenanregung gezielt so, dass
Zeta-Nullstellen in der Dynamik messbar werden; es findet keinen autonomen
Primzahlgenerator. Siehe [He et al., 2021](https://arxiv.org/abs/2102.06936).
Für Zikaden existieren mehrere evolutive Mechanismen; die Aussage, Primzyklen
seien allgemein der einzige stabile Ausgang eines Räuber-Beute-Systems, ist
nicht gedeckt. Beispielsweise untersucht
[Hybridization selects for prime-numbered life cycles](https://pmc.ncbi.nlm.nih.gov/articles/PMC7319174/)
ein spezifisches Hybridisierungsmodell. In einer Ulam-Spirale werden auf Geraden
quadratische Zahlenfolgen sichtbar. Ihre lokalen Teilbarkeitseigenschaften
erklären einen Teil der Muster; daraus folgt keine neue Spektralgeometrie.

## 2. Die konkrete TFPT-Involution: richtig, aber typgebunden

Auf dem Träger `E=E3⊕E2` gilt

\[
Y=\operatorname{diag}(-1/3,-1/3,-1/3,1/2,1/2),\qquad
\iota=(12Y-I)/5=\operatorname{diag}(-1,-1,-1,1,1).
\]

Damit sind `iota²=I`, `P3=(I−iota)/2`, `P2=(I+iota)/2` exakt.
Der aktuelle Architekturtext enthält `6Y²−Y−I=0` und die `3+2`-Aufteilung:
[`tfpt_1_architecture_e8.tex`](../../tfpt_1_architecture_e8.tex), um Zeile 4916.
Die affine Formel ist zusätzlich explizit im archivierten Trägerauszug
[`02_carrier_source.tex`](../../_archive/tfpt-45/source_extracts/02_carrier_source.tex), Zeilen 338–355.
Das ist keine frei erfundene Formel aus den Screenshots.

**Aber die Trägerräume dürfen nicht vermischt werden.** Die obige Formel gilt
auf den fünf Slots. Auf `Λeven E` wird die Involution durch die Exteriorwirkung
angehoben: `v1∧…∧vk ↦ iota v1∧…∧iota vk`. Diese hat `8+8` Vorzeichensektoren.
Die affine Formel auf dem *gesamten* Hypercharge-Operator dieses 16-dimensionalen
Raums ist keine Involution: Schon das Vakuum hat Hypercharge 0 und würde auf
`−1/5` abgebildet. Der spätere endliche Dirac-Träger ist nochmals größer.
Die Identifikation mit Chiraliät, Blattwechsel oder einer modularen Reflexion
braucht jeweils eine explizite Abbildung zwischen denselben Räumen.

Eine einfache strukturelle Grenze folgt unmittelbar: Jedes Polynom `f(Y)`
kommutiert mit `iota`. Wegen der quadratischen Relation reduziert es sich auf
`aI+bY`. Aus `Y` allein entsteht somit kein nichttrivialer `iota`-ungerader
Generator. Ein solcher braucht zusätzliche Kopplungsdaten.

Für `D(z)=D0+zD1` gilt der vorgeschlagene erste Test genau dann, wenn

\[
\iota D_0\iota=D_0,\qquad \iota D_1\iota=-D_1.
\]

Auf dem `3+2`-Träger besteht ein ungerades `D1` aus rechteckigen `3×2`- und
`2×3`-Blöcken. Der Raum solcher Matrizen ist 12-dimensional; jede hat Rang
höchstens 4. Ein Restnullmodus ist dort dimensionsbedingt. Das schließt einen
größeren Träger nicht aus und ist kein allgemeines Dirac-No-go.

## 3. Die ersten beiden vorgeschlagenen Tests reichen nicht

Ein exaktes Gegenmodell auf **derselben TFPT-Involution**:
Sei `B03=B30=4`, alle anderen Einträge von `B` null, und `D(z)=I5+zB`.
Dann gelten

\[
\iota D(z)\iota=D(-z),\qquad
\det D(z)=\det D(-z)=1-16z^2.
\]

Trotzdem liegen die Nullstellen bei `z=±1/4`, also bei `s=1/4,3/4`.
Sie liegen im kritischen Streifen und **nicht** auf dessen kritischer Linie.
Das ist ein Gegenbeispiel zur behaupteten logischen Folgerung, kein Modell
der Riemann-Zeta-Funktion und kein Gegenbeispiel zu RH.

Außerdem ist die genaue Wahl des Pencils entscheidend. Aus einem chiralen
Operator `iota H iota=−H` folgt für `P(z)=H−zI`

\[
\iota P(z)\iota=-P(-z),\qquad
\det P(z)=(-1)^{\dim E}\det P(-z).
\]

In ungerader endlicher Dimension ist die Determinante ungerade, nicht gerade.
Der erste Screenshot-Test darf daher nicht ungeprüft auf einen gewöhnlichen
Dirac-Spektralpencil angewandt werden. Für unbeschränkte Operatoren müssen
Definitionsbereich, Reflexionsinvarianz und Determinantenregularisierung
zusätzlich nachgewiesen werden.

## 4. Woher eine Mellin-Spiegelung tatsächlich kommen kann

Auf einem Skalenraum `x>0` definiere

\[
(R_wf)(x)=x^{-w}f(1/x),\qquad
\mathcal Mf(s)=\int_0^\infty f(x)x^s\,\frac{dx}{x}.
\]

Substitution liefert auf einem gemeinsamen Konvergenzbereich

\[
R_w^2=I,\qquad \mathcal M(R_wf)(s)=\mathcal Mf(w-s).
\]

`R_w` ist für reelles `w` unitär auf `L²(x^w dx/x)`.
Für `Θ=−x∂x` gilt auf kompaktem glattem Kern `R_w Θ R_w=w−Θ`.
Die Zentrierung ist **für jedes w** `w/2`; erst das unabhängig bestimmte Maß
`w=1` liefert `1/2`. Die Gruppe Z2 allein wählt dieses Maß nicht.

Das zeigt zugleich den konstruktiven Anschluss: Ein TFPT-Blattoperator müsste
in einer nachgewiesenen Darstellung diesen *gewichteten Skalenwechsel*
implementieren. Die additive Umbenennung `s=1/2+z` stellt diese Darstellung
nicht her. Selbst eine gelungene Darstellung wäre erst die Symmetrie, noch
keine Identifikation des vollständigen Zeta-Spektrums.

## 5. Der direkteste Anschluss an den vorhandenen D_rel

Der aktuelle Text identifiziert den endlichen modularen Readout mit

\[
K(C)=\log((I-C)C^{-1}),\qquad 0<C<I.
\]

Siehe [`tfpt_2_standard_model.tex`](../../tfpt_2_standard_model.tex), Zeilen 3610–3627,
und [`v258_dirac_covariance_induction.py`](../../verification/v258_dirac_covariance_induction.py).
Der Verifier unterscheidet die klassische Inversionsidentität von der
konditionalen Seam-Identifikation. Er erzeugt in seinen Beispielen `C` aus
bereits gegebenem `H` und gewinnt `H` zurück. Das beweist die Umkehrformel,
keine unabhängige Entstehung des Spektrums aus der Seam.

**Der passende konkrete erste Test ist deshalb:** für eine korrekt angehobene
unitäre Involution `U` und eine unabhängig erzeugte Seam-Kovarianz

\[
U C U^{-1}\stackrel{?}=I-C.
\]

Dann folgt durch Funktionalkalkül

\[
U K(C) U^{-1}=-K(C).
\]

Eine erlaubte Kovarianz oder KMS-Zustandseigenschaft allein erzwingt die erste
Identität nicht. Ein diagonaler Kontrollzustand mit Besetzungen
`(.2,.3,.4,.6,.7)` ist ein Gegenbeispiel auf dem fünfteiligen Träger.
Im neuen Probeprogramm besteht ein *konstruiertes* ungerades Beispiel den
Test; der Kontrollzustand fällt durch. Diese Rechnung prüft die Implikation,
nicht die physische Seam-Quelle. Man darf weder `C` aus dem gewünschten
Zeta-Operator bauen noch die ungerade Projektion nachträglich als Ableitung
ausgeben. Für eine komprimierte Kovarianz braucht es zudem die Verträglichkeit
des Kompressionsprojektors mit `U`.

Auch bei Erfolg fehlen weiterhin der unendliche Skalenraum, die arithmetische
Spuridentifikation und ein unabhängiger Positivitäts- bzw. Selbstadjungiertheitssatz
mit vollständiger Nullstellenzuordnung.

## 6. Primitive Orbits: zwei zusätzliche Hindernisse

Im Euler-Halbraum gilt

\[
\log\zeta(s)=\sum_p\sum_{k\ge1}\frac{p^{-ks}}{k},\qquad
-\frac{\zeta'(s)}{\zeta(s)}=\sum_p\sum_{k\ge1}(\log p)p^{-ks}.
\]

Die logarithmische Ableitung hat Unterstützung auf Primzahlpotenzen.
Produkte verschiedener Primzahlen erscheinen in der Zeta-Funktion, aber
nicht als zusätzliche primitive `pq`-Terme in dieser logarithmischen Ableitung.
Der Operatorpotenzindex zählt Umläufe; geometrische Zeit wäre `k log p`.
Das sind nicht automatisch dieselben Indizes wie ein Integer-Index `n`.

**Blattwechsel:** Hat die Monodromie einer Basisbahn Länge `ell` auf zwei
Blättern die Matrix `S=[[0,1],[1,0]]`, ist mit `x=exp(−s ell)`

\[
\det(I-xS)=1-x^2,\qquad \operatorname{tr}S^k=
\begin{cases}0&k\text{ ungerade},\\2&k\text{ gerade}.\end{cases}
\]

Der vollständige Deck-Trace liefert also `(1−x²)⁻¹` statt `(1−x)⁻¹`.
Auf der Überlagerung schließt die Bahn erst nach `2ell`. Setzt man die
Basislänge auf `log p`, verliert man gerade die ungeraden Primzahlpotenzen.
Eine andere Basislänge, Charakterprojektion oder relative Spur ist möglich,
muss aber unabhängig begründet werden. Das widerlegt das automatische
Argument aus Foto 7, nicht jede denkbare Double-Cover-Konstruktion.

**Gemischte Bahnen:** Im minimalen gekoppelten Modell

\[
L=\begin{pmatrix}x&cx\\cy&y\end{pmatrix},\quad
\det(I-L)=1-x-y+(1-c^2)xy
\]

hat `−log det(I−L)` den gemischten Koeffizienten `[xy]=c²`.
Bei `c=0` liegt das getrennte Eulerprodukt vor; bei Kopplung entstehen
gemischte Umläufe. Eine Seam, die die Primkanäle koppelt, braucht deshalb
einen echten Mechanismus für das Fehlen oder die exakte Auslöschung dieser
Beiträge. Dieses Zweikanalmodell ist kein universelles Graph-No-go.

## 7. Was das Repository hier bereits hat

| Vorhandener Baustein | Genaue Reichweite |
|---|---|
| E8-Theta / Hecke / markierter f8-Kanal | `Theta_E8=E4`, Schalen `240 sigma3(n)`, Eisenstein-Dirichletreihe `240 zeta(s)zeta(s−3)`; konkrete arithmetische Identitäten. |
| Hecke-Pfadraum T52 | Unendlicher arithmetischer Träger als Kandidat; reine endliche Verschiebungen sind strikt dreieckig, also `det(I−L)=1`. Kein Zeta-Fredholm-Operator hergeleitet. |
| Lokaler adelischer Fixpunktkernel | `k_v(q)=|q|_v^(1/2)/|1−q|_v`, inversionssymmetrisch; bei `q=p^k` liefert der p-adische Anteil `p^(−k/2)` und die normierte Ableitung `log(p)p^(−k/2)`. |
| All-place/Tate-Projektion v1021 | `End(V)=Q_l(0)⊕Ad⁰(V)` isoliert den Zeta-Faktor exakt, einschließlich unvermeidlichem Tate-Anteil bei p=2 und Gamma-/Polnormalisierung. |
| Globaler RH-Übergang | Identifikation der gesamten signierten Weil-Form mit einer unabhängig positiven globalen Form bleibt offen. |

Die Korrektur am Hecke-Pfadraum steht ausdrücklich in
[`hecke_orbit_transfer_probe.py`](../tfpt-discovery/hecke_orbit_transfer_probe.py), Zeilen 94–106.
Die vollständige lokale Kernel-Probe aus der früheren Untersuchung liegt unter
`/Users/stefanhamann/Documents/Codex/2026-09-04/unte/outputs/local_adelic_fixedpoint_kernel_probe.py`;
sie wurde erneut ausgeführt. Ihre Primzahlen sind Prüfeingaben für lokale
Identitäten, kein Nachweis autonomer Primzahlentstehung. Die Produktformel
liefert für den bloßen Gesamtprodukt-Kernel sogar `prod_v k_v(q)=1`: Man muss
Ortsbeiträge als Distribution erhalten, nicht bloß multiplizieren.

Der aktuelle [All-place-Bericht](../../rh/catalog/analysis/all_place_tate_audit.md)
erklärt, weshalb die skalare Tate-Projektion keine zusätzliche TFPT-Positivität
transportiert. Sein endlicher Rang-No-go gilt für einen **festen endlichen
linearen Pullback**, unter der ausdrücklich externen strikten Fensteruntergrenze;
er schließt wachsende Räume und unendliche Grenzobjekte nicht aus. v1021 wurde
hier erneut ausgeführt: 23 Prüfungen bestanden, globaler Übergang weiter offen.

Für den Zeta-Primanteil ist auf Log-Zeit beispielsweise die symmetrische
Distribution mit Gewichten
`log(p)p^(−k/2) [delta_(k log p)+delta_(−k log p)]` zu treffen. Zusätzlich
braucht die volle Explizitformel den korrekten Vorzeichenbeitrag, den
archimedischen Term, Pole, zulässige Testfunktionen und Regularisierung.
Die Gewichtskontrolle allein ist noch nicht die ganze Spurformel.

## 8. Verbindung zum Faktorisierungszweig

Hier ist die Geometrie bereits konkret: Gauß-Reduktion quadratischer Formen,
Kettenbruchzyklen von `sqrt(N)`, quadratische Einheiten und Regulatoren.
Diese Systeme nehmen die zu zerlegende Zahl `N` tatsächlich als Eingabe.
Der aktuelle Solver [`seam_geodesic_factor.py`](../tfpt-discovery/seam_geodesic_factor.py)
verwendet SQUFOF und gegebenenfalls Pollard–Brent. Er ist ein klassischer
Faktorisierer; seine Bezeichnung als Seam macht ihn nicht zu einem neuen
TFPT-Verfahren. Zwei kleine SQUFOF-Läufe wurden wiederholt, mit exakten Faktoren:
`1050589=1019·1031` und `100160063=10007·10009`. Die nahe beieinanderliegenden
Faktoren sind einfache Smoke-Fälle, ausdrücklich kein Laufzeitbenchmark.

**Die Geodäten sind nicht bereits die gesuchten Primzahlbahnen.** Für einen
hyperbolischen `gamma` in `PSL2(Z)` gilt

\[
\ell(\gamma)=2\log\varepsilon,\qquad
|\operatorname{tr}\gamma|=\varepsilon+\varepsilon^{-1}\in\mathbb Z.
\]

Wäre `ell=log p`, müsste die ganzzahlige Spur das Quadrat

\[
t^2=p+2+1/p
\]

besitzen. Das ist für jede ganze Zahl `p>1` nicht ganzzahlig: ein Widerspruch.
In der Standardparametrisierung ist also keine solche modulare Geodätenlänge
`log p`. Eine neue Zeitparametrisierung wäre zusätzliche Mathematik.
Längenspektrum und echte Mayer-Determinante beschreibt
[Zagier, New Points of View on the Selberg Zeta Function](https://people.mpim-bonn.mpg.de/zagier/files/tex/NewPointsSelbergZeta/fulltext.pdf).
Die dortige Determinante ist die **Selberg-Zeta-Funktion**, nicht automatisch
die Riemann-Zeta-Funktion. Selbstadjungiertheit des modularen Laplaceoperators
löst diese Identifikationsfrage nicht.

Der konkrete offene Rechenhebel ist der Regulator. Der aktuelle
[`regulator_jump_probe.py`](../tfpt-discovery/regulator_jump_probe.py) implementiert
den intrinsischen Sprung aus einem gegebenen Regulator bzw. geeigneten Vielfachen.
Die Kosten seiner Beschaffung bleiben separat. Die zugrunde liegende Arbeit
[Murru–Salvatori, v2](https://arxiv.org/html/2409.03486v2) gibt eine bedingte
polynomielle Nachbearbeitung; ihre zitierte Regulatorvorberechnung nutzt GRH.
Dieser Faktorisierungszweig liefert damit keinen RH-Beweis. Er ist in diesem
Audit quellengeprüft, aber nicht erneut vollständig benchmarked.

Ein fixer Z2-Operator kann Symmetriepunkte erklären; er berechnet nicht deren
N-abhängige Lage oder Distanz. Eine echte Verbesserung müsste genau diese
fehlende Information günstiger gewinnen. Alternativ wäre ein schneller
E8-Koeffizientenzugriff relevant: Für verschiedene Primzahlen `p,q` und `N=pq`
liefert `sigma3(N)−1−N³=p³+q³` den Wert `r=p+q` als positive passende Wurzel von
`r³−3Nr=p³+q³`; danach spaltet `X²−rX+N`. Das ist eine klassische Reduktion,
kein schneller Koeffizientenauswerter. Schalen-/Divisoraufzählung kann die
eigentliche Arbeit verstecken.

## 9. Präzise nächste Beweisfragen und Stopbedingungen

**TFPT-Symmetrie, kleinster sinnvoller neuer Test:** Einen konkreten Seam-Zustand
`C_L`, dessen Quellkonstruktion keine Ziel-Eigenwerte verwendet, einen Trägerlift
`U_L` und kompatible Kompressionen festlegen. Dann `U_L C_L U_L⁻¹=I−C_L`
beweisen oder widerlegen. Quelle, Definitionsbereich und Maß müssen vorab feststehen.
Wenn die Identität nur durch Erzeugen von `C` aus einem bereits ungeraden `H`
oder durch nachträgliche Projektion gilt, wurde nur die bekannte Umkehrformel geprüft.

**RH, danach als separater schwerer Satz:** Aus derselben Konstruktion eine
unbeschränkte kompatible Skalenfamilie erzeugen; alle Primzahlpotenzen samt
Amplituden, fehlenden gemischten Orbits, Gamma-/Poltermen und Vorzeichen auf
einer dichten Testklasse identifizieren. Dazu unabhängige globale Positivität
oder einen selbstadjungierten Operator mit vollständiger, nullstellenunabhängig
hergeleiteter Spektralidentifikation beweisen. Eine gerade Determinante reicht nicht.
Ein schon mit Primzahlen beschrifteter Graph wäre eine arithmetische Realisierung;
für die stärkere Behauptung, TFPT leite Primzahlperioden ab, müsste ihre
Beschriftung selbst aus den Ausgangsdaten folgen.

**Faktorisierung:** Einen allein aus `N` gespeisten Regulator-/Perioden-Readout
entwickeln und gegen die vorhandene klassische Pipeline vergleichen. Gemessen
werden gesamte Vorverarbeitung, Querys, Präzision, Speicher, Wiederholungen
und Faktorauslesung. Ein Test mit geliefertem Regulator zählt nur für die
Nachbearbeitung. Es gibt aus den Bildern noch keinen konkreten neuen Readout,
den man fair als Beschleunigung implementieren oder messen könnte.

Die gemeinsame Sprache ist arithmetische Korrespondenz plus Skalen-/Periodendynamik.
Das gemeinsame **neue Objekt** ist noch nicht konstruiert. Deshalb folgt aus
den Korrelationen keine Rechtfertigung, RH und Faktorisierung auf denselben
Double-Cover-Operator festzulegen.

## 10. Reproduktion und Reichweite der Rechnungen

```sh
experiments/tfpt-discovery/.venv/bin/python experiments/double-cover-rh-audit-2026-09-08/audit_probe.py
experiments/tfpt-discovery/.venv/bin/python verification/v1021_all_place_tate_rank_audit.py
experiments/tfpt-discovery/.venv/bin/python /Users/stefanhamann/Documents/Codex/2026-09-04/unte/outputs/local_adelic_fixedpoint_kernel_probe.py
experiments/tfpt-discovery/.venv/bin/python experiments/tfpt-discovery/seam_geodesic_factor.py 1050589 100160063 --method squfof --json
```

Neue Probe: **25/25** Prüfungen; symbolische Identitäten und Gegenmodelle plus
eine numerische modulare Beispiel-/Kontrollrechnung. SymPy 1.14.0, NumPy 2.4.6.
Die Ergebnisse und Hashes der relevanten lokalen Quellen stehen in
[`results.json`](results.json), die Wiederholungen in [`v1021.log`](v1021.log),
[`local_adelic_kernel.log`](local_adelic_kernel.log) und [`factor_smoke.json`](factor_smoke.json).
Der Code ist [`audit_probe.py`](audit_probe.py).

Die Rechnungen validieren die genannten Einwände und konditionalen Identitäten.
Sie messen weder RH-Fortschritt noch einen algorithmischen Vorteil und ersetzen
keinen unendlichen Existenz-, Spuren- oder Positivitätssatz.
