while True:
    lama_sewa = int(input("Masukkan lama penyewaan DVD (dalam hari): "))

    if lama_sewa <= 5:
        print("DVD dikembalikan tepat waktu, tidak ada denda.")
    else:
        keterlambatan = lama_sewa - 5
        denda = keterlambatan * 2500 

        if keterlambatan > 10:
            berat_keterlambatan = keterlambatan - 5
            denda_tambahan = (berat_keterlambatan // 5) * 5500
            denda += denda_tambahan 

        print(f"Total denda keterlambatan: Rp{denda}")

        hitung_lagi = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ").strip().lower()
        if hitung_lagi != 'ya':
            print("Terima kasih telah menggunakan program ini!")
            break
        