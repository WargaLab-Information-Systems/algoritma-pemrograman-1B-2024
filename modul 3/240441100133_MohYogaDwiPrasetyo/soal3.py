while True:
    hari_pinjam = int(input("Masukkan lama peminjaman (dalam hari): "))
    
    # hitung terlambat/tidak
    if hari_pinjam > 5:
        keterlambatan = hari_pinjam - 5
    else:
        keterlambatan = 0

    # hitung denda 2500/hari
    denda_dasar = keterlambatan * 2500

    # jika terlambat lebih dr 10 hari, ada denda tambahan 5500/5 hari
    denda_tambahan = 0
    if keterlambatan > 10:
        periode_tambahan = (keterlambatan - 10) // 5
        denda_tambahan = periode_tambahan * 5500

    denda = denda_dasar + denda_tambahan
    
    if keterlambatan > 0:
        print(f"Keterlambatan: {keterlambatan} hari")
        print(f"Total denda: Rp {denda}")
    else:
        print("Tidak ada denda!")
    
    if input("Apakah ingin menghitung lagi? (y/n): ") == 'n':
        print("Terima kasih!")
        break
