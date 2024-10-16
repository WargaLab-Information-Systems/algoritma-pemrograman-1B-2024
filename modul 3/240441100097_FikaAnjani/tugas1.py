tinggi_angka= int(input("masukkan angka :"))

for i in range(tinggi_angka):
    for j in range(tinggi_angka):
        if i==0 or i==tinggi_angka-1 or j==0 or j==tinggi_angka-1:
            print("0")
        else:
            print(" ",end="")
    print()

for i in range(tinggi_angka):
    for j in range(tinggi_angka):
        if i==0 or i==tinggi_angka-1 or j==tinggi_angka-1 or i==tinggi_angka// 2 or (j == 0 and i < tinggi_angka // 2):
            print("9", end="")
        else:
             print(" ", end="")
    print()

for i in range(tinggi_angka):
    for j in range(tinggi_angka):
        if i==0 or j==tinggi_angka-1:
            print("7",end="")
        else:
            print(" ",end="")
    print()


