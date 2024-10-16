# 2 menemukan jumlah nilai dari suku ke 8
sk_5 = 11    # Misalnya, suku ke-5 adalah 11
sk_8_12 = 52    # Misalnya, jumlah dari suku ke-8 hingga ke-12 adalah 52
# Menghitung beda (b)
b = (sk_8_12 - 2 * sk_5) / 10
# Menghitung suku pertama (a)
a = sk_5 - 4 * b
# Menghitung jumlah 8 suku pertama
n = 8
jumlah_8_suku_pertama = (n / 2) * (2 * a + (n - 1) * b)
# Output hasil
print(f"Suku pertama (a) = {a}")
print(f"Beda (b) = {b}")
print(f"Jumlah 8 suku pertama dari deret aritmatika tersebut adalah = {jumlah_8_suku_pertama}")