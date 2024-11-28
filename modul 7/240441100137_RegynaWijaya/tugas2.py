klub_basket = {"Andi", "Budi", "Cici", "Dodi", "Eka"}
klub_renang = {"Cici", "Dodi", "Fani", "Gita", "Hani"}

siswa_kedua_klub = klub_basket & klub_renang
print("Siswa yang mengikuti kedua klub (Basket dan Renang):")
print(siswa_kedua_klub)

siswa_satu_klub = (klub_basket ^ klub_renang)
print("Siswa yang hanya mengikuti satu klub saja:")
print(siswa_satu_klub)

siswa_unik = klub_basket | klub_renang
print("Daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub:")
print(siswa_unik)

jumlah_siswa_unik = len(siswa_unik)
print("Jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub:")
print(jumlah_siswa_unik)
