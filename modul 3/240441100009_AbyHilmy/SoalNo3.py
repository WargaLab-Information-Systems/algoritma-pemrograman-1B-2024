while True:
    # Meminta input dari pengguna
    lama_sewa = int(input("Masukkan lama sewa DVD (dalam hari): "))
    keterlambatan = lama_sewa - 5
    denda = 0
    
    # Menghitung keterlambatan
    for hari in range (1, keterlambatan + 1):
        denda += 2500

        if hari > 10 and hari % 5 == 0:
            denda += 5500
            
    # Menampilkan total denda
    print("Total denda keterlambatan: Rp.", denda)

    # Menanyakan apakah ingin menghitung kembalii
    lagi = input("Apakah Anda ingin menghitung kembali? (ya/tidak): ").strip().lower()
    if lagi != 'ya':
        break
