#!/usr/bin/env python3
"""
generate.py — Generiert eine Job-spezifische Bewerbungsseite für David Girnstein.

Verwendung:
    python generate.py <job-id>

Beispiel:
    python generate.py rzl24

Voraussetzungen:
    pip install anthropic pandas
    export ANTHROPIC_API_KEY=dein-key
"""

import sys
import os
import csv
import anthropic

# ─── Konfiguration ────────────────────────────────────────────────────────────

PROFIL_DATEI = "mein-profil.md"
JOBS_DATEI = "jobs.csv"
OUTPUT_ORDNER = "jobs"

# ─── Hilfsfunktionen ──────────────────────────────────────────────────────────

def lade_profil():
    with open(PROFIL_DATEI, "r", encoding="utf-8") as f:
        return f.read()

def lade_job(job_id):
    with open(JOBS_DATEI, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["id"] == job_id:
                return row
    return None

def generiere_html(job, profil):
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    prompt = f"""Du bist ein Senior Frontend Developer und Copywriter. 
Du erstellst eine einzelne, vollständige HTML-Datei als personalisierte Bewerbungsseite.

## Kontext
Diese Seite wird von einem Recruiter bei {job['company']} aufgerufen.
Der Link steht im Lebenslauf von David Girnstein — der Recruiter klickt drauf und sieht diese Seite.
Ziel: In 30 Sekunden überzeugen. Kein Anschreiben-Stil. Visuell. Direkt. Mutig.

## Bewerberprofil
{profil}

## Stellenbeschreibung ({job['role']} bei {job['company']})
{job['stellenbeschreibung']}

## Anforderungen an die HTML-Seite

### Design-Vorgaben (PFLICHT):
- Farbpalette: Schwarz (#0a0a0a) als Hintergrund, Lime-Grün (#c8e000) als Akzentfarbe, Weiß für Text
- Schriftarten: Lade "Space Grotesk" und "Anton" von Google Fonts
- Vollständig responsive
- Subtile Animationen beim Laden (fade-in, slide-up)
- "Made with AI by David Girnstein" — sichtbares Badge oben rechts

### Inhalt (PFLICHT — in dieser Reihenfolge):
1. **Hero-Bereich**: Große Überschrift "Warum David?" + Unterzeile mit Firmenname {job['company']} und Rolle {job['role']}
2. **Match-Sektion**: Zeige genau 3 Anforderungen aus der Stellenbeschreibung — jeweils daneben Davids konkretes Beispiel dafür. Layout: zwei Spalten, Anforderung links (grau), Davids Beweis rechts (weiß, fett)
3. **Highlight-Projekt**: Das eine Projekt aus Davids Profil, das am besten zur Stelle passt — mit kurzem erklärenden Satz warum
4. **Stellenbeschreibung interaktiv**: Zeige die originale Stellenbeschreibung. Wichtige Keywords/Phrasen sind mit Lime-Grün hervorgehoben. Beim Hover über ein hervorgehobenes Wort erscheint ein Tooltip mit "David kann das, weil: [konkreter Grund aus seinem Profil]"
5. **CTA-Bereich**: Button "Portfolio ansehen" → https://girnstein-david.framer.website und Button "LinkedIn" → https://www.linkedin.com/in/davidgirnstein

### Technische Vorgaben:
- Alles in einer einzigen .html Datei (kein externes CSS, kein externes JS außer Google Fonts)
- Tooltips in reinem JavaScript, kein Framework
- Keine Platzhalter — echter, spezifischer Inhalt basierend auf dem Profil und der Stelle
- Am Ende der Seite kleiner Footer: "Diese Seite wurde mit Claude AI generiert und von David Girnstein kuratiert."

Gib NUR den vollständigen HTML-Code zurück. Keine Erklärungen, kein Markdown, kein ```html Block. Nur reines HTML ab <!DOCTYPE html>."""

    print(f"⏳ Generiere Seite für {job['company']} ({job['role']})...")

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=8000,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text

def speichere_html(job_id, html_inhalt):
    os.makedirs(OUTPUT_ORDNER, exist_ok=True)
    dateiname = f"{OUTPUT_ORDNER}/{job_id}.html"
    with open(dateiname, "w", encoding="utf-8") as f:
        f.write(html_inhalt)
    return dateiname

# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("❌ Verwendung: python generate.py <job-id>")
        print("   Beispiel:   python generate.py rzl24")
        sys.exit(1)

    job_id = sys.argv[1]

    # API Key prüfen
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("❌ ANTHROPIC_API_KEY nicht gesetzt.")
        print("   Führe aus: export ANTHROPIC_API_KEY=dein-key")
        sys.exit(1)

    # Job laden
    job = lade_job(job_id)
    if not job:
        print(f"❌ Job-ID '{job_id}' nicht in jobs.csv gefunden.")
        sys.exit(1)

    # Profil laden
    profil = lade_profil()

    # HTML generieren
    html = generiere_html(job, profil)

    # Speichern
    dateiname = speichere_html(job_id, html)

    print(f"✅ Seite gespeichert: {dateiname}")
    print(f"📤 Jetzt hochladen:")
    print(f"   git add . && git commit -m 'Add {job_id}' && git push")
    print(f"🔗 Link für Bewerbung:")
    print(f"   https://girni123.github.io/hire/jobs/{job_id}.html")

if __name__ == "__main__":
    main()
