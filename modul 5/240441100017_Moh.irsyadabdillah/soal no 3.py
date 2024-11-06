def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

angka = int(input("masukkan angka:"))
hasil = faktorial(angka)
print(f"{angka}! = {hasil}")