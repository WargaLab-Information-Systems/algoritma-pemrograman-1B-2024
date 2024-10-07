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
        diskon += 15
    if totalBelanja >= 500000:
        diskon += 10
        
# rumus harga setelah diskon
hargaDiskon = int((diskon / 100) * totalBelanja)
hargaSetelahDiskon = totalBelanja - hargaDiskon
        
# Hasil        
print(f"Hai {nama}, anda mendapatkan diskon sebesar {diskon}%, harga awal sebesar Rp.{totalBelanja} jadi anda hanya membayar Rp.{hargaSetelahDiskon}")