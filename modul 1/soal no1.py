# input ukuran celengan balok
panjang = 20 #cm
lebar = 13 #cm
tinggi = 7 #cm
volume_balok = panjang*lebar*tinggi
print(f"volume celengan balok : {volume_balok} cm³.")

# input ukuran celengan volume_tabung
diameter = 14 #cm
luas_selimut = 440 #cm
jari_jari = 7
phi = 22/7

# cara untuk menghitung volume celengan tabung
volume_tabung = (diameter, luas_selimut)
jari_jari = diameter / 2
tinggi = luas_selimut / (2*phi*jari_jari)
volume_tabung = phi*jari_jari**2*tinggi
print("tinggi tabung adalah:", tinggi)
print(f"volume celengan tabung : {volume_tabung:}cm³.")