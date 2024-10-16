# input tahun
tahun = int(input("Masukkan tahun "))

#menghitung tahun kabisat
if tahun % 400 == 0:
    print(f"Tahun {tahun} merupakan tahun kabisat")
elif tahun % 100 == 0:
    print(f"Tahun {tahun} bukan merupakan  tahun kabisat")
elif tahun % 4 == 0:
    print(f"Tahun {tahun} merupakan tahun kabisat")
else:
    print(f"Tahun {tahun} bukan merupakan tahun kabisat")
