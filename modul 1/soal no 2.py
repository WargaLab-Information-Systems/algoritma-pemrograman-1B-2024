# mencari d/selisih 
# 2(11 - 4.d) + 18.d = 52
# 22 - 8.d + 18.d = 52
# 10.d = 30
#  d = 3

# mencari a/suku pertama 
# a = suku_ke_5 - 4 * d
# a = hasil suku yang sudah di ketahui - (suku ke berapa -1) * selisih 
# a = 11 - 4 * 3
# a = -1

# Diketahui 
# a = suku pertama = -1
# d = selisih setiap suku = 3

# suku ke-5 (a + 4.d) = 11
# suku ke_8 (a + 7.d) + suku ke-12 (a + 11.d) = 52

# Diketahui 
suku_ke_5 = 11
suku_ke_8_dan_12 = 52
d = 3
a = suku_ke_5 - 4 * d

suku = int(input("masukkan suku yang ingin di cari :"))

mencari_suku = a + (suku-1)*d

print(f"suku ke {suku} bernilai = {mencari_suku}")

# jumlah dari 8 suku pertama: s8 = (n/2)(2a + (n-1)d)
n = int (input("masukkan suku deret aritmatika yang ingin dicari : "))
jumlah_8_suku = int(n / 2) * (2 * a + (n - 1) * d)

print(f"jumlah 8 suku pertama dari deret aritmatika adalah : {jumlah_8_suku}")