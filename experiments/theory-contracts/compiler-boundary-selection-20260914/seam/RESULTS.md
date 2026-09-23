# Die echte positive Hälfte und der minimale Compiler-Anschluss

Stand: 2026-09-14. NON-RH. Nur das vorhandene freie N=8-Modell aus
`verification/v524_woit_beta2_os_quotient.py`; keine Modellvergrößerung,
keine Änderung der Quellen und keine P1-/TOE-Promotion.

## Ergebnis

Der Compiler lässt sich an die **wirkliche positive freie Naht** anschließen,
aber zunächst als zustandsabhängig gefilterter Operatorraum. Der genaue kleine
Satz ist

\[
 W^\dagger G_{\rm OS}W
   =\bigoplus_{k=0}^{4}\wedge^k M,\qquad M>0,\quad\det W=1.
\]

Hier ist M nur der 4×4-Kern zwischen den beiden Schnittseiten und W die aus
dem vorhandenen Zustand berechnete Wick-Normalordnung. Das ist nicht bloß
eine Gleichheit von Dimensionen: Der Checker verifiziert **alle 256 Einträge**
dieser Identität exakt. Damit ist der gesamte 16D-OS-Gram positiv definit.
Die positiv gefilterte Compiler-Norm ist konstruiert; ihre physische Auswahl
und ein zugehöriger voller Zeitgenerator sind damit nicht abgeleitet.

## Welche positive Hälfte liegt tatsächlich in den Quellen vor?

P1 selbst postuliert den primitiven reflektionspositiven Randkern mit
Einheitswindung (`tfpt_1_architecture_e8.tex:167`). Es gibt dort noch keine
konkrete positive Halbseitenalgebra. `v176_seam_collar_realisation.py:1`
kennzeichnet seine Zusammenstellung ausdrücklich als Reduktionszertifikat;
die physische Realisierung bleibt Voraussetzung. Auch die Zustandsidentifikation
mit dem flachen Collar bleibt in `tfpt_research_contracts.tex:747`–`772`
eine benannte offene Prämisse.

Eine wirkliche endliche positive Hälfte erscheint dagegen in v519/v524:

- Volle Algebra: die komplexe Clifford-/CAR-Algebra auf acht Majoranas.
- Positive Seite: Stellen {4,5,6,7}, Schnitt zwischen Gitterstellen,
  Spiegelung r(a)=7−a modulo 8, NS-Vorzeichen.
- Halbseitenalgebra: alle 16 Monome dieser vier Majoranas,
  \(\mathcal A_+=\mathrm{Cl}_4(\mathbb C)\simeq M_4(\mathbb C)\).
- Zustand: der festgelegte chirale quasi-freie NS-Zustand mit
  \(\omega(\gamma_a\gamma_b)=iC(a-b)\) für a≠b,
  \(C(d)=0\) für gerade d und \(C(d)=1/[4\sin(\pi d/8)]\) für ungerade d;
  höhere Momente sind durch Wick/Pfaffian gegeben.
- Die antilineare, graduierte Reflexionsvorschrift verwendet η=+i.
  Der eigentliche Naht-Gram ist
  \(G_{ab}=\omega(\Theta(e_a)e_b)\).

Die ursprüngliche Definition der operationalen Seed-Kategorie bestätigt
diese Richtung noch unmittelbarer:
`_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex:480`–`520`
setzt ein Objekt
\(\mathfrak S=(\mathfrak A_{\rm loc},\tau_t,\Theta,\omega,
[u_\Sigma],\mathcal D_{\rm coll})\) voraus. Das positive Zeitnetz,
der RP- und clusternde Zustand und der elliptische Collar-Generator sind
**Bestandteile des Eingabeobjekts**. Der anschließende Completion-Satz
konstruiert die positive Randhälfte aus einem solchen vollständigen Seed.
„Kanonisch aus S“ ist daher nicht „P1 wählt S eindeutig“; auch die Morphismen
der Kategorie müssen Zustand, Zeit und die weiteren angezeigten Daten
bereits erhalten. Hier wird lediglich diese ausdrücklich erklärte
Abhängigkeitsrichtung bestätigt, nicht die ganze analytische Completion
unabhängig neu bewiesen.

Diese Daten werden in `v524:87` ausdrücklich als gepinnte freie
Operationalisierung geführt. N=8 verwendet die **vollständige** Hälfte,
nicht einen Grad-2-Ausschnitt. Der positive Schnitt und das passende η sind
im festgelegten freien Zustand prüfbar; sie sind keine Herleitung dieses
Zustands aus P1. Die entgegengesetzte Zustandschiraliät bei unverändertem η
liefert bereits auf γ4 die negative Norm −C(1).

Eine wichtige Quellenkorrektur steht in `v524:698`–`740`: Die getwistete
Reflexion ist bei überlappenden Clifford-Produkten nicht anti-multiplikativ:
\(\Theta(\gamma^2)=1\), aber \(\Theta(\gamma)^2=-1\).
Sie darf daher nicht durch das gewöhnliche Matrixadjungieren ersetzt werden.
Die hier verwendete sesquilineare OS-Form braucht eine solche Ersetzung nicht.

## Die vierdimensionale Minimalstruktur

Setze a=C(1) und b=C(3). In der Reihenfolge γ4,γ5,γ6,γ7 ist

\[
 M=\begin{pmatrix}
 a&0&b&0\\
 0&b&0&b\\
 b&0&b&0\\
 0&b&0&a
 \end{pmatrix},\qquad
 a=\frac1{2\sqrt{2-\sqrt2}},\quad
 b=\frac1{2\sqrt{2+\sqrt2}}.
\]

Es gilt a>b>0. Nach der Sortierung {4,6} und {5,7} besteht M aus zwei
positiven 2×2-Blöcken mit Determinante b(a−b)>0. Zusätzlich kontrolliert
der Checker eine exakte algebraische LDL-Zerlegung und deren Rekonstruktion.

W bildet das gewöhnliche Monom auf sein Wick-normalgeordnetes Monom ab,
beispielsweise

\[
 W(\gamma_4\gamma_5)=\gamma_4\gamma_5-
 \omega(\gamma_4\gamma_5)1.
\]

Die Rekursion subtrahiert genau die innerhälftigen Kontraktionen des
**gegebenen** Zustands. W ist unitriangular und invertierbar. In diesem
normalgeordneten System verschwinden die Paarungen verschiedener Grade;
innerhalb eines Grades bleiben die Minoren von M, also dessen äußere
Potenzen. Ihre Dimensionen sind 1,4,6,4,1. Da M>0, sind alle diese
äußeren Potenzen positiv definit. Das beweist Rang 16 und Nullraum {0}.

## Anschluss an den eindeutigen zyklischen Compiler-Kern

Wähle einmal eine markierte Clifford-Identifikation mit dem vorhandenen
Compiler-M4. Der Checker benutzt
X⊗I, Y⊗I, Z⊗X, Z⊗Y als vier Hermitesche Clifford-Generatoren und prüft
die Relationen. Ihre 16 Monome sind bezüglich
\(\tau(A^\dagger B)=\mathrm{Tr}(A^\dagger B)/4\) exakt orthonormal.
Diese Identifikation ist eine endliche algebraische Wahl, keine zusätzliche
Behauptung, dass P1 genau diese Compiler-Markierung auswählt.

Auf diesem zyklischen 16D-Operatorraum existiert daher der eindeutige
positive selbstadjungierte Faktor

\[
 F=G_{\rm OS}^{1/2},\qquad
 \langle A,B\rangle_{\rm OS}
 =\langle FA,FB\rangle_\tau.
\]

F ist invertierbar. Für den Vakuumvektor Ω=1 gilt
\(\|F\Omega\|_\tau=1\), aber **FΩ≠Ω**: bereits
\(G_{0,(4,5)}=\omega(\gamma_4\gamma_5)=-ia\ne0\).

Die Wick-Struktur liefert außerdem einen expliziten, Vakuum-fixierenden
Faktor ohne Berechnung großer algebraischer Eigenwertausdrücke:

\[
 F_W=\left(\bigoplus_{k=0}^4\wedge^k\sqrt M\right)W^{-1},
 \qquad F_W^\dagger F_W=G_{\rm OS},\quad F_W\Omega=\Omega.
\]

F_W ist nicht als positiver selbstadjungierter Operator behauptet. Er ist
ein kanonischer Wick-Faktor **nach** Wahl von Zustand, Schnitt, η und
Identifikation. Er unterscheidet sich vom positiven F durch einen unitären
Faktor auf dem 16D-Hilbertraum.

Dabei bedeutet „Filter“ zunächst metrischer Faktor, nicht bereits zulässiger
normierter Quantenkanal/Krausoperator. Tatsächlich sind F und F_W ohne weitere
Skalierung keine Kontraktionen:
\[
 \det[(I-G_{\rm OS})|_{\{1,\gamma_4\gamma_5\}}]=-a^2<0.
\]
Ein zusätzlich normierter physischer Filter benötigt also einen eigenen
Operationsvertrag. Die Konjugation von Wortmultiplikation mit F verändert
deren gewöhnliches Adjungieren; eine Hilbertraum-Isometrie allein macht
daraus keine *-Darstellung sämtlicher ursprünglicher Compiler-Operationen.

Die Grenze einer bloßen *-Identifikation ist besonders einfach:
γ4 ist ein selbstadjungierter Unitär, aber
\[
 \|[\gamma_4]\|_{\rm OS}^2=a<1,
 \qquad\tau(U^\dagger U)=1\quad\text{für jeden Unitär }U.
\]
Kein unitaler *-Algebra-Basiswechsel macht daher den ungefilterten
Spur-Gram zum OS-Gram. **Das verbietet den Filteranschluss nicht.**
Auch ein bloßer Wechsel zu einer anderen normalisierten positiven
Funktionalform φ(A†B) auf demselben M4 würde diese Unitärnorm immer bei 1
lassen. Die relevante Änderung ist die Nahtpaarung, nicht allein die
Ersetzung des Spurzustands durch eine gewöhnliche Dichtematrix.
Insbesondere muss eine euklidische positive Zeiteinfügung nicht selbst
ein unitärer rekonstruierter Echtzeitoperator sein.

## Was liefert die vorhandene Zeittranslation wirklich?

Es wird keine neue Zeitregel gewählt. v524 verwendet den NS-signierten
Schritt α1 und nur jene Bereiche Dk, deren verschobene Träger in der
positiven Hälfte bleiben. Diese lokalen Bereiche sind nicht der gesamte
16D-Raum; ein kleiner echter Teilraum ist auch nicht dicht in diesem
endlichen Hilbertraum. Der finite Test allein ist somit kein Satz über
einen eindeutigen globalen selbstadjungierten Generator.

Die exakten Ergebnisse sind:

1. Die tatsächliche lokale Zweischritt-Translation ist **keine Kontraktion**:
   \(\|[\alpha_2\gamma_5]\|^2/\|[\gamma_5]\|^2
       =\|[\gamma_7]\|^2/\|[\gamma_5]\|^2=1+\sqrt2>1\).
2. Die Einschritt-Form hat bereits auf γ4−γ5 den Wert −2b<0.
   Sie ist also nicht der positive Operator exp(−H) eines
   selbstadjungierten H auf diesem ganzen lokalen Testbereich.
3. Die **quellenseitig definierte Zweischritt-Kompression** auf
   D2=span{1,γ4γ5,γ4,γ5} ist ein anderer, kleinerer Operator:
   α2 bedeutet genau zwei Vorwärtsschritte α1∘α1, also γ4→γ6,
   γ5→γ7. Sei P_D2 die orthogonale Projektion für den **OS-Gram**, nicht
   für den ungefilterten Spur-Gram. Dann ist
   \(R=P_{D_2}\alpha_2|_{D_2}=G_{D_2}^{-1}\tau_2\), wobei
   \((\tau_2)_{ab}=\omega(\Theta(e_a)\alpha_2(e_b))\).
   R ist bezüglich G_D2 selbstadjungiert,
   fixiert Ω und erfüllt exakt
   \((R-I)(R-(\sqrt2-1)I)=0\), mit beiden Eigenwerten zweifach.
   Daher ist R eine strikt positive Kontraktion auf diesem 4D-Teilraum.
   Dort ist −log R wohldefiniert und positiv; dies ist **nicht** der
   schon bestimmte volle 16D-Zeitgenerator und nicht automatisch ein
   physischer vierdimensionaler Träger.

Die Worte „lokale Translation“, „positive Kompression“ und
„rekonstruierte unitäre Echtzeitgruppe“ bezeichnen verschiedene Objekte.
Die Quelle benennt ihre Operationsverfeinerung selbst als bedingt.

## Genau ein noch fehlender Satz

**P1–Compiler-Zustands- und Zeit-Auswahlsatz:** Aus der ursprünglichen
operationalen P1-Naht, ohne nachträgliche Festlegung eines freien Zustands
oder einer Filtermetrik, folgt bis auf markierte unitäre Äquivalenz eine
positive Halbseitenrealisierung der Compiler-Wörter mitsamt Zustand ωΣ,
Reflexion ΘΣ und zulässiger positiver Zeitrichtung, so dass der aus ihren
Mehrzeitkorrelationen rekonstruierte Filter und Zeitoperator die
Compiler-Komposition respektieren; auf der vorliegenden freien N8-Spezialisierung
müssen sie den hier berechneten OS-Gram und die tatsächlichen lokalen
Zeiteinfügungen ergeben, nicht bloß eine beliebige positive Kompression.

Das ist eine **Auswahl- und Verträglichkeitsaussage**, nicht die Behauptung,
der OS-Gram müsse ungefiltert Tr/4 sein. Der finite Anschluss oben löst die
lineare Konstruktion, sobald die Nahtdaten gegeben sind. Er beweist diesen
einen Auswahl- und Verträglichkeitssatz nicht.

Warum RP und die feste Schnittsymmetrie allein nicht genügen, zeigt bereits
die kleine Zustandsfamilie
\(\omega_t=t\omega_{\rm NS}+(1-t)\tau_{\mathrm{Cl}_8}\), 0<t≤1.
Auf derselben Hälfte und bei derselben Reflexion ist
\(G_t=tG_{\rm OS}+(1-t)E_{00}>0\), aber die Norm von γ4 ist ta.
Die volle Clifford-Spur ist positiv, normalisiert und translationsinvariant;
ihre Nahtform ist E00, weil reflektierte und positive Träger disjunkt sind.
Diese Familie beansprucht **nicht** Reinheit, Quasifreiheit oder sämtliche
weiteren Seed-Clustering-/P1-Windungs-/Primitivitätsannahmen. Sie belegt genau, dass
Reflexionspositivität und die gleiche stationäre Schnittsymmetrie die
fehlende Zustandsauswahl nicht allein ersetzen.

## Reproduzierbarkeit und Grenzen

`checker.py` verwendet direkt die vorhandenen v524-Definitionen, führt
aber nicht dessen ganze Suite aus. `verification.json` enthält den SHA256
der Quelle, die exakten Crosscut-LDL-Pivots, den vollständigen Prüfbericht
und die Statusgrenzen. **322/322 Guards bestanden**, zuletzt auch unter
`python3 -O`; die eigenen Prüfschranken sind keine abschaltbaren asserts.
Positivität beruht auf exakter Algebra und
Wick-Exterior-Kongruenz, nicht auf numerischen Eigenwerten. Die negative
v572-Levi-/Radikalrechnung wurde nicht wiederholt.

Ausführung: `/opt/homebrew/bin/python3 checker.py` in diesem Verzeichnis.
Keine globalen Physik-, P1-, RH- oder TOE-Schlüsse.
