# Program Menghitung Kombinasi
# Menggunakan Rumus Kombinasi C(n,r) = n!/(r!*(n-r)!)
# Declare Variabel
n = 7 # Total Orang
r = 4 # Jumlah Orang Dalam Tim
faktorial_7= 7*6*5*4*3*2*1
faktorial_4 = 4*3*2*1
faktorial_3 = 3*2*1 # Nilai (n-r) / (7-4)

# Rumus Mebcari Jumlah Cara Untuk Memilih Tim
jumlah_cara = (faktorial_7) / (faktorial_4 * faktorial_3)

# Hasil Akhir Tugas Praktikum Soal 4
print ("Nama Praktikan : Galih Samudra Mubin")
print ("NIM Praktikan  : 240441100105")

print ("Soal 4")
print ("Darsono merupakan seorang mandor yang ingin menyusun tim dari beberapa orang, ia memiliki total 7 orang dan ingin memilih 4 orang untuk masuk kedalam timnya. Buatlah program yang dapat membantu Darsono menghitung berapa banyak cara untuk membentuk tim tersebut!")
print ("Jawaban Program Yang Dibutuhkan")
print ("# Program Penghitung Kombinasi")
print ("Diketahui :")
print ("=> Nilai n (Total Orang) Adalah",(n))
print ("=> Nilai r (Jumlah Orang Dalam Tim) Adalah",(r))
print ("Ditanya Ada Berapa Cara Yang Bisa Dilakukan Darsono Untuk Membentuk Tim???")
print (f"Jumlah Cara Yang Bisa Dilakukan Darsono Untuk Membentuk Tim adalah {jumlah_cara}")