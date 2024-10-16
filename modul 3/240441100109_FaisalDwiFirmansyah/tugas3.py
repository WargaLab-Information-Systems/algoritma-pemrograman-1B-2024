ulang = True

while ulang:
    harian = 2500
    sepuluh_hari = 5500
    Total = 0

    Hari = int(input("Masukkan total hari peminjaman: "))

    for i in range(1,Hari+1):
        if i > 5 :
            Total += harian
            if i % 10 == 0:
                Total += sepuluh_hari
    if Hari > 5 :
         print("Pengembalian DVD anda sudah lewat 5 hari dan terlambat selama ",Hari-5, "hari dan anda wajib membayar denda sebesar", Total)
         ulang = input('Ulangi program (iya/tidak): ')
         if ulang == 'iya' :
             continue
         else :
             ulang = False
    else :
        print("Terimakasih telah mengembalikkan DVD tepat waktu sehingga anda tidak dikenai denda apapun")
        if ulang == 'iya' :
            continue
        else :
            ulang = False