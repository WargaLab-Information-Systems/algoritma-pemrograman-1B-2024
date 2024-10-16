while True:
    lama_peminjaman = int(input("Berapa Lama Anda Meminjaman DVD (hari) :"))
    if lama_peminjaman <= 5 :
        print("Terimakasih Telah mengembalikan Tepat Waktu,Anda tidak Mendapatkan Denda Keterlambatan")
    else :
        lama_keterlambatan = lama_peminjaman - 5
        denda_pokok = 2500
        denda_tambahan  = 5500

        total_denda = lama_keterlambatan * denda_pokok

        if lama_keterlambatan > 10:
            sisa_hari = lama_keterlambatan - 10
            tambahan_denda = (sisa_hari // 5) * denda_tambahan
            total_denda += tambahan_denda
            
        print(f"Total Lama Keterlambatan adalah {lama_keterlambatan} Hari")
        print("Total Denda Yang Harus Dibayar : Rp. ", total_denda)
    lanjut = input("Apakah Anda Ingin Melakukan Perhitungan Ulang? (ya/tidak)")
    if lanjut != "ya":
        print("Terimakasih Telah Menggunakan Program Kami!")
        break