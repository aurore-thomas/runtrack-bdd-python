import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user  = 'root',
    password = '05012001',
    database = "LaPlateforme"
)

cursor = database.cursor()
req = "SELECT SUM(capacite) FROM salles;"
cursor.execute(req)
results = cursor.fetchall()
print(f"La superficie de toutes les salles est de {results[0][0]} m²")
cursor.close()
database.close()