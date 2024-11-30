# Mendefinisikan alat kesehatan yang dipinjam Heni menggunakan dictionary
alat_pinjam = {
    "pengukur_tekanan_darah": 2,  # 2 alat pengukur tekanan darah pada hari pertama
    "termometer": 3,              # 3 termometer pada hari pertama
    "stetoskop": 4                # 4 stetoskop pada hari kedua
}
print(f"peminjaman di hari pertama",{alat_pinjam["pengukur_tekanan_darah"]})
# Proses peminjaman awal telah dilakukan, sekarang melakukan pengembalian dan penukaran:
# Heni mengembalikan 1 alat pengukur tekanan darah dan 2 termometer
alat_pinjam["pengukur_tekanan_darah"] -= 1
alat_pinjam["termometer"] -= 2

# Heni menukar 3 stetoskop dengan 2 alat inhaler
alat_pinjam["stetoskop"] -= 3
# Menambahkan 2 alat inhaler ke dalam dictionary
if "inhaler" in alat_pinjam:
    alat_pinjam["inhaler"] += 2
else:
    alat_pinjam["inhaler"] = 2

# Menampilkan hasil alat kesehatan yang dipinjam Heni saat ini
print("Alat kesehatan yang dipinjam Heni saat ini:")
for alat, jumlah in alat_pinjam.items():
    print(f"{alat}: {jumlah}")
