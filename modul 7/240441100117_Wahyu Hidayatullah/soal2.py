klub_basket = {"Kapten Pais", "Ambape", "Mas Fuad", "Mr.Ironi", "Ambaki"}
klub_renang = {"Rusdi", "Mas Fuad", "Ambaki", "Bernadit", "Ambalabu"}

kedua_klub = klub_basket.intersection(klub_renang) # irisan
only_club = klub_basket.symmetric_difference(klub_renang) # simestris untuk  yang sama diffrence untuk perselihihan
all_klub = klub_basket.union(klub_renang)
total = len(all_klub)
print(f"\nSiswa yang mengikuti kedua club: {kedua_klub}")
print(f"\nSiswa yang hanya mengikuti satu klub saja: {only_club}")
print(f"\nDaftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub: {all_klub}")
print(f"\nJumlah siswa unik yang mengikuti setidaknya satu dari kedua klub: {total}")