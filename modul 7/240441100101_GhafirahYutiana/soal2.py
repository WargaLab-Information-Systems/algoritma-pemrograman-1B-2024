basket_club = {"Andi", "Melati", "Abdi", "Arif", "Fifi"}
renang_club = {"Andi", "Citra", "Fahri", "Arif", "Galih"}

print("a. Himpunan (set) dari setiap Klub")
print("   Siswa yang mengikuti klub Basket:", basket_club)
print("   Siswa yang mengikuti klub Renang:", renang_club)

siswa_kedua_klub = basket_club & renang_club
print("b. Siswa yang mengikuti kedua klub:", siswa_kedua_klub)

siswa_satu_klub = basket_club ^ renang_club
print("c. Siswa yang hanya mengikuti satu klub:", siswa_satu_klub)

siswa_unik = basket_club | renang_club
print("d. Daftar semua siswa unik yang mengikuti setidaknya satu klub:", siswa_unik)

jumlah_siswa_unik = len(siswa_unik)
print("e. Jumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)