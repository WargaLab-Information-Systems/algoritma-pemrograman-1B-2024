club_basket = {"Andi", "Budi", "Cici", "Dina", "Eka"}
club_renang = {"Budi", "Dina", "Fanny", "Gina", "Hadi"}

dua_club = club_basket & club_renang
print("Siswa yang mengikuti kedua klub:", dua_club)

satu_club = club_basket ^ club_renang
print("Siswa yang hanya mengikuti satu klub:", satu_club)

semua_siswa = club_basket | club_renang
print("Siswa yang mengikuti setidaknya satu klub:", semua_siswa)

print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", len(semua_siswa))
