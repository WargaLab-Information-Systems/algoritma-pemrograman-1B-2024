# NOMOR 2
print("soal nomor 2")
suku_5 = 11
suku_8_12 = 52

# Diketahui persamaan 1 : suku ke 5 = 11
# diketahui persamaan 2 : menjumlahkan suku 8 dan suku ke 12 dan hasilnya 52
# persamaan 1 : a + 4c  = 11 
# persamaan 2 : (a + 7c) + (a + 11c) = 52
# persamaan 1 kita bisa mengetahui  nilai a = 11 - 4c
# substitusi dari persamaan 2 : (11 - 4c + 7c) + (11 - 4c + 11c) = 52
# 11 + 3c + 11 + 7c = 52
# 10c + 22 = 52
# 10c = 52 - 22
# 10c = 30
#  c = 3


c = 3
a = 11 - 4 * c # menghitung suku pertama
n = 8 # jumlah suku pertama
jumlah_suku_pertama = (n/2)*(2* a + (n - 1) * c)

print(f"jumlah dari 8 suku pertama adalah {jumlah_suku_pertama} ")