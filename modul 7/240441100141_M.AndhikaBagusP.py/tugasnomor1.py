alatDipinjam = {
    "hari Pertama" : {
        "pengukur tekanan darah" : 2,
        "termometer" : 3
    },
    "hari kedua" : {
        "stetoskop" : 4
    }
}

print("Alat yang dipinjam hari pertama: ", alatDipinjam["hari Pertama"])
print("Alat yang dipinjam hari kedua: ", alatDipinjam["hari kedua"])

# Update pengembalian & penukaran
alatDipinjam["hari Pertama"]["pengukur tekanan darah"] -= 1
alatDipinjam["hari Pertama"]["termometer"] -= 2

alatDipinjam["hari kedua"]["stetoskop"] -= 3
alatDipinjam["hari kedua"]["alat inhaler"] = 2

jenisAlat = set()
for alat in alatDipinjam["hari Pertama"]:
    jenisAlat.add(alat)

for alat in alatDipinjam["hari kedua"]:
    jenisAlat.add(alat)
    
print("Jenis alat yang dipinjam: ")
print(jenisAlat)