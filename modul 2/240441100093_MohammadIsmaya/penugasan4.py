
tahun = int(input("masukan tahun:"))


if (tahun % 100 != 0 or tahun % 400 != 0) and tahun % 4 == 0:
    print(f"Tahun{tahun} adalah tahun kabisat")
else:
    print(f"Tahun{tahun} bukanlah tahun kabisat")