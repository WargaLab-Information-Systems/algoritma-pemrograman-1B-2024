# for b in range(-10, 11):
#     a5 = 11
#     a = a5 - 4 * b
#     if 2 * a + 18 * b == 52:
#         jumlah_8_suku = 8 * a + (7 * 8 // 2) * b
#         print("Suku pertama (a): ", a)
#         print("Beda (b): ", b)
#         print("Jumlah 8 suku pertama: " , jumlah_8_suku)

u5 = 11
u8_plus_u12 = 52
b = (u8_plus_u12-2*u5)/10
a = u5-4*b

n=8
jumlah_8_suku=n*(2*a+(n-1)*b)/2

print(f"suku pertama(a)={a}")
print(f"beda(b)={b}")
print(f"jumlah 8 suku pertama={jumlah_8_suku}")