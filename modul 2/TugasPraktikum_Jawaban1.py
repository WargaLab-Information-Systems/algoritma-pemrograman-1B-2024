#  PENYELEKSI KONDISI DINAMIS

nama = (input("Masukan Nama "))
nim = int(input("Masukkan NIM "))
uts = int(input("Masukkan Nilai UTS : "))
uas = int(input("Masukkan Nilai UAS : "))

# menghitung rata-rata nilai
Rata_rata  = (uts + uas)/2

print("Masukan Nama ", nama)
print("NIM anda : ", nim)
print("Nilai rata rata nilai anda ", Rata_rata )

if Rata_rata <= 100 and Rata_rata >= 81:
    print("Anda Mendapatkan Nilai A")
elif Rata_rata <= 80 and Rata_rata >=71:
    print("Anda Mendapatkan Nilai B")
elif Rata_rata <= 70 and Rata_rata >=61:
    print("Anda Mendapatkan Nilai C")
elif Rata_rata <=60 and Rata_rata >= 41:
    print("Anda Mendapatkan Nilai D")
elif Rata_rata <= 40 and Rata_rata >=0:
    print("Anda Mendapatkan Nilai E")
else:
    print("Nilai Anda Tidak Valid")
