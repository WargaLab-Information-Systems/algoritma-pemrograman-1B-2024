while True:

    hari_menggembalikan = int(input("Masukkan hari pelanggan mengembalikkan DVD: "))

    denda_perhari = 2500
    denda_tambahan_per_5hari = 5500
    total_denda = 0

    if hari_menggembalikan <= 5:
        total_denda = 0
    elif hari_menggembalikan <15:
        total_denda = (hari_menggembalikan - 5) * denda_perhari 
    else:
        total_denda = (hari_menggembalikan - 5) * denda_perhari
        sisa_hari = hari_menggembalikan - 10
        if sisa_hari % 5 != 0:
            total_denda += denda_tambahan_per_5hari
        else:
            total_denda += (sisa_hari // 5 ) * denda_tambahan_per_5hari
        
    print(f"Total denda yang harus dibayar adalah Rp. {total_denda}")

    hitung_lagi = input("Apakah anda ingin menghitung kembali (ya/tidak)? ")
    if hitung_lagi != "ya":
        print("Terima kasih! Program selesai")
        break