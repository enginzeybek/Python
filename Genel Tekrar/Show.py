#Değişkenler(variable)
number = 2
name = "İrem Aytepe"
decimalNumber = 56.89
IsPassed = True
karma = 1 + 2j

print(type(number))
print(type(name))
print(type(decimalNumber))
print(type(IsPassed))
print(type(karma))
#---------------------------------
#Liste(List)
renkler = ["Mavi","Kırmızı","Sarı","Yeşil"]
print(renkler[0])
print(renkler[3])
print(renkler[-1])
renkler.append("Mor")
#for renk in renkler:
    #print(renk)
renkler.remove("Mavi")
for renk in renkler:
    print(renk)
#---------------------------------------------------
#Demet(Tuple)
serials = ("Doctor Who","Game Of Thrones","Stranger Things","Leyla İle Mecnun")
print(serials[0])
print(serials[-1])
serials2 = ("Doctor Who","Doctor Who","Stranger Things")
for serial in serials2:
    print(serial)