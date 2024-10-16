# Program Menghitung Deret Aritmatika
# Declare Variabel
suku_5 = 11
jumlah_suku_8_dan_12 = 52
    # 1. a + 4d = 11
    # 2. 2a + 18d = 52

    # Persamaan Pertama
    # a = 11 - 4d
    # Subtitusi Persamaan Kedua
    # 2 (11 - 4d) + 18d = 52
    # 22 - 8d + 18d = 52
    # 10d = 30
    # d = 3
d = 3
a = 11 - 4 * d

# Rumus Mencari Jumlah 8 Suku Pertama
jumlah_8_suku_pertama = 8 / 2  * (2 * a + (8 - 1) * d)

# Hasil Akhir Tugas Praktikum Soal 2
print ("Nama Praktikan : Galih Samudra Mubin")
print ("NIM Praktikan  : 240441100105")

print ("Soal 2")
print ("Darmaji ingin mengetahui jumlah nilai dari 8 suku pertama dari sebuah deret aritmatika dengan keadaan suku ke-5 dari deret tersebut bernilai 11 dan jumlah nilai suku ke-8 dan suku ke-12 nya adalah 52. Buatlah program untuk membantu Darmaji untuk menyelesaikan masalah tersebut!")
print ("Jawaban Program Yang Dibutuhkan")
print ("# Program Penghitung Deret Aritmatika")
print ("Diketahui :")
print ("=> Suku Ke 5 Adalah",(suku_5))
print ("=> Jumlah Suku 8 Dan 12 Adalah",(jumlah_suku_8_dan_12))
print ("=> Nilai d Adalah",(d))
print ("=> Nilai a Adalah",(a))
print ("Ditanya Volume Jumlah 8 Suku Pertama???")
print ("Jumlah 8 Suku Pertama = 8 / 2  x (2 x a + (8 - 1) x d)")
print (f"Hasil Jumlah 8 Suku Pertama adalah : {jumlah_8_suku_pertama}")