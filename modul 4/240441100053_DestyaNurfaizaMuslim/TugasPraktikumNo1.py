# Membuat pola checkerboard belah ketupat
# dengan ukuran sisi N

n = int(input("Masukkan ukuran sisi N : "))
karakter = input("Masukkan karakter pilihan (X/O) : ")

if karakter == "X" or karakter == "O":
    # Membuat segitiga bagian atas
    for i in range(n-1):
        for j in range(i,n):
            print(" ", end=" ")
        for k in range(i):
            print(karakter,end=" ")
        for l in range(i+1):
            print(karakter,end=" ")
        print()
    # Membuat segitiga bagian bawah
    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for k in range(i,n-1):
            print(karakter,end=" ")
        for l in range(i,n):
            print(karakter, end=" ")
        print()
else:
    print("Masukkan karakter ulang")
