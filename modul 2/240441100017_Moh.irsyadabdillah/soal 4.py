tahun = int(input("Masukkan tahun: "))
if tahun >= 1500:
    #habis di modulus 400 berarti tahun kabisat
    if (tahun % 400 == 0):
        print("tahun kabisat")

    #habis di modulus 4 dan harus tidak habis dimodulus 100 (harus bersisa jika dimodulus 100)
    elif (tahun % 4 == 0 and tahun % 100 != 0):
        print("tahun kabisat")
    else:
        print("bukan tahun kabisat")

else:
    print("tahun kabisat dimulai setelah tahun 1500")

