Bilangan = int(input("Masukkan bilangan desimal: "))
Biner = ""
n = Bilangan
while n > 0:
    Biner = str(n % 2) + Biner
    n = n // 2
    print(Biner)