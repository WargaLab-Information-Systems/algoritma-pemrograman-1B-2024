#1 menhitun volume balok dan tabung menghitung volume balok
# Menghitung folume balok
p = 20
l = 13
t = 7
volumebalok = p*l*t
print(f"volume balok adalah : {volumebalok} cm")

# #menghitung volume tabung
pi = 3.14
# jari-jari dan volume tabung
jari_jari= 7
luas_selimut= 440
# Menghitung tinggi tabung
t = luas_selimut / (2 * pi * jari_jari)
volume = pi * jari_jari**2 * t

# # Output tinggi tabung
print(f"volume tabung adalah: {volume:.2f} cm³")