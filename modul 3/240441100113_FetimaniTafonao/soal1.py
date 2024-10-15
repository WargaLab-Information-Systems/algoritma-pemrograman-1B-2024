angka_nim = int(input("masukkan angka :"))

for i in range(angka_nim, 0, -1):
    print('a')
print(" ")

for i in range(angka_nim, 0, -1):
    print('b')
print(" ")

for i in range(angka_nim):  
    for j in range(angka_nim): 
        if i == 0 or i == angka_nim - 1 or j == angka_nim - 1 or ( i == angka_nim // 2) :
            print("c", end="")
        else:
            print(" ", end="")
    print()