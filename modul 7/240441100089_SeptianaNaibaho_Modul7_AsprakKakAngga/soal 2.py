klub_basket = {"Salsa", "Mika", "Sonia", "Dita", "Vivi"}
klub_renang = {"Sonia", "Dita", "Fizi", "James", "Berlin"}

print("Daftar siswa di klub Basket:", klub_basket)
print("Daftar siswa di klub Renang:", klub_renang)

mengikuti_kedua_klub = klub_basket & klub_renang
print("Siswa yang mengikuti kedua klub adalah:", mengikuti_kedua_klub)

mengikuti_satu_klub = (klub_basket ^ klub_renang)
print("Siswa yang hanya mengikuti satu klub adalah:", mengikuti_satu_klub)

siswa_unik = klub_basket | klub_renang
print("Siswa unik yang mengikuti setidaknya satu dari kedua klub adalah:",siswa_unik)

jumlah_siswa_unik = len(siswa_unik)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)