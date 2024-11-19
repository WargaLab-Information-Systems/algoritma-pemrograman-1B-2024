alat_kesehatan = {
    "pengukur tekanan darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "inhaler": 0
}

def tambah_alat(alat, jumlah):
    alat_kesehatan[alat] += jumlah

def kurang_alat(alat, jumlah):
    alat_kesehatan[alat] -= jumlah
    if alat_kesehatan[alat] <= 0:
        alat_kesehatan.pop(alat)

# day 1 peminjaman
tambah_alat('pengukur tekanan darah', 2)
tambah_alat('termometer', 3)

# day 2 peminjaman
tambah_alat('stetoskop', 4)

# pengembalian dan penukaran
kurang_alat('pengukur tekanan darah', 1) # pengembalian
kurang_alat('termometer', 2) #pengembalian
kurang_alat('stetoskop', 3) #penukaran
tambah_alat('inhaler', 2) #penukaran

print("\nAlat kesehatan yang masih dipinjam heni saat ini: ")
for alat, jumlah in alat_kesehatan.items():
    print(f"- {alat}: {jumlah} unit")

print("\nJenis alat yang masih dipinjam: ")
for alat in alat_kesehatan:
    print(f"- {alat}")