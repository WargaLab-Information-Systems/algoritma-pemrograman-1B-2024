alat_kesehatan = {
    "Pengukur Tekanan Darah" : 0,
    "Termometer" : 0,
    "Stetoskop" : 0,
    "Inhaler" : 0
}

# Hari Pertama
alat_kesehatan["Pengukur Tekanan Darah"] += 2
alat_kesehatan["Termometer"] += 3

# Hari Kedua
alat_kesehatan["Stetoskop"] += 4

# Setelah Seminggu
# dikembalikan
alat_kesehatan["Pengukur Tekanan Darah"] -= 1
alat_kesehatan["Termometer"] -= 2

# ditukar
alat_kesehatan["Stetoskop"] -= 3
alat_kesehatan["Inhaler"] += 2

print("Alat Kesehatan yang Dipinjam Heni Saat Ini Adalah : ")
for alat, total in alat_kesehatan.items():
    print(f"{alat} : {total}")