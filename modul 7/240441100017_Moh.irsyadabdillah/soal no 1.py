# Dictionary untuk mencatat jumlah alat kesehatan
alat_kesehatan = {
    "pengukur_tekanan_darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "inhaler": 0
}

# Proses peminjaman dan pengembalian
# Hari pertama
alat_kesehatan["pengukur_tekanan_darah"] += 2
alat_kesehatan["termometer"] += 3

# Hari kedua
alat_kesehatan["stetoskop"] += 4

# Setelah seminggu
# Pengembalian
alat_kesehatan["pengukur_tekanan_darah"] -= 1
alat_kesehatan["termometer"] -= 2

# Penukaran stetoskop dengan inhaler
alat_kesehatan["stetoskop"] -= 3
alat_kesehatan["inhaler"] += 2

# Menampilkan alat kesehatan yang masih dipinjam
alat_dipinjam = {alat for alat, jumlah in alat_kesehatan.items() if jumlah > 0}

# Hasil akhir
print("Jumlah alat kesehatan yang dipinjam Heni:")
for alat, jumlah in alat_kesehatan.items():
    if jumlah > 0:
        print(f"- {alat.replace('_', ' ').capitalize()}: {jumlah}")

print("\nAlat kesehatan yang masih dipinjam (sebagai set):", alat_dipinjam)