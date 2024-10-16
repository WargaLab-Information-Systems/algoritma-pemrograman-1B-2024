#MEMINTA INPUT DARI PENGGUNA
nama = input("masukkan nama:")
nim = input("masukkan nim:")
nilai_uts =int(input("masukkan nilai UTS"))
nilai_uas =int(input("masukkan nilai UAS"))

#MENGHITUNG NILAI RATA-RATA
nilai_rata_rata = (nilai_uts+nilai_uas)/ 2

print("Nama lengkap :", nama)
print("NIM:", nim)
print("Nilai rata-rata kamu adalah", nilai_rata_rata)

if nilai_rata_rata >=81 and nilai_rata_rata <=100 :
    print("Anda mendaptkan nilai A")
elif nilai_rata_rata >= 71 and nilai_rata_rata <=81 :
    print("anda mendapatkan nilai B")
elif nilai_rata_rata >= 61 and nilai_rata_rata <=70:
    print("anda mendapatkan nilai C")
elif nilai_rata_rata >=41 and nilai_rata_rata <=60:
    print("anda mendapatkan nilai D")
else:
    print("Anda mendaptkan nilai E")