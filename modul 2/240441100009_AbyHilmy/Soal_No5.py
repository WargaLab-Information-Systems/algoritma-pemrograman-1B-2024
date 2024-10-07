# Mengambil input dari pengguna
nama_pembeli = input("Masukkan nama pembeli: ")
usia_pembeli = int(input("Masukkan usia pembeli: "))

# Memeriksa usia pembeli
if usia_pembeli < 18:
    print("Maaf, usia anda belum mencukupi.")
else:
    total_belanja = float(input("Masukkan total belanja: "))
    kartu_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ")
    # Menentukan diskon
    diskon = 0
    if kartu_member == 'ya':
        diskon += 15
    if total_belanja > 500000:
        diskon += 10
    
    # Menghitung total harga setelah diskon
    total_harga_sebelum_diskon = total_belanja
    total_harga_setelah_diskon = total_harga_sebelum_diskon * (1 - (diskon / 100))
    
    # Menampilkan hasil
    print(f"Nama Pembeli: {nama_pembeli}")
    print(f"Diskon yang didapat: {diskon}%")
    print(f"Total harga sebelum diskon: Rp{total_harga_sebelum_diskon:}")
    print(f"Total harga setelah diskon: Rp{total_harga_setelah_diskon:}")
