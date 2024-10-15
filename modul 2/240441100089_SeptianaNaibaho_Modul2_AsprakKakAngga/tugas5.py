nama_pembeli = input("Masukkan nama pembeli :")
usia_pembeli = int(input("Masukkan usia pembeli :"))

if usia_pembeli < 18:
    print("Maaf usia anda belum mencukupi")
    exit()

    
else:
    total_belanja = int(input("Masukkan total belanja : Rp"))
    kartu_member = input("Apakah anda memiliki kartu member? (ya/tidak)")

    diskon= 0

    if kartu_member == "ya" :
        diskon += 15
    if total_belanja >500000 :
        diskon += 10

total_diskon = total_belanja * (diskon/100)
total_harga_setelah_diskon = int(total_belanja - total_diskon)

print(f"\nNama Pembeli : {nama_pembeli}")
print(f"Diskon yang didapatkan: {diskon}%")
print(f"Total harga sebelum diskon : RP{total_belanja}")
print("Total harga setelah diskon : Rp{total_harga_setelah_diskon:}")


