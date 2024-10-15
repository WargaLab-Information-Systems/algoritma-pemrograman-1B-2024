tahun = int(input("Masukan tahun berapa yang anda cari: "))
# inputan tahun yang diminta
if tahun % 400 == 0:
    print(tahun, "Adalah tahun kabisat")
elif tahun % 100 == 0:
    print(tahun, "Bukan tahun kabisat")
elif tahun % 4 == 0:
    print(tahun, "Adalah tahun kabisat")
else:
    print(tahun, "bukan tahun kabisat")
# pengondisian