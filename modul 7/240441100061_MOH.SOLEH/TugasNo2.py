klub_basket = {"Celiboy", "Sutsujin", "Gebi", "Lydia", "Kiboy"}
klub_renang = {"Sutsujin", "Gebi", "Anavel", "Wann", "Kayes"}

print("Klub Basket : ")
print(klub_basket)
print()

print("Klub Renang : ")
print(klub_renang)
print()

siswa_kedua_klub = klub_basket & klub_renang # irisan (intersection)
print("Siswa yang mengikuti kedua klub : ")
print(siswa_kedua_klub)
print()

siswa_satu_klub = (klub_basket ^ klub_renang) # Simetris difference (selisih simetris)
print("Siswa yang hanya mengikuti satu klub : ")
print(siswa_satu_klub)
print()

siswa_setidaknya_satu = klub_basket | klub_renang # union (gabungan)
print("Daftar semua siswa unik yang mengikuti setidaknya satu klub : ")
print(siswa_setidaknya_satu)
print()

jumlah_siswa_unik = len(siswa_setidaknya_satu) 
print("Jumlah siswa unik yang mengikuti setidaknya satu klub : ")
print(jumlah_siswa_unik)
print()