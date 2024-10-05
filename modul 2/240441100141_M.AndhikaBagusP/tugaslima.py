# input data
nama = input("Masukkan nama anda: ")
usia = int(input("Masukkan usia anda: "))
kartuMember = input("Apakah anda memiliki kartu member?[y/n]: ")
totalBelanja = int(input("Masukkan total belanja anda: "))
diskon = 0

if usia < 18:
    print("Maaf usia anda belum mencukupi")
    exit()
    
else:
    # menentukan diskon
    if kartuMember == "y":
        diskon += 0.15 # persentase 15% menjadi desimal 0.15
    elif totalBelanja >= 500000:
        diskon += 0.10 # persentase 10% menjadi desimal 0.10
        
# rumus harga setelah diskon
hargaDiskon = int(totalBelanja * (1 - diskon))
        
# Hasil        
print(f"Hai {nama}, anda mendapatkan diskon sebesar {diskon}, harga awal sebesar {totalBelanja} jadi anda hanya membayar {hargaDiskon}")