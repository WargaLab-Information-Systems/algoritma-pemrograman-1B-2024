while True:
    try:
        # Meminta untuk masukkan hari
        lama_sewa = int(input("Masukkan lama penyewaan DVD (dalam hari) : "))
        
        # Diketahui
        batas_pinjam = 5
        denda_harian = 2500
        denda_tambahan_per_5hari = 5500

        # Inisialisasi total denda
        total_denda = 0
        
        # Jika lama penyewaan lebih dari batas pinjam (5 hari)
        if lama_sewa > batas_pinjam:
            # Hitung keterlambatan
            keterlambatan = lama_sewa - batas_pinjam
            
            # Hitung denda harian
            total_denda = keterlambatan * denda_harian
            
            # Jika keterlambatan lebih dari 10 hari, tambahkan denda tambahan
            if keterlambatan > 10:
                # Hitung jumlah blok 5 hari setelah 10 hari keterlambatan
                tambahan_lebih_10_hari = (keterlambatan - 10) // 5
                total_denda += tambahan_lebih_10_hari * denda_tambahan_per_5hari
        
        # Menampilkan total denda yg harus di bayar
        print(f"Total denda: Rp{total_denda}")
    
    except ValueError:
        print("Input tidak valid, harap masukkan angka yang benar.")
        continue

    # Menanyakan apakah ingin menghitung lagi
    ulang = input("Apakah Kamu ingin menghitungnya lagi? (y/g): ").lower()
    if ulang != 'y':
        print("JANGAN LUPA DI BAYAR DENDANYA!")
        break
# test