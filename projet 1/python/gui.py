from tkinter import *
import random
import sqlite3

'''
Réservation
- Client (ID)
- Nom (STRING)
- Date (TIMESTAMP)
- Prix (INT)
- Table (INT)
- Nombre de personne (INT)
'''
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

def createBook(nom, date ,prix, reservation, nombre_personne):
    cursor.execute(f"""INSERT INTO Clients(Nom, Date_reservation, Prix, Reservation, Nombre_personne) VALUES('{nom}', '{date}', {prix}, {reservation}, {nombre_personne});""")
    conn.commit()


def listBook():
    cursor.execute("SELECT * FROM Clients")
    rows = cursor.fetchall()
    for i in rows:
        print("-----------------------")
        print("Réservation de ", i[1], "(",i[0],")")
        print("Date de la commande:", i[2])
        print("Date de la reservation:", i[3])
        print("Prix :", i[4])
        print("Reservation :", i[5])
        print("Nombre personne :", i[6])
        print("")
    return rows

def removeBook(id):
    cursor.execute(f"""DELETE FROM Clients WHERE ID = {id};""")
    conn.commit()

def changeState(id):
    cursor.execute(f"""SELECT Etat FROM Clients WHERE ID = {id};""")
    result = cursor.fetchone()
    print(result)
    cursor.execute(f"""UPDATE Clients SET Etat = true;""")

#createBook('Richard', 95, 5, 13)
#listBook()
#removeBook(1)
#listBook()
#changeState(2)
listBook()

conn.close()

"""
def NouveauLance():
    Texte.set('text random')

# Création de la fenêtre principale (main window)
Window = Tk()

Window.title("Logiciel d'administration")
Window.geometry('1280x720')

BoutonLancer = Button(Window, text ='Lancer', command = NouveauLance)
BoutonLancer.pack(side = LEFT, padx = 5, pady = 5)

Texte = StringVar()
NouveauLance()

#print(listBook())

Window.Label(Window, text="Prénom").grid(row=0)
Window.Label(Window, text="Nom").grid(row=1)

e1 = Window.Entry(Window)
e2 = Window.Entry(Window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

LabelResultat = Label(Window, textvariable = Texte, bg ='white')
LabelResultat.pack(side = LEFT, padx = 5, pady = 5)

BoutonQuitter = Button(Window, text ='Quitter', command = Window.destroy)
BoutonQuitter.pack(side = LEFT, padx = 5, pady = 5)

Window.mainloop()
"""