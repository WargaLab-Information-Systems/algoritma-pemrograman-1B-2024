def faktorial(angka):
    faktorial = 1
    for i in range (1, angka + 1):
        faktorial *= i
    return faktorial

angka = int(input("Masukkan angka : "))

print(f"{angka}! = ", end="")
for i in range (angka, 0, -1):
    print(i,end=" x " if i > 1 else " = ")
    
print(faktorial(angka))

