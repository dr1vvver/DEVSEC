import os
import sqlite3

AWS_ACCESS_KEY = os.environ["AKIAIOSFODNN7EXAMPLE"]

def get_user(uid: int):
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (uid,))
    return cursor.fetchall()