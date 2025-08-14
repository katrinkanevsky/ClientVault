import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('clientvault.db')
c = conn.cursor()  # This is the correct way to create a cursor

# Create the law_firms table if it doesn't already exist
c.execute('''
CREATE TABLE IF NOT EXISTS law_firms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Add a sample law firm login (username: firm1, password: test123)
c.execute("INSERT OR IGNORE INTO law_firms (username, password) VALUES (?, ?)", ('firm1', 'test123'))

# Save and close
conn.commit()
conn.close()

print("Law firm table created and sample user added.")
