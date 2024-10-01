print("====no 2====")

u5 = 11
u8_ditambah_u12 = 52

# dari rumus Un = a + (n-1)*b dapat diketahui
# persamaan 1 --> 11 = a + 4*b)
# persamaan 2 --> 52 = 2*a + 18*b (di sederhanakan dengan membagi di kedua ruas)
# --> 26 = a + 9*b
# dari persamaan 2 - persamaan 1 dapat diketahui
b = 3
a = 11 - 4 * b
print(f"nilai b adalah {b}")
print(f"nilai a adalah {a}")

print("mencari jumlah 8 suku yang pertama")
print("dari rumus Sn = (n/2)*(2*a + (n-1)*b)")
n = 8
S8 = (n/2)*(2*a + (n-1)*b)
print(f"jadi, jumlah 8 suku yang pertama adalah {S8}")