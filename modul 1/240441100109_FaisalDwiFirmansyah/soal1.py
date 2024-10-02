# MENENTUKAN VOLUME DARI MASING-MASING CELENGAN ANDI

# MENGHITUNG VOLUME BALOK
# Diketahui:
panjang = 20
lebar = 13
tinggi = 7
volume_balok = panjang*lebar*tinggi #rumus 
print("Jadi, volume celengan balok Andi adalah: ", volume_balok,"cm^3")

# MENGHITUNG VOLUME TABUNG
diameter = 14
luas_selimut = 440
phi = 22/7
a = 2

# MENGHITUNG JARI-JARI TABUNG
r = diameter/2
# MENGHITUNG TINGGI TABUNG
t = luas_selimut / (a*phi*r)
# MENGHITUNG VOLUME TABUNG
volume_tabung = int(phi*r*r*t)
print("Jadi, volume celengan tabung Andi adalah: ", volume_tabung, "cm^3")
