Tahun = int(input("Masukkan tahun :"))

if (Tahun % 400 == 0) :
    print("merupakan tahun kabisat")
elif (Tahun % 100 == 0) :
    print("bukan tahun kabisat")
elif (Tahun % 4 == 0) :
    print("merupakan tahun kabisat")
else:
    print("bukan tahun kabisat")