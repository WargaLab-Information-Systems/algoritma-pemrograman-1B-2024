tahun = int(input("Masukkan Tahun Yang Ingin Anda Ketahui :"))

if (tahun % 400 != 0 or tahun % 100 != 0) and (tahun % 4 == 0) :
    print(f"{tahun} adalah Tahun Kabisat.")
else :
    print(f"{tahun} Adalah Bukan Tahun kabisat.")