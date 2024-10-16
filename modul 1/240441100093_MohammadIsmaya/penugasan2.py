# NOMER2

# Jumlah nilai dari 8 suku pertama
u5 = 11
u8_plus_u12 = 52

# Mencari a dan b menggunakan rumus Un = a + (n-1)*b
# Persamaan 1 -> 11 = a +4b
# Persamaan 2 -> 52 = 2a + 18b -> 26 = a + 9b
# Persamaan 3 - persamaan 1 -> b=3

b = 3
a = u5 - (5-1)*b
print(b)
print (a)

# Menggunakan rumus Sn = (n/2)*(2a+(n-1)b)
n = 8
Sn = (n/2)*(2*a+(n-1)*b)
print("jadi, jumlah nilai dari 8 suku pertama adalah", Sn)