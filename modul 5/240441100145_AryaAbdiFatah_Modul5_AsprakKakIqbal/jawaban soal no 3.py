def faktorial(angka):
    faktorial = 1
    for i in range (1, angka + 1):
        faktorial *= i #untuk melakukan perkalian i dan faktorial
    return faktorial

angka = int(input("masukan angka:"))

print(f"{angka}! = ", end="")
for i in range (angka, 0, -1):
    print(i,end=" x " if i > 1 else " = ")
    
print(faktorial(angka))