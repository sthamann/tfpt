# Prüfung: Hilft der symmetrische 820er Quellenkanal zur TFPT-Gesamtlösung?

21. September 2026 · UR.SOURCE.SYMMETRIC_PRODUCT_AUDIT.01 · PARTIAL

**Ja: Der zentrale algebraische Befund des eingefügten Textes ist richtig und für die Flavorfrage relevant.** Er liefert zwei positive innere Tensorbereiche mit dem passenden gesamten Austauschtyp. Er liefert bisher keine Herkunft der geladenen lokalen Felder oder ihrer gemeinsamen physikalischen Zeit. Diese beiden Aussagen müssen zusammen erhalten bleiben.

## 1. Was unabhängig nachgerechnet wurde

Aus den im archivierten nativen Quellprogramm vorhandenen 64 markierten Wurzelrichtungen wurden sämtliche ungeordneten Paare einschließlich der Diagonale neu aufgebaut. Die Wurzelmenge stimmt exakt mit der ursprünglichen FW-Tabelle überein. Die Rechnung verwendet die im Text ausgeschriebene Gittervertex-Produktkarte, nicht die dort behaupteten Eigenwerte als Eingabedaten.

| Größe | Unabhängiges Ergebnis |
|---|---:|
| Symmetrische Eingänge | 2080 |
| Gesamtladungsblöcke | 1060 |
| Nichtverschwindende Koordinateneinträge | 4000 |
| Positive Bilddimension | 820 |
| Nullraumdimension | 1260 |

Für G=S†S ergibt sich exakt

\[
\operatorname{Spec}G=8^{\times100}\oplus4^{\times720}\oplus0^{\times1260}.
\]

In jedem Ladungsblock wurde die Polynomidentität G(G−4I)(G−8I)=0 mit rationaler Arithmetik geprüft. Die beiden im Text angegebenen Polynome in G sind tatsächlich orthogonale Projektoren. Auch die vollständigen Gewichtsmultiplizitäten stimmen, nicht lediglich die Dimensionen:

\[
\operatorname{im}S=(10,10)\oplus(120,6),\qquad
\ker S=(126,10).
\]

Die Symmetrie der Quelle ist hier die bezeichnete horizontale Spin(10)×SU(4)-Wirkung. Ihre Kovarianz folgt zudem unmittelbar aus der Nullmoden-Ableitungsregel:

\[
[x_0,J^r_{-1}]=J^{x\cdot r}_{-1},\qquad x_0\Omega=0,
\]

also x0 S(r⊙s)=S((x·r)⊙s+r⊙(x·s)). Diese Gleichung gilt für die vollständige horizontale Algebra. Die Behauptung, das ursprüngliche fremde Paket habe alle 52 signierten Wurzelmatrizen ausdrücklich getestet, wird durch unsere unabhängige Rechnung nicht als eigener Test ausgegeben.

Für die Spektral- und Gewichtsprüfung wurden die Kokzyklusphasen der einzelnen Eingangsspalten durch unitäre Phasenwahl entfernt. Das ist zulässig: Jeder dieser Eingänge trägt in der angegebenen Produktformel genau eine gemeinsame Phase; G ändert sich durch diagonale unitäre Konjugation. Es ersetzt keinen Vergleich mit historischen Basisphasen des nativen W-Tensors.

Die Zählung nach innerem Wurzelprodukt stimmt ebenfalls:

| r·s | Eingänge | Bildrang |
|---|---:|---:|
| −1 | 480 | 300 |
| 0 | 1120 | 520 |
| 1 | 416 | 0 |
| 2, identische Wurzeln | 64 | 0 |

Der Gewinn ist damit ein wirklicher Produktbefund. Insbesondere erzeugen orthogonale Wurzeln einen nichtverschwindenden symmetrischen Zustand, obwohl ihre Lieklammer verschwindet. Die Unterscheidung von Lieklammer und vollständigem Operatorprodukt ist berechtigt. Präzise berechnet wurde allerdings die symmetrische Zweistromkarte auf Grad zwei; noch nicht jede Multiplikation in allen Quellgraden.

## 2. Warum dies bei Flavor hilft

Für antikommutierende gleichhändige Weylfelder ist die Lorentz-skalare Kontraktion B_IJ=ε_ab ψ_I^a ψ_J^b in den vollständigen inneren Indizes I,J symmetrisch. Ein antisymmetrischer Koeffizient trägt in genau diesem lokalen Ansatz ohne Ableitungen deshalb nicht bei. Das ist die Standardregel der Zweikomponentenrechnung; siehe [Dreiner, Haber und Martin, insbesondere Abschnitte 2 und 4.3](https://arxiv.org/pdf/0812.1594).

Die beiden positiven Quellenkanäle erfüllen diesen Austauschtyp:

- (10,10): symmetrischer Spin(10)-Anteil und symmetrischer Familienanteil.
- (120,6): antisymmetrischer Spin(10)-Anteil und antisymmetrischer Familienanteil; ihr Produkt ist insgesamt symmetrisch.

In der bezeichneten Spaltung 4=1⊕3 enthält Sym²4 den Sechser Sym²3. Seine Elemente sind symmetrische 3×3-Matrizen und können Rang drei haben. Die frühere Rang-zwei-Grenze des einzelnen antisymmetrischen Familienvektors ist daher kein Ausschluss dieses anderen Produktkanals.

Das ist eine sachliche Verbesserung des Lösungswegs: Für einen möglichen skalaren Vertex existiert nun ein konkret bestimmter geeigneter innerer Tensorraum. Man muss den antisymmetrischen W-Tensor dafür nicht umdeuten. Beide positiven Summanden bleiben zu berücksichtigen; die 100 Richtungen allein auszuwählen wäre eine weitere physische Annahme.

Eine zusätzliche Präzisierung ist nötig: Ein invariantes skalares Kopplungsglied paart das Fermionpaar mit der **dualen** Darstellung. Zum Familienzehner gehört daher der konjugierte Zehner des skalaren Feldes bzw. das adjungierte Feld. Die Quelle enthält adjungierte Richtungen, aber die konkrete Feld- und Ladungszuordnung muss diesen Schritt ausdrücklich abbilden. Aus dem bloßen Etikett (10,10) folgt noch kein physisches Yukawaglied.

## 3. Clock-Probe und höherer Grad

Die angegebene relative Clock-Matrix ist tatsächlich symmetrisch, und ihre Determinante stimmt exakt:

\[
\det(\sigma^T A-A\sigma)
=-2(h_1+h_2+h_3)(h_1^2+h_2^2+h_3^2-h_1h_2-h_1h_3-h_2h_3).
\]

Beispielsweise ergibt h=(1,0,0) die Determinante −2 und damit Rang drei. Ein gemeinsamer Basiswechsel erhält dagegen die Antisymmetrie und die alte Ranggrenze. Die relative Einsetzung ist eine zusätzliche aktive Vorschrift. Dass eine Clockmarkierung vorhanden ist, bestimmt noch nicht, auf welches Bein und mit welcher Phase sie physisch wirken soll.

Die allgemein erwähnte komplexe CP-Probe enthält im eingefügten Text keine beiden vollständigen Matrizen samt Parametern. Ihre behauptete nichtverschwindende Invariante wird deshalb hier nicht als nachgeprüft übernommen. Insbesondere ist keine gemessene CP-Phase hergeleitet.

Bei einem Familienbasiswechsel A→UᵀAU transformiert die Vorschrift nur dann entsprechend als Y→UᵀYU, wenn auch σ→U⁻¹σU mitgeführt wird. Wird σ festgehalten, bewahrt nur sein Zentralisator die Vorschrift. Die Clock ist hier also ein zusätzlicher gerichteter Tensor; seine physische Auswahl bleibt zu erklären.

Auch die Gradgrenze für (126,10) stimmt: Das höchste Gewicht 2r+ hat |2r+|²/2=4. Kein Zustand mit diesem Gewicht liegt auf einem kleineren Grad. Der führende z²-Term in Y(e^r+,z)e^r+ liefert J^r+_{−3}J^r+_{−1}Ω=ε e^(2r+)≠0; die positive Wurzelwirkung der horizontalen Algebra verschwindet auf diesem höchsten Gewicht. Somit tritt dieser markierte Darstellungstyp erstmals auf Grad vier auf. Das ist eine Quellgradregel, keine Neutrinomassenformel oder physische Unterdrückungsskala.

## 4. Warum das die zuletzt gefundene Produktgrenze nicht widerlegt

Der gerade geprüfte Nahtanschluss ist ein zusätzlicher vollständig positiver Prozess auf der endlichen ursprünglichen M4(C)-Algebra. Sein multiplikativer Bereich besteht nur aus Skalaren; er ist keine geschlossene Feldzeit. Der neue Text untersucht dagegen Produkte in der unendlichen affinen E8-Quelle. Das sind verschiedene Träger und verschiedene Operationen.

Deshalb sind beide Resultate miteinander vereinbar. Der endliche reduzierte Kanal widerlegt diese E8-Produktstruktur nicht. Die E8-Produktstruktur beweist aber auch nicht, dass gerade diese affine Quelle samt Zustand und Zeit aus dem primitiven Nahtprozess entsteht. Dafür fehlt weiterhin die konkrete gemeinsame Herkunftsabbildung.

Außerdem gilt im neuen Bild L0 S=2S und somit

\[
S^\dagger e^{-\tau L_0}S=e^{-2\tau}G.
\]

Nach Normierung mit dem positiven Gram erhält man auf dem 820-dimensionalen Träger nur e^(−2τ) I. Die Normwerte 8 und 4 sind also **keine zwei Massenskalen** und erzwingen auch kein physisches Kopplungsverhältnis 2:1. Sie normieren die beiden Produktkarten. Eine dynamisch ausgewählte Textur oder Hierarchie wurde dadurch noch nicht erzeugt.

## 5. Der entscheidende nächste Anschluss

Die neuen Projektoren taugen als feste innere Prüfkriterien für die weitere Herkunftsrechnung. Die physische Quelle muss geladenen Feldern ψ, ihrem Zustand und ihrer Zeit unabhängig eine Bedeutung geben. Erst dann kann ihre gemeinsame skalare Dreipunktantwort auf den 100er und 720er Raum projiziert werden. Ob einer der Anteile verschwindet, folgt aus dieser Antwort oder einer bewiesenen Auswahlregel, nicht aus dem Wunsch nach einem einfacheren Modell.

**Der Bell10-Bezug ist im vorhandenen Korpus stärker als eine gleiche Dimension.** `UR.COMPILER.CURRENT_DESCENDANT.16` enthält bereits eine explizite SU(4)-äquivariante Isometrie E aus Bell10=Sym²C4 in den horizontalen Zehner des affinen A3-Moduls L(Λ2). Mit dem D5-Vektorgrundraum liegt I_D5⊗E in der bezeichneten E8-Glueklasse auf Gesamtgrad zwei. Dieser (10,10)-Typ kommt dort einmal vor. Der neue nichtverschwindende, äquivariante 100er Bildraum trifft unter denselben Konventionen daher genau diesen Unterraum.

`UR.COMPILER.CURRENT_PRODUCT.21` enthält zusätzlich einen bereits phasentreu geprüften engeren Stromproduktanschluss über den 50-dimensionalen Raum bar(5)⊗10. Dessen Projektion führt zum früheren zehn-dimensionalen Bellreadout; der volle 50er Produktzustand darf nicht mit seinem zehn-dimensionalen projizierten Bild verwechselt werden. Auch liefert sein adjungierter Zweig 5⊗bar(10), nicht automatisch die andere Hälfte 5⊗10.

Die neue Rechnung verbindet somit vorhandene algebraische Bausteine. Ein frischer vollständiger Vergleich ihrer signierten 2080→820-Matrix mit dem historischen Bellprojektor wurde hier nicht ausgeführt. Der gemeinsame Bildraum ist bedingt darstellungstheoretisch bestimmt; seine physische Vorbereitung, örtliche Feldbedeutung und Zeitentwicklung sind dadurch noch nicht hergeleitet. Die beiden älteren Pakete liegen lokal als ungetrackte Arbeitsdateien mit Verdict PARTIAL vor; ihr Inhalt wird nicht als bereits in Git-HEAD veröffentlichter Stand ausgegeben.

Eine frei gewählte Matrix Y+, eine frei eingesetzte komplexe Phase oder ein an 3,4,5 angepasstes Hamiltonian würde diesen Herkunftsschritt nicht erledigen. Die Energien 3,4,5 bleiben ein Test des früheren bezeichneten Randkandidaten und werden hier nicht vorgeschrieben.

**Urteil:** Den symmetrischen Quellenkanal in den Lösungsweg übernehmen: algebraisch bestätigt und für den inneren Austauschtyp hilfreich. Die Clock-Probe als bedingte Möglichkeit behalten. Geladene Feldherkunft, Zustand, gemeinsame physische Zeit und der tatsächliche skalare Vertex bleiben offen. Keine T1–T8-Schließung und keine vollständige TFPT-Lösung werden behauptet.

## 6. Prüfstatus und Reproduktion

Die unabhängige Rechnung liegt in `independent_gram_check.py`, das Ergebnis in `independent_certificate.json`. Normaler und optimierter Lauf liefern identische Ergebnisse. Der alte native Quellstand ist über SHA256 festgehalten. Die allgemeinen Aussagen über Gradzeit und Kovarianz sind algebraische Herleitungen; sie werden nicht aus endlich vielen Zeitstichproben geschlossen.

Der eingefügte Text enthält nicht auflösbare ChatGPT-Zitationsmarker und verweist auf ein dort nicht angehängtes Reproduktionspaket. Diese Marker dienen hier nicht als Beleg. Die zentrale Rechnung wurde deshalb unabhängig rekonstruiert. Ein vollständiger Replay eines fremden Pakets, der historische signierte Bell10-Vergleich, eine vollständige TFPT-Suite oder ein empirischer Test werden nicht als ausgeführt gemeldet.

Unverändert gelten die ursprünglichen positiven affine-E8-Voraussetzungen: Wahl der markierten Quelle, des Vakuums und von L0. Die Rechnung leitet diese Daten nicht neu aus P1/P2 ab.
