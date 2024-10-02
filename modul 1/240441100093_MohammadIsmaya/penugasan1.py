#NOMOR 1

# MENGHITUNG VOLUME CELENGAN BALOK
panjang = 20
lebar = 13
tinggi = 7
volume_balok = panjang * lebar * tinggi

# Menghitung volume celengan tabung
diameter = 14
luas_selimut = 440
phi = 22/7
jari_jari = diameter / 2
tinggi_tabung = luas_selimut / (2 * 22/7 * jari_jari)
volume_tabung = 22/7 * jari_jari**2 * tinggi_tabung

# Menampilkan hasil
print(f"Volume celengan balok: {volume_balok} cm³")
print(f"Volume celengan tabung: {volume_tabung:.2f} cm³")