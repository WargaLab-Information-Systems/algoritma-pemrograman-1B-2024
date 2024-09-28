# input data
panjangBalok = 20 
lebarBalok = 13
tinggiBalok = 7
diameterTabung = 14
jarijariTabung = int(diameterTabung / 2)
luasSelimut = 440 
 
# mencari volume celengan berbentuk balok
volumeBalok = int(panjangBalok * lebarBalok * tinggiBalok)

# mencari tinggi dari celengan berbentuk tabung
tinggiTabung = int(luasSelimut / (2 * 22/7 * jarijariTabung))
# mencari volume celengan berbentuk tabung
volumeTabung = int(22/7 * (jarijariTabung ** 2) * tinggiTabung)

# Hasil
print(f" Volume celengan berbentuk balok adalah {volumeBalok} cm³ dan volume celengan berbentuk tabung adalah {volumeTabung} cm³")