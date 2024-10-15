while True:

    total_hari_pinjam = int(input("masukkan total jumlah hari pinjaman : "))
    max_pinjam = 5
    total_terlambat = total_hari_pinjam - max_pinjam
    denda1 = 2500
    denda2 = 5500
    denda_wajib = total_terlambat * denda1
    jumlah_hari_terlambat_tambahan = total_terlambat - 10 
    denda_tambahan = (jumlah_hari_terlambat_tambahan // 5)* denda2
    total_denda = denda_wajib + denda_tambahan


    if total_hari_pinjam <= max_pinjam:
        print("Anda Berhasil mengembalikan DVD")

    else:
        if total_terlambat >= 10:
            print("Total hari terlambat : ", total_terlambat)
            print ("Anda harus membayar denda sebesar Rp.",total_denda)

        else:        
            print("Total hari terlambat : ", total_terlambat)
            print ("Anda harus membayar denda sebesar Rp. ",denda_wajib)
    ulangi = input("Apakah anda ingin menghitung kembali? (ya/tidak)")
    if ulangi != "iya" :
        break
print("Baik, Terima kasih sudah menggunakan program ini <3")