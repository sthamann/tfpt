# Unabhängiger Gegenreview der Zugriffssätze

10. September 2026. Geprüft durch die parallele Beobachter-/Interventionsspur. Gelesen: BEWEIS.md vollständig, für die Abnahme insbesondere Abschnitte 1–5; check_access.py vollständig; Bindung von checks.json an beide aktuellen Dateien überprüft. Die 38 Kontrollen wurden hier nicht nochmals ausgeführt. Ergebnis: **Die ausgeschriebenen Sätze und Gegenbeispiele tragen im angegebenen Scope. Keine materielle Beweislücke gefunden.**

## 1. Quotientendynamik genau bei Kernelinvarianz

Die Notwendigkeit aus ET=T̄E und die Konstruktion T̄(Ev)=ETv sind korrekt. Surjektivität wird ausdrücklich benutzt und liefert Eindeutigkeit auf dem ganzen W. Die Vertreterunabhängigkeit benötigt genau T(ker E)⊆ker E. Die Erweiterung auf Generatorwörter folgt durch Komposition. Der Zusatz zu inversen Operationen ist ebenfalls korrekt: Bei endlicher Dimension und invertierbarem T besitzt T(ker E) dieselbe Dimension wie ker E; die Inklusion ist daher Gleichheit. Für beliebige unendliche Dimension darf dieser letzte Schluss nicht übernommen werden; der Text tut das nicht.

## 2. CPTP-Rechtsinverse und korrelierte Eingaben

R(σ)=σ⊗τ ist für einen normierten positiven Umgebungszustand τ vollständig positiv und spurerhaltend; ER=id. Wenn die lineare Kernelbedingung gilt, ist Φ=E𝒯R die eindeutige induzierte Abbildung und daher CPTP. Für beliebiges X gilt dann X−R(EX)∈ker E und somit E𝒯X=E𝒯R(EX). Diese Gleichung belegt ausdrücklich die Gültigkeit für korrelierte Eingangszustände. Das bloße Definieren von Φ für eine feste Produktpräparation würde dies nicht leisten; diese Grenze ist im Text richtig dargestellt.

Die Übergabe von der Forderung für alle Dichtematrizen zur linearen Matrixgleichung ist zulässig: Dichtematrizen spannen den hermiteschen Raum reell, und dieser spannt die volle Matrixalgebra komplex. Diese elementare Begründung kann bei Bedarf ergänzt werden; sie ist keine fehlende Zusatzannahme.

## 3. Bell/CNOT-Zeuge

Mit der im Skript verwendeten Basisreihenfolge |00>,|01>,|10>,|11> und A als Steuerbit ist U(|00>±|11>)/√2=(|0>±|1>)/√2⊗|0>. Die beiden reduzierten Eingänge sind I/2 und die reduzierten Ausgänge die orthogonalen X-Eigenzustände. Daher liegt ρ₊−ρ₋ in ker E, während E𝒯(ρ₊−ρ₋)=σ_x. Die Richtung des Signalisierens und die Tensorreihenfolge stimmen. Eine physisch verbotene gemeinsame Operation jenseits eines wirklichen Horizonts wird ausdrücklich nicht vorausgesetzt.

## 4. Minimax-Grenze

Die Dreiecksungleichung des Spurabstands liefert D(η₊,η₋)≤D(η₊,ξ)+D(ξ,η₋)≤2 max D. Bei den orthogonalen Ausgängen ist die untere Grenze exakt 1/2. Sie ist erreichbar: ξ=I/2 besitzt zu beiden X-Eigenzuständen Abstand 1/2. Für die Wiedergewinnung der ursprünglichen Bellzustände erreicht ξ=(ρ₊+ρ₋)/2 dieselbe Grenze. Diese Erreichbarkeiten verstärken die genannte Untergrenze zu einem exakten Minimaxwert, falls dieser Begriff im Bericht benutzt wird. Zufall, der ausschließlich aus demselben reduzierten Eingang erzeugt wird, schafft kein Signal über das verlorene Vorzeichen.

## 5. Produktunitär unter vollständigem einseitigem Nichtsignalisieren

Das Heisenbergbild bildet M_A⊗I in sich ab. Die induzierte Abbildung ist wegen unitärer Konjugation ein unitaler injektiver *-Homomorphismus von M_A in M_A. Endliche gleiche Dimension macht daraus einen Automorphismus. Die Matrixeinheitenkonstruktion begründet dessen innere Implementierung. Nach Entfernen des A-Unitärs liegt das verbleibende Unitär im Kommutanten I⊗M_B. Somit folgt exakt U=U_A⊗U_B. Die Umkehrung gilt direkt. Das Vorzeichen beziehungsweise die Wahl V versus V* ist eine Konvention der im Text definierten inneren Implementierung und ändert das Produktresultat nicht.

Der deklarierte Scope ist erforderlich: feste vollständige endliche Tensorfaktoren, gemeinsames geschlossenes Unitär und sämtliche gemeinsamen Zustände. Daraus folgt weder ein Verbot einseitiger offener Kanäle noch eines eingeschränkten Codebereichs oder von Feldalgebra-/Raumzeit-Horizonten. Der Text hält diese Grenzen ein. Der bekannte Theorem-7-Verweis wird als Literaturresultat und nicht als neue Priorität bezeichnet.

## Gebundene Dateien

- BEWEIS.md SHA-256: `1a0db8252604197c0d082755b7a59dc756c16e83abbaa3cdf77f77a6af9d28c7`
- check_access.py SHA-256: `553ba9f90194e336fa5b8a8ca7e518803f5ac8f4a66cac320edf733d691c41dd`
- checks.json nennt 38 erfolgreiche Kontrollen und bindet genau diese beiden Hashes.

Dieser Gegenreview ist eine mathematische Prüfung der ausgeschriebenen Argumente und ihrer Umsetzung, kein formales Beweisassistent-Zertifikat und keine erneute Prüfung des gesamten Originalartikels.
