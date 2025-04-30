import tkinter as tk
from tkinter import ttk
import utils
class MainDB():
    def __init__(self, win):
        self.objdb = utils.SysDb() # database access
        self.window = win # window

        # visual table
        self.treeProducts = ttk.Treeview(self.window, columns=("Product ID", "Name", "Price")) # column names

        # entry labels for indication
        self.treeProducts.heading("Product ID", text= "ID: ")
        self.treeProducts.heading("Name", text="Name: ")
        self.treeProducts.heading("Price", text="Price: ")
        self.treeProducts.pack() 

        # product database entry
        self.name = tk.Label(self.window, text="Name: ")
        self.name.pack()
        self.entryname = tk.Entry(self.window)
        self.entryname.pack()
        self.price = tk.Label(self.window, text="Price: ")
        self.price.pack()
        self.entryprice = tk.Entry(self.window)
        self.entryprice.pack()
        self.showWindow()

        # buttons for item management
        self.btn_register = tk.Button(self.window, text="Register", command=self.registerProduct)
        self.btn_register.pack()
        self.btn_update = tk.Button(self.window, text = "Update", command=self.updateProduct)
        self.btn_update.pack()
        self.btn_delete = tk.Button(self.window, text="Delete", command=self.deleteProduct)
        self.btn_delete.pack()

    def showWindow(self): # update the treeview and show the items
        try:
            self.treeProducts.delete(*self.treeProducts.get_children())
            products = self.objdb.selectAllProducts()
            for product in products:
                self.treeProducts.insert("", tk.END, values=product)  
        except:
            print("Failed to show products.")

    def registerProduct(self): # function to project register
        try: 
            name = self.entryname.get()
            price = float(self.entryprice.get())
            self.objdb.insertData(name, price)
            self.showWindow()
            self.entryname.delete(0, tk.END)
            self.entryprice.delete(0, tk.END)
            print("Product successfully registered.")
        except:
            print("Failed to register product.")

    def updateProduct(self): # function to project update
        try:
            selected_item = self.treeProducts.selection()
            if not selected_item:
                print("No item selected.")
                return
            print("Selection info: ", selected_item)
            item = self.treeProducts.item(selected_item)
            print("Item info: ", item)
            product = item["values"]
            print("", product)
            product_id = product[0]
            name = self.entryname.get()
            price = float(self.entryprice.get())
            self.objdb.updateProducts(product_id, name, price)
            self.showWindow()

            self.entryname.delete(0, tk.END)
            self.entryprice.delete(0, tk.END)
        except:
            print("Failed to update the item.")

    def deleteProduct(self): # function to project delete
        try:
            selected_item = self.treeProducts.selection()
            if not selected_item:
                print("No item selected.")
                return
            item = self.treeProducts.item(selected_item)
            product = item["values"]
            product_id = product[0]
            self.objdb.deleteProduct(product_id)
            self.showWindow()
        except:
            print("Failed to delete item.")
window = tk.Tk() # main window
product_app = MainDB(window) # connect with the GUI and show the content in the window
window.geometry("1280x720") # window size
window.mainloop() # keep the window open until the user close it