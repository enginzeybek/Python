import pandas as pd

veri = {
    "GorevID": [101, 102, 103, 104, 105, 106],

    "Baslik": ["Kullanıcı Girişi Geliştirme", "Veritabanı Şeması Tasarımı", "CSS Stili Optimizasyonu", "API Endpoint Testleri", "Raporlama Modülü Hazırlama", "Hata Düzeltme (Kritik)"],

    "Kategori": ["Backend", "Backend", "Frontend", "Test", "Backend", "Hata"],

    "Durum": ["Tamamlandı", "Devam Ediyor", "Beklemede", "Devam Ediyor", "Beklemede", "Devam Ediyor"],

    "Oncelik": ["Yüksek", "Yüksek", "Düşük", "Orta", "Yüksek", "Çok Yüksek"],

    "Sure_Tahmini_Saat": [8, 12, 4, 6, 20, 3],

    "Atanan": ["Ayşe Y.", "Mehmet K.", "Deniz E.", "Ayşe Y.", "Burak T.", "Deniz E."],

    "Baslangic_Tarihi": ["2025-11-01", "2025-11-05", "2025-11-10", "2025-11-12", "2025-11-15", "2025-11-18"]
}


class Proje:
    def __init__(self):
        self.db = None

    def loadData(self,veri):
        self.db = pd.DataFrame(veri)

    def showData(self):
        if self.db is None:
            print("Veri kümesi boş.")
            return
        
        print(self.db)

    def findTask(self,baslik):
        baslik = baslik.lower()

        if self.db is None:
            print("Veri yüklenmemiş.")
            return None
        
        sonuc = self.db[self.db["Baslik"].str.lower() == baslik]

        if sonuc.empty:
            print("Görev Bulunamadı")
            return None

        return sonuc
    
    def filterByStatus(self,durum):
        durum = durum.lower()
        if self.db is None:
            print("Veri yüklenmemiş.")
            return None

        sonuc = self.db[self.db["Durum"].str.lower() == durum]

        if sonuc.empty:
            print("Durum bulunamadı")
            return None
        
        return sonuc




project = Proje()

project.loadData(veri)
project.showData()
project.filterByStatus("Devam Ediyor")