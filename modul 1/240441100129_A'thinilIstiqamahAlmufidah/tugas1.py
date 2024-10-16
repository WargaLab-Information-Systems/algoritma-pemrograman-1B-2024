# Tugas praktikum nomor 1
# Soal nomor 1
# Andi mempunyai celengan berbentuk balok dan tabung. celengan yang bebentuk balok memiliki ukuran panjang 20 cm, lebar 13 cm
# dan tinggi 7cm, Sedangkan celengan berbentuk tabung memiliki diameter 14 cm dan luas selimutnya 440cm^2. bantulah andi dengan membuat
# program untuk menghitung volumenya dari kedua celengan miliknya tersebut!

# diketahui data celengan balok  dan tabung :
# data celengan balok
print("soal nomor 1")
panjang = 20 #cm
lebar = 13 #cm
tinggi_balok = 7 #cm

# rumus volume balok
V_balok = panjang * lebar * tinggi_balok
# data celengan tabung
diameter = 14
r = diameter/2
l = 440 
# rumus volume tabung
phi = 22/7
t = l/2*phi*r #rumus tinggi tabung
v_tabung = phi*r*r*t


# hasil output
print(f"volume dari celengan balok : {V_balok} cm³")
print(f"volume dari celengan tabung : {v_tabung} cm³")
