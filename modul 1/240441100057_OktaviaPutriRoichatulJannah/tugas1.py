print("====no 1====")

print("===Volume Balok===")

panjang = 20
lebar = 13
tinggi = 7
print(f"Diketahui panjang balok adalah : {panjang} cm")
print(f"Diketahui lebar balok adalah : {lebar} cm")
print(f"Diketahui tinggi balok adalah : {tinggi} cm")

volume_b = panjang * lebar * tinggi
print(f"Volume balok tersebut adalah : {volume_b}")

print("===Volume Tabung===")

phi = 22/7
jarijari = 7
luas_selimut = 440

print(f"Diketahui phi adalah : {phi} ")
print(f"Diketahui jari-jari tabung adalah : {jarijari} cm")
print(f"Diketahui luas selimut tabung tersebut adalalah : {luas_selimut} cm")

tinggi_tabung = luas_selimut / (2 * phi * jarijari)
print(f"Tinggi tabung tersebut adalah : {tinggi_tabung}")

volume_t = 22/7* jarijari**2*tinggi_tabung
print(f"Jadi volume tabung tersebut adalah : {volume_t}") 
