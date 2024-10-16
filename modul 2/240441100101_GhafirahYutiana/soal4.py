tahun = int(input("Masukkan tahun: "))

if (tahun % 400 == 0):
    kabisat = "tahun kabisat"

elif (tahun % 4 == 0 and tahun % 100 != 0):
    kabisat = "tahun kabisat"
else:
    kabisat = "bukan tahun kabisat"

print(f"{tahun} adalah {kabisat}.")
