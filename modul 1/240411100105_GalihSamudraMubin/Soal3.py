# Program Menghitung Nilai Tukar Mata Uang
# Kurs IDR / 1USD Tanggal 25 September 2024 : 15180
# Declare Variabel
uang_usd = 35
kurs_usd_ke_idr = int (input("Masukkan Kurs USD Ke IDR Hari Ini:"))

# Rumus Menghitung Nilai Tukar
jumlah_idr = uang_usd * kurs_usd_ke_idr

# Hasil Akhir Tugas Praktikum Soal 3
print ("Nama Praktikan : Galih Samudra Mubin")
print ("NIM Praktikan  : 240441100105")

print ("Soal 3")
print ("Suraji mempunyai uang kertas bernilai US$35, ia ingin menukarkannya ke mata uang dari negara asalnya yaitu negara Indonesia. Bantulah Suraji untuk menghitung nominal uang yang didapatkannya dengan mata uang negara asalnya tersebut (Gunakan kurs sesuai dengan tanggal praktikum)!")
print ("Jawaban Program Yang Dibutuhkan")
print ("# Program Penghitung Nilai Tukar Mata Uang")
print ("Diketahui :")
print ("=> Mata Uang Yang Dituju adalah IDR")
print ("=> Nilai Tukar/ Kurs IDR Saat Ini Adalah",(kurs_usd_ke_idr))
print ("=> Jumlah Uang Yang Ingin Ditukarkan Adalah US$",(uang_usd))
print ("Ditanya Nominal Uang Yang Diterima Suraji Dari Penukaran Uang USD Ke IDR???")
print (f"Hasil Nominal Uang Yang Diterima Suraji adalah : IDR {jumlah_idr}")