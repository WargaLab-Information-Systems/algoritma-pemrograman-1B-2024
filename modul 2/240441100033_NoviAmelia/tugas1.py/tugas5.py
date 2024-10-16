#input dari penguna
nama_Pembeli = input("masukkan nama pembeli:")
usia_Pembeli = int(input("masukkan usia pembeli:"))

#cek usia pembeli
if usia_Pembeli < 18:
    print("maaf usia anda belum mencukupi")
else:
    total_harga = float(input("masukkan total harga belanja:"))
    member = input("apakah memiliki kartu member? (ya/tidak):")
    
    #hitung diskon
    diskon = 0
    if member :
        diskon += 0.15 #diskon 15% untuk member
    if total_harga > 500000:
        diskon += 0.10 #diskon tambahan 10% jika total belanja > 500.000

total_diskon = total_harga * diskon
harga_setelah_diskon = total_harga - total_diskon

#output hasil
print(f"nama pembeli: {nama_Pembeli}")
print(f"total harga sebelum diskon : Rp{total_harga}")
print(f"diskon yang didapatkan: Rp{total_diskon}")
print(f"total harga setelah diskon: Rp{harga_setelah_diskon}")