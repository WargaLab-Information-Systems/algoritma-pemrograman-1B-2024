# diketahui balok:
pi = 3.14
panjang = 20  
lebar = 13    
tinggi_balok = 7  
volume_balok = panjang * lebar * tinggi_balok

# diketahui tabung:
diameter = 14   # cm
radius = diameter / 2
luas_selimut = 440  # cm^2

# Menghitung tinggi tabung dari luas selimut
tinggi_tabung = luas_selimut / (2 * pi * radius)
# Menghitung volume tabung
volume_tabung = pi * radius ** 2 * tinggi_tabung

# Menampilkan hasil
print("Volume balok: ",volume_balok," cm³")
print("Volume tabung: ",volume_tabung," cm³")
