import sqlite3
conn = sqlite3.connect('clientvault.db')
c = conn.cursor()

#This will add a law firm id column if it doesnt exist
try: 
    c.execute("ALTER TABLE clients ADD COLUMN law_firm_id INTEGER DEFAULT 1")
    print("Cloumn 'law_firm_id' added successfully.")
except Exception as e:
    print("Could not add column:", e)

conn.commit()
conn.close()