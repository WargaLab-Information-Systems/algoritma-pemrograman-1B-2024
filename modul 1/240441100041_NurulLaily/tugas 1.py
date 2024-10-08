#  Data untuk celengan berbentuk balok
panjang_balok = 20 #cm
lebar_balok = 13 #cm
tinggi_balok = 7 #cm

# Menghitung volume baloknya
volume_balok = panjang_balok * lebar_balok * tinggi_balok
# p x l x t
print("jadi hasil volume celengan baloknya adalah")
print("volume celengan balok:", volume_balok, "cm3")

print("selanjutnya")
# Data celengan tabung
diameter = 14 #cm
r = diameter / 2 # jari-jari
print(f"jari-jari diameter tabung : {r} ")
luas_selimut = 440 

# Menghitung tinggi tabung dari luas selimut
tinggi_tabung = luas_selimut / (2 * 3.14 * r)
print(tinggi_tabung)
# Menghitung volume tabung
volume_tabung = 3.14 * r**2 * tinggi_tabung


# Menampilkan hasil
print (f"volume celengan berbentuk balok : {volume_balok} cm³ ")
print (f"volume celengan berbentuk tabung : {volume_tabung: .2f} cm³ ")