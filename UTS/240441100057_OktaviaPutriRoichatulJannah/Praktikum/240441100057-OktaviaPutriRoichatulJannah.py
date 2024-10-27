
print("=====SEMANGAT NGAMPUSS!=====")

makan = input("Apakah kamu sudah makan (ya/tidak) ? ")
mandi = input("Apakakh kamu sudah mandi (ya/tidak) ? ")
transportasi = input("Transportasi apa yang kamu gunakan (jalan/motor) :")
total_waktu = 0


while True:
    if makan != "ya":
        total_waktu += 15
    if mandi != "ya" :
        total_waktu += 10
    if transportasi == "jalan":
        total_waktu +=  30
    else :
        total_waktu += 15

    print(f"Total waktu persiapan dan perjalanan anda adalah {total_waktu} menit")

    if total_waktu < 50:
        print("Kamu berangkat tepat waktu")
    else:
        print("Terlambat")


    if makan == "ya" or makan == "tidak" or mandi == "ya" or mandi == "tidak" or transportasi == "jalan" or transportasi == "motor":
        print("input sesuai")
        break
    else:
        print("program selesai")   
                
    

