import pandas as pd

Veri = {
    "Meyveler": ["Apple","Orange","Tangerine","Grape","Plum","Fig"],
    "Fiyat": [2.9,2.1,1.8,3.5,4.3,2.9],
    "Adet": [200,350,900,150,1050,1200]
}

dt = pd.DataFrame(Veri)

print(dt)
print("---------------------------------------------------------")

dt["Toplam_Fiyat"] = dt["Fiyat"] * dt["Adet"]

print("Toplam fiyat sütunu eklendi")
print(dt)
print("-----------------------------------------------------------")

ortalama_fiyat = dt["Fiyat"].mean()
ortalama_adet = dt["Adet"].mean()

print(f"Meyvelerin ortalama adeti {ortalama_adet} ve ortalama fiyatı {ortalama_fiyat}")
print("--------------------------------------------------------------")

# Adedi 500'den fazla olan meyveler
print("Adedi 500'ten fazla olan ürünler")
filtre_adet = dt[dt["Adet"] > 500]
print(filtre_adet)
print("-----------------------------------------------------------------")

# Fiyatı 3 TL'den yüksek olan meyveler
print("Fiyatı 3TL'den fazla olan ürünler")
filtre_fiyat = dt[dt["Fiyat"] > 3]
print(filtre_fiyat)
print("------------------------------------------------------------------")

print("Fiyatı 3 TL'den fazla ve adedi 500'den fazla olan ürünler")
filtre_adet_ve_fiyat = dt[(dt["Adet"] > 500) & (dt["Fiyat"] > 3)]
print(filtre_adet_ve_fiyat)
print("------------------------------------------------------------------")

# Fiyatına göre artan sırada
artan_sirala = dt.sort_values(by="Fiyat")
print("Fiyatına göre artan sırada:")
print(artan_sirala)
print("------------------------------------------------------------------")

# Fiyatına göre azalan sırada
azalan_sirala = dt.sort_values(by="Fiyat",ascending=False)
print("Fiyatına göre azalan sırada:")
print(azalan_sirala)
print("------------------------------------------------------------------")

value = dt[dt["Fiyat"] > 2.5].sort_values(by="Fiyat", ascending=False)
print("Fiyatı 2.5 TL’den fazla olan meyveler azalan sırada:")
print(value)
print("------------------------------------------------------------------")

#En düşük toplam fiyatlı meyve

enUcuzMeyveId = dt["Toplam_Fiyat"].idxmin()
enUcuzToplamFiyatlıMeyve = dt.loc[enUcuzMeyveId,"Meyveler"]
enUcuzToplamFiyat = dt.loc[enUcuzMeyveId,"Toplam_Fiyat"]
print(f"En Ucuz meyve {enUcuzToplamFiyatlıMeyve} ve onun toplam fiyatı {enUcuzToplamFiyat}")
print("----------------------------------------------------------------")

# ortalama fiyatın üstünde olan meyveler

ort_fiyat = dt["Fiyat"].mean()
print(f"ortalama fiyat: {ort_fiyat:.1f}")
ort_ust_fiyat = dt[dt["Fiyat"] > ort_fiyat]
print("ortalama fiyatın üstünde olan meyveler")
print(ort_ust_fiyat)
print("----------------------------------------------------------------")

#Adet sütununa göre en fazla ve en az adetteki meyveleri bulun ve yazdırın

en_az_adet_id = dt["Adet"].idxmin()
en_az_meyve = dt.loc[en_az_adet_id,"Meyveler"]
en_az_adet = dt.loc[en_az_adet_id,"Adet"]
print(f"Adedi en az olan meyve {en_az_meyve} ve adedi de {en_az_adet}")
print("\n")

en_fazla_adet_id = dt["Adet"].idxmax()
en_fazla_meyve = dt.loc[en_fazla_adet_id,"Meyveler"]
en_fazla_adet = dt.loc[en_fazla_adet_id,"Adet"]
print(f"Adedi en fazla olan meyve {en_fazla_meyve} ve adedi de {en_fazla_adet}")