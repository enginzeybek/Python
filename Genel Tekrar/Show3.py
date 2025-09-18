#Döngüler(FOR,RANGE,WHİLE)
for x in range(1,21):
    square = x * x
    print(f"1 ile 20 arasındaki sayıların karesi: {x} için {square}")
print("-------------------------------------------------------------")
#List Comprehension
oddSquare = [x ** 2 for x in range(1,16) if x % 2 == 1]
evenSquare = [y ** 3 for y in range(1,16) if y % 2 == 0]

print(f"Tek sayıların karesi {oddSquare}")
print(f"Çift sayıların küpü {evenSquare}")

print("---------------------------------------------------------------")
#-----------------------------------------------------------------------
#Methodlar(Functions)
def squareOfNumbers():
    for x in range(1,11):
        square = x ** 2
        print(f"{x} sayısının karesi {square}")
def cubeOfNumbers():
    for y in range(1,11):
        cube = y ** 3
        print(f"{y} sayısının küpü {cube}")

squareOfNumbers()
cubeOfNumbers()
