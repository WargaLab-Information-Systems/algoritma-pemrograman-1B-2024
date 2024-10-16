# Jawaban Soal No 2

# Variabel
suku_5 = 11 # tipedata integer 
suku_8_dan_12 = 52 # tipedata integer
n = 8 # tipedata integer

# menghitung persamaan pertama
# 11 = a + 4b 
# a = 11 + 4b

# menghitung persamaan kedua 
# u8 = a + 7b
# u12 = a + 11b
# 52 = 2a + 18b

# substitusi persamaan pertama ke persemaan kedua
# 52 = 2 (11 + 4b) + 18b

# menghitung nilai b
b = (suku_8_dan_12 / 2 - suku_5) / (18 / 2 - 4) 

# menghitung a 
a = suku_5 - (4 * b)

# menghitung jumlah 8 suku pertama 
hasil_8_suku = n / 2 * (2 * a + (n - 1) * b)

print("nilai dari b adalah ", b)
print("nilai dari a adalah ", a)
print("jadi jumlah nilai 8 suku pertama adalah ", hasil_8_suku)