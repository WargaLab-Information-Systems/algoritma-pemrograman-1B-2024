alat_kesehatan = {
    "alat_pengukur_tekanan_darah": 2,
    "termometer": 3,
    "stetoskop": 4,
    "inhaler": 0
}

alat_kesehatan["alat_pengukur_tekanan_darah"] -= 1
alat_kesehatan["termometer"] -= 2

# Menukar 
alat_kesehatan["stetoskop"] -= 3
alat_kesehatan["inhaler"] = 2

print("Alat kesehatan yang masih dipinjam Heni saat ini:")
for alat, jumlah in alat_kesehatan.items():
    print(f"{alat}: {jumlah}")
