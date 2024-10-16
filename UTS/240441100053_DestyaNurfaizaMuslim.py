# SEMANGAT NGAMPUSSS

while True: 
    eat = 15
    bath = 10
    walk = 30
    motor = 15
    total = 0

    makan = input("Sudah makan? (ya/tidak)")
    mandi = input("Sudah mandi? (ya/tidak)")
    trans = input("Pilih transportasi (jalan kaki/menggunakan motor):")

    if makan == "tidak":
        total += eat
    if mandi == "tidak":
        total += bath
    if trans == "jalan kaki":
        total += walk
    if trans == "motor":
            total += motor
    if total < 50:
        print("Total waktu persiapan dan perjalanan :", total, "menit")
        print("Kamu berangkat tepat waktu.")
        break
    else:
        print("Kamu terlambat")   
        
    if makan != "ya" and makan != "tidak" and mandi != "ya" and mandi != "tidak" and trans!="jalan kaki" and trans!= "menggunakan motor":
        continue 
