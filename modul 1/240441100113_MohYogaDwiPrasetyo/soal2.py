a5 = 11 
s8_n_s12 = 52

# a5 = a + 4d  =suku ke-5
# s8 + s12 = (a + 7d) + (a + 11d) 
#          = 2a + 18d = 52
# 2a = 52 - 18d
# a = 52 - 18d / 2
# a = 26 - 9d
    
# dr persamaan pertama:
# 26 - 9d + 4d = 11
# 26 - 5d = 11
# -5d = 11 - 26
# -5d = -15
# d = 3
    
d = 3 # beda
a = 26 - 9 * d  # hitung suku pertama

# hitung jumlah 8 suku pertama
s8 = 8 * (2*a + (8 - 1)*d) / 2

print(f"Jumlah 8 suku pertama dari deret aritmatika: {s8}")