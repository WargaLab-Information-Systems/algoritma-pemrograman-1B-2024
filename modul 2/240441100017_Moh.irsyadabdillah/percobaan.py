tahun = int(input("Masukkan tahun: "))
if tahun % 4 == 0:
        if tahun % 100 != 0:
                print(f"tahun{tahun}adalah tahun kabisat.")
        else:
            if tahun % 400 == 0:
                print(f"tahun {tahun} adalah tahun kabisat.")
            else:
                  print(f"tahun {tahun} bukan tahun kabisat.")
    else:
      print(f"tahun{tahun} bukan tahun kabisat")
      