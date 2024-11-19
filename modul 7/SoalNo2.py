# Program untuk mengelola data siswa yang mengikuti klub Basket dan Renang
# # Fungsi untuk memasukkan data siswa ke dalam set
def masukkan_data(klub_nama):
    print(f"Masukkan nama siswa yang mengikuti klub {klub_nama}.")
    print("Ketik 'done' untuk berhenti memasukkan data.")
    data = set()
    while True:
        nama = input(f"Nama siswa ({klub_nama}): ").strip()
        if nama.lower() == 'done':
            break
        # Cegah input kosong
        if nama: 
            data.add(nama)
    return data

# Memasukkan data untuk kedua klub
print("=== Data Klub Basket ===")
klub_basket = masukkan_data("Basket")
print("\n=== Data Klub Renang ===")
klub_renang = masukkan_data("Renang")

# a. Menampilkan set siswa
print("\n=== Daftar Siswa ===")
print("Set siswa klub Basket:", klub_basket)
print("Set siswa klub Renang:", klub_renang)

# b. Siswa yang mengikuti kedua klub (intersection/irisan)
kedua_klub = klub_basket & klub_renang
print("\nSiswa yang mengikuti kedua klub:", kedua_klub)

# c. Siswa yang hanya mengikuti satu klub (symetric difference)
satu_klub_saja = klub_basket ^ klub_renang
print("Siswa yang hanya mengikuti satu klub:", satu_klub_saja)

# d. Semua siswa unik yang mengikuti setidaknya satu klub (union/gabungan)
semua_siswa = klub_basket | klub_renang
print("Semua siswa unik yang mengikuti setidaknya satu klub:", semua_siswa)

# e. Jumlah siswa unik
jumlah_siswa = len(semua_siswa)
print("Jumlah siswa unik:", jumlah_siswa)
