# Inisialisasi set masing-masing klub
klub_basket = {'Andi', 'Budi', 'Citra', 'Diana', 'Eko', 'Fandi'}
klub_renang = {'Budi', 'Diana', 'Gita', 'Hani', 'Iko'}

# a. Set sudah dibuat di atas dengan beberapa nama contoh

print("=== Analisis Keanggotaan Klub ===")
print("\nAnggota Klub Basket:", klub_basket)
print("Anggota Klub Renang:", klub_renang)

# b. Menampilkan siswa yang mengikuti kedua klub
siswa_dua_klub = klub_basket.intersection(klub_renang)
print("\nSiswa yang mengikuti kedua klub:", siswa_dua_klub)

# c. Menampilkan siswa yang hanya mengikuti satu klub
hanya_basket = klub_basket - klub_renang
hanya_renang = klub_renang - klub_basket

print("\nSiswa yang hanya ikut klub Basket:", hanya_basket)
print("Siswa yang hanya ikut klub Renang:", hanya_renang)

# d. Menampilkan semua siswa yang mengikuti minimal satu klub
semua_siswa = klub_basket.union(klub_renang)
print("\nDaftar seluruh siswa yang mengikuti minimal satu klub:", semua_siswa)

# e. Menampilkan jumlah siswa yang mengikuti minimal satu klub
jumlah_total_siswa = len(semua_siswa)
print("\nJumlah total siswa yang mengikuti minimal satu klub:", jumlah_total_siswa)

# Informasi tambahan
print("\n=== Statistik Klub ===")
print(f"Jumlah anggota Klub Basket: {len(klub_basket)}")
print(f"Jumlah anggota Klub Renang: {len(klub_renang)}")
print(f"Jumlah siswa yang mengikuti kedua klub: {len(siswa_dua_klub)}")