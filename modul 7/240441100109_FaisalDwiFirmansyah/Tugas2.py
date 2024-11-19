klub_basket = {'Ambaki','Azka','Fuad','Faiz','Slapur','Rusdi','Ghafur'}
klub_renang = {'Hardin','Rusdi','Agung','Eldi','Faiz','Fuad','Ahmad'}

kedua_klub = klub_basket.intersection(klub_renang)
print(f"Siswa yang mengikuti kedua club adalah : {kedua_klub}")

satu_klub = klub_basket.symmetric_difference(klub_renang) - (kedua_klub)
print(f"Siswa yang mengikuti satu klub saja adalah : {satu_klub}")

semua_siswa = klub_basket.union(klub_renang)
print(f"Menampilkan semua siswa yang mengikuti setidaknya satu klub adalah : {semua_siswa}")

jumlah_siswa = len(semua_siswa)
print(f"Jumlah siswa unik yang mengikuti setidaknya satu klub adalah : {jumlah_siswa}")
