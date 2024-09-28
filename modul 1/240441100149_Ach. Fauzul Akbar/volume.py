# volume tabung 1
import math
diameter_tabung = 14 
luas_selimut = 440
jari_jari_tabung = diameter_tabung / 2
tinggi_tabung = luas_selimut / (2 * math.pi * jari_jari_tabung)
volume_tabung = math.pi * jari_jari_tabung**2 * tinggi_tabung
print(f"hasil,{volume_tabung}, cm³")
