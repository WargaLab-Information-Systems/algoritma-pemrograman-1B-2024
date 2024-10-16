# SOAL PERTAMA MENGHITUNG VOLUME CELENGAN BERBENTUK BALOK DAN TABUNG
# VOLUME TABUNG
# DIKETAHUI:

panjang = int(input("MASUKKAN NILAI PANJANG BALOK: ")) # 20 cm
lebar = int(input("MASUKKAN NILAI LEBAR BALOK: ")) # 13 cm
tinggi = int(input("MASUKKAN NILAI TINGGI BALOK: ")) # 7 cm 

volume_balok = panjang*lebar*tinggi
print("Jadi nilai dari volume balok adalah: ",volume_balok ,"cm")

# VOLUME TABUNG
# DIKETAHUI:

diameter = int(input("\nMASUKKAN NILAI DIAMETER TABUNG: ")) # 14 cm
luas_selimut = int(input("MASUKKAN NILAI LUAS SELIMUT TABUNG: ")) # 440 cm
phi = 22/7
a = 2
hasil_jari_jari = diameter/2
print("hasil dari jari jari tabung adalah: ",hasil_jari_jari)

tinggi_tabung = luas_selimut / (a*phi*hasil_jari_jari)
print("Hasil nilai dari tinggi tabung adalah: ",tinggi_tabung)
# VOLUME TABUNG

volume_tabung = phi* hasil_jari_jari**a *tinggi_tabung
print("Jadi hasil dari volume tabung ",volume_tabung ,"cm")