# Menggunakan rumus faktorial
# Jumlah orang yang dipilih 7
faktorial7 = int(input("Masukkan faktorial 7: "))
faktorial_7 = faktorial7 * 6 * 5 * 4 * 3 * 2 * 1
print ("faktorial 7 =",faktorial_7)

# yang akan dipilih 4!
faktorial4 = int(input("Masukkan faktorial 4: "))
faktorial_4 = faktorial4 * 3 * 2 * 1
print ("Faktorial 4 =", faktorial_4)

jumlah_orang = 7
akan_dipilih =  4

yang_tidak_dipilih = jumlah_orang - akan_dipilih

faktorial_3 = yang_tidak_dipilih * 2 * 1
print("Faktorial 3 =",faktorial_3)

banyak_cara = faktorial_7 // (faktorial_4 * faktorial_3)