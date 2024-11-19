#Membuat dua set untuk siswa yang mengikuti masing-masing klub
klub_basket = {"Andi", "Budi", "Citra", "Dewi", "Eka"}
klub_renang = {"Citra", "Fikri", "Gita", "Budi", "Hani"}

#Menampilkan daftar siswa yang mengikuti masing-masing klub
print("a. Daftar siswa yang mengikuti klub basket:", klub_basket)
print("   Daftar siswa yang mengikuti klub renang:", klub_renang)

#Menampilkan daftar siswa yang mengikuti kedua klub (irisan)
siswa_kedua_klub = klub_basket & klub_renang
print("b. Siswa yang mengikuti kedua klub:", siswa_kedua_klub)

#Menampilkan daftar siswa yang hanya mengikuti satu klub saja (Xor)
siswa_satu_klub = klub_basket ^ klub_renang
print("c. Siswa yang hanya mengikuti satu klub:", siswa_satu_klub)

#Menampilkan daftar semua siswa unik yang mengikuti setidaknya satu klub (gabungan)
siswa_unik = klub_basket | klub_renang
print("d. Daftar semua siswa unik:", siswa_unik)

#Menampilkan jumlah siswa unik ()
jumlah_siswa_unik = len(siswa_unik)
print("e. Jumlah siswa unik:", jumlah_siswa_unik)
