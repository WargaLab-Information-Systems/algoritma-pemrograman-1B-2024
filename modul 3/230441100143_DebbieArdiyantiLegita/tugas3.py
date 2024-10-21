while True:
    try:
        # Input lama peminjaman
        lama_pinjam = int(input("Masukkan lama hari peminjaman DVD: "))
        
        # Variabel yang dibutuhkan
        hari_peminjaman = 5
        denda_per_hari = 2500
        denda_tambahan_per_5_hari = 5500
        
        # Menghitung keterlambatan
        terlambat = lama_pinjam - hari_peminjaman
        
        # Menghitung denda
        if terlambat <= 0:
            total_denda = 0  # Tidak ada denda jika tidak terlambat
            print("Tidak ada denda, DVD dikembalikan tepat waktu.")
        else:
            print(f"Anda terlambat mengembalikan selama {terlambat} hari.")
            total_denda = terlambat * denda_per_hari  # Denda dasar Rp2500/hari
            
            # Jika terlambat lebih dari 10 hari, tambahkan denda tambahan
            if terlambat > 10:
                denda_tambahan = ((terlambat - 10) // 5) * denda_tambahan_per_5_hari
                total_denda += denda_tambahan
            
            print(f"Total denda keterlambatan: Rp{total_denda}")
        
        # Menanyakan apakah ingin menghitung lagi
        ulangi = input("Apakah Anda ingin menghitung lagi? (y/n): ").lower()
        if ulangi != 'y':
            break
    except ValueError:
        print("Input tidak valid, masukkan angka.")

print("Terima kasih telah menggunakan program ini!")