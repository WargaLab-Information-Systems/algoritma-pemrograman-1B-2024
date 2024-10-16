waktu = 0

while waktu >= 0:
    makan = input("Sudah makan?")
    if makan == "tidak":
        waktu += 15
        print(f"Total waktu persiapan anda {waktu} menit")
    else:
        continue
    
    mandi = input("Sudah mandi?")
    if mandi == "tidak":
        waktu += 10
        print(f"Total waktu persiapan anda {waktu} menit")
    else:
        continue
    
    pilihanTransportasi = input("Pilihan transportasi?")
    if pilihanTransportasi == "jalan kaki":
        waktu += 30

    elif pilihanTransportasi == "motor":
        waktu += 15 
    print(f"Total waktu persiapan dan perjalanan anda {waktu} menit")
    
    
    if waktu > 60:
        print("Anda datang tepat waktu")
    elif waktu < 60:
        print("Anda datang terlambat")
        break