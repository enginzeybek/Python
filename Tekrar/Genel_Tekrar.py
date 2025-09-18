#--Değişken Tanımla--

meyve = "Elma"
fiyat = 20.3
adet = 10

#--Array Tanımla--

meyveler = ["Armut","Kivi","Ananas"]
fiyatlar = [14.89,32.87,23.56]
adetler = [560,890,620]

#--DataFrame Tanımlama (pandas)--

import pandas as pd

pazar = {
    "Meyveler" : meyveler,
    "Fiyatlar" : fiyatlar,
    "Adetler"  : adetler
}

df = pd.DataFrame(pazar)

print(df)

#--Koşullar (if ile filtreleme)--

#Adedi 600den fazla olanlar

filtre = df[df["Adetler"] > 600]

print("Adeti 600'den fazla olan meyveler")

print(filtre)

#--Yeni Sütun Oluşturma--

df["Toplam"] = df["Fiyatlar"] * df["Adetler"]

df["Toplam"] = df["Toplam"].astype(int)

print("TOPLAM SÜTUNU EKLENDİ")

print(df)

#--En Yüksek Değeri Bulma--

MaxPriceİd = df["Toplam"].idxmax()

MaxPriceFruit = df.loc[MaxPriceİd,"Meyveler"]

print(f"EN YÜKSEK FİYATLI MEYVE= {MaxPriceFruit}")