# Program Semangat Ngampuss!!

waktu_max = 50
waktu_perjalanan = 0
makan = str(input("Apakah Kamu Sudah Makan??(ya/tidak)"))
waktu_makan = 15
if makan == "tidak" :
    print("Kamu Harus Makan Terlebih dahulu Selama  15 menit")
else :
    mandi = str(input("Apakah Kamu Sudah Mandi?? (ya/tidak)"))
    waktu_mandi = 10
    if mandi == "tidak" :
        print("Kamu Harus Mandi Terlebih Dahulu Selama 10 Menit") 
    else :
        transportasi = str(input("Transportasi Apa Yang Ingin Anda Gunakan??(jalan/motor)"))
        waktu_jalan = 30
        waktu_motor = 10
        if transportasi == "jalan" :
            print("Kamu Akan Sampai Kampus 30 Menit lagi")
        else :
            print("Kamu Akan Sampai Kampus 10 Menit ")


