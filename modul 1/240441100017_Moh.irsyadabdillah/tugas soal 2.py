#diketahui
U5 = 11
U8_tambah_U12 = 52

#dari persamaan diatas didapatkan rumus untuk mencari a dan b sebagai berikut
b = (U8_tambah_U12 - 2 * U5) / 10
a = U5 - 4 * b

#menghitung jumlah 8 suku pertama
n = 8
S8 = n / 2 * (2 * a + (n - 1) * b)

#output hasil
print(f"U5 = {U5}")
print(f"U8_tambah_U12 = {U8_tambah_U12}")
print(f"nilai a adalah {a}")
print(f"nilai b adalah {b}")
print(f"hasil penjumlahan dari 8 suku pertama adalah {S8}")