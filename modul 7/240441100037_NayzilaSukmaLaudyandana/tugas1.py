alat_kesehatan = {
    "pengukur_tekanan_darah": 2, 
    "termometer": 3,
    "stetoskop": 4,              
    "inhaler": 0
}

alat_kesehatan["pengukur_tekanan_darah"] -= 1
alat_kesehatan["termometer"] -= 2
alat_kesehatan["stetoskop"] -= 3
alat_kesehatan["inhaler"] += 2

alat_tersisa = {alat for alat, jumlah in alat_kesehatan.items() if jumlah > 0}  
print("Alat yang sedang dipinjam Heni saat ini:")
for alat in alat_tersisa:
    print(f"- {alat}: {alat_kesehatan[alat]}")
