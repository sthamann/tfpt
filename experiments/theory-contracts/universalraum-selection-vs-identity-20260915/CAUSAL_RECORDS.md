# Drei begriffliche Gleichsetzungen im Selektionsauftrag

15. September 2026 · Ergänzende Beweise des Hauptagenten, keine dritte Modellroute

## 1. Nichtfaktorisierte Antworten sind noch keine Wechselwirkung

Der Ausdruck G_AB≠G_A⊗G_B muss zwischen Zustandskorrelation und dynamischer
Kopplung unterscheiden. Schon die Bell-Präparation (|00>+|11>)/sqrt(2) hat
<X_A X_B>=1, aber <X_A>=<X_B>=0. Bei H=0 beziehungsweise der Produktentwicklung
I_A⊗I_B bleibt diese Korrelation bestehen, ohne Wechselwirkung während der
betrachteten Entwicklung. Die gemeinsame Präparation kann vorher eine
Wechselwirkung benutzt haben; das ist gerade nicht durch den späteren
Korrelationsbefund zeitlich oder dynamisch identifiziert.

Umgekehrt lässt die verschränkende kontrollierte Phase CZ=diag(1,1,1,−1)
die ausgewählte Präparation |00> vollständig unverändert. Ein blinder
Zustandsversuch kann vorhandene Kopplung also übersehen. Dies ist kein
Gegenbeispiel gegen vollständige Prozesstomographie mit allen lokalen Eingriffen.

### Der richtige operative Unterschied

Sei E_A ein spurtreuer lokaler Eingriff vor U und B ein lokaler Leser danach.
Vergleiche dieselbe Präparation mit verschiedenen Eingriffen, ohne
nachträgliche Auswahl von Messergebnissen. Für U=U_A⊗U_B gilt für alle ρ

    tr_A[(E_A⊗id)(ρ)] = tr_A ρ.

In Krausdarstellung folgt das aus Σ K_j†K_j=I durch Zyklizität der partiellen
Spur für Operatoren auf A. Daher kann kein solcher Eingriff die nachfolgende
B-Antwort verändern. Vorhandene Verschränkung widerlegt dies nicht.

Für die kontrollierte Phase, den gleichen Start |0>_A|+>_B und den Leser X_B
erhält man dagegen

    Eingriff I_A:  <X_B>=+1,
    Eingriff X_A:  <X_B>=−1.

Das ist ein wirklicher kontrollierter kausaler Anschluss dieses Beispiels.
Es ist **kein** aus TFPT hergeleiteter Anschluss. Der bestehende Operationssatz
müsste dieselben Eingriffe und den Leser selbst rechtfertigen.

Die Unterscheidung entspricht der primären Analyse von
[Beckman et al., Causal and localizable quantum operations](https://arxiv.org/abs/quant-ph/0102043).
Ein nur bedingter, fernseitig veränderter Zustand nach Postselektion ist kein
unbedingtes Signal; der Checker enthält eine solche Kontrollrechnung.

## 2. Ein unveränderter historischer Record ist kein unveränderter Gegenstand

Eine Speicherhälfte R, auf die die nachfolgende Entwicklung U_S⊗I_R nicht
zugreift, behält ihren reduzierten Zustand für **jedes** U_S. Auch ein zuvor
aufgezeichneter Wert bleibt dort lesbar. Der aktuelle Systemwert darf sich
inzwischen ändern. Beispiel: Im Zustand (|00>+|11>)/sqrt(2) korrelieren aktueller
Z-Wert und Record zunächst mit +1. Nach X_S korrelieren sie mit −1; die
Speicherstatistik ist unverändert.

Wer stattdessen fordert, dass jeder Record auch zu jedem späteren Zeitpunkt
noch den **aktuellen** Wert wiedergibt, fordert zusätzlich eine erhaltene
Observable: U†Π_jU=Π_j. Diese stärkere QND-Bedingung beschränkt U. Sie ist nicht
aus historischer Speicherung allein hergeleitet.

Noch stärker wäre Unveränderlichkeit unter **allen** Operationen einer
irreduziblen Algebra. Für einen Recordprojektor Q folgte [Q,A]=0 für sämtliche
A; dann ist Q nach Schurs Lemma skalar, also Q=0 oder I. Beim Zweiniveaubeispiel
erzwingen bereits [Q,X]=[Q,Z]=0 die Form Q=qI. Dies ist kein No-go für Records
in E₈- oder Quantenmodellen: physische Records sind bezüglich einer bestimmten
Entwicklung/zugänglichen Teilalgebra, nicht zwingend aller denkbaren Operationen,
zu definieren. Approximate Stabilität ist nochmals eine andere Behauptung.

## 3. Information ordnet Beschreibungen, aber bestimmt nicht allein Kausalität

Wenn X aus Y fehlerfrei berechenbar ist, also X=f(Y), entsteht eine
Informations-Vorordnung. Sie ist reflexiv und transitiv. Erst der Quotient
nach gegenseitiger Rekonstruierbarkeit macht daraus eine partielle Ordnung.

Ein früherer Record X und seine spätere perfekte Kopie Y sind jedoch gegenseitig
rekonstruierbar. Diese Ordnung setzt sie gleich, obwohl es verschiedene
physische Ereignisse mit einer gerichteten Kopieroperation sein können.
Informationsrefinement kann eine Relation beschreiben, aber nicht ohne weitere
Prozessinformation Ereigniszeit und kausale Richtung rekonstruieren.

Das kleinste kausale Gegenbeispiel benutzt zwei faire, identische Bits:

    Modell 1: X wird fair erzeugt, anschließend Y=X.
    Modell 2: Y wird fair erzeugt, anschließend X=Y.

Beide haben P(X=Y=0)=P(X=Y=1)=1/2. Nach do(X=1) ist aber P(Y=1) im ersten
Modell eins, im zweiten ein Halb. Die passiven Records enthalten nicht die
Interventionsrichtung. Quantenprozessmodelle benötigen die entsprechenden
operationalen Unterscheidungen ebenfalls; siehe
[Costa und Shrapnel, Quantum causal modelling](https://arxiv.org/abs/1512.07106).
Das leitet noch keine fundamentale externe Zeit ab und setzt keine bestimmte
klassische Kausalordnung für jede mögliche Quantengravitation voraus.

### Kapazität statt neuer Bausteine

Wenn n binäre Ereignisse sämtliche 2^n Kombinationen mit nichtverschwindender
Wahrscheinlichkeit zulassen und dauerhaft **perfekt** gemeinsam auslesbar
bleiben sollen, müssen ihre Recordzustände orthogonale Träger haben. Die
Recorddimension ist mindestens 2^n. Das folgt schon aus dem Rang ihrer
Unterscheidungs-Gram-Matrix. Ein endlicher Speicher kann nicht unbegrenzt neue,
unabhängige, perfekte Records behalten. Kompression korrelierter Geschichten,
unvollkommene Records, Löschung oder ein wachsender/unendlicher Träger sind
andere Verträge. Eine kurze Grundregel kann sehr wohl einen unendlichen
Prozess erzeugen; die Kapazitätsgrenze verlangt keine lange Grundregel.

## 4. Konsequenz für den neuen Selektionsgedanken

»Selbstbeschreibung«, »stabile Records«, »Nichtfaktorisierbarkeit« und
»Informationsordnung« dürfen nicht als vier unabhängige Gründe für dieselbe
Physik gezählt werden. Zuerst sind ihre Objekttypen und Eingriffe festzulegen.
Die obigen Ergebnisse beseitigen falsche Identifikationen; sie wählen noch
keinen fundamentalen Prozess aus. Sie werden mit den zwei ausdrücklich
beauftragten, gegensätzlichen Worker-Ergebnissen zusammengeführt.

Reproduktion: `python3 -B causal_record_checker.py --output causal_normal.json`
und entsprechend `-OO` nach `causal_optimized.json`. Allgemeine Beweise stehen
hier; endliche Kontrollen ersetzen weder Quellenherleitung noch TOE-Abnahme.
