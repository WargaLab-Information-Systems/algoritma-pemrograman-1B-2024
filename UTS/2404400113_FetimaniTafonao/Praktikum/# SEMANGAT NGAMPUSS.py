# SEMANGAT NGAMPUSS

while True:
    eat = 15
    bath =10
    walk = 30
    motor = 15
    total = 0

    makan = input ("sudah? (ya/tidak)")
    mandi = input("sudah? (ya/tidak)")
    trans = input("pilih transportasi (jalan kaki/menggunakan sepeda motor):")


    if makan == "tidak" : 
    total += eat
    if mandi == "tidak" :
        total += bath
        if trans == "jalan kaki" :
            total == walk 
            if trans == "motor" :
                total == "motor"

    if total < 50:
        print("Total waktu persiapan dan perjalanan : ", total)
        print("kamu berangkat tepat waktu.")
        break
else:
    print("kamu terlambat")
    break
if makan != "ya" or makan != "tidak" or mandi != "tidak" or trans != "jalan kaki" or trans != "motor":
    pass
else:
    print("kamu terlambat")
    break

