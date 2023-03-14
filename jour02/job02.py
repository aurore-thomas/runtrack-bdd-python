import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user  = 'root',
    password = '05012001',
    database = "LaPlateforme"
)

cursor = database.cursor()

req_1 = "CREATE TABLE etage (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), numero INT, superficie INT);"
req_2 = "CREATE TABLE salles (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), id_etage INT, capacite INT);"

cursor.execute(req_1)
cursor.execute(req_2)
results = cursor.fetchall()
print(results)
cursor.close()