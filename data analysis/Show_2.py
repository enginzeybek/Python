import pandas as pd

veri = {
    "Kategori": ["Meyve", "Meyve", "Meyve", "Sebze", "Sebze", "İçecek", "İçecek"],

    "Ürün": ["Elma", "Muz", "Armut", "Domates", "Biber", "Kola", "Ayran"],
    "Fiyat": [3.5, 4.2, 2.9, 5.0, 4.4, 12.0, 8.0],
    "Adet": [150, 120, 200, 180, 160, 90, 140]
}

class Market:
    def __init__(self,Veri):
        self.db = pd.DataFrame(Veri)
        self.db["Toplam_Fiyat"] = self.db["Fiyat"] * self.db["Adet"]

    def enCokSatilan(self):
        id_Max = self.db["Adet"].idxmax()
        return self.db.loc[id_Max,"Ürün"],self.db.loc[id_Max,"Adet"]

    def urunEkle(self,kategori,ürün,fiyat,adet):
        yeni_satir = {
            "Kategori": kategori,
            "Ürün": ürün,
            "Fiyat": fiyat,
            "Adet": adet,
            "Toplam_Fiyat": fiyat * adet
        }
        self.db.loc[len(self.db)] = yeni_satir

    def urunSil(self,ürün):
        if ürün not in self.db["Ürün"].values:
            print("Ürün bulunamadı")
            return

        self.db = self.db[self.db["Ürün"] != ürün]
        print(f"{ürün} silindi.")
        
    def fiyatGuncelle(self,ürün,yeniFiyat):
        if ürün not in self.db["Ürün"].values:
            print(f"{ürün} bulunamadı")
            return
        
        self.df.loc[self.df["Ürün"] == ürün, "Fiyat"] = yeniFiyat

        self.df["Toplam_Fiyat"] = self.df["Fiyat"] * self.df["Adet"]

        print(f"{ürün} fiyatı güncellendi: {yeniFiyat} TL")

    def urunAra(self,arananUrun):
        if arananUrun in self.db["Ürün"].values:
            return self.db[self.db["Ürün"] == arananUrun]
        else:
            print("Ürün Bulunamadı!")
    
    def fiyatFiltre(self,minfiyat,maxfiyat):
        filtre = self.db[(self.db["Fiyat"] >= minfiyat) & (self.db["Fiyat"] <= maxfiyat)]
        return filtre



market = Market(veri)

print(f"En çok satılan ürün: {market.enCokSatilan()}")