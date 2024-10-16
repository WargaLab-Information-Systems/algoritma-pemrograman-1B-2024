while True:
    # Kasus 1
    makan = input("Apakah kamu sudah makan? ")
    mandi = input("Apakah kamu sudah mandi? ")
    kendaran = input("Pilih tranformasi: Motor,jalan kaki,sepeda = ")
    tranportasi = "Motor"
    mandi = 15
    kendaraan = 15
    makan = 15
    sepeda = 20

    if makan == "tidak":
        print("kamu belum makan")
    else:
        print("Kamu sudah makan")
    
    if mandi == "iya":
        print("Sudah mandi")
    else:
        print("Kamu belum mandi")

    if kendaraan == "Motor":
        print("Kamu mengguankan motor")
    else:
        print("Kamu menggunakan sepeda")
        
    total_waktu = mandi + sepeda + makan
    if total_waktu == 50:
        print("Total waktu persiapan dan perjalanan ",total_waktu ,"menit")
        print("Kamu berangkat tepat waktu")
    else:
        print("Kamu terlambat")
    
    b = input("Apakah ada yang salah? (iya/tidak) ")
    if b != "iya":
        break