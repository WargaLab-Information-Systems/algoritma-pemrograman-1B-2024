dendaperhari = 2500 #denda
dendatambahan = 5500 #5hari keterlambatan dalam 10 hari

while True:
    lamasewa = int(input("Masukkan lama waktu penyewaan (dalam hari): "))
    keterlambatan = lamasewa - 5
    totaldenda = 0

    if keterlambatan > 0:
        totaldenda += keterlambatan * dendaperhari
        if keterlambatan > 10:
            denda_tambahan_hari = (keterlambatan ) // 5
            totaldenda += denda_tambahan_hari * dendatambahan

    print("Total denda keterlambatan: Rp.", totaldenda)

    ulang = str(input("Apakah Anda ingin menghitung kembali? (y/n):= "))
    if ulang == 'n':
        break
       