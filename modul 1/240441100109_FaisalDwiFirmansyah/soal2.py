# MENENTUKAN JUMLAH NILAI DARI 8 SUKU PERTAMA
# Diketahui
u5 = 11
u8_plus_u12 = 52

# Menghitung beda deret (b) dan suku pertama (a)
# u5: a + 4b = 11
# u8 dan u12: (a + 7b) + (a + 11b) = 52

# Menggunakan dua persamaan
# a + 4
# b = 11
# 2a + 11b = 52

# Kita bisa menyelesaikan b terlebih dahulu
# 2a + 18b = 52 -> a = 11 - 4b
# Substitusi ke dalam persamaan kedua

# 2(11 - 4b) + 18b = 52
# 22 - 8b + 18b = 52
# 10b = 30
b = 3  # Diperoleh dari 10b = 30
a = u5 - 4 * b  # a = 11 - 4 * 3
a = -1

# Menghitung jumlah 8 suku pertama dengan rumus  Sn = (n/2)*(2a+(n-1)b)
n = 8
Sn = (n/2)*(2*a+(n-1)*b)
print("Jadi, jumlah nilai dari 8 suku pertama adalah: ", Sn)