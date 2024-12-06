while True:
    pinjam = int(input(" inputkan data: "))
    if pinjam >= 5:
        terlambat = pinjam - 5
        denda = 2500
        print(denda * terlambat)
        if pinjam >= 10:
            dendab = 5500
            terlambatb = terlambat/5
            hasil = terlambatb * dendab + denda * terlambat
            print (hasil)
    cek = str(input("jika ya, ketik ya"))
    if cek != "ya":
        break