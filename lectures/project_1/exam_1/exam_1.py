# FIRST EXAM FOR THE COURSERA DATABASE WITH PYTHON COURSE
# Santiago Garcia Arango, August 2020

import os

# Current folder obtained with "os" library (to locate files better)
current_folder = os.path.dirname(__file__)

import sqlite3
import re

# Access the sqlite file... if it doesn't exists, create it
conn = sqlite3.connect(os.path.join(current_folder, 'exam_1.sqlite'))
cur = conn.cursor()

# This is an extra caution if the table "Counts" already exits
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Access our given txt with interesting emails sent/received
fname = os.path.join(current_folder, 'mbox.txt')
fh = open(fname)

for line in fh:
    # Only check emails that start with "From: "
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]  # Access the specific location of that email
    org = re.findall('@(.+)', email)[0]  # Access only the org name (not ...@)

    # Remember that the "?" means the placeholder and gets replaced later
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()  # This returns one of the results

    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        # It is better to UPDATE it like this, other ways could cause errors
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))

# Always commit after the SQL queries are done
conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
