import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user  = 'root',
    password = '05012001'
)

cursor = db.cursor()

# Create Database : 
# cursor.execute("CREATE DATABASE Entreprise")
cursor.execute("USE Entreprise")

# Add table : 
cursor.execute("CREATE TABLE employes (id INT PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(255), prenom VARCHAR(255), salaire DECIMAL, id_service INT)")

# Add employees : 
employe_1 = "INSERT INTO employes(nom, prenom, salaire, id_service) VALUES ('Doe', 'John', 2000.5, 1)"
employe_2 = "INSERT INTO employes(nom, prenom, salaire, id_service) VALUES ('Sparrow', 'Jack', 2300.5, 2)"
employe_3 = "INSERT INTO employes(nom, prenom, salaire, id_service) VALUES ('Jones', 'David', 5000.8, 3)"
cursor.execute(employe_1)
cursor.execute(employe_2)
cursor.execute(employe_3)

request = "SELECT * FROM employes WHERE salaire > 3000;"
cursor.execute(request)
results = cursor.fetchall()
print(f'Les employés ayant un salaire supérieur à 3000 sont : {results}')

# Services : 
cursor.execute("CREATE TABLE services (id INT PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(255))")

service_1 = "INSERT INTO services(nom) VALUES ('Java')"
service_2 = "INSERT INTO services(nom) VALUES ('Python')"
service_3 = "INSERT INTO services(nom) VALUES ('C#')"
cursor.execute(service_1)
cursor.execute(service_2)
cursor.execute(service_3)

# Print all : 
request = "SELECT * FROM employes"
cursor.execute(request)
results = cursor.fetchall()
print(f'Les employés sont {results}')

request = "SELECT * FROM services"
cursor.execute(request)
results = cursor.fetchall()
print(f'Les services sont {results}')

db.commit()
cursor.close()
db.close()

class Crud:
    def __init__(self) -> None:
        pass
        
    def create_database(self, db):
        self.create_db = "CREATE " + str(db)
        self.cursor.execute(self.create_db)
        
    def create_tables(self, table):
        self.create_table = "CREATE " + str(table)
        self.cursor.execute(self.create_table)

    def change_database(self, db):
        self.change_db = "USE " + str(db)
        self.cursor.execute(self.change_db)
    
    def insert_into_table(self, table, nb_columns):
        self.insert_table = "INSERT INTO" + str(table) + "VALUES ("
        for i in range (1, nb_columns):
            exec(f"var_{i} = input('Columns ? ')") # On crée autant de variable que de colonnes
            self.insert_table += str(exec(f"var_{i}") + ",")

        self.insert_table += ")"
    
    def read_table(self, table):
        self.read = "SELECT * FROM " + str(table) + ";"
        self.cursor.execute(self.read)

    def delete_all(self, table):
        self.delete = "DELETE FROM " + str(table) + ";"
        self.cursor.execute(self.delete)