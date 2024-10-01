# balok
panjang = 20  #cm
lebar = 13   #cm
tinggi = 7   #cm

# Menghitung volume balok
v = panjang * lebar * tinggi
print(f"Volume balok adalah: {v}")

# tabung
import math
# import math berfungsi untuk menggunakan operasi matematika
diameter = 14  #cm
luas_selimut = 440  #cm

# Menghitung jari-jari tabung
r = diameter / 2 

#Menghitung tinggi tabung
t = luas_selimut / (2 * math.pi * r)
#math.pi berfungsi untuk melakukan fungsi pi(keliling lingkaran)
# Menghitung volume tabung
v= math.pi * r**2 * t
print(f"Volume tabung adalah: {v:.2f}")
