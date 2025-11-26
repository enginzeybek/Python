import pandas as pd

veri = {
    "Ürün": ["Elma", "Armut", "Muz", "Kiraz", "Üzüm"],
    "Fiyat": [3.5, 2.8, 4.1, 5.0, 3.0],
    "Adet": [150, 200, 120, 300, 100]
}


class Market:
    def __init__(self,data):
        self.df = pd.DataFrame(data)
        self.df["Toplam_Fiyat"] = self.df["Fiyat"] * self.df["Adet"]

    def enPahaliUrun(self):
        id_max = self.df["Toplam_Fiyat"].idxmax()
        return self.df.loc[id_max,"Ürün"],self.df.loc[id_max,"Toplam_Fiyat"]
    
    def ortalamaAdetUstu(self):
        ort_adet = self.df["Adet"].mean()
        return self.df[self.df["Adet"] > ort_adet ] 
    
    def fiyatBuyukUcBucuk(self):
        buyuk_uc_buyuk_fiyat = self.df["Fiyat"] > 3.5
        return self.df[filter][["Ürün", "Fiyat"]]


market = Market(veri)

# Sütun adlarını değiştir
market.df.columns = [col.replace(" ", "_") for col in market.df.columns]

print("En pahalı ürün ve toplam fiyatı:", market.enPahaliUrun())
print("Ortalama adetten fazla olan ürünler:")
print(market.ortalamaAdetUstu())
print("---------------------------------------------------------------")
print("Fiyatı 3,5 TL'den büyük ürünler: ", market.fiyatBuyukUcBucuk())
