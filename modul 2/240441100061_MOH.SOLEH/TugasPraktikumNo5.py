# Memasukkan nama dan usia dengan apa yang di minta 
nama = input("Siapa Nama Anda : ")
usia = int(input("Berapa Usia Anda : "))

# Kita cek apakah usianya mencukupi
if usia < 18:
    print("Maaf usia anda belum mencukupi")
    exit()
# Apakah anda punya kartu member, dan total belanja anda 
else:
    total_belanja = int(input("Masukkan total belanja anda : Rp "))
    kartu_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

# Inisialisasi diskon
diskon = 0 

# Cek Diskon yang di peroleh berdasarkan member
if kartu_member == kartu_member:
    diskon += 15 # Diskon 15% jika anda punya kartu member

# Cek diskon berdasarkan total belanja
if total_belanja > 500000:
    diskon += 10 # Diskon tambahan 10% jika anda belanja lebih dari 500.000 ribu

# Hitung total diskon dan harga akhir
total_diskon = (diskon / 100) * total_belanja
total_harga_setelah_diskon = total_belanja - total_diskon

# Bentuk Tampilan Hasilnya
print("===---⭐⭐⭐---=== STRUK PEMBELIAN ===---⭐⭐⭐---===")
print(f"Nama Pembeli : {nama}")
print(f"Diskon yang di dapatkan : {diskon}%")
print(f"Total harga sebelum Diskon : Rp{total_belanja: }")
print(f"Total harga setelah diskon : Rp{total_harga_setelah_diskon: }")
print("======== TERIMA KASIH TELAH BELANJA DI SINI ========")