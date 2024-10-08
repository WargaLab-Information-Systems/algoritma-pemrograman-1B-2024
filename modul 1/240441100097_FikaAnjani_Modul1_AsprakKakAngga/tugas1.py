panjang_balok = 20 
lebar_balok = 13    
tinggi_balok = 7   
volume_balok = panjang_balok * lebar_balok * tinggi_balok
diameter_tabung = 14  
radius_tabung = diameter_tabung / 2
luas_selimut_tabung = 440  

tinggi_tabung = luas_selimut_tabung / (2 * 22/7 * radius_tabung)

volume_tabung = 22/7 * radius_tabung**2 * tinggi_tabung

print(f"Volume celengan berbentuk balok: {volume_balok} cm³")
print(f"Volume celengan berbentuk tabung: {volume_tabung} cm³")