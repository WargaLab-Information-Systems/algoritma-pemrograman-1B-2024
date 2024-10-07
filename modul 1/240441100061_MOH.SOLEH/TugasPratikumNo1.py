# Menghitung volume dari kedua  celengan milik Andi
# NO 1

# Data celengan balok
panjang_balok = 20 #cm
lebar_balok = 13 #cm
tinggi_balok = 7 #cm

# Menghitung volume baloknya
volume_balok = panjang_balok * lebar_balok * tinggi_balok #Vbalok x p x l x t
print("jadi hasil volume celengan baloknya adalah")
print("Volume celengan balok:", volume_balok, "cm³")

print("selanjutnya")
# Data celengan tabung
diameter = 14 #cm
r = diameter / 2 # jari-jari
print(f"jari-jari diameter tabung : {r} ")
luas_selimut = 440 #cm³

# Menghitung tinggi tabung dari luas selimut
tinggi_tabung = luas_selimut / (2 * 3.14 * r)
print(f"volume celengan tabungnya : {tinggi_tabung} ")

# Menghitung volume tabung
volume_tabung = 3.14 * (r ** 2) * tinggi_tabung #Vtabung = pi x r² x t
print("jadi hasil volume celengan tabungnya adalah")
print("Volume celengan tabung:", volume_tabung, "cm³")





