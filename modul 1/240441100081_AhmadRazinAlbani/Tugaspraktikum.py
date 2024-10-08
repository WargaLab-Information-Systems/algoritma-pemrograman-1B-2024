#TugasPraktikum 
#NO1
#MENGHITUNG VOLUME CELENGAN BALOK DAN TABUNG
# data celengan balok
panjang_celbalok = 20 #cm
lebar_celbalok = 13 #cm
tinggi_celbalok = 7 #cm
# menghitung volume balok 
volume_balok = panjang_celbalok * lebar_celbalok * tinggi_celbalok #volumebalok = pxlxt
print(f"Volume celengan balok yang dimiliki Andi : {volume_balok} cm^3")

# data celengan tabung 
diameter_tabung = 14 #cm
luas_selimut = 440 #cm^2

# langkah-langkah menghitung volume tabung
# menghitung jari-jari
jarijari = diameter_tabung / 2
# menghitung tinggi tabung 
tinggi_tabung = luas_selimut / (2 * 3.14 * jarijari)
# menghitung volume celengan tabung
volume_tabung = 3.14 * jarijari ** 2 * tinggi_tabung #volumetabung = pi x r^2 x t
print(f"Volume celengan tabung yang dimiliki Andi : {volume_tabung} cm^3")
