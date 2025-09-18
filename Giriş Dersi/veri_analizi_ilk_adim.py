"""
print("MERHABA")

isim = "ENGİN"
yas = 30

print(f"MERHABA {isim}, yaşın {yas}")

print("\nSEVDİĞİM MEYVELER:")
meyveler = ["ELMA","PORTAKAL","ERİK"]
for meyve in meyveler:
    print("-",meyve)

import pandas as pd
veri = {
    "İsim": ["Ali", "Ayşe", "Mehmet"],
    "Yaş": [25, 30, 35]
}

df = pd.DataFrame(veri)

print("\nDataFrame içeriği:")
print(df)


isim = "Engin"
yas = "32"

print(f"Adı: {isim},Yaşı: {yas}")

meyveler = ["APPLE","ORANGE","TANGERİNE"]

for meyve in meyveler:
    print("MEYVELER SIRASIYLA: " + meyve)



import pandas as pd

veri = {
    "İSİM" : ["İREM","ASENA","MERT RAMAZAN"],
    "YAŞ"  : [21,28,26]
}

kisiler = pd.DataFrame(veri)

print(type(yas))

kisiler["ŞEHİR"] = ["ANKARA","İZMİR","BURSA"]

print(kisiler)

"""

class Veriler:
    def selamla(self,isim):
        print(f"MERHABA {isim}")

    def topla(self,a,b):
        return a + b  
 
    