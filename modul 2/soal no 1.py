nama = str(input("nama saya adalah :"))
nim = str(input("nim saya adalah :"))

nilai_UTS = int(input("masukkan nilai UTS :"))
nilai_UAS = int(input("masukkan nilai UAS :"))

#menghitung rata-rata nilai
rata_rata = (nilai_UTS + nilai_UAS) / 2

print(f"nama saya adalah {nama}")
print(f"NIM saya adalah {nim} ") 
print(f"nilai rata-rata anda:{int(rata_rata)}")

if rata_rata <=100 and rata_rata >=81:
    print("anda mendapatkan nilai A")
elif rata_rata <=80 and rata_rata >=71:
    print("anda mendapatkan nilai B")
elif rata_rata <=70 and rata_rata >=61:
    print("anda mendapatkan nilai C")
elif rata_rata <=60 and rata_rata >=41:
    print("anda mendapatkan nilai D")
elif rata_rata <=40 and rata_rata >=0:
    print("anda mendapatkan nilai E")
else:
    print("nilai tidak lulus")