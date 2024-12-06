klub_basket = {"Aldi", "Aby", "Lia", "Dina", "Toni"}
klub_renang = {"Aby", "Lia", "Fani", "Gilang", "Hana"}

print("Klub Basket:", klub_basket)
print("Klub Renang:", klub_renang)


siswa_kedua_klub = klub_basket & klub_renang
print("Siswa yang mengikuti kedua klub:", siswa_kedua_klub)

siswa_satu_klub = (klub_basket ^ klub_renang)
print("Siswa yang hanya mengikuti satu klub:", siswa_satu_klub)

siswa_setidaknya_satu = klub_basket | klub_renang  
print("Daftar semua siswa unik yang mengikuti setidaknya satu klub:", siswa_setidaknya_satu)

jumlah_siswa_unik = len(siswa_setidaknya_satu)
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)
