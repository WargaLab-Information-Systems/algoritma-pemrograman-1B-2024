nama = input("Masukkan nama: ")
nim = int(input("Masukkan nim: "))
nilai_uts = int(input("Masukkan nilai uts: "))
nilai_uas = int(input("Masukkan nilai uas: "))
nilai_rata_rata = (nilai_uts + nilai_uas) / 2

if nilai_rata_rata >= 81 and nilai_rata_rata <= 100:
    print("Anda mendapatkan nilai A")
elif nilai_rata_rata >= 71 and nilai_rata_rata <= 80:
    print("Anda mendapatkan nilai B")
elif nilai_rata_rata >= 61 and nilai_rata_rata <= 70:
    print("Anda mendapatkan nilai C")
elif nilai_rata_rata >= 41 and nilai_rata_rata <= 60:
    print("Anda mendapatkan nilai D")
elif nilai_rata_rata >= 0 and nilai_rata_rata <= 40:
    print("Anda mendapatkan nilai E")
else:
    print("Data Not Found")

print("Nama anda: " + nama)
print("NIM anda: ", nim)
print("Nilai rata-rata anda: ", nilai_rata_rata)