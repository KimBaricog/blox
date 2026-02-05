from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Allow React to talk to Flask

# Connect to database
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database (create table)
@app.route("/init")
def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """)
    conn.commit()
    return "Database ready!"

# Add user
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    name = data.get("name")

    conn = get_db()
    conn.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()

    return jsonify({"message": "User added!"})

# Get all users
@app.route("/users")
def get_users():
    conn = get_db()
    users = conn.execute("SELECT * FROM users").fetchall()
    return jsonify([dict(u) for u in users])

if __name__ == "__main__":
    app.run(debug=True)
