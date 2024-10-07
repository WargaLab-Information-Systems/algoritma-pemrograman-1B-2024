tahun = int(input("Masukkan tahun: "))

if tahun <= 1500:
    print("tahun sebelum 1500 bukan tahun kabisat")
else:
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        print(f"{tahun} adalah tahun kabisat.")
    else: 
        print(f"{tahun} bukan tahun kabisat.")
