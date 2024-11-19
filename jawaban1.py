# dictionary untuk menyimpan data peminjaman awal
peminjaman_day1 = {
    'alat pengukur tekanan darah': 2,
    'termometer': 3
}

# dictionary untuk menyimpan semua peminjaman
semua_peminjaman = {}

# Memindahkan data dari peminjaman awal ke semua_peminjaman
for alat in peminjaman_day1:
    semua_peminjaman[alat] = peminjaman_day1[alat]

# peminjaman hari kedua
semua_peminjaman['stetoskop'] = 4

# pengembalian dan penukaran
def update_peminjaman(barang):
    # Pengembalian alat
    barang['alat pengukur tekanan darah'] -= 1
    barang['termometer'] -= 2
    
    # Penukaran stetoskop dengan inhaler
    barang['stetoskop'] = 1  # Dari 4 stetoskop, 3 ditukar, sisa 1
    barang['inhaler'] = 2
    
    # list untuk menyimpan alat yang akan dihapus
    alat_kosong = []
    for alat in barang:
        if barang[alat] <= 0:
            alat_kosong.append(alat)
    
    # Menghapus alat yang jumlahnya 0
    for alat in alat_kosong:
        del barang[alat]
    
    return barang

# update peminjaman
hasil_akhir = update_peminjaman(semua_peminjaman)

# Mengkonversi ke set untuk menampilkan alat apa saja yang masih dipinjam
alat_dipinjam = set()
for alat in hasil_akhir:
    alat_dipinjam.add(alat)

# Menampilkan hasil
print("Alat kesehatan yang masih dipinjam Heni:")
for alat in alat_dipinjam:
    print(f"- {alat}: {hasil_akhir[alat]} buah")