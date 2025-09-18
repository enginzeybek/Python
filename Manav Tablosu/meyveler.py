import pandas as my

tb = my.read_csv("C:/Users/LENOVO 2022/Documents/Github/Python/Projeler/Manav Tablosu/meyveler.csv",encoding="windows-1254",sep=";",decimal=",") #windows-1254 pyhton için Türkçe ayarı
#Eğer çıktı bozuk düzensiz gelirse veya ondalıklı bir veri varsa sep=";" kullan.
#decimal=","Pandas’a dedik ki: "ondalık sayıları virgülle ayırmış olabilirim, buna göre oku.

print(tb)

#import os
#print(os.getcwd()) #Bu satır sana kodun nerede çalıştığını gösterecek. Eğer .csv dosyası bu klasörde değilse, ya dosyayı oraya koymalısın ya da read_csv() içindeki yolu ona göre yazmalısın.

tb["Adet"] = tb["Adet"].astype(int) # Convert işlemi yapıyor. Burada da float'dan int çevirdik.

Adet = tb["Adet"].mean()
Fiyat = tb["Fiyat"].mean()
print(f"Meyvelerin Ortalama Fiyatı= {Fiyat:.2f},Meyvelerin Ortalama Adeti= {Adet}")

tb["SonFiyat"] = tb["Adet"] * tb["Fiyat"]
MaxPrice = tb["SonFiyat"].max()
idx = tb["SonFiyat"].idxmax()   # max fiyatın satır indeksini verir.
en_pahali_meyve = tb.loc[idx, "Meyve"]
print(f"En yüksek toplam fiyata sahip meyve: {en_pahali_meyve} ({MaxPrice:.2f} TL)")

meyveler_fazla_olan = tb[tb["Adet"] > 8]
print("8 adetten fazla meyveler:")
print(meyveler_fazla_olan[["Meyve", "Adet"]])



