# Unabhängiger Review der ersten Wilson-Cap-Erweiterung

10. September 2026. Reviewer: unabhängiger Teilagent `prime_chaos_atlas`.

**Befund: PASS_SCOPED_MATHEMATICAL_REVIEW. Keine konkrete mathematische Beanstandung am geprüften Endstand.** Die Erweiterung berechnet echte zusätzliche Richtungen des bezeichneten Parents. Ihr endlicher Block ist ausdrücklich keine abgeschlossene Gesamtdynamik.

Geprüfte Endstände:

| Datei | SHA-256 |
|---|---|
| `tfpt/ERWEITERUNG.md` | `21a481d07c195d2cd3260018d492515254d248a8c8205723cd638b8090de467a` |
| `tfpt/check_extension.py` | `d326e33bea37f1b8d9cffc3def52118839ee739959cdb407411572115f2a1c33` |
| `tfpt/erweiterung-quellenmanifest.json` | `f8ac0dcaa5240386517d72052500f64251deae698ee222b504d6dd95a9dda926` |

## Umfang und unabhängige Kontrollen

`ERWEITERUNG.md`, `check_extension.py`, das Quellenmanifest und der vollständige vorgelagerte `WILSON-CAP-BEWEIS.md` wurden gelesen. Der zugrunde liegende native Hamiltonoperator war im vorausgehenden Review bereits unmittelbar mit `observable-dynamics/README.md` und `ground-state-loop-response/README.md` abgeglichen worden. Hier wurde keine neue native Kampagne gestartet und kein fremdes Artefakt verändert.

Alle **12** referenzierten Datei-/Größen-/Hashpins des Erweiterungsmanifests stimmen mit den vorhandenen Dateien überein. Der neue Checker wurde nochmals ausgeführt, wobei sein einziger Dateischreibversuch ausschließlich im Arbeitsspeicher aufgefangen wurde. Alle **11** Kontrollen bestehen; das dabei berechnete JSON stimmt inhaltlich exakt mit dem gespeicherten Ergebnis überein. Anschließende Hashprüfung bestätigt unveränderte Eingaben und Ergebnisse.

Zusätzlich wurde eine unabhängige, exakt rationale 7×7-Blockmatrix mit nichtkommutierenden 2×2-Blöcken h₀,h₁, einem 3×2-Restblock R und nichtdiagonalem H_R eingesetzt. Sie bestätigt die Momente H⁰ bis H³, den H⁴-Rest und die vollständige verschachtelte Resolventenformel bei z=i. Der allgemeine Beweis steht im Folgenden; die endliche Probe ersetzt ihn nicht.

## 1. Ausgangsisometrie und h₁

Die ursprünglichen gerichteten LH-Ausgänge besitzen je geordnetem Nachbarpaar verschiedene Fockmuster. Deshalb ist Γ*Γ=6Nb²I und η=Γ/g tatsächlich isometrisch. Die Zustände haben genau ein High-Teilchen und liegen orthogonal zur All-Low-Quelle. Daraus folgen die beiden Kopplungsblöcke gI ohne zusätzliche Konvention.

Die CAR-Lochidentität ist richtig: Für H_LL=l*h_Ll und die gefüllte Quelle wirkt der Kommutator auf l_y als −Σ_z(h_L)_{yz}l_z. Weil die Rotor-Koeffizienten miteinander kommutieren, folgt die verwendete Form

    H_LL T J = T Tr(h_L) J − d* Q h_L l J.

Nach Rückkompression mit T* ergibt sich −[a Tr Q³+c Tr Q⁴]/(6N). Die Dreiwegspur verschwindet auf dem angegebenen Torus. Die Vierwegzählung liefert exakt 66N triviale Rückwege und vier Beiträge je orientierter Plaquette. Bei den zwei disjunkten gespeicherten Loops bleiben genau 4K übrig; der offene Randshift und seine Nullwirkung am Rest 3 werden korrekt beibehalten.

Für den elektrischen Anteil sind die Fockmuster der gerichteten Hops orthogonal. Die beiden Richtungen jedes Links heben ihre linearen Fluxinkremente in der Summe auf. Der verbleibende quadratische Zuschlag ist κ/2; die ursprüngliche Codeenergie E_C bleibt erhalten. LH-Terme ändern die High-Zahl und können in h₁ keinen Beitrag liefern.

Damit bestätigt die unabhängige Rechnung

    h₁ = h₀ + (4 + κ/2 − 11c)I − (2c/3N)K.

Mit N=125 und den originalen Koeffizienten erhält man genau

    h₁−h₀ = (57397/14400)I − K/108000.

Der Checker prüft die vollständige Vierwegspur unabhängig durch Wegzählung. Seine abschließende h₁-Kontrolle setzt allerdings die oben hergeleitete CAR-/Energieformel ein; sie ist keine zweite komplette Berechnung aller Hη-Feldamplituden. Der allgemeine Quellenbeweis und die hier nachgerechnete Loch-/Energiebilanz bleiben daher wesentlich.

## 2. Onsite-Kanal mit richtigem Vorzeichen

Z₀ hat ein High-Teilchen und ein Low-Loch am selben Ort. Diese Muster sind sowohl zur All-Low-Quelle als auch zu den benachbarten One-Pair-Mustern in η orthogonal. Verschiedene Orte liefern orthogonale Ausgangsmuster; unveränderter Flux macht die Abbildung isometrisch und Gauss-neutral.

Die Rückkehr eines Low-Lochs über einen ursprünglichen nächsten Nachbarlink trägt das Minuszeichen der CAR-Lochbewegung. Sechs solche Rückwege pro Ort ergeben

    Z₀*Hη = −6ab√N/g I = −a√6 I = −1/√24 I.

Das Vorzeichen ist also negativ, nicht nur das vom Checker kontrollierte Betragsquadrat 1/24. Seine zusätzliche direkte CAR-Probe prüft dieses Minuszeichen unabhängig. Die übrigen ursprünglichen Termarten können aufgrund ihrer High-Zahl oder mangels geschlossener Dreiwegschleife keinen kompensierenden Eintrag erzeugen.

## 3. Zwei-Paar-Gram und orthogonale Fortsetzung

T² auf der gefüllten Low-Quelle erzeugt Zweierminoren von Q mit Faktor zwei durch die beiden zeitlichen Reihenfolgen der geraden, disjunkten LH-Monomiale. Das Normquadrat ist daher viermal die Summe der quadrierten Minoren. Für die kommutierenden Rotor-Koeffizienten ist diese Summe das zweite elementarsymmetrische Polynom von Q*Q=Q²:

    T*²T² = 2[(Tr Q²)² − Tr Q⁴]

als auf die All-Low-Quelle zurückkomprimierte Identität. Das ist genau der im Bericht angegebene Faktor; weder Faktor zwei noch ein Fermionenminus fehlen.

Mit R₂=(b²/g)T²J erhält man folglich

    G₂ = b²[(12N−22)I − (4/3N)K].

Bei N=125 lautet dies exakt

    G₂ = (739/288)I − K/54000.

Die Normschranke ||K||≤4 reicht für strikte Positivität bei allen zugelassenen N≥125 aus. Somit existiert die eindeutige positive inverse Quadratwurzel, und η₂=R₂G₂^−1/2 ist isometrisch. Weil η₂ zwei High-Teilchen trägt, liegt es orthogonal zu J, η und Z₀. Die 64-dimensionale zusammengesetzte Isometrie ist korrekt; sie wird nicht als invariant ausgegeben.

## 4. Momente H⁰ bis H³ und der erste fehlende Beitrag

Schreibe P=V₁V₁*, Q_R=I−P. Aus HJ=Jh₀+ηg folgt Q_R HJ=0. Für die dritten Momente genügt deshalb bereits

    J*H³J = (HJ)* H(HJ) = (HJ)* P H P(HJ).

Das beweist zusammen mit den niedrigeren Potenzen die behauptete Gleichheit bis H³. Für die vierte Potenz benutzt man dagegen die Norm von H²J. Sein Restanteil ist

    Q_R H²J = Q_R Hη g = Rg.

Die orthogonale Zerlegung liefert exakt

    J*H⁴J − E₀*Ĥ₁⁴E₀ = g²R*R.

Die Projektionen auf ran Z₀ und den gesamten Zwei-High-Sektor sind orthogonal und liegen im Rest. Daher ist R*R≥(1/24)I+G₂ korrekt. Die Differenz ist strikt positiv; der erste Block erhält tatsächlich nicht die vierte Antwort.

## 5. Domains und Feshbach-Formel

J, η und alle angegebenen endlichen Blöcke haben ihre Bilder im gemeinsamen endlichen Flux-/Fock-Kern. Dieser Kern wird durch H erhalten. Daher existieren sämtliche hier verwendeten Momente, und es gibt keine unbemerkte H⁴-Domainannahme.

Die Selbstadjungiertheit der Restkompression folgt hier aus einem konkreten endlichrangigen Argument: P hat endlichen Rang und ran P⊂Dom H. Deshalb ist HP beschränkt und Q_RHP hat einen beschränkten Adjungierten. Der Offdiagonaloperator

    B = Q_R H P + (Q_R H P)*

ist beschränkt und selbstadjungiert. H−B ist auf Dom H selbstadjungiert und blockdiagonal bezüglich P,Q_R. Seine Einschränkung auf ran Q_R ist genau H_R mit Domain Dom H∩ran Q_R und somit selbstadjungiert. Die bloße Kompression eines beliebigen unbeschränkten Operators wäre ohne diese Voraussetzungen nicht ausreichend; sie sind hier erfüllt.

In den drei orthogonalen Blöcken J,η,Q_R hat z−H die Kopplungen −gI und −R. Zweimalige Schur-Elimination ergibt genau die berichtete Formel, mit **Minuszeichen** vor R*(z−H_R)^−1R und dem Faktor g² vor dem zweiten inversen Block. Für Im z≠0 sind die Restresolvente und die beiden Schurkomplemente invertierbar; im oberen Halbplan hat das erste Schurkomplement strikt positive Imaginärteilform.

Die Formel ist damit eine exakte Darstellung der ursprünglichen Antwort. Sie ist keine geschlossene oder effizient auswertbare Lösung für die Restdynamik.

## Schlussfolgerung und offene Reichweite

Es ist kein Korrekturbedarf an den geprüften Koeffizienten, Vorzeichen, Momenten oder Domains erkennbar. Die Konstruktion liefert konkrete, durch den ursprünglichen Parent erzwungene zusätzliche physische Richtungen und quantifiziert den nächsten verlorenen Beitrag. Sie beweist weder einen endlichen Gesamtablauf noch die Auswahl von Parent, Präparation oder Zustand aus dem TFPT-Compiler. RH, Faktorisierung und P versus NP bleiben außerhalb ihrer bewiesenen Reichweite.
