while True:
    lama_sewa = int(input("Masukkan lama penyewaan DVD (dalam hari): "))
    
    # Jika lama sewa kurang dari atau sama dengan 5 hari, tidak ada denda
    if lama_sewa <= 5:
        print("DVD dikembalikan tepat waktu, tidak ada denda.")
    
    # Jika terlambat, hitung keterlambatan dan denda
    else:
        keterlambatan = lama_sewa - 5
        denda = keterlambatan * 2500

        # Jika keterlambatan lebih dari 10 hari, hitung denda tambahan
        if keterlambatan > 10:
            keterlambatan_tambahan = keterlambatan - 10
            denda_tambahan = (keterlambatan_tambahan // 5) * 5500
            denda += denda_tambahan
        
        # Tampilkan total denda
        print(f"Total denda keterlambatan: Rp {denda}")
    
    # Tanya pengguna apakah ingin menghitung lagi
    hitung_lagi = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ").strip().lower()
    
    # Jika tidak ingin menghitung lagi, keluar dari loop
    if hitung_lagi != 'ya':
        print("terimaksih telah menyewa di tempat kami")
        break