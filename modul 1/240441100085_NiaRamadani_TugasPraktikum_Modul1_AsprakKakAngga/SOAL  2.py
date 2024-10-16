# SOAL  2

Suku_5 = 11
Suku_8_12 = 52

# Persamaan 1 : a + 4d = 11
# persamaan 2 : (a + 7d) + (a + 11d) = 52
# Dari persamaan 1 : a = 11 - 4d
# Subtitusi persamaan 2 :
# (11 - 4d + 7d) + (11 - 4d + 11d) = 52
# 11 + 3d + 11 + 7d = 52
# 22 + 10d = 52
# 10d = 30
# d = 3


d = 3
a = 11 - 4 * d   #Suku pertama
n = 8            #Jumlah suku pertama

Jumlah_suku_pertama = int(n / 2)*(2 * a + (n - 1) * d)

print(f"Jumlah nilai dari 8 suku pertama  adalah: {Jumlah_suku_pertama}")


