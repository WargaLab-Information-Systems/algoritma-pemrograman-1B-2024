# # panjang balok : 20
# lebar balok : 13
# tinggi balok : 7

# # diameter tabung : 14
# luas selimut : 440
# jari-jari : 7.0
# tinggi tabung : 4835.6


# balok
p_balok = int(input("masukkan nilai"))
l_balok = 13
t_balok = 7

# tabung
d_tabung  = 14
luas_selimut = 440
r_tabung = d_tabung / 2
t_tabung = luas_selimut / (2 *3.14 * r_tabung)

# volume balok
v_balok = p_balok * l_balok * t_balok

# volume tabung
v_tabung = 3.14 * r_tabung ** 22 * t_tabung

print ("panjang balok : ", p_balok)
print ("lebar balok : ", l_balok)
print ("tinggi balok : ", t_balok)
print ("\ndiameter tabung : ", d_tabung)
print ("luas selimut : ", luas_selimut)
print ("jari-jari :", r_tabung)
print ("tinggi tabung :", t_tabung)
print ("\nvolume balok : ", v_balok)
print ("volume tabung : ", v_tabung)
