klub_basket = {'Jep','Roobb','Harry','Lily','Flor','Ron','Sosuke'}
klub_renang = {'Harmione','Ron','Neville','Ginny','Lily','Harry','Luna'}

# Menampilkan daftar siswa yang mengikuti kedua klub
dua_klub = klub_basket.intersection(klub_renang)
print(f"Siswa yang mengikuti dua klub yaitu klub basket dan klub renang adalah : {dua_klub}")
print()

# Menampilkan daftar siswa yang hanya mengikuti satu klub saja
satu_klub = klub_basket.union(klub_renang) - (dua_klub)
print(f"Siswa yang mengikuti satu klub saja adalah : {satu_klub}")
print()

# Menampilkan daftar semua siswa unik, setidaknya 1 dari 2 klub tersebut (min 1)
semua_siswa = klub_basket.union(klub_renang)
print(f"Menampilkan semua siswa yang mengikuti setidaknya satu klub adalah : {semua_siswa}")
print()

# Menampilkan jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub
jumlah_siswa = len(semua_siswa)
print(f"Jumlah siswa unik yang mengikuti setidaknya satu klub adalah : {jumlah_siswa}")
print()