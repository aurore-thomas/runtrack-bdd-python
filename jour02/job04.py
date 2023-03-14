import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user  = 'root',
    password = '05012001',
    database = "LaPlateforme"
)

cursor = database.cursor()
req = "SELECT nom, capacite FROM salles"
cursor.execute(req)
results = cursor.fetchall()
print(results)
cursor.close()