while True:
    lama_sewa = int(input("Masukkan lama sewa DVD (dalam hari): "))
        
    # Hitung keterlambatan
    keterlambatan = lama_sewa - 5
    total_denda = 0
    if lama_sewa > 5:
        denda_hari = keterlambatan * 2500
        total_denda += denda_hari
    if keterlambatan > 10 :
        denda_tambahan = ((keterlambatan - 10) // 5) * 5500
        total_denda += denda_tambahan   
    print(f"Total denda keterlambatan: Rp {total_denda}")

    #menghitung kembali
    hitung_lagi = input("Apakah Anda ingin menghitung kembali? (ya/tidak): ")
    if hitung_lagi != 'ya':
        break

