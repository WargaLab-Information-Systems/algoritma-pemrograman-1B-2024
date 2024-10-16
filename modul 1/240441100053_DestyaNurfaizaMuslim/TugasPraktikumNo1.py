#Program menghitung volume dari kedua celengan milik Andi

#Balok
panjang = 20
lebar = 13
tinggi = 7
volume = panjang*lebar*tinggi #rumus 
print("Jadi, volume balok adalah : ", volume,"cm^3")

#Tabung
diameter = 14
luas_selimut = 440
jari_jari = 1/2*diameter
tinggi = luas_selimut/(2*22/7*jari_jari)
volume = int(22/7*jari_jari*jari_jari*tinggi)
print("Jadi, volume tabung adalah : ", volume, "cm^3")