# Quellenladung, Flussindex und E₈

20. September 2026 · `UR.SOURCE.FLUX_INDEX.01` · **PARTIAL**

**Die vorhandene Randkonstruktion verbindet sich mit einem konkreten bekannten Entstehungsmechanismus für E₈.** Innerhalb ihres festgehaltenen Wörterbuchs wählen die ursprünglichen Ladungsmarkierungen die mögliche Eichladung aus. Ein elementarer Flusssektor dieser bedingt angenommenen Eichquelle trägt dann genau den bereits vorhandenen Rekonstruktionsvektor `n`. Der vollständige neutrale Gitterquotient ist E₈.

Damit wird die Struktur des benötigten Operators enger begründet. Seine tatsächliche Erzeugung durch die Originalquelle ist noch offen. Insbesondere bleiben die Wahl der zehn Kanäle, ihre bisherige E₈-Einbettung und die Einführung eines dynamischen Eichfeldes Voraussetzungen. Es wurde kein neues Gittermodell mit angepassten Kopplungen optimiert.

## 1. Was gegenüber dem bisherigen Ergebnis hinzukommt

Der vorherige Rotorvertrag bestimmte die mögliche Eichladung, indem er sowohl die Neutralität der gesamten E₈-Einbettung als auch die Neutralität des gewünschten Terms `n` verlangte. Die zweite Bedingung lässt sich nun durch die Erhaltung einer bereits vorhandenen Quellmarkierung ersetzen.

Für den gesamten noch möglichen Ladungsraum gilt exakt

\[
g(v,u)=(v a,u,-3v),\qquad
a=(1,1,1,-1,-1,-1,-1,-1).
\]

Die reinen und gemischten Anomaliebilanzen sind

\[
g^TKg=u^2-v^2,\qquad q^TKg=Y^TKg=u+v.
\]

Hier ist `q` die ursprüngliche globale Quellladung, `Y` die vorhandene Hyperladungsmarkierung und `K=diag(1,…,1,−1)`. Die Erhaltung von **q oder Y** erzwingt `u=−v`. Primitive ganzzahlige Normierung lässt dann nur

\[
\boxed{g=\pm Kn}
\]

übrig. Reine Eichanomaliefreiheit allein würde eine zweite Möglichkeit erlauben; sie verletzt beide ursprünglichen Markierungen. Die Neutralität von `n` folgt nun aus der Auswahl. Die bereits festgelegte Einbettung `F(E₈)` bleibt ausdrücklich eine Voraussetzung; dies ist keine unabhängige Entstehungsherleitung von E₈.

## 2. Warum der vorhandene Zwölffermionterm dazu passt

Nehmen wir eine kompakte U(1)-Verbindung mit ganzzahligem Fluss `ν` an, dann lautet der signierte Fermionindex

\[
I(\nu)=\nu Kg=\pm\nu n.
\]

Ein Einheitsfluss verlangt somit genau das bisherige Muster. Es enthält neun Fermionfaktoren aus den neun gleichgerichteten Kanälen und drei identische Faktoren aus dem Gegenkanal. Wegen ihrer Antisymmetrie benötigt die lokale Minimaldarstellung Ableitungsordnungen `0,1,2`:

\[
\boxed{12\text{ Fermionfaktoren},\quad3\text{ Ableitungen},
\quad(h,\bar h)_{\rm frei}=(9/2,9/2).}
\]

Bildlich: Die Ladungsregel bestimmt, welche Felder bei einer elementaren Flussänderung gemeinsam auftreten müssen. Sie sagt noch nicht, mit welcher Wahrscheinlichkeit eine solche Änderung stattfindet. Der Index ist eine Auswahlregel für einen Flusssektor. Er liefert weder einen nichtverschwindenden Cosinuskoeffizienten noch dessen Phase, ein Vakuum oder den benötigten Energieoperator. Mit freier Skalendimension neun ist dieser Operator am ursprünglichen freien Punkt auch nicht automatisch relevant.

Der bekannte Nullmodenmechanismus wird hier angewendet, nicht neu erfunden. Die Unterscheidung zwischen einer berechenbaren Flusskorrelation und einer daraus nicht automatisch folgenden lokalen Wechselwirkung ist bereits in [Narayanan und Neuberger, hep-lat/9609031](https://arxiv.org/abs/hep-lat/9609031) ausdrücklich wichtig.

## 3. Die vollständige neutrale Struktur ist E₈

Der Beweis betrifft das ganze ganzzahlige Gitter:

\[
\ker(g\cdot)=F(E_8)\oplus\mathbb Z n,
\qquad
\boxed{\ker(g\cdot)/\mathbb Z n\simeq E_8.}
\]

Eine zweite Darstellung macht die 240 Wurzeln einfach sichtbar. Nach einem dokumentierten Vorzeichenwechsel erfüllen neutrale Vektoren `(y,k)` die Beziehung `Σyᵢ=3k`. Die Projektion `y−(k/3)(1,…,1)` ergibt einen geraden, unimodularen Rang-acht-Überbau des A₈-Gitters. Seine Wurzeln bestehen aus

\[
72+84+84=240.
\]

Die 72 ersten Vertreter sind Differenzen zweier der neun Koordinaten. Die beiden 84er-Gruppen entstehen aus den möglichen Dreiergruppen: `binom(9,3)=84`. Jeder dieser Vertreter wurde in die vorhandene E₈-Basis zurückübersetzt, einschließlich des ganzzahligen `n`-Anteils.

Die Quotientenbildung ist zunächst algebraisch. Die physische Identifikation von Operatoren, die sich um `n` unterscheiden, verlangt weiterhin eine Zustands- und Korrelationsrechnung. Insbesondere besitzen die vierfaktorigen Vertreter im ursprünglichen freien Modell die Gewichte `(3/2,1/2)`; sie sind dort noch keine rein chiralen Ströme mit Gewicht eins.

## 4. Der genaue Anschluss an bekannte Physik

Die Ladungsbeträge sind neunmal eins und einmal drei bei entgegengesetzter Chiralität. Ihre Eichbilanz ist `9·1²−3²=0`, während die chirale Differenz acht beträgt. Chong Wang verwendet genau diese **9+1-Struktur** in einer E₈-Konstruktion: neun Fermion-Chern-Isolatoren, ein entgegengesetzt chiraler Ladung-drei-Verbund und anschließende U(1)-Eichung. Siehe [Phys. Rev. B 91, 245124 (2015), Abschnitt III](https://link.aps.org/accepted/10.1103/PhysRevB.91.245124).

Das liefert einen konkreten Vergleich für die hier ausgewählte Ladung. Die Literaturkonstruktion setzt jedoch einen 2+1-dimensionalen Bulk, passende Bandstrukturen und Eichdynamik voraus. Sie ist keine Ableitung dieser Voraussetzungen aus TFPT. Auch unser zweidimensionaler Indexbeweis ist nicht allein der Nachweis einer vollständigen physikalischen Gleichsetzung beider Modelle. Herkunft und Reichweite stehen in `LITERATURE.txt`.

## 5. Welche Herkunftsfrage tatsächlich übrig bleibt

Die Originalquelle muss eine **ladungs-, paritäts- und zeittreue Realisierung dieser Eichstruktur** liefern. Das Einheitswinding aus P1 ist nicht bereits die dazu nötige Operatorabbildung auf einen U(1)-Fluss. Gleiche ganze Zahlen reichen dafür nicht.

Der aktuelle benachbarte Vertrag `UR.SOURCE.OPERATOR_ORIGIN.01` zeigt außerdem: Die unveränderte native 64-CAR/60-CCR-Feldalgebra und die ungeraden lokalen Felder des gemeinsamen T-Randwörterbuchs haben unterschiedliche zentrale Gruppenwirkungen. Beliebig höhere Produkte im unveränderten Fockraum lösen diesen Unterschied nicht. Der vor der Familienkompression vorhandene Clifford-Übergang verschwindet nach der tatsächlich verwendeten geraden Kompression. Diese Ergebnisse werden hier als Herkunftsprüfung berücksichtigt, nicht als neu bewiesener Teil des Flussindexvertrags ausgegeben.

Gaugen geladene Hilfsfermionen nur einen bosonischen E₈-Observablensektor, ist eine lokale Eins-zu-eins-Abbildung jedes Hilfsfermions in die ursprüngliche physische Algebra auch nicht selbstverständlich erforderlich. Das wäre aber ein anderer, ausdrücklich zu konstruierender Operatorvertrag. Er dürfte die ursprünglichen physischen Fermionen nicht stillschweigend aus der vollständigen Theorie entfernen. Unsere neutrale Quotientenalgebra allein trägt diese Aufgabe nicht.

Der nächste entscheidende Test betrifft daher die ursprüngliche Feld-/Sektorenrealisierung und ihren gemeinsamen Zeitoperator. Erst wenn diese Abbildung vorliegt, ist die Berechnung einer nativen Flussamplitude und ihrer vollständigen Wirkung begründet. Die bestehende Quelle wird nicht durch ein nachträglich passend gewähltes Partonmodell ersetzt.

## 6. Prüfstatus und Reproduktion

Der vollständige Beweis in `PROOF.txt` wurde intern von einem zweiten Agenten geprüft. `REVIEW.txt` trennt diese Prüfung von ergänzenden bedingten Modellbetrachtungen. Der algebraische Checker kontrolliert 40 Identitäten beziehungsweise Kontrollgruppen, darunter alle 240 Wurzelvertreter. Normale und optimierte Python-Ausführung liefern dasselbe Zertifikat. Die allgemeinen Aussagen stehen im Beweis; die endlichen Kontrollen ersetzen sie nicht. Eine externe Begutachtung oder Formalisierung liegt nicht vor.

Aus dem Repository:

```sh
python3 -B experiments/theory-contracts/source-flux-index-20260920/checker.py --root . --output experiments/theory-contracts/source-flux-index-20260920/certificate.json
python3 -B -OO experiments/theory-contracts/source-flux-index-20260920/checker.py --root . --output experiments/theory-contracts/source-flux-index-20260920/certificate.optimized.json
```

Benötigt: Python 3 und SymPy. Quellpins werden vor den Kontrollen geprüft.

**Vertragsurteil: PARTIAL.** Bedingte Ladungsauswahl, Flussindex und ganzzahliger E₈-Quotient sind bestimmt. Native Eichquelle, Flussamplitude, Phase, gemeinsames Vakuum, vollständige IR-Stromalgebra und die physische 3+1-dimensionale Schließung sind offen. Kein T1–T8-Gate wird hier als geschlossen gewertet.
