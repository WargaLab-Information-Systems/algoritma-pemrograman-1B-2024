# input data
tahun = int(input("Masukkan tahun :"))

# menentukan tahun
if (tahun % 400 == 0):
    print(f"{tahun} adalah tahun kabisat")
elif (tahun % 4 == 0):
    print(f"{tahun} adalah tahun kabisat")
else:
    print(f"{tahun} bukanlah tahun kabisat")