nama = input("Masukkan nama: ")
nim = int(input("Masukkan nim: "))
nilai_uts = int(input("Masukkan nilai uts: "))
nilai_uas = int(input("Masukkan nilai uas: "))
nilai_rata_rata = (nilai_uts + nilai_uas) / 2

if nilai_rata_rata >= 81 <= 100:
    print("Anda mendapatkan nilai A")
elif nilai_rata_rata >= 71 <= 80:
    print("Anda mendapatkan nilai B")
elif nilai_rata_rata >= 61 <= 70:
    print("Anda mendapatkan nilai C")
elif nilai_rata_rata >= 41 <= 60:
    print("Anda mendapatkan nilai D")
else:
    print("Anda mendapatkan nilai E")

print("Nama anda: " + nama)
print("NIM anda: ", nim)
print("Nilai rata-rata anda: ", nilai_rata_rata)
