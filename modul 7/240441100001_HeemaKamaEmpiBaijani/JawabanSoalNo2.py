
"""
    |--------------------------------------------------------------------------
    | Pertanyaan
    |--------------------------------------------------------------------------
    |
    | A. Membuat dua set yang berisi nama siswa yang mengikuti klub renang dan basket
    | B. Menampilkan daftar siswa yang mengikuti kedua klub
    | C. Menampilkan daftar siswa yang hanya mengikuti satu klub saja
    | D. Menampilkan daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub
    | E. Menampilkan jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut
    |
    |
    |
"""
# Poin A
basket = {"dimas", "wing", "bagas", "bimantara", "batari", "lintang"}
renang = {"dimas", "lintang", "pramesti", "bagas"}

# Poin B
print("Siswa yang mengikuti kedua klub:")
print(basket.intersection(renang))

# Poin C
print("Siswa yang hanya mengikuti satu klub saja:")
print(basket.symmetric_difference(renang))

# Poin D
print("Siswa unik yang mengikuti setidaknya satu dari kedua klub:")
print(basket.union(renang))

# Poin E
print("Jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub:")
print(len(basket.union(renang)))

