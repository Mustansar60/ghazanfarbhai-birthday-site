from __future__ import annotations

import os
from datetime import datetime
from typing import List, Dict

from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


# In-memory wishes store (resets on server restart)
WISHES: List[Dict[str, str]] = [
    {
        "from": "Ghazanfar Maqsood",
        "message": "My beloved Laraib, may your day be as radiant as your heart. Happy Birthday!",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
    },
    {
        "from": "Hurain Zahra",
        "message": "Happy Birthday Mama! I love you to the moon and back!",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
    },
    {
        "from": "Nalain Zahra",
        "message": "Mama, you are the best! Happy Birthday!",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
    },
    {
        "from": "Adan Zahra",
        "message": "Happy Birthday Mama! Big hugs and lots of smiles!",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
    },
]


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp"}
MUSIC_EXTENSIONS = {".mp3", ".wav", ".ogg", ".m4a"}


def list_directory_files(base_path: str, allowed_exts: set[str]) -> List[str]:
    if not os.path.isdir(base_path):
        return []
    file_names: List[str] = []
    for entry in os.listdir(base_path):
        _, ext = os.path.splitext(entry.lower())
        if ext in allowed_exts:
            file_names.append(entry)
    # Sort by name for deterministic display
    file_names.sort()
    return file_names


@app.route("/")
def home():
    images_dir = os.path.join(app.static_folder or "static", "images")
    music_dir = os.path.join(app.static_folder or "static", "music")

    image_files = list_directory_files(images_dir, IMAGE_EXTENSIONS)
    music_files = list_directory_files(music_dir, MUSIC_EXTENSIONS)

    return render_template(
        "index.html",
        images=image_files,
        music_files=music_files,
        wishes=WISHES,
    )


@app.post("/wish")
def add_wish():
    # Accept JSON or form-encoded
    if request.is_json:
        payload = request.get_json(silent=True) or {}
        sender_name = (payload.get("from") or payload.get("name") or "Guest").strip()
        message_text = (payload.get("message") or "").strip()
    else:
        sender_name = (request.form.get("from") or request.form.get("name") or "Guest").strip()
        message_text = (request.form.get("message") or "").strip()

    if not message_text:
        return jsonify({"ok": False, "error": "Message cannot be empty."}), 400

    if len(message_text) > 240:
        return jsonify({"ok": False, "error": "Message must be 240 characters or fewer."}), 400

    wish = {
        "from": sender_name[:60] or "Guest",
        "message": message_text,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    WISHES.append(wish)

    return jsonify({"ok": True, "wish": wish, "count": len(WISHES)})


if __name__ == "__main__":
    # Enable reloader and debug for development
    app.run(host="0.0.0.0", port=5000, debug=True)

