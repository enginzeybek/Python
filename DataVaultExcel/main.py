import pandas as pd

class DataVaultExcel:

    def __init__(self):
        self.db = pd.DataFrame({
            "id": [],
            "name": [],
            "category": [],
            "price": []
        })

    def load_from_excel(self,file_path):
        self.db = pd.read_excel(file_path)

    def save_to_excel(self,file_path):
        self.db.to_excel(file_path,index = False)

    def add_row(self,id,name,category,price):
        newRow = {
            "id": id,
            "name": name,
            "category": category,
            "price": price
        }

        self.db.loc[len(self.db)] = newRow

    def update_price(self,id,newprice):
        
        self.db.loc[self.db["id"] == id,"price"] = newprice

    def delete_row(self,id):
        self.db = self.db.loc[self.db["id"] != id]


if __name__ == "__main__":
    vault = DataVaultExcel()
    
    #vault.load_from_excel("products.xlsx")
    #vault.add_row(2, "Kulaklık", "Elektronik", 25)
    #vault.save_to_excel("products.xlsx")

    #vault.load_from_excel("products.xlsx")
    #vault.update_price(1,500)
    #vault.save_to_excel("products.xlsx")

    vault.load_from_excel("products.xlsx")
    vault.delete_row(2)
    vault.save_to_excel("products.xlsx")

