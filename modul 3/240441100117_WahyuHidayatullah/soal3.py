while True:
    harian = 2500
    lebih_10_hari = 5500
    total = 0
    hari = int(input("Berapa hari lama penyewaan DVD anda: "))

    for i in range(hari+1):
        if i > 5:
            total += harian
            if i % 10 == 0:
                total += lebih_10_hari
    if hari > 5 :
        print("Pengembalian DVD anda sudah lebih dari 5 hari dan terlambat selama", hari-5 ,"hari dan total", total)
    else:
        print("DVD dikembalikan tepat waktu tidak ada denda")
    hitung_lagi = input("Apakah Anda ingin menghitung lagi? (iya/tidak): ")
    if hitung_lagi != "iya":
        print("Terima kasih telah menyewa DVD di toko kami.")
        break