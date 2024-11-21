klubBasket = {"bagong", "ririn", "agus"}
klubRenang = {"bayu", "siti", "memet", "ririn"}

print("Siswa mengikuti klub basket", klubBasket)
print("Siswa mengikuti klub renang", klubRenang)
print("Daftar siswa yg mengikuti kedua klub", klubBasket.intersection(klubRenang))
print("Daftar siswa yg mengikuti 1 klub", klubBasket.symmetric_difference(klubRenang))

totalSiswa = set(klubBasket.union(klubRenang))
print("daftar siswa unik yang mengikuti 1 dari kedua klub", totalSiswa)
print("jumlah siswa unik yang mengikuti 1 dari kedua klub: ", len(totalSiswa))