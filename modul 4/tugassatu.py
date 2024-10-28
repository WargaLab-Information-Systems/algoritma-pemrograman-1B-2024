n = int(input("Masukkan ukuran sisi: "))
karakter = input("Masukkan pilihan karakter[X/O]: ").upper()

for i in range(n):
    for j in range(0, n - i):
        print("X", end="")
    for j in range(0, i + 1):
        print(karakter, end=" ")
    print()

for i in range(n):
    for j in range(0, i + 2):
        print(" ", end="")
    for j in range(0, n - i - 1):
        print(karakter, end=" ")
    print()