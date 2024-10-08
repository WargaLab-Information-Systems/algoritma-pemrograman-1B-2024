# celengan bentuk balok

#input ukuran balok
panjang = 20 #cm
lebar = 13 #cm
tinggi = 7 #cm

# rumus volume balok
volume_balok = panjang*lebar*tinggi

#output proses
print("volume baloknya = ", volume_balok)

# input ukuran Tabung
phi = 3.14 
diameter = 14 #cm
luas_selimut = 440 #cm 

# hitung jari-jari
r = diameter / 2

# hitung tinggi menggunakan luas selimut
h = luas_selimut / (2*phi*r)

# hitung volume celengan tabung
volume_tabung = phi*r*r*h

#output 
print("tinggi tabung = ", h)
print("volume_tabung :  ", volume_tabung) 