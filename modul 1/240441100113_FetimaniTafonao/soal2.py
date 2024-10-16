# a = suku pertama
# b = perbedaan
# Persamaan pertama: a + 4b = 11
#     Persamaan kedua: 2a + 18b = 52
    
#     Dari persamaan pertama, kita bisa cari a:
#     a = 11 - 4b
#     Substitusi ke persamaan kedua:
#     2(11 - 4b) + 18b = 52
#     22 - 8b + 18b = 52
#     10b = 30
#     b = 3

# suku pertama
b = int(input("Masukkan b dari hasil subtitusi : ")) 
a = 11 - 4 * b

# hitung jumlah 8 suku pertama
s_8 = 4 * (2 * a + 7 * b)

print("Suku pertama =", a)
print ("Jumlah 8 suku pertama adalah",s_8)

