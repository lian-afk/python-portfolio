import sqlite3
class SysDb(): # system database
    def __init__(self):
        self.createTable()

    def openConnection(self): # open connection with the database
        try:
            self.connect = sqlite3.connect("database.db")
        except sqlite3.Error as error:
            print("Failed to connect with the database.")
    def createTable(self): # create the table for product registration
        self.openConnection()
        create_table_query = """CREATE TABLE IF NOT EXISTS products(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                price REAL NOT NULL)"""
        try:
            cursor = self.connect.cursor()
            cursor.execute(create_table_query)
        except sqlite3.Error as error:
            print("Failed to create table.")
        finally:
            if self.connect:
                cursor.close()
                self.connect.close()
                print("SQLite connection closed.")

    def insertData(self, name, price): # insert items into the table
        self.openConnection()
        insert_query = """ INSERT INTO products(name, price) VALUES (?, ?)"""
        try:
            cursor = self.connect.cursor()
            cursor.execute(insert_query, (name, price))
            print("Product successfully registered.")
            self.connect.commit()
        except sqlite3.Error as error:
            print("Failed to register product.")
        finally:
            if self.connect:
                cursor.close()
                self.connect.close()
                print("SQLite connection closed.")

    def selectAllProducts(self): # list all registered products using select *
        self.openConnection()
        select_query = """SELECT * FROM products"""
        products = []
        try:
            cursor = self.connect.cursor()
            cursor.execute(select_query)
            products = cursor.fetchall() 
        except  sqlite3.Error as error:
                print("Failed to return products.")
        finally:
            if self.connect:
                cursor.close()
                self.connect.close()
                print("SQLite connection closed.")
        return products
    
    def updateProducts(self, id, name, price): # update the item data registered
        self.openConnection()
        update_query = """UPDATE products SET name = ?, price = ? WHERE id = ?"""
        try:
            cursor = self.connect.cursor()
            cursor.execute(update_query, (name, price, id))
            self.connect.commit()
            print("Product successfully updated.")
        except sqlite3.Error as error:
            print("Failed to update product.")
        finally:    
            if self.connect:
                cursor.close()
                self.connect.close()
                print("SQLite connection closed.")

    def deleteProduct(self, id): # delete the item using the id as a parameter
        self.openConnection()
        delete_query = """DELETE FROM products WHERE id=?"""
        try:
            cursor = self.connect.cursor()
            cursor.execute(delete_query, (id,))
            self.connect.commit()
        except sqlite3.Error as error:
            print("Failed to delete product.")
        finally:    
            if self.connect:
                cursor.close()
                self.connect.close()
                print("SQLite connection closed.")