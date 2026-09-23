# Gleicher Quantenkanal, verschiedene Aufzeichnungen

14. September 2026. Neue kleine Anschlussprüfung; keine physische Auswahlbehauptung.

Die Identität zwischen vier zufälligen Quellreflexionen und einer unaufgezeichneten
Kontextmessung sowie ihr spezieller Dimensionsfaktor d=4 waren bereits in
[CONTEXT_INSTRUMENT.md](../compiler-origin-audit-20260913/CONTEXT_INSTRUMENT.md)
bewiesen. Diese Runde schreibt sie nicht als neue Entdeckung um. Der neue
Schritt führt sie mit dem tatsächlichen 3/7-Quantendecode zusammen und hält
die unterschiedlichen Aufzeichnungen ausdrücklich auseinander.

## Einfache, quellengenaue Identitäten

Für die 60 ursprünglichen Gaussian-Strahlen gelten

\[
R_r=I-2P_r,\quad \sum_r P_r=15I,\quad
\sum_r P_rXP_r=3(X+\operatorname{Tr}(X)I).
\]

Daraus folgt auf der gesamten Operatoralgebra, nicht nur auf einzelnen Zuständen,

\[
\frac1{60}\sum_rR_rXR_r^\dagger
=\frac1{15}\sum_rP_rXP_r
=\frac{X+\operatorname{Tr}(X)I}{5}.
\]

Beide Abbildungen sind vollständig positiv und spurtreu. Mische in beiden Fällen
den Identitätsschritt mit Gewicht 2/7 hinzu. In diesem festgelegten Mischansatz
ist das genau das Gewicht, das den vorhandenen Quantendecode reproduziert:

\[
\Phi(X)=\frac{3X+\operatorname{Tr}(X)I}{7}.
\]

## Zwei explizite Instrumente

Die Ergebnisse heißen leer beziehungsweise r für einen der 60 Strahlen.

\[
\begin{aligned}
\mathcal I_{\varnothing}(X)&=2X/7, &
\mathcal I_r(X)&=R_rXR_r^\dagger/84,\\
\mathcal J_{\varnothing}(X)&=2X/7, &
\mathcal J_r(X)&=P_rXP_r/21.
\end{aligned}
\]

Sie haben denselben nichtselektiven Kanal Phi für **jeden** Eingang. Unter
jedem ursprünglichen Reflexionsgenerator werden die 60 Strahlen permutiert;
beide Instrumente sind bezüglich derselben tatsächlichen Quellaktion kovariant.

Aus dem eindeutigen zyklischen Randzustand rho=I4/4 haben sogar alle ersten
Ergebnisetiketten dieselbe Verteilung: p(leer)=2/7 und p(r)=1/84. Dennoch gilt

| Nach aufgezeichnetem r | Reflexionsinstrument I | Projektorinstrument J |
|---|---|---|
| Bedingter Zustand | I4/4 | P_r |
| Rohgewicht zweimal desselben r | 1/7056 | 1/1764 |

J liefert also eine reine bedingte Quellpräparation; I tut das nicht. In J ist
das allgemeine Zweiergewicht Tr(P_s P_r)/1764, in I aus diesem Randzustand stets
1/7056. Es wird keine nachträgliche getrennte Renormierung von Geschichten benutzt.

Auch die kohärente Zuordnung ist explizit: Die Registermatrix
H=J60/30−I60 ist unitär, kommutiert mit allen Permutationen und erfüllt
sum_k H_rk R_k=2P_r. Mit dem unveränderten Leerzweig dreht sie die Krausliste
von I in jene von J. Gleichheit des verdeckten Kanals plus volle endliche
Symmetrie legt die Auslesebasis daher nicht fest.

Das Register H wird hier nicht als zusätzlich aus TFPT physisch hergeleiteter
60-dimensionaler Träger ausgegeben. Die Formel bezeichnet eine bedingte
kohärente Implementierung; der einzelne Vier-Kontext-Fall war bereits bekannt.

## Nicht mit dem ursprünglichen 60-Strahlen-Prozess gleichsetzen

Wenn der Leerzweig als Verbleib im bisherigen Strahl gelesen wird, hat das
neue J-Instrument einen anderen klassischen Strahlprozess als die ursprüngliche
Kontextfolge mit B/7:

| Gleicher ursprünglicher Eingangsstrahl | Ursprüngliche Kontextfolge | Neues J mit Leerzweig |
|---|---:|---:|
| Im selben Strahl bleiben | 1/7 | 1/3 |
| Erreichbare Strahlen in einem Schritt | 13 | 45 |

Die dekodierte Dichtematrix ist dennoch identisch. Matching des Quantendecodes
ist somit kein Matching der ganzen alten Ausführung oder ihrer Aufzeichnungen.

## Typisierung und Grenzen

Ein reiner linearer Intertwiner von einem fundamentalen C4 in zwei identisch
transformierende fundamentale C4-Faktoren ist bei voller Quellsymmetrie
unmöglich: Das zentrale iI verlangt iV=−V. Eine neutrale Umwelt C4⊗conjugate(C4)
vermeidet dies. Das ist kein Verbot gemischter Vierer-Umwelten oder anderer
neutraler Recorddarstellungen. Die minimale reine Umwelt des D3/7-Kanals
wird unabhängig im [Kollisionsbericht](collision/RESULTS.md) bestimmt.

Die ursprünglichen Projektoren, ihre Zusammensetzung und die Kanäle sind
exakt konstruiert. Zugang zu Instrumenten, Wahl der Auslesebasis, physische
Tensorfaktoren und das Stattfinden der Ereignisse bleiben Voraussetzungen.
Weder das Born-Gesetz noch T1–T8 werden aus diesen Identitäten abgeleitet.

## Reproduktion

record_selection.py: 4145 eigene und 1073 geerbte aktive exakte Prüfungen.
replay_record.py: normale und optimierte Ergebnisse byteidentisch; drei
absichtlich falsche Behauptungen wurden abgefangen. Die vielen Prüfbedingungen
sind Eintrags-/Quellprüfungen, keine Zahl unabhängiger physischer Entdeckungen.
Quelle und Loader sind hashgepinnt. Keine ursprünglichen Quellen geändert.
