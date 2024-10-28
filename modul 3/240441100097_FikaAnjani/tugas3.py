# while True:
#     lama_peminjaman = int(input("Masukkan lama keterlambatan (dalam hari): "))
#     denda_pokok = 2500
#     denda_tambahan = 5500

#     if lama_peminjaman > 10:
#         sisa_hari = lama_peminjaman - 10
#         tambahan_denda = sisa_hari // 5 * denda_tambahan
#     total_denda += tambahan_denda
#         print("Total denda yang harus dibayar: Rp",)
#     elif lama_peminjaman >5 <10:
#         lama_sewa_5 = (lama_peminjaman - 5)*denda_pokok
#         print("Total denda yang harus dibayar: Rp",lama_sewa_5")
#     else:
#         print("tidak ada denda yang perlu dibayar")
#     lanjut = input("Ingin menghitung lagi? (ya/tidak): ")
#     if lanjut != 'ya':
#         break
        
# while True:
#     lama_peminjaman = int(input("Masukkan lama keterlambatan (dalam hari): "))
#     denda_pokok = 2500
#     denda_tambahan = 5500
#     lama_sewa_5 = (lama_peminjaman - 5)*denda_pokok
#     if lama_peminjaman <5 >10 :
#         print("Total denda yang harus dibayar: Rp",lama_sewa_5)

while True :
    lama_sewa = int(input("masukkan lama penyewaan DVD : "))

    if lama_sewa <= 5 :
        print(("anda mengembalikkan tepat waktu"))
    else :
        keterlambatan = lama_sewa - 5 
        denda = keterlambatan * 2500

        if keterlambatan > 10 :
            lama_keterlambatan = keterlambatan - 5 
            denda_tambahan = (lama_keterlambatan // 5) * 5500
            denda += denda_tambahan 

        print("total denda keterlambatan yang anda bayar adalah : Rp", denda)

    lanjut = input("Ingin menghitung lagi? (ya/tidak): ")
    if lanjut != 'ya':
        break