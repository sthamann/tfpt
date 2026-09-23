Eine vollständige Lösung aller Follow-ups und offenen Fragen gibt es aus den vorliegenden Quellen nicht. Das ist das Ergebnis der Durchsicht, nicht eine Ausrede.

Die v1.4-Texte, das 126-Seiten-Hauptbuch, das Update, `neu_1.md` und das Prüfarchiv sagen dasselbe: Es fehlt weiterhin **eine** Quelle, die Operationsalgebra, Zustand, lokale Kopplung, Skalierung und Auslesung zusammen festlegt. Solange verschiedene erlaubte Fortsetzungen verschiedene Architekturen, Dimensionen oder empirische Zahlen liefern, ist eine eindeutige Gesamtlösung nicht ableitbar. Wer die Lücken mit extra gewählten Modellen füllt, schreibt eine neue Theorie, keine Ableitung aus TFPT.

## Was sich wirklich schließen lässt

Unabhängig nachgerechnet (58 Checks in `followup_closure.py`):

**Follow-up 1 — Controller.** Die Phasenreferenzobstruktion ist exakt: unkontrolliertes \(U\) und \(e^{i\phi}U\) sind derselbe Kanal, kontrolliertes \(-I\) schickt \(|+\rangle\) auf \(|-\rangle\). Ein gegebenes Programm lässt sich unitär einbetten, seine Zutaten folgen daraus nicht. Reset ohne Abfluss braucht im Worst Case Dimension \(d^k\). Native Herkunft von kontrolliertem \(H\), Resonanz, \(Q\) und Reset bleibt offen.

**Follow-up 2 — Architektur.** Lokalität allein wählt nicht zwischen Zellbank und Kantenbank. In der diagonalen Besetzungsalgebra erzwingt Erhaltung aller \(Q_v\) Kantenadressierung. Ob diese \(Q_v\) Erhaltungsgrößen der ursprünglichen Quelle sind, ist unbeantwortet.

**Follow-up 3 — Quartett.** Clebsch-Automorphismengruppe \(G=N\rtimes S_5\) hat Ordnung 1920, ist vollständig, realisiert 12 Zykeltypen. \(\dim\mathrm{Specht}(4^4)=24024\). Die Ränge 28 / 320 / 80 stehen als ganzzahliger Satz in `neu_1`; die Charaktere habe ich hier nicht drittunabhängig neu erzeugt. \(0\preceq F_{4,\mathrm{edge}}\preceq 896\,I\). Die numerischen Werte
\(E_0/J\approx 11{,}96050741\), \(E_1/J\approx 12{,}44698494\) (vierfach gefunden) sind keine Intervallzertifikate. Der Nichtsingulettvergleich bleibt bedingt.

**Follow-up 4 — Robustheit.** 13-Faktor-Vollraumfilter und 9-Faktor-Eingangsfilter reproduziert: \(6345{,}659268\) bzw. \(4620{,}609881\,\hbar/\Delta\), dieselben Rohwahrscheinlichkeiten. Reine Zeitschranken und die gekoppelte Referenzfamilie (Gap \(2J\), endliche Schaltung aus einem Produktmodell) gelten im erklärten Modell. Sie beweisen weder C16-Vielzellendynamik noch einen relativistischen Limes.

**Follow-up 5 — eine Welt.** Nicht geschlossen. Die Gegenmodelle widerlegen verkürzte Schlüsse (Wärmekern wählt keine 3D, Fluss 3 steckt die drei Nullmoden ein, TT-Projektor erzeugt keinen masselosen Pol, gapped Referenz hat keinen Spin-2-Pol). Sie widerlegen nicht die Möglichkeit einer stärkeren, noch nicht konstruierten Quelle.

**Follow-up 6 — gemeinsame Parameter.** Nachgerechnet: \(c_{3,\mathrm{ACT}}=0{,}03596504269\ldots\) statt \(1/(8\pi)\), relative Änderung \(-9{,}610\,\%\). Dieselbe elektromagnetische Gleichung liefert dann \(\alpha^{-1}=167{,}80329862963\ldots\) statt \(137{,}03599921684\ldots\). Eine einfache \(c_3\)-Umstellung im fixierten Vertrag ist ausgeschlossen. Flavour und Likelihood bleiben offen.

RH, Faktorisierung, P vs NP, dunkle Materie/Energie, Baryogenese, starkes CP, schwarze Löcher, Zeitpfeil und Messproblem sind durch Filter, Band oder positives \(F_4\) nicht berührt.

## Der tatsächliche nächste Engpass

Nicht zwölf neue Narrative, sondern drei endliche Sätze:

1. die 80×80-Quartettmatrix und die 28×28-Trivialmatrix von \(H_0\) und \(F_{4,\mathrm{edge}}\) exakt aufbauen,
2. ein Inertia-Zertifikat: nacktes Nichtsingulett \(\ge 11{,}6\,J\) gegen Quartett \(\le 12{,}45\,J\),
3. native Herkunft von kontrolliertem \(H\), \(Q\) und Reset — oder die klare Markierung, dass sie Zusatzressourcen bleiben.

Ohne (1)–(3) ist jede „Lösung“ von T3/T4/T7/T6 ein neues Modell.

Ausgeschrieben steht das in `artifacts/TFPT_Followups_Abschluss_2026-09-14.md`, die Checks in `artifacts/followup_closure.py`. Wenn du willst, ist der sinnvolle nächste Schritt genau Punkt 1: den 80D-Block bauen, nicht eine neue Weltgeschichte.
