# Denda dan batas waktu
denda_hari = 2500
denda_tambahan = 5500
batas_waktu = 5
batas_tambahan = 10

while True:
    lama_sewa = int(input("Masukkan lama sewa DVD (dalam hari): "))
    
    # Menghitung keterlambatan
    keterlambatan = lama_sewa - batas_waktu

    # Menghitung total denda
    if keterlambatan <= 0:
        total_denda = 0

    else:
        total_denda = keterlambatan * denda_hari

        if keterlambatan > batas_tambahan and batas_waktu % 5 == 0 :
            total_denda += ((keterlambatan - batas_tambahan) // 5) * denda_tambahan

    if total_denda == 0 :
        print("anda mengembalikan buku tepat waktu")
    else :
        print(f"Total denda keterlambatan: Rp {total_denda}")

    lagi = input("Ingin menghitung kembali? (ya/tidak): ")
    if lagi != 'ya':
        print("Terima kasih. Program selesai.")
        break