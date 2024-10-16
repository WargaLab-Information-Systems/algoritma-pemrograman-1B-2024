#suku ke 5 = 11 suku ke 8 dan 12 = 52
# Meminta input dari pengguna
U5 = float(input("Masukkan nilai suku ke-5 (U5): "))
U8_plus_U12 = float(input("Masukkan jumlah nilai suku ke-8 dan suku ke-12 (U8 + U12): "))

# Menghitung nilai b
b = (U8_plus_U12 - 2 * U5) / 10

# Menghitung nilai a
a = U5 - 4 * b

# Menghitung jumlah 8 suku pertama (S8)
n = 8
S8 = n / 2 * (2 * a + (n - 1) * b)
# Menampilkan hasil
print(f"\nNilai suku pertama (a): {a}")
print(f"Nilai beda (b): {b}")
print(f"Jumlah 8 suku pertama (S8): {S8}")
