# Inisialisasi dictionary kosong untuk menyimpan inventaris alat kesehatan
alat_kesehatan = {}

# Fungsi untuk menambah alat ke inventaris
def tambah_alat(alat, jumlah):
    if alat in alat_kesehatan:
        alat_kesehatan[alat] += jumlah
    else:
        alat_kesehatan[alat] = jumlah

# Fungsi untuk mengurangi alat dari inventaris
def kurangi_alat(alat, jumlah):
    if alat in alat_kesehatan:
        alat_kesehatan[alat] -= jumlah
        # Hapus alat jika jumlahnya 0
        if alat_kesehatan[alat] <= 0:
            del alat_kesehatan[alat]

# Hari pertama: meminjam 2 alat pengukur tekanan darah dan 3 termometer
tambah_alat("Alat Pengukur Tekanan Darah", 2)
tambah_alat("Termometer", 3)

# Hari kedua: meminjam 4 stetoskop
tambah_alat("Stetoskop", 4)

# Setelah seminggu:
# - Mengembalikan 1 alat pengukur tekanan darah dan 2 termometer
kurangi_alat("Alat Pengukur Tekanan Darah", 1)
kurangi_alat("Termometer", 2)

# - Menukar 3 stetoskop dengan 2 alat Inhaler
kurangi_alat("Stetoskop", 3)
tambah_alat("Inhaler", 2)

# Mengubah dictionary menjadi set untuk mendapatkan daftar unik alat yang dipinjam
alat_dipinjam = set(alat_kesehatan.keys())

# Menampilkan hasil
print("\nDaftar alat yang dipinjam Heni saat ini:")
for alat in alat_dipinjam:
    print(f"{alat}: {alat_kesehatan[alat]} buah")