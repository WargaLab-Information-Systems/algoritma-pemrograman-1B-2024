# tahun yang terbagi habis  4 adalah tahun kabisat

tahun = int(input("Masukan Tahun :"))

if tahun % 4 == 0:
    print(tahun, "Adalah tahun kabisat ")
else:
    print(tahun, "Adalah bukan tahun kabisat")