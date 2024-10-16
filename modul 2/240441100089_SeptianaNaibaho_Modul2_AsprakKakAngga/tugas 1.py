Nama = str(input("Masukkan nama :"))
NIM = int(input("Masukkan NIM :"))
Nilai_UTS = int(input("Masukkan nilai UTS :"))
Nilai_UAS = int(input("Masukkan nilai UAS :"))
Rata_rata = (Nilai_UTS+Nilai_UAS)/2
print(f"Rata_rata nilai anda adalah", Rata_rata)
      
if Rata_rata >=81 <=100 :
         print("Nilai A")
elif Rata_rata >=71 <=80 :
         print("Nilai B")
elif Rata_rata >=70 <=61 :
        print("Nilai c")
elif Rata_rata >=41 <=60 :
        print("Nilai D")
else:
        print("Nilai E")









