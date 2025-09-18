import pandas as pd

df = pd.read_csv("C:\Users\LENOVO 2022\Documents\Github\Python\Projeler\Student Uygulaması\student.csv")

#Ortalama Hesaplama

df["ORTALAMA"] = (df["Not1"] + df["Not2"]) / 2

basarili = df[df["ORTALAMA"] >= 70]

sinif_ort = df["ORTALAMA"].mean()

print("Tüm veriler:\n", df)
print("\nBaşarılı öğrenciler:\n", basarili)
print(f"\nSınıf Ortalaması: {sinif_ort:.2f}")

#import os

#print("Mevcut dizin:", os.getcwd())
#print("Dizin içindeki dosyalar:")
#print(os.listdir())
