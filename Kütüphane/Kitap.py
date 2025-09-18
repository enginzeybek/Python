class Kitap:
    def __init__(self,isim,yazar,sayfa_sayisi,tur):
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur

#__init__ Python’da yapıcı method (constructor) için sabit, özel bir isimdir.

class Kutuphane:
    def __init__(self):
        self.kitaplar = []

    def kitapEkle(self,kitap):
        self.kitaplar.append(kitap)

    def kitaplari_listele(self):
        for kitap in self.kitaplar:
            print(f"{kitap.isim} - {kitap.yazar} ({kitap.sayfa_sayisi} sayfa) [{kitap.tur}]")

    def tur_filtrele(self, tur):
        filtreli = [k for k in self.kitaplar if k.tur.lower() == tur.lower()]
        for kitap in filtreli:
            print(f"{kitap.isim} - {kitap.yazar} ({kitap.sayfa_sayisi} sayfa) [{kitap.tur}]")

    def en_uzun_kitap(self):
        if not self.kitaplar:
            print("Kütüphane boş.")
            return
        uzun_kitap = max(self.kitaplar, key=lambda k: k.sayfa_sayisi)
        print(f"En uzun kitap: {uzun_kitap.isim} - {uzun_kitap.sayfa_sayisi} sayfa")

        #lambda burada küçük bir fonksiyon tanımlamaya yarıyor, def yazmaya gerek kalmadan tek satırda işimizi görüyor.

        #İstersen lambda yerine normal fonksiyon da yazabilirdik:

        #def sayfa_anahtari(k):
            #return k.sayfa_sayisi

        #uzun_kitap = max(kitaplar, key=sayfa_anahtari)