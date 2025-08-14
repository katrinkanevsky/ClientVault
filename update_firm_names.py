import sqlite3

conn = sqlite3.connect('clientvault.db')
c = conn.cursor()

# Example updates — change these to match your firms
c.execute("UPDATE law_firms SET firm_name = ? WHERE id = ?", ("Sunshine Legal Group", 1))
c.execute("UPDATE law_firms SET firm_name = ? WHERE id = ?", ("Justice & Co", 2))

conn.commit()
conn.close()

print("Firm names updated successfully.")
