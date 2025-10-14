import pandas as pd

veri = {
    "Tür": ["Meyve", "Sebze", "Meyve", "Sebze", "Meyve", "Sebze"],
    "Ürün": ["Elma", "Havuç", "Muz", "Biber", "Armut", "Kabak"],
    "Fiyat": [3.2, 2.4, 4.5, 3.1, 2.8, 2.7],
    "Adet": [120, 200, 150, 180, 90, 220]
}

dt = pd.DataFrame(veri)

gruplanmis = dt.groupby("Tür")[["Fiyat","Adet"]].mean()

print("Türe göre ortalama adet ve fiyat")
print(gruplanmis)

print("--------------------------------------------------")

print("Azalan ortlama fiyata göre sırala")

azalan = gruplanmis.sort_values(by="Fiyat",ascending=False)
print(azalan)