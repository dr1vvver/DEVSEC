import sqlite3

AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

def get_user(uid):
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {uid}"
    cursor.execute(query)
    return cursor.fetchall()