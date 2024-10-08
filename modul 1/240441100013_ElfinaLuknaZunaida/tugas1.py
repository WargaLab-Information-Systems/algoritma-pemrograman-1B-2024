# 1 
# diketahui balok
panjang_balok = 20 #cm
lebar_balok = 13 #cm
tinggi_balok = 7 #cm

volume_balok = panjang_balok * lebar_balok * tinggi_balok
print (f"volume celengan balok adalah {volume_balok} cm^3")

# diketahui tabung
luas_selimut_tabung = 440
diameter_tabung = 14
jari_jari_tabung = diameter_tabung / 2
phi = 22/7
tinggi_tabung = luas_selimut_tabung / (2*phi * jari_jari_tabung)
print(f"tinggi tabung adalah {tinggi_tabung}")
volume_tabung = phi * (jari_jari_tabung**2) * tinggi_tabung
print (f"volume celengan tabung adalah {volume_tabung} cm^3")

#3 uang suraji
uang_dollar_suraji = 35 #usd
kurs_indonesia = 15.102 #tiap satu dollar

uang_suraji_yang_telah_ditukar = uang_dollar_suraji * kurs_indonesia

print (f"Jumlah uang suraji yang telah ditukar adalah {uang_suraji_yang_telah_ditukar}")

#4. menghitung kemungkinan
import math
# diketahui
n = 7 # jumlah orang
r = 4 # orang yang akan dipilih

# 2 Diketahui
suku_ke_5 = 11
jumlah_suku_8_dan_12 = 52


# a + 4d = 11 (suku ke-5)
# (a + 7d) + (a + 11d) = 52 (jumlah suku ke-8 dan suku ke-12)

# Menghitung d
# 2a + 18d = 52
# a + 4d = 11 * 2 = 2a + 8d = 11
#(2a + 18d = 52) - (2a + 8d = 22)
d = 3
 # Menghitung a
a = suku_ke_5 - 4 * d 

# Menghitung jumlah 8 suku pertama
n = 8
S_n = (n / 2) * (2 * a + (n - 1) * d)

# Menampilkan hasil
print(f"Jumlah 8 suku pertama dari deret aritmatika adalah {S_n}")
