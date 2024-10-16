while True:
    lama_sewa = int(input("Masukkan lama sewa DVD (dalam hari): "))
    keterlambatan = max(0, lama_sewa - 5)
    total_denda = 0
 
    for hari in range(1, keterlambatan + 1):
        total_denda += 2500 
        
        if hari > 10 and hari % 5 == 0:
            total_denda += 5500

    if keterlambatan > 0:
        print(f"Total denda keterlambatan: Rp.{total_denda}")
    else:
        print("DVD dikembalikan tepat waktu. Tidak ada denda.")

    if input("Hitung lagi? (ya/tidak): ").lower() != 'ya':
        print("Terima kasih telah menggunakan program ini.")
        break