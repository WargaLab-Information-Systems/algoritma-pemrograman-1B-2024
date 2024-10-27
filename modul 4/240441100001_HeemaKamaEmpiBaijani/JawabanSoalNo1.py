n = int(input("Masukkan size (N): "))
PilihanKlien = str(input("pilih karakter (X/O): "))

for i in range(0, n):
    for j in range(0, n-i-1):
        print(" ", end="")
    for j in range(0, i+1):
        print(f"{PilihanKlien} ", end="")
    print()

for i in range (0, n-1):
    for j in range(0, i+1):
        print(" ", end="")
    for j in range(0, n-i-1):
        print(f"{PilihanKlien} ", end="")
    print()