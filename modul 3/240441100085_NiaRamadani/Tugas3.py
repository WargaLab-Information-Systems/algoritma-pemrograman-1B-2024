ulang = True
    
while ulang:
    harian = 2500
    sepuluh_hari = 5500
    Total = 0

    Hari = int(input("Lama peminjaman: "))

    for i in range(1,Hari+1):
        if i > 5 :
            Total += harian
            if i % 10 == 0:
                Total += sepuluh_hari
    if Hari > 5 :
         print("Pengembalian DVD anda sudah melebihi batas waktu  dan terlambat selama ",Hari-5, "hari maka anda akan dikenakan denda sebesar", Total)
         ulang = input('Apakah anda ingin menghitung ulang ? (iya/tidak): ')
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







