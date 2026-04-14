import pandas as pd
import os

file_name = "inventory.xlsx"

if not os.path.exists(file_name):
    df = pd.DataFrame(
        columns = ["Id","Name","Price","Stock"]
    )
    df.to_excel(file_name,index=False)

class Inventory:
    def __init__(self):
        self.file_name = "inventory.xlsx"
        self.df = pd.read_excel(self.file_name)

    def add_product(self,name,price,stock):
        new_id = 1 if self.df.empty else self.df["Id"].max() + 1

        new_line = {
            "Id":new_id,
            "Name":name,
            "Price":price,
            "Stock":stock
        }
        self.df = pd.concat([self.df, pd.DataFrame([new_line])], ignore_index=True)

        self.df.to_excel(self.file_name, index=False)

    def list_products(self):
        if self.df.empty:
            print("Hiç ürün yok.")
        else:
            for index, row in self.df.iterrows():
                print("Id:", row["Id"])
                print("Name:", row["Name"])
                print("Price:", row["Price"])
                print("Stock:", row["Stock"])
                print("----------------------")
    
    def delete_product(self, product_id):
        # uzun versiyon
        if self.df.empty:
            print("Silinecek ürün yok.")
            return

        # Ürün var mı kontrol et
        product_exists = False

        for index, row in self.df.iterrows():
            if row["Id"] == product_id:
                product_exists = True
                self.df = self.df.drop(index)
                break

        if product_exists:
            self.df.to_excel(self.file_name, index=False)
            print("Ürün silindi.")
        else:
            print("Ürün bulunamadı.")
        # Kısa versiyon
        self.df = self.df[self.df["Id"] != product_id]
        self.df.to_excel(self.file_name, index=False)

    def update_product(self, product_id, name=None, price=None, stock=None):
        index = self.df[self.df["Id"] == product_id].index

        if len(index) == 0:
            print("Ürün bulunamadı.")
            return

        if name is not None:
            self.df.loc[index, "Name"] = name

        if price is not None:
            self.df.loc[index, "Price"] = price

        if stock is not None:
            self.df.loc[index, "Stock"] = stock

        self.df.to_excel(self.file_name, index=False)


inv = Inventory()

#inv.add_product("Laptop", 15000, 5)
#inv.add_product("Mouse", 200, 20)

inv.list_products()

#print(inv.df)