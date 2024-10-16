while True:
    lamaPeminjaman = int(input("Masukkan jumlah lama peminjaman: "))
    denda = int(2500) #Lebih dari 5 hari
    denda2 = int(5500) #Lebih dari 10 hari (denda/5hari)
    totalDenda = 0
   
    if lamaPeminjaman > 5:
        keterlambatan = lamaPeminjaman - 5
        totalDenda += keterlambatan * denda

        if keterlambatan > 10: 
            tambahanDenda = ((keterlambatan - 10) // 5) * denda2
            totalDenda += tambahanDenda     
    print(f"Denda yang harus dibayar: Rp.{totalDenda}")
    
    tanya = input("Apakah anda ingin menghitung kembali?[y/n]")
    if tanya == "n":
        print("Terima kasih")
        break