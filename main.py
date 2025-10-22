import utils.transport
import utils.session
from flask import Flask, render_template, request, redirect
import sqlite3
import random
import string
import os

app = Flask(__name__)

DB_NAME = "urls.db"

# ✅ Ensure database and table exist
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            short_url TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ✅ Generate a random short code
def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


# ✅ Main route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        long_url = request.form["long_url"].strip()

        # Fix logic — use 'and' instead of 'or'
        if not (long_url.startswith("http://") or long_url.startswith("https://")):
            long_url = f"https://{long_url}"

        # Generate unique short code
        short_url = generate_short_url()
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Check for collision
        cursor.execute("SELECT * FROM urls WHERE short_url = ?", (short_url,))
        while cursor.fetchone():
            short_url = generate_short_url()

        cursor.execute("INSERT INTO urls (url, short_url) VALUES (?, ?)", (long_url, short_url))
        conn.commit()
        conn.close()

        full_short_url = request.url_root + short_url
        return render_template("index.html", shortened_url=full_short_url)

    return render_template("index.html", shortened_url=None)


# ✅ Redirection route
@app.route("/<short_url>")
def redirect_to_original(short_url):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM urls WHERE short_url = ?", (short_url,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return redirect(result[0])
    else:
        return "<h3>❌ Invalid or expired short URL.</h3>", 404


if __name__ == "__main__":
    app.run(debug=True)
