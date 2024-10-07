# Inputan
tahun = int(input("Masukkan tahun: "))

# Penyelksian kondisi
if tahun % 4 == 0:
    if tahun % 100 != 0:
        print(f"Tahun {tahun} adalah tahun kabisat.")
    else:
        if tahun % 400 == 0:
            print(f"Tahun {tahun} adalah tahun kabisat.")
        else:
            print(f"Tahun {tahun} bukan tahun kabisat.")
else:
    print(f"Tahun {tahun} bukan tahun kabisat.")
