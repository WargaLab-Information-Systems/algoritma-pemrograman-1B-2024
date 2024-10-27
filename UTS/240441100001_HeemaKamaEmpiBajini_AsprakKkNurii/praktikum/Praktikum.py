# belum_makan = 15
# belum_mandi= 10
# jalan_kaki= 30
# motor= 15
waktu_tiba= 60

makan = str(input("apakah sudah bakan atau belum? (yes/no): "))
mandi= str(input("apkah sudah mandi atau belum? (yes/no):"))
transportasi= str(input("berangkat menggunakan: (jalan kaki/motor): "))
jumlah = 0

play = True
while True:
    if makan == "yes":
        print("lanjut")
        if mandi == "yes":
            print("lanjut")
            if transportasi == "jalan kaki":
                jumlah += 30
                if transportasi == "motor":
                    jumlah += 15
                else:
                    break



if makan == "no":
    jumlah += 15
    if mandi== "no":
        jumlah += 10
        play = False


