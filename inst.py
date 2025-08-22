import os
import sqlite3
from datetime import datetime
from flask import Flask, request, redirect, url_for, render_template_string, send_from_directory, flash

# ------------------- CONFIG -------------------
app = Flask(__name__)
app.secret_key = "supersecret"
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
DB_FILE = "instaclone.db"


# ------------------- DATABASE -------------------
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()

        c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE
        )""")

        c.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            caption TEXT,
            media TEXT,
            created_at TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )""")
        conn.commit()


def get_user(username="demo"):
    """Return a demo user, create if not exists"""
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()
        if not user:
            c.execute("INSERT INTO users(username) VALUES (?)", (username,))
            conn.commit()
            user_id = c.lastrowid
            return {"id": user_id, "username": username}
        return dict(user)


def add_post(user_id, caption, media):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            "INSERT INTO posts(user_id, caption, media, created_at) VALUES (?,?,?,?)",
            (user_id, caption, media, datetime.utcnow().isoformat(timespec="seconds")),
        )
        conn.commit()


def get_feed():
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("""
            SELECT posts.id, posts.caption, posts.media, posts.created_at,
                   users.username
            FROM posts
            JOIN users ON posts.user_id = users.id
            ORDER BY posts.id DESC
        """).fetchall()
        return [dict(r) for r in rows]


# ------------------- ROUTES -------------------
@app.route("/")
def home():
    feed = get_feed()
    return render_template_string(HOME_TEMPLATE, feed=feed)


@app.route("/upload", methods=["GET", "POST"])
def upload():
    user = get_user()
    if request.method == "POST":
        f = request.files["file"]
        caption = request.form.get("caption", "")
        if f and f.filename:
            save_path = os.path.join(UPLOAD_FOLDER, f.filename)
            f.save(save_path)
            add_post(user["id"], caption, f.filename)
            flash("Upload successful!")
            return redirect(url_for("home"))
        else:
            flash("No file selected!")
    return render_template_string(UPLOAD_TEMPLATE)


@app.route("/reels")
def reels():
    feed = get_feed()
    reels = [f for f in feed if f["media"].lower().endswith(".mp4")]
    return render_template_string(REELS_TEMPLATE, reels=reels)


@app.route("/search")
def search():
    q = request.args.get("q", "")
    feed = get_feed()
    if q:
        feed = [f for f in feed if q.lower() in f["caption"].lower()]
    return render_template_string(SEARCH_TEMPLATE, feed=feed, query=q)


@app.route("/user/<username>")
def user_profile(username):
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("""
            SELECT posts.id, posts.caption, posts.media, posts.created_at,
                   users.username
            FROM posts
            JOIN users ON posts.user_id = users.id
            WHERE users.username = ?
            ORDER BY posts.id DESC
        """, (username,)).fetchall()
        feed = [dict(r) for r in rows]
    return render_template_string(PROFILE_TEMPLATE, feed=feed, username=username)


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


# ------------------- HTML TEMPLATES -------------------
HOME_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>InstaClone • Home</title>
    <style>
        body { font-family: sans-serif; margin: 0; background: #fafafa; }
        header { padding: 1em; background: white; display: flex; justify-content: space-around; position: sticky; top: 0; }
        .post { background: white; margin: 1em auto; padding: 1em; max-width: 500px; border-radius: 10px; }
        img, video { width: 100%; border-radius: 10px; }
    </style>
</head>
<body>
<header>
    <a href="/">Home</a>
    <a href="/search">Search</a>
    <a href="/reels">Reels</a>
    <a href="/upload">Upload</a>
</header>

{% for post in feed %}
<div class="post">
    <b>@{{ post.username }}</b> <small>{{ post.created_at }}</small>
    <p>{{ post.caption }}</p>
    {% if post.media.endswith(".mp4") %}
        <video controls src="{{ url_for('uploaded_file', filename=post.media) }}"></video>
    {% else %}
        <img src="{{ url_for('uploaded_file', filename=post.media) }}">
    {% endif %}
</div>
{% endfor %}
</body>
</html>
"""

UPLOAD_TEMPLATE = """
<!doctype html>
<html>
<head><title>Upload</title></head>
<body>
<h2>Upload Post/Reel</h2>
<form method="POST" enctype="multipart/form-data">
    Caption: <input type="text" name="caption"><br><br>
    File: <input type="file" name="file"><br><br>
    <button type="submit">Upload</button>
</form>
</body>
</html>
"""

REELS_TEMPLATE = """
<!doctype html>
<html>
<head>
<title>Reels</title>
<style>
body { margin:0; background:black; overflow-y: scroll; scroll-snap-type: y mandatory; }
.reel { height:100vh; width:100%; display:flex; justify-content:center; align-items:center; scroll-snap-align: start; }
video { height:100%; aspect-ratio: 9 / 16; object-fit: cover; border-radius: 8px; }
</style>
</head>
<body>
{% for r in reels %}
<div class="reel">
    <video src="{{ url_for('uploaded_file', filename=r.media) }}" autoplay muted loop controls></video>
</div>
{% endfor %}
</body>
</html>
"""

SEARCH_TEMPLATE = """
<!doctype html>
<html>
<head><title>Search</title></head>
<body>
<form>
    <input type="text" name="q" value="{{ query }}" placeholder="Search captions...">
    <button type="submit">Search</button>
</form>
<hr>
{% for post in feed %}
<div>
    <b>@{{ post.username }}</b>: {{ post.caption }}
</div>
{% endfor %}
</body>
</html>
"""

PROFILE_TEMPLATE = """
<!doctype html>
<html>
<head><title>@{{ username }}</title></head>
<body>
<h2>Profile: @{{ username }}</h2>
{% for post in feed %}
<div>
    <p>{{ post.caption }}</p>
    {% if post.media.endswith(".mp4") %}
        <video src="{{ url_for('uploaded_file', filename=post.media) }}" controls width="300"></video>
    {% else %}
        <img src="{{ url_for('uploaded_file', filename=post.media) }}" width="300">
    {% endif %}
</div>
{% endfor %}
</body>
</html>
"""


# ------------------- START -------------------
if __name__ == "__main__":
    init_db()

    # Add demo content if empty
    user = get_user()
    if not get_feed():
        sample_media = [
            ("Beautiful mountain view", "photo1.jpg"),
            ("Sunny beach vibes", "photo2.jpg"),
            ("Funny cat reel", "reel1.mp4"),
            ("Nature walk", "reel2.mp4"),
        ]
        for cap, media in sample_media:
            if os.path.exists(os.path.join(UPLOAD_FOLDER, media)):
                add_post(user["id"], cap, media)

    app.run(debug=True)
