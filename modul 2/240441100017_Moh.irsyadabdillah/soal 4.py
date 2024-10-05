
tahun = int(input("Masukkan tahun: "))

#habis di modulus 400 berarti tahun kabisat
if (tahun % 400 == 0):
    kabisat = "tahun kabisat"

    #habis di modulus 4 dan harus tidak habis dimodulus 100 (harus bersisa jika dimodulus 100)
elif (tahun % 4 == 0 and tahun % 100 != 0):
    kabisat = "tahun kabisat"
else:
    kabisat = "bukan tahun kabisat"

print(f"{tahun} adalah {kabisat}.")
