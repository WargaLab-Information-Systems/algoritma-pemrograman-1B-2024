#panjang 20 lebar 13 tinggi 7
#diameter 14 selimut 440
pi = 3.14
# Fungsi untuk menghitung volume balok
def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

# Fungsi untuk menghitung volume tabung berdasarkan diameter dan luas selimut
def volume_tabung(diameter, luas_selimut):
    # Menghitung jari-jari
    jari_jari = diameter / 2
    
    # Menghitung tinggi tabung dari luas selimut
    tinggi = luas_selimut / (2 * pi * jari_jari)
    
    # Menghitung volume tabung
    volume = pi * jari_jari ** 2 * tinggi
    return volume 

panjang_balok = float(input("Masukkan panjang balok (cm): "))
lebar_balok = float(input("Masukkan lebar balok (cm): "))
tinggi_balok = float(input("Masukkan tinggi balok (cm): "))

diameter_tabung = float(input("Masukkan diameter tabung (cm): "))
luas_selimut_tabung = float(input("Masukkan luas selimut tabung (cm²): "))

# Menghitung volume balok dan tabung
volume_b = volume_balok(panjang_balok, lebar_balok, tinggi_balok)
volume_t = volume_tabung(diameter_tabung, luas_selimut_tabung)

# Menampilkan hasil
print(f"\nVolume celengan balok: {volume_b:} cm³")
print(f"Volume celengan tabung: {volume_t:} cm³")
