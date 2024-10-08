# suku_5 = 11
# suku_8_12 = 52
# persamaan 1 : a = 4d - 11
# persamaan 2 : (a + 7d) + (a + 11d) = 52
# substitusi persamaan 2 :
# (11 - 4d + 7d) + (11 - 4d + 11d) = 52
# 11 + 3d + 11 + 7d = 52
# 22 + 10d = 52
# 10d = 30
# d = 3
# d = selisih antar jarak antar suku

d = 3
a = 11 -4 * d #suku pertama
n = 8 #jumlah suku pertama
jumlah_suku_pertama = (n / 2)*(2 * a + (n - 1) *d)
print("jumlah nilai dari 8 suku pertama adalah", (jumlah_suku_pertama))

