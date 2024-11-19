klub_basket = {"Adib", "Balbal", "Shandy", "Dinda", "Ayahka"}
klub_renang = {"Balbal", "Shandy", "Asa", "Gindari", "Dani"}

print("Siswa di klub Basket:", klub_basket)
print("Siswa di klub Renang:", klub_renang)

siswa_kedua_klub = klub_basket & klub_renang
print("\nSiswa yang mengikuti kedua klub:", siswa_kedua_klub)

siswa_satu_klub = (klub_basket ^ klub_renang) 
print("\nSiswa yang hanya mengikuti satu klub saja:", siswa_satu_klub)

siswa_unik = klub_basket | klub_renang
print("\nDaftar semua siswa unik yang mengikuti setidaknya satu klub:", siswa_unik)

jumlah_siswa_unik = len(siswa_unik)
print("\nJumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)