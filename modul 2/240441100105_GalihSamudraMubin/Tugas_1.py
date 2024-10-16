nama = (input("Masukkan Nama Anda :"))
nim = int(input("Masukkan NIM Anda  :"))
nilai_uts = int(input("Masukkan Nilai UTS Anda :"))
nilai_uas = int(input("Masukkan Nilai UAS Anda :"))
rata_rata = (nilai_uts + nilai_uas) / 2

print("Nilai Rata - Rata Anda :", (rata_rata))
if rata_rata >= 81 <= 100 :
    print("Anda Mendapatkan Nilai A")
elif rata_rata >= 71 <=80 :
    print("Anda Mendapatkan Nilai B")
elif rata_rata >= 61 <= 70 :
    print("Anda Mendapatkan Nilai C")
elif rata_rata >= 41 <= 60 :
    print("Anda Mendapatkan Nilai D")
else :
    print("Anda Mendapatkan Nilai E")