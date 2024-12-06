def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

def tampilkan_ekspresi(n):
    ekspresi = ""
    for i in range(n, 0, -1):
        if i > 1:
            ekspresi += (f"{i} * ")
        else:
            ekspresi += (f"{i}")
    return ekspresi

n = int(input("Masukkan bilangan bulat positif: "))
hasil = faktorial(n)
ekspresi = tampilkan_ekspresi(n)
print(f"Faktorial dari {n}! = {ekspresi} = {hasil}")