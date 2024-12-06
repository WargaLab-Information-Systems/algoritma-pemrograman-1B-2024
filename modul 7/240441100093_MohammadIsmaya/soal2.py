
basket_club = {'Andi', 'Budi', 'Caca', 'Dedi', 'Evi'}
renang_club = {'Budi', 'Caca', 'Eka', 'Fia', 'Gina'}

siswa_umum = basket_club.intersection(renang_club)
print(f"Siswa yang mengikuti kedua klub: {', '.join(siswa_umum)}")

hanya_basket = basket_club - renang_club
hanya_renang = renang_club - basket_club
print(f"Siswa yang hanya mengikuti klub Basket: {', '.join(hanya_basket)}")
print(f"Siswa yang hanya mengikuti klub Renang: {', '.join(hanya_renang)}")

semua_siswa = basket_club.union(renang_club)
print(f"Semua siswa unik yang mengikuti setidaknya satu klub: {', '.join(semua_siswa)}")

total_siswa = len(semua_siswa)
print(f"Jumlah siswa unik yang mengikuti setidaknya satu klub: {total_siswa}")

