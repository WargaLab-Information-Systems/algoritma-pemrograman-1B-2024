# Suku ke-5 = 11 suku ke-8 dan suku ke-12 = 52
# Masukan input
suku_ke_5 = float(input("Masukkan nilai suku ke-5: "))
suku_ke_8_12 = float(input("Masukkan jumlah suku ke-8 dan suku ke-12: "))

# Menghitung d dan a
d = (suku_ke_8_12 - 2 * suku_ke_5) / 10
#d = 52 - 22 = 30 / 10 = 3

a = suku_ke_5 - 4 * d
#a = 11 - 4d = 11 - 12 = -1

#beda = d 
#suku_pertama = a

# Menghitung jumlah 8 suku pertama
# Diket:
n = 8
S_n = n / 2 * (2 * a + (n - 1) * d)

# Output hasil
print(f"\nsuku pertama (a) = {a:.2f}")
print(f"beda (d) = {d:.2f}")
print(f"Jumlah dari 8 suku pertama dari deret aritmatika adalah: {S_n}")