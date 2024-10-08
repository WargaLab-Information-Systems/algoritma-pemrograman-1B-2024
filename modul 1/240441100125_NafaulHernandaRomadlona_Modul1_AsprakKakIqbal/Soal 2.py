# Diketahui
suku_ke_5 = 11
suku_ke_8_plus_suku_ke_12 = 52

# Menghitung beda deret (d) dan suku pertama (a)
# Dari suku ke-5: a + 4d = 11
# Dari suku ke-8 dan suku ke-12: (a + 7d) + (a + 11d) = 52

# Menggunakan dua persamaan
# a + 4
# d = 11
# 2a + 11d = 52

# Kita bisa menyelesaikan d terlebih dahulu
# 2a + 18d = 52 -> a = 11 - 4d
# Substitusi ke dalam persamaan kedua

# 2(11 - 4d) + 18d = 52
# 22 - 8d + 18d = 52
# 10d = 30
d = 3  # Diperoleh dari 10d = 30
a = suku_ke_5 - 4 * d  # a = 11 - 4 * 3
a = -1

# Menghitung jumlah 8 suku pertama
jumlah_8_suku = 8 * (2 * a + 7 * d) / 2
print("Jumlah 8 suku pertama adalah:", jumlah_8_suku)

# START

# // Diketahui
# suku_ke_5 ← 11
# suku_ke_8_plus_suku_ke_12 ← 52

# // Hitung beda deret (d)
# d ← (suku_ke_8_plus_suku_ke_12 - 2 * suku_ke_5) / 6

# // Hitung suku pertama (a)
# a ← suku_ke_5 - 4 * d

# // Hitung jumlah 8 suku pertama
# jumlah_8_suku ← 8 * (2 * a + 7 * d) / 2

# // Tampilkan hasil
# PRINT "Jumlah 8 suku pertama adalah:", jumlah_8_suku

# END
