Nama = str(input("Masukkan nama :"))
Nim =int(input("Masukkan nim :"))
Nilai_uts =int(input("Masukkan nilai uts :"))
Nilai_uas =int(input("Masukkan nilai uas :"))

print(f"Mahasiswa dengan nama : {Nama}")
print(f"Dengan Nim : {Nim}")

Nilai_Rata_rata = int((Nilai_uts + Nilai_uas)/(2))
print(f"Rata rata nilai adalah {Nilai_Rata_rata}")

if Nilai_Rata_rata >=81 <=100:
    print("Nilai  A")
elif Nilai_Rata_rata >71 <=80:
    print("Nilai B")
elif Nilai_Rata_rata >=61 <=70:
    print("Nilai C")
elif Nilai_Rata_rata >=41 <=60:
    print("Nilai D") 
else:
    print("Nilai E")
    



