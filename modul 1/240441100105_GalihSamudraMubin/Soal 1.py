# Program Menghitung Volume Balok Dan Tabung
# Balok
p_balok = 20
l_balok = 13
t_balok = 7

# Tabung
d_tabung = 14
luas_selimut = 440
r_tabung = d_tabung / 2
t_tabung = luas_selimut / (2 * 3.14 * r_tabung)

# Volume Balok
v_balok = p_balok * l_balok * t_balok

# Volume Tabung
v_tabung = 3.14 * r_tabung ** 2 * t_tabung

# Hasil Akhir Tugas Praktikum Soal 1
print ("Nama Praktikan : Galih Samudra Mubin")
print ("NIM Praktikan  : 240441100105")

print ("Soal 1")
print ("Andi mempunyai celengan berbentuk balok dan tabung. Celengan yang berbentuk balok memiliki ukuran panjang 20cm dan lebar 13cm, Sedangkan celengan yang berbentuk tabung memiliki diameter 14cm dan luas selimutnya 440cm². Bantulah Andi dengan membuat program untuk menghitung volume dari kedua celengan miliknya tersebut!")
print ("Jawaban Program Yang Dibutuhkan")
print ("# Program Penghitung Volume Balok")
print ("Diketahui :")
print ("=> Panjang Balok adalah",(p_balok),"CM")
print ("=> Lebar Balok adalah",(l_balok),"CM")
print ("=> Tinggi Balok adalah",(t_balok),"CM")
print ("Ditanya Volume Balok???")
print ("Volume Balok = Panjang x Lebar x Tinggi")
print ("Hasil Volume Balok adalah",(v_balok),"CM^3")
print ("# Program Penghitung Volume Tabung")
print ("Diketahui :")
print ("=> Jari Jari Tabung adalah",(r_tabung),"CM")
print ("=> Tinggi Tabung adalah",(t_tabung),"CM")
print ("Ditanya Volume Tabung???")
print ("Volume Tabung = Phi(3.14) x r^2 x Tinggi")
print ("Hasil Volume Tabung adalah",(v_tabung),"CM^3")