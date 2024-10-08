# Input data
U5 = 11 
U8_dan_U12 = 52 

# mencari persamaan suku pertama (a)
# a + 4b = U5
# U8 + U12 = (a + 7b) + (a + 11b) = 2a + 18b = 52 -> a = 26 - 9b

# Menghitung beda (b)
# a + 4b = U5 
# (26 - 9b) + 4b = 11
# 26 - 5b = 11
# -5b = -15
b = 3

# Menghitung suku pertama (a)
a = 26 - 9 * b 

# Hitung jumlah 8 suku pertama
n = 8 #suku8 
U8 = (n / 2 ) * (2 * a + (n -1) * b)

# Hasil
print(f"Jumlah 8 suku pertama deret aritmetika adalah {U8}")