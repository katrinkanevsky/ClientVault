import sqlite3 #here we are importing sqlite as it is a built in data base library for python

#I am learning while creating this project so I will have notes to explain 
conn = sqlite3.connect('clientvault.db') #This connects to a database file named clientvault.db. If this file doesn’t exist yet, Python will create it. conn is your connection to the database (like opening a Word doc).
c = conn.cursor() #The cursor (`c`) is like a pen — you use it to write and run SQL commands in the database.

# Create a table
#It creates a new table named clients. Each column holds one piece of client info:
c.execute('''
CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    dl_number TEXT,
    date_of_loss TEXT
)
''')
#The triple quotes (''') let you write multi-line SQL for better readability.

conn.commit()
#This tells the database to save changes. Without this line, the new table wouldn't actually be written into the file.
conn.close()
#Make sure to close the database connection when you’re done!!! This is like saving and closing a Word doc, keeps things safe and clean.

print("Database and table created successfully.")
