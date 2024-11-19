# Inisialisasi set untuk siswa yang mengikuti klub Basket dan Renang
klub_basket = {"lia", "Budi", "Citra", "Dian", "Eva"}
klub_renang = {"Citra", "Fajar", "Gita", "lia"}

# a. Menampilkan daftar siswa yang mengikuti kedua klub
siswa_kedua_klub = klub_basket & klub_renang    #irisan  
print("Siswa yang mengikuti kedua klub:", siswa_kedua_klub)

# b. Menampilkan daftar siswa yang hanya mengikuti satu klub
siswa_satu_klub = klub_basket ^ klub_renang #difference symettric  #selisih #ada di salah satu tapi tidak keduanya
print("Siswa yang hanya mengikuti satu klub:", siswa_satu_klub)

# c. Menampilkan daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub
siswa_unik = klub_basket | klub_renang #union
print("Siswa yang mengikuti setidaknya satu klub:", siswa_unik)

# d. Menampilkan jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", len(siswa_unik)) #per elemen

