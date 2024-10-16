# Definisikan fungsi untuk menghitung diskon
def hitung_diskon(harga_total, adalah_anggota, usia):
    if usia < 18:
        return "Maaf usia anda belum mencukupi"
    
    diskon = 0
    if adalah_anggota:
        diskon += 0.15
    if harga_total > 500000:
        diskon += 0.10
    
    return diskon

# Input pembeli
nama_pembeli = input("Masukkan nama pembeli: ")
usia_pembeli = int(input("Masukkan usia pembeli: "))
adalah_anggota = input("Apakah pembeli memiliki kartu member? (y/n): ")
harga_total_sebelum_diskon = int(input("Masukkan total harga sebelum diskon: "))

# Hitung diskon
diskon = hitung_diskon(harga_total_sebelum_diskon, adalah_anggota.lower() == 'y', usia_pembeli)

if isinstance(diskon, str):
    print(diskon)
else:
    # Hitung harga total setelah diskon
    harga_total_setelah_diskon = harga_total_sebelum_diskon * (1 - diskon)
    
    # Cetak hasil
    print("Nama Pembeli:", nama_pembeli)
    print("Diskon yang didapatkan:", diskon * 100, "%")
    print("Total harga sebelum diskon:", harga_total_sebelum_diskon)
    print("Total harga setelah diskon:", harga_total_setelah_diskon)