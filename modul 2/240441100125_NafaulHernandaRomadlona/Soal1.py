nama =str(input("Masukkan Nama "))
nim = int(input("masukkan nim"))
nilai_uas= int(input("masukkan nilai uas"))
nilai_uts= int(input("masukkan nilai uts"))
nilai_rata_rata= (nilai_uas + nilai_uts) / 2
print("Masukkan Nama", nama)
print ("Nim Anda :", nim)
print("Nilai rata-rata anda", nilai_rata_rata)
if nilai_rata_rata >80 :
    print("Anda mendapatkan nilai A")
elif nilai_rata_rata >70 :
    print("Anda mendapatkan nilai B")
elif nilai_rata_rata >60 :
    print("Anda mendapatkan nilai C")
elif nilai_rata_rata >40 :
    print("Anda mendapatkan nilai D")
else :
    print("anda mendapatkan nilai E")