# menghitung balo 1
panjang_balok = 20
lebar_balok = 13
tinggi_balok = 7 
volume_balok = (panjang_balok * lebar_balok * tinggi_balok)
print("jumlah volume_balok",volume_balok)

# volume tabung 1
diameter_tabung = 14 
luas_selimut = 440
jari_jari_tabung = diameter_tabung / 2
tinggi_tabung = luas_selimut / (2 * 3.14 * jari_jari_tabung)

volume_tabung = 3.14 * jari_jari_tabung**2 * tinggi_tabung
print(f"hasil,{volume_tabung}, cm³")

# 3
x = 35
z = 15.219
k = x * z 
print("Rp",k)

# 4
n = 7 # total orang
faktorial_n = 7 * 6 * 5 * 4 * 3 * 2 * 1
d = 4 # orang yang dipilih
faktorial_d = 4 * 3 * 2 * 1
c = 3
faktorial_c = 3 * 2 * 1

kombinasi = faktorial_n / faktorial_d * faktorial_c

print(kombinasi)


#2
suku_5 = 11
suku_8_dan_ke_12 = 52
# mencari persamaan 1 (a)
# a + 4d = u5
# u8 + u12 = (a + 7d) + (a + 11d) = 2a + 18d = 52 = a = 26 - 9d 

# menghitung beda (d)
# a + 4d = u5
# (26 - 9d) + 4d = 11
# 26 - 5d = 11
# 5 = 15d
d = 3
# menghitung suku pertama (a)
a = 26 - 9 * d





n = 8 #suku 8
jumlah_8_suku = (n / 2 ) * (2 * a + (n - 1) * d)

print(f"jumlah nilai 8 dari suku pertama: {jumlah_8_suku}")