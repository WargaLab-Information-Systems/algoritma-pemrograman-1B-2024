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

#Seminggu
alat_kesehatan["alat pengukur tekanan darah"] -= 1
alat_kesehatan["termometer"] -= 2

#Menukar
alat_kesehatan["stetoskop"] -= 3
alat_kesehatan["inhaler"] += 2

alat_dipinjam = {alat for alat, jumlah in alat_kesehatan.items() if jumlah > 0}

print("Alat kesehatan yang sedang dipinjam Heni saat ini:")
for alat, jumlah in alat_kesehatan.items():
    if jumlah > 0:
        print(f"{alat}: {jumlah} buah")

print("\nJenis alat yang sedang dipinjam Heni:", alat_dipinjam)
