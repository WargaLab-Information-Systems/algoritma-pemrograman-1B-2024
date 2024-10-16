Nama = str(input("Masukkan Nama anda: "))
Nim = int(input("Masukkan Nim anda :"))
Nilai_UTS = int(input("masukkan Nilai UTS anda:"))
Nilai_UAS = int(input("Masukkan Nilai UAS anda:"))

print(f"\nMahasiwa dengan nama : {Nama}")
print(f"Dengan nim : {Nim}")

Nilai_Rata_rata = int((Nilai_UTS + Nilai_UAS)/(2)) 
print(f"Rata rata nilai anda adalah {Nilai_Rata_rata}")

if Nilai_Rata_rata >=81 <=100:
    print("Nilai A")
elif Nilai_Rata_rata <=71 >=80:
    print("Nilai B")
elif Nilai_Rata_rata <=70 >=61:
    print("Nilai C")
elif Nilai_Rata_rata <=60 >=41:
    print("Nilai D")
else:
    print("Nilai E")
