# Penyeleksian Kondisi secara dinamis

nama = str(input("Masukkan Nama : "))
nim = int(input("Masukkan NIM : "))
nilai_uts = int(input("Masukkan Nilai UTS : "))
nilai_uas = int(input("Masukkan Nilai UAS : "))

nilai_ratarata = (nilai_uts + nilai_uas) / 2
print(f"Nilai rata rata anda {nilai_ratarata}")

if nilai_ratarata > 80 and nilai_ratarata <= 100:
    print("Anda Mendapatkan Nilai A")
elif nilai_ratarata > 70 and nilai_ratarata <=80:
    print("Anda Mendapatkan Nilai B")
elif nilai_ratarata > 60:
    print("Anda Mendapatkan Nilai C")
elif nilai_ratarata > 40:
    print("Anda Mendapatkan Nilai D")
elif nilai_ratarata > 0:
    print("Anda Mendapatkan Nilai E")
else:
    print("Nilai Anda Tidak Tidak Di Mengerti")