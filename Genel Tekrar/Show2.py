#Kümeler(Set)
numbers = {78,12,96,3,74,78}
numbers.add(24)
numbers.remove(3)
print(numbers)
print("---------------------------------")
#------------------------------------------
#Sözlük(Dict)
movies = {
    "Film":"Pirates of the Caribbean",
    "Genre":"Macera-Komedi-Aksiyon",
    "Release Date":"2004"
}
print(movies["Genre"])
movies["Release Date"] = "2005"
movies["Platform"] = "Disney"
print(movies)
print("----------------------------------------")
#------------------------------------------------
#Koşullar(If-Elif-Else)
while True:
    try:
        age = int(input("Yaşınızı Giriniz: "))

        if age <= 18:
            print("Ergen")
        elif age >= 18:
            print("Yetişkin")
    except ValueError:
        print("Geçerli bir sayı giriniz")

    