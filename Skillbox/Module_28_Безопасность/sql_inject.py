import json
import sqlite3
from flask import Flask, g, request


# SQL-command for add data: insert into 'users' (name, role) values ("Leo", "user");
# SQL-inject from Postman:
# {
#   "name": "Hacker\", \"user\"); update 'users' set role=\"admin\" where name=\"John\";--",
#   "role": "user"
# }
app = Flask(__name__)

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("sqlitedb.db")
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

@app.before_request
def create_table():
    with sqlite3.connect("sqlitedb.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users (name VARCHAR(255), role VARCHAR(255))"""
        )

@app.route("/users", methods=["GET", "POST"])
def users():
    conn = get_db()
    cursor = conn.cursor()
    if request.method == "GET":
        result = cursor.execute("SELECT * FROM users")
        return json.dumps(result.fetchall()), 200
    elif request.method == "POST":
        data = request.get_json()
        # Vulnerable code
        cursor.executescript(
            f"""INSERT INTO 'users' (name, role) VALUES ("{data['name']}", "{data['role']}");"""
        )

        # Solution
        # cursor.execute(
        #     """INSERT INTO 'users' (name, role) VALUES (?, ?)""",
        #     (data['name'], data['role'])
        # )
        conn.commit()
        return "OK", 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)


