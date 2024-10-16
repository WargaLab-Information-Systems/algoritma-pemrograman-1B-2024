
nama_pembeli = input("Masukkan nama pembeli: ")
usia = int(input("Masukkan usia pembeli: "))

# Cek usia
if usia < 18:
    print("Maaf, usia anda belum mencukupi.")
else:
    # Input total harga
    total_harga =int(input("Masukkan total belanja: Rp "))
    member = input("Apakah anda memiliki kartu member (ya/tidak)? ")

    # Cek diskon
    diskon = 0
    if member == "ya" and total_harga > 500000:
        diskon = 25
    elif total_harga > 500000:
        diskon = 10
    elif member == "ya" :
        diskon = 15
    # Hitung total harga setelah diskon
    total_setelah_diskon = total_harga - (total_harga * diskon / 100)

    # Tampilkan hasil
    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Diskon yang didapatkan: {diskon}%")
    print(f"Total harga sebelum diskon: Rp {total_harga:}")
    print(f"Total harga setelah diskon: Rp {int(total_setelah_diskon): }")