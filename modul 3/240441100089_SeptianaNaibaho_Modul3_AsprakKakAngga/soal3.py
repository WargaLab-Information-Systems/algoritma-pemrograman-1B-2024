ulang = "ya"  

while ulang == "ya":
    lama_peminjaman = int(input("Masukkan lama waktu penyewaan: "))

    if lama_peminjaman > 5:
        hari_terlambat = lama_peminjaman - 5
        denda_per_hari = 2500
        total_denda = hari_terlambat * denda_per_hari

        if hari_terlambat > 10:
            sisa_hari_terlambat = hari_terlambat - 10
            total_denda += (sisa_hari_terlambat // 5) * 5500

        print(f"Total denda keterlambatan: Rp{total_denda}")
    else:
        print("Tidak ada denda karena penyewaan masih dalam batas waktu.")

    ulang = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")

print("Program selesai.")
