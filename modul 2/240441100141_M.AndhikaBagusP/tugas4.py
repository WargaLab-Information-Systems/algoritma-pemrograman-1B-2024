# input data
tahun = int(input("Masukkan tahun :"))

# menentukan tahun
if (tahun % 4 == 0 and tahun % 100 != 0):
    print(f"{tahun} adalah tahun kabisat")
elif (tahun % 400 == 0):
    print(f"{tahun} adalah tahun kabisat")
else:
    print(f"{tahun} bukanlah tahun kabisat")