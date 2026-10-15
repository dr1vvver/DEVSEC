import sqlite3
AWS_ACCESS_KEY = "NEWPACCESSKEY"

def get_user(uid):
    conn = sqlite3.connect("db.sqlite")
    return conn.execute(f"SELECT * FROM users WHERE id={uid}").fetchone()
