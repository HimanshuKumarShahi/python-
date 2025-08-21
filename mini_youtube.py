# app.py
# Mini YouTube Clone with Flask (single file)

import io
import os
import re
import sqlite3
import mimetypes
from datetime import datetime
from pathlib import Path
from flask import (
    Flask, request, redirect, url_for, send_file, abort,
    render_template_string, flash
)
from werkzeug.utils import secure_filename

# ---------------------- Config ----------------------
APP_TITLE = "PyTube (mini)"
UPLOAD_DIR = Path("uploads")
DB_PATH = Path("videos.db")
MAX_CONTENT_LENGTH = 2 * 1024 * 1024 * 1024  # 2 GB
ALLOWED_EXTS = {".mp4", ".webm", ".mov", ".avi", ".mkv", ".m4v", ".mpg", ".mpeg", ".wmv"}

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH
app.secret_key = "dev-secret-change-me"  # for flash messages


# ---------------------- DB Helpers ----------------------
def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                title TEXT NOT NULL,
                description TEXT DEFAULT '',
                uploaded_at TEXT NOT NULL
            )
        """)
        conn.commit()

# ---------------------- Utilities ----------------------
def is_allowed(filename: str) -> bool:
    ext = Path(filename).suffix.lower()
    return ext in ALLOWED_EXTS

def human_dt(dt_str: str) -> str:
    try:
        dt = datetime.fromisoformat(dt_str)
        return dt.strftime("%b %d, %Y %H:%M")
    except Exception:
        return dt_str

def sanitize_title(s: str) -> str:
    s = s.strip()
    s = re.sub(r"\s+", " ", s)
    return s if s else "Untitled"

# ---------------------- TEMPLATES ----------------------
BASE_HTML = """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{{ title or 'PyTube' }}</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
  body{margin:0;background:#0b0f14;color:#ecf2f8;font-family:sans-serif}
  a{color:#59a6ff;text-decoration:none}
  .container{max-width:1100px;margin:0 auto;padding:20px}
  header{display:flex;gap:16px;align-items:center;justify-content:space-between;margin-bottom:18px}
  .brand{display:flex;gap:10px;align-items:center}
  .logo{width:36px;height:36px;border-radius:10px;background:linear-gradient(135deg,#59a6ff,#8b5dff);display:flex;align-items:center;justify-content:center;color:white;font-weight:700}
  input,textarea{width:100%;background:#0c1218;border:1px solid #1b2632;color:#ecf2f8;padding:10px;border-radius:8px}
  button,.btn{background:#59a6ff;border:none;color:#001628;padding:10px 14px;border-radius:8px;font-weight:700;cursor:pointer}
  .btn-secondary{background:#1b2632;color:#ecf2f8}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px}
  .card{background:#10161d;border-radius:12px;overflow:hidden}
  .thumb{aspect-ratio:16/9;background:#0c1218;display:flex;align-items:center;justify-content:center;color:#567;font-size:14px}
  .content{padding:12px}
  .muted{color:#8aa0b2;font-size:13px}
  .flash{background:#122;border:1px solid #244;padding:10px;border-radius:8px;margin:10px 0}
  .watch video{width:100%;max-height:70vh;background:#000;border-radius:12px}
</style>
</head>
<body>
  <div class="container">
    <header>
      <div class="brand">
        <div class="logo">▶</div>
        <a href="{{ url_for('home') }}"><strong>PyTube</strong></a>
      </div>
      <form class="search" action="{{ url_for('home') }}" method="get">
        <input type="text" name="q" placeholder="Search..." value="{{ q or '' }}">
        <button type="submit">Search</button>
        <a class="btn btn-secondary" href="{{ url_for('upload') }}">Upload</a>
      </form>
    </header>

    {% with messages = get_flashed_messages() %}
      {% if messages %}
        {% for m in messages %}
          <div class="flash">{{ m }}</div>
        {% endfor %}
      {% endif %}
    {% endwith %}

    {% block body %}{% endblock %}
  </div>
</body>
</html>
"""

HOME_HTML = """
{% extends "base.html" %}
{% block body %}
  {% if q %}
    <p class="muted">Search results for: <strong>{{ q }}</strong></p>
  {% endif %}
  {% if not videos %}
    <p>No videos yet. <a href="{{ url_for('upload') }}">Upload one</a>.</p>
  {% else %}
    <div class="grid">
      {% for v in videos %}
        <div class="card">
          <a href="{{ url_for('watch', video_id=v['id']) }}">
            <div class="thumb">{{ v['title']|e }}</div>
          </a>
          <div class="content">
            <a href="{{ url_for('watch', video_id=v['id']) }}"><strong>{{ v['title']|e }}</strong></a>
            <div class="muted">{{ v['description']|e }}</div>
            <div class="muted">Uploaded {{ human_dt(v['uploaded_at']) }}</div>
          </div>
        </div>
      {% endfor %}
    </div>
  {% endif %}
{% endblock %}
"""

UPLOAD_HTML = """
{% extends "base.html" %}
{% block body %}
  <h2>Upload a video</h2>
  <form action="{{ url_for('upload') }}" method="post" enctype="multipart/form-data">
    <input type="file" name="file" accept="video/*" required><br><br>
    <input type="text" name="title" placeholder="Title" required><br><br>
    <textarea name="description" rows="3" placeholder="Description (optional)"></textarea><br><br>
    <button type="submit">Upload</button>
    <a class="btn btn-secondary" href="{{ url_for('home') }}">Cancel</a>
    <p class="muted">Allowed: {{ ', '.join(exts) }}</p>
  </form>
{% endblock %}
"""

WATCH_HTML = """
{% extends "base.html" %}
{% block body %}
  {% if video %}
    <div class="watch">
      <video controls preload="metadata">
        <source src="{{ url_for('stream', filename=video['filename']) }}" type="{{ mimetype }}">
      </video>
      <h2>{{ video['title']|e }}</h2>
      <div class="muted">Uploaded {{ human_dt(video['uploaded_at']) }}</div>
      <p>{{ video['description']|e }}</p>
      <a class="btn btn-secondary" href="{{ url_for('home') }}">← Back</a>
    </div>
  {% else %}
    <p class="danger">Video not found.</p>
  {% endif %}
{% endblock %}
"""

# ---------------------- Routes ----------------------
@app.route("/")
def home():
    q = request.args.get("q", "").strip()
    with db() as conn:
        if q:
            videos = conn.execute(
                "SELECT * FROM videos WHERE title LIKE ? OR description LIKE ? ORDER BY id DESC",
                (f"%{q}%", f"%{q}%")
            ).fetchall()
        else:
            videos = conn.execute("SELECT * FROM videos ORDER BY id DESC").fetchall()
    return render_template_string(HOME_HTML, title=APP_TITLE, videos=videos, q=q, human_dt=human_dt)

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template_string(UPLOAD_HTML, title=f"Upload • {APP_TITLE}", exts=list(ALLOWED_EXTS))

    f = request.files.get("file")
    title = sanitize_title(request.form.get("title", ""))
    description = (request.form.get("description") or "").strip()

    if not f or f.filename == "":
        flash("Please choose a file.")
        return redirect(url_for("upload"))

    if not is_allowed(f.filename):
        flash(f"File type not allowed. Allowed: {', '.join(sorted(ALLOWED_EXTS))}")
        return redirect(url_for("upload"))

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    safe_name = secure_filename(f.filename)
    base, ext = os.path.splitext(safe_name)
    candidate = safe_name
    i = 1
    while (UPLOAD_DIR / candidate).exists():
        candidate = f"{base}_{i}{ext}"
        i += 1

    save_path = UPLOAD_DIR / candidate
    f.save(save_path)

    with db() as conn:
        conn.execute(
            "INSERT INTO videos(filename,title,description,uploaded_at) VALUES (?,?,?,?)",
            (candidate, title, description, datetime.utcnow().isoformat(timespec="seconds")),
        )
        conn.commit()

    flash("Upload successful!")
    return redirect(url_for("home"))

@app.route("/watch/<int:video_id>")
def watch(video_id: int):
    with db() as conn:
        v = conn.execute("SELECT * FROM videos WHERE id=?", (video_id,)).fetchone()
    if not v:
        abort(404)
    mimetype = mimetypes.guess_type(v["filename"])[0] or "video/mp4"
    return render_template_string(WATCH_HTML, title=f"{v['title']} • {APP_TITLE}", video=v, mimetype=mimetype, human_dt=human_dt)

@app.route("/stream/<path:filename>")
def stream(filename: str):
    file_path = UPLOAD_DIR / filename
    if not file_path.exists():
        abort(404)

    mime = mimetypes.guess_type(str(file_path))[0] or "video/mp4"
    file_size = file_path.stat().st_size
    range_header = request.headers.get("Range", None)

    if range_header:
        m = re.match(r"bytes=(\d*)-(\d*)", range_header)
        if m:
            start_str, end_str = m.groups()
            start = int(start_str) if start_str else 0
            end = int(end_str) if end_str else file_size - 1
            length = end - start + 1
            with open(file_path, "rb") as f:
                f.seek(start)
                data = f.read(length)
            rv = send_file(io.BytesIO(data), mimetype=mime, as_attachment=False)
            rv.status_code = 206
            rv.headers.add("Content-Range", f"bytes {start}-{end}/{file_size}")
            rv.headers.add("Accept-Ranges", "bytes")
            rv.headers.add("Content-Length", str(length))
            return rv

    return send_file(file_path, mimetype=mime, as_attachment=False)

# ---------------------- Startup ----------------------
def ensure_fs():
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    init_db()

@app.before_request
def _before():
    ensure_fs()

from jinja2 import DictLoader
app.jinja_loader = DictLoader({
    "base.html": BASE_HTML,
    "home.html": HOME_HTML,
    "upload.html": UPLOAD_HTML,
    "watch.html": WATCH_HTML
})

if __name__ == "__main__":
    ensure_fs()
    app.run(debug=True)
