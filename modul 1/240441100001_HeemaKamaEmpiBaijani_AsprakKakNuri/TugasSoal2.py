#PROGRAM MENYELESAIKAN MASALAH DARMAJI MENCARI JUMLAH NILAI DARI 8 SUKU PERTAMA
print("PROGRAM MENCARI NILAI DARI 8 SUKU PERTAMA")
# DIKETAHUI
# u5 = 11
# u8 + u12 = 52
# deret 1 sampai 8
# Un = a + (n-1) b 
u5_n = 5
u8_n = 8
u12_n = 12

# TODO: mencari persamaan 1
u5_total = 11
u5_a = 1
u5_b = (u5_n - 1)
print(f"Persamaan (1) : a + {u5_b}b = {u5_total}")

# TODO: mencari persamaan 2
u8_a = 1
u8_b = (u8_n - 1)
u12_a = 1
u12_b = (u12_n - 1)
u8_u12_total = 52

u8_u12_a = u8_a + u12_a
u8_u12_b = u8_b + u12_b

print(f"Persamaan (2) : {u8_u12_a}a + {u8_u12_b}b = {u8_u12_total}")

# TODO: mencari nilai a dan b, dengan subtitusi
u5_b *= -1
print(f"Persamaan (3) : a = {u5_total} {u5_b}b")

# subtitusi persamaan 3 ke persamaan 2 dan mendapatkan nilai b
b = (52 - (u8_u12_a * u5_total) ) / ((u8_u12_a * u5_b) + u8_u12_b)
print(f"Nilai b : {b}")
a = u5_total + (u5_b * b)
print(f"Nilai a : {a}")


# TODO: cari deret 1 sampai 8
u1 = a + (1 - 1) * b
u2 = a + (2 - 1) * b
u3 = a + (3 - 1) * b
u4 = a + (4 - 1) * b
u5 = a + (5 - 1) * b
u6 = a + (6 - 1) * b
u7 = a + (7 - 1) * b
u8 = a + (8 - 1) * b

print(f"Deret 1 sampai 8 : {u1}, {u2}, {u3}, {u4}, {u5}, {u6}, {u7}, {u8}")

penjumlahan = u1 + u2 + u3 + u4 + u5 + u6 + u7 + u8
print (f"jadi jumlah banyak suku dari 8 suku pertama adalah sebanyak: {penjumlahan}")

