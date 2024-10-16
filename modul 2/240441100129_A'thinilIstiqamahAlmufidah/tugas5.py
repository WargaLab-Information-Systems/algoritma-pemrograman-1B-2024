nama_pembeli = input("Masukkan nama pembeli : ")
usia = int(input("masukkan usia pembeli : "))
                   
if usia < 18 :
    print ("maaf usia anda belum mencukupi")
else :
    total_belanja = int(input("masukkan total belanja : Rp "))

    member = input("Apakah anda memiliki member (ya/tidak)?")

# diskon 
diskon = 0 
if member == "ya" :
    diskon  += 15 
if total_belanja > 500000 :
    diskon += 10

total_diskon =total_belanja*(diskon/100)
total_harga_setelah_diskon =int(total_belanja - total_diskon)

print(f"\nNama Pembeli : {nama_pembeli}")
print(f"Diskon yang didapatkan : {diskon}%")
print(f"Total Harga Sebelum Diskon : Rp {total_belanja}")
print(f"Total Harga Setelah Diskon : Rp{total_harga_setelah_diskon}")