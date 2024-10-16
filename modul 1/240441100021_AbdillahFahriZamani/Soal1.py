# Diket panjang balok 20cm, lebar balok 13cm, tinggi 7cm
# Diket diameter tabung 14cm, luas selimut tabung 440cm persegi

# Input untuk celengan balok
p = float(input("panjang celengan balok: "))
l = float(input("lebar celengan balok: "))
t = float(input("tinggi celengan balok: "))

# Menghitung volume balok
volume_balok = p * l * t

# Input untuk celengan tabung
diameter_tabung = float(input("diameter celengan tabung: "))
luas_selimut_tabung = float(input("luas selimut celengan tabung: "))

# Menghitung jari-jari dan tinggi tabung
jari_jari_tabung = diameter_tabung / 2
tinggi_tabung = luas_selimut_tabung / (2 * 3.14 * jari_jari_tabung)

# Menghitung volume tabung
volume_tabung = 3.14 * (jari_jari_tabung ** 2) * tinggi_tabung

# Output hasil
print(f"\nVolume celengan balok: {volume_balok} CM kubik")
print(f"Volume celengan tabung: {volume_tabung} CM kubik")
