#volume celengan balok

panjang=20
lebar =13
tinggi=7
volume_balok= panjang*lebar*tinggi
print("berikut adalah volume celengan balok andi")
print("rumus volume balok adalah :","\npanjang x lebar x tinggi", "\n20 x 13 x 7 =")
print(volume_balok)

# #volume celengan tabung

diameter = 14
jarijari= diameter/2 #hasilnya adalah 7
pangkatjarijari= jarijari**2
phi= 22/7
luas_selimut = 440
print("rumus volume tabung adalah :","\nphi * r² * t")
print("mari kita cari tinggi nya terlebih dahulu dengan cara membagi luas selimutnya dengan phi * r² ")
tinggi = luas_selimut / (2 * 22/7 * jarijari)
print("hasilnya adalah", tinggi)
volume_tabung= phi * pangkatjarijari * tinggi 
print("setelah itu cari jari-jari terlebih dahulu","\n jari-jari= diameter dibagi 2", jarijari)
print("lalu setelah itu kita dapat langsung memasukkannya kedalam rumus volume tabung yakni :")
print("phi(22/7 atau 3,14) * 2 * r(jari-jari)")
print(volume_tabung)



# START

# # Volume celengan balok
# DECLARE panjang = 20
# DECLARE lebar = 13
# DECLARE tinggi = 7
# DECLARE luas_balok = panjang * lebar
# PRINT "Berikut adalah volume celengan balok Andi"
# PRINT "Rumus volume balok adalah:"
# PRINT "panjang x lebar x tinggi"
# PRINT "20 x 13 x 7 ="
# PRINT luas_balok

# # Volume celengan tabung
# DECLARE diameter = 14
# DECLARE jarijari = diameter / 2
# DECLARE pangkatjarijari = jarijari^2
# DECLARE phi = 22 / 7
# DECLARE luas_selimut = 440

# PRINT "Rumus volume tabung adalah:"
# PRINT "phi * r² * t"
# PRINT "Mari kita cari tinggi tabung terlebih dahulu"
# PRINT "Caranya dengan membagi luas selimut dengan phi * r²"

# # Cari tinggi tabung
# DECLARE tinggi = luas_selimut / (phi * jarijari^2)
# PRINT "Hasil tinggi tabung adalah" tinggi

# # Hitung volume tabung
# DECLARE volume_tabung = phi * pangkatjarijari * tinggi
# PRINT "Setelah itu kita dapat menghitung volume tabung:"
# PRINT "Phi (22/7 atau 3,14) * r² * tinggi"
# PRINT volume_tabung

# END
