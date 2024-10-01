# Menghitung jumlah nilai dari 8 suku pertama
# NO 2

# Diketahui 
U5 = 11 # Suku ke-5
jmlh_U8_U12 = 52 # Jumlah suku ke-8 dan suku ke-12

# Dari persamaan a + 4b = 11 (suku ke-5)
# Kita bisa mengepresikan a sebagai a = 11 - 4b

# ( a + 7b ) + ( a + 11b ) = 52
# Substitusi ke persamaan kedua: 2a + 18b = 52

# Selesaikan untuk b
# 2(11 - 4b) + 18b = 52
# 22 - 8b + 18b = 52
# 10b = 30
# b = 3

b = 3 

# Setelah kita dapat b, kita masukkan ke persamaan a = 11 - 4b
a = 11 - 4 * b 

# Sekarang kita punya a dan b
print(f"Suku pertama (a): {a}")
print(f"Beda (b): {b}")

# Menghitung jumlah 8 suku pertama
n = 8
jumlah_suku_8_pertama = (n / 2) * (2 * a + (n - 1) * b)

print(f"Jumlah 8 suku pertama : {jumlah_suku_8_pertama}")