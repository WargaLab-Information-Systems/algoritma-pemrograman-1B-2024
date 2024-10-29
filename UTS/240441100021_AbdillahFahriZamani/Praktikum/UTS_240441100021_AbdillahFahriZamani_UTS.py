nama = str(input("masukan nama :"))

while True :
    makan = str(input("apakah anda sudah makan? (sudah/belum)")).lower().strip()
    if makan != "sudah" :
        waktu_makan = 15
    else :
        waktu_makan = 0

    mandi = str(input("apakah anda sudah mandi? (sudah/belum)")).lower().strip()
    if mandi != "sudah" :
        waktu_mandi = 10
    else :
        waktu_mandi = 0

    transportasi = str(input("menggunakan transportasi apa anda untuk ke kampus? (jalan/motor)")).lower().strip()
    waktu = 0
    if transportasi == "jalan" :
        waktu += 30

    elif transportasi == "motor" :
        waktu += 15

    else :
        waktu

    total_waktu = waktu_makan + waktu_mandi + waktu
    print(f"total waktu persiapan dan perjalanan: {total_waktu} menit")
    if total_waktu >= 50 :
        print(f"{nama} telat untuk ke kampus")
    else :
        print(f"{nama} tepat waktu berangkat ke kampus")


    ulang = input("\napakah anda ingin mengulang? (ya/tidak)").lower().strip()
    if ulang != "ya" :
        print("Terima kasih. Program selesai.")
        break
