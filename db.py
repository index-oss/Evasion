import sqlite3

conn = sqlite3.connect("securestack.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS scans(
id INTEGER PRIMARY KEY,
url TEXT,
result TEXT
)
""")

def save_scan(url, result):
    cur.execute("INSERT INTO scans(url,result) VALUES(?,?)",(url,result))
    conn.commit()
