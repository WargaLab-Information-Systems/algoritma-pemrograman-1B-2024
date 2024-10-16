while True:
    pinjam = int(input("Anda sudah pinjam selama berapa hari: "))
    if pinjam >= 5:
        a = pinjam - 5
        if pinjam >= 10:
            denda1 = 2500 * a + 5500 * (a / 5)
            print(f"karena anda telat lebih dari {a} hari, anda terkena denda sebesar {denda1}")
        else:
            denda = 2500 * a
            print(f"karena anda telat lebih dari {a} hari, anda terkena denda sebesar {denda}")
    input("silakan entek kemudian ketik ya untuk mengecek lagi")
    cek = str(input("Apakah anda ingin mengeceknya lagi: "))
    if cek != "ya": break
    
