tahun = int(input("Masukkan tahun: "))

if (tahun % 4) == 0:
    print(tahun, "merupakan tahun kabisat")
elif(tahun % 100) != 0:
    print(tahun, "bukan tahun kabisat")
elif (tahun % 400) == 0:
    print(tahun, "merupakan tahun kabisat.")
else:
    print(tahun, "bukan tahun kabisat.")
