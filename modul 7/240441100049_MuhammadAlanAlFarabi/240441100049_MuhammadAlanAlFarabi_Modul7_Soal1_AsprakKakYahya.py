barang_pinjam = {
    'alat pengukur tekanan darah': 0,
    'termometer': 0,
    'stetoskop': 0,
    'alat inhaler': 0
}

# a. hari pertama
barang_pinjam['alat pengukur tekanan darah'] += 2
barang_pinjam['termometer'] += 3

# b. hari kedua
barang_pinjam['stetoskop'] += 4

# c. setelah 1 minggu
barang_pinjam['alat pengukur tekanan darah'] -= 1
barang_pinjam['termometer'] -= 2
barang_pinjam['stetoskop'] -= 3
barang_pinjam['alat inhaler'] += 2 


print("Alat kesehatan yang dipinjam saat ini:")
for alat, jumlah in barang_pinjam.items():
    print(alat, jumlah)