import matplotlib.pyplot as plt

Sebzeler= ["Patates","Domates","Soğan","Biber"]
Adetler= [100,150,80,120]

plt.pie(Adetler,labels=Sebzeler,autopct="%1.1f%%",startangle=90)
plt.title("Sebze Adet Dağılımı")
plt.show()