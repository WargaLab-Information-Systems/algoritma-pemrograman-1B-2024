print("PROGRAM MENGHITUNG VOLUME TABUNG")

diameter= 14
luas_selimut= 440
pi= 22/7
#MENGHITUNG JARI-JARI DAN TINGGI VOLUME TABUNG
r = diameter / 2
t = luas_selimut / (2 * pi * r)
#hitung volume tabung
volume = pi * (r ** 2) * t

print(f"hasil dari menghitung volume celengan tabung andi adalah: ", volume, "cm**3")
print()

#HITUNG VOLUME BALOK
print("PROGRAM MENGHITUNG VOLUME BALOK")

panjang = 20
lebar = 13
tinggi = 7
#mencari volume
volume = panjang * lebar * tinggi

print(f"hasil dari menghitung volume celengan balok andi adalah: ", volume, "cm**3")