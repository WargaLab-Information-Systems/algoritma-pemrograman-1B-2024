makan = input("sudah makan ? (ya/tidak)")
mandi = input("sudah mandi (ya/ tidak)")
trasportasi1 = input("pilih transportasi (jalan kaki/motor) : ")
jam_makan = 15
jam_mandi = 10
total = 0


while True :
    if makan == "tidak":
        total += 15
    if mandi == "tidak":
        total += 10
        if trasportasi1 == "jalan kaki":
            total += 30
            if trasportasi1 == "motor":
                total += 15
                if total < 50:
                 print ("kamu terlambat")
                 if total > 50:
                     print ("kamu tidak terlambat")
                


