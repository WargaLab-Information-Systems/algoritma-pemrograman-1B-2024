while True:
    lama_waktu_meneyewa = int(input("Masukkan total hari penyewaan : "))
    dendalebih5hari = 2500
    telatlebih10hari = 5500
    total = 0

    for i in range(1, lama_waktu_meneyewa + 1):
        if i > 5:
            total += dendalebih5hari
            if i % 10 == 0:
                total += telatlebih10hari
    if lama_waktu_meneyewa > 5:
        print("Anda telah terlambat mengembalikan DVD selama ", lama_waktu_meneyewa-5,"hari, anda terkena denda Rp. ", total)
    
        ulang = (input("Apakah anda ingin menghitung ulang (yes/no) : "))
        if ulang == "yes":
            continue
        else:
            break
    else:
        pass