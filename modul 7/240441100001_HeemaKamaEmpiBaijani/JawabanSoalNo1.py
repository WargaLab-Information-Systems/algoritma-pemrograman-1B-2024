alat_kesehatan= {
    "pengukur Tekanan Darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "inhaler": 0
}

jenisAlat= set()

alat_kesehatan["pengukur Tekanan Darah"] += 2
alat_kesehatan["termometer"]+= 3
jenisAlat.update(["pengukur Tekanan Darah", "termometer"])

alat_kesehatan["stetoskop"]+=4
jenisAlat.add("stetoskop")

alat_kesehatan["pengukur Tekanan Darah"]-= 1
alat_kesehatan["termometer"]-=2

if alat_kesehatan["pengukur Tekanan Darah"] == 0:
    jenisAlat.discard("pengukur Tekanan Darah")
if alat_kesehatan ["termometer"] == 0:
    jenisAlat.discard("stetoskop")

alat_kesehatan["stetoskop"] -=3
alat_kesehatan["inhaler"] +=2

if alat_kesehatan["inhaler"] > 0:
    jenisAlat.add("inhaler")
    
if alat_kesehatan["stetoskop"] == 0:
    jenisAlat.discard("stetoskop")

print("\njenis alat yang dipinjam heni: ")
for alat in jenisAlat:
    print(f"{alat}: {alat_kesehatan[alat]}")