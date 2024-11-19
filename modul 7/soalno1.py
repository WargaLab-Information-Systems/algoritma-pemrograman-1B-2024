# Inisialisasi dictionary untuk mencatat jumlah alat yang dipinjam
alat_kesehatan = {
    "alat pengukur tekanan darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "inhaler": 0
}

# Hari pertama
alat_kesehatan["alat pengukur tekanan darah"] += 2
alat_kesehatan["termometer"] += 3

# Hari kedua
alat_kesehatan["stetoskop"] += 4

# Setelah seminggu
alat_kesehatan["alat pengukur tekanan darah"] -= 1
alat_kesehatan["termometer"] -= 2

# Penukaran alat
alat_kesehatan["stetoskop"] -= 3
alat_kesehatan["inhaler"] += 2

# Membuat set untuk daftar alat yang sedang dipinjam (jumlah > 0)
alat_dipinjam = {alat for alat, jumlah in alat_kesehatan.items() if jumlah > 0}

print("Alat kesehatan yang sedang dipinjam Heni:")
for alat in alat_dipinjam:
    print(f"- {alat}: {alat_kesehatan[alat]}")
