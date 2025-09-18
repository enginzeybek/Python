from Kitap import Kitap

kitap1 = Kitap('Suç ve Ceza','Fyodor Dostoyevski',430,'Roman')
kitap2 = Kitap('Kürk Mantolu Madonna','Sabahattin Ali',160,'Roman')
kitap3 = Kitap('Sapiens: İnsan Türünün Kısa Tarihi','Yuval Noah Harari',498,'Popüler Bilim')


from Kitap import Kutuphane

library = Kutuphane()

library1 = library.kitapEkle(kitap1)
library2 = library.kitapEkle(kitap2)
library3 = library.kitapEkle(kitap3)
libraryList = library.kitaplari_listele()
libraryTur = library.tur_filtrele("Roman")
libraryMaxPage = library.en_uzun_kitap()
