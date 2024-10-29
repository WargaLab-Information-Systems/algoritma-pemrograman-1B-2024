while True:

    total_hari_pinjam = int(input("masukkan total jumlah hari pinjaman : "))
    denda_1 = 2500
    denda_2 = 5500
    max_pinjam = 5
    total_terlambat = total_hari_pinjam - max_pinjam
    denda_wajib = total_terlambat * denda_1
    jumlah_hari_terlambat_tambahan = total_terlambat - 10 
    denda_tambahan = (jumlah_hari_terlambat_tambahan // 5)*denda_2 
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
    ulangi = input("Apakah anda ingin menghitung kembali?")
    if ulangi != "iya" :
        break
print("Program telah selesai")