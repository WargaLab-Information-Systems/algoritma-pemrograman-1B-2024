print("=== Program Pendataan Anggota Klub Ekstrakurikuler ===")

# dictionary untuk menyimpan data klub dan anggotanya
klub_ekstrakurikuler = {
   'Basket': {'Andi', 'Budi', 'Cindy', 'Dodi', 'Ega'},
   'Renang': {'Budi', 'Cindy', 'Farah', 'Gita', 'Hani'}
}

# set anggota masing-masing klub
anggota_basket = klub_ekstrakurikuler['Basket']
anggota_renang = klub_ekstrakurikuler['Renang']

print("\na) Daftar anggota setiap klub:")
print("Klub Basket:", anggota_basket)
print("Klub Renang:", anggota_renang)

# siswa yang ikut kedua klub (intersection)
ikut_dua_klub = anggota_basket.intersection(anggota_renang)
print("\nb) Siswa yang mengikuti kedua klub:", ikut_dua_klub)

# siswa yang hanya ikut satu klub (symmetric_difference)
ikut_satu_klub = anggota_basket.symmetric_difference(anggota_renang)
print("\nc) Siswa yang hanya mengikuti satu klub:", ikut_satu_klub)

# detail siswa yang hanya ikut satu klub
print("\nDetail siswa yang hanya ikut satu klub:")
print("Hanya ikut Basket:", anggota_basket - anggota_renang)
print("Hanya ikut Renang:", anggota_renang - anggota_basket)

# semua siswa yang ikut klub (union)
semua_siswa = anggota_basket.union(anggota_renang)
print("\nd) Daftar semua siswa yang ikut klub:", semua_siswa)

# Menghitung jumlah siswa unik
jumlah_siswa = len(semua_siswa)
print("\ne) Jumlah siswa unik yang mengikuti klub:", jumlah_siswa, "siswa")

# Membuat dictionary ringkasan statistik
statistik_klub = {
   'Total Siswa Unik': jumlah_siswa,
   'Ikut Kedua Klub': len(ikut_dua_klub),
   'Hanya Ikut Satu Klub': len(ikut_satu_klub),
   'Anggota Basket': len(anggota_basket),
   'Anggota Renang': len(anggota_renang)
}

print("\n=== Ringkasan Statistik ===")
for kategori, jumlah in statistik_klub.items():
   print(f"{kategori}: {jumlah} siswa")