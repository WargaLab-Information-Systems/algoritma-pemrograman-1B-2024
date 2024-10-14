nama_pembeli = input("Masukkan nama pembeli : ")
usia = int(input("Masukkan usia anda : "))

if usia < 18 :
    print("Maaf usia anda belum cukup ")
    exit()
else :
    total_belanja = int(input("Masukkan tottal belanja anda : rp "))
    member = input("apakah anda memiliki member (y/t)? ")

diskon = 0
if member == "y" :
    diskon += 15
    if total_belanja > 500000 :
        diskon += 10

total_diskon = total_belanja*(diskon/100)
total_harga_setelah_diskon = (total_belanja - total_diskon)

print("\nNama pembeli : ", nama_pembeli)
print("Diskon yang di dapat : ", diskon ,"%")
print("Total harga sebelum diskon : Rp ",total_belanja)
print("Total harga setelah diskon : Rp ",total_harga_setelah_diskon)