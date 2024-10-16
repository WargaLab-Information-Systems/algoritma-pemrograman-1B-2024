tahun = int(input("Masukkan tahun: "))

if (tahun % 400 == 0):
    print(f"{tahun} Merupakan tahun kabisat")
elif (tahun % 4 == 0):
    print(f"{tahun} Merupakan tahun kabisat")
else:
    print(f"{tahun} Bukan termasuk tahun kabisat")