basket = {'Alice', 'Bob', 'Charlie', 'David', 'Eva'}
renang = {'Bob', 'Charlie', 'Frank', 'Grace', 'Alice'}

kedua_klub = basket.intersection(renang)
print("Siswa yang mengikuti kedua klub:")
print(kedua_klub)

hanya_satu_klub = basket.symmetric_difference(renang)
print("\nSiswa yang hanya mengikuti satu klub:")
print(hanya_satu_klub)

semua_siswa = basket.union(renang)
print("\nSemua siswa yang mengikuti setidaknya satu klub:")
print(semua_siswa)

jumlah_siswa = len(semua_siswa)
print("\nJumlah siswa unik yang mengikuti setidaknya satu klub:")
print(jumlah_siswa)