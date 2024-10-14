nama = (input("MASUKKAN NAMA ANDA: "))
nim = int(input("MASUKKAN NIM ANDA: "))
nilai_uts = int(input("MASUKKAN NILAI UTS ANDA: "))
nilai_uas = int(input("MASUKKAN NILAI UAS ANDA: "))

nilai_rara_rata = (nilai_uts + nilai_uas)/2
print("NILAI RATA RATA ANDA ADALAH", nilai_rara_rata)

if nilai_rara_rata >= 81 and nilai_rara_rata <= 100 :
    print("Anda mendapatkan nilai A")
elif nilai_rara_rata >= 71 and nilai_rara_rata <= 80 :
    print("Anda mendapatkan nilai B")
elif nilai_rara_rata >= 61 and nilai_rara_rata <= 70 :
    print("Anda mendapatkan niali C")
elif nilai_rara_rata >= 41 and nilai_rara_rata <= 60 :
    print("Anda mendapatkan nilai D")
elif nilai_rara_rata >= 0 and nilai_rara_rata <= 40 :
    print("Anda mendapatkan nilai E")
else :
    print("Nilai tidak terdeteksi")