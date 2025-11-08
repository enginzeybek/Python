import matplotlib.pyplot as plt

Sebzeler= ["Patates", "Domates", "Soğan", "Biber"]
Fiyatlar= [2.5, 3.8, 1.9, 4.0]

plt.bar(Sebzeler,Fiyatlar)
plt.title("Sebze Fiyatları")
plt.xlabel("Sebzeler")
plt.ylabel("Fiyat (TL)")
plt.show()