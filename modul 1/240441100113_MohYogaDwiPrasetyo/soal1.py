# VOLUME BALOK
panjang = 20
lebar = 13
tinggi = 7 
volume_balok = panjang * lebar * tinggi

# VOLUME TABUNG
diameter = 14
luas_selimut = 440
pi = 22/7 #bisa 22/7 atau 3.14
jari_jari = diameter / 2 # 7
tinggi = luas_selimut / (2 * pi * jari_jari) # 10
volume_tabung = pi * jari_jari**2 * tinggi

print(f"Volume balok: {volume_balok} cm³")
print(f"Volume tabung: {volume_tabung:.2f} cm³") # 2f untuk menampilkan 2 angka dibelakang koma desimal
