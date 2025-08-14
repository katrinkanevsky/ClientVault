import sqlite3

conn = sqlite3.connect('clientvault.db')
c = conn.cursor()

try:
    c.execute("ALTER TABLE law_firms ADD COLUMN firm_name TEXT")
    print("Column 'firm_name' added successfully.")
except Exception as e:
    print("Could not add column:", e)

conn.commit()
conn.close()

