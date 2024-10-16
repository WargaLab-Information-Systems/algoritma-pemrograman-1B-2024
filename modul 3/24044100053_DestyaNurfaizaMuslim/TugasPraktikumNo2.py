angka = int(input("masukkan angka : "))
balik_angka = 0

while angka > 0:
    x = angka % 10
    balik_angka = (balik_angka * 10) + x
    angka = angka // 10

print (("saat angka dibalik akan menjadi "),balik_angka)