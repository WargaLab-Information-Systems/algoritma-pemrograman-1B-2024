# Menghitung volume balok
print("Hitung Volume balok")
panjang = int(input("Masukkan Panjang: "))  # cm
lebar = int(input("Masukkan Lebar: ")) # cm
tinggi = int(input("Masukkan Tinggi: "))    # cm
volume_balok = panjang * lebar * tinggi

# Menghitung volume tabung
# print()
print("Hitung volume tabung")
phi = 22/7
diameter = int(input("Masukkan Diameter: "))  # cm
jari_jari = diameter / 2 #cm
luas_selimut = int(input("Masukkan Selimut: "))  # cm²
tinggi_tabung = luas_selimut / (2 * phi * jari_jari)
volume_tabung = phi * jari_jari**2 * tinggi_tabung

# Menampilkan hasil
print()
print("Volume balok:", volume_balok, "cm³")
print("Volume tabung:", volume_tabung, "cm³")