# Produkt-Roadmap
Diese Roadmap zeigt die geplanten Entwicklungsschritte für unsere App zur Berechnung und zum bewussten Umgang mit Koffein.
Die Funktionen wurden nach Priorität und Nutzermehrwert in mehrere aufeinanderfolgende Versionen gegliedert.
Jede Version ist funktionsfähig und erweiterbar.

## MVP Basis - Auf dem Weg zum MVP
Grundstruktur der App erstellen:
- Leere, lauffähige App aufsetzen 
- Navigation mit ersten Seiten vorbereiten, z. B. Home, Calculator
- App veröffentlichen

Logins:
- Mehrere Nutzer: Nutzung durch verschiedene Personen 
- Datensicherung: Speicherung der Daten pro Nutzer

Profilseite (Your Profile):
- Name, Alter, Gewicht (kg), Grösse (cm) 
- Geschlecht 

Zusätzliche Daten (Additional Data):
- Medikamenteneinnahme 
- weitere relevante Faktoren (z. B. Grunderkrankungen, Allergien)

Diese Version bildet die Basis der App.

## Version 1.0 - Calculator - MVP (Minimal Viable Product)
Eingaben:
- Auswahl der verschiedenen koffeinhaltigen Getränke (z. B. Kaffee, Energy Drink, Mate) -> jedes Getränk hat bereits hinterlegte Werte
- Datum und Uhrzeit des Konsums
- Körpergewicht aus dem Profil wird für eine personalisierte Berechnung verwendet
- Suchbegriff -> Nutzer:innen können Getränke suchen, Suche erkennt auch kleine Tippfehler

Berechnung:
- Gesamte aktuelle Koffeinmenge -> alle aktuell ausgewählten Getränke werden zusammengerechnet
- Wirkungsdauer des Koffeins -> Countdown (zählt in Echtzeit runter)
- Remaining Effect -> App berechnet die verbleibende Wirkungszeit
- Koffeinmenge pro Kilogramm Körpergewicht und persönlicher Tagesrichtwert wird berechnet
- Risikoeinschätzung -> App bewertet die Koffeinmenge anhand mg/kg

Ausgabe:
- Ausgewähltes Getränk
- Koffeinmenge und Volumen
- Caffeine Timeline -> App zeigt die wichtigsten Wirkungsphasen
- Animierter Countdown -> Zeigt die verbleibende Wirkungszeit in Stunden, Minuten und Sekunden (inkl. visueller Darstellung anhand eines Gefässes bei dem der Flüssigkeitsstand mit der verbleibenden Wirkung sinkt)
- Current Calculator Entries -> zeigt aktuell gespeicherte Koffeinmenge im Rechner
- Clear Button -> Nutzer:innen können die aktuellen Einträge direkt löschen
- Personalized Caffeine Impact -> zeigt persönliche Werte
- Fortschrittsbalken zeigt, wie viel Prozent des persönlichen richtwerts bereits erreicht wurde

Ziel: Funktionierender Kern der App

### Koffein-History
Datenspeicherung:
- Speicherung der eingegebenen Koffeinwerte
- Darstellung der Werte in Tabellenform und Grafik
- Sortierung nach Datum und Zeit (Timestamp)

My Diary:
- Tagebuch, um seine persönlichen Gedanken, Symptome und Gefühle zum Koffeinkonsum festzuhalten

Ziel: langfristiges Tracking des Konsums

## Version 2.0 - Erweiterung: Empfehlungen (Recommendations)
Visualisierung:
- Darstellung in Form einer Kurve (z. B. Peak, Abbau, Müdigkeit) 

Empfehlungssystem: 
Anzeige von Zuständen wie:
- „Peak“
- „I can't fall asleep“
- „I feel tired“

Interaktive Auswahl:
- Nutzer können auswählen, wie sie sich fühlen
- passende Empfehlungen werden angezeigt 

Detailseiten (z. B. „I can’t fall asleep“):
- konkrete Tipps zur Verbesserung 
- Hinweise zum Umgang mit zu viel Koffein 

Ziel: Nutzer verstehen ihren Koffeinzustand besser und erhalten direkte Hilfe bei Problemen 

## Version 3.0 - Erweiterung: Alternativen
Auswahl alternativer Getränke:
- mit Koffein (z. B. Guarana)
- ohne Koffein (z. B. Kräutertee) 

Empfehlungen je nach Situation:
- z. B. bei Müdigkeit oder Schlafproblemen 

Informationsbereich:
- kurze Beschreibung der Alternativen 

Ziel: bewusster Konsum statt nur Berechnung

## Version 4.0: Erweiterung: Professionelle Hilfe
Verknüpfung mit Fachpersonen:
- Weiterleitung zu Ernährungsberater:innen oder medizinischen Fachstellen

Ziel: Unterstützung bei starkem Koffeinkonsum oder gesundheitlichen Problemen

## Version 5.0: Optional - Weiterführende Ideen (nicht Teil des aktuellen Zeitrahmens)
Diese weiterführenden Ideen zeigen das Potenzial der App und mögliche Ausbaustufen, die im Rahmen dieses Projekts nicht umgesetzt werden, aber zukünftige Weiterentwicklungen ermöglichen.

Soziale Funktionen:
- Verbindung mit Freund:innen
- Gegenseitiges Teilen des Koffeinkonsums

Ziel: Unterstützung im Alltag, Wir-Gefühl erzeugen
  
Spielerische Elemente:
- Belohnungssystem (z. B. Punkte, Levels, Streaks)

Ziel: Motivation und Durchhaltevermögen fördern
