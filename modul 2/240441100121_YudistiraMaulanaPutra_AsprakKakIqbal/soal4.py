tahun = int(input("Masukkan tahun yang ingin dicek: "))

# RUMUS
# Jika angka tahun habis dibagi 400, maka tahun tersebut merupakan tahun kabisat.
# Jika angka tahun tidak habis dibagi 400 tetapi habis dibagi 100, 
# maka tahun tersebut bukan merupakan tahun kabisat.

# Jika angka tahun tidak habis dibagi 400, tidak habis dibagi 100, tetapi habis dibagi 4, 
# maka tahun tersebut merupakan tahun kabisat.

# Jika angka tahun tidak habis dibagi 400, tidak habis dibagi 100, dan tidak habis dibagi 4, 
# maka tahun tersebut bukan merupakan tahun kabisat.

if tahun % 400 == 0:
    print(tahun, "adalah tahun kabisat.")
elif tahun % 100 == 0:
    print(tahun, "bukan tahun kabisat.")
elif tahun % 4 == 0:
    print(tahun, "adalah tahun kabisat.")
else:
    print(tahun, "bukan tahun kabisat.")