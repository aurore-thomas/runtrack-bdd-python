import mysql.connector

db = mysql.connector.connect(
        host = "localhost",
        user  = 'root',
        password = '05012001'
        )

class Crud:
    def __init__(self):
        self.cursor = db.cursor()
        
    def create_database(self, name):
        self.create_db = "CREATE " + str(name)
        print(self.create_db)
        self.cursor.execute(self.create_db)
        db.commit()
        self.cursor.close()
        db.close()
        
    def create_tables(self, table):
        self.create_table = "CREATE " + str(table) + ";"
        self.cursor.execute(self.create_table)
        db.commit()
        self.cursor.close()
        db.close()

    def change_database(self, name):
        self.change_db = "USE " + str(name)
        self.cursor.execute(self.change_db)
        db.commit()
        self.cursor.close()
        db.close()
    
    def insert_into_table(self, table, nb_columns):
        self.insert_table = "INSERT INTO" + str(table) + "VALUES ("
        for i in range (1, nb_columns):
            exec(f"var_{i} = input('Columns ? ')") # On crée autant de variable que de colonnes
            self.insert_table += str(exec(f"var_{i}") + ",")


        self.insert_table += ")"
        db.commit()
        self.cursor.close()
        db.close()
    
    def read_table(self, table):
        self.read = "SELECT * FROM " + str(table) + ";"
        self.cursor.execute(self.read)
        db.commit()
        self.cursor.close()
        db.close()

    def delete_all(self, table):
        self.delete = "DELETE FROM " + str(table) + ";"
        self.cursor.execute(self.delete)
        db.commit()
        self.cursor.close()
        db.close()

zoo = Crud()
zoo.create_database("zoo")
# zoo.create_tables()