# FIRST SCRPIT TO INTEGRATE PYTHON WITH SQLITE DATABASE
# Santiago Garcia Arango, August 2020

import os

# Current folder obtained with "os" library (to locate files better)
current_folder = os.path.dirname(__file__)

import sqlite3

"""
This is our first script working with a real database and using "sqlite3" as
our amazing connector to the database!!
This process is always divided into two steps:
1. Connection to the DB to give us access to the file. 
2. Cursor is the "handler" to make the connection and interactions.
"""

# Access the sqlite file... if it doesn't exists, create it
conn = sqlite3.connect(os.path.join(current_folder, 'my_email.sqlite'))
cur = conn.cursor()

# This is an extra caution if the table "Counts" already exits
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

# Access our given txt with interesting emails sent/received
fname = os.path.join(current_folder, 'mbox-short.txt')
fh = open(fname)

for line in fh:
    # Only check emails that start with "From: "
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]  # Access the specific location of that email

    # Remember that the "?" means the placeholder and gets replaced later
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()  # This returns one of the results

    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        # It is better to UPDATE it like this, other ways could cause errors
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))

    # Always commit after the SQL queries are done
    conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
