# variabel gaji L(Lembur) dan R(reguler)
r = 100000 * 7
l = 0
jam = 0
for hari in range(1, 7 + 1):
    print(f"apakah anda lembur hari ke-{hari} (ya/tidak)")
    lembur = str(input("jawaban anda: "))
    while lembur != "ya" and lembur != "tidak":
        print("tolong jawab dengan ya dan tidak")
        print(f"apakah anda lembur hari ke-{hari}? (ya/tidak)")
        lembur = str(input("jawaban anda: "))
    if lembur == "ya":
        print(f"berapa lama anda melakukan lembur pada hari ke-{hari}? ")
        lama = int(input("Jawaban anda: "))
        if lama < 4:
            jam = jam + lama
            l = 25000 * lama
        elif lama >= 4 and lama < 6:
            jam = jam + lama
            l = l + 100000
        elif lama >= 6 and lama < 8:
            jam = jam + lama
            l = l + 200000
        elif lama == 8:
            jam = jam + lama
            l = l + 300000
        else:
            jam = jam + lama
            print(f"lembur hari ke-{hari} sudah melebihi batas ketentuan, anda tidak mendapat gaji lembur hari ke-{hari}")

    else:
        print(f"anda tidak lembur pada hari ke-{hari}. tentu saja tidak dapat gaji lembur")
    
    
    print(f"Sementara gaji anda adalah {l}")
    print(f"Sementara total waktu anda dari hari ke hari adalah {jam}")


    if jam > 40:
        print("Anda lembur sudah melebihi batas")
        break
    

total = l + r
hariL = total // 7
print(f"Gaji lembur dalam 1 minggu adalah : {l}")
print(f"Gaji anda keseluruhan adalah: {total}")
print(f"Gaji anda perhari rata rata adalah: {hariL}")
