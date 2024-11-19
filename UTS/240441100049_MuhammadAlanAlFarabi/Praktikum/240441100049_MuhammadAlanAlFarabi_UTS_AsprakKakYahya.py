jalan = 60
motor = 15
makanT = 15
mandiT = 10
makan = str(input())
mandi = str(input())
t = 0
while True:
    if mandi == "ya":
        if mandi == "ya":
            transportasi = str(input("pilih transportasi"))
            if transportasi == "motor":
                print("waktu persiapan dan perjalanan adalah " , motor)
                print("kamu tepat waktu")
            else:
                print("waktu persiapan dan perjalanan adalah " , jalan)
                print("kamu terlambat")
        else:
            t2 = t + mandi
            transportasi = input()
            if transportasi == "motor":
                print("waktu persiapan dan perjalanan adalah " , motor)
                if t2 + motor >= 50:
                    print("terlambat")
                else:
                    print("tepat waktu")
            else:
                print("waktu persiapan dan perjalanan adalah " , jalan)
                if t2 + jalan >= 50:
                    print("terlambat")
                else:
                    print("tepat waktu")
    else:
        t = 0
        t1 = t + makan
        transportasi = input()
        if transportasi == "motor":
            print("waktu persiapan dan perjalanan adalah " , motor)
            if t1 + motor >= 50:
                print("terlambat")
            else:
                print("tepat waktu")
        else:
            print("waktu persiapan dan perjalanan adalah " , jalan)
            if t1 + jalan >= 50:
                print("terlambat")
            else:
                print("tepat waktu")
    hari = str(input())
    if hari != "selesai": break
