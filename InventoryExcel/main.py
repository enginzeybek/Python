import pandas as pd
import os

class inventory:
    
    def __init__(self):
        if os.path.exists("inventory.xlsx"):
            self.df = pd.read_excel("inventory.xlsx")
        else:
            self.df = pd.DataFrame({
            "Id":[],
            "ProductName":[],
            "Price":[],
            "Stock":[]
            })
            self.df.to_excel("inventory.xlsx",index=False)

    def AddProduct(self,Id,ProductName,Price,Stock):
        new_line = {
            "Id":Id,
            "ProductName":ProductName,
            "Price":Price,
            "Stock":Stock
        }
        self.df.loc[len(self.df)] = new_line
        self.df.to_excel("inventory.xlsx",index=False)
    
    def ProductList(self):
        print(self.df)

    def RemoveProduct(self,id):
        self.df = self.df[self.df["Id"] != id]
        self.df.to_excel("inventory.xlsx", index=False)

    def UpdateProductName(self,id,productname):
        self.df.loc[self.df("Id") == id, "ProductName"] = productname
        self.df.to_excel("inventory.xlsx", index=False)

    def UpdatePrice(self,id,price):
        self.df.loc[self.df["Id"] == id, "Price"] = price
        self.df.to_excel("inventory.xlsx", index=False)

    def UpdateStock(self,id,stock):
        self.df.loc[self.df["Id"] == id, "Stock"] = stock
        self.df.to_excel("inventory.xlsx", index=False)

data = inventory()

data.AddProduct(1, "Laptop", 2999.99, 250)
data.ProductList()



        

