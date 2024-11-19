alat_kesehatan = {
    "alat pengukur tekanan darah": 2,
    "termometer": 3,
    "stetoskop": 0,
    "inhaler": 0
}

alat_kesehatan["stetoskop"] += 4

alat_kesehatan["alat pengukur tekanan darah"] -= 1
alat_kesehatan["termometer"] -= 2
alat_kesehatan["stetoskop"] -= 3
alat_kesehatan["inhaler"] += 2

alat_kesehatan_aktif = {alat: jumlah for alat, jumlah in alat_kesehatan.items() if jumlah > 0}

print("Alat kesehatan yang masih dipinjam oleh Heni:")
for alat, jumlah in alat_kesehatan_aktif.items():
    print(f"{alat}: {jumlah} buah")