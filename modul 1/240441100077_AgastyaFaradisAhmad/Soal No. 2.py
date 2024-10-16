# Diketahui/Input
suku5 = 11
suku8_tambah_suku12 = 52
def suku_pertama_dan_beda(suku5, suku8_tambah_suku12):
#(rumus: an = a+(n-1)b)
# Temukan a dalam bentuk a = 11 - 4b (dari suku5 = a + 4b)
# Persamaan pertama:
# suku5 = a + 4b
# 11 = a + 4b
# a = 11 - 4b

# Lalu gunakan persamaan kedua untuk mencari b
# suku8 + suku12 = (a + 7b) + (a + 11b) = 52
#2a + 18b = suku8 + suku12 = 52
# Dari persamaan 1: a = suku5 - 4b
# Substitusi ke persamaan 2: 
# 2(suku5 - 4b) + 18b = suku8 + suku12
# 2 suku5 - 8b + 18b = suku8 + suku12
# 2 suku5 + 10b = suku8 + suku 12
# b = (suku8 + suku12 - 2 * suku5) / 10
    b = (suku8_tambah_suku12 - 2 * suku5) / 10  
    a = suku5 - 4 * b                    
    return a, b

# Menyelesaikan persamaan
a, b= suku_pertama_dan_beda(suku5, suku8_tambah_suku12)
# Menghitung jumlah nilai 8 suku pertama
n = 8
JumlahS8 = n / 2 * (2 * a + (n - 1) * b)

# Hasil jumlah/Output
print(f"Suku pertama (a) = {a}")
print(f"Beda (b) = {b}")
print(f"Jumlah 8 suku pertama (S_8) = {JumlahS8}")