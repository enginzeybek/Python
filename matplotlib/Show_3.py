import pandas as pd
import matplotlib.pyplot as mpb

coffeeSale = {
    "Ürün":["Espresso","Latte","Cappuccino","Türk Kahvesi","Filtre Kahve"],
    "Fiyat":[5,6,6,4,3],
    "Adet":[30,45,25,50,40],
    "Tarih":["2025-11-01","2025-11-01","2025-11-02","2025-11-02","2025-11-03"]
}

dt = pd.DataFrame(coffeeSale)
print("CoffeeShop Satış Tablosu")
print(dt)
print("-------------------------------------------------------")

# Tek figür, 1 satır 2 sütun subplot
fig, (ax1, ax2) = mpb.subplots(1, 2, figsize=(12, 5))

print("-------------------------------------------------------")

urun_toplam_satis = dt["Fiyat"] * dt["Adet"]
print("Ürünlerin Toplam Satışı")
print(urun_toplam_satis)

print("-------------------------------------------------------")

toplam_satis = sum(urun_toplam_satis)
print("Toplam Satışı")
print(toplam_satis)

print("-------------------------------------------------------")

ax1.bar(dt["Tarih"],urun_toplam_satis)
ax1.set_title("Günlere Göre Satış")
ax1.set_xlabel("Tarih")
ax1.set_ylabel("Toplam Satış")


print("-------------------------------------------------------")

ax2.pie(urun_toplam_satis,labels=dt["Ürün"],startangle=90,autopct="%1.1f%%")
ax2.set_title("En çok satan kahveler")

print("-------------------------------------------------------")

mpb.tight_layout()
mpb.show()
