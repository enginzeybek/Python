import pandas as Pd

Veri = {
    "Meyveler": ["Elma","Armut","Muz","Kiraz","Üzüm"],
    "Fiyat": [3.5, 2.8, 4.1, 5.0, 3.0],
    "Adet": [150, 200, 120, 300, 100]
}

dt = Pd.DataFrame(Veri)

dt["Toplam Fiyat"] = dt["Fiyat"] * dt["Adet"]

filtre = dt[dt["Adet"] > 150]

print(f"Adedi 150'den fazla olan meyveler")
print(filtre)
print("-------------------------------------")

artan_sirala = filtre.sort_values(by="Adet", ascending=False)

print("Artan sırada")
print(artan_sirala)

print("---------------------------------------------")

print("Toplam fiyata göre en pahalı meyve")

pahali_id = dt["Toplam Fiyat"].idxmax()
pahali_meyve = dt.loc[pahali_id,"Meyveler"]
print(f"En pahalı meyve {pahali_meyve}")

print("---------------------------------------------")

print("Toplam fiyata göre en ucuz meyve")

ucuz_id = dt["Toplam Fiyat"].idxmin()
ucuz_meyve = dt.loc [ucuz_id,"Meyveler"]
print(f"En ucuz meyve {ucuz_meyve}")

print("---------------------------------------------")

ortalama_adet = dt["Adet"].mean()
ortalama_ustu = dt[dt["Adet"] > ortalama_adet]

print(f"Meyveler ortalama {ortalama_adet} adettir.")
print(ortalama_ustu)

