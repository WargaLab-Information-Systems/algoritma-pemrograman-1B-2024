klub_basket = {"Ani", "Udin", "Citra", "Dewi"}
klub_renang = {"Udin", "Dewi", "Farah", "Gita"}

siswa_kedua_klub = klub_basket.intersection(klub_renang)
print("Siswa yang mengikuti kedua klub (Basket dan Renang):", siswa_kedua_klub)

siswa_satu_klub = klub_basket.symmetric_difference(klub_renang)
print("Siswa yang hanya mengikuti satu klub saja:", siswa_satu_klub)

siswa_unik = klub_basket.union(klub_renang)
print("Daftar semua siswa yang mengikuti setidaknya satu dari kedua klub:", siswa_unik)

jumlah_siswa_unik = len(siswa_unik)
print("Jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub:", jumlah_siswa_unik)