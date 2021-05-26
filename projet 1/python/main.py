'''
Réservation
- Client (ID)
- Nom (STRING)
- Date (TIMESTAMP)
- Prix (INT)
- Table (INT)
- Nombre de personne (INT)
'''

import sqlite3

conn = sqlite3.connect('VanillaUnicorn.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clients(
     ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     Nom TEXT,
     Date DATETIME DEFAULT CURRENT_TIMESTAMP,
     Prix INTEGER,
     Reservation INTEGER,
     Nombre_personne INTEGER
)
""")


def createBook(nom, prix, reservation, nombre_personne):
    cursor.execute(f"""INSERT INTO Clients(Nom, Prix, Reservation, Nombre_personne) VALUES('{nom}', {prix}, {reservation}, {nombre_personne});""")
    conn.commit()


def listBook():
    cursor.execute("SELECT * FROM Clients")
    rows = cursor.fetchall()
    return rows


createBook('Richard', 95, 5, 13)

x = listBook()
for i in x:
    print(i)

conn.close()