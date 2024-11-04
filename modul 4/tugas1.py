n = int(input("Masukkan ukuran sisi N : "))
karakter = input("Masukkan karakter yang anda inginkan(X/O): ")
while karakter != "X" and karakter != "O":
    karakter = str(input("Pilihlan antara X atau O : "))

print()
for i in range(n-1):
    for j in range(n,i,-1):
        print(" ",end = "")
    for j in range(2*i+1):
        print(karakter, end="")
    print()
for i in range(n-1,-1,-1):
    for j in range(n,i,-1):
        print(" ",end="")
    for j in range(2*i+1):
        print(karakter,end="")
    print() 