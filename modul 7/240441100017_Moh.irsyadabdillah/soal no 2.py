# Set nama siswa yang mengikuti klub Basket dan Renang
klub_basket = {"Andi", "Budi", "Citra", "Dina", "Eka"}
klub_renang = {"Citra", "Dina", "Fajar", "Gita", "Hana"}

# a. Menampilkan dua set (anggota klub Basket dan Renang)
print("Anggota klub Basket:", klub_basket)
print("Anggota klub Renang:", klub_renang)

# b. Siswa yang mengikuti kedua klub (irisan)
kedua_klub = klub_basket & klub_renang
print("\nSiswa yang mengikuti kedua klub:", kedua_klub)

# c. Siswa yang hanya mengikuti satu klub saja (eksklusif)
satu_klub_saja = klub_basket ^ klub_renang  # Simetri difference
print("Siswa yang hanya mengikuti satu klub:", satu_klub_saja)

# d. Semua siswa unik yang mengikuti setidaknya satu dari kedua klub
semua_siswa = klub_basket | klub_renang  # Union
print("Semua siswa yang mengikuti setidaknya satu klub:", semua_siswa)

# e. Jumlah siswa unik
jumlah_siswa_unik = len(semua_siswa)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)