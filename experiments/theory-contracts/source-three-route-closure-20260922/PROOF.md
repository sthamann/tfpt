# Gemeinsame Quelle: Auswahl, Stromantwort und Familienanschluss

22. September 2026 · `UR.SOURCE.THREE_ROUTE_CLOSURE.01` · **PARTIAL**

## Ergebnis in verständlicher Form

Alle drei vorgeschlagenen Wege wurden am ursprünglichen Quellenproblem bearbeitet. Die Wechselwirkung und die vorhandene Familienmischung lassen sich mathematisch sparsamer anschließen als über zusätzliche skalare Massenfelder oder eine neu erfundene gekrümmte Berry-Geometrie. Ihre Herkunft aus derselben ausgewählten TFPT-Quelle ist weiterhin nicht bewiesen.

Die Arbeit liefert drei konkrete Ergebnisse:

1. **Auswahl:** Der bisherige Eindeutigkeitsschluss enthält zwei getrennte offene Schritte: die Auswahl der vollständigen Zeitkorrelationen und deren identifizierender Anschluss an den Kragenoperator. Ein Standard-Rekonstruktionssatz schließt den zweiten Schritt nur unter einer zusätzlichen, bisher nicht bewiesenen Injektivitätsvoraussetzung. Eine vollständig zulässige zweite TFPT-Quelle wurde ebenfalls nicht konstruiert.
2. **Wechselwirkung:** Der benötigte Vierfermion-Koeffizient ist direkt eine gemischte verbundene Quellenantwort. Im deklarierten invarianten Austauschkanal gilt exakt \(g(\omega)=(C_-(\omega)-C_+(\omega))/2\). Dafür braucht es kein zusätzliches elementares Skalarfeld. Positivität allein wählt weder das Vorzeichen noch ein kontrolliertes lokales Regime.
3. **Familien:** Die vorhandenen exakten Monodromiematrizen erzeugen eine nichtabelsche Gruppe mit zwölf Elementen. Sie passen in den gemeinsamen Träger mit drei Familien und einer Singulettkomponente. Dieser globale Anschluss auf der punktierten Basis benötigt keine Quadratwurzel der Determinantenlinie. Eine rein skalare, global verklebte Quellenverbindung kann ihn nicht erzeugen.

Das schließt Prüfungen einzelner Anschlüsse. Es schließt weder die Ursprungsauswahl noch eine vollständige physikalische TFPT-Theorie.

## 1. Was beim ursprünglichen Auswahlbeweis fehlt

Der operationale Seed ist im Original

\[
\mathfrak S=(\mathfrak A_{\rm loc},\tau_t,\Theta,\omega,[u_\Sigma],D_{\rm coll}).
\]

Zeitentwicklung, Zustand und Kragenoperator sind hier separate Eingaben. Die vier Defekte wählen einen minimalen **Defektvektor**. Der Originalbeweis sagt ausdrücklich, dass Eindeutigkeit anschließend von der Klassifikation der minimalen Schicht abhängt. In der späteren Eindeutigkeitsbehauptung wird diese Klassifikation nicht durchgeführt. Die Master-Barriere \(0\) auf \(B\cong B_{\min}\), sonst \(+\infty\), setzt die gesuchte Klasse schon voraus.

Die nun präzise getrennte Kette lautet:

\[
\text{P1/P2 und Clocks}
\stackrel{\text{offen}}{\longrightarrow}
\text{vollständige markierte Schwingerdaten}
\longrightarrow T_s=e^{-sH}
\stackrel{\text{offen}}{\longrightarrow}D_{\rm coll}.
\]

**Bedingtes Resultat:** Stimmen sämtliche relevanten Schwingerdaten einschließlich Zeitverschiebungen überein, bestimmen sie bei erfüllten Rekonstruktionsvoraussetzungen dieselbe OS-Semigruppe. Deren selbstadjungierter Generator ist eindeutig. Wenn zusätzlich eine feste, unitär natürliche und injektive Beziehung \(H=F(D_{\rm coll})\) samt Domäne, reeller Struktur, Graduierung und Markierungen hergeleitet ist, folgt die Eindeutigkeit des Kragenoperators.

Dieser Standardschritt wählt die vorausgesetzten Schwingerdaten nicht aus. Ein Zweipunktkern allein ist für eine allgemeine nichtgaußsche Quelle auch keine vollständige Schwingerhierarchie. Die klassische Rekonstruktion verlangt geeignete vollständige Daten und Regularitätsbedingungen; siehe [Osterwalder–Schrader, 1975](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-42/issue-3/Axioms-for-Euclidean-Greens-functions-II-with-an-Appendix-by/cmp/1103899050.pdf). Hier wird nur der im Bericht ausdrücklich vorausgesetzte Semigruppenschritt benutzt, kein neuer 4D-Rekonstruktionsbeweis behauptet.

**Gegentest:** \(D_t=D_0+tV\) mit beschränktem symmetrischem Nullordnungsterm behält Domäne und Hauptsymbol. Die Erhaltung von Nullität, Clock-Struktur, markiertem Spektralfluss, Reflexionspositivität und relativer Wirkung folgt daraus nicht automatisch. Sie muss für ein konkretes \(V\) gezeigt werden. Erst dann wäre ein veränderliches dimensionsloses Verhältnis \(\lambda_k^+(|B_t|)/\lambda_1^+(|B_t|)\) ein echter Nachweis verbleibender Quellenfreiheit. Ein solches vollständig zulässiges \(V\) liegt hier nicht vor.

Damit ist weder Eindeutigkeit noch physische Mehrdeutigkeit bewiesen. Die Beweislücke ist präzise lokalisiert, ohne einen formalen Perturbationsansatz zum Gegenmodell hochzustufen. Details: [SELECTION.md](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/source-three-route-closure-20260922/SELECTION.md).

## 2. Stromkopplung aus derselben Quellenantwort

Die bereits exakt geprüfte Normalordnungsidentität übersetzt die Gross–Neveu-Kopplung in die bekannten Kanäle 45, 15 und 60. Neu ist das direkte Antwortkriterium. Bei tatsächlich hergeleiteten linearen Stromvertices ist der quadratische Anteil von minus dem logarithmischen Quellenfunktional

\[
-\frac12\int J_i(x)\,C_{ij}(x,y)\,J_j(y),
\qquad C_{ij}=\langle\mathcal T O_iO_j\rangle_c.
\]

Diese Koeffizientenidentität benötigt keine Gaußannahme. Nichtgaußsche Antworten führen allerdings zu weiteren Termen; vorhandene Kontakt- und direkte Vierfermionterme bleiben zusätzlich zu prüfen. Die Trennung zwischen Quelle und verbleibenden Strömen darf keine Freiheitsgrade doppelt zählen.

Unter der erklärten reellen Austausch- und Invariantenstruktur gilt

\[
\boxed{g(\omega)=-C_{RL}(\omega)=\tfrac12[C_-(\omega)-C_+(\omega)].}
\]

Für den untersuchten attraktiven GN-Weg muss die ungerade Antwort auf dem relevanten Frequenzband überwiegen. Zwei positive Kovarianzen mit gleichen ungeordneten Eigenwerten können entgegengesetzte Vorzeichen liefern. Selbst \(g(0)>0\) reicht nicht: Der exakte Zeuge

\[
C_-(\omega)=\frac1{\omega^2+1},\qquad
C_+(\omega)=\frac2{\omega^2+4}
\]

wechselt bei \(\omega^2=2\) das Vorzeichen von \(g\). Das zugehörige Zertifikat prüft die rationale Identität symbolisch; es ist kein TFPT-Quellenmodell.

Der bestehende \(W\)-Produktkanal \(\Lambda^2(16,4)\to(10,6)\) und der GN-Strom aus \((10,1)\otimes(1,6)\) haben verschiedene Eingangsobjekte. Ihre gleiche Ausgangsdarstellung erlaubt keine Gleichsetzung der Felder oder Propagatoren. Die vorhandenen Yukawa-Invarianten bleiben gültige Bausteine; ihre erneute Berechnung würde den fehlenden Antwortkern nicht liefern.

Für die Quelle fehlt damit ein konkret benanntes Objekt: \(C_{RL}(\omega)\), berechnet aus ihren tatsächlichen geladenen Operatoren und ihrem tatsächlichen Zustand. Ohne dieses Objekt rechtfertigt die exakte RG-Flussgleichung im Original keine eingesetzte GN-Kopplung. Details, Konventionen und Frequenzfehlergrenze: [CURRENT.md](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/source-three-route-closure-20260922/CURRENT.md).

## 3. Direkter Anschluss der vorhandenen flachen Familienverbindung

Für die exakten Vertreter \(M,U\) der vorhandenen v117-Rechnung setzen wir \(M_k=U^kMU^{-k}\). Die vier markierten Umläufe erfüllen

\[
M_0M_1M_2M_3=I,
\quad |\langle M_0,M_1,M_2,M_3\rangle|=12,
\quad \operatorname{tr}[M_0,M_1]=-1.
\]

Die Umlaufgruppe ist der vorhandene \(A_4\)-Typ; mit der Deckwirkung \(U\) erhält man die Gruppe mit 24 Elementen. Die Deckwirkung bleibt von gewöhnlicher Schleifenholonomie getrennt. Die Invariantenrechnung ergibt \(\dim\operatorname{End}(V)^{A_4}=1\): Der Dreiersektor ist irreduzibel. Eine Darstellung, die ausschließlich durch die primitive Windungszahl \(\mathbb Z\) faktorisiert, hat dagegen abelsches Bild und scheitert bereits am Kommutator.

Dies widerlegt nicht jede mögliche P1-Quelle. P1 kann mehr Daten als ihre Windungszahl tragen. Ausgeschlossen ist der Anschluss ausschließlich über diese skalare Zahl bzw. über eine global skalare Verbindung einschließlich ihrer Verklebung.

Mit dem ursprünglichen Rang-fünf-Träger \(E\), \(D=\det E\) und dem vorhandenen flachen Rang-drei-System \(L_F\) ist der gemeinsame Anschluss für ganzzahliges \(r\)

\[
\mathcal W=(\Lambda^{\rm even}E\otimes D^r\otimes L_F)
\oplus(\Lambda^{\rm even}E\otimes D^{-2-3r}).
\]

Er hat Rang 64. Wegen \(c_1(\Lambda^{\rm even}E)=8c_1(E)\) — jedes der fünf Chern-Wurzelsymbole erscheint in acht geraden Teilmengen — addieren sich die Chernbeiträge zu

\[
(24+48r)d+(-24-48r)d=0.
\]

Die Konstruktion verwendet nur ganzzahlige Potenzen von \(D\). Halbdeterminanten dienen höchstens der Beschreibung auf einer Überlagerung; eine globale Quadratwurzellinie wird nicht postuliert. Die gemeinsame Quotientenstruktur darf nicht in zwei unabhängig behauptete globale Spin- und Familienbündel zerlegt werden.

Dieser Anschluss gilt auf der punktierten Basis. Die parabolische Fortsetzung über die Punktierungen und die Operator-Domänen sind eigene Herkunftsbedingungen. Auch \(r\) und \(A_F\) werden durch diese Kompatibilitätsrechnung nicht ausgewählt.

Der nächste Vergleich ist nun eindeutig: Der tatsächliche Kragenoperator muss mit seiner **globalen** Verklebung vier Transporte \(H_k\) und eine Deckwirkung liefern. Eine gemeinsame unitäre Abbildung muss alle \(H_k\) zugleich in \(M_k\) und die Deckwirkung in \(U\) überführen. Einzelne passende Eigenwertlisten reichen nicht. Dass eine flache Verbindung lokal verschwindet, verbietet keine nichttriviale globale Holonomie.

Die endliche Algebra der gewählten Matrizen ist exakt; ihre Identifikation mit der ursprünglichen Differentialgleichung bleibt die getrennte numerische Prüfung der älteren Rechnung. Details: [FAMILY.md](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/source-three-route-closure-20260922/FAMILY.md).

## 4. Gemeinsamer Abschlussmaßstab

| Frage | Erreicht | Weiterhin nötig |
|---|---|---|
| Warum gerade diese Quelle? | Zwei offene Auswahl-/Identifikationsschritte präzisiert; zulässiger Gegenfamilientest formuliert | Vollständige Klassifikation oder hergeleitete Auswahl, einschließlich Zustand und Zeit |
| Erzeugt sie den GN-Kanal? | Exakter Quellenantwort-Koeffizient und kontrollierbares Frequenzkriterium | Native Operatoren/Vertices, Zustand und tatsächlicher Wert von \(C_{RL}\) |
| Liefert sie den Flavor-Anschluss? | Exakte nichtabelsche Umlaufprüfung und gemeinsamer Bündelanschluss | Ableitung derselben markierten Verbindung aus dem Quellenoperator |

Diese drei Ergebnisse müssen aus **einem** gemeinsamen Prozess stammen. Drei unabhängig angepasste Modelle wären kein Abschluss. Die Energien 3, 4 und 5 bleiben ein Test des entsprechenden früheren Kandidaten, keine hier auferlegte universelle Bedingung.

Ein genetischer Algorithmus wurde nicht eingesetzt: Es gibt in dieser Arbeit noch keine aus dem ursprünglichen vollständigen Kragenproblem hergeleitete Kandidatenklasse, deren Suche die Auswahlfrage entscheiden könnte. Der nächste entscheidende Rechenschritt betrifft den tatsächlichen zulässigen Operatorraum und seine Quellenantwort. Sobald dieser Raum begründet ist, können numerische oder evolutionäre Verfahren Gegenkandidaten suchen; einen globalen Auswahlbeweis ersetzen sie nicht.

Die vorhandenen Träger-, E8-, Ladungs-, Yukawa-, Flavor- und Clock-Ergebnisse werden durch diese Herkunftsprüfung nicht pauschal verworfen. Sie werden ebenso wenig als Beweis einer gemeinsamen vollständigen Dynamik benutzt. Der Gesamtstatus bleibt **PARTIAL**, ohne Promotion in Ledger oder Physikabschluss.

## 5. Nachweise und Validierung

Die Originalstellen und verwendeten früheren Ergebnisse sind in `source_pins.json` mit SHA-256 festgehalten. Relevant sind insbesondere ursprünglicher Seed und Defektbeweis in `01_boundary_kernel_source.tex:480–682`, Master-Barriere in `02_carrier_source.tex:3021–3062`, separate Dynamikannahme in `04_qft_source.tex:1770–1790`, bedingte OS-Rekonstruktion dort ab Zeile 2748, und das vorhandene Quellenfunktional dort ab Zeile 2164.

Die neue symbolische Stromprüfung und die exakte Familienprüfung laufen mit Normal- und optimiertem Python; verglichen werden vollständige Zertifikate. Die mathematische Auswahlprüfung ist ein Argument am Originaltext, kein numerischer Beweis. Interne Agentenprüfung ist keine externe Begutachtung. `validation.json` dokumentiert den begrenzten Prüfungsumfang. Der Theoriegraph wird nach Abschluss der Artefakte neu gebaut und auf Aktualität geprüft; bekannte ältere Graphwarnungen bleiben davon getrennt.
