# Program untuk menghitung denda keterlambatan DVD
while True:
    try:
        hari_pinjam = int(input("Masukkan lama hari penyewaan DVD: "))  # Meminta input lama hari penyewaan
        
        # Menghitung denda keterlambatan
        if hari_pinjam <= 5:
            denda = 0
        else:
            terlambat = hari_pinjam - 5
            denda = 2500 * terlambat
            
            if terlambat > 10:
                # Menghitung denda tambahan jika lebih dari 10 hari keterlambatan
                denda_tambahan = ((terlambat - 10) // 5) * 5500
                denda += denda_tambahan
        
        print(f"Total denda keterlambatan: Rp{denda}")
        
        # Menanyakan apakah ingin menghitung ulang
        ulang = input("Ingin menghitung denda lagi? (y/n): ").lower()
        if ulang != 'y':
            break  # Keluar dari loop jika tidak ingin melanjutkan
    except ValueError:
        print("Input tidak valid, masukkan angka bulat.")
        continue  # Melanjutkan ke input berikutnya jika input tidak valid