
nama = input("Masukan Nama:")
nim = int(input("Masukan Nim:"))
nilai_uts = int(input("Masukan Nilai UTS:"))
nilai_uas = int(input("Masukan Nilai UAS:"))

#Menghitung Rumus
nilai_rata_rata = (nilai_uts + nilai_uas)/2

if nilai_rata_rata >= 81 <= 100:
    print("Anda Mendapatkan Nilai A")
elif nilai_rata_rata >= 71 <= 80:
    print("Anda Mendapatkan Nilai B")
elif nilai_rata_rata >= 61 <= 70:
    print("Anda Mendapatkan Nilai C")
elif nilai_rata_rata >= 41 <= 60:
    print("Anda Mendaptkan Nilai D")
else:
    print("Anda Mendapatkan Nilai E")
    
# Menampilkan hasil
print("Masukan Nama", nama)  
print("Nim anda :", nim)
print("Nilai rata rata nilai anda", nilai_rata_rata)