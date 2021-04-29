import sqlite3

db = sqlite3.connect('users.db')

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
""")

print("Database conectado!")
