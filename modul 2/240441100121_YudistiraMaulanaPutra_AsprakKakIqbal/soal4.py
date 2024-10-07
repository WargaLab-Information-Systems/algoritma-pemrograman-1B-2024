tahun = int(input("Masukkan tahun yang ingin dicek: "))

if tahun % 400 == 0:
    print(tahun, "adalah tahun kabisat.")
elif tahun % 100 == 0:
    print(tahun, "bukan tahun kabisat.")
elif tahun % 4 == 0:
    print(tahun, "adalah tahun kabisat.")
else:
    print(tahun, "bukan tahun kabisat.")