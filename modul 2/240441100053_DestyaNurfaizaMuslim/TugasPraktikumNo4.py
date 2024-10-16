# Program untuk menentukan tahun kabisat

tahun = int(input("masukkan tahun : "))
if (tahun % 400) == 0:
    print("tahun", tahun, "merupakan tahun kabisat")
elif (tahun % 100) == 0:
    print("tahun", tahun, "bukan tahun kabisat")
elif (tahun % 4) == 0:
    print("tahun", tahun, "merupakan tahun kabisat")
else:
    print("tahun", tahun, "bukan tahun kabisat")
