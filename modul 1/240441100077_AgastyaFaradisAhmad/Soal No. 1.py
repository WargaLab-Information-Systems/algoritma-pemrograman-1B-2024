# Diket data celengan balok
panjangCB = 20    #(dalam cm)
lebarCB = 13
tinggiCB = 7   
# Diket data celengan tabung
diameter = 14
luas_selimut = 440

volume_balok = panjangCB * lebarCB * tinggiCB #Volume celengan balok (20x13x7)
 
jari_jari_tabung = diameter / 2 #Mencari jari-jari dan tinggi tabung (14:2)
tinggi_tabung = luas_selimut / (2 * 3.14 * jari_jari_tabung) #Rumus mencari tinggi tabung (440:(2x3,14x7))
volume_tabung = 3.14 * jari_jari_tabung**2 * tinggi_tabung   #Volume celengan tabung (3,14x7²x10.004)

# Hasil perhitungan/Output
print("Volume celengan balok Andi:", volume_balok, "cm³")   #Luas volume celengan balok
print("Volume celengan tabung Andi:", volume_tabung, "cm³") #Luas volume celengan tabung