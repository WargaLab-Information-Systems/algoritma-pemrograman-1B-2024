# a. Membuat dua set yang berisi nama siswa yang mengikuti klub Basket dan Renang
basket = {'alan', 'jihar', 'jois', 'ibrah', 'aris'}
renang = {'alan', 'rafly', 'jois', 'kifah', }

# b. Menampilkan daftar siswa yang mengikuti kedua klub (irisan)
dua_klub = basket.intersection(renang)
print("Siswa yang mengikuti kedua klub:", dua_klub)

# c. Menampilkan daftar siswa yang hanya mengikuti satu klub saja
# Siswa yang hanya mengikuti klub Basket
# Siswa yang hanya mengikuti klub Renang
hanya_basket = basket - renang
hanya_renang = renang - basket
satu_klub = hanya_basket.union(hanya_renang)
print("Siswa yang hanya mengikuti satu klub:", satu_klub)

# d. Menampilkan daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub
siswa_terdaftar = basket.union(renang)
print("Semua siswa unik yang mengikuti setidaknya satu klub:", siswa_terdaftar)

# e. Menampilkan jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub
total_terdaftar = len(siswa_terdaftar)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", total_terdaftar)
