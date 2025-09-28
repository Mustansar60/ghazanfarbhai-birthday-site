# Birthday Celebration Website for Laraib Zahra

A fun, loving, and sparkly website built with Python Flask and Bootstrap to celebrate Laraib Zahra. Includes family wishes, visitor wishes, photo gallery, music player, and celebration effects (confetti, fireworks, cake message).

## Features
- Animated hero banner and balloons
- Family wishes (preloaded) + visitor-submitted wishes (in-memory)
- Photo gallery loading all images from `static/images/` with modal viewer
- Music player loading tracks from `static/music/` with play/pause/mute
- Confetti, fireworks, and a special cake interaction
- Mobile-first responsive design and warm theme (pink, purple, gold, white)

## Project Structure
```
app.py
requirements.txt
templates/
  index.html
static/
  images/
  music/
```

## Setup
1. Create and activate a virtual environment (recommended):
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your assets:
- Place photos in `static/images/`
- Place MP3 files in `static/music/`

4. Run the app:
```bash
python app.py
```
The site will be available at `http://localhost:5000`.

## Notes
- Visitor wishes are stored in memory and reset on server restart.
- Supported image extensions: .png .jpg .jpeg .gif .webp
- Supported audio extensions: .mp3 .wav .ogg .m4a

## Deploying
For production, use a WSGI server such as `gunicorn` and set `debug=False`.