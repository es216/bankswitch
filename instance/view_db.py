import sqlite3
import json

# connect to the database
conn = sqlite3.connect("banks.db")
cursor = conn.cursor()

# see all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

# see all banks
cursor.execute("SELECT * FROM bank;")
rows = cursor.fetchall()

# print each bank nicely
for row in rows:
    # row order: id, name, min_deposit, min_direct_debits, switch_bonus, excludes
    print({
        "id": row[0],
        "name": row[1],
        "min_deposit": row[2],
        "min_direct_debits": row[3],
        "switch_bonus": row[4],
        "excludes": json.loads(row[5]) if row[5] else []
    })

conn.close()