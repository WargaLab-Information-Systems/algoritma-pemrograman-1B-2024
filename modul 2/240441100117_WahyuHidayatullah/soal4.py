tahun = int(input("MASUKKAN TAHUN: "))

if (tahun % 400 == 0):
    print(tahun, "MERUPAKAN TAHUN KABISAT")
elif (tahun % 100 == 0):
    print(tahun, "BUKAN TAHUN KABISAT")
elif (tahun % 4 == 0):
    print(tahun, "MERUPAKAN TAHUN KABISAT")
else:
    print(tahun, "BUKAN TAHUN KABISAT")

# FUNGSI == 0 ADALAH UNTUK MENGECEK APAKAH ANGKA TERSEBUT SAMA DENGAN 0 ATAU TIDAK