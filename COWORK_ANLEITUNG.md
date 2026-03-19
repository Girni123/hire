# ANLEITUNG FÜR CLAUDE — hire-portfolio

Diese Anleitung ist für Claude (AI), damit er genau weiß was zu tun ist wenn er Zugriff auf diesen Ordner bekommt.

---

## Was dieser Ordner ist

Das ist Davids personalisiertes Bewerbungssystem. Für jede Stelle, auf die David sich bewirbt, generiere ich eine individuelle HTML-Seite die:
- Die Stellenbeschreibung des Unternehmens interaktiv darstellt (hover → tooltips mit Davids Bezug)
- Drei konkrete Matches zwischen Anforderungen und Davids Erfahrung zeigt
- Ein passendes Highlight-Projekt vorstellt
- Das Firmenlogo einbindet (wenn vorhanden)
- Einen großen, prominenten "Made with AI by David" Banner hat
- Einen Terminal-Ladescreen hat, der den AI-Charakter unterstreicht

---

## Dateien die du lesen musst

1. `mein-profil.md` — Davids vollständiges Profil, Projekte, Skills, Zertifikate, Links
2. `jobs.csv` — Die Tabelle aller Bewerbungen mit Stellenbeschreibungen

---

## jobs.csv Spalten

| Spalte | Inhalt |
|---|---|
| id | Kurz-ID, z.B. rzl24 (wird Dateiname) |
| company | Unternehmensname |
| role | Stellenbezeichnung |
| url | Link zur Stellenanzeige |
| status | beworben / geplant / abgelehnt |
| date_added | Datum |
| layout | 1, 2 oder 3 (welches Design) |
| logo_url | URL zum Firmenlogo (optional, leer lassen wenn keins) |
| stellenbeschreibung | Vollständiger Text der Stellenausschreibung |

---

## Layouts

| Nummer | Style | Einsatz |
|---|---|---|
| 1 | Schwarz + Lime-Grün, Anton Font, mutig/modern | Tech-Startups, Agenturen, Digital-first Companies |
| 2 | Weiß + Navy + Gold, Playfair Serif, klassisch | Banken, Versicherungen, traditionelle Konzerne |
| 3 | Dunkelblau/GitHub-Style, Syne Font, developer-ish | IT-Firmen, SaaS, Developer-Tools |

Template-Dateien liegen in `/templates/`:
- `layout1-bold.html` = das Grundformat (rzl24.html ist ein Beispiel)
- `layout2-classic.html`
- `layout3-dev.html`

---

## Was ich von dir will wenn du eine neue Seite generieren sollst

David wird dir sagen: "Erstell mir eine Seite für Job-ID [xyz]"

### Dann machst du folgendes:

1. **`jobs.csv` lesen** — Zeile mit der ID finden, alle Infos extrahieren
2. **`mein-profil.md` lesen** — Davids vollständiges Profil kennen
3. **Passendes Template auswählen** — basierend auf der `layout`-Spalte
4. **Template befüllen** mit:
   - Firmenname, Rolle, Logo-URL
   - Stellenbeschreibung mit 4–6 hervorgehobenen Keywords + je einem tooltip der erklärt warum David das kann (konkret, aus dem Profil, nicht generisch)
   - 3 Match-Rows: je eine Anforderung aus der Stelle + Davids konkreter Beweis
   - Das am besten passende Projekt aus dem Profil + warum es für genau diese Stelle relevant ist
5. **Datei speichern als** `jobs/[id].html`
6. David Bescheid geben dass er mit `git add . && git commit -m "Add [id]" && git push` hochladen kann

### Wichtige Prinzipien bei der Generierung:
- **Kein Bullshit**: Nur echte Verbindungen zwischen Stelle und Profil, keine ausgedachten Kompetenzen
- **Konkret, nicht generisch**: Nicht "David hat Erfahrung mit PM" sondern "Bei REWE koordiniert David..."
- **Stellenbeschreibung komplett übernehmen**: Den echten Text der Stelle verwenden, nicht paraphrasieren
- **Tooltips sind der Kern**: Mindestens 4 hervorgehobene Keywords mit echten, konkreten Begründungen
- **Projekt muss wirklich passen**: Wähle das Projekt das am ehesten zur Stelle passt, erkläre warum

---

## Links die immer gleich bleiben
- Portfolio: https://girnstein-david.framer.website
- LinkedIn: https://www.linkedin.com/in/davidgirnstein
- Email: david@girnstein.studio
- GitHub Pages Base: https://girni123.github.io/hire/jobs/

---

## Was du NICHT tun sollst
- Keine neuen Spalten in jobs.csv anlegen ohne Rückfrage
- Keine anderen Dateien verändern außer den generierten HTML-Seiten in /jobs/
- Kein Profil von dir aus erweitern oder verändern
- Keine Links erfinden — nur Links aus mein-profil.md oder der Stellenanzeige verwenden
