# E₈ und geladene Felder: welche gemeinsame Beschreibung ist möglich?

20. September 2026 · `UR.SOURCE.CHARGED_LIFT.01` · **PARTIAL**

**Der neutrale E₈-Quotient und die zuletzt gefundenen geladenen Spinorfelder lassen sich unter der festgehaltenen gemeinsamen Gruppenwirkung nicht einfach als dieselbe lokale Feldtheorie zusammensetzen.** Das ist jetzt für alle integralen additiven Vertreter des Quotienten bestimmt. Eine konkrete algebraische Erweiterung ist möglich; sie ändert aber, welche Felder lokal sind.

Es wurde kein Hamiltonterm ergänzt und keine Kopplung eingestellt. Die Untersuchung entscheidet eine notwendige Strukturfrage, bevor ein weiterer Dynamikansatz gebaut wird.

## Der neue Ausgangspunkt aus der anderen Lane

Der inzwischen vorliegende Vertrag `UR.SOURCE.CLIFFORD_GRADE.01` entscheidet bereits die einfache Fortsetzung über zusätzliche Clifford-Majoranas. Bei gleicher Gruppenwirkung haben ihre Produkte mit den nativen Fermionen die falsche Statistik. Dies wird hier nicht erneut als eigenes Ergebnis ausgegeben.

Derselbe Vertrag liefert einen positiven bedingten Anschluss: Das bereits vorhandene Randfeld `e9` erzeugt unter zusammengesetzten D₈-Strömen den gewünschten geladenen Spinororbit. Die besondere gemeinsame Energievorschrift `Vc` und ihre Herkunft bleiben dabei vorausgesetzt. Der vorherige Flussindexvertrag hatte seinerseits den vollständigen neutralen E₈-Quotienten bestimmt. Jetzt wurde geprüft, ob beide Aussagen dieselbe Wirkung auf geladene Felder zulassen.

## 1. Alle möglichen integralen Vertreter sind klassifiziert

Ein neutraler Quotientenvektor `r` besitzt mehrere Vertreter, die sich um den Nullvektor `n` unterscheiden können. Jede additive ganzzahlige Wahl hat genau die Form

\[
S_\lambda(r)=F(r)+(\lambda\cdot r)n,
\qquad \lambda\in E_8.
\]

Das folgt aus der Selbstdualität des ganzen E₈-Gitters. Es ist eine vollständige Klassifikation ohne endlichen Suchradius.

Die gewünschte gemeinsame D₈-Wirkung `T` würde

\[
\lambda=\frac a2,
\qquad a=(1,1,1,-1,-1,-1,-1,-1)
\]

verlangen. Aber `a/2` liegt gerade im anderen Spinor-Coset und gehört nicht zu E₈. Daher existiert kein solcher vollständiger integraler E₈-Vertreter, der die exakten bisherigen Cartangewichte beziehungsweise OPE-Paarungen beibehält. Gleiche Vorzeichen nach einem ganzen Umlauf allein wären eine schwächere Bedingung und reichen hier nicht.

Für den ursprünglichen lokalen Feldraum funktioniert `T` genau auf D₈: **112 Wurzelströme sind integral; die übrigen 128 benötigen einen halbzahlig ergänzten Sektor.** Das ist keine Aussage, dass E₈ keine Fermionen zulässt. Es entscheidet diese konkrete lokale Einbettung mit der festgehaltenen Gruppen- und Feldzuordnung.

## 2. Warum der neutrale Quotient die Lücke nicht sehen konnte

Die zusätzliche Richtung `n` verschwindet im neutralen Quotienten. Ein geladenes Feld reagiert weiterhin darauf. Für jeden der fehlenden 128 Ströme ist seine volle Umlaufphase mit einem ursprünglichen Feld `x`

\[
\exp\bigl(2\pi i B(T(r),x)\bigr)=(-1)^{g\cdot x}.
\]

Bei jedem ursprünglichen ungeraden Feld ergibt sich ein Minuszeichen. Dieses ist die zusätzliche Monodromie mit dem bosonischen Strom; es lässt sich nicht durch die üblichen fermionischen Austauschzeichen entfernen.

Bildlich: Zwei reduzierte Beschreibungen können dieselben neutralen Zustände zeigen. Sobald ein geladenes Feld hinzukommt, unterscheiden sich ihre tatsächlichen Transformationsregeln. Die beim Reduzieren verschwundene Information wird dann wieder benötigt.

Auch die ursprünglichen globalen Markierungen `q` und `Y` wählen den Vertreter nicht allein aus. Eine ausdrücklich geprüfte Familie ganzzahliger Gitterisometrien erhält beide. Werden alle Operatoren, Zustände und Energien mitübersetzt, ist das lediglich ein Koordinatenwechsel. Offen ist deren Abbildung auf die festgehaltenen ursprünglichen Quellfelder und ihre Zeit.

## 3. Die kleinste lokale Erweiterung ist explizit bekannt

Setze `h=n/2`. Genau die ursprünglichen Felder mit gerader Kandidaten-Eichladung sind mit diesem Zusatz ganzzahlig lokal. Dieser Teilraum heißt `Γ₀`. Dann ergibt sich

\[
\boxed{
L_h=\Gamma_0+\mathbb Z h
=T(E_8)\oplus U,
\qquad U=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
}
\]

Das ist ein gerades, unimodulares Gitter der Signatur `(9,1)`. Seine vollständige Basis und beide Gittereinschlüsse sind geprüft. Die Erweiterung ist minimal **unter der Voraussetzung, dass der ganze gerade Originalsektor erhalten bleibt und genau T(E₈) aufgenommen werden soll**.

Hier sind alle 240 gewünschten E₈-Wurzelströme lokal. Die ursprünglichen ungeraden Fermionfelder sind es nicht mehr. Insbesondere ist `e9` kein lokales Feld von `L_h`. Ihre mögliche Beschreibung als verdrillte Felder oder Endpunkte von Linien verlangt eine zusätzliche, ausdrücklich zu konstruierende Sektoren- und Korrelationsbeschreibung.

Die genaue Entscheidung lässt sich so zusammenfassen:

| Beibehaltene Beschreibung | Was sie trägt | Was nicht automatisch mitkommt |
|---|---|---|
| Ursprünglicher Feldraum Γ mit F(E₈) | Integrales E₈ und ursprüngliche Fermionfelder | Die gewünschte gemeinsame Spinorwirkung; e9 ist hier E₈-Singulett |
| Γ mit gemeinsamer T(D₈)-Wirkung | Der bisherige geladene Spinororbit bei vorausgesetztem Vc | Die fehlenden 128 lokalen T(E₈)-Ströme |
| Neuer gerader Feldraum L_h mit T(E₈) | Vollständige lokale T(E₈)-Struktur | Die ursprünglichen ungeraden Felder als lokale Operatoren |

Es gibt insgesamt zwei gerade Nachbargitter von Γ. Die Forderung nach dem bestimmten T(E₈)-Stromsystem wählt eines davon. Ihre physikalische Auswahl folgt damit noch nicht aus der Quelle.

Außerdem trägt `g` auf `L_h` nur noch gerade Ladungswerte; dort wäre `g/2` primitiv. Man darf diesen Wechsel nicht zugleich als Erhaltung der alten lokalen Ladung-eins-Felder darstellen. `n/2` ist auch nicht schon ein hergeleitetes halbes Flussereignis: Der vorherige Flussindex verwendete andere, ausdrücklich festgelegte Bündel- und Ladungsvoraussetzungen.

## 4. Bedeutung für die Gesamtlösung

Die notwendige gemeinsame Struktur umfasst **lokale neutrale Observablen und die geladenen beziehungsweise verdrillten Feldsektoren samt ihrer Zeitentwicklung**. Ein neutraler E₈-Abschluss allein legt diese vollständige Struktur nicht fest.

Der bekannte Zusammenhang von Fermionisierung, Paritätsprojektion und verdrillten Sektoren bietet dafür einen passenden mathematischen Rahmen; beispielsweise [Burbano, Kulp und Neuser, Abschnitte 3.5.2–3.5.3](https://arxiv.org/pdf/2112.14323). Dieser Rahmen ist keine neue TFPT-Entdeckung. Seine konkrete Realisierung aus der ursprünglichen endlichen Quelle und den vorhandenen Clock-Operatoren ist weiterhin offen.

Der nächste Herkunftstest muss zeigen, welche dieser lokalen Algebra- und Sektorregeln die ursprüngliche Quelle tatsächlich erzeugt und wie die geladenen Korrelationen zeitlich mitgeführt werden. Weder E₈ als physische Eichgruppe noch eine bestimmte (3+1)-dimensionale Teilchentheorie wird aus dem heutigen Gitterresultat abgeleitet. Das gesamte Compiler-, Flavor-, Clock- und Gravitationsziel bleibt erhalten; die vorliegende Rechnung entscheidet einen Anschluss des aktuell untersuchten Randwegs.

## Prüfung und Dateien

- `PROOF.txt`: vollständige allgemeine Argumente, einschließlich aller Schnitte und beider Nachbargitter.
- `checker.py`, `certificate.json`, `certificate.optimized.json`: 33 exakte algebraische Kontrollen; normale und optimierte Ausführung stimmen byteweise überein.
- `REVIEW.txt`: interner unabhängiger mathematischer Audit mit genauer Reichweite.
- `PRIOR_COVERAGE.txt`: Abgrenzung zu den bereits vorhandenen Einzelbeispielen und Feldrechnungen.
- `source_manifest.json`: Quell- und Ergebnispins.

Die allgemeinen Sätze folgen aus den ausgeschriebenen Beweisen, nicht aus einer endlichen Stichprobe. Keine externe Begutachtung, keine Formalisierung in einem Beweisassistenten und keine empirische Evidenz werden behauptet.

Reproduktion aus dem Repository:

```sh
python3 -B experiments/theory-contracts/source-charged-lift-20260920/checker.py --root . --output experiments/theory-contracts/source-charged-lift-20260920/certificate.json
python3 -B -OO experiments/theory-contracts/source-charged-lift-20260920/checker.py --root . --output experiments/theory-contracts/source-charged-lift-20260920/certificate.optimized.json
```

**Verdikt: PARTIAL.** Die bedingte Strukturfrage ist entschieden; native Sektorerzeugung, Dynamik, Vakuum und die vollständige physische TFPT-Schließung sind nicht hergeleitet. Keine Paper-, Ledger-, Scorecard- oder T1–T8-Promotion.
