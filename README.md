# hire-portfolio

Personalisierte Bewerbungsseiten für David Girnstein — one link per job.

## Setup (einmalig, ~10 Minuten)

### 1. Repo auf GitHub erstellen
- GitHub → New Repository → Name: `hire`
- Public ✓ → Create repository

### 2. GitHub Pages aktivieren
- Settings → Pages → Source: `Deploy from a branch` → Branch: `main` → `/root` → Save
- Dein Link wird: `https://girni123.github.io/hire/`

### 3. Lokal einrichten
```bash
git clone https://github.com/girni123/hire.git
cd hire
# Alle Dateien aus diesem Ordner reinkopieren
git add .
git commit -m "Initial setup"
git push
```

### 4. API Key setzen (für generate.py)
```bash
export ANTHROPIC_API_KEY=sk-ant-...
```
Tipp: In deine `~/.zshrc` oder `~/.bashrc` eintragen damit du das nicht jedes Mal machst.

### 5. Dependencies installieren
```bash
pip install anthropic
```

---

## Workflow — neuer Job

### Schritt 1: Job in jobs.csv eintragen
Öffne `jobs.csv` in Numbers (oder Excel) und füge eine Zeile hinzu:

| id | company | role | url | status | date_added | stellenbeschreibung |
|---|---|---|---|---|---|---|
| rzl24 | CHECK24 | Junior Digital PM | https://... | beworben | 2026-03-18 | [Stellenbeschreibung reinkopieren] |

**ID-Format:** 3 Buchstaben Firma + 2 Ziffern (fortlaufend)  
Beispiele: `rzl24` (Rewe), `c2424` (CHECK24), `ama01` (Amazon)

### Schritt 2: Seite generieren
```bash
python generate.py rzl24
```

### Schritt 3: Kurz anschauen
```bash
open jobs/rzl24.html
```
Schau kurz drüber — passt alles? Stimmt der Ton?

### Schritt 4: Hochladen
```bash
git add .
git commit -m "Add rzl24 CHECK24"
git push
```

### Schritt 5: Link in Bewerbung einbauen
```
https://girni123.github.io/hire/jobs/rzl24.html
```

---

## Dateistruktur

```
hire/
├── index.html          ← Fallback wenn kein Job-Link
├── mein-profil.md      ← Dein Profil (einmal pflegen)
├── jobs.csv            ← Alle Bewerbungen
├── generate.py         ← Das Generator-Script
└── jobs/
    ├── rzl24.html      ← CHECK24
    └── ...
```

---

## jobs.csv in Apple Numbers öffnen

Numbers öffnet CSV automatisch. Beim Speichern: `Ablage → Exportieren → CSV`.  
Alternativ einfach in einem Texteditor bearbeiten — es ist eine normale Textdatei.

---

## Kosten

| Was | Kosten |
|---|---|
| GitHub Pages | Kostenlos |
| Anthropic API (generate.py) | ~0,05–0,15€ pro generierter Seite |
| Hosting | Kostenlos |

Die generierten HTML-Dateien haben **keine laufenden Kosten** — sie sind statische Seiten.
