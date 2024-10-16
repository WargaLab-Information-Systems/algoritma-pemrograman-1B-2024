nama = str(input("Nama pembeli: "))
usia = int(input("masukkan usia anda: "))
if usia < 18:
    print("Maaf usia anda belum mencukupi")
    quit()
#total harga belanja
total_harga = int(input("Total harga belanja: Rp "))
kartu_member = input("Apakah anda mempunyai kartu member? (y/n): ")
diskon = 0

if kartu_member == "y":
    diskon += 15
    print("Anda mendapatkan diskon 15%.")
else:
    print("Anda tidak mendapatkan diskon 15%.")

# Cek total belanja untuk diskon tambahan
if total_harga > 500000:
    diskon += 10
    print("Anda mendapatkan diskon tambahan 10%")

# Hitung total harga setelah diskon
total_diskon = (diskon / 100) * total_harga
total_setelah_diskon = total_harga - total_diskon

# Hasil
print("=================HASIL PEMBELIAN=======================")
print(f"Nama Pembeli: {nama}")
print(f"Total harga sebelum diskon: Rp {total_harga}")
print(f"Diskon yang didapat: {diskon}%")
print(f"Total harga setelah diskon: Rp {total_setelah_diskon}")
print("=======================================================")