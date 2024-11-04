n = int(input("Masukkan ukuran sisi N: "))
pola = input("Pilihlah pola (X/O): ")
while pola != "x" and pola != "o":
    pola = str(input("Pilihlah pola (X/O): "))
print()
for i in range(n):
    spasi = n - i - 1
    print(" " * spasi, end= "")
    for j in range(i + 1):
        if (j + spasi) % 2 == 0:
            print(pola, end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(n - 1):
    spasi = i + 1
    print(" " * spasi, end= "")
    for j in range(n - spasi):
        if (j + spasi) % 2 == 0:
            print(pola, end=" ")
        else:
            print(" ", end=" ")
    print()