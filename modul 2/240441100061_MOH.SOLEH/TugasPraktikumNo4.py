# Menentukan Tahun Kabisat
tahun = int(input("Masukkan Tahun : "))

# Menentukan Apakah Tahun Kabisat
if tahun % 400 == 0:
    print(f"{tahun} adalah tahun kabisat.")
elif tahun % 100 == 0:
    print(f"{tahun} adalah bukan tahun kabisat.")
elif tahun % 4 == 0:
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat")
