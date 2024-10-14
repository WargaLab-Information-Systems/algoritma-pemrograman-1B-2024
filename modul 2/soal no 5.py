nama_pembeli = input("Masukkan nama pembeli:")
usia = int(input("Masukkan usia pembeli:"))
total_belanja =int(input("Masukkan total belanja (Rp):"))
member_input = input("apakah anda memiliki kartu member?(ya/tidak): ")

if usia < 18: # Memeriksa usia
    print("Maaf usia anda belum mencukupi")
else:
    diskon = 0 # Menghitung diskon
    member = (member_input == 'ya')

    if member:
        diskon += 15
    if total_belanja > 500000:
        diskon += 10

    total_sebelum_diskon = total_belanja

    total_setelah_diskon = total_belanja * (1-diskon / 100)

print(f"\nNama Pembeli: {nama_pembeli}")
print(f"diskon yang didapatkan: {diskon}%")
print(f"total harga sebelum diskon: Rp.{total_sebelum_diskon}")
print(f"total harga setelah diskon: Rp.{int(total_setelah_diskon)}")