import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user  = 'root',
    password = '05012001',
    database = "LaPlateforme"
)

cursor = database.cursor()
req_1 = "INSERT INTO etage(nom, numero, superficie) VALUES ('RDC', 0, 500)"
req_2 = "INSERT INTO etage(nom, numero, superficie) VALUES ('R+1', 1, 500)"

req_3 = "INSERT INTO salles(nom, id_etage, capacite) VALUES ('Lounge', 1, 100);"
req_4 = "INSERT INTO salles(nom, id_etage, capacite) VALUES ('Studio Son', 1, 5);"
req_5 = "INSERT INTO salles(nom, id_etage, capacite) VALUES ('Broadcasting', 2, 50);"
req_6 = "INSERT INTO salles(nom, id_etage, capacite) VALUES ('Bocal Peda', 2, 4);"
req_7 = "INSERT INTO salles(nom, id_etage, capacite) VALUES ('Coworking', 2, 80);"
req_8 = "INSERT INTO salles(nom, id_etage, capacite) VALUES ('Studio Video', 2, 5);"

cursor.execute(req_1)
cursor.execute(req_2)
cursor.execute(req_3)
cursor.execute(req_4)
cursor.execute(req_5)
cursor.execute(req_6)
cursor.execute(req_7)
cursor.execute(req_8)

database.commit()
database.close()
cursor.close()