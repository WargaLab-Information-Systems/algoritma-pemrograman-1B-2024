#input NAMA dan NIM
nama = input("masukkan nama :")
nim = input("masukkan nim:")

#input nilai UTS dan UAS
nilai_UTS = int(input("masukkan nilai UTS :"))
nilai_UAS = int(input("masukkan nilai UAS :"))

print("masukkan nama :",nama)
print("nim anda:" , nim)


#menghitung rata-rata nilai
rata_rata = (nilai_UTS + nilai_UAS) / 2
print (f"nilai rata-rata nilai anda : {rata_rata}")
if rata_rata >=81 and rata_rata <=100:
    print("anda mendapatkan nilai A")
elif rata_rata >=71 and rata_rata  <=80:
    print("anda mendapatkan nilai B")
elif rata_rata >=61 and rata_rata <=70:
    print("anda mendapatkan nilai C")
elif rata_rata >=41 and rata_rata <=60:
    print("anda mendapatkan nilai D")
elif rata_rata >=0 and rata_rata <=40:
    print("anda mendapatkan nilai E")
else:
    print("nilai anda tidak memenuhi")
