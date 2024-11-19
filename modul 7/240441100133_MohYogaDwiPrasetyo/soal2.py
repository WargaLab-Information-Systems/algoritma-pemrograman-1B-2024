klub_basket = {"Agus", "Budi", "Layla", "Miya", "Akai"}
klub_renang = {"Budi", "Miya", "Lance", "Nana", "Hanabi"}

# nampilkan daftar siswa sg ngikuti kedua klub (irisan)
siswa_kedua_klub = klub_basket.intersection(klub_renang) 
print("Siswa yang mengikuti kedua klub:", siswa_kedua_klub)

# nampilkan dftar siswa sg hanya mengikuti satu klub tok
siswa_satu_klub = klub_basket.symmetric_difference(klub_renang) 
print("Siswa yang hanya mengikuti satu klub:", siswa_satu_klub)

# nampilkan dftar semua siswa unik sg ngikuti setidaknya satu dari kedua klub
siswa_setidaknya_satu_klub = klub_basket.union(klub_renang) 
print("Siswa yang mengikuti setidaknya satu dari kedua klub:", siswa_setidaknya_satu_klub)

# nampilkan jmlh siswa unik sg ngikuti setidaknya satu dari kedua klub
jumlah_siswa_setidaknya_satu_klub = len(siswa_setidaknya_satu_klub)
print("Jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub:", jumlah_siswa_setidaknya_satu_klub)
