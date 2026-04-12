import sqlite3

conn = sqlite3.connect("farmassist.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    query TEXT,
    response TEXT
)
""")

def save_to_db(query, response):
    cursor.execute("INSERT INTO history VALUES (?, ?)", (query, response))
    conn.commit()
