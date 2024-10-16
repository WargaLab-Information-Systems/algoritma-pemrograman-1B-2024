# variabel 
jam_makan = 15
jam_mandi = 10
total = 0

lanjut = 'yes'
while lanjut == 'yes':
    makan = input("Apakah kamu sudah makan (ya/tidak)? ")
    mandi = input("Aapkah kamu sudah mandi (ya/tidak)? ")
    motor = 15
    jalan_kaki= 30
    if makan == "tidak":
        total += jam_makan
        if makan == "ya":
            total += 0
            if mandi == "tidak":
                total += jam_mandi
                if mandi == "ya" :
                    total += 0
    else:
        print("anda terlambat")
        print(total)
        
        perjalanan = input("pilih transportasi Anda (motor/jalan kaki): ")
        if perjalanan == "motor":
            total += motor
            if perjalanan == "jalan_kaki" :
                total += jalan_kaki
        else:
            print("anda terlambat")
            print(total)
            break

lanjut = input("apakah anda ingin mengulang? (ya/tidak)")