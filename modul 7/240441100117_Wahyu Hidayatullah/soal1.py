alat_kesehatan = {
    "tekanan_darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "inhaler": 0,
}

# Hari pertama: meminjam 2 alat pengukur tekanan darah dan 3 termometer
alat_kesehatan["tekanan_darah"] += 2
alat_kesehatan["termometer"] += 3

# Hari kedua: meminjam 4 stetoskop
alat_kesehatan["stetoskop"] += 4

# Setelah seminggu:
# Mengembalikan 1 alat pengukur tekanan darah dan 2 termometer
alat_kesehatan["tekanan_darah"] -= 1
alat_kesehatan["termometer"] -= 2

# Menukar 3 stetoskop dengan 2 alat inhaler
alat_kesehatan["stetoskop"] -= 3
alat_kesehatan["inhaler"] += 2

alat_terpinjam = set()
for alat, jumlah in alat_kesehatan.items():
    if jumlah > 0:
        alat_terpinjam.add(alat)

print("Alat kesehatan yang sedang dipinjam Heni saat ini:")
for alat, jumlah in alat_kesehatan.items():
    if jumlah > 0:
        print(f"- {alat}: {jumlah} buah")

print("\nSet alat yang sedang dipinjam saat ini:", alat_terpinjam)