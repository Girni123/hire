# GIT SPICKZETTEL — hire-portfolio

## Erstes Mal Setup (einmalig)
```bash
cd /pfad/zu/hire-ordner
git init
git remote add origin https://github.com/Girni123/hire.git
git add .
git commit -m "Initial setup"
git branch -M main
git push -u origin main
```

## Neue Seite hochladen (jedes Mal)
```bash
cd /pfad/zu/hire-ordner
git add .
git commit -m "Add rzl24 CHECK24"
git push
```

## Neue Seite generieren + hochladen (kompletter Flow)
```bash
# 1. Seite generieren
python generate.py rzl24

# 2. Kurz im Browser anschauen
open jobs/rzl24.html

# 3. Hochladen
git add .
git commit -m "Add rzl24 CHECK24"
git push
```

## Status checken (was wurde geändert?)
```bash
git status
```

## Was ist der aktuelle Link?
```
https://girni123.github.io/hire/jobs/[JOB-ID].html
Beispiel: https://girni123.github.io/hire/jobs/rzl24.html
```

## ID-Schema für neue Jobs
Format: 3 Buchstaben Firma + 2 Ziffern
- CHECK24    → c2401, c2402, ...
- Zalando    → zal01, zal02, ...
- Amazon     → amz01, amz02, ...
- Rewe       → rwe01, rwe02, ...
- Spotify    → spt01, spt02, ...

## API Key setzen (einmalig, bleibt gespeichert)
```bash
echo 'export ANTHROPIC_API_KEY=sk-ant-DEIN-KEY' >> ~/.zshrc
source ~/.zshrc
```
