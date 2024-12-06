def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

n = int(input("Masukkan angka: "))
hasil = faktorial(n)

print(f"{n}! = ", end="")
for i in range(n, 0, -1):
    print(i, end="")
    if i > 1:
        print(" x ", end="")

print(f" = {hasil}")

