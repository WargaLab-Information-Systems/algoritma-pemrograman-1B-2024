# a. Daftar siswa yang mengikuti klub Basket dan Renang
klub_basket = {"Siti", "Tika", "Sholeh", "Naysila", "Arif"}
klub_renang = {"Sholeh", "Diana", "Amel", "Tika", "Elfina"}

print("Klub Basket:", klub_basket)
print("Klub Renang:", klub_renang)

# b. Menampilkan daftar siswa yang mengikuti kedua klub
siswa_kedua_klub = klub_basket & klub_renang
print("Siswa yang mengikuti kedua klub:", siswa_kedua_klub)

# c. Menampilkan daftar siswa yang hanya mengikuti satu klub saja
siswa_hanya_basket = klub_basket - klub_renang
siswa_hanya_renang = klub_renang - klub_basket
siswa_hanya_satu_klub = siswa_hanya_basket | siswa_hanya_renang
print("Siswa yang hanya mengikuti satu klub:", siswa_hanya_satu_klub)

# d. Menampilkan daftar semua siswa unik yang mengikuti setidaknya satu klub
siswa_unik = klub_basket | klub_renang
print("Siswa yang mengikuti setidaknya satu klub:", siswa_unik)

# e. Menampilkan jumlah siswa unik yang mengikuti setidaknya satu klub
jumlah_siswa_unik = len(siswa_unik)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)