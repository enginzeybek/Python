import pandas as pd

veri = {
    "Kategori": ["Meyve","Meyve","Meyve","Sebze","Sebze","Sebze","İçecek","İçecek","Atıştırmalık","Atıştırmalık"],

    "Ürün": ["Elma","Muz","Çilek","Domates","Salatalık","Patates","Kola","Ayran","Cips","Çikolata"],

    "Fiyat": [4.2,5.5,12.0,6.0,4.8,3.2,15.0,6.0,10.0,8.5],
    "Adet": [180,120,60,150,200,300,90,140,110,95],
    "Tarih": ["2025-01-10","2025-01-10","2025-01-11","2025-01-10","2025-01-11","2025-01-12","2025-01-10","2025-01-10","2025-01-11","2025-01-12"]
}

for key,value in veri.items():
    print(f"Sütunlar: {key},satırlar: {value}")

class Market:
    def __init__(self,veri):
        self.db = pd.DataFrame(veri)
        self.db["Toplam_Fiyat"] = self.db["Fiyat"] * self.db["Adet"]
    
    def addProduct(self,kategori,ürün,fiyat,adet,tarih):
        yeni_satir = {
            "Kategori": kategori,
            "Ürün": ürün,
            "Fiyat": fiyat,
            "Adet": adet,
            "Tarih": tarih,
            "Toplam_Fiyat": fiyat * adet
        }
        self.db.loc[len(self.db)] = yeni_satir
    
    def removeProduct(self,ürün):
        self.db = self.db[self.db["Ürün"] != ürün]
        print(f"{ürün} silindi")
    
    def updatePrice(self,ürün,yenifiyat):
        self.db.loc[self.db["Ürün"] == ürün, "Fiyat"] = yenifiyat
        self.db["Toplam_Fiyat"] = self.db["Fiyat"] * self.db["Adet"]

        print("Güncelleme işlemi paşarılı")

    def findProduct(self,ürün):
        product = self.db.loc[self.db["Ürün"] == ürün]

        return product
    
    def priceFiltre(self):
        dusukfiyat = self.db["Fiyat"].idxmin()
        yuksekfiyat = self.db["Fiyat"].idxmax()

        en_ucuz_urun = self.db.loc[dusukfiyat]
        en_pahali_urun = self.db.loc[yuksekfiyat]

        print("\n--- Fiyat Analizi ---")
        
        print(f"💰 En Yüksek Fiyatlı Ürün:")
        print(f"  Ürün Adı: {en_pahali_urun['Ürün']}")
        print(f"  Fiyatı: {en_pahali_urun['Fiyat']} TL")
        print(f"  Kategori: {en_pahali_urun['Kategori']}")
        
        print(f"\n💸 En Düşük Fiyatlı Ürün:")
        print(f"  Ürün Adı: {en_ucuz_urun['Ürün']}")
        print(f"  Fiyatı: {en_ucuz_urun['Fiyat']} TL")
        print(f"  Kategori: {en_ucuz_urun['Kategori']}")
        print("----------------------")


