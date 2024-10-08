tahun_input = int(input("Masukkan tahun: "))

if tahun_input < 1500:
    print(f"{tahun_input} bukan tahun kabisat.")
else:
    if (tahun_input % 4 == 0 and tahun_input % 100 != 0) or (tahun_input % 400 == 0):
        print(f"{tahun_input} adalah tahun kabisat.")
    else:
        print(f"{tahun_input} bukan tahun kabisat.")
