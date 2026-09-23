# Nachtrag C: überwiegend bereits abgedeckte fundamentale Reduktion

## Übernahmeurteil

Der neue Text ist eine ausführlichere Fassung der bereits eingefrorenen
fundamentalen Reduktion, ergänzt um die weitgehend gleiche frühere
Gesprächszusammenfassung. Er bringt **keinen neuen H-Term, keine neue
Operationsquelle und keinen neuen Transferbeweis**. Seine wesentlichen
mathematischen Einschränkungen sind richtig und bleiben in der gemeinsamen
Darstellung erhalten. Eine neue Großrechnung ist dafür nicht notwendig.

Neue Eingabe: 299 Zeilen,
SHA-256 `a10f702306c7409535df9f4d26f0995970833a62297a1cb93d8c95cdce746d4d`.
Quelle: `/Users/stefanhamann/.codex/attachments/b0d7e533-3ca8-4a84-966c-2546b066dd08/pasted-text.txt`.

Bereits eingefrorene Kurzfassung:
`universalraum-singlet-observable-20260915/late_sources/fundamental_reduction.txt`,
99 Zeilen, SHA-256
`0081cebd9759e8fa776995ee8efb3231c7611a82bea9cdeea86967073d1459a2`.
Die Dateien sind nicht bytegleich; der Neuheitsbefund betrifft ihren Inhalt.

## Was bestätigt und bereits abgedeckt ist

| Aussage | Urteil und Grenze |
|---|---|
| Volle Schur-Antwort T†F(H−E0)T=γF I64 | Richtig bei gruppeninvariantem H und Grundzustand sowie irreduziblem ursprünglichem Entnahmemultiplett. Gilt für die volle beschränkte Spektralfunktion, nicht nur einen dominanten Pol. Schon in v1.6.7 BIG_PICTURE B2 und der eingefrorenen Kurzfassung enthalten. |
| Aus C_rs(t)=δ_rs c(t) folgt kein Ortsindex in diesen 64 Labels | Richtig. Eine andere lineare Benennung erzeugt nur einen Gramfaktor. Keine pauschale Sperre gegen Vielteilchendynamik, nichtinvariante Referenzzustände oder andere Operatorfamilien. |
| Symmetriekommutant und Operationskommutant haben verschiedene Bedeutung | Richtig und bereits unterschieden. Erstgenannter erlaubt Dynamik zwischen Vorkommen desselben Typs; ein großer Kommutant eines eingeschränkten Operationssatzes kann fehlenden Zugriff anzeigen. Seine Größe beweist weder Raum noch ausführbare Kontrolle. |
| μN ist bei festem Gesamt-N eine Konstante | Richtig. Auf demselben präparierten Eingang bleiben freie Heisenbergentwicklungen neutraler Observablen identisch. Für ganze Interventionsfolgen muss auch deren zugelassener Gesamtvertrag respektiert werden. |
| Eine globale Zustandsregel braucht keinen äußeren Präparator | Richtig. Das Verbot, mit N-erhaltenden Operationen aus N=0 nach N=64 zu gelangen, ist ein Satz über einen bestimmten Präparationsweg. Es verbietet weder eine globale Randbedingung noch eine andere begründete Zustandsregel. Interne Detektoren und Präparationen bleiben trotzdem herzuleiten. |
| Keine nichttriviale Fermion-Teilparität in einer nativen Bank bei festen Bosonen | Bereits exakt geprüft: zusammenhängender W-Paargraph und binärer Rang 63. Ein Paritätsverbot getrennt kopierter Banken darf nicht auf beliebige Teilmengen derselben Bank übertragen werden. |

Das eigene v1.6.8-Ergebnis ergänzt diese Diagnose: Der bedingte lokale
Phasenimpuls und die terminale Tomografie benutzen einen gemeinsamen
invarianten N=2-Dreizustandsraum. Dessen Startzustand ist nicht der in
Schurs Aussage vorausgesetzte invariante N=64-Grundzustand. Es gibt daher
keinen Widerspruch und keine Berechtigung, die neue Umverteilung auf dessen
geladenen Einlochpol oder auf räumliche Bewegung zu übertragen.

## μ=Δ/50: gegen die älteren gepinnten Zertifikate bestätigt

Das ältere
`universalraum-native-ground-response-20260915/ground_replay/weak_coupling_ground_normal.json`
enthält genau die genannte Grenze: g/Δ=1/20, μ/Δ=1/50 und neuer Grundsektor
N=0. Sein SHA-256 ist
`e1cd19988edd33c6799ec6b80f0a52d56e1a532bfe1b56870623a4efaf06bd0c`;
dies stimmt mit `ground_replay_manifest.json` überein. Normaler und
optimierter vorhandener Bericht sind weiterhin bytegleich. Der eingetragene
Programmpin
`794554393c495ba395f34e6a58d490da821408d4f8effbc394653cd4cec4e80a`
stimmt mit der vorhandenen `ground_replay/work/many_pair/weak_coupling.py`
überein.

Die stärkere und direktere Begründung ist bereits in
`universalraum-v16-integrated-20260915/RESULTS.md` §3 und dessen
`new_checks.json` dokumentiert. Der Checkerhash
`c3304a1cf502e5c4fffd63391cfb29db02ad3f2b3517f96e047c07170b63416e`
stimmt mit dem vorhandenen Programm und `replay_manifest.json` überein.
Aus der dort geprüften Voll-Fock-Schranke

\[
A=\sum_A P_A^\dagger P_A\le\frac{15}{2}N_f
\]

und quadratischer Ergänzung folgt

\[
H_\mu\ge\left(\mu-\frac{15g^2}{2\Delta}\right)N_f+2\mu N_b.
\]

Die einzige erneut benötigte Rechnung ist rational:

\[
\frac1{50}-\frac{15}{2}\left(\frac1{20}\right)^2=\frac1{800},
\qquad2\mu/\Delta=\frac1{25}.
\]

Also gilt \(H_\mu\ge\Delta N/800\). Da N=0 nur das leere Fockvakuum
enthält und Hμ dieses mit Energie null annihiliert, ist es eindeutig
minimal. Der globale Zustandsgegenvergleich ist damit bestätigt. Der
vollständige ältere Grundzustands-/Casimir-Prüflauf wurde für diesen
Nachtrag nicht neu ausgeführt; Pins, vorhandene Aussagen und die relevante
exakte Ungleichung wurden geprüft.

## Zwei Präzisierungen bei der Übernahme

1. In §7 sollte „ein positiver Unterschied“ durch **„eine
   nichtverschwindende Differenz“** ersetzt werden. Ein negativer signierter
   Unterschied ist ebenso ein kausaler Interventionsnachweis; genau dies
   zeigt der neue N=2-Phasenversuch.
2. Die globale Sektorwahl und die Beobachtbarkeit innerhalb eines festen
   Gesamtsektors getrennt halten. Ein System-Referenz-Vergleich kann relative
   Ladungsenergien aufdecken; ein Zusatz μN_total auf einem festgehaltenen
   Gesamtsektor bleibt dennoch eine unbeobachtbare gemeinsame Phase.

**Fazit:** Hauptpunkt abgedeckt, keine neue globale Schließung. Die
ausführlichere Quelle stärkt die Dokumentation der Voraussetzungen und die
Abgrenzung der Zustandsregel. Die tatsächliche neue Konstruktion dieser
Runde bleibt die gemeinsame bedingte N=2-Ausführung aus kausalem Eingriff
und terminaler Zustandstomografie.
