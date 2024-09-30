# jawaban soal no 1

# variabel balok 
panjang = 20 # tipedata integer (cm)
lebar = 13 # tipedata integer (cm)
tinggi = 7 # tipedata integer (cm)
# variabel tabung 
diameter = 14 # tipedata integer (cm)
luas_selimut = 440 # tipedata integer  (cm2)
pi = 3.14 # tipedata float 

# volume balok
volume_balok = panjang * lebar * tinggi
# volume tabung
jarijari_tabung = diameter / 2
tinggi_tabung = luas_selimut / (2 * pi * jarijari_tabung)
volume_tabung = pi * jarijari_tabung**2 * tinggi_tabung

print(f"volume balok Andi adalah {volume_balok} cm^3")
print(f"volume tabung adalah {volume_tabung} cm^3")

