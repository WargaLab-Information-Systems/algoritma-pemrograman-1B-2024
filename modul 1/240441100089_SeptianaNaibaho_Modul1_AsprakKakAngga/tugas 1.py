#Celengan Balok Andi
panjang_balok= 20
lebar_balok= 13
tinggi_balok= 7
panjang = int(input("masukkan panjang :"))
lebar= int(input("masukkan lebar :"))
tinggi= int(input("masukkan tinggi :"))
volume= panjang*lebar*tinggi
print(f"volume celengan balok Andi adalah {volume} cm3")

#Celengan Tabung Andi
diameter = 14
luasselimut = 440
phi = 22/7
jari_jari = diameter/2
diameter = int(input("masukkan diameter :"))
luasselimut = int(input("masukkan luas selimut :"))
tinggi = luasselimut/(2*phi*jari_jari)
volume = phi*jari_jari**2*tinggi
print(f"volume celengan tabung Andi adalah {volume} cm3")







