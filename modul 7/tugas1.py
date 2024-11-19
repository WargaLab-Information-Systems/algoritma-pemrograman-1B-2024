
peminjaman = {
    "pengukur_tekanan_darah" : 0,
    "termometer" : 0,
    "stetoskop" : 0,
    "inhaler" : 0
}

# hari 1
peminjaman["pengukur_tekanan_darah"] += 2
peminjaman["termometer"] += 3

# hari 2
peminjaman["stetoskop"] += 4

# stlh seminggu
peminjaman["pengukur_tekanan_darah"] -= 1
peminjaman["termometer"] -= 2
peminjaman["stetoskop"] -= 3
peminjaman["inhaler"] += 2

print("Alat yang dipinjam Heni saat ini : ")
print(peminjaman)